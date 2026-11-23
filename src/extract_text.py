"""Extract text from Republic of Cyprus parliamentary PDFs with garbled-OCR detection and VLM cache loading.

Key features tailored to parliament.cy historical PDFs:
  1. Detects Adobe Acrobat's English-only OCR on Greek pages (e.g. 'TnOTPrEION', 'npOE6POI')
     and marks those pages as `pdf_needs_ocr` instead of polluting the corpus.
  2. Handles malformed PDF page-tree cycles (e.g. page 719 of 1960-1961 PDF) gracefully per page.
  3. Merges cached VLM / manual page transcriptions from `data/reocr/<volume_key>/pNNNN.txt`
     (and optional Turkish translations `pNNNN.tr.txt`) so runs are fully resumable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import pymupdf

MANIFEST_PATH = Path("data/manifest.jsonl")
RAW_DIR = Path("data/raw")
EXTRACTED_DIR = Path("data/extracted")
REOCR_DIR = Path("data/reocr")

_GREEK_RE = re.compile(r"[\u0370-\u03FF\u1F00-\u1FFF]")
_LATIN_RE = re.compile(r"[A-Za-zÇĞİÖŞÜçğıöşü]")
_TR_WORD_RE = re.compile(
    r"\b(?:Sayın|Meclis|Cumhuriyet|Anayasa|Türk|Üye|Teklif|Kabul|Toplantı|Gündem|Başkan|Reis|Kâtip|Kanun|Madde|Bakan)\b",
    re.I,
)
_GARBLED_GREEK_RE = re.compile(
    r"(?:npOE|TnOT|XAAIT|rPAMM|fPAMM|O\},\w|1tp|6\.\.\s|t\.\s*T|Jtp|ci\.;)",
)


def volume_key(volume_id: str) -> str:
    return hashlib.sha1(volume_id.encode("utf-8")).hexdigest()[:16]


def classify_page_text(text: str) -> str:
    """Classify an extracted PDF page's embedded text layer:
    - 'empty': no usable text (scanned image)
    - 'garbled_ocr': noisy English-OCR-on-Greek layer (must be re-OCR'd)
    - 'digital_el': clean Greek text
    - 'digital_tr': clean Turkish text
    - 'digital_bilingual': clean Greek + Turkish text
    """
    s = (text or "").strip()
    if len(s) < 30:
        return "empty"

    greek_cnt = len(_GREEK_RE.findall(s))
    latin_cnt = len(_LATIN_RE.findall(s))
    tr_hits = len(_TR_WORD_RE.findall(s))
    non_space = max(1, len(re.sub(r"\s+", "", s)))
    alpha_ratio = (greek_cnt + latin_cnt) / non_space
    weird_punct = len(re.findall(r"[~^`|\\{}\[\]<>¬§±£¥¤]", s))

    # Adobe Acrobat English-OCR-on-Greek produces heavy punctuation/digits mixed inside Latin tokens
    if _GARBLED_GREEK_RE.search(s) or (weird_punct / non_space > 0.03) or alpha_ratio < 0.52:
        if tr_hits < 3 and greek_cnt < 40:
            return "garbled_ocr"
    # Mixed case mid-word noise like "TnOTPrEION" or "npOE6POI"
    noisy_tokens = len(re.findall(r"[a-z][A-Z]|[A-Za-z]\d[A-Za-z]", s))
    words = max(1, len(s.split()))
    if noisy_tokens / words > 0.08 and greek_cnt < 40 and tr_hits < 4:
        return "garbled_ocr"

    if greek_cnt >= 40 and tr_hits >= 2:
        return "digital_bilingual"
    if greek_cnt >= 40:
        return "digital_el"
    if tr_hits >= 2 or (latin_cnt >= 60 and alpha_ratio >= 0.72):
        return "digital_tr"
    return "garbled_ocr"


def load_reocr_page(reocr_root: Path, vol_id: str, page_num: int) -> tuple[str | None, str | None]:
    """Load cached original page text (pNNNN.txt) and optional Turkish text (pNNNN.tr.txt)."""
    vdir_by_id = reocr_root / vol_id
    vdir_by_hash = reocr_root / volume_key(vol_id)
    for base in (vdir_by_id, vdir_by_hash):
        p_orig = base / f"p{page_num:04d}.txt"
        p_tr = base / f"p{page_num:04d}.tr.txt"
        if p_orig.exists() or p_tr.exists():
            orig = p_orig.read_text(encoding="utf-8").strip() if p_orig.exists() else None
            tr = p_tr.read_text(encoding="utf-8").strip() if p_tr.exists() else None
            return orig, tr
    return None, None


def extract_volume(
    entry: dict,
    raw_dir: Path = RAW_DIR,
    reocr_dir: Path = REOCR_DIR,
    max_pages: int | None = None,
    only_cached: bool = False,
) -> dict:
    pdf_path = raw_dir / entry["local_filename"]
    vol_id = entry["volume_id"]
    pages_out: list[dict] = []
    counts = {
        "reocr_bilingual": 0,
        "reocr_orig_only": 0,
        "digital": 0,
        "needs_ocr": 0,
        "pdf_error": 0,
    }

    total_pages = 0
    doc = None
    if pdf_path.exists():
        doc = pymupdf.open(str(pdf_path))
        total_pages = len(doc)

    # Determine page range
    if only_cached:
        cached_nums = set()
        for base in (reocr_dir / vol_id, reocr_dir / volume_key(vol_id)):
            if base.exists():
                for f in base.glob("p*.txt"):
                    m = re.match(r"p(\d{4})(?:\.tr)?\.txt$", f.name)
                    if m:
                        cached_nums.add(int(m.group(1)))
        page_indices = sorted(cached_nums)
        if not total_pages and page_indices:
            total_pages = max(page_indices)
    else:
        limit = min(total_pages, max_pages) if max_pages else total_pages
        page_indices = list(range(1, limit + 1))

    for pno in page_indices:
        orig_cached, tr_cached = load_reocr_page(reocr_dir, vol_id, pno)
        if orig_cached or tr_cached:
            src = "reocr_vlm_tr" if tr_cached else "reocr_vlm"
            if tr_cached:
                counts["reocr_bilingual"] += 1
            else:
                counts["reocr_orig_only"] += 1
            pages_out.append(
                {
                    "page": pno,
                    "text_source": src,
                    "text_original": orig_cached or tr_cached or "",
                    "text_tr": tr_cached,
                    "status": "ok",
                }
            )
            continue

        if doc is None:
            counts["needs_ocr"] += 1
            continue

        try:
            raw_text = doc[pno - 1].get_text("text") or ""
            cls = classify_page_text(raw_text)
            if cls.startswith("digital_"):
                counts["digital"] += 1
                pages_out.append(
                    {
                        "page": pno,
                        "text_source": f"pdf_{cls}",
                        "text_original": raw_text.strip(),
                        "text_tr": raw_text.strip() if cls == "digital_tr" else None,
                        "status": "ok",
                    }
                )
            else:
                counts["needs_ocr"] += 1
                pages_out.append(
                    {
                        "page": pno,
                        "text_source": "pdf_needs_ocr",
                        "text_original": "",
                        "text_tr": None,
                        "status": cls,
                    }
                )
        except Exception as e:
            counts["pdf_error"] += 1
            pages_out.append(
                {
                    "page": pno,
                    "text_source": "pdf_error",
                    "text_original": "",
                    "text_tr": None,
                    "status": f"error: {e}",
                }
            )

    if doc is not None:
        doc.close()

    return {
        "volume_id": vol_id,
        "meclis": entry.get("meclis", "KC"),
        "donem": entry.get("donem"),
        "yasama_yili": entry.get("yasama_yili"),
        "date_start": entry.get("date_start"),
        "date_end": entry.get("date_end"),
        "source_file": entry["source_file"],
        "source_url": entry["source_url"],
        "local_filename": entry["local_filename"],
        "total_pages": total_pages,
        "extracted_pages": len(pages_out),
        "counts": counts,
        "pages": pages_out,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Extract pages from parliament.cy PDFs and merge VLM OCR caches.")
    ap.add_argument("--reocr-dir", type=Path, default=REOCR_DIR, help="Directory holding pNNNN.txt / pNNNN.tr.txt caches")
    ap.add_argument("--max-pages", type=int, default=None, help="Optional cap on scanned pages per volume")
    ap.add_argument("--only-cached", action="store_true", help="Only emit pages that already have re-OCR cache files")
    args = ap.parse_args()

    if not MANIFEST_PATH.exists():
        raise SystemExit("Run `python src/crawl_manifest.py` first.")

    EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)
    entries = [json.loads(l) for l in MANIFEST_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    for entry in entries:
        res = extract_volume(entry, reocr_dir=args.reocr_dir, max_pages=args.max_pages, only_cached=args.only_cached)
        out_path = EXTRACTED_DIR / f"{entry['volume_id']}.json"
        out_path.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        print(
            f"[EXTRACTED] {entry['volume_id']} | total={res['total_pages']} | "
            f"counts={res['counts']} -> {out_path}"
        )


if __name__ == "__main__":
    main()
