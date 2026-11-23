"""Cross-script (Greek & Turkish) speaker canonicalization for Republic of Cyprus House of Representatives.

Maps Greek polytonic/monotonic headers, initials, Turkish headers, and presiding chair titles
(`ΠΡΟΕΔΡΟΣ`, `BAŞKAN`, `H. A. RIZA`, `ΧΑΛΙΤ ΑΛΗ ΡΙΖΑ`, `Ü. SÜLEYMAN`, `Β. ΛΥΣΣΑΡΙΔΗΣ`, etc.)
onto unified canonical Turkish display names with constituency, community ('Rum' / 'Türk'),
and audit metadata (`speaker_name_parsed`, `canon_method`).
"""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

from rapidfuzz import fuzz

ROSTERS_PATH = Path("data/official_rosters.json")

_TR_FOLD = str.maketrans(
    {
        "Ç": "c", "ç": "c", "Ğ": "g", "ğ": "g", "İ": "i", "I": "i", "ı": "i",
        "Ö": "o", "ö": "o", "Ş": "s", "ş": "s", "Ü": "u", "ü": "u",
        "Â": "a", "â": "a", "Î": "i", "î": "i", "Û": "u", "û": "u",
    }
)

_GREEK_TO_LATIN = {
    "Α": "a", "Β": "v", "Γ": "g", "Δ": "d", "Ε": "e", "Ζ": "z", "Η": "i", "Θ": "th",
    "Ι": "i", "Κ": "k", "Λ": "l", "Μ": "m", "Ν": "n", "Ξ": "ks", "Ο": "o", "Π": "p",
    "Ρ": "r", "Σ": "s", "Τ": "t", "Υ": "y", "Φ": "f", "Χ": "h", "Ψ": "ps", "Ω": "o",
}

# Presiding Speaker by Term (for resolving bare 'ΠΡΟΕΔΡΟΣ' / 'BAŞKAN' turns)
TERM_SPEAKERS = {
    1: "Glafkos Kleridis",
    2: "Glafkos Kleridis",
    3: "Spiru Kiprianu",
    4: "Georgios Ladas",
    5: "Vasos Lissaridis",
    6: "Aleksis Galanos",
    7: "Spiru Kiprianu",
    8: "Dimitris Hristofyas",
    9: "Marios Garoyan",
    10: "Yannakis Omiru",
    11: "Dimitris Silluris",
    12: "Annita Dimitriu",
}

TERM_VICE_SPEAKERS = {
    1: "Orhan Müderrisoğlu",
}

GENERIC_ROLES = {
    "meclis baskani": ("Meclis Başkanı", "baskan", "Meclis Başkanı"),
    "baskan": ("Meclis Başkanı", "baskan", "Meclis Başkanı"),
    "katip": ("Kâtip", "katip", "Kâtip"),
    "katipler": ("Kâtipler", "katip", "Kâtip"),
    "grammateys": ("Kâtip", "katip", "Kâtip"),
    "grammateis": ("Kâtipler", "katip", "Kâtip"),
    "ellin voyleytis": ("Rum Milletvekili (Adı Belirtilmemiş)", "milletvekili_bakan", "Rum Milletvekili"),
    "rum milletvekili": ("Rum Milletvekili (Adı Belirtilmemiş)", "milletvekili_bakan", "Rum Milletvekili"),
    "turk milletvekili": ("Türk Milletvekili (Adı Belirtilmemiş)", "milletvekili_bakan", "Türk Milletvekili"),
}

_PREFIX_STRIP_RE = re.compile(
    r"^(?:Sayın|Sn\.?|Bay|Dr\.?|Avukat|Geçici\s+Meclis\s+Reis\s+Vekili|Geçici\s+Meclis\s+Reisi|Geçici\s+Reis\s+Vekili|"
    r"Meclis\s+Reisi|Meclis\s+Reis\s+Vekilliği\s+Kürsüsüne\s+gelen|Riyaset\s+Kürsüsüne\s+gelen|"
    r"Βουλευτής|κ\.|Δρ\.?)\s+",
    re.I,
)


def fold_cross_script(s: str) -> str:
    """Normalize Turkish & polytonic/monotonic Greek into a comparable ASCII key."""
    nfd = unicodedata.normalize("NFD", s or "")
    stripped = "".join(ch for ch in nfd if unicodedata.category(ch) != "Mn")
    out = []
    for ch in stripped:
        up = ch.upper()
        if up in _GREEK_TO_LATIN:
            out.append(_GREEK_TO_LATIN[up])
        else:
            out.append(ch)
    latin = "".join(out).translate(_TR_FOLD).lower()
    latin = re.sub(r"[^a-z0-9\s]", " ", latin)
    return re.sub(r"\s+", " ", latin).strip()


def load_rosters(path: Path = ROSTERS_PATH) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def build_alias_lookup(rosters: dict) -> tuple[dict[str, dict], dict[str, dict]]:
    """Return (exact_alias_map, canonical_member_map)."""
    alias_map: dict[str, dict] = {}
    canon_map: dict[str, dict] = {}
    for term_id, entry in rosters.items():
        for m in entry.get("members", []):
            name = m["name"]
            info = {
                "name": name,
                "party": m.get("party", ""),
                "constituency": m.get("constituency", ""),
                "community": m.get("community", ""),
                "note": m.get("note", ""),
                "term_id": term_id,
            }
            canon_map[name] = info
            for cand in [name, *(m.get("aliases") or [])]:
                k = fold_cross_script(cand)
                if k:
                    alias_map[k] = info
                # Also index "Initial Surname" (e.g. "h a riza", "v lissaridis", "g kleridis")
                parts = k.split()
                if len(parts) >= 2:
                    init_sur = f"{parts[0][0]} {parts[-1]}"
                    alias_map.setdefault(init_sur, info)
                    if len(parts) == 3:
                        init2_sur = f"{parts[0][0]} {parts[1][0]} {parts[-1]}"
                        alias_map.setdefault(init2_sur, info)
    return alias_map, canon_map


def resolve_records(speeches: list[dict], rosters: dict | None = None) -> dict:
    """Resolve speaker_name, constituency, community, and canon_method across all speeches in-place."""
    if rosters is None:
        rosters = load_rosters()
    alias_map, canon_map = build_alias_lookup(rosters)
    method_counts: Counter = Counter()
    mappings: Counter = Counter()

    for s in speeches:
        raw_tr = (s.get("speaker_name_parsed") or s.get("speaker_name") or "").strip()
        raw_orig = (s.get("speaker_raw") or raw_tr).strip()
        donem = s.get("donem") or 1

        # Strip decorative narrative prefixes ("Bay Glafkos Kliridis", "Geçici Meclis Reisi Bay H. Hacıharos")
        cleaned = raw_tr
        for _ in range(3):
            nxt = _PREFIX_STRIP_RE.sub("", cleaned).strip()
            if nxt == cleaned:
                break
            cleaned = nxt

        fk_tr = fold_cross_script(cleaned)
        fk_orig = fold_cross_script(raw_orig)
        fk_full = fold_cross_script(raw_tr)

        # 1. Explicit bare presiding Chair / Vice-Chair -> resolve to Term Speaker / Vice-Speaker
        if fk_full in ("baskan", "meclis baskani", "meclis reisi", "proedros") or fk_orig == "proedros":
            if donem in TERM_SPEAKERS:
                target = TERM_SPEAKERS[donem]
                info = canon_map.get(target, {})
                s["speaker_name"] = target
                s["speaker_role"] = "baskan"
                s["speaker_title"] = "Meclis Başkanı"
                s["constituency"] = info.get("constituency", "")
                s["community"] = info.get("community", "Rum")
                s["canon_method"] = "chair_roster"
                method_counts["chair_roster"] += 1
                mappings[(raw_tr, target)] += 1
                continue

        if fk_full in ("baskan yardimcisi", "meclis reis vekili", "antiproedros") or fk_orig == "antiproedros":
            if donem in TERM_VICE_SPEAKERS:
                target = TERM_VICE_SPEAKERS[donem]
                info = canon_map.get(target, {})
                s["speaker_name"] = target
                s["speaker_role"] = "baskan"
                s["speaker_title"] = "Meclis Başkan Yardımcısı"
                s["constituency"] = info.get("constituency", "")
                s["community"] = info.get("community", "Türk")
                s["canon_method"] = "chair_roster"
                method_counts["chair_roster"] += 1
                mappings[(raw_tr, target)] += 1
                continue

        # 2. Exact cross-script alias match (Greek or Turkish)
        hit = alias_map.get(fk_tr) or alias_map.get(fk_orig) or alias_map.get(fk_full)
        if hit:
            s["speaker_name"] = hit["name"]
            if not s.get("constituency"):
                s["constituency"] = hit["constituency"]
            if not s.get("community"):
                s["community"] = hit["community"]
            method = "exact" if raw_tr == hit["name"] else "roster_alias"
            s["canon_method"] = method
            method_counts[method] += 1
            if raw_tr != hit["name"]:
                mappings[(raw_tr, hit["name"])] += 1
            continue

        # 3. Generic institutional roles (Katip, Rum Milletvekili, etc.)
        if fk_full in GENERIC_ROLES or fk_orig in GENERIC_ROLES:
            g_name, g_role, g_title = GENERIC_ROLES.get(fk_full) or GENERIC_ROLES[fk_orig]
            s["speaker_name"] = g_name
            s["speaker_role"] = g_role
            s["speaker_title"] = g_title
            if "Rum" in g_name:
                s["community"] = "Rum"
            elif "Türk" in g_name:
                s["community"] = "Türk"
            s["canon_method"] = "role_title"
            method_counts["role_title"] += 1
            continue

        # 4. High-confidence fuzzy match against official roster aliases (handles OCR/transliteration variants)
        best_score = 0
        best_info = None
        if len(fk_tr) >= 5:
            for ak, info in alias_map.items():
                if len(ak) < 5:
                    continue
                sc = fuzz.ratio(fk_tr, ak)
                if sc > best_score:
                    best_score = sc
                    best_info = info
        if best_score >= 86 and best_info is not None:
            s["speaker_name"] = best_info["name"]
            if not s.get("constituency"):
                s["constituency"] = best_info["constituency"]
            if not s.get("community"):
                s["community"] = best_info["community"]
            s["canon_method"] = "anchor_fuzzy"
            method_counts["anchor_fuzzy"] += 1
            mappings[(raw_tr, best_info["name"])] += 1
            continue

        # 5. Fallback: preserve cleaned display name
        s["speaker_name"] = cleaned or raw_tr
        s["canon_method"] = "unmatched"
        method_counts["unmatched"] += 1

    return {
        "anchors": len(canon_map),
        "method_counts": dict(method_counts),
        "top_mappings": [
            {"from": a, "to": b, "count": c}
            for (a, b), c in mappings.most_common(60)
        ],
    }
