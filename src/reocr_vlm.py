"""Resumable two-column bilingual OCR (polytonic Greek + Turkish) & optional Turkish translation for parliament.cy PDFs.

Mirrors kktc-meclis-tutanak/src/reocr_vlm.py while handling:
  - Two-column printed minutes (reads left column top-to-bottom, then right column top-to-bottom).
  - Polytonic Greek (Katharevousa) + 1960s Turkish on the same page.
  - Malformed PDF pages (falls back to `pdftoppm` when PyMuPDF hits a page-tree cycle).
  - Three engines:
      1. Gemini Vision API (`--engine gemini`, default, requires GEMINI_API_KEY)
      2. Local OpenAI-compatible VLM (`--engine openai --base-url http://localhost:8000/v1`)
      3. Local two-column Tesseract (`--engine tesseract`, requires `tesseract-ocr-ell` + `tesseract-ocr-tur`)

Every page is cached under `data/reocr/<volume_id>/pNNNN.txt` (verbatim original) and optionally
`pNNNN.tr.txt` (faithful Turkish version), so interrupted runs resume with zero duplicate work.
"""

from __future__ import annotations

import argparse
import base64
import concurrent.futures as cf
import io
import json
import os
import subprocess
import tempfile
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

import pymupdf
from PIL import Image

MANIFEST_PATH = Path("data/manifest.jsonl")
RAW_DIR = Path("data/raw")
REOCR_DIR = Path("data/reocr")
_lock = threading.Lock()

PROMPT_ORIG = (
    "Bu görüntü, Kıbrıs Cumhuriyeti Temsilciler Meclisi tutanaklarından taranmış iki sütunlu tek bir sayfadır. "
    "Sayfadaki metni basıldığı orijinal dilinde (Yunanca kısımları aynen Yunanca, Türkçe kısımları aynen Türkçe) harfi harfine yaz.\n"
    "Kurallar:\n"
    "- İki sütunlu sayfalarda ÖNCE sol sütunu yukarıdan aşağıya, SONRA sağ sütunu yukarıdan aşağıya oku. Sütunları asla karıştırma.\n"
    "- Oturum başlıklarını (ör. 'ΣΥΝΕΔΡΙΑΣΙΣ ΤΗΣ ...', '29 AĞUSTOS 1960 TARİHLİ TOPLANTI') ve konuşmacı başlıklarını "
    "(ör. 'ΠΡΟΕΔΡΟΣ :', 'Β. ΛΥΣΣΑΡΙΔΗΣ :', 'H. A. RIZA :', 'Ü. SÜLEYMAN :') yeni satırda aynen koru.\n"
    "- Hiçbir kelimeyi özetleme, yorumlama veya düzeltme. Eski imlayı koru.\n"
    "- Okunamayan yerleri [okunamadı] yaz; tahmin etme.\n"
    "- Sadece düz metni ver; markdown, kod bloğu veya açıklama ekleme."
)

PROMPT_TR = (
    "Bu görüntü, Kıbrıs Cumhuriyeti Temsilciler Meclisi tutanaklarından taranmış iki sütunlu tek bir sayfadır. "
    "Kıbrıs Türk okuyucuların ve araştırmacıların eksiksiz okuyabilmesi için sayfanın TAMAMINI doğru ve sadık TÜRKÇE olarak yaz.\n"
    "Kurallar:\n"
    "- İki sütunlu sayfalarda ÖNCE sol sütunu yukarıdan aşağıya, SONRA sağ sütunu yukarıdan aşağıya oku.\n"
    "- Zaten Türkçe olan konuşmaları ve bölümleri KELİMESİ KELİMESİNE aynen koru (özetleme veya değiştirme).\n"
    "- Yunanca (Katharevousa) konuşmaları hukuki ve meclis terminolojisine sadık kalarak tam ve eksiksiz Türkçeye çevir.\n"
    "- Konuşmacı başlıklarını yeni satırda 'KONUŞMACI ADI :' biçiminde koru (ör. 'BAŞKAN :', 'V. LİSSARİDİS :', 'H. A. RIZA :').\n"
    "- Oturum tarihini, saatini ve gündem maddelerini eksiksiz yaz.\n"
    "- Sadece düz metni ver; markdown, kod bloğu veya açıklama ekleme."
)


def render_page_png(pdf_path: Path, page_num: int, dpi: int = 180) -> bytes:
    """Render 1-indexed page to grayscale PNG, falling back to pdftoppm if PyMuPDF hits a page-tree error."""
    try:
        with pymupdf.open(str(pdf_path)) as doc:
            pix = doc[page_num - 1].get_pixmap(dpi=dpi, colorspace="gray")
            return pix.tobytes("png")
    except Exception:
        with tempfile.TemporaryDirectory() as td:
            prefix = Path(td) / "pg"
            subprocess.run(
                ["pdftoppm", "-png", "-gray", "-r", str(dpi), "-f", str(page_num), "-l", str(page_num), str(pdf_path), str(prefix)],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
            )
            pngs = sorted(Path(td).glob("pg*.png"))
            if not pngs:
                raise RuntimeError(f"pdftoppm failed to render page {page_num}")
            return pngs[0].read_bytes()


def transcribe_gemini(model: str, png: bytes, prompt: str, retries: int = 6) -> tuple[str, dict]:
    from google import genai
    from google.genai import types

    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise SystemExit("GEMINI_API_KEY ortam değişkeni tanımlı değil.")
    client = genai.Client(api_key=key)

    delay = 5.0
    for attempt in range(retries):
        try:
            r = client.models.generate_content(
                model=model,
                contents=[types.Part.from_bytes(data=png, mime_type="image/png"), prompt],
                config=types.GenerateContentConfig(temperature=0.0),
            )
            u = r.usage_metadata
            usage = {
                "in": getattr(u, "prompt_token_count", 0) or 0,
                "out": getattr(u, "candidates_token_count", 0) or 0,
            }
            text = (r.text or "").strip()
            if text.startswith("```"):
                text = text.strip("`").split("\n", 1)[-1].strip()
            return text, usage
        except Exception as e:
            if attempt + 1 >= retries:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 60.0)
    raise RuntimeError("transcribe_gemini exhausted retries")


def transcribe_openai(base_url: str, model: str, png: bytes, prompt: str, retries: int = 4) -> tuple[str, dict]:
    url = base_url.rstrip("/") + "/chat/completions"
    b64 = base64.b64encode(png).decode("ascii")
    payload = {
        "model": model,
        "temperature": 0.0,
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
                    {"type": "text", "text": prompt},
                ],
            }
        ],
    }
    headers = {"Content-Type": "application/json"}
    if os.environ.get("OPENAI_API_KEY"):
        headers["Authorization"] = f"Bearer {os.environ['OPENAI_API_KEY']}"
    body = json.dumps(payload).encode("utf-8")

    delay = 2.0
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=body, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            text = (data["choices"][0]["message"].get("content") or "").strip()
            if text.startswith("```"):
                text = text.strip("`").split("\n", 1)[-1].strip()
            u = data.get("usage") or {}
            return text, {"in": int(u.get("prompt_tokens", 0) or 0), "out": int(u.get("completion_tokens", 0) or 0)}
        except Exception:
            if attempt + 1 >= retries:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 30.0)
    raise RuntimeError("transcribe_openai exhausted retries")


def transcribe_tesseract_two_column(png: bytes, lang: str = "ell+tur") -> tuple[str, dict]:
    """Split a two-column minutes page cleanly down the gutter and OCR left then right."""
    import pytesseract

    img = Image.open(io.BytesIO(png))
    w, h = img.size
    # Top header banner (14%) + left column + right column
    header = img.crop((0, 0, w, int(h * 0.14)))
    left = img.crop((0, int(h * 0.13), int(w * 0.51), h))
    right = img.crop((int(w * 0.49), int(h * 0.13), w, h))
    parts = [
        pytesseract.image_to_string(crop, lang=lang, config="--psm 6").strip()
        for crop in (header, left, right)
    ]
    text = "\n\n".join(p for p in parts if p)
    return text, {"in": 0, "out": len(text)}


def main() -> None:
    ap = argparse.ArgumentParser(description="Resumable two-column bilingual OCR for parliament.cy PDFs.")
    ap.add_argument("--volume-id", help="Specific volume_id from data/manifest.jsonl (default: first)")
    ap.add_argument("--from-page", type=int, default=3, help="1-indexed start page")
    ap.add_argument("--to-page", type=int, default=16, help="1-indexed end page (inclusive)")
    ap.add_argument("--engine", choices=("gemini", "openai", "tesseract"), default="gemini")
    ap.add_argument("--model", default="gemini-2.5-flash")
    ap.add_argument("--base-url", default="http://localhost:8000/v1", help="OpenAI-compatible VLM endpoint")
    ap.add_argument("--dpi", type=int, default=180)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--with-turkish", action="store_true", help="Also generate pNNNN.tr.txt faithful Turkish page")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    entries = [json.loads(l) for l in MANIFEST_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    entry = next((e for e in entries if e["volume_id"] == args.volume_id), entries[0])
    pdf_path = RAW_DIR / entry["local_filename"]
    if not pdf_path.exists():
        raise SystemExit(f"Missing PDF: {pdf_path}. Run `python src/download_files.py` first.")

    out_dir = REOCR_DIR / entry["volume_id"]
    out_dir.mkdir(parents=True, exist_ok=True)
    usage_log = out_dir / "usage.jsonl"

    def process_page(pno: int) -> str:
        p_orig = out_dir / f"p{pno:04d}.txt"
        p_tr = out_dir / f"p{pno:04d}.tr.txt"
        need_orig = args.overwrite or not p_orig.exists()
        need_tr = args.with_turkish and (args.overwrite or not p_tr.exists())
        if not need_orig and not need_tr:
            return f"p{pno:04d}: cached"

        png = render_page_png(pdf_path, pno, dpi=args.dpi)
        log_rec = {"page": pno, "engine": args.engine, "model": args.model}

        if need_orig:
            if args.engine == "gemini":
                txt, u = transcribe_gemini(args.model, png, PROMPT_ORIG)
            elif args.engine == "openai":
                txt, u = transcribe_openai(args.base_url, args.model, png, PROMPT_ORIG)
            else:
                txt, u = transcribe_tesseract_two_column(png)
            p_orig.write_text(txt + "\n", encoding="utf-8")
            log_rec["orig_usage"] = u

        if need_tr and args.engine != "tesseract":
            if args.engine == "gemini":
                tr_txt, u2 = transcribe_gemini(args.model, png, PROMPT_TR)
            else:
                tr_txt, u2 = transcribe_openai(args.base_url, args.model, png, PROMPT_TR)
            p_tr.write_text(tr_txt + "\n", encoding="utf-8")
            log_rec["tr_usage"] = u2

        with _lock:
            with usage_log.open("a", encoding="utf-8") as f:
                f.write(json.dumps(log_rec, ensure_ascii=False) + "\n")
        return f"p{pno:04d}: ok"

    pages = list(range(args.from_page, args.to_page + 1))
    print(f"Running {args.engine} ({args.model}) on {entry['volume_id']} pages {args.from_page}..{args.to_page}")
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        for res in ex.map(process_page, pages):
            print(" ", res)


if __name__ == "__main__":
    main()
