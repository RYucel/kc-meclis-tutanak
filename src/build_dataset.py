"""Canonicalize speaker names, export Hugging Face Parquet dataset + Dataset Card, and build SQLite FTS5 index."""

from __future__ import annotations

import argparse
import json
import sqlite3
import time
from collections import Counter, defaultdict
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from speaker_resolution import load_rosters, resolve_records

PARSED_DIR = Path("data/parsed")
HF_DIR = Path("data/hf_dataset")
HF_DATA_DIR = HF_DIR / "data"
DB_PATH = Path("data/search.db")


def write_parquet(rows: list[dict], path: Path) -> tuple[int, int]:
    path.parent.mkdir(parents=True, exist_ok=True)
    table = pa.Table.from_pylist(rows)
    pq.write_table(table, path, compression="zstd")
    return len(rows), path.stat().st_size


def build_sqlite_fts(speeches: list[dict], speakers_rows: list[dict], db_path: Path = DB_PATH) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    con = sqlite3.connect(str(db_path))
    cur = con.cursor()
    cur.executescript(
        """
        CREATE TABLE speeches (
            speech_id TEXT PRIMARY KEY,
            doc_id TEXT,
            meclis TEXT,
            donem INTEGER,
            yasama_yili INTEGER,
            birlesim INTEGER,
            oturum INTEGER,
            tarih TEXT,
            turn_index INTEGER,
            speaker_name TEXT,
            speaker_name_parsed TEXT,
            speaker_raw TEXT,
            speaker_role TEXT,
            speaker_title TEXT,
            constituency TEXT,
            community TEXT,
            language TEXT,
            page_start INTEGER,
            page_end INTEGER,
            text TEXT,
            text_original TEXT,
            word_count INTEGER,
            source_file TEXT,
            source_url TEXT
        );
        CREATE VIRTUAL TABLE speeches_fts USING fts5(
            speech_id UNINDEXED,
            speaker_name,
            text,
            text_original,
            tokenize='unicode61'
        );
        CREATE TABLE speakers (
            speaker_name TEXT PRIMARY KEY,
            speech_count INTEGER,
            word_count INTEGER,
            doc_count INTEGER,
            first_date TEXT,
            last_date TEXT,
            community TEXT
        );
        """
    )
    cur.executemany(
        """
        INSERT INTO speeches VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        [
            (
                s["speech_id"], s["doc_id"], s["meclis"], s["donem"], s["yasama_yili"],
                s["birlesim"], s["oturum"], s["tarih"], s["turn_index"],
                s["speaker_name"], s["speaker_name_parsed"], s["speaker_raw"],
                s["speaker_role"], s["speaker_title"], s["constituency"],
                s.get("community", ""), s.get("language", "tr"),
                s.get("page_start"), s.get("page_end"),
                s["text"], s.get("text_original", ""), s["word_count"],
                s["source_file"], s["source_url"],
            )
            for s in speeches
        ],
    )
    cur.executemany(
        "INSERT INTO speeches_fts VALUES (?,?,?,?)",
        [(s["speech_id"], s["speaker_name"], s["text"], s.get("text_original", "")) for s in speeches],
    )
    cur.executemany(
        "INSERT INTO speakers VALUES (?,?,?,?,?,?,?)",
        [
            (
                r["speaker_name"], r["speech_count"], r["word_count"], r["doc_count"],
                r["first_date"], r["last_date"], r.get("community", ""),
            )
            for r in speakers_rows
        ],
    )
    con.commit()
    con.close()


def write_dataset_card(docs: list[dict], speeches: list[dict], speakers_rows: list[dict]) -> None:
    total_words = sum(s["word_count"] for s in speeches)
    total_chars = sum(s["char_count"] for s in speeches)
    dates = sorted(d["tarih"] for d in docs if d.get("tarih"))
    date_min = dates[0] if dates else "—"
    date_max = dates[-1] if dates else "—"
    by_lang = Counter(s.get("language", "tr") for s in speeches)

    top_spk_md = [
        f"| {r['speaker_name']} | {r.get('community') or '—'} | {r['speech_count']:,} | {r['word_count']:,} | {r['first_date'] or '—'} – {r['last_date'] or '—'} |"
        for r in speakers_rows[:20]
    ]

    card = f"""---
language:
- tr
- el
license: cc-by-4.0
task_categories:
- text-retrieval
- translation
pretty_name: Kıbrıs Cumhuriyeti Temsilciler Meclisi Tutanakları (Türkçe & Orijinal İki Dilli)
configs:
- config_name: speeches
  default: true
  data_files:
  - split: train
    path: data/speeches.parquet
- config_name: documents
  data_files:
  - split: train
    path: data/documents.parquet
- config_name: speakers
  data_files:
  - split: train
    path: data/speakers.parquet
---

# Kıbrıs Cumhuriyeti Temsilciler Meclisi Tutanakları (Türkçe Konuşmacı Bazlı Veri Seti)

Kıbrıs Cumhuriyeti Temsilciler Meclisi (`parliament.cy`) resmî tutanak arşivinin, **Kıbrıs Türk okuyucuların tamamını Türkçe okuyup arayabilmesi** için konuşmacı bazlı (speaker-turn) yapılandırılmış, Yunanca konuşmaları sadık Türkçe çevirisi ve orijinal Yunanca metniyle birlikte sunan açık veri seti.

* **Kaynak:** [Kıbrıs Cumhuriyeti Temsilciler Meclisi (parliament.cy)](https://www.parliament.cy/)
* **Toplam Birleşim (Belge):** {len(docs):,}
* **Toplam Konuşma Bloğu (Turn):** {len(speeches):,}
* **Benzersiz Konuşmacı:** {len(speakers_rows):,}
* **Toplam Kelime / Karakter (Türkçe):** {total_words:,} kelime · {total_chars:,} karakter
* **Tarih Aralığı:** `{date_min}` – `{date_max}`
* **Orijinal Dil Dağılımı:** {", ".join(f"`{k}`: {v:,}" for k, v in by_lang.most_common())}

## Alt Veri Setleri (Configs)

1. **`speeches` (varsayılan):** Her satır tek bir konuşmacı sözüdür (`speech_id`, `doc_id`, `meclis`, `donem`, `yasama_yili`, `birlesim`, `oturum`, `tarih`, `turn_index`, `speaker_name`, `speaker_name_parsed`, `speaker_raw`, `speaker_role`, `speaker_title`, `constituency`, `modifiers`, `canon_method`, `text`, `text_original`, `language`, `community`, `page_start`, `page_end`, `char_count`, `word_count`, `text_source`, `source_file`, `source_url`).
   - `text`: Kıbrıs Türk okuyucular için tam metin **Türkçe** konuşma (orijinal Türkçe konuşmalar kelimesi kelimesine; Yunanca konuşmalar sadık Türkçe çeviri).
   - `text_original`: Tutanaktaki **orijinal** Yunanca veya Türkçe zabıt metni.
2. **`documents`:** Birleşim düzeyinde tam metin (Türkçe + orijinal) ve meta veriler.
3. **`speakers`:** Konuşmacı dizini (konuşma sayısı, kelime sayısı, aktif dönem, cemaat, unvanlar ve seçim bölgeleri).

## En Çok Söz Alan Konuşmacılar

| Konuşmacı | Toplum | Konuşma | Kelime | Tarih Aralığı |
|---|---|---:|---:|---|
{chr(10).join(top_spk_md)}
"""
    (HF_DIR / "README.md").write_text(card, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Build Parquet dataset + SQLite FTS5 from parsed JSONL.")
    ap.add_argument("--skip-sqlite", action="store_true")
    args = ap.parse_args()

    t0 = time.time()
    docs = [json.loads(l) for l in (PARSED_DIR / "documents.jsonl").open("r", encoding="utf-8") if l.strip()]
    speeches = [json.loads(l) for l in (PARSED_DIR / "speeches.jsonl").open("r", encoding="utf-8") if l.strip()]
    print(f"Loaded {len(docs):,} docs and {len(speeches):,} speeches.")

    res_report = resolve_records(speeches, load_rosters())
    (PARSED_DIR / "speaker_resolution_report.json").write_text(
        json.dumps(res_report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Resolved speakers: anchors={res_report['anchors']} | methods={res_report['method_counts']}")

    doc_speakers = defaultdict(set)
    spk_stats = defaultdict(
        lambda: {
            "speech_count": 0,
            "word_count": 0,
            "docs": set(),
            "dates": [],
            "meclisler": set(),
            "donemler": set(),
            "titles": Counter(),
            "constituencies": Counter(),
            "communities": Counter(),
            "raw_variants": Counter(),
        }
    )

    for s in speeches:
        nm = s["speaker_name"]
        doc_speakers[s["doc_id"]].add(nm)
        st = spk_stats[nm]
        st["speech_count"] += 1
        st["word_count"] += s["word_count"]
        st["docs"].add(s["doc_id"])
        if s.get("tarih"):
            st["dates"].append(s["tarih"])
        if s.get("meclis"):
            st["meclisler"].add(s["meclis"])
        if s.get("donem") is not None:
            st["donemler"].add(int(s["donem"]))
        if s.get("speaker_title"):
            st["titles"][s["speaker_title"]] += 1
        if s.get("constituency"):
            st["constituencies"][s["constituency"]] += 1
        if s.get("community"):
            st["communities"][s["community"]] += 1
        if s.get("speaker_name_parsed"):
            st["raw_variants"][s["speaker_name_parsed"]] += 1

    for d in docs:
        d["konusmacilar"] = sorted(doc_speakers.get(d["doc_id"], set()))

    speakers_rows = []
    for nm, st in spk_stats.items():
        dates_s = sorted(st["dates"])
        comm = st["communities"].most_common(1)[0][0] if st["communities"] else ""
        speakers_rows.append(
            {
                "speaker_name": nm,
                "speech_count": st["speech_count"],
                "word_count": st["word_count"],
                "doc_count": len(st["docs"]),
                "first_date": dates_s[0] if dates_s else None,
                "last_date": dates_s[-1] if dates_s else None,
                "community": comm,
                "meclisler": sorted(st["meclisler"]),
                "donemler": sorted(st["donemler"]),
                "titles": [t for t, _ in st["titles"].most_common(15)],
                "constituencies": [c for c, _ in st["constituencies"].most_common(5)],
                "raw_variants": [v for v, _ in st["raw_variants"].most_common(20)],
            }
        )
    speakers_rows.sort(key=lambda r: (-r["speech_count"], r["speaker_name"]))

    n_sp, sz_sp = write_parquet(speeches, HF_DATA_DIR / "speeches.parquet")
    n_doc, sz_doc = write_parquet(docs, HF_DATA_DIR / "documents.parquet")
    n_spk, sz_spk = write_parquet(speakers_rows, HF_DATA_DIR / "speakers.parquet")
    print(
        f"  speeches.parquet:  {n_sp:,} rows ({sz_sp / 1024:.1f} KB)\n"
        f"  documents.parquet: {n_doc:,} rows ({sz_doc / 1024:.1f} KB)\n"
        f"  speakers.parquet:  {n_spk:,} rows ({sz_spk / 1024:.1f} KB)"
    )

    write_dataset_card(docs, speeches, speakers_rows)
    if not args.skip_sqlite:
        build_sqlite_fts(speeches, speakers_rows)
        print(f"Built {DB_PATH} ({DB_PATH.stat().st_size / 1024:.1f} KB) in {time.time() - t0:.2f}s.")


if __name__ == "__main__":
    main()
