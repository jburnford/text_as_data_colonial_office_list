#!/usr/bin/env python3
"""
Sierra Leone Extraction Post-Processing Fixes
===============================================

Loads each JSON extraction file, applies targeted fixes, and writes
corrected output back. Keeps original generated code untouched while
producing clean data.

Fixes applied:
  1. Remove historical governor list from 1950 (28 false records)
  2. Resolve salary scales A-F to min/max ranges (1924-1940)
  3. Fix null-name records → set to "VACANT"
  4. Fix 1931 governor record (position text in name field)
  5. Fix known OCR misspellings
  6. Add notes to 1932 (truncated source)
  7. Add format-change metadata to 1952-1960

Usage:
    python extraction/sierra_leone/fix_extractions.py
    python extraction/sierra_leone/fix_extractions.py --dry-run
"""

import json
import os
import sys
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
JSON_DIR = SCRIPT_DIR / "json"
SCALES_PATH = SCRIPT_DIR / "salary_scales.json"
GAPS_PATH = SCRIPT_DIR / "known_gaps.json"


# =============================================================================
# SALARY SCALE DEFINITIONS
# =============================================================================

def load_salary_scales() -> dict:
    """Load salary scale definitions from JSON."""
    with open(SCALES_PATH) as f:
        data = json.load(f)
    return data["scales"], data["applicable_years"]


# =============================================================================
# FIX 1: Remove historical governors from 1950
# =============================================================================

def fix_1950_historical_governors(data: dict) -> dict:
    """Remove historical governor entries that pollute the 1950 data.

    The 1950 extraction incorrectly included the 'Governors since ...'
    list as current officials. These are all records with:
      - position == "Governor"
      - department == "Governor's Office - Sierra Leone"
      - no salary data (salary_min absent)

    The actual 1950 Governor (Beresford-Stooke) has salary data and
    department "Governor and Personal Staff - Sierra Leone".
    """
    if data.get("year") != 1950:
        return data

    original_count = len(data["officials"])
    filtered = []
    removed = []

    for official in data["officials"]:
        is_historical = (
            official.get("position") == "Governor"
            and official.get("department") == "Governor's Office - Sierra Leone"
            and official.get("salary_min") is None
        )
        if is_historical:
            removed.append(official.get("name", "?"))
        else:
            filtered.append(official)

    data["officials"] = filtered
    data["total_officials"] = len(filtered)

    if removed:
        print(f"  [1950] Removed {len(removed)} historical governors "
              f"({original_count} → {len(filtered)} records)")

    return data


# =============================================================================
# FIX 2: Resolve salary scales to min/max
# =============================================================================

def fix_salary_scales(data: dict, scales: dict, applicable: dict) -> dict:
    """Resolve scale letters (A-F) to salary_min/salary_max ranges.

    Only applies to years within the applicable range (1924-1940) where
    the scale definitions are well-documented.
    """
    year = data.get("year", 0)
    if year < applicable["min"] or year > applicable["max"]:
        return data

    resolved_count = 0
    for official in data["officials"]:
        scale = official.get("salary_scale")
        if scale and scale in scales:
            # Only fill in if salary_min/salary_max are not already set
            if official.get("salary_min") is None and official.get("salary_max") is None:
                official["salary_min"] = scales[scale]["salary_min"]
                official["salary_max"] = scales[scale]["salary_max"]
                resolved_count += 1

    if resolved_count:
        print(f"  [{year}] Resolved {resolved_count} salary scales to min/max ranges")

    return data


# =============================================================================
# FIX 3: Null-name records
# =============================================================================

def fix_null_names(data: dict) -> dict:
    """Set null or empty name fields to 'VACANT'."""
    fixed_count = 0
    for official in data["officials"]:
        if official.get("name") is None or official.get("name", "").strip() == "":
            official["name"] = "VACANT"
            official["canonical_name"] = "VACANT"
            official["surname"] = "VACANT"
            if "given_names" in official:
                official["given_names"] = None
            fixed_count += 1

    if fixed_count:
        print(f"  [{data.get('year')}] Fixed {fixed_count} null-name records → VACANT")

    return data


# =============================================================================
# FIX 4: 1931 governor record
# =============================================================================

def fix_1931_governor(data: dict) -> dict:
    """Fix the garbled governor record in 1931.

    Record #0 has name="Governor, Commander-in-Chief and Vice-Admiral"
    (the position was put in the name field). The actual governor in 1931
    was Sir Arnold W. Hodson, K.C.M.G. (confirmed from the 1932 RAG
    governors list: "1931. Sir Arnold W. Hodson, K.C.M.G.")
    """
    if data.get("year") != 1931:
        return data

    for official in data["officials"]:
        if (official.get("name") == "Governor, Commander-in-Chief and Vice-Admiral"
                and official.get("position") == "Governor, Commander-in-Chief and Vice-Admiral"):
            official["name"] = "Sir Arnold W. Hodson"
            official["canonical_name"] = "Hodson, Arnold W."
            official["given_names"] = "Arnold W."
            official["surname"] = "Hodson"
            official["honors"] = ["K.C.M.G."]
            print(f"  [1931] Fixed governor: → Sir Arnold W. Hodson, K.C.M.G.")
            break

    return data


# =============================================================================
# FIX 5: OCR misspellings
# =============================================================================

# Format: (year, field, wrong, correct)
OCR_FIXES = [
    # 1932: "Pritohard" → "Pritchard" (J. A. L.)
    {
        "year": 1932,
        "match": {"surname": "Pritohard"},
        "fix": {
            "name": lambda n: n.replace("Pritohard", "Pritchard"),
            "canonical_name": lambda n: n.replace("Pritohard", "Pritchard"),
            "surname": "Pritchard",
        },
    },
    # 1919: "Drawshtman" → "Draughtsman" (3 records)
    {
        "year": 1919,
        "match": {"position": "Drawshtman"},
        "fix": {
            "position": "Draughtsman",
        },
    },
    # 1899: "Cardow" → "Cardew" (Governor F. Cardew)
    {
        "year": 1899,
        "match": {"surname": "Cardow"},
        "fix": {
            "name": lambda n: n.replace("Cardow", "Cardew"),
            "canonical_name": lambda n: n.replace("Cardow", "Cardew"),
            "surname": "Cardew",
        },
    },
]


def fix_ocr_misspellings(data: dict) -> dict:
    """Fix known OCR misspellings in specific years."""
    year = data.get("year")
    year_fixes = [f for f in OCR_FIXES if f["year"] == year]
    if not year_fixes:
        return data

    total_fixed = 0
    for fix_def in year_fixes:
        for official in data["officials"]:
            # Check if this record matches the pattern
            match = True
            for field, value in fix_def["match"].items():
                if official.get(field) != value:
                    match = False
                    break

            if match:
                for field, correction in fix_def["fix"].items():
                    if callable(correction):
                        official[field] = correction(official.get(field, ""))
                    else:
                        official[field] = correction
                total_fixed += 1

    if total_fixed:
        print(f"  [{year}] Fixed {total_fixed} OCR misspelling(s)")

    return data


# =============================================================================
# FIX 6: Add notes to 1932
# =============================================================================

def fix_1932_note(data: dict) -> dict:
    """Add truncation note to the 1932 extraction."""
    if data.get("year") != 1932:
        return data

    data["notes"] = (
        "Source text truncated — only Railway and WAFF Battalion sections "
        "survived. ~330 officials missing compared to ~350 expected. "
        "Re-OCR from original PDF needed to recover full text."
    )
    print(f"  [1932] Added truncation note (18 records only)")
    return data


# =============================================================================
# FIX 7: Add format-change metadata to 1952-1960
# =============================================================================

FORMAT_CHANGE_YEARS = set(range(1952, 1960))


def fix_format_change_metadata(data: dict) -> dict:
    """Add metadata noting the post-1951 format change."""
    if data.get("year") not in FORMAT_CHANGE_YEARS:
        return data

    data["notes"] = (
        "Colonial Office List changed format after 1951. Post-1951 editions "
        "list only department heads and senior officials, not full civil "
        "establishments. Record counts are not comparable to pre-1952 years."
    )
    return data


# =============================================================================
# MAIN
# =============================================================================

def process_all(dry_run: bool = False):
    """Apply all fixes to all Sierra Leone JSON files."""
    print("=" * 60)
    print("SIERRA LEONE EXTRACTION POST-PROCESSING FIXES")
    print("=" * 60)

    if dry_run:
        print("*** DRY RUN — no files will be modified ***\n")

    # Load salary scales
    scales, applicable = load_salary_scales()
    print(f"Loaded {len(scales)} salary scale definitions "
          f"(years {applicable['min']}-{applicable['max']})")

    # Discover JSON files
    json_files = sorted(JSON_DIR.glob("sierra_leone_*.json"))
    print(f"Found {len(json_files)} JSON extraction files\n")

    # Statistics
    stats = {
        "files_processed": 0,
        "files_modified": 0,
        "governors_removed": 0,
        "scales_resolved": 0,
        "null_names_fixed": 0,
        "ocr_fixed": 0,
        "total_records_before": 0,
        "total_records_after": 0,
    }

    for json_path in json_files:
        with open(json_path) as f:
            data = json.load(f)

        year = data.get("year", 0)
        original_count = len(data.get("officials", []))
        stats["total_records_before"] += original_count
        original_json = json.dumps(data, sort_keys=True)

        print(f"Processing {json_path.name} ({original_count} records)...")

        # Apply fixes in order
        data = fix_1950_historical_governors(data)
        data = fix_salary_scales(data, scales, applicable)
        data = fix_null_names(data)
        data = fix_1931_governor(data)
        data = fix_ocr_misspellings(data)
        data = fix_1932_note(data)
        data = fix_format_change_metadata(data)

        new_count = len(data.get("officials", []))
        stats["total_records_after"] += new_count

        # Check if anything changed
        new_json = json.dumps(data, sort_keys=True)
        if new_json != original_json:
            stats["files_modified"] += 1
            if not dry_run:
                with open(json_path, 'w') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    f.write("\n")

        stats["files_processed"] += 1

    # Summary
    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    print(f"Files processed:  {stats['files_processed']}")
    print(f"Files modified:   {stats['files_modified']}")
    print(f"Records before:   {stats['total_records_before']:,}")
    print(f"Records after:    {stats['total_records_after']:,}")
    print(f"Records removed:  {stats['total_records_before'] - stats['total_records_after']}")

    if dry_run:
        print("\n*** DRY RUN — no files were modified ***")

    return stats


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    process_all(dry_run=dry_run)
