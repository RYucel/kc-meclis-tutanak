"""Resumable downloader for parliament.cy minutes PDFs listed in data/manifest.jsonl."""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path

MANIFEST_PATH = Path("data/manifest.jsonl")
RAW_DIR = Path("data/raw")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def download_volume(entry: dict, raw_dir: Path = RAW_DIR, force: bool = False) -> Path:
    raw_dir.mkdir(parents=True, exist_ok=True)
    dest = raw_dir / entry["local_filename"]
    if dest.exists() and dest.stat().st_size > 1024 and not force:
        print(f"[SKIP] {dest.name} ({dest.stat().st_size / (1024*1024):.1f} MB) already present")
        return dest

    url = entry["source_url"]
    tmp = dest.with_suffix(".pdf.part")
    print(f"[GET]  {url} -> {dest.name}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=180) as resp, tmp.open("wb") as out:
        total = 0
        while True:
            buf = resp.read(1024 * 1024)
            if not buf:
                break
            out.write(buf)
            total += len(buf)
    tmp.replace(dest)
    print(f"[OK]   {dest.name} ({total / (1024*1024):.1f} MB)")
    return dest


def main() -> None:
    ap = argparse.ArgumentParser(description="Download PDFs listed in data/manifest.jsonl")
    ap.add_argument("--force", action="store_true", help="Re-download existing files")
    ap.add_argument("--checksum", action="store_true", help="Compute and record SHA-256 in manifest")
    args = ap.parse_args()

    if not MANIFEST_PATH.exists():
        raise SystemExit("Run `python src/crawl_manifest.py` first.")

    entries = [json.loads(l) for l in MANIFEST_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    for e in entries:
        dest = download_volume(e, force=args.force)
        e["local_path"] = str(dest)
        e["size_bytes"] = dest.stat().st_size
        if args.checksum:
            e["sha256"] = sha256_file(dest)

    MANIFEST_PATH.write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in entries) + "\n", encoding="utf-8")
    print(f"All {len(entries)} volume(s) ready in {RAW_DIR}/")


if __name__ == "__main__":
    main()
