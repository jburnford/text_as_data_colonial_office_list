#!/usr/bin/env python3
"""
Colonial Office List — Extraction Validation Framework
=======================================================

Discovers all generated extraction scripts, validates them against
the shared schema, runs plausibility checks, and compares against
gold standards where available.

Usage:
    python validation/validate_extractions.py
    python validation/validate_extractions.py --colony gold_coast
    python validation/validate_extractions.py --gold-standard
    python validation/validate_extractions.py --report

Output:
    validation/report.md — Per-file status, corpus-wide statistics, failure list
"""

import os
import sys
import json
import re
import importlib.util
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Add parent dir to path so we can import the schema
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from guides.schema import (
    validate_official,
    validate_officials_list,
    REQUIRED_FIELDS,
    ALL_FIELDS,
    SCHEMA_FIELDS,
)

EXTRACTION_DIR = BASE_DIR / "extraction"
GOLD_COAST_EXTRACTION_DIR = BASE_DIR / "gold_coast_extraction"
VALIDATION_DIR = BASE_DIR / "validation"
TEST_DATA_DIR = BASE_DIR / "test_data"


# =============================================================================
# DISCOVERY
# =============================================================================

def discover_extraction_scripts(extraction_dir: Path = EXTRACTION_DIR) -> list:
    """Find all extraction .py files in the extraction directory tree.

    Returns list of dicts with: path, colony, year, is_section, section_name
    """
    scripts = []

    if not extraction_dir.exists():
        return scripts

    for py_file in sorted(extraction_dir.rglob("*_extraction.py")):
        info = parse_extraction_filename(py_file)
        if info:
            scripts.append(info)

    # Also check gold_coast_extraction/generated/
    gc_generated = GOLD_COAST_EXTRACTION_DIR / "generated"
    if gc_generated.exists():
        for py_file in sorted(gc_generated.glob("*_extraction.py")):
            info = parse_extraction_filename(py_file)
            if info:
                info["source"] = "gold_coast_extraction"
                scripts.append(info)

    return scripts


def parse_extraction_filename(filepath: Path) -> dict:
    """Parse extraction script filename to extract metadata.

    Patterns:
        gold_coast_1867_extraction.py  → colony=gold_coast, year=1867
        1923_sec01_civil_establishment.py → year=1923, section
        1923_merge.py → year=1923, merge script
        gold_coast_1923_Medical_Department_extraction.py → section
    """
    stem = filepath.stem
    name = stem.replace("_extraction", "")

    # Try pattern: {colony}_{year}_{section}
    m = re.match(r'^([a-z_]+)_(\d{4})(?:_(.+))?$', name)
    if m:
        colony = m.group(1)
        year = int(m.group(2))
        section = m.group(3)
        return {
            "path": filepath,
            "colony": colony,
            "year": year,
            "is_section": section is not None and section not in ("merge",),
            "is_merge": section == "merge",
            "section_name": section,
            "source": "extraction",
        }

    # Try pattern: {year}_{section}
    m = re.match(r'^(\d{4})(?:_(.+))?$', name)
    if m:
        year = int(m.group(1))
        section = m.group(2)
        colony = filepath.parent.name
        return {
            "path": filepath,
            "colony": colony,
            "year": year,
            "is_section": section is not None and section not in ("merge",),
            "is_merge": section == "merge",
            "section_name": section,
            "source": "extraction",
        }

    return None


# =============================================================================
# VALIDATION
# =============================================================================

def validate_script(script_info: dict) -> dict:
    """Validate a single extraction script.

    Returns result dict with: status, message, official_count, errors, warnings
    """
    filepath = script_info["path"]
    result = {
        "path": str(filepath),
        "colony": script_info["colony"],
        "year": script_info["year"],
        "status": "pending",
        "message": "",
        "official_count": 0,
        "errors": [],
        "warnings": [],
        "schema_errors": 0,
    }

    # 1. Check syntax
    try:
        with open(filepath, 'r') as f:
            code = f.read()
        compile(code, str(filepath), 'exec')
    except SyntaxError as e:
        result["status"] = "syntax_error"
        result["message"] = f"Syntax error: {e}"
        result["errors"].append(str(e))
        return result

    # 2. Try to import and check OFFICIALS
    try:
        spec = importlib.util.spec_from_file_location(
            f"extraction_{script_info['colony']}_{script_info['year']}",
            filepath
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        result["status"] = "import_error"
        result["message"] = f"Import error: {e}"
        result["errors"].append(str(e))
        return result

    # 3. Check OFFICIALS exists
    if not hasattr(module, 'OFFICIALS'):
        result["status"] = "missing_officials"
        result["message"] = "Module has no OFFICIALS list"
        result["errors"].append("Missing OFFICIALS list")
        return result

    officials = module.OFFICIALS
    if not isinstance(officials, list):
        result["status"] = "invalid_type"
        result["message"] = f"OFFICIALS is {type(officials).__name__}, not list"
        result["errors"].append(f"OFFICIALS is not a list")
        return result

    if len(officials) == 0:
        result["status"] = "empty"
        result["message"] = "OFFICIALS list is empty"
        result["errors"].append("Empty OFFICIALS list")
        return result

    result["official_count"] = len(officials)

    # 4. Schema validation
    validation = validate_officials_list(officials)
    result["schema_errors"] = validation["error_count"]
    if validation["error_count"] > 0:
        for idx, errs in validation["errors"][:5]:  # Show first 5
            result["errors"].append(f"Official #{idx}: {'; '.join(errs)}")

    # 5. Plausibility checks
    result["warnings"].extend(plausibility_checks(officials, script_info))

    # 6. Determine overall status
    if result["schema_errors"] > 0 and result["schema_errors"] == len(officials):
        result["status"] = "all_invalid"
        result["message"] = f"All {len(officials)} officials have schema errors"
    elif result["schema_errors"] > 0:
        result["status"] = "partial_valid"
        result["message"] = (
            f"{len(officials)} officials, {result['schema_errors']} with errors"
        )
    else:
        result["status"] = "valid"
        result["message"] = f"Valid: {len(officials)} officials"

    return result


def plausibility_checks(officials: list, script_info: dict) -> list:
    """Run plausibility checks on extracted officials.

    Returns list of warning strings.
    """
    warnings = []
    year = script_info["year"]

    # Check: very few officials for year range (post-1900 should have many)
    if year >= 1900 and len(officials) < 5:
        warnings.append(
            f"Only {len(officials)} officials for {year} — expected more"
        )

    # Check: salary ranges
    for i, off in enumerate(officials):
        salary_min = off.get("salary_min")
        salary_max = off.get("salary_max")

        if salary_min is not None:
            if salary_min < 0:
                warnings.append(f"Official #{i}: negative salary_min={salary_min}")
            if year < 1940 and salary_min > 10000:
                warnings.append(
                    f"Official #{i}: salary_min={salary_min} seems high for {year}"
                )

    # Check: duplicate (name, position, department) triples
    seen = set()
    for i, off in enumerate(officials):
        key = (
            off.get("name", ""),
            off.get("position", ""),
            off.get("department", ""),
        )
        if key in seen:
            warnings.append(
                f"Official #{i}: duplicate entry {key[0]} / {key[1]}"
            )
        seen.add(key)

    # Check: all same department (suspicious)
    departments = set(off.get("department", "") for off in officials)
    if len(departments) == 1 and len(officials) > 10:
        warnings.append(
            f"All {len(officials)} officials in same department: {departments.pop()}"
        )

    return warnings


# =============================================================================
# GOLD STANDARD COMPARISON
# =============================================================================

def compare_gold_standard() -> dict:
    """Compare Sierra Leone 1896 extraction against gold standard.

    Returns comparison results dict.
    """
    gold_path = TEST_DATA_DIR / "gold_standard.json"
    if not gold_path.exists():
        return {"error": f"Gold standard not found: {gold_path}"}

    with open(gold_path) as f:
        gold_data = json.load(f)

    gold_officials = gold_data.get("officials", [])
    gold_names = {off["canonical_name"] for off in gold_officials}

    # Find Sierra Leone 1896 extraction
    sl_patterns = [
        EXTRACTION_DIR / "sierra_leone" / "1896_extraction.py",
        EXTRACTION_DIR / "sierra_leone" / "sierra_leone_1896_extraction.py",
        GOLD_COAST_EXTRACTION_DIR / "generated" / "sierra_leone_1896_extraction.py",
        BASE_DIR / "generated" / "sierra_leone_1896_extraction.py",
    ]

    extraction_path = None
    for p in sl_patterns:
        if p.exists():
            extraction_path = p
            break

    if extraction_path is None:
        return {
            "error": "Sierra Leone 1896 extraction not found",
            "searched": [str(p) for p in sl_patterns],
        }

    # Load extraction
    try:
        spec = importlib.util.spec_from_file_location("sl_1896", extraction_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        extracted = module.OFFICIALS
    except Exception as e:
        return {"error": f"Failed to load extraction: {e}"}

    extracted_names = {off.get("canonical_name", "") for off in extracted}

    # Compare
    true_positives = gold_names & extracted_names
    false_negatives = gold_names - extracted_names
    false_positives = extracted_names - gold_names

    recall = len(true_positives) / len(gold_names) if gold_names else 0
    precision = len(true_positives) / len(extracted_names) if extracted_names else 0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0

    return {
        "gold_standard_count": len(gold_officials),
        "extracted_count": len(extracted),
        "true_positives": len(true_positives),
        "false_negatives": len(false_negatives),
        "false_positives": len(false_positives),
        "recall": round(recall, 4),
        "precision": round(precision, 4),
        "f1": round(f1, 4),
        "missing_names": sorted(false_negatives),
        "extra_names": sorted(false_positives),
        "extraction_path": str(extraction_path),
    }


# =============================================================================
# GOLD COAST COMPARISON
# =============================================================================

def compare_gold_coast_json() -> dict:
    """Compare Gold Coast extraction scripts against existing JSON outputs.

    Returns comparison results.
    """
    json_dir = GOLD_COAST_EXTRACTION_DIR / "json"
    if not json_dir.exists():
        return {"error": "Gold Coast JSON directory not found"}

    results = {}
    for json_file in sorted(json_dir.glob("gold_coast_*.json")):
        year_match = re.search(r'gold_coast_(\d{4})', json_file.name)
        if not year_match:
            continue
        year = int(year_match.group(1))

        with open(json_file) as f:
            data = json.load(f)

        json_count = len(data.get("officials", []))

        # Look for corresponding extraction script
        script_patterns = [
            EXTRACTION_DIR / "gold_coast" / f"{year}_extraction.py",
            EXTRACTION_DIR / "gold_coast" / f"gold_coast_{year}_extraction.py",
        ]

        script_count = None
        for sp in script_patterns:
            if sp.exists():
                try:
                    spec = importlib.util.spec_from_file_location(f"gc_{year}", sp)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    script_count = len(module.OFFICIALS)
                except Exception:
                    pass
                break

        results[year] = {
            "json_count": json_count,
            "script_count": script_count,
            "match": script_count == json_count if script_count is not None else None,
        }

    return results


# =============================================================================
# REPORT GENERATION
# =============================================================================

def generate_report(results: list, gold_standard: dict = None,
                    gold_coast: dict = None) -> str:
    """Generate markdown validation report."""
    lines = []
    lines.append("# Colonial Office List — Extraction Validation Report")
    lines.append(f"\nGenerated: {datetime.now().isoformat()}")
    lines.append("")

    # Summary statistics
    total = len(results)
    valid = sum(1 for r in results if r["status"] == "valid")
    partial = sum(1 for r in results if r["status"] == "partial_valid")
    failures = sum(1 for r in results if r["status"] in (
        "syntax_error", "import_error", "missing_officials", "invalid_type",
        "empty", "all_invalid"
    ))
    total_officials = sum(r["official_count"] for r in results)
    total_warnings = sum(len(r["warnings"]) for r in results)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total scripts | {total} |")
    lines.append(f"| Valid | {valid} ({valid/total*100:.1f}%) |" if total else "| Valid | 0 |")
    lines.append(f"| Partial (some errors) | {partial} |")
    lines.append(f"| Failed | {failures} |")
    lines.append(f"| Total officials | {total_officials:,} |")
    lines.append(f"| Total warnings | {total_warnings} |")
    lines.append("")

    # Colony breakdown
    by_colony = defaultdict(list)
    for r in results:
        by_colony[r["colony"]].append(r)

    lines.append("## By Colony")
    lines.append("")
    lines.append("| Colony | Scripts | Officials | Valid | Errors | Warnings |")
    lines.append("|--------|---------|-----------|-------|--------|----------|")
    for colony in sorted(by_colony.keys()):
        colony_results = by_colony[colony]
        c_total = len(colony_results)
        c_officials = sum(r["official_count"] for r in colony_results)
        c_valid = sum(1 for r in colony_results if r["status"] == "valid")
        c_errors = sum(r["schema_errors"] for r in colony_results)
        c_warnings = sum(len(r["warnings"]) for r in colony_results)
        lines.append(
            f"| {colony} | {c_total} | {c_officials:,} | {c_valid} | "
            f"{c_errors} | {c_warnings} |"
        )
    lines.append("")

    # Gold standard comparison
    if gold_standard and "error" not in gold_standard:
        lines.append("## Gold Standard Comparison (Sierra Leone 1896)")
        lines.append("")
        lines.append(f"| Metric | Value |")
        lines.append(f"|--------|-------|")
        lines.append(f"| Gold standard officials | {gold_standard['gold_standard_count']} |")
        lines.append(f"| Extracted officials | {gold_standard['extracted_count']} |")
        lines.append(f"| True positives | {gold_standard['true_positives']} |")
        lines.append(f"| False negatives (missed) | {gold_standard['false_negatives']} |")
        lines.append(f"| False positives (extra) | {gold_standard['false_positives']} |")
        lines.append(f"| **Recall** | **{gold_standard['recall']:.1%}** |")
        lines.append(f"| **Precision** | **{gold_standard['precision']:.1%}** |")
        lines.append(f"| **F1** | **{gold_standard['f1']:.1%}** |")
        lines.append("")

        if gold_standard["missing_names"]:
            lines.append("### Missing from extraction:")
            for name in gold_standard["missing_names"]:
                lines.append(f"- {name}")
            lines.append("")

    # Failures
    failures_list = [r for r in results if r["status"] not in ("valid", "partial_valid")]
    if failures_list:
        lines.append("## Failures")
        lines.append("")
        for r in failures_list:
            lines.append(f"- **{r['path']}**: {r['status']} — {r['message']}")
        lines.append("")

    # Warnings
    warning_scripts = [(r, w) for r in results for w in r["warnings"]]
    if warning_scripts:
        lines.append("## Warnings")
        lines.append("")
        for r, w in warning_scripts[:50]:  # Cap at 50
            lines.append(f"- {r['colony']}/{r['year']}: {w}")
        if len(warning_scripts) > 50:
            lines.append(f"- ... and {len(warning_scripts) - 50} more")
        lines.append("")

    return "\n".join(lines)


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Validate Colonial Office List extraction scripts"
    )
    parser.add_argument("--colony", type=str, help="Validate only this colony")
    parser.add_argument("--gold-standard", action="store_true",
                        help="Compare against Sierra Leone 1896 gold standard")
    parser.add_argument("--gold-coast", action="store_true",
                        help="Compare against existing Gold Coast JSON outputs")
    parser.add_argument("--report", action="store_true",
                        help="Generate full report (default if no other flags)")
    parser.add_argument("--json", action="store_true",
                        help="Output results as JSON instead of report")
    args = parser.parse_args()

    print("=" * 70)
    print("COLONIAL OFFICE LIST — EXTRACTION VALIDATION")
    print("=" * 70)

    # Discover scripts
    print("\nDiscovering extraction scripts...")
    scripts = discover_extraction_scripts()
    print(f"  Found {len(scripts)} extraction scripts")

    # Filter by colony if specified
    if args.colony:
        scripts = [s for s in scripts if args.colony.lower() in s["colony"].lower()]
        print(f"  Filtered to {len(scripts)} scripts for '{args.colony}'")

    # Validate each script
    print("\nValidating scripts...")
    results = []
    for i, script_info in enumerate(scripts):
        result = validate_script(script_info)
        results.append(result)
        status_icon = {
            "valid": "OK",
            "partial_valid": "WARN",
        }.get(result["status"], "FAIL")
        print(f"  [{status_icon}] {script_info['colony']}/{script_info['year']}: "
              f"{result['message']}")

    # Gold standard comparison
    gold_standard = None
    if args.gold_standard or not (args.colony or args.gold_coast):
        print("\nComparing against gold standard...")
        gold_standard = compare_gold_standard()
        if "error" in gold_standard:
            print(f"  {gold_standard['error']}")
        else:
            print(f"  Recall: {gold_standard['recall']:.1%}, "
                  f"Precision: {gold_standard['precision']:.1%}, "
                  f"F1: {gold_standard['f1']:.1%}")

    # Gold Coast comparison
    gold_coast = None
    if args.gold_coast:
        print("\nComparing against Gold Coast JSON outputs...")
        gold_coast = compare_gold_coast_json()
        if isinstance(gold_coast, dict) and "error" in gold_coast:
            print(f"  {gold_coast['error']}")
        else:
            for year, data in sorted(gold_coast.items()):
                status = "MATCH" if data["match"] else (
                    "DIFF" if data["match"] is not None else "N/A"
                )
                print(f"  {year}: JSON={data['json_count']}, "
                      f"Script={data['script_count']} [{status}]")

    # Output
    if args.json:
        output = {
            "timestamp": datetime.now().isoformat(),
            "results": results,
            "gold_standard": gold_standard,
            "gold_coast": gold_coast,
        }
        print(json.dumps(output, indent=2, default=str))
    else:
        # Generate and save report
        report = generate_report(results, gold_standard, gold_coast)
        report_path = VALIDATION_DIR / "report.md"
        with open(report_path, 'w') as f:
            f.write(report)
        print(f"\nReport saved to: {report_path}")

    # Summary
    total = len(results)
    valid = sum(1 for r in results if r["status"] == "valid")
    officials = sum(r["official_count"] for r in results)
    failures = total - valid - sum(1 for r in results if r["status"] == "partial_valid")

    print(f"\n{'=' * 70}")
    print(f"VALIDATION COMPLETE: {valid}/{total} valid, "
          f"{failures} failures, {officials:,} total officials")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
