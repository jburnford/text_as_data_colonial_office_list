"""
Batch Extraction — Sierra Leone Multi-Year Pipeline
=====================================================

Runs chunked extraction across all usable Sierra Leone source files
using gpt-oss:120b via Ollama. Processes in 4 batches with review
checkpoints between each.

Reuses extraction functions from extraction_ollama.py and evaluation
functions from benchmark_local_models.py.

Usage:
    python extraction_batch.py                      # run batch 1 (middle era)
    python extraction_batch.py --batch 2            # run batch 2 (transitional)
    python extraction_batch.py --batch all          # run all batches
    python extraction_batch.py --years 1896 1899    # run specific years
    python extraction_batch.py --dry-run             # show what would be extracted

Output:
    generated/sierra_leone_{year}_data_gpt-oss_120b_chunked.json  (per year)
    generated/sierra_leone_all_years.json                          (aggregate)
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path
from datetime import datetime

# Import from existing modules
sys.path.insert(0, str(Path(__file__).parent))
from extraction_ollama import extract_chunked, chunk_by_department
from benchmark_local_models import (
    evaluate_against_gold as evaluate_against_gemini_ref,
    stop_all_models, ollama_stop, ollama_list_running
)
from scaffold_neo4j import normalize_colony_name


def load_gemini_reference(filepath: str) -> list[dict]:
    """Load Gemini reference officials from JSON file."""
    with open(filepath) as f:
        data = json.load(f)
    return data.get("officials", data if isinstance(data, list) else [])


# =============================================================================
# CONFIGURATION
# =============================================================================

SCRIPT_DIR = Path(__file__).parent
GEMINI_REF_FILE = SCRIPT_DIR / "test_data" / "gold_standard.json"
OUTPUT_DIR = SCRIPT_DIR / "generated"

DEFAULT_MODEL = "gpt-oss:120b"

# All usable years (skip 1867 — just a cross-reference)
ALL_YEARS = [
    1879, 1880, 1883,              # Early
    1894, 1896, 1899,              # Middle
    1909, 1911, 1921, 1923,        # Transitional
    1946, 1948, 1950, 1951, 1953, 1958, 1960,  # Late
]

# Batches for staged processing
BATCHES = {
    1: {"name": "Middle era", "years": [1894, 1896, 1899]},
    2: {"name": "Transitional era", "years": [1909, 1911, 1921, 1923]},
    3: {"name": "Early era", "years": [1879, 1880, 1883]},
    4: {"name": "Late era", "years": [1946, 1948, 1950, 1951, 1953, 1958, 1960]},
}


# =============================================================================
# SOURCE FILE DISCOVERY
# =============================================================================

def find_source_file(year: int, colony_name: str = "sierra_leone") -> Path | None:
    """Find a colony source file for a given year.

    Args:
        year: The year to search
        colony_name: Colony filename stem (e.g. "sierra_leone", "hong_kong").
                     Also accepts canonical names like "Sierra Leone" which
                     get converted to filename form.

    Returns:
        Path to the source file, or None if not found.
    """
    # Convert canonical name to filename form
    stem = colony_name.lower().replace(" ", "_").replace("-", "_")

    year_dir = SCRIPT_DIR / f"{year}_manual_parsed"
    if not year_dir.exists():
        return None

    # Try the direct stem first
    for ext in ["txt", "md"]:
        path = year_dir / f"{stem}.{ext}"
        if path.exists():
            return path

    # Try variant forms: with/without common prefixes/suffixes
    variants = [stem]
    for prefix in ["the_", "british_"]:
        if stem.startswith(prefix):
            variants.append(stem[len(prefix):])
        else:
            variants.append(prefix + stem)
    for suffix in ["_colony", "_protectorate", "_ref"]:
        if stem.endswith(suffix):
            variants.append(stem[:-len(suffix)])
        else:
            variants.append(stem + suffix)

    for variant in variants:
        for ext in ["txt", "md"]:
            path = year_dir / f"{variant}.{ext}"
            if path.exists():
                return path

    # Brute-force: scan directory and match via normalize_colony_name
    canonical_target = normalize_colony_name(stem)
    for f in year_dir.iterdir():
        if f.suffix in [".txt", ".md"]:
            canonical_found = normalize_colony_name(f.stem)
            if canonical_found == canonical_target:
                return f

    return None


def discover_all_sources() -> dict[int, Path]:
    """Discover all available Sierra Leone source files."""
    sources = {}
    for year in ALL_YEARS:
        path = find_source_file(year, "sierra_leone")
        if path:
            sources[year] = path
    return sources


# =============================================================================
# PREAMBLE STRIPPING
# =============================================================================

# Cascading marker patterns for staff list start, in priority order.
# Each is tried in a full pass before falling back to the next.
_STAFF_LIST_MARKERS = [
    re.compile(r'CIVIL\s+ESTABLISHMENT|Civil\s+Establishment', re.IGNORECASE),
    re.compile(r'Executive\s+Council', re.IGNORECASE),
    re.compile(r'Legislative\s+Council', re.IGNORECASE),
    re.compile(r'GOVERNOR.*(?:COMMANDER|STAFF)|Governor.*(?:Commander|Staff)', re.IGNORECASE),
]

# Salary-line heuristic: matches "300l." or "£300" but NOT inside pipe-delimited tables
_SALARY_PATTERN = re.compile(r'\d+l\.|£\d+')
_TABLE_LINE = re.compile(r'^\s*\|')


def find_staff_list_start(text: str) -> int | None:
    """Find the line index where the staff list begins.

    Uses a cascading marker search (in priority order):
    1. "Civil Establishment"
    2. "Executive Council"
    3. "Legislative Council"
    4. "Governor ... Commander" / "Governor ... Staff"
    5. Salary-line heuristic (final fallback): first line containing a salary
       figure (e.g. "300l." or "£300") that is NOT inside a pipe-delimited
       table. Backs up 5 lines to catch the department header.

    All markers handle markdown headers (###), bold (**/__), and UPPERCASE.
    """
    lines = text.split('\n')

    # Try each marker pattern in priority order
    for pattern in _STAFF_LIST_MARKERS:
        for i, line in enumerate(lines):
            clean = re.sub(r'^#{1,6}\s+', '', line)
            clean = clean.replace('**', '').replace('__', '').strip()
            if pattern.search(clean):
                return i

    # Final fallback: salary-line heuristic
    for i, line in enumerate(lines):
        if _SALARY_PATTERN.search(line) and not _TABLE_LINE.match(line):
            # Back up 5 lines to catch the department header
            return max(0, i - 5)

    return None


def strip_preamble(text: str) -> str:
    """Remove preamble (geography, history, statistics) and return only
    the staff list portion of the source text.

    The staff list typically starts at "Civil Establishment" or
    "Executive Council" and continues to the end of the file.
    """
    start = find_staff_list_start(text)
    if start is None:
        print("  WARNING: Could not find staff list start, using full text")
        return text

    lines = text.split('\n')
    # Back up a few lines to catch any section header context
    start = max(0, start - 2)
    result = '\n'.join(lines[start:])
    preamble_lines = start
    total_lines = len(lines)
    print(f"  Stripped preamble: {preamble_lines} lines removed, "
          f"{total_lines - preamble_lines} lines kept")
    return result


# =============================================================================
# SINGLE YEAR EXTRACTION
# =============================================================================

def run_year(year: int, source_file: Path, model: str = DEFAULT_MODEL,
             timeout: int = 600, json_mode: bool = False,
             dry_run: bool = False) -> dict:
    """Extract officials from a single year's source file.

    Returns a results dict with year, officials count, timing, and
    any errors encountered.
    """
    result = {
        "year": year,
        "source_file": str(source_file),
        "model": model,
        "timestamp": datetime.now().isoformat(),
        "total_officials": 0,
        "departments": {},
        "generation_time": None,
        "error": None,
        "output_file": None,
    }

    print(f"\n{'='*60}")
    print(f"YEAR {year}")
    print(f"{'='*60}")
    print(f"Source: {source_file}")

    # Read source text
    with open(source_file, 'r') as f:
        full_text = f.read()

    # Strip preamble
    staff_text = strip_preamble(full_text)

    if not staff_text.strip():
        result["error"] = "Empty staff list after preamble stripping"
        print(f"  ERROR: {result['error']}")
        return result

    # Show chunking preview
    chunks = chunk_by_department(staff_text)
    print(f"  Departments detected: {len(chunks)}")
    for dept, text in chunks:
        line_count = len([l for l in text.split('\n') if l.strip()])
        print(f"    {dept} ({line_count} lines)")

    if dry_run:
        result["departments"] = {dept: len([l for l in text.split('\n') if l.strip()])
                                  for dept, text in chunks}
        print("  [DRY RUN — skipping extraction]")
        return result

    # Run extraction
    start = time.time()
    try:
        officials = extract_chunked(
            staff_text, model, "Sierra Leone", year,
            str(source_file), timeout=timeout,
            json_mode=json_mode
        )
        elapsed = time.time() - start
        result["generation_time"] = round(elapsed, 1)
        result["total_officials"] = len(officials)

        # Count officials per department
        for o in officials:
            dept = o.get("department") or "Unknown"
            result["departments"][dept] = result["departments"].get(dept, 0) + 1

        # Save output
        OUTPUT_DIR.mkdir(exist_ok=True)
        model_slug = model.replace(":", "_").replace("/", "_")
        output_file = OUTPUT_DIR / f"sierra_leone_{year}_data_{model_slug}_chunked.json"

        data = {
            "colony": "Sierra Leone",
            "year": year,
            "generated": datetime.now().isoformat(),
            "total_officials": len(officials),
            "officials": officials,
        }

        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)

        result["output_file"] = str(output_file)
        print(f"\n  Saved: {output_file}")
        print(f"  Total: {len(officials)} officials in {elapsed:.1f}s")

    except Exception as e:
        elapsed = time.time() - start
        result["generation_time"] = round(elapsed, 1)
        result["error"] = str(e)
        print(f"  ERROR: {e}")

    return result


# =============================================================================
# SPOT CHECK REPORT
# =============================================================================

def spot_check_report(results: list[dict], gemini_ref: list[dict] | None = None):
    """Print a summary report with per-department counts and sample entries.
    If Gemini reference is provided, validate the 1896 extraction against it.
    """
    print(f"\n{'='*70}")
    print("BATCH SUMMARY REPORT")
    print(f"{'='*70}")

    # Summary table
    print(f"\n{'Year':<8} {'Officials':>10} {'Depts':>8} {'Time':>10} {'Status':<20}")
    print("-" * 60)

    for r in results:
        year = r["year"]
        n = r["total_officials"]
        depts = len(r.get("departments", {}))
        t = f"{r['generation_time']}s" if r.get("generation_time") else "N/A"
        status = r.get("error", "OK") or "OK"
        if status != "OK":
            status = f"ERROR: {status[:30]}"
        print(f"{year:<8} {n:>10} {depts:>8} {t:>10} {status:<20}")

    # Department breakdown per year
    print(f"\n{'='*70}")
    print("DEPARTMENT COUNTS PER YEAR")
    print(f"{'='*70}")

    for r in results:
        if r.get("departments"):
            print(f"\n  {r['year']}:")
            for dept, count in sorted(r["departments"].items(), key=lambda x: x[0] or ""):
                print(f"    {dept}: {count}")

    # Sample entries
    for r in results:
        if r.get("output_file"):
            print(f"\n--- Sample entries for {r['year']} ---")
            try:
                with open(r["output_file"]) as f:
                    data = json.load(f)
                officials = data.get("officials", [])
                for o in officials[:3]:
                    name = o.get("name", "?")
                    pos = o.get("position", "?")
                    dept = o.get("department", "?")
                    sal = o.get("salary_min", "?")
                    print(f"  {name} — {pos} ({dept}), salary: {sal}")
                if len(officials) > 3:
                    print(f"  ... and {len(officials)-3} more")
            except Exception:
                pass

    # Gold standard validation for 1896
    if gemini_ref:
        for r in results:
            if r["year"] == 1896 and r.get("output_file"):
                print(f"\n{'='*70}")
                print("GEMINI REFERENCE COMPARISON (1896)")
                print(f"{'='*70}")
                try:
                    with open(r["output_file"]) as f:
                        data = json.load(f)
                    officials = data.get("officials", [])
                    ev = evaluate_against_gemini_ref(officials, gemini_ref)

                    print(f"  Recall:    {ev['recall']:.0%} ({ev['matched']}/{ev['total_gemini_ref']})")
                    print(f"  Precision: {ev['precision']:.0%} ({ev['matched']}/{ev['total_extracted']})")

                    for field_name, counts in ev["field_accuracy"].items():
                        if counts["total"] > 0:
                            pct = f"{counts['accuracy']:.0%}"
                            print(f"  {field_name}: {pct} ({counts['correct']}/{counts['total']})")

                    if ev.get("missed"):
                        print(f"\n  Missed ({len(ev['missed'])}):")
                        for name in ev["missed"]:
                            print(f"    - {name}")
                    if ev.get("extra"):
                        print(f"\n  Extra ({len(ev['extra'])}):")
                        for name in ev["extra"][:10]:
                            print(f"    - {name}")
                except Exception as e:
                    print(f"  ERROR validating: {e}")

    # Anomaly detection
    print(f"\n{'='*70}")
    print("ANOMALY FLAGS")
    print(f"{'='*70}")

    anomalies = []
    sorted_results = sorted([r for r in results if r["total_officials"] > 0],
                            key=lambda r: r["year"])

    for i, r in enumerate(sorted_results):
        n = r["total_officials"]
        year = r["year"]

        # Very low count
        if n < 10:
            anomalies.append(f"  {year}: Only {n} officials — possible extraction failure")

        # Fewer than previous year (bureaucracy generally grew)
        if i > 0:
            prev = sorted_results[i-1]
            if n < prev["total_officials"] * 0.5:
                anomalies.append(
                    f"  {year}: {n} officials vs {prev['total_officials']} in "
                    f"{prev['year']} — large drop, check for missing departments")

        # No departments detected
        if len(r.get("departments", {})) <= 1:
            anomalies.append(f"  {year}: Only {len(r.get('departments', {}))} department(s) detected")

    if anomalies:
        for a in anomalies:
            print(a)
    else:
        print("  None detected.")


# =============================================================================
# AGGREGATE
# =============================================================================

def aggregate_results(output_dir: Path = OUTPUT_DIR):
    """Combine all per-year JSON files into a single aggregate file."""
    all_data = {
        "colony": "Sierra Leone",
        "generated": datetime.now().isoformat(),
        "years": {},
    }

    model_slug = DEFAULT_MODEL.replace(":", "_").replace("/", "_")

    for year in ALL_YEARS:
        json_file = output_dir / f"sierra_leone_{year}_data_{model_slug}_chunked.json"
        if json_file.exists():
            with open(json_file) as f:
                data = json.load(f)
            all_data["years"][str(year)] = {
                "total_officials": data["total_officials"],
                "officials": data["officials"],
            }

    output_file = output_dir / "sierra_leone_all_years.json"
    with open(output_file, 'w') as f:
        json.dump(all_data, f, indent=2)

    print(f"\nAggregate saved: {output_file}")
    print(f"Years included: {len(all_data['years'])}")

    total = sum(y["total_officials"] for y in all_data["years"].values())
    print(f"Total officials across all years: {total}")

    # Summary table
    print(f"\n{'Year':<8} {'Officials':>10}")
    print("-" * 20)
    for year_str in sorted(all_data["years"].keys(), key=int):
        n = all_data["years"][year_str]["total_officials"]
        print(f"{year_str:<8} {n:>10}")

    return output_file


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Batch extraction of Sierra Leone Colonial Office List data"
    )
    parser.add_argument("--batch", default="1",
                        help="Batch number (1-4) or 'all' (default: 1)")
    parser.add_argument("--years", nargs="+", type=int,
                        help="Specific years to process (overrides --batch)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Ollama model (default: {DEFAULT_MODEL})")
    parser.add_argument("--timeout", type=int, default=600,
                        help="API timeout per chunk in seconds (default: 600)")
    parser.add_argument("--json-mode", action="store_true",
                        help="Use JSON extraction mode instead of code generation")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be extracted without running the model")
    parser.add_argument("--force", action="store_true",
                        help="Re-extract even if output file already exists")
    parser.add_argument("--aggregate", action="store_true",
                        help="Only aggregate existing results (no extraction)")
    args = parser.parse_args()

    # Aggregate-only mode
    if args.aggregate:
        aggregate_results()
        return

    # Determine which years to process
    if args.years:
        years = args.years
        batch_name = f"Custom ({', '.join(str(y) for y in years)})"
    elif args.batch == "all":
        years = ALL_YEARS
        batch_name = "All years"
    else:
        batch_num = int(args.batch)
        if batch_num not in BATCHES:
            print(f"ERROR: Invalid batch number {batch_num}. Choose 1-4 or 'all'.")
            sys.exit(1)
        batch = BATCHES[batch_num]
        years = batch["years"]
        batch_name = f"Batch {batch_num}: {batch['name']}"

    # Discover sources
    sources = discover_all_sources()
    missing = [y for y in years if y not in sources]
    if missing:
        print(f"WARNING: No source files found for years: {missing}")
        years = [y for y in years if y in sources]

    if not years:
        print("ERROR: No valid years to process.")
        sys.exit(1)

    # Load Gemini reference for 1896 validation
    gemini_ref = None
    if GEMINI_REF_FILE.exists() and 1896 in years:
        gemini_ref = load_gemini_reference(GEMINI_REF_FILE)

    print("=" * 60)
    print("SIERRA LEONE BATCH EXTRACTION")
    print("=" * 60)
    print(f"Batch:  {batch_name}")
    print(f"Years:  {', '.join(str(y) for y in years)}")
    print(f"Model:  {args.model}")
    mode = "JSON" if args.json_mode else "Code Generation"
    print(f"Mode:   Chunked {mode}")
    if args.dry_run:
        print("        [DRY RUN]")
    print()

    # Stop any running models before starting
    if not args.dry_run:
        print("Stopping any running models...")
        stop_all_models()

    # Process each year
    model_slug = args.model.replace(":", "_").replace("/", "_")
    all_results = []
    for i, year in enumerate(years):
        print(f"\n[{i+1}/{len(years)}] Processing {year}...")
        source_file = sources[year]

        # Skip if output already exists (unless --force)
        output_file = OUTPUT_DIR / f"sierra_leone_{year}_data_{model_slug}_chunked.json"
        if output_file.exists() and not args.force and not args.dry_run:
            print(f"  Output exists: {output_file}")
            print(f"  Skipping (use --force to re-extract)")
            with open(output_file) as f:
                data = json.load(f)
            result = {
                "year": year,
                "source_file": str(source_file),
                "model": args.model,
                "timestamp": data.get("generated", ""),
                "total_officials": data.get("total_officials", 0),
                "departments": {},
                "generation_time": None,
                "error": None,
                "output_file": str(output_file),
            }
            for o in data.get("officials", []):
                dept = o.get("department") or "Unknown"
                result["departments"][dept] = result["departments"].get(dept, 0) + 1
            all_results.append(result)
            continue

        result = run_year(
            year, source_file, model=args.model,
            timeout=args.timeout, json_mode=args.json_mode,
            dry_run=args.dry_run
        )
        all_results.append(result)

    # Spot check report
    spot_check_report(all_results, gemini_ref=gemini_ref)

    # Save batch results metadata
    OUTPUT_DIR.mkdir(exist_ok=True)
    batch_meta_file = OUTPUT_DIR / f"batch_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(batch_meta_file, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nBatch metadata saved: {batch_meta_file}")

    # Prompt for next step
    if not args.dry_run:
        print(f"\n{'='*60}")
        print("NEXT STEPS")
        print(f"{'='*60}")
        print("1. Review the output files and sample entries above")
        print("2. Check for anomalies in department counts")
        if 1896 in years and gemini_ref:
            print("3. Compare 1896 output against Gemini reference")
        print(f"4. Run next batch: python extraction_batch.py --batch <N>")
        print(f"5. After all batches: python extraction_batch.py --aggregate")


if __name__ == "__main__":
    main()
