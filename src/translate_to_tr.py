"""Translate Greek-language parliamentary speech turns into faithful Turkish while keeping original Greek intact.

- Originally Turkish speeches (`language == 'tr'`) are NEVER altered — their verbatim historical text is preserved.
- Originally Greek speeches (`language == 'el'`) that do not yet have a Turkish text are translated via Gemini API
  or a local OpenAI-compatible LLM, cached per `speech_id` in `data/translations/`.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import re
import time
import urllib.request
from pathlib import Path

PARSED_DIR = Path("data/parsed")
TRANS_DIR = Path("data/translations")

_GREEK_RE = re.compile(r"[\u0370-\u03FF\u1F00-\u1FFF]")

TRANSLATE_PROMPT = (
    "Aşağıdaki metin, Kıbrıs Cumhuriyeti Temsilciler Meclisi zabıtlarından tek bir konuşma bloğudur (Yunanca). "
    "Bu konuşmayı Kıbrıs Türk okuyucuların ve araştırmacıların eksiksiz okuyabilmesi için sadık, açık ve doğru Türkçeye çevir.\n"
    "Kurallar:\n"
    "- Hiçbir cümleyi atlama, özetleme veya yorum ekleme.\n"
    "- Anayasa ve meclis terminolojisini doğru kullan (örn. Βουλή των Αντιπροσώπων = Temsilciler Meclisi, "
    "Επιτροπή Επιλογής = Seçme Komitesi, Ανώτατον Συνταγματικόν Δικαστήριον = Yüksek Anayasa Mahkemesi, "
    "απαρτία = toplantı yeter sayısı / nisap, ημερησία διάταξις = gündem).\n"
    "- Özel isimleri ve madde numaralarını doğru koru.\n"
    "- Sadece Türkçe çeviri metnini ver; açıklama veya tırnak ekleme.\n\n"
    "YUNANCA METİN:\n"
)


def needs_translation(rec: dict) -> bool:
    if rec.get("language") == "tr":
        return False
    txt = (rec.get("text") or "").strip()
    if not txt:
        return True
    # Still contains predominantly Greek letters -> not yet translated to Turkish
    greek_cnt = len(_GREEK_RE.findall(txt))
    return greek_cnt > max(15, len(txt) * 0.25)


def translate_gemini(model: str, greek_text: str, retries: int = 5) -> str:
    from google import genai
    from google.genai import types

    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise SystemExit("GEMINI_API_KEY ortam değişkeni tanımlı değil.")
    client = genai.Client(api_key=key)
    delay = 4.0
    for attempt in range(retries):
        try:
            r = client.models.generate_content(
                model=model,
                contents=TRANSLATE_PROMPT + greek_text,
                config=types.GenerateContentConfig(temperature=0.0),
            )
            return (r.text or "").strip()
        except Exception:
            if attempt + 1 >= retries:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 45.0)
    raise RuntimeError("translate_gemini exhausted retries")


def translate_openai(base_url: str, model: str, greek_text: str, retries: int = 4) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "temperature": 0.0,
        "max_tokens": 4096,
        "messages": [{"role": "user", "content": TRANSLATE_PROMPT + greek_text}],
    }
    headers = {"Content-Type": "application/json"}
    if os.environ.get("OPENAI_API_KEY"):
        headers["Authorization"] = f"Bearer {os.environ['OPENAI_API_KEY']}"
    body = json.dumps(payload).encode("utf-8")
    delay = 2.0
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=body, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return (data["choices"][0]["message"].get("content") or "").strip()
        except Exception:
            if attempt + 1 >= retries:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 30.0)
    raise RuntimeError("translate_openai exhausted retries")


def main() -> None:
    ap = argparse.ArgumentParser(description="Translate untranslated Greek speech turns to Turkish (resumable).")
    ap.add_argument("--engine", choices=("gemini", "openai"), default="gemini")
    ap.add_argument("--model", default="gemini-2.5-flash")
    ap.add_argument("--base-url", default="http://localhost:8000/v1")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0, help="Optional cap on number of speeches to translate")
    args = ap.parse_args()

    sp_path = PARSED_DIR / "speeches.jsonl"
    if not sp_path.exists():
        raise SystemExit("Run `python src/parse_speakers.py` first.")

    TRANS_DIR.mkdir(parents=True, exist_ok=True)
    speeches = [json.loads(l) for l in sp_path.read_text(encoding="utf-8").splitlines() if l.strip()]

    todo = [s for s in speeches if needs_translation(s)]
    if args.limit > 0:
        todo = todo[: args.limit]
    print(f"Total speeches: {len(speeches)} | Need Greek->Turkish translation: {len(todo)}")

    def run_one(s: dict) -> tuple[str, str]:
        sid = s["speech_id"]
        cache = TRANS_DIR / f"{sid}.txt"
        if cache.exists():
            return sid, cache.read_text(encoding="utf-8").strip()
        src_text = s.get("text_original") or s.get("text") or ""
        if args.engine == "gemini":
            tr = translate_gemini(args.model, src_text)
        else:
            tr = translate_openai(args.base_url, args.model, src_text)
        cache.write_text(tr + "\n", encoding="utf-8")
        return sid, tr

    translated: dict[str, str] = {}
    if todo:
        with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
            for sid, tr in ex.map(run_one, todo):
                translated[sid] = tr

    updated = 0
    for s in speeches:
        if s["speech_id"] in translated and translated[s["speech_id"]]:
            s["text"] = translated[s["speech_id"]]
            s["char_count"] = len(s["text"])
            s["word_count"] = len(s["text"].split())
            s["translated_to_tr"] = True
            updated += 1

    sp_path.write_text("\n".join(json.dumps(s, ensure_ascii=False) for s in speeches) + "\n", encoding="utf-8")
    print(f"Updated {updated} speech turns with Turkish translations in {sp_path}")


if __name__ == "__main__":
    main()
