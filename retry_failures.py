"""
Retry Extraction Failures
===========================

Identifies files with extraction failures (complete failures + chunk failures)
and prepares them for re-extraction via OpenRouter.

Three categories of failures:
1. Completely failed (in corpus_state.json["failed"])
2. Chunk failures with Ollama-only output — logged in corpus_full.log
3. Chunk failures with OpenRouter output — logged in openrouter_*.log

Strategy: parse extraction logs for "chunk(s) failed" warnings, associate
them with colony/year, remove those keys from state, then run
extraction_openrouter.py which picks them up as pending.

Usage:
    python retry_failures.py --scan              # scan and report all failures
    python retry_failures.py --prepare           # modify state file for re-extraction
    python retry_failures.py --prepare --dry-run # show what would change
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Local imports
sys.path.insert(0, str(Path(__file__).parent))
from extraction_corpus import (
    load_state, save_state, STATE_FILE, OUTPUT_DIR,
)

# Log files (OpenRouter logs in chronological order)
GENERATED = Path(__file__).parent / "generated"
OLLAMA_LOG = GENERATED / "corpus_full.log"
OPENROUTER_LOGS = [
    GENERATED / "openrouter_full.log",
    GENERATED / "openrouter_full_8w.log",
    GENERATED / "openrouter_full_8w_r2.log",
    GENERATED / "openrouter_full_8w_r3.log",
    GENERATED / "openrouter_full_8w_r4.log",
    GENERATED / "openrouter_full_8w_r5.log",
    GENERATED / "openrouter_final_303.log",
]

# Patterns for parsing log headers
_HEADER_RE = re.compile(r'^(\S.+?)\s+(\d{4})\s+\[(SMALL|STANDARD|LARGE|XLARGE)\]$')
_IDX_HEADER_RE = re.compile(
    r'^\[(\d+)/(\d+)\]\s+(\S.+?)\s+(\d{4})\s+\[(SMALL|STANDARD|LARGE|XLARGE)\]'
)
_CHUNK_FAIL_RE = re.compile(r'(\d+) chunk\(s\) failed: (.+)')


def _parse_log_failures(log_path: Path) -> dict[str, list[str]]:
    """Parse a single log file for chunk failure warnings.

    Returns {colony_year_key: [failed_dept_names]}.
    """
    failures = {}
    current_colony = None
    current_year = None

    if not log_path.exists():
        return failures

    with open(log_path) as f:
        for line in f:
            line = line.rstrip()

            # Try standard header: "Colony Year [TIER]"
            m = _HEADER_RE.match(line)
            if m:
                current_colony = m.group(1)
                current_year = int(m.group(2))
                continue

            # Try indexed header: "[N/M] Colony Year [TIER]"
            m = _IDX_HEADER_RE.match(line)
            if m:
                current_colony = m.group(3)
                current_year = int(m.group(4))
                continue

            # Check for chunk failure warning
            if 'chunk(s) failed:' in line and current_colony and current_year:
                m = _CHUNK_FAIL_RE.search(line)
                if m:
                    key = f"{current_colony}_{current_year}"
                    depts = [d.strip() for d in m.group(2).split(',')]
                    failures[key] = failures.get(key, []) + depts

    return failures


def scan_failures(verbose: bool = False) -> dict:
    """Scan all extraction logs for failures.

    Returns dict with:
        complete_failures: [(key, error)] — from state["failed"]
        ollama_chunk_failures: {key: [depts]} — Ollama-only, still unresolved
        openrouter_chunk_failures: {key: [depts]} — OpenRouter, latest-run failures
    """
    state = load_state()

    # 1. Complete failures from state
    complete_failures = [(k, v.get("error", "unknown")) for k, v in state["failed"].items()]

    # 2. Ollama chunk failures from corpus_full.log
    ollama_log = _parse_log_failures(OLLAMA_LOG)

    # Only keep Ollama failures where state still points to Ollama output
    # (if OpenRouter re-extracted it, the Ollama failure is superseded)
    ollama_chunk_failures = {}
    for k, depts in ollama_log.items():
        if k in state["completed"]:
            outf = state["completed"][k].get("output_file", "")
            if "openai_gpt-oss-120b" not in outf:
                ollama_chunk_failures[k] = depts

    # 3. OpenRouter chunk failures — use latest run per file
    # Process logs in chronological order; later runs overwrite earlier
    key_latest_outcome = {}  # key -> ('ok', []) or ('fail', [depts])

    for log_path in OPENROUTER_LOGS:
        if not log_path.exists():
            continue

        processed_in_run = set()
        failures_in_run = {}

        with open(log_path) as f:
            current_colony = current_year = None
            for line in f:
                line = line.rstrip()
                m = _HEADER_RE.match(line)
                if m:
                    current_colony, current_year = m.group(1), int(m.group(2))
                    continue
                m = _IDX_HEADER_RE.match(line)
                if m:
                    current_colony, current_year = m.group(3), int(m.group(4))
                    continue
                if current_colony and current_year:
                    key = f"{current_colony}_{current_year}"
                    if '— starting' in line or 'Saved:' in line:
                        processed_in_run.add(key)
                    if 'chunk(s) failed:' in line:
                        m2 = _CHUNK_FAIL_RE.search(line)
                        if m2:
                            depts = [d.strip() for d in m2.group(2).split(',')]
                            failures_in_run[key] = depts
                            processed_in_run.add(key)

        for key in processed_in_run:
            if key in failures_in_run:
                key_latest_outcome[key] = ('fail', failures_in_run[key])
            else:
                key_latest_outcome[key] = ('ok', [])

    # Only keep latest-run failures that are still in state['completed'] with OpenRouter output
    openrouter_chunk_failures = {}
    for k, (status, depts) in key_latest_outcome.items():
        if status == 'fail' and k in state["completed"]:
            openrouter_chunk_failures[k] = depts

    if verbose:
        for k, depts in sorted(ollama_chunk_failures.items()):
            print(f"  {k} [Ollama]: {', '.join(depts)}")
        for k, depts in sorted(openrouter_chunk_failures.items()):
            print(f"  {k} [OpenRouter]: {', '.join(depts)}")
        for k, err in complete_failures:
            print(f"  {k} [FAILED]: {err[:80]}")

    return {
        "complete_failures": complete_failures,
        "ollama_chunk_failures": ollama_chunk_failures,
        "openrouter_chunk_failures": openrouter_chunk_failures,
    }


def prepare_state(results: dict, dry_run: bool = False) -> int:
    """Remove failure keys from corpus_state.json so they'll be re-extracted.

    Returns the number of keys removed.
    """
    state = load_state()
    keys_to_remove = set()

    for k, _ in results["complete_failures"]:
        keys_to_remove.add(k)
    for k in results["ollama_chunk_failures"]:
        keys_to_remove.add(k)
    for k in results["openrouter_chunk_failures"]:
        keys_to_remove.add(k)

    if dry_run:
        from_completed = sum(1 for k in keys_to_remove if k in state['completed'])
        from_failed = sum(1 for k in keys_to_remove if k in state['failed'])
        print(f"\nDRY RUN — would remove {len(keys_to_remove)} keys from state:")
        print(f"  From completed: {from_completed}")
        print(f"  From failed:    {from_failed}")
        print(f"\nKeys:")
        for k in sorted(keys_to_remove):
            loc = ("completed" if k in state["completed"]
                   else "failed" if k in state["failed"]
                   else "not in state")
            print(f"  {k} ({loc})")
        return len(keys_to_remove)

    # Back up current state
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = STATE_FILE.with_suffix(f".backup_{ts}.json")
    with open(backup_file, 'w') as f:
        json.dump(state, f, indent=2, default=str)
    print(f"State backed up to: {backup_file}")

    removed_completed = 0
    removed_failed = 0
    for k in keys_to_remove:
        if k in state["completed"]:
            del state["completed"][k]
            removed_completed += 1
        if k in state["failed"]:
            del state["failed"][k]
            removed_failed += 1

    save_state(state)

    print(f"\nRemoved {removed_completed} from completed, {removed_failed} from failed")
    print(f"New state: {len(state['completed'])} completed, {len(state['failed'])} failed")
    print(f"\nThese {len(keys_to_remove)} files will be picked up as pending by extraction_openrouter.py")

    return len(keys_to_remove)


def main():
    parser = argparse.ArgumentParser(description="Retry extraction failures")
    parser.add_argument("--scan", action="store_true",
                        help="Scan and report all failures")
    parser.add_argument("--prepare", action="store_true",
                        help="Modify state file for re-extraction")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would change without modifying state")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show per-file details")
    args = parser.parse_args()

    if not args.scan and not args.prepare:
        parser.print_help()
        print("\nUse --scan to see failures, --prepare to modify state for retry")
        return

    print("=" * 60)
    print("EXTRACTION FAILURE SCAN")
    print("=" * 60)
    print(f"\nParsing extraction logs for chunk failures...\n")

    results = scan_failures(verbose=args.verbose)

    n_complete = len(results["complete_failures"])
    n_ollama = len(results["ollama_chunk_failures"])
    n_openrouter = len(results["openrouter_chunk_failures"])

    ollama_chunks = sum(len(d) for d in results["ollama_chunk_failures"].values())
    or_chunks = sum(len(d) for d in results["openrouter_chunk_failures"].values())

    # Dedup total
    all_keys = set()
    for k, _ in results["complete_failures"]:
        all_keys.add(k)
    all_keys.update(results["ollama_chunk_failures"])
    all_keys.update(results["openrouter_chunk_failures"])

    print(f"{'='*60}")
    print(f"FAILURE SUMMARY")
    print(f"{'='*60}")
    print(f"Complete failures:          {n_complete:>4} files")
    print(f"Ollama chunk failures:      {n_ollama:>4} files ({ollama_chunks} missing chunks)")
    print(f"OpenRouter chunk failures:  {n_openrouter:>4} files ({or_chunks} missing chunks)")
    print(f"{'─'*40}")
    print(f"TOTAL unique to retry:      {len(all_keys):>4} files")

    if args.scan and not args.prepare:
        # Top failing departments
        dept_counts = {}
        for depts in results["ollama_chunk_failures"].values():
            for d in depts:
                dept_counts[d] = dept_counts.get(d, 0) + 1
        for depts in results["openrouter_chunk_failures"].values():
            for d in depts:
                dept_counts[d] = dept_counts.get(d, 0) + 1

        if dept_counts:
            print(f"\nTop failing departments:")
            for dept, count in sorted(dept_counts.items(), key=lambda x: -x[1])[:15]:
                print(f"  {dept:<50} {count:>3}x")

        if n_complete > 0:
            print(f"\nComplete failures:")
            for k, err in results["complete_failures"]:
                print(f"  {k}: {err[:80]}")

    if args.prepare:
        print()
        prepare_state(results, dry_run=args.dry_run)

        if not args.dry_run:
            print(f"\nNext steps:")
            print(f"  python extraction_openrouter.py --cost-only  # estimate cost")
            print(f"  python extraction_openrouter.py --dry-run    # preview files")
            print(f"  python extraction_openrouter.py              # run extraction")


if __name__ == "__main__":
    main()
