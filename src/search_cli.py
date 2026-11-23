"""Instant CLI search over the local SQLite FTS5 database (data/search.db)."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

DB_PATH = Path("data/search.db")


def main() -> None:
    ap = argparse.ArgumentParser(description="Search Republic of Cyprus parliamentary minutes (Turkish).")
    ap.add_argument("--list-speakers", help="List speakers matching substring")
    ap.add_argument("--speaker", help="Filter by speaker name (substring or exact)")
    ap.add_argument("--query", "-q", help="FTS5 query on Turkish speech text")
    ap.add_argument("--from-date", help="Start date YYYY-MM-DD")
    ap.add_argument("--to-date", help="End date YYYY-MM-DD")
    ap.add_argument("--language", choices=("tr", "el", "bilingual"), help="Filter by original spoken language")
    ap.add_argument("--show-original", action="store_true", help="Also print original Greek/Turkish verbatim text")
    ap.add_argument("-n", "--limit", type=int, default=10)
    args = ap.parse_args()

    if not DB_PATH.exists():
        raise SystemExit("Run `python src/build_dataset.py` first to create data/search.db.")

    con = sqlite3.connect(str(DB_PATH))
    cur = con.cursor()

    if args.list_speakers is not None:
        rows = cur.execute(
            """
            SELECT speaker_name, community, speech_count, word_count, first_date, last_date
            FROM speakers
            WHERE lower(speaker_name) LIKE ?
            ORDER BY speech_count DESC
            LIMIT ?
            """,
            (f"%{args.list_speakers.lower()}%", args.limit),
        ).fetchall()
        for nm, comm, sc, wc, fd, ld in rows:
            print(f"  {nm:28s} | {comm or '-':5s} | {sc:5d} söz | {wc:7d} kelime | {fd}..{ld}")
        return

    where = []
    params = []
    from_clause = "speeches s"

    if args.query:
        from_clause = "speeches_fts f JOIN speeches s ON s.speech_id = f.speech_id"
        where.append("speeches_fts MATCH ?")
        params.append(args.query)
    if args.speaker:
        where.append("lower(s.speaker_name) LIKE ?")
        params.append(f"%{args.speaker.lower()}%")
    if args.from_date:
        where.append("s.tarih >= ?")
        params.append(args.from_date)
    if args.to_date:
        where.append("s.tarih <= ?")
        params.append(args.to_date)
    if args.language:
        where.append("s.language = ?")
        params.append(args.language)

    w_sql = ("WHERE " + " AND ".join(where)) if where else ""
    sql = f"""
        SELECT s.speech_id, s.tarih, s.birlesim, s.page_start, s.speaker_name, s.speaker_title,
               s.community, s.language, s.text, s.text_original
        FROM {from_clause}
        {w_sql}
        ORDER BY s.tarih DESC, s.turn_index ASC
        LIMIT ?
    """
    params.append(args.limit)
    rows = cur.execute(sql, params).fetchall()
    print(f"Found {len(rows)} result(s):")
    for sid, dt, b, pg, spk, title, comm, lang, txt, orig in rows:
        tag = "Orijinal Türkçe" if lang == "tr" else "Yunanca → Türkçe"
        print(f"\n[{dt} · B{b} · s.{pg}] {spk} ({title or comm or 'Üye'}) [{tag}]")
        print(f"  {txt[:420]}{'...' if len(txt) > 420 else ''}")
        if args.show_original and lang != "tr" and orig:
            print(f"  [Orijinal]: {orig[:300]}{'...' if len(orig) > 300 else ''}")


if __name__ == "__main__":
    main()
