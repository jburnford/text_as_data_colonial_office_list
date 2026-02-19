"""
Full-Corpus Extraction Orchestrator
=====================================

Scales the extraction pipeline to ~2,900 colony-year files across 68 years
and ~133 colonies. Replaces extraction_batch.py for full-corpus runs.
extraction_batch.py stays as-is for Sierra Leone-specific work.

Features:
- File discovery via scan_corpus() / normalize_colony_name()
- Quality tiers (SKIP/SMALL/STANDARD/LARGE/XLARGE) by file size
- Precision-first processing order (1896 first)
- Checkpointing to corpus_state.json (survives restarts)
- Graceful SIGINT handling (finish current file, save state)
- Source-text validation with quarantine
- Per-file + progress + final logging

Usage:
    python extraction_corpus.py                         # run all (resume)
    python extraction_corpus.py --year 1896             # one year, all colonies
    python extraction_corpus.py --colony "Hong Kong"    # one colony, all years
    python extraction_corpus.py --tier STANDARD         # one tier only
    python extraction_corpus.py --dry-run               # preview what would run
    python extraction_corpus.py --report                # report from state
    python extraction_corpus.py --retry-failed          # re-attempt failed files
"""

import argparse
import json
import os
import signal
import sys
import time
from datetime import datetime
from pathlib import Path

# Local imports
sys.path.insert(0, str(Path(__file__).parent))
from scaffold_neo4j import scan_corpus, normalize_colony_name
from extraction_batch import find_staff_list_start, strip_preamble, find_source_file
from extraction_ollama import extract_chunked, chunk_by_department
from validation import validate_and_partition
from benchmark_local_models import stop_all_models


# =============================================================================
# CONFIGURATION
# =============================================================================

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "generated"
STATE_FILE = OUTPUT_DIR / "corpus_state.json"

DEFAULT_MODEL = "gpt-oss:120b"
REFERENCE_YEAR = 1896

# Quality tiers by file size (bytes)
TIER_THRESHOLDS = {
    "SKIP":     (0,      500),
    "SMALL":    (500,    5_000),
    "STANDARD": (5_000,  50_000),
    "LARGE":    (50_000, 200_000),
    "XLARGE":   (200_000, float('inf')),
}

# Processing order: precision-first
TIER_ORDER = ["STANDARD", "LARGE", "SMALL", "XLARGE"]

# Timeouts per tier (seconds per chunk)
TIER_TIMEOUTS = {
    "SMALL":    300,
    "STANDARD": 600,
    "LARGE":    900,
    "XLARGE":   1200,
}


# =============================================================================
# SIGNAL HANDLING
# =============================================================================

_shutdown_requested = False


def _signal_handler(signum, frame):
    global _shutdown_requested
    if _shutdown_requested:
        print("\n\nForce quit. State may be inconsistent.")
        sys.exit(1)
    _shutdown_requested = True
    print("\n\nShutdown requested. Finishing current file, then saving state...")


signal.signal(signal.SIGINT, _signal_handler)


# =============================================================================
# FILE DISCOVERY AND TIERING
# =============================================================================

def classify_tier(file_size: int) -> str:
    """Classify a file into a quality tier by size."""
    for tier, (lo, hi) in TIER_THRESHOLDS.items():
        if lo <= file_size < hi:
            return tier
    return "XLARGE"


def discover_corpus(repo_dir: Path) -> list[dict]:
    """Discover all colony-year files and classify into tiers.

    Returns list of dicts:
        {colony, year, source_file, file_size, tier, stem}
    """
    corpus = scan_corpus(repo_dir)
    files = []

    for year, entries in sorted(corpus.items()):
        year_dir = repo_dir / f"{year}_manual_parsed"
        for filename, stem, canonical in entries:
            source_file = year_dir / filename
            file_size = source_file.stat().st_size if source_file.exists() else 0
            tier = classify_tier(file_size)
            files.append({
                "colony": canonical,
                "year": year,
                "source_file": str(source_file),
                "file_size": file_size,
                "tier": tier,
                "stem": stem,
            })

    return files


def sort_for_processing(files: list[dict]) -> list[dict]:
    """Sort files in precision-first processing order.

    1. Reference year (1896), all colonies
    2. STANDARD tier, remaining years
    3. LARGE tier
    4. SMALL tier
    5. XLARGE tier last
    """
    # Separate reference year from rest
    ref_year = [f for f in files if f["year"] == REFERENCE_YEAR and f["tier"] != "SKIP"]
    rest = [f for f in files if f["year"] != REFERENCE_YEAR and f["tier"] != "SKIP"]

    # Sort each tier group by year then colony
    def by_year_colony(f):
        return (f["year"], f["colony"])

    ref_year.sort(key=by_year_colony)

    ordered = list(ref_year)
    for tier in TIER_ORDER:
        tier_files = [f for f in rest if f["tier"] == tier]
        tier_files.sort(key=by_year_colony)
        ordered.extend(tier_files)

    return ordered


# =============================================================================
# STATE MANAGEMENT
# =============================================================================

def load_state() -> dict:
    """Load checkpointed state from disk."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {
        "started": datetime.now().isoformat(),
        "last_updated": None,
        "completed": {},   # "colony_year" -> result dict
        "failed": {},      # "colony_year" -> error info
        "skipped": {},     # "colony_year" -> reason
    }


def save_state(state: dict):
    """Save state to disk."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    state["last_updated"] = datetime.now().isoformat()
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2, default=str)


def state_key(colony: str, year: int) -> str:
    return f"{colony}_{year}"


# =============================================================================
# SINGLE FILE EXTRACTION
# =============================================================================

def process_file(entry: dict, model: str, state: dict,
                 json_mode: bool = False) -> dict:
    """Extract officials from a single colony-year file.

    Returns a result dict with colony, year, officials count, timing, etc.
    """
    colony = entry["colony"]
    year = entry["year"]
    source_file = Path(entry["source_file"])
    tier = entry["tier"]
    timeout = TIER_TIMEOUTS.get(tier, 600)

    result = {
        "colony": colony,
        "year": year,
        "tier": tier,
        "source_file": str(source_file),
        "timestamp": datetime.now().isoformat(),
        "total_officials": 0,
        "passed_officials": 0,
        "quarantined_officials": 0,
        "departments": {},
        "generation_time": None,
        "validation_summary": None,
        "error": None,
        "output_file": None,
    }

    print(f"\n{'='*60}")
    print(f"{colony} {year} [{tier}]")
    print(f"{'='*60}")
    print(f"Source: {source_file} ({entry['file_size']:,} bytes)")

    # Read source text
    try:
        with open(source_file, 'r') as f:
            full_text = f.read()
    except Exception as e:
        result["error"] = f"Cannot read source file: {e}"
        print(f"  ERROR: {result['error']}")
        return result

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

    # Run extraction
    start = time.time()
    try:
        officials = extract_chunked(
            staff_text, model, colony, year,
            str(source_file), timeout=timeout,
            json_mode=json_mode
        )
        elapsed = time.time() - start
        result["generation_time"] = round(elapsed, 1)
        result["total_officials"] = len(officials)

        # Validate against source text
        passed, quarantined, val_summary = validate_and_partition(
            officials, staff_text, colony, year, verbose=True
        )
        result["passed_officials"] = len(passed)
        result["quarantined_officials"] = len(quarantined)
        result["validation_summary"] = val_summary

        # Count officials per department
        for o in passed:
            dept = o.get("department", "Unknown")
            result["departments"][dept] = result["departments"].get(dept, 0) + 1

        # Save output
        OUTPUT_DIR.mkdir(exist_ok=True)
        colony_slug = colony.lower().replace(" ", "_").replace("'", "")
        model_slug = model.replace(":", "_").replace("/", "_")

        # Save passed officials
        output_file = OUTPUT_DIR / f"{colony_slug}_{year}_data_{model_slug}.json"
        data = {
            "colony": colony,
            "year": year,
            "generated": datetime.now().isoformat(),
            "model": model,
            "tier": tier,
            "total_officials": len(passed),
            "officials": passed,
            "validation_summary": val_summary,
        }
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        result["output_file"] = str(output_file)

        # Save quarantined separately if any
        if quarantined:
            q_file = OUTPUT_DIR / f"{colony_slug}_{year}_quarantined_{model_slug}.json"
            with open(q_file, 'w') as f:
                json.dump({
                    "colony": colony, "year": year,
                    "total_quarantined": len(quarantined),
                    "officials": quarantined,
                }, f, indent=2)

        print(f"\n  Saved: {output_file}")
        print(f"  Total: {len(officials)} extracted, {len(passed)} passed, "
              f"{len(quarantined)} quarantined in {elapsed:.1f}s")

    except Exception as e:
        elapsed = time.time() - start
        result["generation_time"] = round(elapsed, 1)
        result["error"] = str(e)
        print(f"  ERROR: {e}")

    return result


# =============================================================================
# DRY RUN
# =============================================================================

def dry_run(files: list[dict]):
    """Preview what would be processed without running any extraction."""
    tier_counts = {}
    for f in files:
        tier_counts[f["tier"]] = tier_counts.get(f["tier"], 0) + 1

    print("\n" + "=" * 60)
    print("DRY RUN — Corpus Discovery")
    print("=" * 60)
    print(f"\nTotal files discovered: {len(files)}")
    print(f"\nTier breakdown:")
    for tier in ["SKIP", "SMALL", "STANDARD", "LARGE", "XLARGE"]:
        count = tier_counts.get(tier, 0)
        lo, hi = TIER_THRESHOLDS[tier]
        hi_str = f"{hi:,}" if hi != float('inf') else "∞"
        print(f"  {tier:<10} {count:>5} files  ({lo:,}–{hi_str} bytes)")

    # Processing order preview
    ordered = sort_for_processing(files)
    print(f"\nProcessing order ({len(ordered)} files, excluding SKIP):")

    # Show first 20 and last 5
    for i, f in enumerate(ordered[:20]):
        print(f"  {i+1:>4}. {f['colony']:<40} {f['year']}  [{f['tier']}]  "
              f"{f['file_size']:>8,} bytes")
    if len(ordered) > 25:
        print(f"  ... ({len(ordered) - 25} more) ...")
        for i, f in enumerate(ordered[-5:]):
            idx = len(ordered) - 5 + i + 1
            print(f"  {idx:>4}. {f['colony']:<40} {f['year']}  [{f['tier']}]  "
                  f"{f['file_size']:>8,} bytes")

    # Unique colonies and years
    colonies = set(f["colony"] for f in files)
    years = set(f["year"] for f in files)
    print(f"\nUnique colonies: {len(colonies)}")
    print(f"Unique years: {len(years)} ({min(years)}–{max(years)})")


# =============================================================================
# REPORT
# =============================================================================

def generate_report(state: dict):
    """Generate a summary report from the saved state."""
    print("\n" + "=" * 70)
    print("CORPUS EXTRACTION REPORT")
    print("=" * 70)
    print(f"Started: {state.get('started', 'N/A')}")
    print(f"Last updated: {state.get('last_updated', 'N/A')}")

    completed = state.get("completed", {})
    failed = state.get("failed", {})
    skipped = state.get("skipped", {})

    print(f"\nCompleted: {len(completed)}")
    print(f"Failed: {len(failed)}")
    print(f"Skipped: {len(skipped)}")

    if not completed:
        print("\nNo completed extractions yet.")
        return

    # Aggregate stats
    total_officials = 0
    total_passed = 0
    total_quarantined = 0
    total_time = 0.0
    tier_stats = {}

    for key, result in completed.items():
        n = result.get("total_officials", 0)
        p = result.get("passed_officials", 0)
        q = result.get("quarantined_officials", 0)
        t = result.get("generation_time", 0) or 0
        tier = result.get("tier", "?")

        total_officials += n
        total_passed += p
        total_quarantined += q
        total_time += t

        if tier not in tier_stats:
            tier_stats[tier] = {"count": 0, "officials": 0, "time": 0}
        tier_stats[tier]["count"] += 1
        tier_stats[tier]["officials"] += p
        tier_stats[tier]["time"] += t

    print(f"\nTotal officials extracted: {total_officials}")
    print(f"Total passed validation: {total_passed}")
    print(f"Total quarantined: {total_quarantined}")
    quarantine_pct = (total_quarantined / total_officials * 100) if total_officials else 0
    print(f"Quarantine rate: {quarantine_pct:.1f}%")
    print(f"Total processing time: {total_time/3600:.1f} hours")

    print(f"\nPer-tier stats:")
    print(f"  {'Tier':<10} {'Files':>6} {'Officials':>10} {'Time (hr)':>10}")
    print(f"  {'-'*40}")
    for tier in ["SMALL", "STANDARD", "LARGE", "XLARGE"]:
        s = tier_stats.get(tier, {"count": 0, "officials": 0, "time": 0})
        print(f"  {tier:<10} {s['count']:>6} {s['officials']:>10} {s['time']/3600:>10.1f}")

    # Anomaly flags
    anomaly_files = []
    for key, result in completed.items():
        vs = result.get("validation_summary", {})
        if vs:
            q_rate = vs.get("quarantined", 0) / max(vs.get("total", 1), 1)
            if q_rate > 0.1:
                anomaly_files.append((key, q_rate, vs))

    if anomaly_files:
        print(f"\nHigh quarantine rate (>10%) — {len(anomaly_files)} files:")
        anomaly_files.sort(key=lambda x: -x[1])
        for key, rate, vs in anomaly_files[:20]:
            print(f"  {key}: {rate:.0%} quarantined "
                  f"({vs.get('quarantined', 0)}/{vs.get('total', 0)})")

    if failed:
        print(f"\nFailed extractions ({len(failed)}):")
        for key, info in sorted(failed.items()):
            err = info.get("error", "unknown")[:60]
            print(f"  {key}: {err}")


# =============================================================================
# MAIN PROCESSING LOOP
# =============================================================================

def run_corpus(files: list[dict], model: str, state: dict,
               json_mode: bool = False, retry_failed: bool = False):
    """Process all files with checkpointing and progress logging."""
    ordered = sort_for_processing(files)
    total = len(ordered)

    # Filter already-completed files
    pending = []
    for entry in ordered:
        key = state_key(entry["colony"], entry["year"])
        if key in state["completed"] and not retry_failed:
            continue
        if key in state["failed"] and not retry_failed:
            continue
        pending.append(entry)

    if not pending:
        print("\nAll files already processed. Use --retry-failed to re-attempt failures.")
        return

    already_done = total - len(pending)
    print(f"\nProcessing {len(pending)} files ({already_done} already completed)")
    print(f"Model: {model}")
    print(f"Checkpointing to: {STATE_FILE}")

    # Stop any running models before starting
    print("Stopping any running models...")
    stop_all_models()

    start_time = time.time()

    for i, entry in enumerate(pending):
        if _shutdown_requested:
            print("\nShutdown requested. Saving state...")
            save_state(state)
            print(f"State saved. {i} files processed this session.")
            return

        key = state_key(entry["colony"], entry["year"])

        # Progress header
        global_idx = already_done + i + 1
        print(f"\n[{global_idx}/{total}] Processing {entry['colony']} {entry['year']} "
              f"[{entry['tier']}]...")

        # Process
        result = process_file(entry, model, state, json_mode=json_mode)

        # Save to state
        if result.get("error"):
            state["failed"][key] = {
                "error": result["error"],
                "timestamp": result["timestamp"],
                "tier": entry["tier"],
            }
            # Remove from completed if retrying
            state["completed"].pop(key, None)
        else:
            state["completed"][key] = result
            # Remove from failed if retrying
            state["failed"].pop(key, None)

        # Checkpoint after every file
        save_state(state)

        # Progress summary every 10 files
        if (i + 1) % 10 == 0:
            elapsed = time.time() - start_time
            avg_per_file = elapsed / (i + 1)
            remaining = avg_per_file * (len(pending) - i - 1)
            print(f"\n--- Progress: {i+1}/{len(pending)} this session, "
                  f"{global_idx}/{total} overall ---")
            print(f"    Elapsed: {elapsed/3600:.1f}h, "
                  f"ETA: {remaining/3600:.1f}h remaining")
            completed_count = len(state["completed"])
            failed_count = len(state["failed"])
            print(f"    Completed: {completed_count}, Failed: {failed_count}")

    # Final save
    save_state(state)

    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"SESSION COMPLETE")
    print(f"{'='*60}")
    print(f"Processed {len(pending)} files in {elapsed/3600:.1f}h")
    print(f"Total completed: {len(state['completed'])}")
    print(f"Total failed: {len(state['failed'])}")


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Full-corpus extraction orchestrator"
    )
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Ollama model (default: {DEFAULT_MODEL})")
    parser.add_argument("--year", type=int,
                        help="Process only this year")
    parser.add_argument("--colony",
                        help="Process only this colony (canonical name)")
    parser.add_argument("--tier", choices=["SMALL", "STANDARD", "LARGE", "XLARGE"],
                        help="Process only this tier")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview what would be processed")
    parser.add_argument("--report", action="store_true",
                        help="Generate report from saved state")
    parser.add_argument("--retry-failed", action="store_true",
                        help="Re-attempt previously failed files")
    parser.add_argument("--json-mode", action="store_true",
                        help="Use JSON extraction mode instead of code generation")
    parser.add_argument("--timeout", type=int,
                        help="Override per-chunk timeout (seconds)")
    args = parser.parse_args()

    # Report mode
    if args.report:
        state = load_state()
        generate_report(state)
        return

    # Discover corpus
    print("=" * 60)
    print("FULL-CORPUS EXTRACTION")
    print("=" * 60)
    print(f"\nScanning corpus at: {SCRIPT_DIR}")

    files = discover_corpus(SCRIPT_DIR)
    print(f"Discovered {len(files)} colony-year files")

    # Apply filters
    if args.year:
        files = [f for f in files if f["year"] == args.year]
        print(f"Filtered to year {args.year}: {len(files)} files")

    if args.colony:
        target = args.colony.lower()
        files = [f for f in files
                 if f["colony"].lower() == target or f["stem"].lower() == target]
        print(f"Filtered to colony '{args.colony}': {len(files)} files")

    if args.tier:
        files = [f for f in files if f["tier"] == args.tier]
        print(f"Filtered to tier {args.tier}: {len(files)} files")

    if not files:
        print("No files match the specified filters.")
        return

    # Override timeout if specified
    if args.timeout:
        for tier in TIER_TIMEOUTS:
            TIER_TIMEOUTS[tier] = args.timeout

    # Dry run
    if args.dry_run:
        dry_run(files)
        return

    # Load state and run
    state = load_state()
    run_corpus(files, args.model, state,
               json_mode=args.json_mode,
               retry_failed=args.retry_failed)

    # Generate report at end
    generate_report(state)


if __name__ == "__main__":
    main()
