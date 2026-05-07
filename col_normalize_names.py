"""
COL Stage 1.5: Name Normalization
==================================

Normalizes canonical_name on COL_PersonRecord nodes so that the same person
gets the same canonical_name across editions, enabling correct grouping
in Stage 2 (COL_Official creation).

Problems fixed:
  1. Titles in given_names: "Sir Anthony" → "Anthony"
  2. Honours in canonical_name: "Guggisberg, D.S.O., Brigadier-General Sir Frederic Gordon" → "Guggisberg, Frederic Gordon"
  3. Name variant unification: "Guggisberg, F. G." and "Guggisberg, F. Gordon" → "Guggisberg, F. Gordon"
  4. Bare names without comma: "Attorney-General" → skipped (not a person name)

Approach:
  - Clean each PersonRecord's given_names by stripping titles/honours/ranks
  - Rebuild canonical_name as "Surname, CleanGivenNames"
  - Within each (surname, colony) group, find compatible name variants
    and unify to the most specific form
  - Update canonical_name in Neo4j

Usage:
    python col_normalize_names.py              # full run
    python col_normalize_names.py --dry-run    # preview changes
    python col_normalize_names.py --stats      # report current state
    python col_normalize_names.py --colony X   # single colony

Requires:
    pip install neo4j
"""

import argparse
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


# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
BATCH_SIZE = 1000


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
# TITLE / HONOUR STRIPPING
# =============================================================================

# Titles to strip from given names (order matters — longer first)
TITLE_PATTERNS = [
    r"\bH\.H\.\s*",          # His Highness
    r"\bH\.E\.\s*",          # His Excellency
    r"\bRt\.?\s*Hon\.?\s*",  # Right Honourable
    r"\bHon\.?\s*",          # Honourable
    r"\bSir\s+",             # Sir
    r"\bDame\s+",            # Dame
    r"\bLady\s+",            # Lady
    r"\bLord\s+",            # Lord
    r"\bRev\.?\s*",          # Reverend
    r"\bVen\.?\s*",          # Venerable
]

# Military ranks to strip (these should be in military_rank field)
RANK_PATTERNS = [
    r"\bField\s+Marshal\s*",
    r"\bLieutenant-General\s*",
    r"\bMajor-General\s*",
    r"\bBrigadier-General\s*",
    r"\bBrigadier\s*",
    r"\bColonel\s*",
    r"\bLieutenant-Colonel\s*",
    r"\bLt\.?\s*-?\s*Col\.?\s*",
    r"\bMajor\b\s*",
    r"\bCaptain\b\s*",
    r"\bCapt\.?\s*",
    r"\bLieutenant\b\s*",
    r"\bLieut\.?\s*",
    r"\bLt\.?\s+",
    r"\bRear-Admiral\s*",
    r"\bVice-Admiral\s*",
    r"\bAdmiral\s*",
    r"\bCommander\b\s*",
    r"\bCdr\.?\s*",
]

# Honours/decorations to strip (these should be in honors field)
HONOUR_PATTERNS = [
    r"\bG\.C\.M\.G\.?\s*",
    r"\bK\.C\.M\.G\.?\s*",
    r"\bC\.M\.G\.?\s*",
    r"\bG\.C\.B\.?\s*",
    r"\bK\.C\.B\.?\s*",
    r"\bC\.B\.?\s*",
    r"\bG\.C\.V\.O\.?\s*",
    r"\bK\.C\.V\.O\.?\s*",
    r"\bC\.V\.O\.?\s*",
    r"\bM\.V\.O\.?\s*",
    r"\bG\.B\.E\.?\s*",
    r"\bK\.B\.E\.?\s*",
    r"\bC\.B\.E\.?\s*",
    r"\bO\.B\.E\.?\s*",
    r"\bM\.B\.E\.?\s*",
    r"\bG\.C\.S\.I\.?\s*",
    r"\bK\.C\.S\.I\.?\s*",
    r"\bC\.S\.I\.?\s*",
    r"\bG\.C\.I\.E\.?\s*",
    r"\bK\.C\.I\.E\.?\s*",
    r"\bC\.I\.E\.?\s*",
    r"\bD\.S\.O\.?\s*",
    r"\bM\.C\.?\s*",
    r"\bI\.S\.O\.?\s*",
    r"\bE\.D\.?\s*",
    r"\bT\.D\.?\s*",
    r"\bQ\.C\.?\s*",
    r"\bK\.C\.?\s*",
    r"\bKt\.?\s*",
    r"\bR\.E\.?\s*",
    r"\bR\.N\.?\s*",
    r"\bR\.A\.?\s*",
    r"\bR\.F\.?\s*",
    r"\bR\.M\.?\s*",
    r"\bF\.R\.C\.S\.?\s*",
    r"\bM\.D\.?\s*",
    r"\bLL\.D\.?\s*",
    r"\bPh\.D\.?\s*",
    r"\bB\.A\.?\s*",
    r"\bM\.A\.?\s*",
    r"\bB\.Sc\.?\s*",
    r"\bM\.Sc\.?\s*",
]

# Compile all patterns
_STRIP_PATTERNS = []
for patterns in [TITLE_PATTERNS, RANK_PATTERNS, HONOUR_PATTERNS]:
    for p in patterns:
        _STRIP_PATTERNS.append(re.compile(p, re.IGNORECASE))


def clean_given_names(given_names: str) -> str:
    """Strip titles, ranks, and honours from given names.

    Returns cleaned given names string.
    """
    if not given_names:
        return ""

    text = given_names.strip()

    # Apply all stripping patterns
    for pattern in _STRIP_PATTERNS:
        text = pattern.sub("", text)

    # Clean up: remove leading/trailing commas, whitespace, dots
    text = re.sub(r"\s*,\s*", " ", text)  # commas to spaces
    text = re.sub(r"\s+", " ", text)      # collapse whitespace
    text = text.strip(" .,;")

    return text


def build_canonical_name(surname: str, clean_given: str) -> str:
    """Build canonical_name from surname and cleaned given names."""
    if not surname:
        return ""
    if not clean_given:
        return surname
    return f"{surname}, {clean_given}"


# =============================================================================
# INITIAL COMPATIBILITY
# =============================================================================

def extract_initials(given_names: str) -> list[str]:
    """Extract ordered initials from given names.

    "Frederick Gordon" → ['F', 'G']
    "F. G." → ['F', 'G']
    "F. Gordon" → ['F', 'G']
    """
    if not given_names:
        return []

    initials = []
    for token in given_names.split():
        token = token.strip(".,;")
        if not token:
            continue
        if token[0].isalpha():
            initials.append(token[0].upper())

    return initials


def _is_initial(token: str) -> bool:
    """Check if a token is an initial (single letter or letter-dot)."""
    t = token.strip(".,;")
    return len(t) <= 1


def _tokenize_given(given: str) -> list[str]:
    """Split given names into tokens, stripping punctuation."""
    return [t.strip(".,;") for t in given.split() if t.strip(".,;")]


def initials_compatible(a_given: str, b_given: str) -> bool:
    """Check if two given name strings could refer to the same person.

    Rules for each position:
    - Both initials: first letters must match
    - One initial, one full word: first letters must match
    - Both full words: must be equal (catches "Elizabeth" vs "Edwin")

    "F. G." and "F. Gordon" → True (initial F matches F, initial G matches Gordon)
    "F. G." and "H. G." → False (F≠H)
    "Elizabeth" and "Edwin" → False (both full words, not equal)
    "" and "F. G." → True (bare surname matches anything)
    """
    a_tokens = _tokenize_given(a_given)
    b_tokens = _tokenize_given(b_given)

    if not a_tokens or not b_tokens:
        return True  # bare surname matches anything

    # Compare position by position up to the shorter list
    for i in range(min(len(a_tokens), len(b_tokens))):
        a_tok = a_tokens[i]
        b_tok = b_tokens[i]

        a_is_init = _is_initial(a_tok)
        b_is_init = _is_initial(b_tok)

        if a_is_init or b_is_init:
            # At least one is an initial — compare first letters
            if a_tok[0].upper() != b_tok[0].upper():
                return False
        else:
            # Both are full words — must match exactly
            if a_tok.lower() != b_tok.lower():
                return False

    return True


def specificity_score(given_names: str) -> int:
    """Score how specific/informative a given name string is.

    Higher = more specific = preferred as the canonical form.
    """
    if not given_names:
        return 0

    score = 0
    for token in given_names.split():
        token = token.strip(".,;")
        if not token:
            continue
        if len(token) == 1 or (len(token) == 2 and token[1] == "."):
            score += 1  # initial
        elif len(token) >= 3:
            score += 3  # full name component
        else:
            score += 2  # short but not initial

    return score


def choose_best_name(name_variants: list[str]) -> str:
    """Choose the most specific given name from a list of compatible variants."""
    if not name_variants:
        return ""
    return max(name_variants, key=specificity_score)


# =============================================================================
# UNIFICATION WITHIN (SURNAME, COLONY) GROUPS
# =============================================================================

def unify_name_group(
    records: list[dict],
) -> dict[str, str]:
    """Given records sharing (surname, colony), unify compatible canonical_names.

    Returns: {old_canonical_name: new_canonical_name} for records that changed.
    """
    # Group by cleaned given names → collect all clean variants
    # First, clean all given names
    cleaned = []
    for rec in records:
        clean_gn = clean_given_names(rec["given_names"] or "")
        cleaned.append({
            "uri": rec["uri"],
            "surname": rec["surname"],
            "original_cn": rec["canonical_name"],
            "clean_given": clean_gn,
            "clean_cn": build_canonical_name(rec["surname"], clean_gn),
        })

    # Group cleaned records by their clean canonical name
    by_clean_cn = defaultdict(list)
    for c in cleaned:
        by_clean_cn[c["clean_cn"]].append(c)

    # Now find compatible groups that can be merged
    # Each group key is a clean_cn; we need to merge groups whose
    # given names are initial-compatible
    clean_cns = list(by_clean_cn.keys())
    merged_groups = []  # list of sets of clean_cn keys
    assigned = set()

    for i, cn_a in enumerate(clean_cns):
        if cn_a in assigned:
            continue

        group = {cn_a}
        given_a = cn_a.split(", ", 1)[1] if ", " in cn_a else ""

        for cn_b in clean_cns[i + 1:]:
            if cn_b in assigned:
                continue
            given_b = cn_b.split(", ", 1)[1] if ", " in cn_b else ""

            if initials_compatible(given_a, given_b):
                group.add(cn_b)

        for cn in group:
            assigned.add(cn)
        merged_groups.append(group)

    # For each merged group, pick the best canonical name
    updates = {}  # uri → new_canonical_name
    for group in merged_groups:
        all_given = []
        all_records = []
        for cn in group:
            for c in by_clean_cn[cn]:
                all_records.append(c)
                if c["clean_given"]:
                    all_given.append(c["clean_given"])

        best_given = choose_best_name(all_given) if all_given else ""
        surname = all_records[0]["surname"]
        best_cn = build_canonical_name(surname, best_given)

        for c in all_records:
            if c["original_cn"] != best_cn:
                updates[c["uri"]] = best_cn

    return updates


# =============================================================================
# MAIN PIPELINE
# =============================================================================

def fetch_all_records(session, colony_filter=None) -> list[dict]:
    """Fetch all PersonRecords with name fields."""
    if colony_filter:
        result = session.run(
            "MATCH (pr:COL_PersonRecord) "
            "WHERE pr.colony = $colony "
            "RETURN pr.uri AS uri, pr.canonical_name AS canonical_name, "
            "       pr.surname AS surname, pr.given_names AS given_names, "
            "       pr.colony AS colony",
            colony=colony_filter,
        )
    else:
        result = session.run(
            "MATCH (pr:COL_PersonRecord) "
            "RETURN pr.uri AS uri, pr.canonical_name AS canonical_name, "
            "       pr.surname AS surname, pr.given_names AS given_names, "
            "       pr.colony AS colony",
        )
    return [dict(r) for r in result]


def resolve_bare_surnames_cross_colony(
    records: list[dict],
    updates: dict[str, str],
) -> dict[str, str]:
    """Resolve bare surnames using cross-colony evidence.

    For records where canonical_name is just a surname (no given names),
    check if that surname is unambiguous across all colonies. If there's
    exactly one compatible given-name form, adopt it.

    This catches cases like Guggisberg in Southern Nigeria (bare surname)
    when Guggisberg, F. Gordon exists in Gold Coast/Togoland.
    """
    uri_to_rec = {r["uri"]: r for r in records}

    # Build surname → set of distinct clean given names (across all colonies)
    # Use the already-updated canonical names where available
    surname_givens = defaultdict(set)
    surname_records = defaultdict(list)
    for rec in records:
        surname = rec.get("surname") or ""
        if not surname or not surname[0].isalpha():
            continue

        # Use the updated canonical_name if we already changed it
        cn = updates.get(rec["uri"], rec["canonical_name"])
        given = cn.split(", ", 1)[1] if ", " in cn else ""
        if given:
            surname_givens[surname].add(given)
        surname_records[surname].append(rec)

    # Find bare-surname records that can be resolved
    extra_updates = {}
    resolved_surnames = 0

    for surname, givens in surname_givens.items():
        if not givens:
            continue

        # Check: are all given-name forms compatible with each other?
        given_list = list(givens)
        all_compatible = True
        for i, a in enumerate(given_list):
            for b in given_list[i + 1:]:
                if not initials_compatible(a, b):
                    all_compatible = False
                    break
            if not all_compatible:
                break

        if not all_compatible:
            continue

        # All forms are compatible — pick the best one
        best_given = choose_best_name(given_list)
        best_cn = build_canonical_name(surname, best_given)

        # Update any bare-surname records for this surname
        found = False
        for rec in surname_records[surname]:
            cn = updates.get(rec["uri"], rec["canonical_name"])
            if ", " not in cn and cn == surname:
                # Bare surname — resolve it
                if rec["uri"] not in updates or updates[rec["uri"]] == surname:
                    extra_updates[rec["uri"]] = best_cn
                    found = True

        if found:
            resolved_surnames += 1

    print(f"  Cross-colony bare surname resolution: {len(extra_updates)} records, "
          f"{resolved_surnames} surnames")
    return extra_updates


def compute_all_updates(records: list[dict]) -> dict[str, str]:
    """Compute all canonical_name updates across all records.

    Returns: {uri: new_canonical_name}
    """
    # Group by (surname, colony)
    groups = defaultdict(list)
    skipped = 0
    for rec in records:
        surname = rec.get("surname") or ""
        if not surname or not surname[0].isalpha():
            skipped += 1
            continue
        colony = rec.get("colony") or ""
        groups[(surname, colony)].append(rec)

    print(f"  {len(groups)} (surname, colony) groups")
    print(f"  {skipped} records skipped (no valid surname)")

    # Pass 1: within-colony unification
    all_updates = {}
    for (surname, colony), group_records in groups.items():
        updates = unify_name_group(group_records)
        all_updates.update(updates)

    print(f"  Within-colony updates: {len(all_updates)}")

    # Pass 2: cross-colony bare surname resolution
    extra = resolve_bare_surnames_cross_colony(records, all_updates)
    all_updates.update(extra)

    return all_updates


UPDATE_QUERY = """
UNWIND $batch AS rec
MATCH (pr:COL_PersonRecord {uri: rec.uri})
SET pr.canonical_name_original = pr.canonical_name,
    pr.canonical_name = rec.new_cn
"""

UPDATE_QUERY_PRESERVE = """
UNWIND $batch AS rec
MATCH (pr:COL_PersonRecord {uri: rec.uri})
SET pr.canonical_name = rec.new_cn
"""


def write_updates(session, updates: dict[str, str]):
    """Write canonical_name updates to Neo4j.

    Preserves original canonical_name in canonical_name_original (first run only).
    """
    batch = [{"uri": uri, "new_cn": new_cn} for uri, new_cn in updates.items()]
    total = 0

    for i in range(0, len(batch), BATCH_SIZE):
        chunk = batch[i:i + BATCH_SIZE]
        # Check if canonical_name_original already exists
        session.run(UPDATE_QUERY, batch=chunk)
        total += len(chunk)
        if total % 5000 < BATCH_SIZE:
            print(f"  Updated {total}/{len(batch)} records...")

    return total


# =============================================================================
# STATS
# =============================================================================

def print_stats(driver):
    """Report on name normalization state."""
    with driver.session() as session:
        print("\n" + "=" * 60)
        print("NAME NORMALIZATION STATISTICS")
        print("=" * 60)

        r = session.run(
            "MATCH (pr:COL_PersonRecord) "
            "WHERE pr.canonical_name_original IS NOT NULL "
            "RETURN count(pr) AS n"
        ).single()
        print(f"\n  Records with normalized names: {r['n']}")

        # Records with titles still in canonical_name
        r = session.run(
            "MATCH (pr:COL_PersonRecord) "
            "WHERE pr.canonical_name CONTAINS 'Sir ' "
            "RETURN count(pr) AS n"
        ).single()
        print(f"  Records still containing 'Sir': {r['n']}")

        # Sample normalizations
        print("\n  Sample normalizations:")
        result = session.run(
            "MATCH (pr:COL_PersonRecord) "
            "WHERE pr.canonical_name_original IS NOT NULL "
            "  AND pr.canonical_name <> pr.canonical_name_original "
            "RETURN pr.canonical_name_original AS old, "
            "       pr.canonical_name AS new, pr.colony AS colony "
            "LIMIT 20"
        )
        for r in result:
            print(f"    {r['old']:<50} → {r['new']}")


# =============================================================================
# DRY RUN
# =============================================================================

def dry_run_report(updates: dict[str, str], records: list[dict]):
    """Preview normalization changes."""
    print("\n" + "=" * 60)
    print("[DRY RUN] NAME NORMALIZATION PREVIEW")
    print("=" * 60)

    print(f"\n  Total records processed: {len(records)}")
    print(f"  Records to update: {len(updates)}")
    print(f"  Records unchanged: {len(records) - len(updates)}")

    if not updates:
        print("  Nothing to change.")
        return

    # Build lookup for display
    uri_to_rec = {r["uri"]: r for r in records}

    # Categorize changes
    title_stripped = 0
    honour_stripped = 0
    variant_unified = 0
    for uri, new_cn in updates.items():
        rec = uri_to_rec.get(uri, {})
        old_cn = rec.get("canonical_name", "")
        if "Sir " in old_cn or "Hon." in old_cn:
            title_stripped += 1
        elif any(h in old_cn for h in ["C.M.G.", "D.S.O.", "K.C.M.G.", "C.B.E.", "O.B.E."]):
            honour_stripped += 1
        else:
            variant_unified += 1

    print(f"\n  Change categories (approximate):")
    print(f"    Title stripped (Sir, Hon., etc.): {title_stripped}")
    print(f"    Honour stripped (C.M.G., etc.):   {honour_stripped}")
    print(f"    Variant unified:                  {variant_unified}")

    # Sample changes
    print("\n  Sample changes:")
    shown = 0
    for uri, new_cn in updates.items():
        if shown >= 30:
            break
        rec = uri_to_rec.get(uri, {})
        old_cn = rec.get("canonical_name", "")
        colony = rec.get("colony", "")
        if old_cn != new_cn:
            print(f"    {old_cn:<50} → {new_cn:<35} [{colony}]")
            shown += 1

    print(f"\n[DRY RUN] No data written.")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Stage 1.5: Normalize canonical_name on PersonRecords"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without writing to Neo4j")
    parser.add_argument("--stats", action="store_true",
                        help="Report normalization state")
    parser.add_argument("--colony", type=str,
                        help="Filter to specific colony")
    args = parser.parse_args()

    print("=" * 60)
    print("COL STAGE 1.5: NAME NORMALIZATION")
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

        # --- Fetch records ---
        print("\nFetching PersonRecords...")
        with driver.session() as session:
            records = fetch_all_records(session, colony_filter=args.colony)
        print(f"  {len(records)} records fetched")

        # --- Compute updates ---
        print("Computing name normalizations...")
        updates = compute_all_updates(records)
        print(f"  {len(updates)} records to update")

        if not updates:
            print("\nNothing to normalize.")
            return

        # --- Dry run or write ---
        if args.dry_run:
            dry_run_report(updates, records)
            return

        print(f"Writing {len(updates)} canonical_name updates...")
        with driver.session() as session:
            written = write_updates(session, updates)
        print(f"  {written} records updated.")

        # --- Final stats ---
        print_stats(driver)

    finally:
        driver.close()

    print("\nDone.")


if __name__ == "__main__":
    main()
