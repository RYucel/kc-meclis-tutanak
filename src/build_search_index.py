"""Build a serverless prefix-sharded inverted index (`space_static/search_idx/`) for instant keyword search on HF Static Spaces.

Architecture:
  - Tokenizes Turkish speech text (`replace(lower(text), 'ı', 'i')`) into words of length >= 3.
  - Shards postings by 2-letter ASCII-folded prefix (`an.json`, `fo.json`, `te.json`, `uz.json`, ...).
  - Delta-encodes sorted integer doc IDs (`[id0, id1-id0, id2-id1, ...]`) to keep shards tiny over HTTP.
  - Because Turkish is agglutinative (`anayasa` -> `anayasanın`, `anayasaya`, `anayasal`), all inflections
    share the exact same 2-letter prefix file; the browser fetches ONE ~5–80 KB shard and performs
    prefix-union + multi-term intersection in <1 ms before letting DuckDB-WASM read only matching rows!
"""

from __future__ import annotations

import argparse
import json
import re
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import duckdb

HF_DATA = Path("data/hf_dataset/data")
STATIC_SPACE = Path("space_static")
SEARCH_IDX_DIR = STATIC_SPACE / "search_idx"

_TR_FOLD = str.maketrans(
    {
        "ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u",
        "â": "a", "î": "i", "û": "u",
    }
)

# Ultra-frequent Turkish glue words excluded from inverted postings (DuckDB handles them directly if queried)
STOPWORDS = {
    "bir", "bu", "ve", "ile", "için", "icin", "olan", "olarak", "daha", "çok", "cok",
    "gibi", "kadar", "ancak", "fakat", "ama", "lakin", "lâkin", "veya", "yahut",
    "değil", "degil", "ise", "diye", "göre", "gore", "sonra", "önce", "once",
    "üzere", "uzere", "böyle", "boyle", "şöyle", "soyle", "hangi", "her", "hiç", "hic",
    "ben", "biz", "siz", "onu", "bunu", "şunu", "sunu", "bize", "size", "bizim", "sizin",
    "var", "yok", "olan", "oldu", "olur", "olup", "etmek", "eden", "etti", "edilen",
}

_TOKEN_RE = re.compile(r"[a-z0-9çğöşü]+")
MAX_POSTINGS_PER_TOKEN = 15000  # Beyond this, term is too ubiquitous; browser falls back to DuckDB scan


def norm_tr_i(s: str) -> str:
    """Exact equivalent of DuckDB `replace(lower(text), 'ı', 'i')`."""
    return (s or "").replace("İ", "i").replace("I", "i").replace("ı", "i").lower().replace("\u0307", "")


def fold_prefix(tok: str) -> str:
    f = tok.translate(_TR_FOLD)
    f = re.sub(r"[^a-z0-9]", "", f)
    return f[:2] if len(f) >= 2 else (f + "_")[:2]


def delta_encode(sorted_ids: list[int]) -> list[int]:
    if not sorted_ids:
        return []
    out = [sorted_ids[0]]
    prev = sorted_ids[0]
    for x in sorted_ids[1:]:
        out.append(x - prev)
        prev = x
    return out


def delta_decode(deltas: list[int]) -> list[int]:
    out = []
    acc = 0
    for d in deltas:
        acc += d
        out.append(acc)
    return out


def tokenize_text(text: str) -> set[str]:
    norm = norm_tr_i(text)
    return {
        tok
        for tok in _TOKEN_RE.findall(norm)
        if len(tok) >= 3 and tok not in STOPWORDS
    }


def build_inverted_index(
    sp_path: Path = HF_DATA / "speeches.parquet",
    out_dir: Path = SEARCH_IDX_DIR,
) -> dict:
    t0 = time.time()
    if not sp_path.exists():
        raise SystemExit(f"Missing {sp_path}. Run `python src/build_dataset.py` first.")

    if out_dir.exists():
        for old in out_dir.glob("*.json"):
            old.unlink()
    out_dir.mkdir(parents=True, exist_ok=True)

    con = duckdb.connect()
    rows = con.execute(
        f"""
        SELECT speech_id, speaker_name, meclis, donem, SUBSTR(COALESCE(tarih, ''), 1, 4) AS yr, text
        FROM read_parquet('{sp_path}')
        ORDER BY tarih ASC NULLS LAST, turn_index ASC, speech_id ASC
        """
    ).fetchall()
    con.close()

    # Compact lookup tables: int_id -> (speech_id, speaker_idx, term_idx)
    speakers_vocab: list[str] = []
    spk_to_idx: dict[str, int] = {}
    terms_vocab: list[str] = []
    term_to_idx: dict[str, int] = {}

    # For corpora <= 50,000 turns we ship compact speech_id lookup so browser can prune directly by speech_id + speaker_name.
    # For very large corpora (>50,000 turns) we ship term/speaker pruning metadata to keep manifest tiny.
    docs_meta: list[list] = []
    postings: dict[str, list[int]] = defaultdict(list)

    for idx, (sid, spk, meclis, donem, yr, txt) in enumerate(rows):
        s_i = spk_to_idx.get(spk)
        if s_i is None:
            s_i = len(speakers_vocab)
            spk_to_idx[spk] = s_i
            speakers_vocab.append(spk)

        t_key = f"{meclis}_{donem}" if donem is not None else str(meclis)
        t_i = term_to_idx.get(t_key)
        if t_i is None:
            t_i = len(terms_vocab)
            term_to_idx[t_key] = t_i
            terms_vocab.append(t_key)

        docs_meta.append([sid, s_i, t_i, int(yr) if yr.isdigit() else 0])

        for tok in tokenize_text(txt):
            postings[tok].append(idx)

    # Group tokens into 2-letter prefix shards
    shards: dict[str, dict[str, list[int]]] = defaultdict(dict)
    omitted_high_freq: list[str] = []
    for tok, id_list in postings.items():
        if len(id_list) > MAX_POSTINGS_PER_TOKEN:
            omitted_high_freq.append(tok)
            continue
        p2 = fold_prefix(tok)
        shards[p2][tok] = delta_encode(id_list)

    shard_sizes: dict[str, int] = {}
    for p2, tok_map in sorted(shards.items()):
        payload = json.dumps(tok_map, ensure_ascii=False, separators=(",", ":"))
        p_file = out_dir / f"{p2}.json"
        p_file.write_text(payload, encoding="utf-8")
        shard_sizes[p2] = len(payload.encode("utf-8"))

    manifest = {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "doc_count": len(rows),
        "token_count": sum(len(m) for m in shards.values()),
        "shard_count": len(shards),
        "total_shard_bytes": sum(shard_sizes.values()),
        "max_shard_bytes": max(shard_sizes.values(), default=0),
        "stopwords": sorted(STOPWORDS),
        "omitted_high_freq": sorted(omitted_high_freq),
        "shards": sorted(shards.keys()),
        "speakers": speakers_vocab,
        "terms": terms_vocab,
        "docs": docs_meta if len(rows) <= 50000 else [],
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    dt = time.time() - t0
    print(
        f"Built serverless inverted index in {out_dir}/: {manifest['token_count']:,} tokens across "
        f"{manifest['shard_count']} shards ({manifest['total_shard_bytes']/1024:.1f} KB total, "
        f"max shard {manifest['max_shard_bytes']/1024:.1f} KB) in {dt:.2f}s."
    )
    return manifest


def main() -> None:
    ap = argparse.ArgumentParser(description="Build prefix-sharded inverted index for instant DuckDB-WASM search.")
    ap.add_argument("--speeches", type=Path, default=HF_DATA / "speeches.parquet")
    ap.add_argument("--out-dir", type=Path, default=SEARCH_IDX_DIR)
    args = ap.parse_args()
    build_inverted_index(args.speeches, args.out_dir)


if __name__ == "__main__":
    main()
