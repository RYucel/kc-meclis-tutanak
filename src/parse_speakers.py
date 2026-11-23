"""Parse extracted Republic of Cyprus parliamentary minutes (Greek + Turkish) into session documents & speaker turns.

Handles:
  - Splitting multi-session volume PDFs into individual sittings (Birleşim) using both Greek
    (`ΣΥΝΕΔΡΙΑΣΙΣ ΤΗΣ 29ης ΑΥΓΟΥΣΤΟΥ 1960`, `ΕΚΤΑΚΤΟΣ ΣΥΝΕΔΡΙΑΣΙΣ ΤΗΣ 7ΗΣ ΑΥΓΟΥΣΤΟΥ 1961`)
    and Turkish (`29 AĞUSTOS 1960 TARİHLİ TOPLANTI`, `16 EYLÜL 1960 TARİHLİ TOPLANTI`) headers.
  - Detecting speaker turns in BOTH Greek (`ΠΡΟΕΔΡΟΣ :`, `Β. ΛΥΣΣΑΡΙΔΗΣ :`, `Ε. ΠΑΠΑΪΩΑΝΝΟΥ :`,
    `ΧΑΛΙΤ ΑΛΗ ΡΙΖΑ :`, `ΓΡΑΜΜΑΤΕΥΣ :`) and Turkish (`H. A. RIZA :`, `Ü. SÜLEYMAN :`,
    `B. NALBANTOĞLU :`, `O. MÜDERRİSOĞLU :`, `KÂTİP :`, `BAŞKAN :`, `GEÇİCİ MECLİS REİSİ ... :`).
  - Aligning paired original (`pNNNN.txt`) and Turkish (`pNNNN.tr.txt`) transcriptions so every
    speech record stores `text` (Turkish for reading/search) AND `text_original` (verbatim source)
    plus `language` (`tr` | `el` | `bilingual`) and `page_start` / `page_end`.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

EXTRACTED_DIR = Path("data/extracted")
PARSED_DIR = Path("data/parsed")

GREEK_MONTHS = {
    "ΙΑΝΟΥΑΡΙΟΥ": 1, "ΙΑΝΟΥΑΡΙΟΣ": 1,
    "ΦΕΒΡΟΥΑΡΙΟΥ": 2, "ΦΕΒΡΟΥΑΡΙΟΣ": 2,
    "ΜΑΡΤΙΟΥ": 3, "ΜΑΡΤΙΟΣ": 3,
    "ΑΠΡΙΛΙΟΥ": 4, "ΑΠΡΙΛΙΟΣ": 4,
    "ΜΑΙΟΥ": 5, "ΜΑΪΟΥ": 5, "ΜΑΙΟΣ": 5,
    "ΙΟΥΝΙΟΥ": 6, "ΙΟΥΝΙΟΣ": 6,
    "ΙΟΥΛΙΟΥ": 7, "ΙΟΥΛΙΟΣ": 7,
    "ΑΥΓΟΥΣΤΟΥ": 8, "ΑΥΓΟΥΣΤΟΣ": 8,
    "ΣΕΠΤΕΜΒΡΙΟΥ": 9, "ΣΕΠΤΕΜΒΡΙΟΣ": 9,
    "ΟΚΤΩΒΡΙΟΥ": 10, "ΟΚΤΩΒΡΙΟΣ": 10,
    "ΝΟΕΜΒΡΙΟΥ": 11, "ΝΟΕΜΒΡΙΟΣ": 11,
    "ΔΕΚΕΜΒΡΙΟΥ": 12, "ΔΕΚΕΜΒΡΙΟΣ": 12,
}

TURKISH_MONTHS = {
    "OCAK": 1, "SUBAT": 2, "ŞUBAT": 2, "MART": 3, "NISAN": 4, "NİSAN": 4,
    "MAYIS": 5, "HAZIRAN": 6, "HAZİRAN": 6, "TEMMUZ": 7, "AGUSTOS": 8, "AĞUSTOS": 8,
    "EYLUL": 9, "EYLÜL": 9, "EKIM": 10, "EKİM": 10, "KASIM": 11, "ARALIK": 12,
}

_GREEK_CHAR_RE = re.compile(r"[\u0370-\u03FF\u1F00-\u1FFF]")
_LATIN_CHAR_RE = re.compile(r"[A-Za-zÇĞİÖŞÜçğıöşü]")

# Session header regexes (Greek and Turkish)
_GR_MONTH_PAT = "|".join(GREEK_MONTHS.keys())
_TR_MONTH_PAT = "|".join(TURKISH_MONTHS.keys())

SESSION_GR_RE = re.compile(
    rf"(?:ΕΚΤΑΚΤΟΣ\s+)?ΣΥΝΕΔΡΙΑΣΙΣ\s+(?:ΤΗΣ\s+)?(\d{{1,2}})(?:ης|ΗΣ|η|Η)?\s+({_GR_MONTH_PAT})\s+(19[6-9]\d|20[0-3]\d)",
    re.I,
)
SESSION_TR_RE = re.compile(
    rf"(\d{{1,2}})\s+({_TR_MONTH_PAT})\s+(19[6-9]\d|20[0-3]\d)\s+TAR[İI]HL[İI]\s+(?:OLAĞANÜSTÜ\s+)?TOPLANTI",
    re.I,
)

# Speaker header line patterns (must end with ':' or ':-' or '—' with short uppercase/name prefix)
SPEAKER_LINE_RE = re.compile(
    r"^\s*([A-ZÇĞİÖŞÜÂÎÛΑ-ΩΆΈΉΊΌΎΏΪΫ][A-ZÇĞİÖŞÜÂÎÛa-zçğıöşüâîûΑ-ΩΆΈΉΊΌΎΏΪΫα-ωάέήίόύώϊϋ.\-\s()]{1,62}?)\s*[:：]\s*(?:[-–—]\s*)?(.*)$"
)

NON_SPEAKER_HEADINGS = {
    "ΗΜΕΡΗΣΙΑ ΔΙΑΤΑΞΙΣ", "ΗΜΕΡΗΣΙΑ ΔΙΑΤΑΞΗ", "GÜNDEM", "GUNDEM",
    "ΠΑΡΟΝΤΕΣ", "ΑΠΟΝΤΕΣ", "KATILANLAR", "KATILMAYANLAR",
    "ΘΕΜΑ", "KONU", "NOT", "AÇIKLAMA", "SONUÇ", "KARAR",
    "ΩΡΑ ΕΝΑΡΞΕΩΣ", "ΩΡΑ ΛΗΞΕΩΣ", "BAŞLANGIÇ SAATİ", "SONA ERİŞ SAATİ",
    "ΠΕΡΙΕΧΟΜΕΝΑ", "İÇİNDEKİLER", "YUNANCA METİN", "TÜRKÇE METİN",
    "SORU", "CEVAP", "ΕΡΩΤΗΣΙΣ", "ΑΠΑΝΤΗΣΙΣ", "ΕΡΩΤΑΤΑΙ",
}


def strip_diacritics_upper(s: str) -> str:
    nfd = unicodedata.normalize("NFD", s)
    clean = "".join(ch for ch in nfd if unicodedata.category(ch) != "Mn")
    return clean.upper().strip()


def detect_language(text: str) -> str:
    """Return 'el', 'tr', or 'bilingual' based on script counts."""
    gr = len(_GREEK_CHAR_RE.findall(text or ""))
    la = len(_LATIN_CHAR_RE.findall(text or ""))
    total = gr + la
    if total == 0:
        return "tr"
    gr_ratio = gr / total
    if gr_ratio >= 0.72:
        return "el"
    if gr_ratio <= 0.18:
        return "tr"
    return "bilingual"


def extract_session_date(line: str) -> tuple[str | None, bool]:
    """Return (YYYY-MM-DD, is_extraordinary) if line is a sitting header, else (None, False)."""
    norm = strip_diacritics_upper(line)
    m_gr = SESSION_GR_RE.search(norm)
    if m_gr:
        d, mo_s, yr = int(m_gr.group(1)), m_gr.group(2).upper(), int(m_gr.group(3))
        mo = GREEK_MONTHS.get(mo_s)
        if mo and 1 <= d <= 31:
            return f"{yr:04d}-{mo:02d}-{d:02d}", ("ΕΚΤΑΚΤΟΣ" in norm)
    m_tr = SESSION_TR_RE.search(line.upper())
    if m_tr:
        d, mo_s, yr = int(m_tr.group(1)), m_tr.group(2).upper(), int(m_tr.group(3))
        mo = TURKISH_MONTHS.get(mo_s)
        if mo and 1 <= d <= 31:
            return f"{yr:04d}-{mo:02d}-{d:02d}", ("OLAĞANÜSTÜ" in line.upper())
    return None, False


def is_valid_speaker_label(raw_label: str) -> bool:
    """Check whether a colon-terminated prefix is a real speaker header rather than prose/agenda."""
    lbl = re.sub(r"\s+", " ", raw_label).strip()
    if len(lbl) < 2 or len(lbl) > 64:
        return False
    norm = strip_diacritics_upper(lbl)
    if norm in NON_SPEAKER_HEADINGS:
        return False
    if any(norm.startswith(h) for h in ("ΕΡΩΤΗΣΙΣ ΥΠΟΒΛΗΘΕΙΣΑ", "ΑΠΑΝΤΗΣΙΣ ΥΠΟΥΡΓΟΥ", "LEYMOSUN TEMSILCISI", "BAF TEMSILCISI", "SAYIN MECLIS", "MADDE ", "ΑΡΘΡΟΝ ")):
        return False
    # Reject pure numbers or sentences with commas/verbs
    if re.match(r"^\d", lbl) or "," in lbl or ";" in lbl:
        return False
    words = lbl.split()
    if len(words) > 7:
        return False

    # Known role headers (Greek & Turkish)
    role_tokens = (
        "ΠΡΟΕΔΡΟΣ", "ΠΡΟΕΔΡΕΥΩΝ", "ΑΝΤΙΠΡΟΕΔΡΟΣ", "ΓΡΑΜΜΑΤΕΥΣ", "ΓΡΑΜΜΑΤΕΙΣ",
        "ΕΛΛΗΝ ΒΟΥΛΕΥΤΗΣ", "ΤΟΥΡΚΟΣ ΒΟΥΛΕΥΤΗΣ",
        "BASKAN", "BAŞKAN", "MECLIS REISI", "MECLİS REİSİ", "REIS", "REİS",
        "GECICI MECLIS REISI", "GEÇİCİ MECLİS REİSİ", "GECICI REIS VEKILI", "GEÇİCİ REİS VEKİLİ",
        "REIS VEKILI", "REİS VEKİLİ", "RIYASET KURSUSUNE", "MECLIS REIS VEKILLIGI",
        "KATIP", "KÂTİP", "KATIPLER", "KÂTİPLER", "SEKRETER",
    )
    if any(rt in norm for rt in role_tokens):
        return True

    # Uppercase speaker names like "Β. ΛΥΣΣΑΡΙΔΗΣ", "H. A. RIZA", "Ü. SÜLEYMAN", "B. NALBANTOĞLU", "ΧΑΛΙΤ ΑΛΗ ΡΙΖΑ"
    letters = [c for c in lbl if c.isalpha()]
    if not letters:
        return False
    upper_ratio = sum(1 for c in letters if c.isupper()) / len(letters)
    if upper_ratio >= 0.78 and 1 <= len(words) <= 5:
        return True

    # Narrative opening-session speaker attributions like "Bay Mihailidis Savvidis :" or "Dr. Orhan Müderrisoğlu :"
    # Every non-particle word after the honorific must be capitalized (rejects prose like "Bay Pavlu özetle şunu söyledi:")
    if re.match(r"^(?:Bay|Dr\.?|Avukat|Sayın)\s+[A-ZÇĞİÖŞÜ]", lbl) and 2 <= len(words) <= 5:
        rest_words = [w for w in words[1:] if w.lower() not in ("ve", "dr", "dr.")]
        if rest_words and all(w[0].isupper() for w in rest_words):
            return True

    return False


def classify_speaker_role(label: str) -> tuple[str, str]:
    """Return (speaker_role, speaker_title) matching kktc-meclis-tutanak taxonomy:
    speaker_role in {'baskan', 'katip', 'milletvekili_bakan'}
    """
    norm = strip_diacritics_upper(label)
    if any(k in norm for k in ("ΠΡΟΕΔΡΕΥΩΝ", "GEÇİCİ MECLİS REİSİ", "GECICI MECLIS REISI", "GEÇİCİ REİS VEKİLİ", "GECICI REIS VEKILI")):
        return "baskan", "Geçici Başkan"
    if any(k in norm for k in ("ΑΝΤΙΠΡΟΕΔΡΟΣ", "REIS VEKILI", "REİS VEKİLİ", "BASKAN YARDIMCISI", "BAŞKAN YARDIMCISI")):
        return "baskan", "Meclis Başkan Yardımcısı"
    if any(k in norm for k in ("ΠΡΟΕΔΡΟΣ", "BASKAN", "BAŞKAN", "MECLIS REISI", "MECLİS REİSİ", "RIYASET")):
        return "baskan", "Meclis Başkanı"
    if any(k in norm for k in ("ΓΡΑΜΜΑΤΕΥΣ", "ΓΡΑΜΜΑΤΕΙΣ", "KATIP", "KÂTİP", "SEKRETER")):
        return "katip", "Kâtip"
    return "milletvekili_bakan", ""


def split_volume_into_sessions(pages: list[dict], default_date: str | None = None) -> list[dict]:
    """Group page dictionaries into distinct parliamentary sittings (Birleşim)."""
    sessions: list[dict] = []
    cur: dict | None = None

    for pg in pages:
        pno = pg["page"]
        orig = (pg.get("text_original") or "").strip()
        tr = (pg.get("text_tr") or "").strip()
        probe_text = tr or orig
        if not probe_text:
            continue

        # Check top lines for a new session header
        top_lines = [l.strip() for l in (orig.splitlines()[:12] + tr.splitlines()[:12]) if l.strip()]
        found_date = None
        is_extra = False
        for ln in top_lines:
            dt, ex = extract_session_date(ln)
            if dt:
                found_date = dt
                is_extra = ex
                break

        if found_date and (cur is None or cur["tarih"] != found_date):
            cur = {
                "tarih": found_date,
                "extraordinary": is_extra,
                "pages": [],
            }
            sessions.append(cur)
        elif cur is None:
            cur = {
                "tarih": default_date,
                "extraordinary": False,
                "pages": [],
            }
            sessions.append(cur)

        cur["pages"].append(pg)

    return sessions


def parse_turns_from_pages(pages: list[dict], use_field: str) -> list[dict]:
    """Extract ordered speaker turns from a session's pages using either 'text_tr' or 'text_original'."""
    turns: list[dict] = []
    cur: dict | None = None

    for pg in pages:
        pno = pg["page"]
        body = (pg.get(use_field) or "").strip()
        if not body:
            continue

        for raw_line in body.splitlines():
            line = raw_line.strip()
            if not line:
                if cur is not None:
                    cur["lines"].append("")
                continue

            # Skip standalone page numbers
            if re.match(r"^\d{1,4}$", line):
                continue

            # Skip session title / time banners inside text
            dt, _ = extract_session_date(line)
            if dt:
                continue

            m = SPEAKER_LINE_RE.match(line)
            if m and is_valid_speaker_label(m.group(1)):
                label = re.sub(r"\s+", " ", m.group(1)).strip()
                rest = m.group(2).strip()
                # Check if label is immediately followed by prose on same line or next lines
                role, title = classify_speaker_role(label)
                cur = {
                    "speaker_raw": label,
                    "speaker_role": role,
                    "speaker_title": title,
                    "page_start": pno,
                    "page_end": pno,
                    "lines": [rest] if rest else [],
                }
                turns.append(cur)
            elif cur is not None:
                cur["lines"].append(line)
                cur["page_end"] = pno

    out: list[dict] = []
    for t in turns:
        text = re.sub(r"\n{3,}", "\n\n", "\n".join(t["lines"]).strip())
        if len(text) < 2:
            continue
        out.append(
            {
                "speaker_raw": t["speaker_raw"],
                "speaker_role": t["speaker_role"],
                "speaker_title": t["speaker_title"],
                "page_start": t["page_start"],
                "page_end": t["page_end"],
                "text": text,
            }
        )
    return out


def parse_extracted_volume(vol: dict) -> tuple[list[dict], list[dict]]:
    """Parse one extracted volume JSON into (documents, speeches)."""
    sessions = split_volume_into_sessions(vol.get("pages", []), default_date=vol.get("date_start"))
    docs: list[dict] = []
    speeches: list[dict] = []

    meclis = vol.get("meclis", "KC")
    donem = vol.get("donem") or 1
    yasama_yili = vol.get("yasama_yili") or 1
    source_file = vol["source_file"]
    source_url = vol["source_url"]

    for b_idx, sess in enumerate(sessions, start=1):
        tarih = sess["tarih"] or vol.get("date_start") or "1960-08-16"
        doc_id = f"{meclis}_D{donem}_Y{yasama_yili}_{tarih}_B{b_idx:03d}"
        s_pages = sess["pages"]
        p_start = min(p["page"] for p in s_pages)
        p_end = max(p["page"] for p in s_pages)

        has_tr = any(p.get("text_tr") for p in s_pages)
        orig_turns = parse_turns_from_pages(s_pages, "text_original")
        tr_turns = parse_turns_from_pages(s_pages, "text_tr") if has_tr else []

        # Align paired Turkish and Original turns when counts match; otherwise fall back safely
        aligned: list[dict] = []
        if tr_turns and len(tr_turns) == len(orig_turns):
            for t_tr, t_or in zip(tr_turns, orig_turns):
                lang = detect_language(t_or["text"])
                aligned.append(
                    {
                        "speaker_raw": t_tr["speaker_raw"],
                        "speaker_raw_original": t_or["speaker_raw"],
                        "speaker_role": t_tr["speaker_role"],
                        "speaker_title": t_tr["speaker_title"] or t_or["speaker_title"],
                        "page_start": t_tr["page_start"],
                        "page_end": t_tr["page_end"],
                        "text": t_tr["text"],
                        "text_original": t_or["text"],
                        "language": lang,
                    }
                )
        elif tr_turns:
            for t_tr in tr_turns:
                aligned.append(
                    {
                        "speaker_raw": t_tr["speaker_raw"],
                        "speaker_raw_original": t_tr["speaker_raw"],
                        "speaker_role": t_tr["speaker_role"],
                        "speaker_title": t_tr["speaker_title"],
                        "page_start": t_tr["page_start"],
                        "page_end": t_tr["page_end"],
                        "text": t_tr["text"],
                        "text_original": t_tr["text"],
                        "language": detect_language(t_tr["text"]),
                    }
                )
        else:
            for t_or in orig_turns:
                lang = detect_language(t_or["text"])
                aligned.append(
                    {
                        "speaker_raw": t_or["speaker_raw"],
                        "speaker_raw_original": t_or["speaker_raw"],
                        "speaker_role": t_or["speaker_role"],
                        "speaker_title": t_or["speaker_title"],
                        "page_start": t_or["page_start"],
                        "page_end": t_or["page_end"],
                        "text": t_or["text"],
                        "text_original": t_or["text"],
                        "language": lang,
                    }
                )

        # Build clean full Turkish session document text for the "Tüm Birleşim Tutanağını Yükle" drawer
        full_tr_text = "\n\n".join(
            (p.get("text_tr") or p.get("text_original") or "").strip()
            for p in s_pages
            if (p.get("text_tr") or p.get("text_original") or "").strip()
        )
        full_orig_text = "\n\n".join(
            (p.get("text_original") or "").strip()
            for p in s_pages
            if (p.get("text_original") or "").strip()
        )
        text_source = s_pages[0].get("text_source", "reocr_vlm_tr")

        for turn_idx, t in enumerate(aligned, start=1):
            speech_id = f"{doc_id}_{turn_idx:04d}"
            txt = t["text"]
            speeches.append(
                {
                    "speech_id": speech_id,
                    "doc_id": doc_id,
                    "meclis": meclis,
                    "donem": donem,
                    "yasama_yili": yasama_yili,
                    "birlesim": b_idx,
                    "oturum": 1,
                    "tarih": tarih,
                    "turn_index": turn_idx,
                    "speaker_name": t["speaker_raw"],
                    "speaker_name_parsed": t["speaker_raw"],
                    "speaker_raw": t["speaker_raw_original"],
                    "speaker_role": t["speaker_role"],
                    "speaker_title": t["speaker_title"],
                    "constituency": "",
                    "modifiers": "",
                    "canon_method": "exact",
                    "text": txt,
                    "text_original": t["text_original"],
                    "language": t["language"],
                    "community": "",
                    "page_start": t["page_start"],
                    "page_end": t["page_end"],
                    "char_count": len(txt),
                    "word_count": len(txt.split()),
                    "text_source": text_source,
                    "source_file": source_file,
                    "source_url": source_url,
                }
            )

        docs.append(
            {
                "doc_id": doc_id,
                "volume_id": vol["volume_id"],
                "meclis": meclis,
                "donem": donem,
                "yasama_yili": yasama_yili,
                "birlesim": b_idx,
                "tarih": tarih,
                "extraordinary": bool(sess["extraordinary"]),
                "page_start": p_start,
                "page_end": p_end,
                "page_count": len(s_pages),
                "turn_count": len(aligned),
                "word_count": len(full_tr_text.split()),
                "char_count": len(full_tr_text),
                "text": full_tr_text,
                "text_original": full_orig_text,
                "text_source": text_source,
                "source_file": source_file,
                "source_url": source_url,
                "konusmacilar": [],
            }
        )

    return docs, speeches


def main() -> None:
    ap = argparse.ArgumentParser(description="Parse extracted parliament.cy volumes into documents.jsonl and speeches.jsonl.")
    ap.add_argument("--extracted-dir", type=Path, default=EXTRACTED_DIR)
    ap.add_argument("--parsed-dir", type=Path, default=PARSED_DIR)
    args = ap.parse_args()

    args.parsed_dir.mkdir(parents=True, exist_ok=True)
    all_docs: list[dict] = []
    all_speeches: list[dict] = []

    for f in sorted(args.extracted_dir.glob("*.json")):
        vol = json.loads(f.read_text(encoding="utf-8"))
        docs, sps = parse_extracted_volume(vol)
        all_docs.extend(docs)
        all_speeches.extend(sps)

    (args.parsed_dir / "documents.jsonl").write_text(
        "\n".join(json.dumps(d, ensure_ascii=False) for d in all_docs) + ("\n" if all_docs else ""),
        encoding="utf-8",
    )
    (args.parsed_dir / "speeches.jsonl").write_text(
        "\n".join(json.dumps(s, ensure_ascii=False) for s in all_speeches) + ("\n" if all_speeches else ""),
        encoding="utf-8",
    )
    print(f"Parsed {len(all_docs)} sitting documents and {len(all_speeches)} speaker turns -> {args.parsed_dir}/")


if __name__ == "__main__":
    main()
