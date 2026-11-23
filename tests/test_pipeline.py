"""End-to-end tests for the Republic of Cyprus parliamentary minutes Turkish archive pipeline."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from crawl_manifest import parse_parliament_cy_filename
from extract_text import classify_page_text
from parse_speakers import detect_language, extract_session_date, is_valid_speaker_label
from speaker_resolution import load_rosters, resolve_records


def test_parse_parliament_cy_filename():
    url = "https://www.parliament.cy/images/media/redirectfile/A%20Vouleftiki%20periodos%20-Synodos%20A%20-%2016.08.1960-07.081961.pdf"
    meta = parse_parliament_cy_filename(url)
    assert meta["meclis"] == "KC"
    assert meta["donem"] == 1
    assert meta["yasama_yili"] == 1
    assert meta["date_start"] == "1960-08-16"
    assert meta["date_end"] == "1961-08-07"


def test_garbled_acrobat_greek_ocr_detection():
    garbled = "TnOTPrEION IHKOINONI-ON KA I EPrON. npOE6POI : 'Ox. rlOl~. XAAIT AA H PIZA : 1tpbaT\"l') ~},I)"
    assert classify_page_text(garbled) == "garbled_ocr"

    clean_tr = "Sayın Meclis Reisi, Anayasanın 73'üncü maddesinin 2'nci fıkrası Seçme Komitesini açıkça düzenlemektedir."
    assert classify_page_text(clean_tr) == "digital_tr"

    clean_el = "Συμφώνως τῶν προνοιῶν τοῦ ἄρθρου 76 τοῦ Συντάγματος κηρύσσω τὴν ἔναρξιν τῆς συνεδριάσεως τῆς Βουλῆς."
    assert classify_page_text(clean_el) == "digital_el"


def test_session_date_and_speaker_labels():
    assert extract_session_date("ΣΥΝΕΔΡΙΑΣΙΣ ΤΗΣ 29ης ΑΥΓΟΥΣΤΟΥ 1960") == ("1960-08-29", False)
    assert extract_session_date("ΕΚΤΑΚΤΟΣ ΣΥΝΕΔΡΙΑΣΙΣ ΤΗΣ 7ΗΣ ΑΥΓΟΥΣΤΟΥ 1961") == ("1961-08-07", True)
    assert extract_session_date("16 EYLÜL 1960 TARİHLİ TOPLANTI") == ("1960-09-16", False)

    assert is_valid_speaker_label("ΠΡΟΕΔΡΟΣ")
    assert is_valid_speaker_label("Β. ΛΥΣΣΑΡΙΔΗΣ")
    assert is_valid_speaker_label("H. A. RIZA")
    assert is_valid_speaker_label("Ü. SÜLEYMAN")
    assert is_valid_speaker_label("Bay Mihailidis Savvidis")
    # Prose lines with verbs must NOT be mistaken for speakers
    assert not is_valid_speaker_label("Bay Pavlu özetle şunu söyledi")
    assert not is_valid_speaker_label("GÜNDEM")
    assert not is_valid_speaker_label("ΗΜΕΡΗΣΙΑ ΔΙΑΤΑΞΙΣ")


def test_cross_script_speaker_resolution():
    rosters = load_rosters(ROOT / "data/official_rosters.json")
    sample = [
        {"speaker_name": "H. A. RIZA", "speaker_name_parsed": "H. A. RIZA", "speaker_raw": "H. A. RIZA", "donem": 1},
        {"speaker_name": "ΧΑΛΙΤ ΑΛΗ ΡΙΖΑ", "speaker_name_parsed": "ΧΑΛΙΤ ΑΛΗ ΡΙΖΑ", "speaker_raw": "ΧΑΛΙΤ ΑΛΗ ΡΙΖΑ", "donem": 1},
        {"speaker_name": "ΠΡΟΕΔΡΟΣ", "speaker_name_parsed": "BAŞKAN", "speaker_raw": "ΠΡΟΕΔΡΟΣ", "donem": 1},
        {"speaker_name": "Β. ΛΥΣΣΑΡΙΔΗΣ", "speaker_name_parsed": "V. LİSSARİDİS", "speaker_raw": "Β. ΛΥΣΣΑΡΙΔΗΣ", "donem": 1},
        {"speaker_name": "Ü. SÜLEYMAN", "speaker_name_parsed": "Ü. SÜLEYMAN", "speaker_raw": "Ü. SÜLEYMAN", "donem": 1},
        {"speaker_name": "GEÇİCİ MECLİS REİS VEKİLİ NİYAZİ MANYERA", "speaker_name_parsed": "GEÇİCİ MECLİS REİS VEKİLİ NİYAZİ MANYERA", "speaker_raw": "GEÇİCİ MECLİS REİS VEKİLİ NİYAZİ MANYERA", "donem": 1},
    ]
    resolve_records(sample, rosters)
    assert [s["speaker_name"] for s in sample] == [
        "Halit Ali Rıza",
        "Halit Ali Rıza",
        "Glafkos Kleridis",
        "Vasos Lissaridis",
        "Ümit Süleyman Onan",
        "Niyazi Manyera",
    ]
    assert sample[0]["community"] == "Türk"
    assert sample[2]["community"] == "Rum"


def test_parquet_and_static_indices_consistency():
    sp_path = ROOT / "space_static/data/speeches.parquet"
    orig_path = ROOT / "space_static/data/speeches_original.parquet"
    doc_path = ROOT / "space_static/data/documents.parquet"
    assert sp_path.exists() and orig_path.exists() and doc_path.exists()

    spk_idx = json.loads((ROOT / "space_static/speakers_index.json").read_text(encoding="utf-8"))
    terms_idx = json.loads((ROOT / "space_static/terms_index.json").read_text(encoding="utf-8"))
    topics_idx = json.loads((ROOT / "space_static/topics_index.json").read_text(encoding="utf-8"))
    spk_topics = json.loads((ROOT / "space_static/speaker_topics.json").read_text(encoding="utf-8"))
    bios = json.loads((ROOT / "space_static/mp_bios.json").read_text(encoding="utf-8"))

    con = duckdb.connect()
    sp_cols = {r[0] for r in con.execute(f"DESCRIBE SELECT * FROM read_parquet('{sp_path}')").fetchall()}
    assert "text_original" not in sp_cols, "Hot speeches.parquet must stay skinny without text_original!"
    assert "has_original" in sp_cols

    n_sp = con.execute(f"SELECT COUNT(*) FROM read_parquet('{sp_path}')").fetchone()[0]
    n_el = con.execute(f"SELECT COUNT(*) FROM read_parquet('{sp_path}') WHERE language = 'el'").fetchone()[0]
    n_tr = con.execute(f"SELECT COUNT(*) FROM read_parquet('{sp_path}') WHERE language = 'tr'").fetchone()[0]
    n_orig = con.execute(f"SELECT COUNT(*) FROM read_parquet('{orig_path}')").fetchone()[0]
    assert n_sp == spk_idx["stats"]["speeches"] == 104
    assert n_el > 50 and n_tr > 30
    assert n_orig == n_el

    # Every speech's primary `text` field must be Turkish readable (no untranslated Greek blocks)
    untranslated = con.execute(
        f"SELECT COUNT(*) FROM read_parquet('{sp_path}') WHERE regexp_matches(text, '[Α-Ωα-ω]{{10,}}')"
    ).fetchone()[0]
    assert untranslated == 0, "All speeches must be readable in Turkish!"

    # Every Greek speech in speeches_original.parquet must retain its verbatim Greek original
    missing_orig = con.execute(
        f"SELECT COUNT(*) FROM read_parquet('{orig_path}') WHERE NOT regexp_matches(text_original, '[Α-Ωα-ω]')"
    ).fetchone()[0]
    assert missing_orig == 0

    # Verify topics_index.json badge count === DuckDB RE2 query count!
    for tp in topics_idx["topics"][:5]:
        rx = tp["rx"].replace("'", "''")
        cnt = con.execute(
            f"SELECT COUNT(*) FROM read_parquet('{sp_path}') WHERE regexp_matches(replace(lower(text), 'ı', 'i'), '{rx}')"
        ).fetchone()[0]
        assert cnt == tp["total"], f"Mismatch for topic {tp['id']}: {cnt} != {tp['total']}"

    assert len(terms_idx["terms"]) >= 1
    assert "topic_ids" in spk_topics and "Glafkos Kleridis" in spk_topics["speakers"]
    assert "bios" in bios and "Halit Ali Rıza" in bios["bios"]
    con.close()


def test_serverless_inverted_index_recall():
    from build_search_index import delta_decode, fold_prefix, norm_tr_i

    idx_dir = ROOT / "space_static/search_idx"
    manifest = json.loads((idx_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["doc_count"] == 104
    assert manifest["token_count"] > 1000
    assert manifest["shard_count"] > 50

    def query_idx(words: list[str]) -> set[str]:
        inter = None
        for w in words:
            wn = norm_tr_i(w)
            p2 = fold_prefix(wn)
            shard = json.loads((idx_dir / f"{p2}.json").read_text(encoding="utf-8"))
            hits = set()
            for tok, deltas in shard.items():
                if tok.startsWith(wn) if hasattr(tok, "startsWith") else tok.startswith(wn):
                    for idx in delta_decode(deltas):
                        hits.add(manifest["docs"][idx][0])
            inter = hits if inter is None else (inter & hits)
        return inter or set()

    con = duckdb.connect()
    sp_path = ROOT / "space_static/data/speeches.parquet"
    for q_words in [["forsthoff"], ["anayasa"], ["tercüme"], ["üzüm"], ["anayasa", "tercüme"]]:
        idx_hits = query_idx(q_words)
        cond = " AND ".join(
            f"contains(replace(lower(text), 'ı', 'i'), '{norm_tr_i(w)}')" for w in q_words
        )
        sql_hits = {
            r[0]
            for r in con.execute(f"SELECT speech_id FROM read_parquet('{sp_path}') WHERE {cond}").fetchall()
        }
        assert len(idx_hits) > 0, f"Expected hits for {q_words}"
        assert sql_hits.issubset(idx_hits), f"Inverted index missed SQL hits for {q_words}: {sql_hits - idx_hits}"
    con.close()
