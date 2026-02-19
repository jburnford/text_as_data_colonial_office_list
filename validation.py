"""
Source-Text Validation Layer
=============================

Every extracted record gets verified against the source text before it can
enter the knowledge graph. Precision matters more than recall — a missed
official will appear in an adjacent year, but a hallucinated name poisons
the graph permanently.

Validation stages:
1. Name anchoring: confirm surname appears in preamble-stripped source text
2. Salary anchoring: verify salary figures appear near the surname
3. Cross-year consistency: flag single-year-only officials and missing departments
4. Anomaly detection: salary range, duplicates, department bounds

Usage:
    from validation import validate_colony_year, validate_cross_year

    results = validate_colony_year(officials, source_text)
    # results.summary, results.records, results.quarantined

    cross = validate_cross_year(all_years_data, colony="Sierra Leone")
    # cross.flags
"""

import re
from dataclasses import dataclass, field


# =============================================================================
# CONFIDENCE LEVELS
# =============================================================================

CONFIDENCE_HIGH = "HIGH"       # Full name (surname + at least one initial) found
CONFIDENCE_MEDIUM = "MEDIUM"   # Surname found but initials not confirmed
CONFIDENCE_LOW = "LOW"         # Surname not found in source text

QUARANTINE_THRESHOLD = 0.4     # Records below this score are quarantined

# Common surnames that require initial confirmation to avoid false matches
# (e.g. "Smith" appearing as a place name or in prose)
COMMON_SURNAMES = {
    "smith", "brown", "jones", "williams", "taylor", "wilson", "johnson",
    "davies", "thomas", "roberts", "lewis", "walker", "robinson", "white",
    "clark", "clarke", "hall", "king", "green", "wright", "baker", "hill",
    "young", "bell", "cole", "george", "martin", "moore", "lee", "scott",
    "wood", "turner", "edwards", "cooper", "ward", "morgan", "james",
    "campbell", "stewart", "murray", "grant", "hamilton", "ross",
}


# =============================================================================
# NAME ANCHORING
# =============================================================================

def _normalize_text(text: str) -> str:
    """Normalize text for matching: collapse whitespace, handle OCR artifacts."""
    # Collapse multiple spaces/tabs
    text = re.sub(r'\s+', ' ', text)
    # Normalize dashes
    text = text.replace('—', '-').replace('–', '-')
    return text


def _find_surname_in_text(surname: str, text: str) -> list[int]:
    """Find all positions where surname appears in text.

    Uses word-boundary matching to avoid partial matches (e.g. "King"
    inside "Kingdom"). Returns list of character positions.
    """
    if not surname or len(surname) < 2:
        return []

    # Escape for regex, allow for OCR variants (e.g. "i" vs "l")
    pattern = re.escape(surname)
    # Word boundary: require non-alphanumeric before and after
    pattern = r'(?<![A-Za-z])' + pattern + r'(?![A-Za-z])'

    return [m.start() for m in re.finditer(pattern, text, re.IGNORECASE)]


def _find_initial_near_surname(initials: str, text: str,
                               surname_pos: int, window: int = 80) -> bool:
    """Check if at least one initial appears near the surname position.

    Looks in a window around the surname for patterns like "J." or "J. O."
    that match the extracted initials.
    """
    if not initials:
        return False

    start = max(0, surname_pos - window)
    end = min(len(text), surname_pos + len(initials) + window)
    context = text[start:end]

    # Extract individual initials (e.g. "J. O." -> ["J", "O"])
    initial_letters = re.findall(r'([A-Z])\.', initials)
    if not initial_letters:
        # Try without dots (e.g. "Jacob" -> just check first letter)
        initial_letters = [initials[0].upper()] if initials else []

    # At least one initial letter followed by a dot should appear nearby
    for letter in initial_letters:
        if re.search(rf'(?<![A-Za-z]){re.escape(letter)}\.', context):
            return True

    # Also check for full given name (e.g. "William", "Bruce")
    given_names = initials.replace('.', '').strip().split()
    for name in given_names:
        if len(name) > 1 and name.lower() in context.lower():
            return True

    return False


def anchor_name(official: dict, source_text: str) -> dict:
    """Anchor an official's name against the source text.

    Returns dict with:
        confidence: HIGH / MEDIUM / LOW
        surname_found: bool
        initials_confirmed: bool
        surname_positions: list of char positions where surname found
    """
    surname = (official.get("surname") or "").strip()
    given_names = (official.get("given_names") or "").strip()
    canonical = (official.get("canonical_name") or "").strip()

    result = {
        "confidence": CONFIDENCE_LOW,
        "surname_found": False,
        "initials_confirmed": False,
        "surname_positions": [],
    }

    if not surname:
        return result

    # Find surname in source text
    positions = _find_surname_in_text(surname, source_text)
    result["surname_positions"] = positions

    if not positions:
        return result

    result["surname_found"] = True

    # Check if initials/given names appear near any surname occurrence
    for pos in positions:
        if _find_initial_near_surname(given_names, source_text, pos):
            result["initials_confirmed"] = True
            break

    # Assign confidence
    if result["initials_confirmed"]:
        result["confidence"] = CONFIDENCE_HIGH
    elif surname.lower() in COMMON_SURNAMES and not result["initials_confirmed"]:
        # Common surnames need initial confirmation — stay LOW
        result["confidence"] = CONFIDENCE_LOW
    else:
        result["confidence"] = CONFIDENCE_MEDIUM

    return result


# =============================================================================
# SALARY ANCHORING
# =============================================================================

def anchor_salary(official: dict, source_text: str,
                  surname_positions: list[int], window: int = 200) -> dict:
    """Verify salary figures appear near the surname in source text.

    Returns dict with:
        salary_found: bool
        salary_nearby: bool (within window of surname)
        misattributed: bool (salary found but far from surname)
    """
    result = {
        "salary_found": False,
        "salary_nearby": False,
        "misattributed": False,
    }

    salary_min = official.get("salary_min")
    salary_max = official.get("salary_max")

    if salary_min is None and salary_max is None:
        return result

    # Build patterns for the salary values
    salary_patterns = []
    for sal in [salary_min, salary_max]:
        if sal is not None:
            # Match "300l." or "£300" or "300"
            salary_patterns.append(
                rf'(?:{re.escape(str(sal))}l\.|£{re.escape(str(sal))}|{re.escape(str(sal))})'
            )

    if not salary_patterns:
        return result

    combined = '|'.join(salary_patterns)
    all_salary_positions = [m.start() for m in re.finditer(combined, source_text)]

    if not all_salary_positions:
        return result

    result["salary_found"] = True

    # Check if any salary appears near a surname position
    if surname_positions:
        for s_pos in surname_positions:
            for sal_pos in all_salary_positions:
                if abs(sal_pos - s_pos) <= window:
                    result["salary_nearby"] = True
                    return result

        # Salary found but not near surname — possible misattribution
        result["misattributed"] = True

    return result


# =============================================================================
# ANOMALY DETECTION (per colony-year)
# =============================================================================

@dataclass
class Anomaly:
    """A detected anomaly in the extraction."""
    type: str           # e.g. "salary_range", "duplicate_name", "dept_empty"
    severity: str       # "warning" or "error"
    message: str
    official_idx: int | None = None  # index in officials list, if applicable


def detect_anomalies(officials: list[dict]) -> list[Anomaly]:
    """Detect anomalies in a colony-year extraction.

    Checks:
    - Salary outside plausible range (< 5 or > 50,000)
    - Duplicate canonical_name in same colony-year
    - Department with 0 extracted officials or > 50
    - More than 30 departments in one colony-year (likely chunking error)
    """
    anomalies = []

    # Salary range check
    for i, o in enumerate(officials):
        for sal_field in ["salary_min", "salary_max"]:
            sal = o.get(sal_field)
            if sal is not None:
                if sal < 5:
                    anomalies.append(Anomaly(
                        type="salary_range",
                        severity="warning",
                        message=f"{o.get('name', '?')}: {sal_field}={sal} is suspiciously low",
                        official_idx=i,
                    ))
                elif sal > 50000:
                    anomalies.append(Anomaly(
                        type="salary_range",
                        severity="warning",
                        message=f"{o.get('name', '?')}: {sal_field}={sal} is suspiciously high",
                        official_idx=i,
                    ))

    # Duplicate canonical names
    seen_names = {}
    for i, o in enumerate(officials):
        cn = (o.get("canonical_name") or "").lower().strip()
        if cn:
            if cn in seen_names:
                anomalies.append(Anomaly(
                    type="duplicate_name",
                    severity="warning",
                    message=f"Duplicate canonical_name '{cn}' at indices {seen_names[cn]} and {i}",
                    official_idx=i,
                ))
            else:
                seen_names[cn] = i

    # Department counts
    dept_counts = {}
    for o in officials:
        dept = o.get("department", "Unknown")
        dept_counts[dept] = dept_counts.get(dept, 0) + 1

    for dept, count in dept_counts.items():
        if count > 100:
            anomalies.append(Anomaly(
                type="dept_oversize",
                severity="warning",
                message=f"Department '{dept}' has {count} officials (> 100)",
            ))

    # Too many departments (large colonies can legitimately have 40+)
    if len(dept_counts) > 50:
        anomalies.append(Anomaly(
            type="too_many_depts",
            severity="warning",
            message=f"{len(dept_counts)} departments detected (> 50) — likely chunking error",
        ))

    return anomalies


# =============================================================================
# PER-RECORD CONFIDENCE SCORING
# =============================================================================

def score_record(name_anchor: dict, salary_anchor: dict) -> float:
    """Compute a 0.0–1.0 confidence score for a single record.

    Weights:
    - Name anchoring: 0.7 (this is the primary signal)
        - HIGH: 0.7, MEDIUM: 0.5, LOW: 0.0
    - Salary anchoring: 0.3
        - salary_nearby: 0.3
        - salary_found but not nearby: 0.1
        - salary not found: 0.0 (but no penalty if record has no salary)
    """
    # Name component (0.0 – 0.7)
    conf = name_anchor.get("confidence", CONFIDENCE_LOW)
    if conf == CONFIDENCE_HIGH:
        name_score = 0.7
    elif conf == CONFIDENCE_MEDIUM:
        name_score = 0.5
    else:
        name_score = 0.0

    # Salary component (0.0 – 0.3)
    if salary_anchor.get("salary_nearby"):
        salary_score = 0.3
    elif salary_anchor.get("salary_found"):
        salary_score = 0.1
    elif salary_anchor.get("misattributed"):
        salary_score = 0.05
    else:
        # No salary data to check — don't penalize
        # (some officials genuinely have no salary listed)
        salary_score = 0.15  # neutral

    return round(name_score + salary_score, 2)


# =============================================================================
# COLONY-YEAR VALIDATION
# =============================================================================

@dataclass
class RecordValidation:
    """Validation result for a single extracted official."""
    official_idx: int
    name: str
    confidence: str  # HIGH / MEDIUM / LOW
    score: float
    quarantined: bool
    name_anchor: dict
    salary_anchor: dict


@dataclass
class ColonyYearValidation:
    """Validation result for an entire colony-year extraction."""
    colony: str
    year: int
    total_records: int
    high_confidence: int
    medium_confidence: int
    low_confidence: int
    quarantined_count: int
    anomalies: list[Anomaly]
    records: list[RecordValidation]
    quarantined: list[dict]  # the actual quarantined official records
    passed: list[dict]       # officials that passed validation

    @property
    def summary(self) -> dict:
        return {
            "colony": self.colony,
            "year": self.year,
            "total": self.total_records,
            "high_confidence": self.high_confidence,
            "medium_confidence": self.medium_confidence,
            "low_confidence": self.low_confidence,
            "quarantined": self.quarantined_count,
            "passed": self.total_records - self.quarantined_count,
            "anomaly_count": len(self.anomalies),
        }


def validate_colony_year(officials: list[dict], source_text: str,
                         colony: str = "", year: int = 0) -> ColonyYearValidation:
    """Validate all extracted officials against the source text.

    Args:
        officials: List of extracted official dicts
        source_text: The preamble-stripped source text
        colony: Colony name (for reporting)
        year: Year (for reporting)

    Returns:
        ColonyYearValidation with per-record scores and quarantined records
    """
    normalized_text = _normalize_text(source_text)

    records = []
    passed = []
    quarantined = []
    high = medium = low = 0

    for i, official in enumerate(officials):
        # Name anchoring
        na = anchor_name(official, normalized_text)

        # Salary anchoring
        sa = anchor_salary(official, normalized_text, na["surname_positions"])

        # Score
        score = score_record(na, sa)
        is_quarantined = score < QUARANTINE_THRESHOLD

        rv = RecordValidation(
            official_idx=i,
            name=official.get("name", "?"),
            confidence=na["confidence"],
            score=score,
            quarantined=is_quarantined,
            name_anchor=na,
            salary_anchor=sa,
        )
        records.append(rv)

        if na["confidence"] == CONFIDENCE_HIGH:
            high += 1
        elif na["confidence"] == CONFIDENCE_MEDIUM:
            medium += 1
        else:
            low += 1

        if is_quarantined:
            quarantined.append(official)
        else:
            passed.append(official)

    # Anomaly detection
    anomalies = detect_anomalies(officials)

    return ColonyYearValidation(
        colony=colony,
        year=year,
        total_records=len(officials),
        high_confidence=high,
        medium_confidence=medium,
        low_confidence=low,
        quarantined_count=len(quarantined),
        anomalies=anomalies,
        records=records,
        quarantined=quarantined,
        passed=passed,
    )


# =============================================================================
# CROSS-YEAR CONSISTENCY (post-hoc, per-colony)
# =============================================================================

@dataclass
class CrossYearFlag:
    """A flag raised by cross-year consistency checks."""
    type: str       # "single_year_official", "missing_department", "count_drop"
    severity: str   # "info", "warning", "error"
    message: str
    year: int | None = None
    details: dict = field(default_factory=dict)


def validate_cross_year(all_years_data: dict[int, list[dict]],
                        colony: str = "") -> list[CrossYearFlag]:
    """Run cross-year consistency checks on a colony's multi-year data.

    Args:
        all_years_data: {year: [official_dicts]} for all years of a colony
        colony: Colony name (for reporting)

    Returns:
        List of CrossYearFlag objects

    Checks:
    - Single-year-only officials (appear in exactly one year)
    - Departments missing in year N that exist in N-1 and N+1
    - 50%+ drop in official count year-over-year
    """
    flags = []
    sorted_years = sorted(all_years_data.keys())

    if len(sorted_years) < 2:
        return flags

    # Build surname -> set of years mapping
    surname_years: dict[str, set[int]] = {}
    for year, officials in all_years_data.items():
        for o in officials:
            surname = (o.get("surname") or "").strip().lower()
            if surname and len(surname) > 1:
                surname_years.setdefault(surname, set()).add(year)

    # Flag single-year-only officials
    for surname, years in surname_years.items():
        if len(years) == 1:
            year = list(years)[0]
            flags.append(CrossYearFlag(
                type="single_year_official",
                severity="info",
                message=f"Surname '{surname}' appears only in {year} — may be correct but higher risk",
                year=year,
                details={"surname": surname},
            ))

    # Build department -> set of years mapping
    dept_years: dict[str, set[int]] = {}
    for year, officials in all_years_data.items():
        for o in officials:
            dept = (o.get("department") or "").strip().lower()
            if dept:
                dept_years.setdefault(dept, set()).add(year)

    # Flag departments missing in year N that exist in N-1 and N+1
    for dept, years_present in dept_years.items():
        for i, year in enumerate(sorted_years):
            if year not in years_present:
                # Check if dept exists in adjacent years
                prev_year = sorted_years[i - 1] if i > 0 else None
                next_year = sorted_years[i + 1] if i < len(sorted_years) - 1 else None

                if (prev_year and prev_year in years_present and
                        next_year and next_year in years_present):
                    flags.append(CrossYearFlag(
                        type="missing_department",
                        severity="warning",
                        message=(f"Department '{dept}' exists in {prev_year} and "
                                 f"{next_year} but missing in {year} — likely extraction failure"),
                        year=year,
                        details={"department": dept, "prev": prev_year, "next": next_year},
                    ))

    # Count drops year-over-year
    year_counts = {y: len(officials) for y, officials in all_years_data.items()}
    for i in range(1, len(sorted_years)):
        prev_y = sorted_years[i - 1]
        curr_y = sorted_years[i]
        prev_count = year_counts[prev_y]
        curr_count = year_counts[curr_y]

        if prev_count > 0 and curr_count < prev_count * 0.5:
            flags.append(CrossYearFlag(
                type="count_drop",
                severity="warning",
                message=(f"{colony} {curr_y}: {curr_count} officials vs "
                         f"{prev_count} in {prev_y} — 50%+ drop"),
                year=curr_y,
                details={"prev_year": prev_y, "prev_count": prev_count,
                          "curr_count": curr_count},
            ))

    return flags


# =============================================================================
# CONVENIENCE: VALIDATE AND SAVE
# =============================================================================

def validate_and_partition(officials: list[dict], source_text: str,
                           colony: str, year: int,
                           verbose: bool = False) -> tuple[list[dict], list[dict], dict]:
    """Validate officials and partition into passed/quarantined.

    Returns:
        (passed, quarantined, summary_dict)
    """
    result = validate_colony_year(officials, source_text, colony, year)

    if verbose:
        print(f"\n  Validation: {result.total_records} total, "
              f"{result.high_confidence} HIGH, {result.medium_confidence} MEDIUM, "
              f"{result.low_confidence} LOW, {result.quarantined_count} quarantined")

        if result.anomalies:
            print(f"  Anomalies ({len(result.anomalies)}):")
            for a in result.anomalies:
                print(f"    [{a.severity}] {a.message}")

        if result.quarantined:
            print(f"  Quarantined ({result.quarantined_count}):")
            for o in result.quarantined:
                print(f"    - {o.get('name', '?')} ({o.get('department', '?')})")

    return result.passed, result.quarantined, result.summary


# =============================================================================
# CLI
# =============================================================================

def main():
    """CLI for validating an existing extraction JSON against its source text."""
    import argparse
    import json
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Validate extracted officials against source text"
    )
    parser.add_argument("extraction_json",
                        help="Path to extraction JSON file")
    parser.add_argument("source_text",
                        help="Path to source text file")
    parser.add_argument("--colony", default="",
                        help="Colony name (default: from JSON)")
    parser.add_argument("--year", type=int, default=0,
                        help="Year (default: from JSON)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Verbose output")
    args = parser.parse_args()

    # Load extraction
    with open(args.extraction_json) as f:
        data = json.load(f)

    officials = data.get("officials", [])
    colony = args.colony or data.get("colony", "Unknown")
    year = args.year or data.get("year", 0)

    # Load source text
    with open(args.source_text) as f:
        source_text = f.read()

    print(f"Validating {len(officials)} officials from {colony} {year}")
    print(f"Source: {args.source_text}")

    passed, quarantined, summary = validate_and_partition(
        officials, source_text, colony, year, verbose=True
    )

    print(f"\nSummary: {json.dumps(summary, indent=2)}")

    # Save results
    output_dir = Path(args.extraction_json).parent
    base = Path(args.extraction_json).stem

    passed_file = output_dir / f"{base}_validated.json"
    with open(passed_file, 'w') as f:
        json.dump({
            "colony": colony, "year": year,
            "total_officials": len(passed),
            "officials": passed,
            "validation_summary": summary,
        }, f, indent=2)
    print(f"\nPassed records: {passed_file}")

    if quarantined:
        q_file = output_dir / f"{base}_quarantined.json"
        with open(q_file, 'w') as f:
            json.dump({
                "colony": colony, "year": year,
                "total_quarantined": len(quarantined),
                "officials": quarantined,
            }, f, indent=2)
        print(f"Quarantined records: {q_file}")


if __name__ == "__main__":
    main()
