#!/usr/bin/env python3
"""
COL Stage 5: Wikidata Anchoring
================================

Links COL_Official nodes to WD_Person nodes via SAME_AS relationships,
creating ground-truth identity anchors.

Matching strategy:
  1. Extract surname from WD_Person name (last word, or after comma)
  2. Match against COL_Official surname with Mac/Mc/M' normalization
  3. Check temporal overlap (WD position dates vs COL edition years)
  4. Score candidates on name match, colony match, date overlap, honours
  5. Create SAME_AS edges for high-confidence matches

Design principle: Under-link rather than over-link. Only create SAME_AS
for matches where evidence is overwhelming.

Usage:
    python col_link_wikidata.py                # full run
    python col_link_wikidata.py --dry-run      # preview, no writes
    python col_link_wikidata.py --stats        # report
    python col_link_wikidata.py --clear        # remove SAME_AS edges
    python col_link_wikidata.py --colony X     # single colony
    python col_link_wikidata.py --threshold N  # min score (default 0.70)

Requires:
    pip install neo4j
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

# Reuse domain classifier from Stage 4a
from col_link_officials import classify_domain, compute_name_specificity, COMMON_SURNAMES


# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
SCORE_VERSION = "5.0"
BATCH_SIZE = 500

# Matching thresholds
DEFAULT_THRESHOLD = 0.70   # minimum confidence to create SAME_AS
HIGH_CONFIDENCE = 0.90     # auto-accept threshold


def _load_dotenv():
    """Load .env file from repo root."""
    env_path = REPO_DIR / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())


_load_dotenv()

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "")


# =============================================================================
# NAME PARSING AND NORMALIZATION
# =============================================================================

# Mac/Mc/M' normalization for surname comparison
_MC_PATTERN = re.compile(r"^(ma?c|m')[- ]?", re.IGNORECASE)

# Title/honour stripping for WD names
_TITLE_PREFIXES = re.compile(
    r"^(sir|dame|lord|lady|hon\.?|rev\.?|ven\.?|rt\.?\s*hon\.?|"
    r"field\s*marshal|general|lieutenant[- ]general|major[- ]general|"
    r"brigadier[- ]general|brigadier|colonel|captain|major|"
    r"lieutenant|admiral|commodore|air\s*marshal)\s+",
    re.IGNORECASE
)

# Ordinal suffixes in names: "7th Earl of Jersey"
_ORDINAL_SUFFIX = re.compile(
    r",?\s*\d+(?:st|nd|rd|th)\s+(?:earl|baron|viscount|marquess|duke|"
    r"count|baronet)\s+(?:of\s+\w+)?", re.IGNORECASE
)


def normalize_surname(surname: str) -> str:
    """Normalize a surname for comparison, handling Mac/Mc/M' variants."""
    s = surname.lower().strip().rstrip(",")
    # Mac/Mc/M' → "mac"
    s = _MC_PATTERN.sub("mac", s)
    # Remove hyphens for compound names
    s = s.replace("-", "").replace("'", "").replace("'", "")
    return s


def parse_wd_name(full_name: str) -> tuple[str, str]:
    """Parse a Wikidata-style name into (surname, given_names).

    WD names are typically "Given Surname" or "Given Middle Surname".
    Some have "Surname, Given" format (483 out of 34594).
    """
    name = full_name.strip()

    # Strip titles
    name = _TITLE_PREFIXES.sub("", name).strip()

    # Strip ordinal suffixes like "7th Earl of Jersey"
    name = _ORDINAL_SUFFIX.sub("", name).strip()

    # If comma-separated, assume "Surname, Given"
    if ", " in name:
        parts = name.split(", ", 1)
        return parts[0].strip(), parts[1].strip()

    # Otherwise "Given ... Surname" — last word is surname
    words = name.split()
    if not words:
        return "", ""
    if len(words) == 1:
        return words[0], ""

    # Handle "van der X", "de la X" etc. — take last word as surname
    # but keep prefixes like "von", "de", "van" with the surname
    lower_prefixes = {"van", "von", "de", "du", "di", "le", "la", "el",
                      "al", "bin", "ibn", "den", "der", "ter", "ten"}
    surname_parts = [words[-1]]
    i = len(words) - 2
    while i >= 1 and words[i].lower() in lower_prefixes:
        surname_parts.insert(0, words[i])
        i -= 1
    surname = " ".join(surname_parts)
    given = " ".join(words[:i + 1])
    return surname, given


def parse_col_name(col_name: str) -> tuple[str, str]:
    """Parse a COL-style name 'Surname, Given' into (surname, given_names)."""
    if ", " in col_name:
        parts = col_name.split(", ", 1)
        return parts[0].strip(), parts[1].strip()
    return col_name.strip(), ""


def _tokens_compatible(tokens_a: list[str], tokens_b: list[str]) -> tuple[int, int]:
    """Compare two token lists position-by-position. Returns (matched, mismatched)."""
    matched = mismatched = 0
    for i in range(min(len(tokens_a), len(tokens_b))):
        a = tokens_a[i].rstrip(".").lower()
        b = tokens_b[i].rstrip(".").lower()
        if a == b:
            matched += 1
        elif len(a) == 1 or len(b) == 1:
            if a[0] == b[0]:
                matched += 1
            else:
                mismatched += 1
        else:
            mismatched += 1
    return matched, mismatched


def initials_match(wd_given: str, col_given: str) -> str:
    """Check if given names are compatible.

    Handles cases where WD uses middle name as primary:
    e.g. WD "Gordon" vs COL "F. Gordon" — "Gordon" matches COL token [1].

    Returns: 'exact', 'initial_compatible', 'partial', 'bare', or 'mismatch'.
    """
    if not wd_given or not col_given:
        return "bare"

    wd_tokens = re.findall(r"[A-Za-z]+\.?", wd_given)
    col_tokens = re.findall(r"[A-Za-z]+\.?", col_given)

    if not wd_tokens or not col_tokens:
        return "bare"

    # Full name match
    wd_full = " ".join(t.rstrip(".").lower() for t in wd_tokens)
    col_full = " ".join(t.rstrip(".").lower() for t in col_tokens)
    if wd_full == col_full:
        return "exact"

    # Strategy 1: Position-by-position comparison
    matched, mismatched = _tokens_compatible(wd_tokens, col_tokens)

    # Strategy 2: WD tokens as subset of COL tokens (WD may skip first name)
    # e.g. WD "Gordon" vs COL "F. Gordon" — try aligning "Gordon" at COL[1]
    if mismatched > 0 and len(wd_tokens) < len(col_tokens):
        for offset in range(1, len(col_tokens) - len(wd_tokens) + 1):
            m2, mm2 = _tokens_compatible(wd_tokens, col_tokens[offset:])
            if mm2 < mismatched or (mm2 == mismatched and m2 > matched):
                matched, mismatched = m2, mm2

    # Strategy 3: COL tokens as subset of WD tokens (COL may have only initials)
    # e.g. WD "Frederick Gordon" vs COL "F." — try each WD token
    if mismatched > 0 and len(col_tokens) < len(wd_tokens):
        for offset in range(1, len(wd_tokens) - len(col_tokens) + 1):
            m2, mm2 = _tokens_compatible(wd_tokens[offset:], col_tokens)
            if mm2 < mismatched or (mm2 == mismatched and m2 > matched):
                matched, mismatched = m2, mm2

    if mismatched > 0:
        return "mismatch"
    if matched >= 2:
        return "exact"
    if matched == 1:
        return "initial_compatible"
    return "partial"


# =============================================================================
# TEMPORAL OVERLAP
# =============================================================================

def parse_year_from_date(date_str: str | None) -> int | None:
    """Extract year from a date string like '1883-03-30' or '1883'."""
    if not date_str:
        return None
    m = re.match(r"(\d{4})", str(date_str))
    return int(m.group(1)) if m else None


def compute_temporal_overlap(
    wd_positions: list[dict],
    col_first_year: int,
    col_last_year: int,
    col_colony: str,
    territory_qid_map: dict[str, str],
) -> tuple[float, list[dict]]:
    """Score temporal overlap between WD positions and a COL stint.

    Returns (overlap_score, matching_positions).
    overlap_score: 0.0 (no overlap) to 1.0 (perfect match).
    """
    col_colony_qid = territory_qid_map.get(col_colony, "")
    matching = []

    for pos in wd_positions:
        start_year = parse_year_from_date(pos.get("start"))
        end_year = parse_year_from_date(pos.get("end"))

        # Check colony match via QID
        pos_colony_qid = pos.get("colony_qid", "")
        pos_colony_name = (pos.get("colony_name") or "").lower()

        colony_match = False
        if pos_colony_qid and col_colony_qid and pos_colony_qid == col_colony_qid:
            colony_match = True
        elif pos_colony_name and (col_colony.lower() in pos_colony_name
                                  or pos_colony_name in col_colony.lower()):
            colony_match = True
        # Check position label for colony name (minimum 4 chars to avoid false matches)
        elif len(col_colony) >= 4:
            pos_label = (pos.get("position_label") or "").lower()
            if pos_label and col_colony.lower() in pos_label:
                colony_match = True

        if not colony_match:
            continue

        # Check temporal overlap
        if start_year is None and end_year is None:
            # No dates — colony match alone is weak signal
            matching.append({"pos": pos, "overlap_years": 0, "colony_match": True})
            continue

        wd_start = start_year or (end_year - 5 if end_year else col_first_year)
        wd_end = end_year or (start_year + 10 if start_year else col_last_year)

        overlap_start = max(wd_start, col_first_year)
        overlap_end = min(wd_end, col_last_year)
        overlap = max(0, overlap_end - overlap_start + 1)

        if overlap > 0 or abs(wd_start - col_last_year) <= 3 or abs(wd_end - col_first_year) <= 3:
            matching.append({
                "pos": pos,
                "overlap_years": overlap,
                "colony_match": True,
                "wd_start": wd_start,
                "wd_end": wd_end,
            })

    if not matching:
        return 0.0, []

    # Best overlap
    max_overlap = max(m.get("overlap_years", 0) for m in matching)
    col_span = col_last_year - col_first_year + 1

    if max_overlap >= col_span:
        return 1.0, matching
    elif max_overlap > 0:
        return min(1.0, max_overlap / max(1, col_span)), matching
    else:
        # Colony match but no temporal data / near-miss
        return 0.3, matching


# =============================================================================
# CONFIDENCE SCORING
# =============================================================================

def compute_match_confidence(
    name_match: str,          # exact/initial_compatible/partial/bare/mismatch
    temporal_score: float,    # 0.0-1.0
    col_name_specificity: str,  # high/medium/low
    wd_has_birth: bool,
    wd_has_death: bool,
    col_editions: int,
    matching_positions: list[dict],
    honours_match: str,       # exact/partial/none/mismatch
) -> float:
    """Compute confidence score for a WD↔COL match.

    Returns 0.0-1.0 where higher = more confident this is the same person.
    """
    if name_match == "mismatch":
        return 0.0

    # Base from name match quality
    base = {
        "exact": 0.50,
        "initial_compatible": 0.35,
        "partial": 0.20,
        "bare": 0.10,
    }.get(name_match, 0.0)

    # Temporal overlap bonus (up to +0.35)
    temporal_bonus = temporal_score * 0.35

    # Name specificity modifier
    name_mod = {
        "high": 0.10,
        "medium": 0.0,
        "low": -0.15,
    }.get(col_name_specificity, 0.0)

    # Multiple matching positions = stronger signal
    n_matches = len(matching_positions)
    multi_match_bonus = min(0.10, (n_matches - 1) * 0.05) if n_matches > 1 else 0.0

    # Biographical data bonus
    bio_bonus = 0.0
    if wd_has_birth:
        bio_bonus += 0.03
    if wd_has_death:
        bio_bonus += 0.02

    # Tenure bonus — longer COL stints = more distinctive
    tenure_bonus = min(0.08, col_editions * 0.01)

    # Honours match
    honours_mod = {
        "exact": 0.10,
        "partial": 0.05,
        "none": 0.0,
        "mismatch": -0.10,
    }.get(honours_match, 0.0)

    confidence = (base + temporal_bonus + name_mod + multi_match_bonus
                  + bio_bonus + tenure_bonus + honours_mod)
    return round(max(0.0, min(1.0, confidence)), 3)


# =============================================================================
# HONOURS COMPARISON
# =============================================================================

# Map common WD honour QIDs to COL honour abbreviations
WD_HONOUR_TO_COL = {
    "Q12177423": "G.C.M.G.",
    "Q12177415": "K.C.M.G.",
    "Q12177413": "C.M.G.",
    "Q93710": "C.I.E.",      # Order of Indian Empire
    "Q1330936": "C.S.I.",    # Order of Star of India
    "Q1810753": "I.S.O.",    # Imperial Service Order
    "Q186748": "K.C.B.",     # Knight Commander of the Bath
    "Q10762767": "C.B.",     # Companion of the Bath
    "Q11179145": "G.C.B.",   # Knight Grand Cross of the Bath
}


def extract_col_honours(records: list[dict]) -> set[str]:
    """Extract honour abbreviations from COL PersonRecords."""
    honours = set()
    for rec in records:
        h = rec.get("honours") or ""
        # Parse comma/semicolon-separated honours
        for token in re.split(r"[,;]\s*", h):
            token = token.strip().rstrip(".")
            if token and len(token) <= 20:
                honours.add(token + "." if not token.endswith(".") else token)
    return honours


def compute_honours_match_wd(wd_honour_qids: set[str], col_honours: set[str]) -> str:
    """Compare WD honours (QIDs) against COL honours (abbreviations).

    Returns: 'exact', 'partial', 'none', or 'mismatch'.
    """
    if not wd_honour_qids and not col_honours:
        return "none"
    if not wd_honour_qids or not col_honours:
        return "none"

    # Convert WD QIDs to COL abbreviations
    wd_abbrevs = set()
    for qid in wd_honour_qids:
        abbrev = WD_HONOUR_TO_COL.get(qid)
        if abbrev:
            wd_abbrevs.add(abbrev)

    if not wd_abbrevs:
        return "none"

    # Normalize COL honours for comparison
    col_normalized = set()
    for h in col_honours:
        col_normalized.add(h.upper().strip())

    wd_normalized = set()
    for h in wd_abbrevs:
        wd_normalized.add(h.upper().strip())

    shared = col_normalized & wd_normalized
    if shared:
        if len(shared) == len(wd_normalized):
            return "exact"
        return "partial"

    # Check for upgrade paths (CMG → KCMG → GCMG)
    # If one set has a higher grade, that's still compatible
    cmg_chain = ["C.M.G.", "K.C.M.G.", "G.C.M.G."]
    cb_chain = ["C.B.", "K.C.B.", "G.C.B."]

    for chain in [cmg_chain, cb_chain]:
        wd_in = [h for h in chain if h.upper() in wd_normalized]
        col_in = [h for h in chain if h.upper() in col_normalized]
        if wd_in and col_in:
            return "partial"  # Same honour family, different grade

    return "mismatch" if wd_normalized else "none"


# =============================================================================
# CANDIDATE GENERATION (NEO4J QUERIES)
# =============================================================================

FETCH_OFFICIALS_QUERY = """
MATCH (o:COL_Official)
WHERE NOT (o)-[:SAME_AS]->(:WD_Person)
OPTIONAL MATCH (pr:COL_PersonRecord)-[:RECORD_OF]->(o)
WITH o,
     collect(DISTINCT pr.honours) AS all_honours,
     collect(DISTINCT pr.position_raw) AS all_positions,
     collect(DISTINCT pr.department_raw) AS all_depts
RETURN o.id AS id, o.name AS name, o.colony AS colony,
       o.first_year AS first_year, o.last_year AS last_year,
       o.num_editions AS num_editions, o.editions AS editions,
       all_honours, all_positions, all_depts
"""

FETCH_OFFICIALS_COLONY_QUERY = """
MATCH (o:COL_Official)
WHERE o.colony = $colony AND NOT (o)-[:SAME_AS]->(:WD_Person)
OPTIONAL MATCH (pr:COL_PersonRecord)-[:RECORD_OF]->(o)
WITH o,
     collect(DISTINCT pr.honours) AS all_honours,
     collect(DISTINCT pr.position_raw) AS all_positions,
     collect(DISTINCT pr.department_raw) AS all_depts
RETURN o.id AS id, o.name AS name, o.colony AS colony,
       o.first_year AS first_year, o.last_year AS last_year,
       o.num_editions AS num_editions, o.editions AS editions,
       all_honours, all_positions, all_depts
"""

FETCH_WD_PERSONS_QUERY = """
MATCH (w:WD_Person)
WHERE w.era IN ['colonial', 'late_colonial'] OR w.era IS NULL
OPTIONAL MATCH (w)-[hp:HELD_POSITION]->(pos:WD_Position)
OPTIONAL MATCH (w)-[:RECEIVED_HONOUR]->(h:WD_Honour)
WITH w,
     collect(DISTINCT {
       position_qid: pos.qid,
       position_label: pos.label,
       start: hp.start,
       end: hp.end,
       colony_qid: hp.colony_qid,
       colony_name: hp.colony_name
     }) AS positions,
     collect(DISTINCT h.qid) AS honour_qids
RETURN w.qid AS qid, w.name AS name,
       w.birthYear AS birthYear, w.deathYear AS deathYear,
       positions, honour_qids
"""

FETCH_TERRITORY_QIDS = """
MATCH (t:COL_Territory)
WHERE t.wikidata_id IS NOT NULL
RETURN t.name AS name, t.wikidata_id AS qid
"""

EXISTING_SAME_AS_QUERY = """
MATCH (o:COL_Official)-[r:SAME_AS]->(w:WD_Person)
RETURN o.id AS official_id, w.qid AS wd_qid
"""


# =============================================================================
# CANDIDATE MATCHING
# =============================================================================

def build_wd_surname_index(wd_persons: list[dict]) -> dict[str, list[dict]]:
    """Build an index of WD persons by normalized surname."""
    index = defaultdict(list)
    for wp in wd_persons:
        surname, given = parse_wd_name(wp["name"])
        if surname:
            norm = normalize_surname(surname)
            wp["_parsed_surname"] = surname
            wp["_parsed_given"] = given
            wp["_norm_surname"] = norm
            index[norm].append(wp)
    return dict(index)


def find_candidates(
    officials: list[dict],
    wd_surname_index: dict[str, list[dict]],
    territory_qid_map: dict[str, str],
) -> list[dict]:
    """Find candidate WD↔COL pairs based on surname + temporal overlap."""
    candidates = []

    for off in officials:
        col_surname, col_given = parse_col_name(off["name"])
        norm_surname = normalize_surname(col_surname)

        wd_matches = wd_surname_index.get(norm_surname, [])
        if not wd_matches:
            continue

        col_first = off["first_year"]
        col_last = off["last_year"]
        col_colony = off["colony"]
        col_editions = off["num_editions"] or len(off.get("editions") or [])

        # Extract COL honours
        col_honours = set()
        for h in (off.get("all_honours") or []):
            if h:
                for token in re.split(r"[,;]\s*", h):
                    token = token.strip()
                    if token:
                        col_honours.add(token)

        col_name_spec = compute_name_specificity(off["name"])

        for wp in wd_matches:
            # Check given name compatibility
            name_match = initials_match(wp["_parsed_given"], col_given)
            if name_match == "mismatch":
                continue

            # Check temporal overlap
            positions = wp.get("positions") or []
            # Filter out null position entries
            positions = [p for p in positions if p.get("position_qid")]

            temporal_score, matching_positions = compute_temporal_overlap(
                positions, col_first, col_last, col_colony, territory_qid_map,
            )

            # Fallback for WD persons with no positions but with
            # birth/death dates overlapping the COL career period.
            # Only for non-low specificity names to avoid common-name spam.
            if temporal_score == 0.0 and not matching_positions:
                if col_name_spec == "low":
                    continue

                wd_birth = wp.get("birthYear")
                wd_death = wp.get("deathYear")
                if wd_birth and wd_death:
                    career_start = wd_birth + 25
                    career_end = min(wd_death, wd_birth + 65)
                    if career_start <= col_last and career_end >= col_first:
                        temporal_score = 0.30
                    else:
                        continue
                elif wd_birth and not wd_death:
                    if wd_birth + 25 <= col_last and wd_birth + 65 >= col_first:
                        temporal_score = 0.20
                    else:
                        continue
                else:
                    continue

            # Honours comparison
            wd_honour_qids = set(wp.get("honour_qids") or [])
            # Filter None values
            wd_honour_qids = {q for q in wd_honour_qids if q}
            honours_match = compute_honours_match_wd(wd_honour_qids, col_honours)

            # Compute confidence
            confidence = compute_match_confidence(
                name_match=name_match,
                temporal_score=temporal_score,
                col_name_specificity=col_name_spec,
                wd_has_birth=wp.get("birthYear") is not None,
                wd_has_death=wp.get("deathYear") is not None,
                col_editions=col_editions,
                matching_positions=matching_positions,
                honours_match=honours_match,
            )

            if confidence >= 0.30:  # pre-filter: keep plausible candidates
                candidates.append({
                    "official_id": off["id"],
                    "wd_qid": wp["qid"],
                    "confidence": confidence,
                    "name_match": name_match,
                    "temporal_score": temporal_score,
                    "honours_match": honours_match,
                    "col_name": off["name"],
                    "wd_name": wp["name"],
                    "col_colony": col_colony,
                    "col_years": f"{col_first}-{col_last}",
                    "col_name_specificity": col_name_spec,
                    "n_matching_positions": len(matching_positions),
                    "wd_birth": wp.get("birthYear"),
                    "wd_death": wp.get("deathYear"),
                })

    return candidates


def resolve_conflicts(candidates: list[dict]) -> list[dict]:
    """Resolve cases where one official matches multiple WD persons or vice versa.

    Strategy: keep only the highest-confidence match for each official,
    and only if it's significantly better than the second-best.
    """
    # Group by official
    by_official = defaultdict(list)
    for c in candidates:
        by_official[c["official_id"]].append(c)

    resolved = []
    ambiguous = 0
    for official_id, matches in by_official.items():
        if len(matches) == 1:
            resolved.append(matches[0])
            continue

        # Sort by confidence descending
        matches.sort(key=lambda m: m["confidence"], reverse=True)
        best = matches[0]
        second = matches[1]

        # Require clear winner — best must be 0.15+ above second
        if best["confidence"] - second["confidence"] >= 0.15:
            resolved.append(best)
        else:
            ambiguous += 1

    if ambiguous:
        print(f"  {ambiguous} officials had ambiguous matches (skipped)")

    # Also check: one WD person shouldn't match too many officials
    # (They might match multiple stints of the same person — that's OK)
    by_wd = defaultdict(list)
    for c in resolved:
        by_wd[c["wd_qid"]].append(c)

    final = []
    for wd_qid, matches in by_wd.items():
        if len(matches) <= 5:
            # Up to 5 stints per person is reasonable for a long career
            final.extend(matches)
        else:
            # Too many — likely a common name collision
            print(f"  WARNING: {matches[0]['wd_name']} ({wd_qid}) matched "
                  f"{len(matches)} officials — skipping all (likely collision)")

    return final


# =============================================================================
# CASCADE: VERIFY EXISTING POSSIBLE_MATCH EDGES
# =============================================================================

CASCADE_QUERY = """
// Find POSSIBLE_MATCH chains connected to Wikidata-anchored officials
MATCH (o1:COL_Official)-[:SAME_AS]->(w:WD_Person)
MATCH (o1)-[pm:POSSIBLE_MATCH]-(o2:COL_Official)
WHERE NOT (o2)-[:SAME_AS]->(:WD_Person)
RETURN o1.id AS anchored_id, o2.id AS unanchored_id,
       o1.name AS name, o1.colony AS anchored_colony,
       o2.colony AS unanchored_colony,
       o1.first_year AS a_first, o1.last_year AS a_last,
       o2.first_year AS b_first, o2.last_year AS b_last,
       pm.uncertainty AS uncertainty,
       w.qid AS wd_qid, w.name AS wd_name,
       w.birthYear AS wd_birth, w.deathYear AS wd_death
"""


def cascade_verify(driver, territory_qid_map: dict[str, str]) -> list[dict]:
    """Use Wikidata anchors to verify connected POSSIBLE_MATCH edges.

    If a COL_Official is SAME_AS a WD_Person, and that WD_Person held
    positions in the colony of a connected official, we can verify the edge.
    """
    print("\n--- CASCADE VERIFICATION ---")

    with driver.session() as session:
        result = session.run(CASCADE_QUERY)
        chains = [dict(r) for r in result]

    if not chains:
        print("  No cascade candidates found (no SAME_AS edges yet)")
        return []

    print(f"  {len(chains)} POSSIBLE_MATCH edges connected to anchored officials")

    # For each chain, check if the WD_Person's career supports the link
    verified = []
    rejected = []

    # Fetch WD person position data
    wd_qids = {c["wd_qid"] for c in chains}

    with driver.session() as session:
        wd_data = {}
        for qid in wd_qids:
            r = session.run("""
                MATCH (w:WD_Person {qid: $qid})
                OPTIONAL MATCH (w)-[hp:HELD_POSITION]->(pos:WD_Position)
                WITH w, collect({
                    position_label: pos.label,
                    start: hp.start, end: hp.end,
                    colony_qid: hp.colony_qid,
                    colony_name: hp.colony_name
                }) AS positions
                RETURN positions
            """, qid=qid)
            rec = r.single()
            if rec:
                wd_data[qid] = [p for p in rec["positions"] if p.get("position_label")]

    for chain in chains:
        wd_positions = wd_data.get(chain["wd_qid"], [])
        if not wd_positions:
            continue

        # Check: does the WD person have a position in the unanchored colony?
        unanchored_colony = chain["unanchored_colony"]
        b_first = chain["b_first"]
        b_last = chain["b_last"]

        temporal_score, matching = compute_temporal_overlap(
            wd_positions, b_first, b_last,
            unanchored_colony, territory_qid_map,
        )

        if temporal_score > 0.3:
            verified.append({
                "anchored_id": chain["anchored_id"],
                "unanchored_id": chain["unanchored_id"],
                "wd_qid": chain["wd_qid"],
                "original_uncertainty": chain["uncertainty"],
                "verified_reason": f"WD {chain['wd_qid']} held position in {unanchored_colony}",
            })
        elif chain["uncertainty"] and chain["uncertainty"] > 0.5:
            # High uncertainty + no WD support → suspect
            rejected.append(chain)

    print(f"  Verified: {len(verified)} edges (WD career supports the link)")
    print(f"  Suspect: {len(rejected)} edges (high uncertainty, no WD support)")

    return verified


# =============================================================================
# WRITE TO NEO4J
# =============================================================================

SAME_AS_MERGE_QUERY = """
UNWIND $batch AS rec
MATCH (o:COL_Official {id: rec.official_id})
MATCH (w:WD_Person {qid: rec.wd_qid})
MERGE (o)-[r:SAME_AS]->(w)
SET r.confidence = rec.confidence,
    r.method = 'automated_wikidata_linking',
    r.score_version = $score_version,
    r.name_match = rec.name_match,
    r.temporal_score = rec.temporal_score,
    r.honours_match = rec.honours_match,
    r.n_matching_positions = rec.n_matching_positions,
    r.date_created = $date_created
RETURN count(r) AS c
"""

CASCADE_VERIFY_QUERY = """
UNWIND $batch AS rec
MATCH (a:COL_Official {id: rec.anchored_id})-[pm:POSSIBLE_MATCH]-(b:COL_Official {id: rec.unanchored_id})
SET pm.verified_by = 'wikidata_cascade',
    pm.verified_date = $date_created,
    pm.verified_wd_qid = rec.wd_qid,
    pm.uncertainty = CASE
        WHEN pm.uncertainty > 0.10 THEN pm.uncertainty * 0.5
        ELSE pm.uncertainty
    END
RETURN count(pm) AS c
"""

CASCADE_SAME_AS_QUERY = """
UNWIND $batch AS rec
MATCH (o:COL_Official {id: rec.unanchored_id})
MATCH (w:WD_Person {qid: rec.wd_qid})
MERGE (o)-[r:SAME_AS]->(w)
SET r.confidence = 0.80,
    r.method = 'wikidata_cascade',
    r.score_version = $score_version,
    r.date_created = $date_created
RETURN count(r) AS c
"""


def write_same_as(session, matches: list[dict]) -> int:
    """Write SAME_AS edges in batches."""
    total = 0
    today = date.today().isoformat()
    for i in range(0, len(matches), BATCH_SIZE):
        batch = matches[i:i + BATCH_SIZE]
        r = session.run(SAME_AS_MERGE_QUERY, batch=batch,
                        score_version=SCORE_VERSION, date_created=today)
        total += r.single()["c"]
    return total


def write_cascade_verifications(session, verified: list[dict]) -> int:
    """Update verified POSSIBLE_MATCH edges and create cascade SAME_AS."""
    today = date.today().isoformat()
    total_verified = 0
    total_same_as = 0

    for i in range(0, len(verified), BATCH_SIZE):
        batch = verified[i:i + BATCH_SIZE]
        r = session.run(CASCADE_VERIFY_QUERY, batch=batch, date_created=today)
        total_verified += r.single()["c"]

        r = session.run(CASCADE_SAME_AS_QUERY, batch=batch,
                        score_version=SCORE_VERSION, date_created=today)
        total_same_as += r.single()["c"]

    return total_verified, total_same_as


# =============================================================================
# SCHEMA
# =============================================================================

def ensure_schema(session):
    """Create indexes for SAME_AS relationships."""
    stmts = [
        "CREATE INDEX col_official_same_as IF NOT EXISTS FOR ()-[r:SAME_AS]->() ON (r.confidence)",
    ]
    for stmt in stmts:
        try:
            session.run(stmt)
        except Exception as e:
            if "already exists" not in str(e).lower():
                print(f"  WARNING: {e}")


# =============================================================================
# STATS
# =============================================================================

def print_stats(driver):
    """Report on SAME_AS edges and Wikidata anchoring."""
    with driver.session() as session:
        print("\n" + "=" * 60)
        print("WIKIDATA ANCHORING STATISTICS")
        print("=" * 60)

        # SAME_AS counts
        r = session.run(
            "MATCH ()-[r:SAME_AS]->(:WD_Person) RETURN count(r) AS c"
        ).single()
        total_same_as = r["c"]
        print(f"\n  Total SAME_AS edges: {total_same_as}")

        r = session.run(
            "MATCH (o:COL_Official)-[:SAME_AS]->(:WD_Person) "
            "RETURN count(DISTINCT o) AS officials, count(DISTINCT o.colony) AS colonies"
        ).single()
        print(f"  Unique officials anchored: {r['officials']}")
        print(f"  Across colonies: {r['colonies']}")

        if total_same_as == 0:
            print("  No SAME_AS edges yet.")
            return

        # Method breakdown
        result = session.run(
            "MATCH ()-[r:SAME_AS]->(:WD_Person) "
            "RETURN r.method AS method, count(r) AS n "
            "ORDER BY n DESC"
        )
        print("\n  By method:")
        for rec in result:
            print(f"    {rec['method']:<35} {rec['n']:>5}")

        # Confidence distribution
        print("\n  Confidence distribution:")
        result = session.run(
            "MATCH ()-[r:SAME_AS]->(:WD_Person) "
            "WITH CASE "
            "  WHEN r.confidence >= 0.9 THEN '0.90-1.00' "
            "  WHEN r.confidence >= 0.8 THEN '0.80-0.89' "
            "  WHEN r.confidence >= 0.7 THEN '0.70-0.79' "
            "  WHEN r.confidence >= 0.6 THEN '0.60-0.69' "
            "  ELSE '< 0.60' "
            "END AS bucket, count(*) AS n "
            "RETURN bucket, n ORDER BY bucket"
        )
        for rec in result:
            bar = "█" * max(1, rec["n"] * 40 // max(1, total_same_as))
            print(f"    {rec['bucket']}  {rec['n']:>5}  {bar}")

        # Top colonies
        print("\n  Top 15 colonies by anchored officials:")
        result = session.run(
            "MATCH (o:COL_Official)-[:SAME_AS]->(:WD_Person) "
            "RETURN o.colony AS colony, count(o) AS n "
            "ORDER BY n DESC LIMIT 15"
        )
        for rec in result:
            print(f"    {rec['colony']:<40} {rec['n']:>5}")

        # POSSIBLE_MATCH edges verified by cascade
        result = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH]->() "
            "WHERE r.verified_by = 'wikidata_cascade' "
            "RETURN count(r) AS n"
        ).single()
        print(f"\n  POSSIBLE_MATCH edges verified by cascade: {result['n']}")

        # Sample matches
        print("\n  Sample SAME_AS matches (highest confidence):")
        result = session.run(
            "MATCH (o:COL_Official)-[r:SAME_AS]->(w:WD_Person) "
            "RETURN o.name AS col_name, o.colony AS colony, "
            "       o.first_year AS first_year, o.last_year AS last_year, "
            "       w.name AS wd_name, w.qid AS qid, "
            "       r.confidence AS confidence "
            "ORDER BY r.confidence DESC LIMIT 10"
        )
        for rec in result:
            print(f"    {rec['confidence']:.2f}  {rec['col_name']:<30} "
                  f"({rec['colony']}, {rec['first_year']}-{rec['last_year']}) "
                  f"↔ {rec['wd_name']} ({rec['qid']})")


# =============================================================================
# DRY RUN
# =============================================================================

def dry_run_report(candidates: list[dict], threshold: float):
    """Preview matching results without writing."""
    print("\n" + "=" * 60)
    print("[DRY RUN] PREVIEW")
    print("=" * 60)

    above = [c for c in candidates if c["confidence"] >= threshold]
    below = [c for c in candidates if c["confidence"] < threshold]

    print(f"\n  Total candidates: {len(candidates)}")
    print(f"  Above threshold ({threshold:.2f}): {len(above)}")
    print(f"  Below threshold: {len(below)}")

    if not candidates:
        print("  No candidates found.")
        return

    # Confidence distribution
    buckets = defaultdict(int)
    for c in candidates:
        b = int(c["confidence"] * 10)
        b = min(b, 9)
        label = f"{b/10:.1f}0-{(b+1)/10:.1f}{'0' if b < 9 else ''}"
        buckets[label] += 1

    print("\n  Confidence distribution (all candidates):")
    for label in sorted(buckets):
        n = buckets[label]
        bar = "█" * max(1, n * 40 // len(candidates))
        print(f"    {label:<10}  {n:>5}  {bar}")

    # Name match breakdown
    nm_counts = defaultdict(int)
    for c in above:
        nm_counts[c["name_match"]] += 1
    print("\n  Name match (above threshold):")
    for nm in sorted(nm_counts, key=nm_counts.get, reverse=True):
        print(f"    {nm:<25} {nm_counts[nm]:>5}")

    # Sample high-confidence matches
    sorted_cands = sorted(above, key=lambda c: c["confidence"], reverse=True)
    n_show = min(20, len(sorted_cands))
    print(f"\n  Top {n_show} matches:")
    for c in sorted_cands[:n_show]:
        print(f"    {c['confidence']:.2f}  {c['col_name']:<30} "
              f"({c['col_colony']}, {c['col_years']}) "
              f"↔ {c['wd_name']} ({c['wd_qid']})")
        print(f"          name={c['name_match']} temporal={c['temporal_score']:.2f} "
              f"honours={c['honours_match']} positions={c['n_matching_positions']}")

    # Low-confidence near-misses
    near_miss = [c for c in below if c["confidence"] >= threshold - 0.10]
    if near_miss:
        print(f"\n  Near-misses ({threshold - 0.10:.2f}-{threshold:.2f}, "
              f"not linked):")
        for c in sorted(near_miss, key=lambda c: c["confidence"], reverse=True)[:10]:
            print(f"    {c['confidence']:.2f}  {c['col_name']:<30} "
                  f"({c['col_colony']}, {c['col_years']}) "
                  f"↔ {c['wd_name']} ({c['wd_qid']})")

    print("\n[DRY RUN] No data written.")


# =============================================================================
# CLEAR
# =============================================================================

def clear_same_as(driver):
    """Remove all SAME_AS edges between COL_Official and WD_Person."""
    with driver.session() as session:
        r = session.run(
            "MATCH (o:COL_Official)-[r:SAME_AS]->(w:WD_Person) "
            "DELETE r RETURN count(r) AS c"
        ).single()
        print(f"Deleted {r['c']} SAME_AS edges.")

        # Also clear cascade verifications
        r = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH]->() "
            "WHERE r.verified_by = 'wikidata_cascade' "
            "REMOVE r.verified_by, r.verified_date, r.verified_wd_qid "
            "RETURN count(r) AS c"
        ).single()
        print(f"Cleared {r['c']} cascade verifications from POSSIBLE_MATCH edges.")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Stage 5: Wikidata anchoring — link COL_Officials to WD_Persons"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without writing to Neo4j")
    parser.add_argument("--stats", action="store_true",
                        help="Report SAME_AS statistics")
    parser.add_argument("--clear", action="store_true",
                        help="Remove all SAME_AS edges")
    parser.add_argument("--colony", type=str,
                        help="Filter to specific colony")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD,
                        help=f"Minimum confidence for SAME_AS (default {DEFAULT_THRESHOLD})")
    parser.add_argument("--cascade", action="store_true",
                        help="Run cascade verification on POSSIBLE_MATCH edges")
    parser.add_argument("--no-cascade", action="store_true",
                        help="Skip cascade verification after linking")
    args = parser.parse_args()

    print("=" * 60)
    print("COL STAGE 5: WIKIDATA ANCHORING")
    print("=" * 60)

    # Connect
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        if args.stats:
            print_stats(driver)
            return

        if args.clear:
            clear_same_as(driver)
            return

        # --- Fetch territory QID mapping ---
        print("\nFetching territory → Wikidata QID mapping...")
        with driver.session() as session:
            ensure_schema(session)
            result = session.run(FETCH_TERRITORY_QIDS)
            territory_qid_map = {r["name"]: r["qid"] for r in result}
        print(f"  {len(territory_qid_map)} territories with Wikidata QIDs")

        if args.cascade:
            # Cascade-only mode
            verified = cascade_verify(driver, territory_qid_map)
            if verified and not args.dry_run:
                with driver.session() as session:
                    n_verified, n_same_as = write_cascade_verifications(
                        session, verified)
                print(f"  Updated {n_verified} POSSIBLE_MATCH edges")
                print(f"  Created {n_same_as} cascade SAME_AS edges")
            print_stats(driver)
            return

        # --- Fetch officials ---
        print("\nFetching COL_Official nodes...")
        with driver.session() as session:
            if args.colony:
                result = session.run(FETCH_OFFICIALS_COLONY_QUERY, colony=args.colony)
            else:
                result = session.run(FETCH_OFFICIALS_QUERY)
            officials = [dict(r) for r in result]
        print(f"  {len(officials)} officials (not yet anchored)")

        # --- Fetch WD_Person nodes ---
        print("Fetching WD_Person nodes...")
        with driver.session() as session:
            result = session.run(FETCH_WD_PERSONS_QUERY)
            wd_persons = [dict(r) for r in result]
        print(f"  {len(wd_persons)} WD_Person nodes (colonial/late_colonial era)")

        # --- Build surname index ---
        print("Building surname index...")
        wd_surname_index = build_wd_surname_index(wd_persons)
        print(f"  {len(wd_surname_index)} unique normalized surnames")

        # --- Find candidates ---
        print(f"Finding candidates (threshold={args.threshold:.2f})...")
        candidates = find_candidates(officials, wd_surname_index, territory_qid_map)
        print(f"  {len(candidates)} raw candidates (confidence >= 0.30)")

        # --- Resolve conflicts ---
        print("Resolving conflicts...")
        resolved = resolve_conflicts(candidates)
        print(f"  {len(resolved)} resolved candidates")

        # --- Apply threshold ---
        above_threshold = [c for c in resolved if c["confidence"] >= args.threshold]
        print(f"  {len(above_threshold)} above threshold ({args.threshold:.2f})")

        # --- Dry run or write ---
        if args.dry_run:
            dry_run_report(resolved, args.threshold)
            return

        if above_threshold:
            print(f"\nWriting {len(above_threshold)} SAME_AS edges...")
            with driver.session() as session:
                written = write_same_as(session, above_threshold)
            print(f"  {written} SAME_AS edges created")

        # --- Cascade verification ---
        if not args.no_cascade and above_threshold:
            verified = cascade_verify(driver, territory_qid_map)
            if verified:
                with driver.session() as session:
                    n_verified, n_same_as = write_cascade_verifications(
                        session, verified)
                print(f"  Updated {n_verified} POSSIBLE_MATCH edges")
                print(f"  Created {n_same_as} cascade SAME_AS edges")

        # --- Final stats ---
        print_stats(driver)

    finally:
        driver.close()

    print("\nDone.")


if __name__ == "__main__":
    main()
