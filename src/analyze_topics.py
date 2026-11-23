"""Analyze Republic of Cyprus parliamentary topics & unified concepts in Turkish (DuckDB vectorized RE2).

Produces `space_static/topics_index.json` and `space_static/speaker_topics.json` in the exact schema
used by `kktcmeclisarsivi.org`, guaranteeing `badge_count === search_count` in DuckDB-WASM.
"""

from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import duckdb

from optimize_for_wasm import TERM_CATALOG

HF_DATA = Path("data/hf_dataset/data")
STATIC_SPACE = Path("space_static")

_WB_L = "(^|[^a-zçğöşü])"
_WB_R = "($|[^a-zçğöşü])"


def norm_tr_i(s: str) -> str:
    """Exact equivalent of DuckDB `replace(lower(text), 'ı', 'i')`."""
    return s.replace("İ", "i").replace("I", "i").replace("ı", "i").lower().replace("\u0307", "")


def build_re2_pattern(terms: list[str]) -> str:
    alts = [re.escape(norm_tr_i(t)) for t in terms if t.strip()]
    return f"{_WB_L}({'|'.join(alts)})"


CURATED_TOPICS = [
    {
        "id": "anayasa_kurulus",
        "label": "Anayasa & 1960 Kuruluş Düzeni",
        "note": "Anayasa, Zürih, madde 73, madde 76, madde 69, bağımsızlık, toprak bütünlüğü",
        "patterns": ["anayasa", "zürih", "bağimsizlik", "toprak bütünlüğ", "egemenlik", "cumhuriyet"],
    },
    {
        "id": "iki_toplumlu_tercume",
        "label": "İki Toplumlu Yönetim, Cemaatler & Tercüme",
        "note": "Türk Grubu, Rum/Elen, cemaat, tercüme, tercüman, ayrı çoğunluk, ikili dil",
        "patterns": ["tercüme", "tercüman", "türk grub", "türk cemaat", "elen cemaat", "rum cemaat", "iki toplum", "ayri çoğunluk", "ekseriyet"],
    },
    {
        "id": "meclis_ictuzuk",
        "label": "Meclis İç Tüzüğü, Komiteler & Soru Hakkı",
        "note": "Seçme Komitesi, iç tüzük, gündem, soru önergesi, tenkit, yeter sayısı / nisap, oylama",
        "patterns": ["seçme komite", "iç tüzük", "tüzük", "gündem", "sual", "soru", "tenkit", "nisap", "yeter sayi", "oylama", "komite"],
    },
    {
        "id": "yargi_anayasa_mahkemesi",
        "label": "Yargı, Yüksek Anayasa Mahkemesi & Hukuk",
        "note": "Yüksek Anayasa Mahkemesi, Forsthoff, avukat, mahkeme, adalet, hukuk",
        "patterns": ["anayasa mahkeme", "forsthoff", "mahkeme", "adalet", "avukat", "hukuk", "yargi", "tekaüdiye"],
    },
    {
        "id": "secim_temsil",
        "label": "Seçimler, Ara Seçim & Temsil",
        "note": "seçim, ara seçim, aday, milletvekili, boşalan koltuk, müstenkif",
        "patterns": ["ara seçim", "seçim", "aday", "namzet", "müstenkif", "vekil", "temsilci"],
    },
    {
        "id": "tarim_uzum_koylu",
        "label": "Tarım, Üzüm, Çiftçi & Kooperatifler",
        "note": "üzüm, tarım, ziraat, çiftçi, köylü, kooperatif, bağcılık, fiyat",
        "patterns": ["üzüm", "tarim", "ziraat", "çiftçi", "köylü", "kooperatif", "bağci", "müstahsil"],
    },
    {
        "id": "issizlik_emek",
        "label": "İşsizlik, İşçi Sınıfı & Sosyal Politika",
        "note": "işsizlik, işçi, emek, istihdam, geçim, yardım, 300.000 sterlin",
        "patterns": ["işsizlik", "işçi", "istihdam", "çalişan", "ücret", "maaş", "ödenek", "yardim"],
    },
    {
        "id": "butce_maliye_vergi",
        "label": "Bütçe, Maliye, Vergi & Harçlar",
        "note": "bütçe, maliye, vergi, harç, sterlin, gümrük, tarife, ödenek",
        "patterns": ["bütçe", "maliye", "vergi", "harç", "sterlin", "gümrük", "tarife", "ekonomi"],
    },
    {
        "id": "tapu_mulkiyet_somurge",
        "label": "Tapu, Mülkiyet & Sömürge Dönemi Yasaları",
        "note": "tapu, taşınmaz, gayrimenkul, sömürge/müstemleke kanunu, mülkiyet",
        "patterns": ["tapu", "gayrimenkul", "taşinmaz", "müstemleke", "sömürge", "mülkiyet", "arazi"],
    },
    {
        "id": "kamu_personel_idare",
        "label": "Kamu Yönetimi, Meclis Personeli & Bakanlıklar",
        "note": "personel, memur, icra organı, bakanlar kurulu, bakanlık, kadro, atama",
        "patterns": ["personel", "memur", "icra organ", "yürütme", "bakanlar kurul", "bakanlik", "kadro", "tayin", "atama"],
    },
    {
        "id": "belediye_altyapi",
        "label": "Belediyeler, Bayındırlık & Altyapı",
        "note": "belediye, bayındırlık, yol, su, ulaşım, imar",
        "patterns": ["belediye", "bayindirlik", "ulaştirma", "altyapi", "imar", "karayol"],
    },
    {
        "id": "ticaret_sanayi",
        "label": "Ticaret, Sanayi & Piyasa Düzenlemesi",
        "note": "ticaret, sanayi, ihracat, ithalat, üretim, piyasa",
        "patterns": ["ticaret", "sanayi", "ihracat", "ithalat", "üretim", "istihsal", "piyasa"],
    },
    {
        "id": "egitim_kultur",
        "label": "Eğitim, Okullar & Üniversite",
        "note": "eğitim, okul, öğretmen, öğrenci, üniversite",
        "patterns": ["eğitim", "okul", "öğretmen", "öğrenci", "üniversite", "maarif"],
    },
    {
        "id": "saglik_hastane",
        "label": "Sağlık, Hastane & Hekimlik",
        "note": "sağlık, hastane, doktor, ilaç, tedavi",
        "patterns": ["sağlik", "hastane", "doktor", "hekim", "ilaç", "tedavi"],
    },
    {
        "id": "dis_politika_uluslararasi",
        "label": "Dış Politika & Uluslararası Anlaşmalar",
        "note": "Bretton Woods, İngiltere, Yunanistan, Türkiye, dışişleri, uluslararası, anlaşma",
        "patterns": ["bretton", "yunanistan", "türkiye", "ingiltere", "dişişleri", "uluslararasi", "antlaşma", "anlaşma"],
    },
]

CURATED_CONCEPTS = [
    ("Anayasa", "Anayasa, anayasal, madde", ["anayasa"]),
    ("Tercüme / Çeviri", "tercüme, tercüman, çeviri", ["tercüme", "tercüman", "çeviri"]),
    ("Seçme Komitesi", "Seçme Komitesi, Komite", ["seçme komite"]),
    ("Türk Grubu / Cemaati", "Türk Grubu, Türk Cemaati, Türk Temsilciler", ["türk grub", "türk cemaat", "türk temsilci", "türk üye"]),
    ("Rum / Elen Cemaati", "Elen Cemaati, Rum Cemaati, Elen Üyeler", ["elen", "rum cemaat", "rum üye"]),
    ("İç Tüzük", "İç Tüzük, tüzük, yönetmelik", ["iç tüzük", "tüzük"]),
    ("Soru Hakkı / Denetim", "sual, soru önergesi, tenkit", ["sual", "soru", "tenkit"]),
    ("İngilizce Metin (Anayasa)", "İngilizce metin, parafe edilen metin", ["ingilizce metin", "ingilizce"]),
    ("Yüksek Anayasa Mahkemesi", "Yüksek Anayasa Mahkemesi, Forsthoff", ["anayasa mahkeme", "forsthoff"]),
    ("Ara Seçim", "ara seçim, boşalan koltuklar, 25 Eylül", ["ara seçim", "25 eylül", "inhilal"]),
    ("İşsizlik & 300.000 Sterlin", "işsizlik, 300.000 sterlin, istihdam", ["işsizlik", "300.000", "300,000"]),
    ("Üzüm Fiyatları & Çiftçi", "üzüm, çiftçi, kooperatif, okka", ["üzüm", "çiftçi", "kooperatif"]),
    ("Avukatlar Tekaüdiye Sandığı", "avukat, tekaüdiye, emeklilik sandığı", ["avukat", "tekaüdiye"]),
    ("Tapu Harçları (44/1958)", "tapu, 44/1958, sömürge kanunu, gayrimenkul", ["tapu", "44/1958", "gayrimenkul", "müstemleke"]),
    ("Meclis Personeli & Ödenek", "personel, kadro, milletvekili ödeneği", ["personel", "ödenek", "maaş"]),
    ("Zürih Anlaşması", "Zürih anlaşması, kuruluş anlaşmaları", ["zürih"]),
    ("Başkanlık Sistemi / İcra", "başkanlık rejimi, icra organı, yürütme", ["başkanlik", "icra organ", "yürütme"]),
    ("Demokrasi & Özgürlük", "demokrasi, hürriyet, insan hakları", ["demokrasi", "demokratik", "hürriyet", "özgürlük", "insan hak"]),
]


def main() -> None:
    t0 = time.time()
    sp_path = HF_DATA / "speeches.parquet"
    if not sp_path.exists():
        raise SystemExit("Run `python src/build_dataset.py` first.")

    STATIC_SPACE.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect()

    topics_meta = []
    for tp in CURATED_TOPICS:
        rx = build_re2_pattern(tp["patterns"])
        topics_meta.append(
            {
                "id": tp["id"],
                "label": tp["label"],
                "note": tp["note"],
                "terms": [norm_tr_i(p) for p in tp["patterns"]],
                "rx": rx,
                "total": 0,
            }
        )

    concepts_meta = []
    for idx, (label, note, pats) in enumerate(CURATED_CONCEPTS, start=1):
        rx = build_re2_pattern(pats)
        concepts_meta.append(
            {
                "id": idx,
                "label": label,
                "note": note,
                "terms": [norm_tr_i(p) for p in pats],
                "rx": rx,
                "total": 0,
            }
        )

    # Single vectorized SQL scan over speeches.parquet for topics and concepts per term
    topic_exprs = [
        f"SUM(CASE WHEN regexp_matches(norm_t, '{tp['rx'].replace(chr(39), chr(39)*2)}') THEN 1 ELSE 0 END) AS t_{i}"
        for i, tp in enumerate(topics_meta)
    ]
    concept_exprs = [
        f"SUM(CASE WHEN regexp_matches(norm_t, '{cp['rx'].replace(chr(39), chr(39)*2)}') THEN 1 ELSE 0 END) AS c_{i}"
        for i, cp in enumerate(concepts_meta)
    ]

    sql_terms = f"""
        WITH base AS (
            SELECT meclis, donem, replace(lower(text), 'ı', 'i') AS norm_t
            FROM read_parquet('{sp_path}')
        )
        SELECT meclis, donem, COUNT(*) AS turns,
               {', '.join(topic_exprs + concept_exprs)}
        FROM base
        GROUP BY 1, 2
    """
    term_rows = con.execute(sql_terms).fetchall()
    by_term_key = {(r[0], r[1]): r for r in term_rows}

    total_turns_all = sum(int(r[2]) for r in term_rows) or 1
    n_topics = len(topics_meta)
    n_concepts = len(concepts_meta)

    for i in range(n_topics):
        topics_meta[i]["total"] = sum(int(r[3 + i]) for r in term_rows)
    for j in range(n_concepts):
        concepts_meta[j]["total"] = sum(int(r[3 + n_topics + j]) for r in term_rows)

    terms_out = []
    for meclis, donem, label, years, group_label in TERM_CATALOG:
        r = by_term_key.get((meclis, donem))
        if not r:
            continue
        turns = int(r[2]) or 1
        t_list = []
        for i, tp in enumerate(topics_meta):
            c = int(r[3 + i])
            t_list.append({"id": tp["id"], "c": c, "p": round((c / turns) * 100.0, 2)})
        t_list.sort(key=lambda x: -x["c"])

        c_list = []
        cc_map = {}
        dist_list = []
        for j, cp in enumerate(concepts_meta):
            c = int(r[3 + n_topics + j])
            cc_map[str(cp["id"])] = c
            if c > 0:
                p = round((c / turns) * 100.0, 2)
                c_list.append({"id": cp["id"], "c": c, "p": p})
                global_rate = max(1e-6, cp["total"] / total_turns_all)
                lift = round((c / turns) / global_rate, 2)
                dist_list.append({"id": cp["id"], "c": c, "l": lift})
        c_list.sort(key=lambda x: -x["c"])
        dist_list.sort(key=lambda x: (-x["l"], -x["c"]))

        terms_out.append(
            {
                "id": f"{meclis}:{donem}",
                "meclis": meclis,
                "donem": donem,
                "label": label,
                "years": years,
                "group": group_label,
                "turns": turns,
                "topics": t_list,
                "top_concepts": c_list[:22],
                "distinctive": dist_list[:12],
                "cc": cc_map,
            }
        )

    topics_payload = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "topics": topics_meta,
        "concepts": concepts_meta,
        "terms": terms_out,
    }
    (STATIC_SPACE / "topics_index.json").write_text(
        json.dumps(topics_payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
    )

    # Per-speaker topic & concept breakdown (matching kktcmeclisarsivi.org speaker_topics.json schema)
    chair_counts = dict(
        con.execute(
            f"""
            SELECT speaker_name, COUNT(*)
            FROM read_parquet('{sp_path}')
            WHERE speaker_role <> 'milletvekili_bakan'
            GROUP BY 1
            """
        ).fetchall()
    )

    sql_spk = f"""
        WITH base AS (
            SELECT speaker_name, speaker_role, replace(lower(text), 'ı', 'i') AS norm_t
            FROM read_parquet('{sp_path}')
        )
        SELECT speaker_name,
               SUM(CASE WHEN speaker_role = 'milletvekili_bakan' THEN 1 ELSE 0 END) AS mp_turns,
               COUNT(*) AS all_turns,
               {', '.join(topic_exprs + concept_exprs)}
        FROM base
        GROUP BY 1
    """
    spk_rows = con.execute(sql_spk).fetchall()
    spk_total_turns = sum(int(r[2]) for r in spk_rows) or 1
    global_c_totals = [sum(int(r[3 + n_topics + j]) for r in spk_rows) for j in range(n_concepts)]

    topic_ids = [tp["id"] for tp in topics_meta]
    speakers_topics_map = {}
    for r in spk_rows:
        nm = r[0]
        mp_n = int(r[1])
        all_n = int(r[2]) or 1
        basis_n = mp_n if mp_n > 0 else all_n
        tp_list = []
        for i, tp in enumerate(topics_meta):
            c = int(r[3 + i])
            if c > 0:
                tp_list.append([i, c])
        tp_list.sort(key=lambda x: -x[1])

        cp_list = []
        for j, cp in enumerate(concepts_meta):
            c = int(r[3 + n_topics + j])
            if c > 0:
                g_rate = max(1e-6, global_c_totals[j] / spk_total_turns)
                lift = round((c / all_n) / g_rate, 2)
                cp_list.append([cp["id"], c, lift])
        cp_list.sort(key=lambda x: (-x[2], -x[1]))

        speakers_topics_map[nm] = {
            "m": all_n,
            "x": int(chair_counts.get(nm, 0)) if mp_n > 0 else 0,
            "t": tp_list[:8],
            "d": cp_list[:8],
        }

    (STATIC_SPACE / "speaker_topics.json").write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "topic_ids": topic_ids,
                "speakers": speakers_topics_map,
            },
            ensure_ascii=False,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )

    con.close()
    print(
        f"Built topics_index.json ({len(topics_meta)} topics, {len(concepts_meta)} concepts) "
        f"& speaker_topics.json ({len(speakers_topics_map)} speakers) in {time.time() - t0:.2f}s."
    )


if __name__ == "__main__":
    main()
