"""
COL Stage 4c: Cross-Colony Career Linking
==========================================

Creates POSSIBLE_MATCH relationships between COL_Official stints in
DIFFERENT colonies — finding the same person moving between postings.

Cross-colony linking is inherently less certain than within-colony
(Stage 4a), so the base uncertainty is higher (0.15 vs 0.03). Signals
include name specificity, honours matching, military rank, regional
transfer circuits, career domain continuity, seniority direction, and
temporal gap analysis.

Concurrent postings (temporal overlap) are classified, not filtered:
  - Federal duplicates (St Vincent ↔ Windward Islands): identity signal
  - 1-year overlap: scored normally (neutral)
  - Multi-year overlap: heavy penalty (almost certainly different people)

Usage:
    python col_link_cross_colony.py              # full run
    python col_link_cross_colony.py --dry-run    # preview, no writes
    python col_link_cross_colony.py --stats      # report
    python col_link_cross_colony.py --clear      # remove cross-colony edges
    python col_link_cross_colony.py --colony X   # only pairs involving colony X
    python col_link_cross_colony.py --force      # recompute scores
    python col_link_cross_colony.py --max-colonies 5  # skip names in too many colonies
    python col_link_cross_colony.py --threshold 0.70  # uncertainty cutoff

Requires:
    pip install neo4j
"""

import argparse
import json
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

# Reuse domain classifier and name specificity from Stage 4a
from col_link_officials import (
    DOMAIN_KEYWORDS,
    PLAUSIBLE_TRANSITIONS,
    classify_domain,
    compute_domain_match,
    compute_name_specificity,
    COMMON_SURNAMES,
    is_bare_member_position,
)

# Reuse initial compatibility from normalization module
from col_normalize_names import initials_compatible, clean_given_names

# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
SCORE_VERSION = "3.0"
BATCH_SIZE = 500
DEFAULT_THRESHOLD = 0.70
DEFAULT_MAX_COLONIES = 5
UNCERTAINTY_FLOOR = 0.10
UNCERTAINTY_CEILING = 1.0


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
# TRANSFER CIRCUITS
# =============================================================================

TRANSFER_CIRCUITS = {
    "west_africa": {
        "Gold Coast", "Sierra Leone", "Gambia", "Nigeria", "Lagos",
        "Northern Nigeria", "Southern Nigeria", "Niger Territories",
        "Niger Coast Protectorate", "Niger Protectorate", "Togoland",
        "Cameroons", "West Africa", "West Africa Settlements",
    },
    "caribbean": {
        "Jamaica", "Trinidad", "Trinidad and Tobago", "Barbados",
        "British Guiana", "British Honduras", "Bahamas", "Bermuda",
        "Leeward Islands", "Windward Islands", "Antigua", "Montserrat",
        "St Christopher and Nevis", "Virgin Islands", "Dominica",
        "Grenada", "St Lucia", "St Vincent", "Tobago", "Nevis",
        "Turks and Caicos Islands", "Cayman Islands",
        "West Indies", "West Indies Federation",
    },
    "east_africa": {
        "Kenya", "Uganda", "Tanganyika", "Zanzibar", "Nyasaland",
        "British Somaliland", "British East Africa and Zanzibar",
        "East Africa High Commission",
    },
    "southern_africa": {
        "Northern Rhodesia", "Southern Rhodesia", "Rhodesia",
        "Federation of Rhodesia and Nyasaland",
        "Basutoland", "Bechuanaland", "British Bechuanaland", "Swaziland",
        "High Commission Territories",
        "South Africa", "Cape of Good Hope", "Natal", "Transvaal",
        "Orange River Colony", "Griqualand West", "Zululand",
    },
    "malaya": {
        "Straits Settlements", "Federated Malay States",
        "Unfederated Malay States", "Federation of Malaya", "Malaysia",
        "Singapore", "North Borneo", "Sarawak", "Brunei", "Labuan",
        "Hong Kong",
    },
    "pacific": {
        "Fiji", "Western Pacific", "Gilbert and Ellice Islands",
        "British Solomon Islands", "Tonga", "New Hebrides",
        "Cook Islands", "Pitcairn Island",
    },
    "mediterranean": {
        "Malta", "Gibraltar", "Cyprus",
    },
    "middle_east": {
        "Palestine", "Transjordan", "Aden", "Iraq", "Mesopotamia",
    },
    "indian_ocean": {
        "Ceylon", "Mauritius", "Seychelles", "Rodrigues",
        "Christmas Island",
    },
    "settler_pacific": {
        "Australia", "New Zealand", "New South Wales", "Queensland",
        "Victoria", "South Australia", "Western Australia", "Tasmania",
        "Papua", "British New Guinea", "Territory of New Guinea",
        "Norfolk Island",
    },
    "settler_atlantic": {
        "Canada", "Newfoundland", "New Brunswick", "Nova Scotia",
        "Prince Edward Island", "British Columbia", "Vancouver Island",
        "Falkland Islands", "British Antarctic Territory",
        "St Helena", "Ascension", "Tristan da Cunha",
    },
    "west_indian_federations": {
        "Leeward Islands", "Windward Islands",
        "Antigua", "Montserrat", "St Christopher and Nevis",
        "Virgin Islands", "Dominica",
        "Grenada", "St Lucia", "St Vincent", "Tobago",
    },
}

# Build colony→circuit lookup
_COLONY_TO_CIRCUIT = {}
for circuit, colonies in TRANSFER_CIRCUITS.items():
    for colony in colonies:
        _COLONY_TO_CIRCUIT.setdefault(colony, set()).add(circuit)


# =============================================================================
# FEDERAL PAIRS (known administrative double-counting)
# =============================================================================

# These are colony pairs where officials are routinely listed under both
# the sub-colony AND the federation. Detected as "federal_duplicate".
FEDERAL_PAIRS = {
    # Windward Islands federation
    frozenset({"St Vincent", "Windward Islands"}),
    frozenset({"Grenada", "Windward Islands"}),
    frozenset({"St Lucia", "Windward Islands"}),
    frozenset({"Dominica", "Windward Islands"}),
    frozenset({"Tobago", "Windward Islands"}),
    # Leeward Islands federation
    frozenset({"Antigua", "Leeward Islands"}),
    frozenset({"Montserrat", "Leeward Islands"}),
    frozenset({"St Christopher and Nevis", "Leeward Islands"}),
    frozenset({"Virgin Islands", "Leeward Islands"}),
    frozenset({"Dominica", "Leeward Islands"}),
    frozenset({"Nevis", "Leeward Islands"}),
    # West Africa — administered together
    frozenset({"Gold Coast", "Togoland"}),
    # Nigeria groupings
    frozenset({"Northern Nigeria", "Nigeria"}),
    frozenset({"Southern Nigeria", "Nigeria"}),
    frozenset({"Lagos", "Nigeria"}),
    frozenset({"Lagos", "Southern Nigeria"}),
    # Rhodesia federation
    frozenset({"Northern Rhodesia", "Federation of Rhodesia and Nyasaland"}),
    frozenset({"Southern Rhodesia", "Federation of Rhodesia and Nyasaland"}),
    frozenset({"Nyasaland", "Federation of Rhodesia and Nyasaland"}),
    # Malaya groupings
    frozenset({"Straits Settlements", "Federation of Malaya"}),
    frozenset({"Federated Malay States", "Federation of Malaya"}),
    frozenset({"Unfederated Malay States", "Federation of Malaya"}),
    frozenset({"Singapore", "Federation of Malaya"}),
    # West Indies federation
    frozenset({"Jamaica", "West Indies Federation"}),
    frozenset({"Trinidad and Tobago", "West Indies Federation"}),
    frozenset({"Barbados", "West Indies Federation"}),
    frozenset({"Windward Islands", "West Indies Federation"}),
    frozenset({"Leeward Islands", "West Indies Federation"}),
    # East Africa High Commission
    frozenset({"Kenya", "East Africa High Commission"}),
    frozenset({"Uganda", "East Africa High Commission"}),
    frozenset({"Tanganyika", "East Africa High Commission"}),
    # High Commission Territories
    frozenset({"Basutoland", "High Commission Territories"}),
    frozenset({"Bechuanaland", "High Commission Territories"}),
    frozenset({"Swaziland", "High Commission Territories"}),
    # South Africa
    frozenset({"Cape of Good Hope", "South Africa"}),
    frozenset({"Natal", "South Africa"}),
    frozenset({"Transvaal", "South Africa"}),
    frozenset({"Orange River Colony", "South Africa"}),
    # Australian federation (1901) — colony → Commonwealth
    frozenset({"New South Wales", "Australia"}),
    frozenset({"Victoria", "Australia"}),
    frozenset({"Queensland", "Australia"}),
    frozenset({"South Australia", "Australia"}),
    frozenset({"Western Australia", "Australia"}),
    frozenset({"Tasmania", "Australia"}),
    frozenset({"New South Wales", "Commonwealth Of Australia"}),
    frozenset({"Victoria", "Commonwealth Of Australia"}),
    frozenset({"Queensland", "Commonwealth Of Australia"}),
    frozenset({"South Australia", "Commonwealth Of Australia"}),
    frozenset({"Western Australia", "Commonwealth Of Australia"}),
    frozenset({"Tasmania", "Commonwealth Of Australia"}),
    # New Zealand (colony → dominion name change)
    frozenset({"New Zealand", "Dominion of New Zealand"}),
    # British Central Africa → Nyasaland (renamed 1907)
    frozenset({"British Central Africa", "Nyasaland"}),
}


def is_federal_pair(colony_a: str, colony_b: str) -> bool:
    """Check if two colonies are in a federal/administrative relationship."""
    return frozenset({colony_a, colony_b}) in FEDERAL_PAIRS


# =============================================================================
# REGIONAL PROXIMITY
# =============================================================================

def compute_regional_proximity(colony_a: str, colony_b: str) -> str:
    """Compute regional proximity between two colonies.

    Returns: 'circuit' (same named transfer circuit), 'same' (share a circuit),
             'adjacent' (circuits with some overlap), 'distant' (no shared circuits).
    """
    circuits_a = _COLONY_TO_CIRCUIT.get(colony_a, set())
    circuits_b = _COLONY_TO_CIRCUIT.get(colony_b, set())

    if not circuits_a or not circuits_b:
        return "distant"

    shared = circuits_a & circuits_b
    if shared:
        # Check for the specific named circuits (not the federation one)
        non_federation = shared - {"west_indian_federations"}
        if non_federation:
            return "circuit"
        return "same"

    # Check for adjacent circuits (e.g., east_africa and southern_africa
    # share some connections). We define adjacency as circuits that
    # historically shared personnel.
    ADJACENT_CIRCUITS = {
        frozenset({"east_africa", "southern_africa"}),
        frozenset({"east_africa", "middle_east"}),
        frozenset({"west_africa", "caribbean"}),
        frozenset({"caribbean", "settler_atlantic"}),
        frozenset({"malaya", "pacific"}),
        frozenset({"malaya", "indian_ocean"}),
        frozenset({"indian_ocean", "east_africa"}),
        frozenset({"mediterranean", "middle_east"}),
        frozenset({"mediterranean", "settler_atlantic"}),
    }

    for ca in circuits_a:
        for cb in circuits_b:
            if frozenset({ca, cb}) in ADJACENT_CIRCUITS:
                return "adjacent"

    return "distant"


# =============================================================================
# HONOURS MATCHING
# =============================================================================

# Honours ranked roughly by precedence. Used for matching.
KNOWN_HONOURS = {
    # Knight Grand Cross
    "G.C.M.G.", "G.C.B.", "G.C.V.O.", "G.C.S.I.", "G.C.I.E.", "G.B.E.",
    # Knight Commander
    "K.C.M.G.", "K.C.B.", "K.C.V.O.", "K.C.S.I.", "K.C.I.E.", "K.B.E.",
    # Commander / Companion
    "C.M.G.", "C.B.", "C.V.O.", "C.S.I.", "C.I.E.", "C.B.E.",
    # Officer / Member
    "O.B.E.", "M.B.E.", "M.V.O.",
    # Other
    "D.S.O.", "M.C.", "I.S.O.", "E.D.", "T.D.", "Q.C.", "K.C.", "Kt.",
}

# Honours that represent upgrades of the same order (not mismatches)
HONOUR_UPGRADES = {
    ("C.M.G.", "K.C.M.G."), ("K.C.M.G.", "G.C.M.G."), ("C.M.G.", "G.C.M.G."),
    ("C.B.", "K.C.B."), ("K.C.B.", "G.C.B."), ("C.B.", "G.C.B."),
    ("C.B.E.", "K.B.E."), ("K.B.E.", "G.B.E."), ("C.B.E.", "G.B.E."),
    ("O.B.E.", "C.B.E."), ("M.B.E.", "O.B.E."), ("M.B.E.", "C.B.E."),
    ("C.V.O.", "K.C.V.O."), ("K.C.V.O.", "G.C.V.O."),
    ("M.V.O.", "C.V.O."), ("M.V.O.", "K.C.V.O."),
    ("C.S.I.", "K.C.S.I."), ("K.C.S.I.", "G.C.S.I."),
    ("C.I.E.", "K.C.I.E."), ("K.C.I.E.", "G.C.I.E."),
}


def _normalize_honours(honours_list) -> set[str]:
    """Normalize honours to a comparable set."""
    if not honours_list:
        return set()
    if isinstance(honours_list, str):
        # Sometimes stored as string rather than list
        honours_list = [h.strip() for h in honours_list.split(",")]
    return {h.strip() for h in honours_list if h and h.strip()}


def compute_honours_match(a_honours, b_honours) -> str:
    """Compare honours between two stints.

    Returns: 'exact', 'partial', 'none', 'unknown', 'mismatch'.
    """
    set_a = _normalize_honours(a_honours)
    set_b = _normalize_honours(b_honours)

    if not set_a and not set_b:
        return "none"
    if not set_a or not set_b:
        return "unknown"

    if set_a == set_b:
        return "exact"

    # Check if difference is just upgrades (e.g., C.M.G. → K.C.M.G.)
    diff_a = set_a - set_b  # in A but not B
    diff_b = set_b - set_a  # in B but not A

    if not diff_a and not diff_b:
        return "exact"

    # Check if all differences are explained by upgrades
    explained = set()
    for ha in diff_a:
        for hb in diff_b:
            if (ha, hb) in HONOUR_UPGRADES or (hb, ha) in HONOUR_UPGRADES:
                explained.add(ha)
                explained.add(hb)

    unexplained_a = diff_a - explained
    unexplained_b = diff_b - explained

    if not unexplained_a and not unexplained_b:
        # All differences are upgrades — strong identity signal
        return "exact"

    # Shared honours exist
    shared = set_a & set_b
    if shared or explained:
        return "partial"

    # No shared honours and unexplained differences — possible mismatch
    return "mismatch"


# =============================================================================
# MILITARY RANK MATCHING
# =============================================================================

RANK_ORDER = {
    # Army ranks in ascending order
    "lieutenant": 1, "captain": 2, "major": 3,
    "lieutenant-colonel": 4, "colonel": 5, "brigadier": 6,
    "major-general": 7, "lieutenant-general": 8, "general": 9,
    "field marshal": 10,
    # Some naval equivalents
    "sub-lieutenant": 1, "commander": 3,
    "rear-admiral": 7, "vice-admiral": 8, "admiral": 9,
}


def compute_rank_match(a_rank: str | None, b_rank: str | None) -> str:
    """Compare military ranks between two stints.

    Returns: 'exact', 'compatible' (promotion), 'none', 'unknown', 'mismatch'.
    """
    if not a_rank and not b_rank:
        return "none"
    if not a_rank or not b_rank:
        return "unknown"

    a_lower = a_rank.lower().strip()
    b_lower = b_rank.lower().strip()

    if a_lower == b_lower:
        return "exact"

    a_ord = RANK_ORDER.get(a_lower)
    b_ord = RANK_ORDER.get(b_lower)

    if a_ord is not None and b_ord is not None:
        if b_ord >= a_ord:
            return "compatible"  # promotion or lateral
        else:
            return "mismatch"  # demotion

    return "unknown"


# =============================================================================
# SENIORITY DIRECTION
# =============================================================================

# Position keywords that suggest seniority level
SENIORITY_KEYWORDS = {
    "senior": {
        "governor", "chief justice", "chief secretary", "colonial secretary",
        "administrator", "high commissioner", "attorney-general",
        "solicitor-general", "auditor-general", "inspector-general",
        "director", "chief", "principal", "senior",
    },
    "mid": {
        "secretary", "commissioner", "registrar", "judge",
        "treasurer", "comptroller", "collector", "inspector",
        "superintendent", "engineer", "surveyor-general",
    },
    "junior": {
        "assistant", "deputy", "clerk", "cadet", "junior",
        "probationer", "acting",
    },
}


def _estimate_seniority(position: str | None) -> str | None:
    """Estimate seniority level from position text."""
    if not position:
        return None
    pos_lower = position.lower()
    for level in ["senior", "mid", "junior"]:
        for kw in SENIORITY_KEYWORDS[level]:
            if kw in pos_lower:
                return level
    return None


def compute_seniority_direction(a_position: str | None, b_position: str | None) -> str:
    """Determine seniority direction of transfer.

    Returns: 'promotion', 'lateral', 'demotion', 'unknown'.
    """
    a_sen = _estimate_seniority(a_position)
    b_sen = _estimate_seniority(b_position)

    if a_sen is None or b_sen is None:
        return "unknown"

    levels = {"junior": 0, "mid": 1, "senior": 2}
    a_lvl = levels[a_sen]
    b_lvl = levels[b_sen]

    if b_lvl > a_lvl:
        return "promotion"
    elif b_lvl == a_lvl:
        return "lateral"
    else:
        return "demotion"


# =============================================================================
# SENIORITY PROGRESSION (career ladder detection)
# =============================================================================

# Known promotion patterns: (from_keyword, to_keyword, strength)
# strength: "strong" = very distinctive identity signal, "moderate" = good signal
PROMOTION_PATTERNS = [
    # Colonial Secretary → Governor (classic promotion)
    ("colonial secretary", "governor", "strong"),
    ("chief secretary", "governor", "strong"),
    # Legal career ladder: SG → AG → CJ → Governor
    ("solicitor-general", "attorney-general", "strong"),
    ("solicitor general", "attorney-general", "strong"),
    ("solicitor-general", "attorney general", "strong"),
    ("solicitor general", "attorney general", "strong"),
    ("attorney-general", "chief justice", "strong"),
    ("attorney general", "chief justice", "strong"),
    ("attorney-general", "governor", "strong"),
    ("attorney general", "governor", "strong"),
    ("solicitor-general", "chief justice", "moderate"),
    ("solicitor general", "chief justice", "moderate"),
    ("solicitor-general", "judge", "moderate"),
    ("solicitor general", "judge", "moderate"),
    ("crown counsel", "solicitor-general", "moderate"),
    ("crown counsel", "solicitor general", "moderate"),
    ("crown counsel", "attorney-general", "moderate"),
    ("crown counsel", "attorney general", "moderate"),
    # Administrative ladder
    ("district commissioner", "provincial commissioner", "moderate"),
    ("provincial commissioner", "chief secretary", "moderate"),
    ("provincial commissioner", "colonial secretary", "moderate"),
    ("district commissioner", "colonial secretary", "moderate"),
    ("assistant colonial secretary", "colonial secretary", "moderate"),
    ("assistant secretary", "colonial secretary", "moderate"),
    # Resident Commissioner → Governor
    ("resident commissioner", "governor", "moderate"),
    ("resident", "governor", "moderate"),
    # Survey/technical → executive (Guggisberg pattern)
    ("director of surveys", "governor", "moderate"),
    ("director of public works", "governor", "moderate"),
    ("surveyor-general", "governor", "moderate"),
    ("surveyor general", "governor", "moderate"),
    # Cadet → anything senior
    ("cadet", "secretary", "moderate"),
    ("cadet", "commissioner", "moderate"),
    ("cadet", "treasurer", "moderate"),
    # Judge promotions
    ("puisne judge", "chief justice", "strong"),
    ("magistrate", "judge", "moderate"),
    ("magistrate", "puisne judge", "moderate"),
]


def compute_seniority_progression(a_position: str | None, b_position: str | None) -> str:
    """Detect known career ladder progressions between positions.

    Returns: 'strong_promotion' (very distinctive pattern like ColSec→Governor),
             'moderate_promotion' (known career ladder),
             'none' (no recognized pattern).
    """
    if not a_position or not b_position:
        return "none"

    a_lower = a_position.lower()
    b_lower = b_position.lower()

    best = "none"
    for from_kw, to_kw, strength in PROMOTION_PATTERNS:
        if from_kw in a_lower and to_kw in b_lower:
            if strength == "strong":
                return "strong_promotion"
            best = "moderate_promotion"

    return best


# =============================================================================
# CROSS-COLONY UNCERTAINTY SCORE
# =============================================================================

def compute_cross_colony_uncertainty(
    name_specificity: str,
    honours_match: str,
    rank_match: str,
    regional_proximity: str,
    domain_match: str,
    seniority_direction: str,
    seniority_progression: str,
    gap_years: int,
    overlap_years: int,
    overlap_type: str,
    colony_count: int,
    a_editions: int,
    b_editions: int,
) -> float:
    """Compute uncertainty score for a cross-colony candidate pair."""

    # 1. Base
    base = 0.15

    # 2. Name specificity (PRIMARY signal)
    name_mod = {"high": -0.10, "medium": 0.0, "low": 0.20}.get(name_specificity, 0.0)

    # 3. Honours match
    honours_mod = {
        "exact": -0.12, "partial": -0.06, "none": 0.05,
        "unknown": 0.0, "mismatch": 0.15,
    }.get(honours_match, 0.0)

    # 4. Military rank match
    rank_mod = {
        "exact": -0.06, "compatible": -0.03, "none": 0.0,
        "unknown": 0.0, "mismatch": 0.10,
    }.get(rank_match, 0.0)

    # 5. Regional proximity
    region_mod = {
        "circuit": -0.10, "same": -0.06, "adjacent": -0.02, "distant": 0.12,
    }.get(regional_proximity, 0.12)

    # 6. Domain match (reused from Stage 4a, now with expanded PLAUSIBLE_TRANSITIONS)
    # If seniority_progression is detected, override "implausible" to "plausible"
    # because we've confirmed this IS a valid career path
    effective_domain = domain_match
    if domain_match == "implausible" and seniority_progression != "none":
        effective_domain = "plausible"

    domain_mod = {
        "exact": -0.08, "overlap": -0.04, "plausible": 0.0,
        "unknown": 0.05, "implausible": 0.20,
    }.get(effective_domain, 0.05)

    # 7. Seniority direction (generic up/down/lateral)
    seniority_mod = {
        "promotion": -0.04, "lateral": 0.0, "demotion": 0.10, "unknown": 0.02,
    }.get(seniority_direction, 0.02)

    # 8. Seniority progression bonus (specific career ladder detection)
    # Strong promotions (ColSec→Governor, SG→AG→CJ) are very distinctive
    # identity signals — two people with the same name rarely follow the
    # same specific career ladder across colonies
    progression_mod = {
        "strong_promotion": -0.12,
        "moderate_promotion": -0.06,
        "none": 0.0,
    }.get(seniority_progression, 0.0)

    # 9. Gap penalty
    if overlap_years > 0:
        gap_penalty = 0.0  # handled by overlap penalty below
    elif gap_years <= 0:
        gap_penalty = 0.0
    elif gap_years <= 2:
        gap_penalty = -0.03  # ideal transfer gap
    elif gap_years <= 5:
        gap_penalty = 0.0
    elif gap_years <= 10:
        gap_penalty = 0.05
    elif gap_years <= 15:
        gap_penalty = 0.05 + (gap_years - 10) * 0.01
    else:
        gap_penalty = 0.10 + (gap_years - 15) * 0.015

    # 10. Colony penalty (names in many colonies = higher collision risk)
    if colony_count <= 2:
        colony_penalty = 0.0
    elif colony_count == 3:
        colony_penalty = 0.05
    else:
        colony_penalty = 0.15

    # 11. Tenure bonus
    min_tenure = min(a_editions, b_editions)
    tenure_bonus = min(0.08, min_tenure * 0.015)

    # 12. Overlap handling
    overlap_penalty = 0.0
    if overlap_type == "federal_duplicate":
        overlap_penalty = -0.10  # identity signal
    elif overlap_years > 1:
        overlap_penalty = 0.25 * (overlap_years - 1)  # heavy penalty

    score = (base + name_mod + honours_mod + rank_mod + region_mod
             + domain_mod + seniority_mod + progression_mod + gap_penalty
             + colony_penalty + overlap_penalty - tenure_bonus)

    return round(max(UNCERTAINTY_FLOOR, min(UNCERTAINTY_CEILING, score)), 3)


# =============================================================================
# DATA FETCHING
# =============================================================================

OFFICIALS_QUERY = """
MATCH (o:COL_Official)
WHERE EXISTS {
    MATCH (pr:COL_PersonRecord)-[:RECORD_OF]->(o)
    WHERE pr.quarantined IS NULL OR pr.quarantined = false
}
OPTIONAL MATCH (pr_first:COL_PersonRecord)-[:RECORD_OF]->(o)
WHERE pr_first.year = o.first_year
  AND (pr_first.quarantined IS NULL OR pr_first.quarantined = false)
OPTIONAL MATCH (pr_last:COL_PersonRecord)-[:RECORD_OF]->(o)
WHERE pr_last.year = o.last_year
  AND (pr_last.quarantined IS NULL OR pr_last.quarantined = false)
WITH o, pr_first, pr_last
OPTIONAL MATCH (pr_any:COL_PersonRecord)-[:RECORD_OF]->(o)
WHERE pr_any.quarantined IS NULL OR pr_any.quarantined = false
RETURN
    o.id AS id,
    o.name AS name,
    o.colony AS colony,
    o.first_year AS first_year,
    o.last_year AS last_year,
    o.editions AS editions,
    pr_first.position_raw AS first_position,
    pr_first.department_raw AS first_dept,
    pr_first.honors AS first_honours,
    pr_first.military_rank AS first_rank,
    pr_last.position_raw AS last_position,
    pr_last.department_raw AS last_dept,
    pr_last.honors AS last_honours,
    pr_last.military_rank AS last_rank,
    collect(DISTINCT pr_any.given_names) AS given_name_variants
"""


def fetch_all_officials(session) -> list[dict]:
    """Fetch all COL_Official data with first/last PersonRecord details.

    Excludes officials whose PersonRecords are ALL quarantined.
    Also collects given_name variants from non-quarantined PersonRecords.
    """
    result = session.run(OFFICIALS_QUERY)
    return [dict(r) for r in result]


# =============================================================================
# CANDIDATE PAIR GENERATION
# =============================================================================

def _compute_name_match_quality(a: dict, b: dict) -> str:
    """Compute how well two officials' names match.

    Returns:
      'exact_name' — identical official names
      'fuzzy_compatible' — same surname, initials compatible across variants
      'bare' — one side has bare surname (no given names)
      'incompatible' — initials conflict, skip pair
    """
    if a["name"] == b["name"]:
        return "exact_name"

    # Extract given-name variants (from PersonRecords)
    a_variants = [clean_given_names(g) for g in (a.get("given_name_variants") or []) if g]
    b_variants = [clean_given_names(g) for g in (b.get("given_name_variants") or []) if g]

    # Also extract given names from the official name itself
    a_given_from_name = a["name"].split(", ", 1)[1].strip() if ", " in a["name"] else ""
    b_given_from_name = b["name"].split(", ", 1)[1].strip() if ", " in b["name"] else ""
    if a_given_from_name and a_given_from_name not in a_variants:
        a_variants.append(a_given_from_name)
    if b_given_from_name and b_given_from_name not in b_variants:
        b_variants.append(b_given_from_name)

    # Check if either side is bare surname
    if not a_variants or not b_variants:
        return "bare"

    # Check if ANY variant pair is initials-compatible
    for av in a_variants:
        for bv in b_variants:
            if initials_compatible(av, bv):
                return "fuzzy_compatible"

    return "incompatible"


def generate_candidate_pairs(
    officials: list[dict],
    max_colonies: int = DEFAULT_MAX_COLONIES,
    colony_filter: str | None = None,
) -> list[dict]:
    """Generate cross-colony candidate pairs.

    Groups officials by SURNAME (not full name), then uses initials_compatible
    to find fuzzy matches across colonies. Exact-name matches are preserved
    as before; fuzzy matches get an additional uncertainty penalty.
    """
    # Group by surname
    by_surname = defaultdict(list)
    for off in officials:
        surname = off["name"].split(",", 1)[0].strip()
        by_surname[surname].append(off)

    pairs = []
    skipped_large = 0
    for surname, stints in by_surname.items():
        # Safety cap: skip very large surname groups
        if len(stints) > 200:
            skipped_large += 1
            continue

        # Get distinct colonies
        colonies = {s["colony"] for s in stints}
        if len(colonies) < 2:
            continue

        # Apply colony filter
        if colony_filter and colony_filter not in colonies:
            continue

        # Generate all cross-colony pairs
        for i, a in enumerate(stints):
            for b in stints[i + 1:]:
                if a["colony"] == b["colony"]:
                    continue

                # Exclude bare legislative members (MPs, Senators)
                if (is_bare_member_position(a.get("last_position"))
                        or is_bare_member_position(b.get("last_position"))
                        or is_bare_member_position(a.get("first_position"))
                        or is_bare_member_position(b.get("first_position"))):
                    continue

                # Check name match quality (fuzzy matching)
                nmq = _compute_name_match_quality(a, b)
                if nmq == "incompatible":
                    continue

                # For colony_count, count colonies with compatible officials
                # (not all surname-sharing officials)
                if nmq == "exact_name":
                    # Original behavior: count colonies for this exact name
                    compat_colonies = {s["colony"] for s in stints if s["name"] == a["name"]}
                else:
                    # Count colonies where we have compatible-initial officials
                    compat_colonies = {a["colony"], b["colony"]}

                if len(compat_colonies) > max_colonies:
                    continue

                colony_count = len(compat_colonies)

                # Order chronologically
                a_pair, b_pair = a, b
                if a_pair["last_year"] > b_pair["last_year"]:
                    a_pair, b_pair = b_pair, a_pair
                elif a_pair["last_year"] == b_pair["last_year"] and a_pair["first_year"] > b_pair["first_year"]:
                    a_pair, b_pair = b_pair, a_pair

                # Compute overlap
                overlap_start = max(a_pair["first_year"], b_pair["first_year"])
                overlap_end = min(a_pair["last_year"], b_pair["last_year"])
                overlap_years = max(0, overlap_end - overlap_start + 1)

                # Gap (only when no overlap)
                if overlap_years > 0:
                    gap_years = 0
                else:
                    gap_years = b_pair["first_year"] - a_pair["last_year"]

                # Classify overlap
                if overlap_years > 0 and is_federal_pair(a_pair["colony"], b_pair["colony"]):
                    overlap_type = "federal_duplicate"
                elif overlap_years == 1:
                    overlap_type = "transition_year"
                elif overlap_years > 1:
                    overlap_type = "multi_year_overlap"
                else:
                    overlap_type = "sequential"

                pairs.append({
                    "name": a_pair["name"],  # use a's name as display name
                    "a_id": a_pair["id"],
                    "b_id": b_pair["id"],
                    "a_colony": a_pair["colony"],
                    "b_colony": b_pair["colony"],
                    "a_first_year": a_pair["first_year"],
                    "a_last_year": a_pair["last_year"],
                    "b_first_year": b_pair["first_year"],
                    "b_last_year": b_pair["last_year"],
                    "a_editions": len(a_pair["editions"]) if a_pair["editions"] else 1,
                    "b_editions": len(b_pair["editions"]) if b_pair["editions"] else 1,
                    "a_last_position": a_pair["last_position"],
                    "a_last_dept": a_pair["last_dept"],
                    "a_last_honours": a_pair["last_honours"],
                    "a_last_rank": a_pair["last_rank"],
                    "b_first_position": b_pair["first_position"],
                    "b_first_dept": b_pair["first_dept"],
                    "b_first_honours": b_pair["first_honours"],
                    "b_first_rank": b_pair["first_rank"],
                    "gap_years": gap_years,
                    "overlap_years": overlap_years,
                    "overlap_type": overlap_type,
                    "colony_count": colony_count,
                    "name_match_quality": nmq,
                })

    if skipped_large:
        print(f"  Skipped {skipped_large} surname groups with >200 officials")
    return pairs


# =============================================================================
# EVIDENCE COMPUTATION
# =============================================================================

def compute_evidence(pair: dict) -> dict:
    """Compute all evidence fields and uncertainty for a candidate pair."""
    name_spec = compute_name_specificity(pair["name"])
    honours = compute_honours_match(pair["a_last_honours"], pair["b_first_honours"])
    rank = compute_rank_match(pair["a_last_rank"], pair["b_first_rank"])
    region = compute_regional_proximity(pair["a_colony"], pair["b_colony"])
    domain = compute_domain_match(
        pair["a_last_position"], pair["a_last_dept"],
        pair["b_first_position"], pair["b_first_dept"],
    )
    seniority = compute_seniority_direction(
        pair["a_last_position"], pair["b_first_position"],
    )
    progression = compute_seniority_progression(
        pair["a_last_position"], pair["b_first_position"],
    )

    uncertainty = compute_cross_colony_uncertainty(
        name_specificity=name_spec,
        honours_match=honours,
        rank_match=rank,
        regional_proximity=region,
        domain_match=domain,
        seniority_direction=seniority,
        seniority_progression=progression,
        gap_years=pair["gap_years"],
        overlap_years=pair["overlap_years"],
        overlap_type=pair["overlap_type"],
        colony_count=pair["colony_count"],
        a_editions=pair["a_editions"],
        b_editions=pair["b_editions"],
    )

    # Apply name_match_quality penalty for fuzzy/bare matches
    nmq = pair.get("name_match_quality", "exact_name")
    nmq_mod = {
        "exact_name": 0.0,
        "fuzzy_compatible": 0.06,
        "bare": 0.12,
    }.get(nmq, 0.0)

    # Extra penalty for common surname + single initial fuzzy matches
    if nmq == "fuzzy_compatible" and name_spec == "low":
        nmq_mod += 0.09  # total +0.15 for common surname single-initial fuzzy

    uncertainty = round(
        max(UNCERTAINTY_FLOOR, min(UNCERTAINTY_CEILING, uncertainty + nmq_mod)), 3
    )

    return {
        "a_id": pair["a_id"],
        "b_id": pair["b_id"],
        "props": {
            "uncertainty": uncertainty,
            "score_version": SCORE_VERSION,
            "method": "cross_colony_linking",
            "name": pair["name"],
            "a_colony": pair["a_colony"],
            "b_colony": pair["b_colony"],
            "gap_years": pair["gap_years"],
            "overlap_years": pair["overlap_years"],
            "overlap_type": pair["overlap_type"],
            "name_specificity": name_spec,
            "name_match_quality": nmq,
            "honours_match": honours,
            "military_rank_match": rank,
            "regional_proximity": region,
            "domain_match": domain,
            "seniority_direction": seniority,
            "seniority_progression": progression,
            "a_last_position": pair["a_last_position"],
            "b_first_position": pair["b_first_position"],
            "a_last_dept": pair["a_last_dept"],
            "b_first_dept": pair["b_first_dept"],
            "a_editions": pair["a_editions"],
            "b_editions": pair["b_editions"],
            "colony_count": pair["colony_count"],
            "date_created": date.today().isoformat(),
        },
    }


# =============================================================================
# WRITE TO NEO4J
# =============================================================================

MERGE_QUERY = """
UNWIND $batch AS rec
MATCH (a:COL_Official {id: rec.a_id})
MATCH (b:COL_Official {id: rec.b_id})
MERGE (a)-[r:POSSIBLE_MATCH]->(b)
SET r += rec.props
"""

MERGE_QUERY_FORCE = """
UNWIND $batch AS rec
MATCH (a:COL_Official {id: rec.a_id})
MATCH (b:COL_Official {id: rec.b_id})
MERGE (a)-[r:POSSIBLE_MATCH]->(b)
SET r.uncertainty = rec.props.uncertainty,
    r.score_version = rec.props.score_version,
    r.method = rec.props.method,
    r.name = rec.props.name,
    r.a_colony = rec.props.a_colony,
    r.b_colony = rec.props.b_colony,
    r.gap_years = rec.props.gap_years,
    r.overlap_years = rec.props.overlap_years,
    r.overlap_type = rec.props.overlap_type,
    r.name_specificity = rec.props.name_specificity,
    r.name_match_quality = rec.props.name_match_quality,
    r.honours_match = rec.props.honours_match,
    r.military_rank_match = rec.props.military_rank_match,
    r.regional_proximity = rec.props.regional_proximity,
    r.domain_match = rec.props.domain_match,
    r.seniority_direction = rec.props.seniority_direction,
    r.seniority_progression = rec.props.seniority_progression,
    r.a_last_position = rec.props.a_last_position,
    r.b_first_position = rec.props.b_first_position,
    r.a_last_dept = rec.props.a_last_dept,
    r.b_first_dept = rec.props.b_first_dept,
    r.a_editions = rec.props.a_editions,
    r.b_editions = rec.props.b_editions,
    r.colony_count = rec.props.colony_count,
    r.date_created = rec.props.date_created
"""


def write_links(session, evidence_list: list[dict], force: bool = False):
    """Write POSSIBLE_MATCH edges in batches."""
    query = MERGE_QUERY_FORCE if force else MERGE_QUERY
    total = 0
    for i in range(0, len(evidence_list), BATCH_SIZE):
        batch = evidence_list[i:i + BATCH_SIZE]
        session.run(query, batch=batch)
        total += len(batch)
    return total


# =============================================================================
# STATS
# =============================================================================

def print_stats(driver):
    """Report on cross-colony POSSIBLE_MATCH edges."""
    with driver.session() as session:
        print("\n" + "=" * 60)
        print("CROSS-COLONY LINKING STATISTICS")
        print("=" * 60)

        r = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH {method: 'cross_colony_linking'}]->() "
            "RETURN count(r) AS c"
        ).single()
        total = r["c"]
        print(f"\n  Total cross-colony edges: {total}")

        if total == 0:
            print("  No edges found.")
            return

        # Uncertainty distribution
        print("\n  Uncertainty distribution:")
        result = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH {method: 'cross_colony_linking'}]->() "
            "WITH CASE "
            "  WHEN r.uncertainty < 0.2 THEN '0.10-0.19' "
            "  WHEN r.uncertainty < 0.3 THEN '0.20-0.29' "
            "  WHEN r.uncertainty < 0.4 THEN '0.30-0.39' "
            "  WHEN r.uncertainty < 0.5 THEN '0.40-0.49' "
            "  WHEN r.uncertainty < 0.6 THEN '0.50-0.59' "
            "  WHEN r.uncertainty < 0.7 THEN '0.60-0.69' "
            "  ELSE '0.70+' "
            "END AS bucket, count(*) AS n "
            "RETURN bucket, n ORDER BY bucket"
        )
        for record in result:
            bar = "█" * max(1, record["n"] * 40 // total)
            print(f"    {record['bucket']:<10}  {record['n']:>5}  {bar}")

        # Overlap type breakdown
        print("\n  Overlap type breakdown:")
        result = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH {method: 'cross_colony_linking'}]->() "
            "RETURN r.overlap_type AS ot, count(*) AS n, "
            "       round(avg(r.uncertainty) * 1000) / 1000 AS avg_unc "
            "ORDER BY n DESC"
        )
        for record in result:
            print(f"    {record['ot']:<25} {record['n']:>5}  "
                  f"avg uncertainty: {record['avg_unc']:.3f}")

        # Regional proximity breakdown
        print("\n  Regional proximity breakdown:")
        result = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH {method: 'cross_colony_linking'}]->() "
            "RETURN r.regional_proximity AS rp, count(*) AS n, "
            "       round(avg(r.uncertainty) * 1000) / 1000 AS avg_unc "
            "ORDER BY n DESC"
        )
        for record in result:
            print(f"    {record['rp']:<15} {record['n']:>5}  "
                  f"avg uncertainty: {record['avg_unc']:.3f}")

        # Honours match breakdown
        print("\n  Honours match breakdown:")
        result = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH {method: 'cross_colony_linking'}]->() "
            "RETURN r.honours_match AS hm, count(*) AS n, "
            "       round(avg(r.uncertainty) * 1000) / 1000 AS avg_unc "
            "ORDER BY n DESC"
        )
        for record in result:
            print(f"    {record['hm']:<15} {record['n']:>5}  "
                  f"avg uncertainty: {record['avg_unc']:.3f}")

        # Top colony pairs
        print("\n  Top 15 colony pairs:")
        result = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH {method: 'cross_colony_linking'}]->() "
            "RETURN r.a_colony + ' → ' + r.b_colony AS route, count(*) AS n, "
            "       round(avg(r.uncertainty) * 1000) / 1000 AS avg_unc "
            "ORDER BY n DESC LIMIT 15"
        )
        for record in result:
            print(f"    {record['route']:<50} {record['n']:>4}  "
                  f"avg: {record['avg_unc']:.3f}")

        # Sample high-confidence edges
        print("\n  Sample high-confidence matches (uncertainty < 0.30):")
        result = session.run(
            "MATCH (a:COL_Official)-[r:POSSIBLE_MATCH {method: 'cross_colony_linking'}]->(b:COL_Official) "
            "WHERE r.uncertainty < 0.30 "
            "RETURN a.name AS name, r.a_colony AS from_col, a.last_year AS from_year, "
            "       r.b_colony AS to_col, b.first_year AS to_year, "
            "       r.uncertainty AS unc, r.overlap_type AS ot "
            "ORDER BY r.uncertainty LIMIT 15"
        )
        for record in result:
            ot = f" [{record['ot']}]" if record["ot"] != "sequential" else ""
            print(f"    {record['unc']:.3f}  {record['name']:<30} "
                  f"{record['from_col']} ({record['from_year']}) → "
                  f"{record['to_col']} ({record['to_year']}){ot}")


# =============================================================================
# DRY RUN
# =============================================================================

def dry_run_report(evidence_list: list[dict], threshold: float):
    """Preview linking results without writing."""
    print("\n" + "=" * 60)
    print("[DRY RUN] CROSS-COLONY LINKING PREVIEW")
    print("=" * 60)

    total = len(evidence_list)
    under_threshold = [e for e in evidence_list if e["props"]["uncertainty"] <= threshold]
    print(f"\n  Total candidate pairs scored: {total}")
    print(f"  Pairs under threshold ({threshold}): {len(under_threshold)}")
    print(f"  Pairs over threshold (excluded): {total - len(under_threshold)}")

    if not under_threshold:
        print("  No pairs under threshold. Nothing would be written.")
        return

    ev_list = under_threshold

    # Score distribution
    buckets = defaultdict(int)
    for ev in ev_list:
        score = ev["props"]["uncertainty"]
        bucket = int(score * 10)
        bucket = min(bucket, 9)
        label = f"{bucket / 10:.1f}0-{(bucket + 1) / 10:.1f}{'0' if bucket < 9 else ''}"
        buckets[label] += 1

    print("\n  Uncertainty distribution (under threshold only):")
    for label in sorted(buckets):
        n = buckets[label]
        bar = "█" * max(1, n * 40 // len(ev_list))
        print(f"    {label:<10}  {n:>5}  {bar}")

    # Overlap type breakdown
    ot_counts = defaultdict(int)
    ot_scores = defaultdict(list)
    for ev in ev_list:
        ot = ev["props"]["overlap_type"]
        ot_counts[ot] += 1
        ot_scores[ot].append(ev["props"]["uncertainty"])

    print("\n  Overlap type breakdown:")
    for ot in sorted(ot_counts, key=ot_counts.get, reverse=True):
        avg_s = sum(ot_scores[ot]) / len(ot_scores[ot])
        print(f"    {ot:<25} {ot_counts[ot]:>5}  avg uncertainty: {avg_s:.3f}")

    # Regional proximity
    rp_counts = defaultdict(int)
    rp_scores = defaultdict(list)
    for ev in ev_list:
        rp = ev["props"]["regional_proximity"]
        rp_counts[rp] += 1
        rp_scores[rp].append(ev["props"]["uncertainty"])

    print("\n  Regional proximity breakdown:")
    for rp in sorted(rp_counts, key=rp_counts.get, reverse=True):
        avg_s = sum(rp_scores[rp]) / len(rp_scores[rp])
        print(f"    {rp:<15} {rp_counts[rp]:>5}  avg uncertainty: {avg_s:.3f}")

    # Name match quality
    nmq_counts = defaultdict(int)
    nmq_scores = defaultdict(list)
    for ev in ev_list:
        nmq = ev["props"].get("name_match_quality", "exact_name")
        nmq_counts[nmq] += 1
        nmq_scores[nmq].append(ev["props"]["uncertainty"])

    print("\n  Name match quality breakdown:")
    for nmq in sorted(nmq_counts, key=nmq_counts.get, reverse=True):
        avg_s = sum(nmq_scores[nmq]) / len(nmq_scores[nmq])
        print(f"    {nmq:<20} {nmq_counts[nmq]:>5}  avg uncertainty: {avg_s:.3f}")

    # Honours match
    hm_counts = defaultdict(int)
    hm_scores = defaultdict(list)
    for ev in ev_list:
        hm = ev["props"]["honours_match"]
        hm_counts[hm] += 1
        hm_scores[hm].append(ev["props"]["uncertainty"])

    print("\n  Honours match breakdown:")
    for hm in sorted(hm_counts, key=hm_counts.get, reverse=True):
        avg_s = sum(hm_scores[hm]) / len(hm_scores[hm])
        print(f"    {hm:<15} {hm_counts[hm]:>5}  avg uncertainty: {avg_s:.3f}")

    # Domain match
    dm_counts = defaultdict(int)
    dm_scores = defaultdict(list)
    for ev in ev_list:
        dm = ev["props"]["domain_match"]
        dm_counts[dm] += 1
        dm_scores[dm].append(ev["props"]["uncertainty"])

    print("\n  Domain match breakdown:")
    for dm in sorted(dm_counts, key=dm_counts.get, reverse=True):
        avg_s = sum(dm_scores[dm]) / len(dm_scores[dm])
        print(f"    {dm:<15} {dm_counts[dm]:>5}  avg uncertainty: {avg_s:.3f}")

    # Sample pairs at different score levels
    sorted_ev = sorted(ev_list, key=lambda e: e["props"]["uncertainty"])
    print("\n  Sample pairs:")
    samples = []
    if len(sorted_ev) >= 5:
        step = max(1, len(sorted_ev) // 5)
        samples = [sorted_ev[i * step] for i in range(5)]
        if sorted_ev[-1] not in samples:
            samples.append(sorted_ev[-1])
    else:
        samples = sorted_ev

    for ev in samples:
        p = ev["props"]
        print(f"\n    {p['uncertainty']:.3f}  {p['name']}")
        print(f"           {p['a_colony']} → {p['b_colony']}  "
              f"(gap={p['gap_years']}y, overlap={p['overlap_years']}y, {p['overlap_type']})")
        print(f"           name={p['name_specificity']} nmq={p.get('name_match_quality', 'exact_name')} "
              f"honours={p['honours_match']} "
              f"rank={p['military_rank_match']} region={p['regional_proximity']}")
        print(f"           domain={p['domain_match']} seniority={p['seniority_direction']} "
              f"progression={p.get('seniority_progression', 'n/a')} "
              f"colonies={p['colony_count']}")
        print(f"           a_pos: {p['a_last_position']}")
        print(f"           b_pos: {p['b_first_position']}")

    # Summary of all scored pairs (including over threshold)
    if total > len(under_threshold):
        over = [e for e in evidence_list if e["props"]["uncertainty"] > threshold]
        print(f"\n  --- {len(over)} pairs ABOVE threshold ({threshold}) ---")
        ot_over = defaultdict(int)
        for ev in over:
            ot_over[ev["props"]["overlap_type"]] += 1
        for ot in sorted(ot_over, key=ot_over.get, reverse=True):
            print(f"    {ot:<25} {ot_over[ot]:>5}")

    print("\n[DRY RUN] No data written.")


# =============================================================================
# CLEAR
# =============================================================================

def clear_cross_colony(driver):
    """Remove all cross-colony POSSIBLE_MATCH edges."""
    with driver.session() as session:
        r = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH {method: 'cross_colony_linking'}]->() "
            "DELETE r RETURN count(r) AS c"
        ).single()
        print(f"Deleted {r['c']} cross-colony POSSIBLE_MATCH edges.")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Stage 4c: Cross-colony career linking"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without writing to Neo4j")
    parser.add_argument("--stats", action="store_true",
                        help="Report cross-colony POSSIBLE_MATCH statistics")
    parser.add_argument("--clear", action="store_true",
                        help="Remove all cross-colony POSSIBLE_MATCH edges")
    parser.add_argument("--colony", type=str,
                        help="Only pairs involving this colony")
    parser.add_argument("--force", action="store_true",
                        help="Recompute scores (preserves verified_by/verified_date)")
    parser.add_argument("--max-colonies", type=int, default=DEFAULT_MAX_COLONIES,
                        help=f"Skip names in more than N colonies (default: {DEFAULT_MAX_COLONIES})")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD,
                        help=f"Uncertainty cutoff for edge creation (default: {DEFAULT_THRESHOLD})")
    parser.add_argument("--ml-score", action="store_true",
                        help="After linking, apply ML scorer to write ml_uncertainty")
    args = parser.parse_args()

    print("=" * 60)
    print("COL STAGE 4c: CROSS-COLONY CAREER LINKING")
    print("=" * 60)

    # Connect to Neo4j
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        # --- Stats only ---
        if args.stats:
            print_stats(driver)
            return

        # --- Clear ---
        if args.clear:
            clear_cross_colony(driver)
            return

        # --- Fetch all officials ---
        print("\nFetching all COL_Official data...")
        with driver.session() as session:
            officials = fetch_all_officials(session)
        print(f"  {len(officials)} COL_Official nodes loaded")

        # --- Generate candidate pairs ---
        print(f"Generating cross-colony candidate pairs "
              f"(max-colonies={args.max_colonies})...")
        pairs = generate_candidate_pairs(
            officials,
            max_colonies=args.max_colonies,
            colony_filter=args.colony,
        )
        print(f"  {len(pairs)} raw candidate pairs generated")

        if not pairs:
            print("\nNo candidate pairs found. Nothing to do.")
            return

        # --- Compute evidence ---
        print("Computing evidence and scores...")
        all_evidence = []
        for pair in pairs:
            all_evidence.append(compute_evidence(pair))

        # --- Apply threshold ---
        under_threshold = [e for e in all_evidence
                           if e["props"]["uncertainty"] <= args.threshold]
        over_threshold = len(all_evidence) - len(under_threshold)
        print(f"  {len(under_threshold)} pairs under threshold ({args.threshold})")
        print(f"  {over_threshold} pairs over threshold (excluded)")

        # --- Dry run or write ---
        if args.dry_run:
            dry_run_report(all_evidence, args.threshold)
            return

        if not under_threshold:
            print("\nNo pairs under threshold. Nothing to write.")
            return

        print(f"Writing {len(under_threshold)} POSSIBLE_MATCH edges...")
        with driver.session() as session:
            written = write_links(session, under_threshold, force=args.force)
        print(f"  {written} edges written.")

        # --- Final stats ---
        print_stats(driver)

        # --- Optional ML scoring ---
        if args.ml_score:
            print("\nApplying ML scorer...")
            try:
                from col_ml_score import load_model, score_edges, write_scores_to_neo4j
                from col_ml_features import fetch_all_edges
                model, scaler, feature_cols = load_model("gb")
                with driver.session() as session:
                    edges = fetch_all_edges(session)
                    results = score_edges(edges, model, scaler, feature_cols)
                    written = write_scores_to_neo4j(session, results, "gb")
                    print(f"  ML scores written to {written} edges")
            except Exception as e:
                print(f"  ML scoring failed: {e}")
                print("  Run col_ml_train.py first to train the model")

    finally:
        driver.close()

    print("\nDone.")


if __name__ == "__main__":
    main()
