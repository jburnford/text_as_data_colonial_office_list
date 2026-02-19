#!/usr/bin/env python3
"""
Live Progress Monitor for Sierra Leone Batch Extraction
========================================================

Watches the overnight log and generated JSON files to show real-time
progress of the extraction_batch.py --batch all run.

Usage:
    python monitor.py              # live updating display (every 10s)
    python monitor.py --once       # print once and exit
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "generated"
LOG_GLOB = "overnight_run_*.log"
MODEL_SLUG = "gpt-oss_120b"

ALL_YEARS = [
    1879, 1880, 1883,
    1894, 1896, 1899,
    1909, 1911, 1921, 1923,
    1946, 1948, 1950, 1951, 1953, 1958, 1960,
]

BATCHES = {
    1: ("Middle era",        [1894, 1896, 1899]),
    2: ("Transitional era",  [1909, 1911, 1921, 1923]),
    3: ("Early era",         [1879, 1880, 1883]),
    4: ("Late era",          [1946, 1948, 1950, 1951, 1953, 1958, 1960]),
}

# Batch processing order
BATCH_ORDER = [1, 2, 3, 4]


def find_log_file() -> Path | None:
    logs = sorted(OUTPUT_DIR.glob(LOG_GLOB))
    return logs[-1] if logs else None


def get_completed_years() -> dict[int, dict]:
    """Scan generated JSON files for completed years."""
    results = {}
    for year in ALL_YEARS:
        json_file = OUTPUT_DIR / f"sierra_leone_{year}_data_{MODEL_SLUG}_chunked.json"
        if json_file.exists():
            stat = json_file.stat()
            try:
                with open(json_file) as f:
                    data = json.load(f)
                results[year] = {
                    "officials": data.get("total_officials", 0),
                    "finished": datetime.fromtimestamp(stat.st_mtime),
                    "size": stat.st_size,
                }
            except (json.JSONDecodeError, KeyError):
                results[year] = {
                    "officials": 0,
                    "finished": datetime.fromtimestamp(stat.st_mtime),
                    "size": stat.st_size,
                }
    return results


def parse_log_tail(log_file: Path, tail_lines: int = 200) -> dict:
    """Parse the end of the log file for current progress."""
    info = {
        "current_year": None,
        "current_chunk": None,
        "total_chunks": None,
        "current_dept": None,
        "last_tok_s": None,
        "last_activity": None,
        "process_running": False,
    }

    # Check if process is still running
    try:
        import subprocess
        result = subprocess.run(
            ["pgrep", "-f", "extraction_batch.py"],
            capture_output=True, text=True, timeout=5
        )
        info["process_running"] = result.returncode == 0
    except Exception:
        pass

    if not log_file or not log_file.exists():
        return info

    # Read tail of log
    try:
        with open(log_file, 'rb') as f:
            # Seek to approximate tail position
            f.seek(0, 2)
            size = f.tell()
            seek_pos = max(0, size - 20000)
            f.seek(seek_pos)
            tail = f.read().decode('utf-8', errors='replace')
    except Exception:
        return info

    lines = tail.split('\n')

    # Find current year
    for line in reversed(lines):
        m = re.match(r'^YEAR (\d{4})', line)
        if m:
            info["current_year"] = int(m.group(1))
            break

    # Find current chunk
    for line in reversed(lines):
        m = re.search(r'Chunk (\d+)/(\d+): (.+) ---', line)
        if m:
            info["current_chunk"] = int(m.group(1))
            info["total_chunks"] = int(m.group(2))
            info["current_dept"] = m.group(3).strip()
            break

    # Find last tok/s
    for line in reversed(lines):
        m = re.search(r'([\d.]+) tok/s', line)
        if m:
            info["last_tok_s"] = float(m.group(1))
            break

    # Last activity timestamp from file mtime
    info["last_activity"] = datetime.fromtimestamp(log_file.stat().st_mtime)

    return info


def render(completed: dict, log_info: dict, start_time: datetime | None):
    """Render the progress display."""
    now = datetime.now()

    # Clear screen
    print("\033[2J\033[H", end="")

    print("╔══════════════════════════════════════════════════════════════╗")
    print("║        Sierra Leone Batch Extraction — Live Monitor        ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    # Process status
    if log_info["process_running"]:
        status = "\033[32m● RUNNING\033[0m"
    else:
        status = "\033[31m● STOPPED\033[0m"
    print(f"  Status: {status}")

    if log_info["last_activity"]:
        ago = now - log_info["last_activity"]
        if ago.total_seconds() < 60:
            ago_str = f"{int(ago.total_seconds())}s ago"
        else:
            ago_str = f"{int(ago.total_seconds() / 60)}m ago"
        print(f"  Last activity: {log_info['last_activity'].strftime('%H:%M:%S')} ({ago_str})")

    if log_info["last_tok_s"]:
        print(f"  Generation speed: {log_info['last_tok_s']:.1f} tok/s")

    # Overall progress
    done = len(completed)
    total = len(ALL_YEARS)
    pct = done / total * 100
    bar_len = 40
    filled = int(bar_len * done / total)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"\n  Overall: [{bar}] {done}/{total} years ({pct:.0f}%)")

    # Current work
    if log_info["current_year"] and log_info["current_year"] not in completed:
        yr = log_info["current_year"]
        chunk = log_info["current_chunk"] or "?"
        total_c = log_info["total_chunks"] or "?"
        dept = log_info["current_dept"] or "?"
        print(f"\n  Working on: {yr} — chunk {chunk}/{total_c}: {dept}")

    # Per-batch breakdown
    print(f"\n  {'Batch':<4} {'Era':<20} {'Years':<40} {'Done'}")
    print(f"  {'─'*4} {'─'*20} {'─'*40} {'─'*6}")

    for batch_num in BATCH_ORDER:
        name, years = BATCHES[batch_num]
        year_strs = []
        batch_done = 0
        for y in years:
            if y in completed:
                year_strs.append(f"\033[32m{y}✓\033[0m")
                batch_done += 1
            elif y == log_info.get("current_year"):
                year_strs.append(f"\033[33m{y}⟳\033[0m")
            else:
                year_strs.append(f"\033[90m{y}\033[0m")
        years_display = "  ".join(year_strs)
        print(f"  {batch_num:<4} {name:<20} {years_display}")

    # Completed years detail
    print(f"\n  {'Year':<8} {'Officials':>10} {'Finished':>12} {'Size':>10}")
    print(f"  {'─'*8} {'─'*10} {'─'*12} {'─'*10}")

    for year in ALL_YEARS:
        if year in completed:
            c = completed[year]
            fin = c["finished"].strftime("%H:%M:%S")
            size_kb = f"{c['size'] / 1024:.0f} KB"
            print(f"  {year:<8} {c['officials']:>10} {fin:>12} {size_kb:>10}")

    # Estimate time remaining
    if done > 0 and done < total:
        finished_times = sorted(c["finished"] for c in completed.values())
        if len(finished_times) >= 2:
            elapsed = (finished_times[-1] - finished_times[0]).total_seconds()
            # Exclude the first completed file from avg (it was already done)
            avg_per_year = elapsed / max(done - 1, 1)
            remaining = (total - done) * avg_per_year
            eta = now + timedelta(seconds=remaining)
            print(f"\n  Avg per year: {avg_per_year / 60:.0f} min")
            print(f"  Remaining: ~{remaining / 3600:.1f} hours ({total - done} years)")
            print(f"  ETA: {eta.strftime('%H:%M')}")

    # Total officials so far
    total_officials = sum(c["officials"] for c in completed.values())
    print(f"\n  Total officials extracted so far: {total_officials:,}")

    print(f"\n  \033[90mRefreshing every 10s — Ctrl+C to exit\033[0m")


def main():
    once = "--once" in sys.argv

    while True:
        log_file = find_log_file()
        completed = get_completed_years()
        log_info = parse_log_tail(log_file)

        render(completed, log_info, None)

        if once or not log_info["process_running"]:
            if not log_info["process_running"] and not once:
                print(f"\n  Process has finished!")
            break

        try:
            time.sleep(10)
        except KeyboardInterrupt:
            print("\n")
            break


if __name__ == "__main__":
    main()
