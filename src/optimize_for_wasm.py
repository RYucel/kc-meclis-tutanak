"""Re-pack speeches.parquet (sorted by speaker_name, tarih DESC) & documents.parquet with small row groups
for instant DuckDB-WASM HTTP range reads, generate per-term shards in terms_cache/, and build
space_static/speakers_index.json + space_static/terms_index.json in the exact kktcmeclisarsivi.org format.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path

import duckdb

HF_DATA = Path("data/hf_dataset/data")
TERMS_CACHE = Path("data/hf_dataset/terms_cache")
STATIC_SPACE = Path("space_static")
OFFICIAL_ROSTERS_PATH = Path("data/official_rosters.json")

_TR_FOLD = str.maketrans(
    {
        "Ç": "c", "ç": "c", "Ğ": "g", "ğ": "g", "İ": "i", "I": "i", "ı": "i",
        "Ö": "o", "ö": "o", "Ş": "s", "ş": "s", "Ü": "u", "ü": "u",
        "Â": "a", "â": "a", "Î": "i", "î": "i", "Û": "u", "û": "u",
    }
)

# Republic of Cyprus House of Representatives Terms (1960–2026), newest -> oldest (active terms first when populated)
TERM_CATALOG = [
    ("KC", 1, "KC 1. Yasama Dönemi", "1960–1970", "Kıbrıs Cumhuriyeti Temsilciler Meclisi (1960–1963 İki Toplumlu Dönem Dahil)"),
    ("KC", 2, "KC 2. Yasama Dönemi", "1970–1976", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
    ("KC", 3, "KC 3. Yasama Dönemi", "1976–1981", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
    ("KC", 4, "KC 4. Yasama Dönemi", "1981–1985", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
    ("KC", 5, "KC 5. Yasama Dönemi", "1985–1991", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
    ("KC", 6, "KC 6. Yasama Dönemi", "1991–1996", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
    ("KC", 7, "KC 7. Yasama Dönemi", "1996–2001", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
    ("KC", 8, "KC 8. Yasama Dönemi", "2001–2006", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
    ("KC", 9, "KC 9. Yasama Dönemi", "2006–2011", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
    ("KC", 10, "KC 10. Yasama Dönemi", "2011–2016", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
    ("KC", 11, "KC 11. Yasama Dönemi", "2016–2021", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
    ("KC", 12, "KC 12. Yasama Dönemi", "2021–2026", "Kıbrıs Cumhuriyeti Temsilciler Meclisi"),
]

ROLE_LABELS = {"Meclis Başkanı", "Geçici Başkan", "Kâtip", "Kâtipler", "Rum Milletvekili (Adı Belirtilmemiş)", "Türk Milletvekili (Adı Belirtilmemiş)"}


def fold_ascii(s: str) -> str:
    s = (s or "").translate(_TR_FOLD).lower().replace("\u0307", "")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s]", " ", s)).strip()


def build_speakers_index(con: duckdb.DuckDBPyConnection, sp_path: str, doc_path: str, rosters: dict) -> dict:
    verified_names = {
        m["name"]
        for entry in rosters.values()
        for m in entry.get("members", [])
    }
    alias_tokens: dict[str, list[str]] = {}
    for entry in rosters.values():
        for m in entry.get("members", []):
            toks = sorted({fold_ascii(a) for a in (m.get("aliases") or []) if fold_ascii(a)})
            if toks:
                alias_tokens[m["name"]] = toks

    rows = con.execute(
        f"""
        SELECT speaker_name,
               COUNT(*) AS s,
               SUM(word_count) AS w,
               COUNT(DISTINCT doc_id) AS d,
               MIN(tarih) AS a,
               MAX(tarih) AS b,
               LIST(DISTINCT constituency) FILTER (WHERE constituency IS NOT NULL AND constituency <> '') AS c,
               LIST(DISTINCT speaker_title) FILTER (WHERE speaker_title IS NOT NULL AND speaker_title <> '') AS t,
               MODE(community) FILTER (WHERE community IS NOT NULL AND community <> '') AS comm
        FROM read_parquet('{sp_path}')
        GROUP BY 1
        ORDER BY s DESC, speaker_name ASC
        """
    ).fetchall()

    # Yearly breakdown per speaker for the dossier timeline chart
    yr_rows = con.execute(
        f"""
        SELECT speaker_name, SUBSTR(tarih, 1, 4) AS yr, COUNT(*) AS cnt
        FROM read_parquet('{sp_path}')
        WHERE tarih IS NOT NULL AND LENGTH(tarih) >= 4
        GROUP BY 1, 2
        ORDER BY 1, 2
        """
    ).fetchall()
    by_year: dict[str, dict[str, int]] = {}
    for nm, yr, cnt in yr_rows:
        by_year.setdefault(nm, {})[yr] = int(cnt)

    speakers_list = []
    for nm, s, w, d, a, b, c, t, comm in rows:
        is_role = nm in ROLE_LABELS
        is_verified = nm in verified_names
        yr_pairs = sorted(by_year.get(nm, {}).items())
        folded_variants = [fold_ascii(nm)]
        for al in alias_tokens.get(nm, []):
            if al not in folded_variants:
                folded_variants.append(al)
        entry = {
            "n": nm,
            "f": " | ".join(folded_variants),
            "s": int(s),
            "w": int(w or 0),
            "d": int(d),
            "a": a or "",
            "b": b or "",
            "c": [x for x in (c or []) if x],
            "t": [x for x in (t or []) if x],
            "y": [[yr, cnt] for yr, cnt in yr_pairs],
            "cm": comm or "",
            "v": 1 if is_verified else 0,
            "r": 1 if is_role else 0,
            "p": 1 if (not is_verified and not is_role and len(nm.split()) >= 2) else 0,
        }
        speakers_list.append(entry)

    tot_sp, tot_words, tot_docs, min_d, max_d = con.execute(
        f"SELECT COUNT(*), SUM(word_count), COUNT(DISTINCT doc_id), MIN(tarih), MAX(tarih) FROM read_parquet('{sp_path}')"
    ).fetchone()
    latest = con.execute(
        f"""
        SELECT doc_id, meclis, donem, birlesim, tarih, source_file, source_url
        FROM read_parquet('{doc_path}')
        ORDER BY tarih DESC NULLS LAST, doc_id DESC
        LIMIT 1
        """
    ).fetchone()

    lang_counts = dict(
        con.execute(f"SELECT language, COUNT(*) FROM read_parquet('{sp_path}') GROUP BY 1").fetchall()
    )

    stats = {
        "speeches": int(tot_sp or 0),
        "words": int(tot_words or 0),
        "docs": int(tot_docs or 0),
        "speakers": len(speakers_list),
        "min_date": min_d or "",
        "max_date": max_d or "",
        "latest_date": latest[4] if latest else "",
        "latest_doc_id": latest[0] if latest else "",
        "latest_meclis": latest[1] if latest else "KC",
        "latest_donem": latest[2] if latest else 1,
        "latest_birlesim": latest[3] if latest else 1,
        "latest_source_file": latest[5] if latest else "",
        "latest_source_url": latest[6] if latest else "",
        "languages": {k: int(v) for k, v in lang_counts.items()},
        "synced_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }

    return {"stats": stats, "speakers": speakers_list}


def build_terms_index(con: duckdb.DuckDBPyConnection, sp_path: str, rosters: dict) -> dict:
    term_totals: dict[tuple, tuple[int, int, str | None, str | None]] = {}
    for m, d, docs, turns, mn, mx in con.execute(
        f"""
        SELECT meclis, donem, COUNT(DISTINCT doc_id), COUNT(*), MIN(tarih), MAX(tarih)
        FROM read_parquet('{sp_path}')
        GROUP BY 1, 2
        """
    ).fetchall():
        term_totals[(m, d)] = (int(docs), int(turns), mn, mx)

    global_counts = {
        nm: int(cnt)
        for nm, cnt in con.execute(
            f"SELECT speaker_name, COUNT(*) FROM read_parquet('{sp_path}') GROUP BY 1"
        ).fetchall()
    }

    per_term_rows: dict[tuple, dict[str, dict]] = {}
    for m, d, nm, turns, words, docs, const, title, comm in con.execute(
        f"""
        SELECT meclis, donem, speaker_name,
               COUNT(*) AS turns,
               SUM(word_count) AS words,
               COUNT(DISTINCT doc_id) AS docs,
               MODE(constituency) FILTER (WHERE constituency IS NOT NULL AND constituency <> '') AS const,
               MODE(speaker_title) FILTER (WHERE speaker_title IS NOT NULL AND speaker_title <> '') AS title,
               MODE(community) FILTER (WHERE community IS NOT NULL AND community <> '') AS comm
        FROM read_parquet('{sp_path}')
        GROUP BY 1, 2, 3
        """
    ).fetchall():
        per_term_rows.setdefault((m, d), {})[nm] = {
            "s": int(turns),
            "w": int(words or 0),
            "d": int(docs),
            "c": const or "",
            "t": title or "",
            "cm": comm or "",
        }

    terms_out = []
    for meclis, donem, label, years, group_label in TERM_CATALOG:
        key = (meclis, donem)
        term_id = f"{meclis}:{donem}"
        off = rosters.get(term_id)
        if key not in term_totals and not off:
            continue

        docs_cnt, turns_cnt, min_d, max_d = term_totals.get(key, (0, 0, None, None))
        sp_map = per_term_rows.get(key, {})
        members = []
        seen = set()

        if off and off.get("members"):
            for om in off["members"]:
                nm = om["name"]
                seen.add(nm)
                st = sp_map.get(nm)
                members.append(
                    {
                        "n": nm,
                        "o": 1,
                        "p": om.get("party", ""),
                        "c": om.get("constituency", "") or (st["c"] if st else ""),
                        "cm": om.get("community", "") or (st["cm"] if st else ""),
                        "t": (st["t"] if st else ""),
                        "s": st["s"] if st else 0,
                        "ts": int(global_counts.get(nm, st["s"] if st else 0)),
                        "w": st["w"] if st else 0,
                        "d": st["d"] if st else 0,
                        "nt": om.get("note", ""),
                    }
                )
        for nm, st in sp_map.items():
            if nm in seen or nm in ROLE_LABELS:
                continue
            members.append(
                {
                    "n": nm,
                    "o": 0,
                    "p": "",
                    "c": st["c"],
                    "cm": st["cm"],
                    "t": st["t"],
                    "s": st["s"],
                    "ts": int(global_counts.get(nm, st["s"])),
                    "w": st["w"],
                    "d": st["d"],
                    "nt": "",
                }
            )

        members.sort(key=lambda x: (-x["s"], x["n"]))
        terms_out.append(
            {
                "id": term_id,
                "meclis": meclis,
                "donem": donem,
                "label": label,
                "years": years,
                "group": group_label,
                "docs": docs_cnt,
                "speeches": turns_cnt,
                "min_date": min_d or "",
                "max_date": max_d or "",
                "official": bool(off and off.get("members")),
                "partial": bool(off and off.get("partial")),
                "members": members,
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "terms": terms_out,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Optimize Parquet files for DuckDB-WASM and build static JSON indices.")
    ap.add_argument("--local-copy", action="store_true", help="Also mirror Parquet files into space_static/data/ for local preview")
    args = ap.parse_args()

    t0 = time.time()
    STATIC_SPACE.mkdir(parents=True, exist_ok=True)
    TERMS_CACHE.mkdir(parents=True, exist_ok=True)

    sp_in = HF_DATA / "speeches.parquet"
    doc_in = HF_DATA / "documents.parquet"
    if not sp_in.exists():
        raise SystemExit("Run `python src/build_dataset.py` first.")

    con = duckdb.connect()

    # Check whether input speeches.parquet still contains text_original (idempotent re-runs!)
    cols = {r[0] for r in con.execute(f"DESCRIBE SELECT * FROM read_parquet('{sp_in}')").fetchall()}
    orig_out = HF_DATA / "speeches_original.parquet"

    if "text_original" in cols:
        # 1. Extract original Greek/bilingual verbatim texts into a separate speech_id-sorted Parquet
        #    so hot search queries NEVER download Greek text unless user clicks "Orijinal Yunanca" or opens Drawer!
        orig_tmp = HF_DATA / "speeches_original.opt.parquet"
        con.execute(
            f"""
            COPY (
                SELECT speech_id, language, text_original
                FROM read_parquet('{sp_in}')
                WHERE text_original IS NOT NULL AND text_original <> '' AND language <> 'tr'
                ORDER BY speech_id ASC
            ) TO '{orig_tmp}' (FORMAT PARQUET, COMPRESSION ZSTD, ROW_GROUP_SIZE 2000)
            """
        )
        orig_tmp.replace(orig_out)

        # 2. Re-pack hot speeches.parquet WITHOUT text_original (adds tiny has_original boolean)
        sp_tmp = HF_DATA / "speeches.opt.parquet"
        con.execute(
            f"""
            COPY (
                SELECT * EXCLUDE (text_original),
                       (language <> 'tr' AND text_original IS NOT NULL AND text_original <> '' AND text_original <> text) AS has_original
                FROM read_parquet('{sp_in}')
                ORDER BY speaker_name ASC, tarih DESC NULLS LAST, turn_index ASC
            ) TO '{sp_tmp}' (FORMAT PARQUET, COMPRESSION ZSTD, ROW_GROUP_SIZE 10000)
            """
        )
        sp_tmp.replace(sp_in)
    else:
        sp_tmp = HF_DATA / "speeches.opt.parquet"
        con.execute(
            f"""
            COPY (
                SELECT * FROM read_parquet('{sp_in}')
                ORDER BY speaker_name ASC, tarih DESC NULLS LAST, turn_index ASC
            ) TO '{sp_tmp}' (FORMAT PARQUET, COMPRESSION ZSTD, ROW_GROUP_SIZE 10000)
            """
        )
        sp_tmp.replace(sp_in)

    doc_tmp = HF_DATA / "documents.opt.parquet"
    con.execute(
        f"""
        COPY (
            SELECT * FROM read_parquet('{doc_in}')
            ORDER BY doc_id ASC
        ) TO '{doc_tmp}' (FORMAT PARQUET, COMPRESSION ZSTD, ROW_GROUP_SIZE 500)
        """
    )
    doc_tmp.replace(doc_in)

    # Build per-term skinny Parquet shards (sorted by tarih DESC for fast chronological term scans)
    active_terms = con.execute(
        f"SELECT DISTINCT meclis, donem FROM read_parquet('{sp_in}') ORDER BY 1, 2"
    ).fetchall()
    for meclis, donem in active_terms:
        fname = f"{meclis}_{donem}.parquet" if donem is not None else f"{meclis}.parquet"
        cond = f"meclis = '{meclis}' AND donem = {int(donem)}" if donem is not None else f"meclis = '{meclis}'"
        con.execute(
            f"""
            COPY (
                SELECT * FROM read_parquet('{sp_in}')
                WHERE {cond}
                ORDER BY tarih DESC NULLS LAST, turn_index ASC
            ) TO '{TERMS_CACHE / fname}' (FORMAT PARQUET, COMPRESSION ZSTD, ROW_GROUP_SIZE 10000)
            """
        )

    rosters = json.loads(OFFICIAL_ROSTERS_PATH.read_text(encoding="utf-8")) if OFFICIAL_ROSTERS_PATH.exists() else {}
    spk_idx = build_speakers_index(con, str(sp_in), str(doc_in), rosters)
    terms_idx = build_terms_index(con, str(sp_in), rosters)

    (STATIC_SPACE / "speakers_index.json").write_text(
        json.dumps(spk_idx, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
    )
    (STATIC_SPACE / "terms_index.json").write_text(
        json.dumps(terms_idx, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
    )

    if args.local_copy:
        local_data = STATIC_SPACE / "data"
        local_cache = STATIC_SPACE / "terms_cache"
        local_data.mkdir(parents=True, exist_ok=True)
        local_cache.mkdir(parents=True, exist_ok=True)
        shutil.copy2(sp_in, local_data / "speeches.parquet")
        if orig_out.exists():
            shutil.copy2(orig_out, local_data / "speeches_original.parquet")
        shutil.copy2(doc_in, local_data / "documents.parquet")
        for f in TERMS_CACHE.glob("*.parquet"):
            shutil.copy2(f, local_cache / f.name)
        print(f"Mirrored local Parquet files into {local_data}/ and {local_cache}/")

    con.close()

    # Build prefix-sharded serverless inverted index for instant keyword lookup
    from build_search_index import build_inverted_index
    build_inverted_index(sp_in, STATIC_SPACE / "search_idx")

    orig_kb = (orig_out.stat().st_size / 1024) if orig_out.exists() else 0.0
    print(
        f"Optimized Parquet (speeches={sp_in.stat().st_size/1024:.1f} KB, "
        f"speeches_original={orig_kb:.1f} KB) + built indices ({len(spk_idx['speakers'])} speakers, "
        f"{len(terms_idx['terms'])} terms) in {time.time() - t0:.2f}s."
    )


if __name__ == "__main__":
    main()
