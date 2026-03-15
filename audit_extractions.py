"""
Extraction Completeness Audit
===============================

Verifies that all corpus source files have corresponding extraction output,
and checks department-level coverage for each output file.

Usage:
    python audit_extractions.py                # full audit
    python audit_extractions.py --threshold 20 # flag files with >20% dept gap
    python audit_extractions.py --year 1950    # audit only one year
    python audit_extractions.py --summary      # counts only, no per-file detail
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from extraction_batch import strip_preamble
from extraction_ollama import chunk_by_department
from extraction_corpus import (
    discover_corpus, state_key, load_state,
    OUTPUT_DIR, SCRIPT_DIR,
)


def find_output_file(colony: str, year: int) -> Path | None:
    """Find the best output JSON for a colony-year.

    Prefers OpenRouter output over Ollama output.
    """
    slug = colony.lower().replace(" ", "_").replace("'", "")
    openrouter = OUTPUT_DIR / f"{slug}_{year}_data_openai_gpt-oss-120b.json"
    ollama = OUTPUT_DIR / f"{slug}_{year}_data_gpt-oss_120b.json"

    if openrouter.exists():
        return openrouter
    if ollama.exists():
        return ollama
    return None


def audit_file(entry: dict) -> dict:
    """Audit a single colony-year file.

    Returns dict with:
        key, colony, year, tier, has_output, output_model,
        source_depts, output_depts, missing_depts, extra_depts,
        total_officials, coverage_pct
    """
    colony = entry["colony"]
    year = entry["year"]
    key = state_key(colony, year)
    source_file = Path(entry["source_file"])

    result = {
        "key": key,
        "colony": colony,
        "year": year,
        "tier": entry["tier"],
        "has_output": False,
        "output_model": None,
        "source_depts": 0,
        "output_depts": 0,
        "missing_depts": [],
        "extra_depts": [],
        "total_officials": 0,
        "coverage_pct": 100.0,
    }

    if entry["tier"] == "SKIP":
        result["coverage_pct"] = 100.0  # SKIP = intentionally no output
        return result

    # Find output
    output_path = find_output_file(colony, year)
    if not output_path:
        result["coverage_pct"] = 0.0
        return result

    result["has_output"] = True
    result["output_model"] = "openrouter" if "openai" in output_path.name else "ollama"

    # Load output
    try:
        with open(output_path) as f:
            data = json.load(f)
    except Exception:
        result["coverage_pct"] = 0.0
        return result

    officials = data.get("officials", [])
    result["total_officials"] = len(officials)

    # Get actual departments from output
    actual_depts = set()
    for o in officials:
        dept = o.get("department", "")
        if dept:
            actual_depts.add(dept)
    result["output_depts"] = len(actual_depts)

    # Get expected departments from source
    if not source_file.exists():
        return result

    try:
        full_text = source_file.read_text()
    except Exception:
        return result

    staff_text = strip_preamble(full_text)
    if not staff_text.strip():
        return result

    expected_chunks = chunk_by_department(staff_text)
    expected_depts = {dept for dept, _ in expected_chunks}
    result["source_depts"] = len(expected_depts)

    # Compare: fuzzy match
    missing = []
    for exp_dept in expected_depts:
        exp_lower = exp_dept.lower().strip()
        found = False
        for act_dept in actual_depts:
            act_lower = act_dept.lower().strip()
            if (exp_lower == act_lower or
                exp_lower in act_lower or
                act_lower in exp_lower):
                found = True
                break
        if not found:
            missing.append(exp_dept)

    result["missing_depts"] = missing
    if expected_depts:
        result["coverage_pct"] = round(
            100 * (len(expected_depts) - len(missing)) / len(expected_depts), 1
        )
    else:
        result["coverage_pct"] = 100.0

    return result


def main():
    parser = argparse.ArgumentParser(description="Audit extraction completeness")
    parser.add_argument("--threshold", type=float, default=0,
                        help="Flag files with coverage gap > N%% (default: show all)")
    parser.add_argument("--year", type=int, help="Audit only this year")
    parser.add_argument("--colony", help="Audit only this colony")
    parser.add_argument("--summary", action="store_true",
                        help="Summary counts only")
    args = parser.parse_args()

    print("=" * 60)
    print("EXTRACTION COMPLETENESS AUDIT")
    print("=" * 60)

    files = discover_corpus(SCRIPT_DIR)

    if args.year:
        files = [f for f in files if f["year"] == args.year]
    if args.colony:
        target = args.colony.lower()
        files = [f for f in files
                 if f["colony"].lower() == target or f["stem"].lower() == target]

    print(f"\nAuditing {len(files)} corpus files...")

    # Counters
    total = len(files)
    skip_tier = sum(1 for f in files if f["tier"] == "SKIP")
    expected = total - skip_tier

    has_output = 0
    perfect = 0      # 100% coverage
    partial = 0      # >0% but <100%
    no_output = 0    # 0% (no file or empty)
    total_officials = 0
    total_missing_chunks = 0

    flagged = []  # files exceeding threshold

    for f in files:
        if f["tier"] == "SKIP":
            continue

        result = audit_file(f)

        if result["has_output"]:
            has_output += 1
            total_officials += result["total_officials"]

        gap = 100 - result["coverage_pct"]

        if result["coverage_pct"] == 100.0 and result["has_output"]:
            perfect += 1
        elif result["has_output"]:
            partial += 1
            total_missing_chunks += len(result["missing_depts"])
        else:
            no_output += 1

        if gap > args.threshold and not args.summary:
            flagged.append(result)

    # Summary
    print(f"\n{'='*60}")
    print(f"AUDIT SUMMARY")
    print(f"{'='*60}")
    print(f"Total corpus files:      {total}")
    print(f"SKIP tier (no data):     {skip_tier}")
    print(f"Expected outputs:        {expected}")
    print(f"")
    print(f"Has output:              {has_output:>5} ({100*has_output/expected:.1f}%)")
    print(f"  Perfect coverage:      {perfect:>5}")
    print(f"  Partial coverage:      {partial:>5} ({total_missing_chunks} missing dept chunks)")
    print(f"No output:               {no_output:>5}")
    print(f"")
    print(f"Total officials:         {total_officials:,}")

    state = load_state()
    print(f"\nState file:")
    print(f"  Completed: {len(state['completed'])}")
    print(f"  Failed:    {len(state['failed'])}")

    if flagged and not args.summary:
        print(f"\n{'='*60}")
        gap_label = f"coverage gap > {args.threshold}%" if args.threshold else "any gap"
        print(f"FILES WITH {gap_label.upper()} ({len(flagged)} files)")
        print(f"{'='*60}")

        # Sort by coverage ascending
        flagged.sort(key=lambda r: r["coverage_pct"])

        for r in flagged:
            model_tag = f"[{r['output_model']}]" if r["output_model"] else "[MISSING]"
            print(f"\n  {r['key']} {model_tag}")
            print(f"    Coverage: {r['coverage_pct']:.0f}% "
                  f"({r['source_depts'] - len(r['missing_depts'])}/{r['source_depts']} depts)")
            print(f"    Officials: {r['total_officials']}")
            if r["missing_depts"]:
                print(f"    Missing: {', '.join(r['missing_depts'][:10])}"
                      f"{'...' if len(r['missing_depts']) > 10 else ''}")


if __name__ == "__main__":
    main()
