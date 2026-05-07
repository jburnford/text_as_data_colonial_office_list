"""
COL ML Feature Engineering (Phase 2)
=====================================

Computes pairwise features for ground truth pairs directly from
COL_Official and COL_PersonRecord node properties.

CRITICAL: Features are computed fresh from node properties, NOT read from
POSSIBLE_MATCH edge properties. This ensures the ML model is independent
of the hand-tuned linker.

Input:  ml_data/ground_truth_pairs.csv (from col_build_ground_truth.py)
Output: ml_data/feature_matrix.csv (ready for col_ml_train.py)

Usage:
    python col_ml_features.py                # compute features for GT pairs
    python col_ml_features.py --stats        # report feature coverage

Requires:
    pip install neo4j
"""

import argparse
import csv
import json
import math
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

# Import domain logic from existing pipeline (read-only)
from col_link_officials import classify_domain, COMMON_SURNAMES, is_bare_member_position
from col_link_cross_colony import (
    compute_regional_proximity as _cc_regional_proximity,
    FEDERAL_PAIRS,
)
from col_normalize_names import clean_given_names

# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent

_env_file = REPO_DIR / ".env"
if _env_file.exists():
    with open(_env_file) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _key, _val = _line.split("=", 1)
                os.environ.setdefault(_key.strip(), _val.strip())

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "")

ML_DIR = REPO_DIR / "ml_data"
GT_PAIRS_FILE = ML_DIR / "ground_truth_pairs.csv"
FEATURE_MATRIX_FILE = ML_DIR / "feature_matrix.csv"

# =============================================================================
# SENIORITY CLASSIFICATION
# =============================================================================

SENIORITY_KEYWORDS = {
    "senior": {
        "governor", "chief justice", "chief secretary", "colonial secretary",
        "attorney-general", "attorney general", "administrator",
        "high commissioner", "resident", "commander",
    },
    "mid": {
        "secretary", "commissioner", "registrar", "judge", "treasurer",
        "auditor", "director", "inspector-general", "surveyor-general",
        "postmaster-general", "comptroller", "puisne",
    },
    "junior": {
        "assistant", "deputy", "clerk", "cadet", "junior",
        "probationer", "acting", "writer", "apprentice",
    },
}


def classify_seniority(position):
    """Classify position into senior/mid/junior."""
    if not position:
        return "unknown"
    pos_lower = position.lower()
    for level in ("senior", "mid", "junior"):
        for kw in SENIORITY_KEYWORDS[level]:
            if kw in pos_lower:
                return level
    return "unknown"


def compute_seniority_direction(a_pos, b_pos):
    """Compute career direction from a (earlier) to b (later)."""
    a_level = classify_seniority(a_pos)
    b_level = classify_seniority(b_pos)
    levels = {"junior": 0, "mid": 1, "senior": 2, "unknown": -1}
    if a_level == "unknown" or b_level == "unknown":
        return "unknown"
    if levels[b_level] > levels[a_level]:
        return "promotion"
    elif levels[b_level] == levels[a_level]:
        return "lateral"
    else:
        return "demotion"


# =============================================================================
# ACTING DETECTION (plan amendment #2)
# =============================================================================

_ACTING_PATTERNS = re.compile(
    r"\b(?:acting|ag\.|officiating|temporary|temp\.)\b", re.IGNORECASE
)


def is_acting(position):
    """Detect if a position is an acting/temporary appointment."""
    if not position:
        return False
    return bool(_ACTING_PATTERNS.search(position))


# =============================================================================
# HONOURS LOGIC
# =============================================================================

HONOUR_RANKS = {
    "M.B.E.": 1, "O.B.E.": 2, "C.B.E.": 3, "K.B.E.": 4, "G.B.E.": 5,
    "C.M.G.": 1, "K.C.M.G.": 2, "G.C.M.G.": 3,
    "C.B.": 1, "K.C.B.": 2, "G.C.B.": 3,
    "C.V.O.": 1, "K.C.V.O.": 2, "G.C.V.O.": 3,
    "C.I.E.": 1, "K.C.I.E.": 2, "G.C.I.E.": 3,
    "C.S.I.": 1, "K.C.S.I.": 2, "G.C.S.I.": 3,
    "D.S.O.": 1, "M.C.": 1, "D.C.M.": 1,
    "Kt.": 4,
}

_HONOUR_PATTERN = re.compile(
    r"(?:K\.?C\.?M\.?G|G\.?C\.?M\.?G|C\.?M\.?G|"
    r"K\.?C\.?B|G\.?C\.?B|C\.?B(?:\.?E)?|"
    r"K\.?B\.?E|G\.?B\.?E|O\.?B\.?E|M\.?B\.?E|"
    r"K\.?C\.?V\.?O|G\.?C\.?V\.?O|C\.?V\.?O|"
    r"K\.?C\.?I\.?E|G\.?C\.?I\.?E|C\.?I\.?E|"
    r"K\.?C\.?S\.?I|G\.?C\.?S\.?I|C\.?S\.?I|"
    r"D\.?S\.?O|M\.?C|D\.?C\.?M|Kt)\.?"
)


def extract_honours(text):
    """Extract standardized honour abbreviations from text."""
    if not text:
        return set()
    return set(_HONOUR_PATTERN.findall(text))


def compute_honours_features(a_honours_text, b_honours_text):
    """Compute honour-related features including the ratchet.

    Returns dict with:
        honours_match: exact/partial/none/unknown/mismatch
        honours_ratchet: True if B (later) lost honours A had (strong negative)
        honours_upgrade: True if B has expected upgrade of A's honours
    """
    a_set = extract_honours(a_honours_text)
    b_set = extract_honours(b_honours_text)

    if not a_set and not b_set:
        return {"honours_match": "none", "honours_ratchet": False, "honours_upgrade": False}
    if not a_set or not b_set:
        return {"honours_match": "unknown", "honours_ratchet": False, "honours_upgrade": False}
    if a_set == b_set:
        return {"honours_match": "exact", "honours_ratchet": False, "honours_upgrade": False}

    a_only = a_set - b_set
    b_only = b_set - a_set
    shared = a_set & b_set

    upgrades_found = False
    unexplained_loss = False

    for a_hon in a_only:
        found_upgrade = False
        for b_hon in b_only:
            a_rank = HONOUR_RANKS.get(a_hon, 0)
            b_rank = HONOUR_RANKS.get(b_hon, 0)
            a_base = re.sub(r"^[KG]\.?C\.?", "C.", a_hon)
            b_base = re.sub(r"^[KG]\.?C\.?", "C.", b_hon)
            if a_base == b_base and b_rank > a_rank:
                found_upgrade = True
                upgrades_found = True
                break
        if not found_upgrade:
            unexplained_loss = True

    match = "partial" if shared else "mismatch"
    if upgrades_found and not unexplained_loss:
        match = "exact"

    return {
        "honours_match": match,
        "honours_ratchet": unexplained_loss,
        "honours_upgrade": upgrades_found,
    }


# =============================================================================
# DOMAIN MATCHING
# =============================================================================

def compute_domain_match(a_position, a_dept, b_position, b_dept):
    """Compute domain match between two officials' positions."""
    a_domain = classify_domain(a_position, a_dept)
    b_domain = classify_domain(b_position, b_dept)

    if a_domain is None or b_domain is None:
        return "unknown"
    if a_domain == b_domain:
        return "exact"

    pair = frozenset({a_domain, b_domain})
    PLAUSIBLE = {
        frozenset({"EXECUTIVE", d}) for d in [
            "LEGAL", "CLERICAL", "LEGISLATIVE", "SURVEY", "MILITARY",
            "POLICE_PRISONS", "FINANCE", "EDUCATION", "WORKS", "AGRICULTURE",
        ]
    } | {
        frozenset({"LEGAL", "LEGISLATIVE"}),
        frozenset({"LEGAL", "CLERICAL"}),
        frozenset({"SURVEY", "WORKS"}),
        frozenset({"SURVEY", "AGRICULTURE"}),
        frozenset({"POLICE_PRISONS", "MILITARY"}),
        frozenset({"POSTAL_COMMS", "CLERICAL"}),
    }
    if pair in PLAUSIBLE:
        return "plausible"
    return "implausible"


# =============================================================================
# EXCLUSION RULES
# =============================================================================


def _is_bare_member(official_data):
    """Return True if this official's only positions are bare legislative titles."""
    for key in ("first_position", "last_position"):
        pos = official_data.get(key) or ""
        if pos.strip() and not is_bare_member_position(pos):
            return False  # has at least one substantive position
    # Both positions are empty or bare-member — check at least one IS a member
    return (is_bare_member_position(official_data.get("first_position") or "")
            or is_bare_member_position(official_data.get("last_position") or ""))


# =============================================================================
# LOAD OFFICIAL DATA FROM NEO4J
# =============================================================================

def load_official_data(driver, official_ids):
    """Load properties for a set of officials from COL_Official + PersonRecords.

    For each official, fetches the boundary PersonRecords (first and last year)
    to get position, department, honours at career start and end.

    Returns dict: {official_id: {properties...}}
    """
    officials = {}

    query = """
    UNWIND $ids AS oid
    MATCH (o:COL_Official {id: oid})
    OPTIONAL MATCH (pr_first:COL_PersonRecord)-[:RECORD_OF]->(o)
        WHERE pr_first.year = o.first_year
    OPTIONAL MATCH (pr_last:COL_PersonRecord)-[:RECORD_OF]->(o)
        WHERE pr_last.year = o.last_year
    RETURN o.id AS id,
           o.name AS name,
           o.colony AS colony,
           o.first_year AS first_year,
           o.last_year AS last_year,
           o.num_editions AS num_editions,
           pr_first.position_raw AS first_position,
           pr_first.department_raw AS first_department,
           pr_first.honors AS first_honours,
           pr_first.salary_min AS first_salary_min,
           pr_first.salary_max AS first_salary_max,
           pr_last.position_raw AS last_position,
           pr_last.department_raw AS last_department,
           pr_last.honors AS last_honours,
           pr_last.salary_min AS last_salary_min,
           pr_last.salary_max AS last_salary_max
    """

    id_list = list(official_ids)
    BATCH_SIZE = 500
    for i in range(0, len(id_list), BATCH_SIZE):
        batch = id_list[i:i + BATCH_SIZE]
        with driver.session() as session:
            result = session.run(query, ids=batch)
            for record in result:
                officials[record["id"]] = dict(record)

    return officials


# =============================================================================
# FEATURE COMPUTATION
# =============================================================================

NAME_SPECIFICITY_ORD = {"high": 2, "medium": 1, "low": 0}
DOMAIN_MATCH_ORD = {"exact": 4, "overlap": 3, "plausible": 2, "unknown": 1, "implausible": 0}
HONOURS_MATCH_ORD = {"exact": 4, "partial": 3, "none": 2, "unknown": 1, "mismatch": 0}
REGIONAL_PROXIMITY_ORD = {"circuit": 3, "same": 2, "adjacent": 1, "distant": 0}
SENIORITY_DIRECTION_ORD = {"promotion": 3, "lateral": 2, "unknown": 1, "demotion": 0}

FEATURE_COLS = [
    # Structural
    "gap_years", "overlap_years", "time_decay",
    "a_editions", "b_editions",
    "same_colony",
    # Name
    "name_specificity", "name_exact_match",
    # Career
    "domain_match", "seniority_direction", "seniority_direction_no_acting",
    # Honours
    "honours_match", "honours_ratchet", "honours_upgrade",
    # Acting
    "is_acting_a", "is_acting_b", "acting_pair",
    # Geographic
    "regional_proximity",
    # Federal
    "is_federal_pair",
]


def compute_name_specificity(name):
    """Classify name specificity: high (2+ initials), medium, low."""
    if not name or "," not in name:
        return "low"
    surname, given = name.split(",", 1)
    surname = surname.strip().lower()
    given_clean = clean_given_names(given.strip())
    tokens = given_clean.split() if given_clean else []

    if len(tokens) >= 2:
        return "high"
    elif len(tokens) == 1:
        return "low" if surname in COMMON_SURNAMES else "medium"
    return "low"


def compute_features(a_data, b_data):
    """Compute all features for an (a, b) pair of officials.

    a should be the earlier official (first_year <= b.first_year).
    """
    features = {}

    # --- Structural ---
    a_last = a_data.get("last_year") or 0
    b_first = b_data.get("first_year") or 0

    gap = b_first - a_last
    features["gap_years"] = max(0, gap)
    features["overlap_years"] = max(0, -gap) if gap < 0 else 0
    features["time_decay"] = math.exp(-max(0, gap) / 10.0)
    features["a_editions"] = a_data.get("num_editions") or 1
    features["b_editions"] = b_data.get("num_editions") or 1
    features["same_colony"] = 1 if a_data.get("colony") == b_data.get("colony") else 0

    # --- Name ---
    a_name = a_data.get("name", "")
    b_name = b_data.get("name", "")
    features["name_specificity"] = NAME_SPECIFICITY_ORD.get(
        compute_name_specificity(a_name), 0)
    features["name_exact_match"] = 1 if a_name == b_name else 0

    # --- Career ---
    a_last_pos = a_data.get("last_position") or ""
    a_last_dept = a_data.get("last_department") or ""
    b_first_pos = b_data.get("first_position") or ""
    b_first_dept = b_data.get("first_department") or ""

    dm = compute_domain_match(a_last_pos, a_last_dept, b_first_pos, b_first_dept)
    features["domain_match"] = DOMAIN_MATCH_ORD.get(dm, 1)

    sd = compute_seniority_direction(a_last_pos, b_first_pos)
    features["seniority_direction"] = SENIORITY_DIRECTION_ORD.get(sd, 1)

    # Seniority ignoring acting stints (plan amendment #2)
    a_is_acting = is_acting(a_last_pos)
    b_is_acting = is_acting(b_first_pos)
    if a_is_acting or b_is_acting:
        a_pos_for_sen = (a_data.get("first_position") or "") if a_is_acting else a_last_pos
        b_pos_for_sen = (b_data.get("last_position") or "") if b_is_acting else b_first_pos
        sd_no_acting = compute_seniority_direction(a_pos_for_sen, b_pos_for_sen)
    else:
        sd_no_acting = sd
    features["seniority_direction_no_acting"] = SENIORITY_DIRECTION_ORD.get(sd_no_acting, 1)

    # --- Honours ---
    a_honours = a_data.get("last_honours") or ""
    b_honours = b_data.get("first_honours") or ""
    if isinstance(a_honours, list):
        a_honours = " ".join(a_honours)
    if isinstance(b_honours, list):
        b_honours = " ".join(b_honours)
    hon = compute_honours_features(a_honours, b_honours)
    features["honours_match"] = HONOURS_MATCH_ORD.get(hon["honours_match"], 1)
    features["honours_ratchet"] = 1 if hon["honours_ratchet"] else 0
    features["honours_upgrade"] = 1 if hon["honours_upgrade"] else 0

    # --- Acting ---
    features["is_acting_a"] = 1 if a_is_acting else 0
    features["is_acting_b"] = 1 if b_is_acting else 0
    features["acting_pair"] = 1 if (a_is_acting or b_is_acting) else 0

    # --- Geographic ---
    a_colony = a_data.get("colony", "")
    b_colony = b_data.get("colony", "")
    if a_colony == b_colony:
        features["regional_proximity"] = REGIONAL_PROXIMITY_ORD["same"]
    else:
        rp = _cc_regional_proximity(a_colony, b_colony)
        features["regional_proximity"] = REGIONAL_PROXIMITY_ORD.get(rp, 0)

    # Federal pair
    features["is_federal_pair"] = 1 if frozenset({a_colony, b_colony}) in FEDERAL_PAIRS else 0

    return features


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Compute ML features for ground truth pairs")
    parser.add_argument("--stats", action="store_true", help="Report feature coverage only")
    args = parser.parse_args()

    if not NEO4J_PASSWORD:
        print("ERROR: Set NEO4J_PASSWORD environment variable")
        sys.exit(1)

    # 1. Load ground truth pairs
    print("1. Loading ground truth pairs...")
    pairs = []
    with open(GT_PAIRS_FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            pairs.append(row)
    n_pos = sum(1 for p in pairs if p["label"] == "1")
    n_neg = sum(1 for p in pairs if p["label"] == "0")
    print(f"  {len(pairs)} pairs ({n_pos} positive, {n_neg} negative)")

    # 2. Collect unique official IDs
    all_ids = set()
    for pair in pairs:
        all_ids.add(pair["official_a"])
        all_ids.add(pair["official_b"])
    print(f"  {len(all_ids)} unique officials")

    # 3. Load official data
    print("\n2. Loading official data from Neo4j...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        officials = load_official_data(driver, all_ids)
    finally:
        driver.close()

    loaded = sum(1 for v in officials.values() if v.get("name"))
    print(f"  Loaded {loaded}/{len(all_ids)} officials")
    missing = all_ids - set(officials.keys())
    if missing:
        print(f"  WARNING: {len(missing)} missing:")
        for m in list(missing)[:5]:
            print(f"    {m}")

    # 4. Compute features
    print("\n3. Computing features...")
    rows = []
    skipped = 0
    excluded_member = 0
    for pair in pairs:
        a_id = pair["official_a"]
        b_id = pair["official_b"]
        a_data = officials.get(a_id)
        b_data = officials.get(b_id)

        if not a_data or not b_data:
            skipped += 1
            continue

        # Exclude bare legislative members (MPs, Senators) — too noisy for
        # career linking and this data is available from parliamentary sources.
        if _is_bare_member(a_data) or _is_bare_member(b_data):
            excluded_member += 1
            continue

        # Ensure a is the earlier official
        if (a_data.get("first_year") or 0) > (b_data.get("first_year") or 0):
            a_data, b_data = b_data, a_data
            a_id, b_id = b_id, a_id

        features = compute_features(a_data, b_data)
        features["official_a"] = a_id
        features["official_b"] = b_id
        features["label"] = int(pair["label"])
        features["source"] = pair.get("source", "")
        features["pair_type"] = pair.get("pair_type", "")
        rows.append(features)

    if skipped:
        print(f"  Skipped {skipped} pairs (missing official data)")
    if excluded_member:
        print(f"  Excluded {excluded_member} pairs (bare legislative member)")
    print(f"  Computed features for {len(rows)} pairs")

    # 5. Write feature matrix
    print("\n4. Writing feature matrix...")
    fieldnames = ["official_a", "official_b", "label", "source", "pair_type"] + FEATURE_COLS
    with open(FEATURE_MATRIX_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})
    print(f"  Wrote {len(rows)} rows to {FEATURE_MATRIX_FILE}")

    # Print feature stats
    _print_feature_stats(rows)


def _print_feature_stats(rows):
    """Print summary statistics for the feature matrix."""
    if not rows:
        print("  No data.")
        return

    pos = [r for r in rows if r["label"] == 1]
    neg = [r for r in rows if r["label"] == 0]

    print(f"\n  Feature summary ({len(pos)} positive, {len(neg)} negative):")
    for col in FEATURE_COLS:
        vals_pos = [float(r[col]) for r in pos if col in r and r[col] != ""]
        vals_neg = [float(r[col]) for r in neg if col in r and r[col] != ""]
        if vals_pos and vals_neg:
            avg_p = sum(vals_pos) / len(vals_pos)
            avg_n = sum(vals_neg) / len(vals_neg)
            print(f"    {col:35s}  pos={avg_p:6.2f}  neg={avg_n:6.2f}  "
                  f"delta={avg_p - avg_n:+.2f}")


if __name__ == "__main__":
    main()
