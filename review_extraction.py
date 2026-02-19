"""
Human Review CLI for Extracted Officials
==========================================

Shows source text, extracted JSON, and validation flags side by side.
Supports APPROVE / REJECT / FLAG workflow. Writes review state that the
Neo4j loader respects.

Mandatory review targets:
- First year of each colony (~133 files)
- All XLARGE files (~43 files)
- Any file where >10% of names fail source-text anchoring

Sampling:
- 10% random sample of STANDARD per decade
- 20% random sample of LARGE per decade

Usage:
    python review_extraction.py                         # review next pending
    python review_extraction.py --list                  # list all review targets
    python review_extraction.py --colony "Hong Kong"    # review specific colony
    python review_extraction.py --year 1896             # review specific year
    python review_extraction.py --mandatory-only        # only mandatory reviews
    python review_extraction.py --status                # show review progress
"""

import argparse
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from scaffold_neo4j import scan_corpus


# =============================================================================
# CONFIGURATION
# =============================================================================

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "generated"
STATE_FILE = OUTPUT_DIR / "corpus_state.json"
REVIEW_FILE = OUTPUT_DIR / "review_state.json"


# =============================================================================
# REVIEW STATE
# =============================================================================

def load_review_state() -> dict:
    """Load review state from disk."""
    if REVIEW_FILE.exists():
        with open(REVIEW_FILE) as f:
            return json.load(f)
    return {
        "reviews": {},    # "colony_year" -> {"status": ..., "notes": ..., "timestamp": ...}
        "mandatory": [],  # list of "colony_year" keys that must be reviewed
        "sampled": [],    # list of "colony_year" keys selected for sampling
    }


def save_review_state(state: dict):
    """Save review state to disk."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    with open(REVIEW_FILE, 'w') as f:
        json.dump(state, f, indent=2)


# =============================================================================
# REVIEW TARGET SELECTION
# =============================================================================

def identify_review_targets(corpus_state: dict) -> tuple[list[str], list[str]]:
    """Identify mandatory and sampled review targets.

    Mandatory:
    - First year of each colony
    - XLARGE tier files
    - Files with >10% quarantine rate

    Sampled:
    - 10% of STANDARD per decade
    - 20% of LARGE per decade

    Returns:
        (mandatory_keys, sampled_keys)
    """
    completed = corpus_state.get("completed", {})
    if not completed:
        return [], []

    # Group by colony for first-year detection
    colony_years: dict[str, list[int]] = {}
    for key, result in completed.items():
        colony = result.get("colony", "")
        year = result.get("year", 0)
        if colony and year:
            colony_years.setdefault(colony, []).append(year)

    # Find first year per colony
    first_years = set()
    for colony, years in colony_years.items():
        first_year = min(years)
        first_years.add(f"{colony}_{first_year}")

    mandatory = set()
    for key, result in completed.items():
        # First year of each colony
        colony = result.get("colony", "")
        year = result.get("year", 0)
        if f"{colony}_{year}" in first_years:
            mandatory.add(key)

        # XLARGE tier
        if result.get("tier") == "XLARGE":
            mandatory.add(key)

        # High quarantine rate (>10%)
        vs = result.get("validation_summary", {})
        if vs:
            total = vs.get("total", 0)
            quarantined = vs.get("quarantined", 0)
            if total > 0 and quarantined / total > 0.1:
                mandatory.add(key)

    # Sampling: group by tier and decade
    standard_by_decade: dict[int, list[str]] = {}
    large_by_decade: dict[int, list[str]] = {}

    for key, result in completed.items():
        if key in mandatory:
            continue
        year = result.get("year", 0)
        decade = (year // 10) * 10
        tier = result.get("tier", "")

        if tier == "STANDARD":
            standard_by_decade.setdefault(decade, []).append(key)
        elif tier == "LARGE":
            large_by_decade.setdefault(decade, []).append(key)

    sampled = set()
    random.seed(42)  # reproducible sampling

    for decade, keys in standard_by_decade.items():
        n = max(1, len(keys) // 10)
        sampled.update(random.sample(keys, min(n, len(keys))))

    for decade, keys in large_by_decade.items():
        n = max(1, len(keys) // 5)
        sampled.update(random.sample(keys, min(n, len(keys))))

    return sorted(mandatory), sorted(sampled)


# =============================================================================
# DISPLAY
# =============================================================================

def display_source_excerpt(source_file: str, max_lines: int = 60):
    """Display an excerpt of the source text."""
    try:
        with open(source_file) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("  [Source file not found]")
        return

    # Find staff list start (simplified)
    import re
    start_idx = 0
    for i, line in enumerate(lines):
        clean = line.strip().replace('**', '').replace('__', '')
        clean = re.sub(r'^#{1,6}\s+', '', clean)
        if re.match(r'(?:Civil\s+Establishment|Executive\s+Council)',
                     clean, re.IGNORECASE):
            start_idx = max(0, i - 2)
            break

    excerpt = lines[start_idx:start_idx + max_lines]
    for i, line in enumerate(excerpt, start=start_idx + 1):
        print(f"  {i:>4} | {line.rstrip()}")
    if start_idx + max_lines < len(lines):
        print(f"  ... ({len(lines) - start_idx - max_lines} more lines)")


def display_officials(officials: list[dict], max_show: int = 30):
    """Display extracted officials in a compact table."""
    print(f"\n  {'#':>3} {'Name':<30} {'Position':<35} {'Dept':<25} {'Salary':<12}")
    print(f"  {'':>3} {'-'*30} {'-'*35} {'-'*25} {'-'*12}")

    for i, o in enumerate(officials[:max_show]):
        name = (o.get("name") or "?")[:30]
        pos = (o.get("position") or "?")[:35]
        dept = (o.get("department") or "?")[:25]
        sal_min = o.get("salary_min")
        sal_max = o.get("salary_max")
        if sal_min == sal_max:
            sal = str(sal_min) if sal_min else "?"
        elif sal_min and sal_max:
            sal = f"{sal_min}-{sal_max}"
        else:
            sal = str(sal_min or sal_max or "?")
        print(f"  {i+1:>3} {name:<30} {pos:<35} {dept:<25} {sal:<12}")

    if len(officials) > max_show:
        print(f"  ... and {len(officials) - max_show} more officials")


def display_validation(result: dict):
    """Display validation summary and flags."""
    vs = result.get("validation_summary", {})
    if not vs:
        print("  [No validation data]")
        return

    print(f"\n  Validation:")
    print(f"    Total: {vs.get('total', 0)}")
    print(f"    HIGH confidence: {vs.get('high_confidence', 0)}")
    print(f"    MEDIUM confidence: {vs.get('medium_confidence', 0)}")
    print(f"    LOW confidence: {vs.get('low_confidence', 0)}")
    print(f"    Quarantined: {vs.get('quarantined', 0)}")
    print(f"    Anomalies: {vs.get('anomaly_count', 0)}")


# =============================================================================
# REVIEW WORKFLOW
# =============================================================================

def review_file(key: str, result: dict, review_state: dict) -> str | None:
    """Interactive review of a single extraction.

    Returns the review decision: "APPROVE", "REJECT", "FLAG", or None (skip).
    """
    colony = result.get("colony", "?")
    year = result.get("year", "?")
    tier = result.get("tier", "?")

    print(f"\n{'='*70}")
    print(f"REVIEW: {colony} {year} [{tier}]")
    print(f"{'='*70}")

    # Source text excerpt
    source_file = result.get("source_file", "")
    if source_file:
        print(f"\n--- Source Text (excerpt) ---")
        display_source_excerpt(source_file)

    # Extracted officials
    output_file = result.get("output_file")
    if output_file and Path(output_file).exists():
        with open(output_file) as f:
            data = json.load(f)
        officials = data.get("officials", [])
        print(f"\n--- Extracted Officials ({len(officials)}) ---")
        display_officials(officials)
    else:
        print(f"\n  [Output file not found: {output_file}]")
        officials = []

    # Validation summary
    print(f"\n--- Validation ---")
    display_validation(result)

    # Previous review status
    prev = review_state.get("reviews", {}).get(key)
    if prev:
        print(f"\n  Previous review: {prev.get('status', '?')} "
              f"({prev.get('timestamp', '?')})")
        if prev.get("notes"):
            print(f"  Notes: {prev['notes']}")

    # Prompt for decision
    print(f"\n  [A]pprove  [R]eject  [F]lag for further review  [S]kip  [Q]uit")
    while True:
        try:
            choice = input("  Decision: ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            return None

        if choice in ("A", "APPROVE"):
            notes = input("  Notes (optional): ").strip()
            return _record_review(key, "APPROVE", notes, review_state)
        elif choice in ("R", "REJECT"):
            notes = input("  Reason for rejection: ").strip()
            return _record_review(key, "REJECT", notes, review_state)
        elif choice in ("F", "FLAG"):
            notes = input("  What needs attention: ").strip()
            return _record_review(key, "FLAG", notes, review_state)
        elif choice in ("S", "SKIP"):
            return None
        elif choice in ("Q", "QUIT"):
            return "QUIT"
        else:
            print("  Invalid choice. Enter A, R, F, S, or Q.")


def _record_review(key: str, status: str, notes: str, review_state: dict) -> str:
    """Record a review decision."""
    from datetime import datetime
    review_state.setdefault("reviews", {})[key] = {
        "status": status,
        "notes": notes,
        "timestamp": datetime.now().isoformat(),
    }
    save_review_state(review_state)
    print(f"  Recorded: {status}")
    return status


# =============================================================================
# LIST AND STATUS
# =============================================================================

def show_status(review_state: dict, corpus_state: dict):
    """Show review progress summary."""
    reviews = review_state.get("reviews", {})
    mandatory = review_state.get("mandatory", [])
    sampled = review_state.get("sampled", [])

    approved = sum(1 for r in reviews.values() if r["status"] == "APPROVE")
    rejected = sum(1 for r in reviews.values() if r["status"] == "REJECT")
    flagged = sum(1 for r in reviews.values() if r["status"] == "FLAG")

    print(f"\n{'='*60}")
    print("REVIEW STATUS")
    print(f"{'='*60}")
    print(f"\nMandatory targets: {len(mandatory)}")
    print(f"Sampled targets: {len(sampled)}")
    print(f"Total review targets: {len(mandatory) + len(sampled)}")
    print(f"\nReviewed: {len(reviews)}")
    print(f"  Approved: {approved}")
    print(f"  Rejected: {rejected}")
    print(f"  Flagged: {flagged}")

    # Pending
    all_targets = set(mandatory) | set(sampled)
    pending = [k for k in all_targets if k not in reviews]
    print(f"\nPending review: {len(pending)}")

    if pending:
        print(f"\nNext 10 pending:")
        for k in pending[:10]:
            print(f"  - {k}")


def list_targets(review_state: dict, mandatory_only: bool = False):
    """List all review targets."""
    mandatory = review_state.get("mandatory", [])
    sampled = review_state.get("sampled", [])
    reviews = review_state.get("reviews", {})

    print(f"\nMandatory targets ({len(mandatory)}):")
    for key in mandatory:
        status = reviews.get(key, {}).get("status", "PENDING")
        marker = "+" if status == "APPROVE" else "x" if status == "REJECT" else "!" if status == "FLAG" else " "
        print(f"  [{marker}] {key}")

    if not mandatory_only:
        print(f"\nSampled targets ({len(sampled)}):")
        for key in sampled:
            status = reviews.get(key, {}).get("status", "PENDING")
            marker = "+" if status == "APPROVE" else "x" if status == "REJECT" else "!" if status == "FLAG" else " "
            print(f"  [{marker}] {key}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Human review CLI for extracted officials"
    )
    parser.add_argument("--list", action="store_true",
                        help="List all review targets")
    parser.add_argument("--status", action="store_true",
                        help="Show review progress")
    parser.add_argument("--colony",
                        help="Review specific colony")
    parser.add_argument("--year", type=int,
                        help="Review specific year")
    parser.add_argument("--mandatory-only", action="store_true",
                        help="Only show/process mandatory reviews")
    parser.add_argument("--refresh-targets", action="store_true",
                        help="Recalculate review targets from corpus state")
    args = parser.parse_args()

    # Load states
    review_state = load_review_state()

    if not STATE_FILE.exists():
        print(f"No corpus state found at {STATE_FILE}.")
        print("Run extraction_corpus.py first.")
        return

    with open(STATE_FILE) as f:
        corpus_state = json.load(f)

    # Refresh targets if needed or if they're empty
    if args.refresh_targets or not review_state.get("mandatory"):
        print("Identifying review targets...")
        mandatory, sampled = identify_review_targets(corpus_state)
        review_state["mandatory"] = mandatory
        review_state["sampled"] = sampled
        save_review_state(review_state)
        print(f"Mandatory: {len(mandatory)}, Sampled: {len(sampled)}")

    # Status mode
    if args.status:
        show_status(review_state, corpus_state)
        return

    # List mode
    if args.list:
        list_targets(review_state, args.mandatory_only)
        return

    # Interactive review mode
    completed = corpus_state.get("completed", {})
    reviews = review_state.get("reviews", {})

    # Determine which files to review
    if args.colony or args.year:
        # Review specific colony/year
        targets = []
        for key, result in completed.items():
            if args.colony and result.get("colony", "").lower() != args.colony.lower():
                continue
            if args.year and result.get("year") != args.year:
                continue
            targets.append(key)
    else:
        # Review pending targets in order
        mandatory = review_state.get("mandatory", [])
        sampled = review_state.get("sampled", [])

        if args.mandatory_only:
            targets = [k for k in mandatory if k not in reviews]
        else:
            targets = [k for k in mandatory if k not in reviews]
            targets += [k for k in sampled if k not in reviews]

    if not targets:
        print("No files pending review.")
        return

    print(f"\n{len(targets)} files to review")

    for key in targets:
        result = completed.get(key)
        if not result:
            print(f"  Skipping {key} — not in completed state")
            continue

        decision = review_file(key, result, review_state)
        if decision == "QUIT":
            break

    print(f"\nReview session complete.")
    show_status(review_state, corpus_state)


if __name__ == "__main__":
    main()
