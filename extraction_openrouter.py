"""
OpenRouter API Extraction — Parallel Batch Script
===================================================

Processes remaining corpus files via the OpenRouter API in parallel,
using the same extraction pipeline as the local Ollama process.

Reads corpus_state.json to find unprocessed files, runs them through
extract_chunked() with LLM_PROVIDER=openrouter, and writes results to
the same generated/ directory. File-level locking on corpus_state.json
prevents conflicts with the running local Ollama pipeline.

Usage:
    python extraction_openrouter.py                    # process all remaining files
    python extraction_openrouter.py --workers 8         # 8 parallel files
    python extraction_openrouter.py --year 1905         # only 1905
    python extraction_openrouter.py --colony Aden        # only one colony
    python extraction_openrouter.py --dry-run            # preview without calling API
    python extraction_openrouter.py --cost-only          # estimate cost without running
    python extraction_openrouter.py --max-cost 15.00     # stop after $15 spent
"""

import argparse
import json
import os
import signal
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

# Force OpenRouter provider before importing extraction modules
os.environ["LLM_PROVIDER"] = "openrouter"

# Local imports
sys.path.insert(0, str(Path(__file__).parent))
from scaffold_neo4j import scan_corpus, normalize_colony_name
from extraction_batch import strip_preamble
from extraction_ollama import extract_chunked, chunk_by_department, OllamaError
from extraction_corpus import (
    discover_corpus, sort_for_processing, classify_tier,
    load_state, save_state, state_key, process_file,
    TIER_TIMEOUTS, OUTPUT_DIR, STATE_FILE, SCRIPT_DIR,
)
from validation import validate_and_partition


# =============================================================================
# CONFIGURATION
# =============================================================================

DEFAULT_MODEL = "openai/gpt-oss-120b"

# Cost per million tokens (DeepInfra bf16 pricing)
COST_PER_M_INPUT = 0.039
COST_PER_M_OUTPUT = 0.19

# =============================================================================
# COST TRACKING
# =============================================================================

_cost_lock = threading.Lock()
_total_cost = 0.0
_total_input_tokens = 0
_total_output_tokens = 0
_files_processed = 0


def estimate_file_cost(source_file: Path) -> float:
    """Estimate API cost for a single file based on size."""
    try:
        text = source_file.read_text()
    except Exception:
        return 0.0
    staff_text = strip_preamble(text)
    chunks = chunk_by_department(staff_text)
    # Rough estimate: ~4 chars per token for input, ~200 output tokens per official,
    # ~1 official per 2 source lines
    total_input_chars = sum(len(c[1]) for c in chunks)
    # Each chunk also gets the prompt template (~2000 chars)
    total_input_chars += len(chunks) * 2000
    input_tokens = total_input_chars / 4
    source_lines = sum(len([l for l in c[1].split('\n') if l.strip()]) for c in chunks)
    output_tokens = (source_lines / 2) * 200
    cost = (input_tokens / 1_000_000 * COST_PER_M_INPUT +
            output_tokens / 1_000_000 * COST_PER_M_OUTPUT)
    return cost


# =============================================================================
# SIGNAL HANDLING
# =============================================================================

_shutdown_requested = False


def _signal_handler(signum, frame):
    global _shutdown_requested
    if _shutdown_requested:
        print("\n\nForce quit.")
        sys.exit(1)
    _shutdown_requested = True
    print("\n\nShutdown requested. Waiting for in-flight requests to finish...")


signal.signal(signal.SIGINT, _signal_handler)


# =============================================================================
# STATE MANAGEMENT (thread-safe wrappers)
# =============================================================================

_state_lock = threading.Lock()


def safe_load_state() -> dict:
    """Thread-safe state load."""
    with _state_lock:
        return load_state()


def safe_save_result(key: str, result: dict):
    """Thread-safe state update for a single completed/failed file."""
    with _state_lock:
        state = load_state()
        if result.get("error"):
            state["failed"][key] = {
                "error": result["error"],
                "timestamp": result["timestamp"],
                "tier": result.get("tier", "?"),
            }
            state["completed"].pop(key, None)
        else:
            state["completed"][key] = result
            state["failed"].pop(key, None)
        save_state(state)


def is_already_done(key: str, state: dict) -> bool:
    """Check if a file is already completed in state."""
    return key in state.get("completed", {})


# =============================================================================
# WORKER
# =============================================================================

def process_one(entry: dict, model: str, idx: int, total: int) -> dict:
    """Process a single file via OpenRouter. Called from thread pool."""
    global _total_cost, _total_input_tokens, _total_output_tokens, _files_processed

    colony = entry["colony"]
    year = entry["year"]
    key = state_key(colony, year)

    # Re-check state to avoid double-processing (another worker or local pipeline
    # may have completed this file since we built the pending list)
    current_state = safe_load_state()
    if is_already_done(key, current_state):
        print(f"  [{idx}/{total}] {colony} {year} — already done, skipping")
        return {"skipped": True}

    print(f"\n[{idx}/{total}] {colony} {year} [{entry['tier']}] — starting...")
    result = process_file(entry, model, current_state)

    # Save result to shared state
    safe_save_result(key, result)

    with _cost_lock:
        _files_processed += 1

    status = "DONE" if not result.get("error") else f"FAILED: {result['error'][:60]}"
    n = result.get("passed_officials", 0)
    t = result.get("generation_time", 0) or 0
    print(f"  [{idx}/{total}] {colony} {year} — {status} "
          f"({n} officials, {t:.0f}s)")

    return result


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="OpenRouter parallel batch extraction"
    )
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"OpenRouter model (default: {DEFAULT_MODEL})")
    parser.add_argument("--workers", type=int, default=4,
                        help="Number of parallel workers (default: 4)")
    parser.add_argument("--year", type=int,
                        help="Process only this year")
    parser.add_argument("--colony",
                        help="Process only this colony")
    parser.add_argument("--tier", choices=["SMALL", "STANDARD", "LARGE", "XLARGE"],
                        help="Process only this tier")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without calling API")
    parser.add_argument("--cost-only", action="store_true",
                        help="Estimate cost without running")
    parser.add_argument("--max-cost", type=float, default=0,
                        help="Stop after this much $ spent (0 = no limit)")
    parser.add_argument("--retry-failed", action="store_true",
                        help="Re-attempt previously failed files")
    args = parser.parse_args()

    # Validate API key
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key and not args.dry_run and not args.cost_only:
        print("ERROR: OPENROUTER_API_KEY environment variable not set")
        print("  export OPENROUTER_API_KEY='sk-or-v1-...'")
        sys.exit(1)

    print("=" * 60)
    print("OPENROUTER PARALLEL EXTRACTION")
    print("=" * 60)
    print(f"Model:   {args.model}")
    print(f"Workers: {args.workers}")
    print(f"Provider preference: bf16/fp16 quantization")
    if args.max_cost > 0:
        print(f"Cost cap: ${args.max_cost:.2f}")
    print()

    # Discover corpus
    files = discover_corpus(SCRIPT_DIR)
    print(f"Discovered {len(files)} total corpus files")

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

    # Remove SKIP tier
    files = [f for f in files if f["tier"] != "SKIP"]

    # Load state and filter completed
    state = safe_load_state()
    pending = []
    for entry in sort_for_processing(files):
        key = state_key(entry["colony"], entry["year"])
        if key in state["completed"] and not args.retry_failed:
            continue
        if key in state["failed"] and not args.retry_failed:
            continue
        pending.append(entry)

    already_done = len(files) - len(pending)
    print(f"\nPending: {len(pending)} files ({already_done} already completed)")

    if not pending:
        print("Nothing to process.")
        return

    # Cost estimate
    if args.cost_only or args.dry_run:
        print("\nEstimating cost...")
        total_est = 0.0
        for entry in pending:
            cost = estimate_file_cost(Path(entry["source_file"]))
            total_est += cost

        print(f"\nEstimated cost for {len(pending)} files:")
        print(f"  At DeepInfra bf16 (${COST_PER_M_INPUT}/${COST_PER_M_OUTPUT} per M tokens):")
        print(f"    ~${total_est:.2f}")
        print(f"  At higher-tier providers (5x):")
        print(f"    ~${total_est * 5:.2f}")

        if args.dry_run:
            print(f"\nFirst 20 files that would be processed:")
            for i, entry in enumerate(pending[:20]):
                cost = estimate_file_cost(Path(entry["source_file"]))
                print(f"  {i+1:>4}. {entry['colony']:<40} {entry['year']}  "
                      f"[{entry['tier']}]  ~${cost:.3f}")
            if len(pending) > 20:
                print(f"  ... ({len(pending) - 20} more)")
        return

    # Run parallel extraction
    print(f"\nStarting extraction with {args.workers} workers...")
    start_time = time.time()
    total = len(pending)
    completed_count = 0
    failed_count = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {}
        for i, entry in enumerate(pending):
            if _shutdown_requested:
                break
            future = executor.submit(process_one, entry, args.model, i + 1, total)
            futures[future] = entry

        for future in as_completed(futures):
            if _shutdown_requested:
                break
            entry = futures[future]
            try:
                result = future.result()
                if result.get("skipped"):
                    continue
                if result.get("error"):
                    failed_count += 1
                else:
                    completed_count += 1
            except Exception as e:
                failed_count += 1
                print(f"  ERROR processing {entry['colony']} {entry['year']}: {e}")

            # Check cost cap
            if args.max_cost > 0:
                with _cost_lock:
                    if _total_cost >= args.max_cost:
                        print(f"\nCost cap reached (${_total_cost:.2f} >= ${args.max_cost:.2f})")
                        executor.shutdown(wait=False, cancel_futures=True)
                        break

    elapsed = time.time() - start_time

    print(f"\n{'='*60}")
    print(f"SESSION COMPLETE")
    print(f"{'='*60}")
    print(f"Processed: {completed_count} succeeded, {failed_count} failed")
    print(f"Elapsed: {elapsed/60:.1f} minutes ({elapsed/3600:.2f} hours)")
    if completed_count > 0:
        print(f"Average: {elapsed/completed_count:.1f}s per file")

    # Final state summary
    final_state = safe_load_state()
    print(f"\nTotal corpus state: {len(final_state['completed'])} completed, "
          f"{len(final_state['failed'])} failed")


if __name__ == "__main__":
    main()
