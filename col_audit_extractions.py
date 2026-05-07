#!/usr/bin/env python3
"""
COL Extraction Quality Audit
==============================

Systematic audit of extraction files and loaded Neo4j data to identify:
  1. Honours list contamination (honours lists parsed as colony staff)
  2. Count anomalies (spikes/collapses vs colony median)
  3. Missing Governor sections
  4. Empty extractions (0 officials)
  5. Dual extraction discrepancies (openai vs gpt-oss)
  6. Neo4j vs file count mismatches

Usage:
    python col_audit_extractions.py              # full audit, print to terminal
    python col_audit_extractions.py --report     # also write EXTRACTION_AUDIT_RESULTS.md
    python col_audit_extractions.py --colony X   # single colony
    python col_audit_extractions.py --year Y     # single year

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
from statistics import median, stdev, mean

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

from scaffold_neo4j import normalize_colony_name


# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
GENERATED_DIR = REPO_DIR / "generated"
BATCH_SIZE = 2000


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
# HONOURS VOCABULARY
# =============================================================================

HONOURS_DEPARTMENTS = {
    "knights grand cross", "knights commander", "commanders",
    "companions", "members", "honorary members",
    "knights bachelor", "imperial service order",
    "order of st. michael and st. george",
    "order of the british empire", "order of the bath",
    "order of the star of india", "order of the indian empire",
    "most distinguished order", "most honourable order",
    "most excellent order", "royal victorian order",
    "k.g.c.m.g.", "k.c.m.g.", "c.m.g.", "g.c.m.g.",
    "k.b.e.", "c.b.e.", "o.b.e.", "m.b.e.",
}

GOVERNOR_KEYWORDS = {
    "governor", "administrator", "high commissioner",
    "governor-general", "governor general",
    "officer administering", "acting governor",
    "lieutenant-governor", "lieutenant governor",
    "chief commissioner", "resident commissioner",
    "commissioner",
}


# =============================================================================
# FILE DISCOVERY & PARSING
# =============================================================================

def parse_extraction_filename(filename: str):
    """Parse extraction filename to get (colony_stem, year, model).

    Expected pattern: {colony_stem}_{year}_data_{model}.json
    """
    m = re.match(r'^(.+)_(\d{4})_data_(.+)\.json$', filename)
    if m:
        return m.group(1), int(m.group(2)), m.group(3)
    return None


def scan_extraction_files(year_filter=None, colony_filter=None):
    """Load each extraction JSON and compute per-file metrics.

    Returns list of dicts with keys:
        path, colony_stem, canonical_name, year, model,
        total, no_position_count, no_position_pct,
        has_governor, departments, is_quarantined
    """
    if not GENERATED_DIR.exists():
        print(f"WARNING: {GENERATED_DIR} does not exist")
        return []

    metrics = []
    for path in sorted(GENERATED_DIR.glob("*_data_*.json")):
        parsed = parse_extraction_filename(path.name)
        if not parsed:
            continue

        colony_stem, year, model = parsed
        canonical_name = normalize_colony_name(colony_stem)

        if year_filter is not None and year != year_filter:
            continue
        if colony_filter is not None and canonical_name != colony_filter:
            continue

        # Check for quarantined version
        quarantine_name = path.name.replace("_data_", "_quarantined_")
        is_quarantined = (GENERATED_DIR / quarantine_name).exists()

        try:
            with open(path) as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            metrics.append({
                "path": path,
                "colony_stem": colony_stem,
                "canonical_name": canonical_name,
                "year": year,
                "model": model,
                "total": -1,
                "error": str(e),
                "no_position_count": 0,
                "no_position_pct": 0.0,
                "has_governor": False,
                "departments": set(),
                "is_quarantined": is_quarantined,
            })
            continue

        officials = data.get("officials", [])
        total = len(officials)

        # Count nulls and detect governor
        no_position = 0
        has_governor = False
        departments = set()

        for off in officials:
            pos = off.get("position") or ""
            dept = off.get("department") or ""

            if not pos:
                no_position += 1
            else:
                pos_lower = pos.lower()
                for kw in GOVERNOR_KEYWORDS:
                    if kw in pos_lower:
                        has_governor = True
                        break

            if dept:
                departments.add(dept.lower())

        metrics.append({
            "path": path,
            "colony_stem": colony_stem,
            "canonical_name": canonical_name,
            "year": year,
            "model": model,
            "total": total,
            "no_position_count": no_position,
            "no_position_pct": (no_position / total * 100) if total > 0 else 0.0,
            "has_governor": has_governor,
            "departments": departments,
            "is_quarantined": is_quarantined,
        })

    return metrics


# =============================================================================
# COLONY BASELINES FROM NEO4J
# =============================================================================

def compute_colony_baselines(session):
    """Query Neo4j for per-colony median/mean/stddev of PersonRecord counts.

    Returns dict: {colony: {median, mean, stddev, counts: [per-year counts]}}
    """
    result = session.run(
        "MATCH (ty:COL_TerritoryYear) "
        "WHERE ty.stage1_loaded = true "
        "RETURN ty.name AS colony, ty.year AS year, ty.record_count AS count"
    )

    colony_counts = defaultdict(list)
    for r in result:
        count = r["count"]
        if count is not None and count > 0:
            colony_counts[r["colony"]].append(count)

    baselines = {}
    for colony, counts in colony_counts.items():
        if len(counts) >= 2:
            baselines[colony] = {
                "median": median(counts),
                "mean": mean(counts),
                "stddev": stdev(counts) if len(counts) >= 3 else 0.0,
                "counts": sorted(counts),
                "n": len(counts),
            }
        elif len(counts) == 1:
            baselines[colony] = {
                "median": counts[0],
                "mean": counts[0],
                "stddev": 0.0,
                "counts": counts,
                "n": 1,
            }

    return baselines


def fetch_neo4j_counts(session):
    """Get per (colony, year) PersonRecord counts from Neo4j.

    Returns dict: {(colony, year): count}
    """
    result = session.run(
        "MATCH (pr:COL_PersonRecord) "
        "RETURN pr.colony AS colony, pr.year AS year, count(pr) AS n "
    )
    counts = {}
    for r in result:
        counts[(r["colony"], r["year"])] = r["n"]
    return counts


# =============================================================================
# DETECTION FUNCTIONS
# =============================================================================

def detect_honours_contamination(metrics_list):
    """Flag files where honours list was parsed as colony staff.

    Criteria: >60% records have position=null AND department names
    match honours vocabulary.
    """
    flagged = []
    for m in metrics_list:
        if m["total"] <= 0:
            continue

        # Check honours vocabulary in departments
        dept_match = False
        for dept in m["departments"]:
            for vocab in HONOURS_DEPARTMENTS:
                if vocab in dept:
                    dept_match = True
                    break
            if dept_match:
                break

        if m["no_position_pct"] > 60 and dept_match:
            flagged.append({
                **m,
                "reason": f"{m['no_position_pct']:.0f}% no position, honours departments detected",
                "severity": "HIGH",
            })
        elif m["no_position_pct"] > 60 and m["total"] > 100:
            flagged.append({
                **m,
                "reason": f"{m['no_position_pct']:.0f}% no position ({m['total']} records)",
                "severity": "MEDIUM",
            })

    return flagged


def detect_count_anomalies(metrics_list, baselines):
    """Flag files with counts > 3x colony median (spike) or < 10% median (collapse)."""
    flagged = []

    # Group file metrics by colony
    by_colony = defaultdict(list)
    for m in metrics_list:
        by_colony[m["canonical_name"]].append(m)

    for colony, files in by_colony.items():
        baseline = baselines.get(colony)
        if not baseline or baseline["median"] < 5:
            continue

        med = baseline["median"]
        for m in files:
            if m["total"] <= 0:
                continue

            ratio = m["total"] / med
            if ratio > 3.0:
                flagged.append({
                    **m,
                    "reason": f"SPIKE: {m['total']} officials vs colony median {med:.0f} ({ratio:.1f}x)",
                    "severity": "HIGH" if ratio > 5.0 else "MEDIUM",
                    "ratio": ratio,
                })
            elif ratio < 0.1 and med > 20:
                flagged.append({
                    **m,
                    "reason": f"COLLAPSE: {m['total']} officials vs colony median {med:.0f} ({ratio:.2f}x)",
                    "severity": "MEDIUM",
                    "ratio": ratio,
                })

    return flagged


def detect_missing_governors(metrics_list):
    """Flag files with >30 officials but no Governor-class position."""
    flagged = []
    for m in metrics_list:
        if m["total"] > 30 and not m["has_governor"]:
            flagged.append({
                **m,
                "reason": f"{m['total']} officials but no Governor/Administrator/Commissioner found",
                "severity": "MEDIUM",
            })
    return flagged


def detect_empty_files(metrics_list):
    """Flag files with 0 officials or JSON parse errors."""
    flagged = []
    for m in metrics_list:
        if m["total"] == 0:
            flagged.append({
                **m,
                "reason": "Empty extraction (0 officials)",
                "severity": "HIGH",
            })
        elif m["total"] == -1:
            flagged.append({
                **m,
                "reason": f"JSON error: {m.get('error', 'unknown')}",
                "severity": "HIGH",
            })
    return flagged


def compare_dual_extractions(metrics_list):
    """Compare openai vs gpt-oss where both exist for same colony-year.

    Flag when one has >2x the count of the other.
    """
    # Group by (colony, year)
    by_ty = defaultdict(list)
    for m in metrics_list:
        by_ty[(m["canonical_name"], m["year"])].append(m)

    flagged = []
    for (colony, year), files in by_ty.items():
        if len(files) < 2:
            continue

        # Sort by total descending
        files.sort(key=lambda f: f["total"], reverse=True)
        biggest = files[0]
        smallest = files[-1]

        if smallest["total"] <= 0:
            flagged.append({
                **smallest,
                "reason": f"Dual extraction: {biggest['model']} has {biggest['total']}, "
                          f"this ({smallest['model']}) has {smallest['total']}",
                "severity": "HIGH",
                "other_model": biggest["model"],
                "other_total": biggest["total"],
            })
        elif biggest["total"] / max(smallest["total"], 1) > 2.0:
            ratio = biggest["total"] / smallest["total"]
            flagged.append({
                **smallest,
                "reason": f"Dual extraction discrepancy: {biggest['model']}={biggest['total']} vs "
                          f"{smallest['model']}={smallest['total']} ({ratio:.1f}x)",
                "severity": "MEDIUM",
                "other_model": biggest["model"],
                "other_total": biggest["total"],
            })

    return flagged


def detect_neo4j_mismatches(metrics_list, neo4j_counts):
    """Flag files where loaded count differs from extraction file count."""
    flagged = []

    # Build best-file index (prefer non-chunked, newest)
    best_files = {}
    for m in metrics_list:
        key = (m["canonical_name"], m["year"])
        if key not in best_files:
            best_files[key] = m
        else:
            existing = best_files[key]
            # Prefer non-chunked, then newest
            is_chunked = "_chunked" in str(m["path"])
            was_chunked = "_chunked" in str(existing["path"])
            if is_chunked and not was_chunked:
                continue
            if not is_chunked and was_chunked:
                best_files[key] = m
            elif m["path"].stat().st_mtime > existing["path"].stat().st_mtime:
                best_files[key] = m

    for (colony, year), m in best_files.items():
        neo4j_n = neo4j_counts.get((colony, year))
        if neo4j_n is None:
            continue  # Not loaded yet

        if m["total"] <= 0:
            continue

        diff = abs(neo4j_n - m["total"])
        if diff > 0 and diff / m["total"] > 0.1:
            flagged.append({
                **m,
                "reason": f"Neo4j has {neo4j_n} vs file has {m['total']} "
                          f"(diff={diff}, {diff/m['total']*100:.0f}%)",
                "severity": "LOW",
                "neo4j_count": neo4j_n,
            })

    return flagged


# =============================================================================
# REPORT GENERATION
# =============================================================================

def generate_report(results, write_file=False):
    """Print and optionally write markdown audit report."""

    lines = []
    lines.append("# Extraction Audit Results")
    lines.append(f"\nGenerated: {date.today().isoformat()}")
    lines.append("")

    # Summary
    total_flagged = sum(len(v) for v in results.values())
    lines.append(f"## Summary")
    lines.append("")
    lines.append(f"| Check | Flagged |")
    lines.append(f"|-------|---------|")
    for check, items in results.items():
        lines.append(f"| {check} | {len(items)} |")
    lines.append(f"| **Total** | **{total_flagged}** |")
    lines.append("")

    # Detail sections
    check_labels = {
        "honours_contamination": "Honours List Contamination",
        "count_anomalies": "Count Anomalies (Spikes/Collapses)",
        "missing_governors": "Missing Governor Section",
        "empty_files": "Empty/Broken Extractions",
        "dual_discrepancies": "Dual Extraction Discrepancies",
        "neo4j_mismatches": "Neo4j vs File Mismatches",
    }

    for check, items in results.items():
        label = check_labels.get(check, check)
        lines.append(f"## {label}")
        lines.append("")

        if not items:
            lines.append("None detected.")
            lines.append("")
            continue

        lines.append(f"| Colony | Year | Total | Severity | Reason |")
        lines.append(f"|--------|------|-------|----------|--------|")
        for item in sorted(items, key=lambda x: (x.get("severity", ""), x["canonical_name"], x["year"])):
            lines.append(
                f"| {item['canonical_name']} | {item['year']} | {item['total']} "
                f"| {item.get('severity', '')} | {item['reason']} |"
            )
        lines.append("")

    report_text = "\n".join(lines)

    # Print to terminal
    print("\n" + "=" * 70)
    print("EXTRACTION AUDIT RESULTS")
    print("=" * 70)

    for check, items in results.items():
        label = check_labels.get(check, check)
        print(f"\n--- {label}: {len(items)} flagged ---")
        for item in sorted(items, key=lambda x: (x.get("severity", ""), x["canonical_name"], x["year"])):
            print(f"  [{item.get('severity', '?')}] {item['canonical_name']} {item['year']} "
                  f"(n={item['total']}): {item['reason']}")

    print(f"\n{'=' * 70}")
    print(f"Total flagged: {total_flagged}")

    if write_file:
        report_path = REPO_DIR / "EXTRACTION_AUDIT_RESULTS.md"
        with open(report_path, "w") as f:
            f.write(report_text)
        print(f"\nReport written to {report_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Audit extraction quality across COL corpus"
    )
    parser.add_argument("--report", action="store_true",
                        help="Write EXTRACTION_AUDIT_RESULTS.md")
    parser.add_argument("--colony", type=str,
                        help="Filter to specific colony")
    parser.add_argument("--year", type=int,
                        help="Filter to specific year")
    args = parser.parse_args()

    print("=" * 60)
    print("COL EXTRACTION QUALITY AUDIT")
    print("=" * 60)

    # --- Scan extraction files ---
    print(f"\nScanning extraction files in {GENERATED_DIR}...")
    metrics = scan_extraction_files(
        year_filter=args.year,
        colony_filter=args.colony,
    )
    print(f"  {len(metrics)} extraction files found")

    if not metrics:
        print("No files to audit.")
        return

    # --- Connect to Neo4j ---
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        with driver.session() as session:
            # --- Compute baselines ---
            print("Computing colony baselines from Neo4j...")
            baselines = compute_colony_baselines(session)
            print(f"  {len(baselines)} colonies with baselines")

            # --- Fetch Neo4j counts ---
            print("Fetching Neo4j PersonRecord counts...")
            neo4j_counts = fetch_neo4j_counts(session)
            print(f"  {len(neo4j_counts)} (colony, year) pairs loaded")

        # --- Run all checks ---
        print("\nRunning checks...")

        results = {}

        results["honours_contamination"] = detect_honours_contamination(metrics)
        print(f"  Honours contamination: {len(results['honours_contamination'])} flagged")

        results["count_anomalies"] = detect_count_anomalies(metrics, baselines)
        print(f"  Count anomalies: {len(results['count_anomalies'])} flagged")

        results["missing_governors"] = detect_missing_governors(metrics)
        print(f"  Missing governors: {len(results['missing_governors'])} flagged")

        results["empty_files"] = detect_empty_files(metrics)
        print(f"  Empty/broken files: {len(results['empty_files'])} flagged")

        results["dual_discrepancies"] = compare_dual_extractions(metrics)
        print(f"  Dual discrepancies: {len(results['dual_discrepancies'])} flagged")

        results["neo4j_mismatches"] = detect_neo4j_mismatches(metrics, neo4j_counts)
        print(f"  Neo4j mismatches: {len(results['neo4j_mismatches'])} flagged")

        # --- Generate report ---
        generate_report(results, write_file=args.report)

    finally:
        driver.close()

    print("\nDone.")


if __name__ == "__main__":
    main()
