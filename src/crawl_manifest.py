"""Manage the catalog (manifest) of Republic of Cyprus House of Representatives (parliament.cy) minutes PDFs.

Because parliament.cy HTML listing pages sit behind a Cloudflare browser challenge while direct
/images/media/redirectfile/*.pdf links download cleanly, this module supports:
  1. Seed manifest with the initial 1960-1961 Term 1 Session A PDF.
  2. Adding individual PDF URLs via --add-url.
  3. Importing a text file of PDF URLs via --from-urls-file.
  4. Parsing a browser-saved parliament.cy minutes HTML page via --from-html.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urljoin

from bs4 import BeautifulSoup

DATA_DIR = Path("data")
MANIFEST_PATH = DATA_DIR / "manifest.jsonl"
SUMMARY_PATH = DATA_DIR / "manifest_summary.json"

DEFAULT_SEED_URLS = [
    "https://www.parliament.cy/images/media/redirectfile/A%20Vouleftiki%20periodos%20-Synodos%20A%20-%2016.08.1960-07.081961.pdf",
]

# Greek / Latin parliamentary term prefixes used on parliament.cy
TERM_PREFIX_MAP = {
    "A": 1, "Α": 1, "I": 1, "1": 1,
    "B": 2, "Β": 2, "II": 2, "2": 2,
    "G": 3, "Γ": 3, "C": 3, "III": 3, "3": 3,
    "D": 4, "Δ": 4, "IV": 4, "4": 4,
    "E": 5, "Ε": 5, "V": 5, "5": 5,
    "ST": 6, "ΣΤ": 6, "VI": 6, "6": 6,
    "Z": 7, "Ζ": 7, "VII": 7, "7": 7,
    "H": 8, "Η": 8, "VIII": 8, "8": 8,
    "TH": 9, "Θ": 9, "IX": 9, "9": 9,
    "I": 10, "Ι": 10, "X": 10, "10": 10,
    "IA": 11, "ΙΑ": 11, "XI": 11, "11": 11,
    "IB": 12, "ΙΒ": 12, "XII": 12, "12": 12,
    "IG": 13, "ΙΓ": 13, "XIII": 13, "13": 13,
}

SESSION_MAP = {
    "A": 1, "Α": 1, "1": 1,
    "B": 2, "Β": 2, "2": 2,
    "G": 3, "Γ": 3, "C": 3, "3": 3,
    "D": 4, "Δ": 4, "4": 4,
    "E": 5, "Ε": 5, "5": 5,
    "ST": 6, "ΣΤ": 6, "6": 6,
}


def parse_parliament_cy_filename(url: str) -> dict:
    """Infer parliamentary term (donem), legislative year (yasama_yili), date range, and safe filename."""
    decoded = unquote(url.split("?")[0].rstrip("/").split("/")[-1])
    stem = re.sub(r"\.pdf$", "", decoded, flags=re.I)

    donem = None
    m_term = re.search(
        r"(?:^|[\s_-])(IB|IA|IG|ST|TH|[ABGDEZHI]|[ΑΒΓΔΕΖΗΘΙ]|1[0-3]|[1-9])['΄’]?\s*(?:Vouleftiki|Βουλευτικ)",
        stem,
        re.I,
    )
    if m_term:
        tok = m_term.group(1).upper()
        # Disambiguate 'I' (10th term vs Roman I) using year if present
        donem = TERM_PREFIX_MAP.get(tok)

    yasama_yili = None
    m_syn = re.search(
        r"(?:Synodos|Σ[υύ]νοδος)\s*['΄’]?\s*(ST|[ABGDE]|[ΑΒΓΔΕ]|[1-6])",
        stem,
        re.I,
    )
    if m_syn:
        yasama_yili = SESSION_MAP.get(m_syn.group(1).upper())

    # Extract dates like 16.08.1960 and malformed 07.081961 -> 1961-08-07
    dates: list[str] = []
    for m_d in re.finditer(r"(\d{1,2})[.\-/](\d{1,2})[.\-/]?((?:19|20)\d{2})", stem):
        d, mo, y = int(m_d.group(1)), int(m_d.group(2)), int(m_d.group(3))
        if 1 <= d <= 31 and 1 <= mo <= 12:
            dates.append(f"{y:04d}-{mo:02d}-{d:02d}")

    date_start = dates[0] if dates else None
    date_end = dates[1] if len(dates) >= 2 else date_start

    # Infer donem from start year if missing or ambiguous
    if date_start:
        yr = int(date_start[:4])
        if donem is None:
            for lo, hi, num in [
                (1960, 1969, 1), (1970, 1975, 2), (1976, 1980, 3),
                (1981, 1984, 4), (1985, 1990, 5), (1991, 1995, 6),
                (1996, 2000, 7), (2001, 2005, 8), (2006, 2010, 9),
                (2011, 2015, 10), (2016, 2020, 11), (2021, 2026, 12),
            ]:
                if lo <= yr <= hi:
                    donem = num
                    break

    safe_parts = []
    if m_term:
        safe_parts.append(f"{m_term.group(1).upper()}_Vouleftiki_periodos")
    elif donem:
        safe_parts.append(f"Donem_{donem}")
    if m_syn:
        safe_parts.append(f"Synodos_{m_syn.group(1).upper()}")
    if date_start and date_end and date_start != date_end:
        safe_parts.append(f"{date_start}_{date_end}")
    elif date_start:
        safe_parts.append(date_start)

    if safe_parts:
        local_name = "_".join(safe_parts) + ".pdf"
    else:
        slug = re.sub(r"[^A-Za-z0-9._-]+", "_", stem).strip("_") or hashlib.sha1(url.encode()).hexdigest()[:12]
        local_name = f"{slug}.pdf"

    volume_id = f"KC_D{donem or 0}_S{yasama_yili or 0}_{date_start or hashlib.sha1(url.encode()).hexdigest()[:8]}"

    return {
        "volume_id": volume_id,
        "meclis": "KC",
        "donem": donem,
        "yasama_yili": yasama_yili,
        "date_start": date_start,
        "date_end": date_end,
        "source_file": decoded,
        "local_filename": local_name,
        "source_url": url.strip(),
        "ext": ".pdf",
    }


def load_manifest(path: Path = MANIFEST_PATH) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def save_manifest(entries: list[dict], path: Path = MANIFEST_PATH, summary_path: Path = SUMMARY_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Deduplicate by source_url preserving deterministic sort
    by_url = {e["source_url"]: e for e in entries}
    ordered = sorted(
        by_url.values(),
        key=lambda e: (e.get("donem") or 999, e.get("yasama_yili") or 999, e.get("date_start") or "", e["source_url"]),
    )
    path.write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in ordered) + "\n", encoding="utf-8")

    by_donem: dict[str, int] = {}
    for e in ordered:
        k = f"KC:{e['donem']}" if e.get("donem") else "KC"
        by_donem[k] = by_donem.get(k, 0) + 1
    summary = {
        "total_volumes": len(ordered),
        "by_term": by_donem,
        "min_date": min((e["date_start"] for e in ordered if e.get("date_start")), default=None),
        "max_date": max((e["date_end"] for e in ordered if e.get("date_end")), default=None),
    }
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


def extract_urls_from_html(html_path: Path, base_url: str = "https://www.parliament.cy/") -> list[str]:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8", errors="replace"), "html.parser")
    urls: list[str] = []
    seen = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if ".pdf" not in href.lower() and "redirectfile" not in href.lower():
            continue
        full = urljoin(base_url, href)
        if full not in seen:
            seen.add(full)
            urls.append(full)
    return urls


def main() -> None:
    ap = argparse.ArgumentParser(description="Build or update parliament.cy minutes manifest.")
    ap.add_argument("--add-url", action="append", default=[], help="Add one or more direct parliament.cy PDF URLs")
    ap.add_argument("--from-urls-file", type=Path, help="Import PDF URLs (one per line)")
    ap.add_argument("--from-html", type=Path, help="Import PDF URLs from a browser-saved parliament.cy HTML page")
    ap.add_argument("--reset", action="store_true", help="Rebuild manifest from scratch instead of merging")
    args = ap.parse_args()

    entries = [] if args.reset else load_manifest()
    urls: list[str] = []
    if not entries and not args.add_url and not args.from_urls_file and not args.from_html:
        urls.extend(DEFAULT_SEED_URLS)
    urls.extend(args.add_url)
    if args.from_urls_file:
        urls.extend(
            line.strip()
            for line in args.from_urls_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        )
    if args.from_html:
        urls.extend(extract_urls_from_html(args.from_html))

    for url in urls:
        entries.append(parse_parliament_cy_filename(url))

    save_manifest(entries)
    final_entries = load_manifest()
    print(f"Manifest updated: {len(final_entries)} volume(s) -> {MANIFEST_PATH}")
    for e in final_entries:
        print(f"  - {e['volume_id']} | Dönem {e['donem']} Yıl {e['yasama_yili']} | {e['date_start']}..{e['date_end']} | {e['local_filename']}")


if __name__ == "__main__":
    main()
