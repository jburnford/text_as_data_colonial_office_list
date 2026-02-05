"""
Colonial Office List Regex Extraction
=====================================

Production-quality regex-based extraction for Colonial Office List data.
Part of the extraction method comparison test.

Features:
- Section/department classification
- Multi-pattern extraction (simple, honors, multiple people, ditto)
- Salary parsing (ranges, allowances)
- Military rank detection
- Qualification parsing
- Location extraction from position titles

Usage:
    python extraction_regex.py test_data/sierra_leone_1896_test.txt

Output:
    test_data/regex_extraction_results.json
"""

import re
import json
import sys
from dataclasses import dataclass, field, asdict
from typing import Optional
from pathlib import Path


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class Official:
    """Extracted official record."""
    name: str
    canonical_name: str
    given_names: str
    surname: str
    position: str
    department: str
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    allowances: Optional[str] = None
    honors: list[str] = field(default_factory=list)
    qualifications: list[str] = field(default_factory=list)
    military_rank: Optional[str] = None
    location: Optional[str] = None
    extraction_notes: Optional[str] = None


# =============================================================================
# PATTERNS AND CONSTANTS
# =============================================================================

# Military ranks (appear before name)
MILITARY_RANKS = [
    r"Colonel", r"Lt\.-Col\.", r"Lieut\.-Col\.", r"Major-General",
    r"Lieut\.-General", r"Major", r"Captain", r"Capt\.", r"Brigadier-Gen\.",
    r"Surgeon-Major", r"Staff-Surgeon", r"Fleet-Surgeon"
]
MILITARY_RANK_PATTERN = re.compile(r'^(' + '|'.join(MILITARY_RANKS) + r')\s+', re.IGNORECASE)

# Honorific titles (appear before name)
HONORIFICS = [
    r"Sir", r"The Right Hon\.", r"The Hon\.", r"Right Rev\.", r"Rev\.",
    r"Ven\.", r"Dr\."
]
HONORIFIC_PATTERN = re.compile(r'^(' + '|'.join(HONORIFICS) + r')\s+', re.IGNORECASE)

# Honors (appear after name, uppercase abbreviations with periods)
HONORS = [
    "K.C.M.G.", "G.C.M.G.", "C.M.G.", "K.C.B.", "G.C.B.", "C.B.",
    "K.C.S.I.", "G.C.S.I.", "C.S.I.", "K.C.I.E.", "K.B.E.", "C.B.E.",
    "O.B.E.", "M.B.E.", "D.S.O.", "V.C.", "Kt.", "Knt."
]
HONOR_PATTERN = re.compile(r'\b(' + '|'.join([re.escape(h) for h in HONORS]) + r')')

# Qualifications (academic/professional, appear after name)
QUALIFICATIONS = [
    "M.D.", "M.B.", "B.A.", "M.A.", "B.Sc.", "M.Sc.", "LL.D.", "D.D.", "Ph.D.",
    "M.R.C.S.", "F.R.C.S.", "L.R.C.S.", "L.R.C.P.", "F.R.C.P.", "M.R.C.P.",
    "R.E.", "R.A.", "R.N.", "C.E.", "M.I.C.E.", "A.I.C.E.", "F.R.S.",
    "F.R.G.S.", "F.S.A.", "B.L."
]
QUAL_PATTERN = re.compile(r'\b(' + '|'.join([re.escape(q) for q in QUALIFICATIONS]) + r')')

# Salary patterns
SALARY_SIMPLE = re.compile(r'(\d+)l\.')  # 200l.
SALARY_RANGE = re.compile(r'(\d+)l\.\s+to\s+(\d+)l\.')  # 300l. to 400l.
SALARY_WITH_SHILLINGS = re.compile(r'(\d+)l\.\s+(\d+)s\.')  # 91l. 5s.

# Department headers - end with period, no salary, typically short
DEPT_HEADER_PATTERN = re.compile(r'^([A-Z][A-Za-z\s\-\']+(?:Department|Office|Establishment|Council)?)\.?\s*$')

# Ditto pattern
DITTO_PATTERN = re.compile(r'^(\d+(?:st|nd|rd|th)?\s+)?ditto', re.IGNORECASE)


# =============================================================================
# EXTRACTION FUNCTIONS
# =============================================================================

def detect_department(line: str) -> Optional[str]:
    """Detect if line is a department header."""
    line = line.strip()

    # Skip empty lines
    if not line:
        return None

    # Skip lines with salary indicators
    if 'l.' in line and re.search(r'\d+l\.', line):
        return None

    # Check common department patterns
    dept_keywords = [
        "Department", "Office", "Establishment", "Council",
        "Savings Bank", "Board of"
    ]

    # Line ends with period and contains department keyword
    if line.endswith('.') or any(kw in line for kw in dept_keywords):
        # Remove trailing period and check length
        clean = line.rstrip('.')
        if len(clean) < 60 and not re.search(r'\d+l\.', line):
            return clean

    # Specific known headers
    known_headers = [
        "Civil Establishment", "Colonial Secretary's Department",
        "Treasury Department", "Audit Department", "Medical Department",
        "Private Secretary", "Dispensers-", "Dispensers"
    ]
    for header in known_headers:
        if line.startswith(header):
            return header.rstrip('-')

    return None


def parse_salary(text: str) -> tuple[Optional[int], Optional[int], Optional[str]]:
    """
    Parse salary from text.
    Returns (min_salary, max_salary, allowances)
    """
    salary_min = None
    salary_max = None
    allowances = None

    # Extract salary range first
    range_match = SALARY_RANGE.search(text)
    if range_match:
        salary_min = int(range_match.group(1))
        salary_max = int(range_match.group(2))
        # Remove from text to find allowances
        text_remainder = text[range_match.end():]
    else:
        # Try simple salary
        simple_match = SALARY_SIMPLE.search(text)
        if simple_match:
            salary_min = int(simple_match.group(1))
            salary_max = salary_min
            text_remainder = text[simple_match.end():]
        else:
            text_remainder = text

    # Extract allowances (everything after salary with keywords)
    allowance_patterns = [
        r',?\s+and\s+([\w\s\.,]+(?:allowance|quarters|rent|personal)[\w\s\.,]*)',
        r',?\s+(travelling\s+allowance[\w\s\.,]*)',
        r',?\s+(quarters(?:\s+or\s+rent)?)',
        r',?\s+and\s+([\d]+l\.\s+\d*s?\.\s*\d*d?\.?\s*(?:allowance)?)',
    ]

    for pattern in allowance_patterns:
        allow_match = re.search(pattern, text_remainder, re.IGNORECASE)
        if allow_match:
            allowances = allow_match.group(1).strip().rstrip(',').rstrip('.')
            if allowances and not allowances.startswith('and '):
                break

    # Clean up allowances
    if allowances:
        allowances = re.sub(r'^and\s+', '', allowances)
        allowances = allowances.strip()

    return salary_min, salary_max, allowances if allowances else None


def extract_military_rank(text: str) -> tuple[Optional[str], str]:
    """Extract military rank from beginning of text. Returns (rank, remaining_text)."""
    match = MILITARY_RANK_PATTERN.match(text)
    if match:
        return match.group(1), text[match.end():].strip()
    return None, text


def extract_honorifics(text: str) -> tuple[list[str], str]:
    """Extract honorific titles from text. Returns (titles, remaining_text)."""
    titles = []
    remaining = text

    while True:
        match = HONORIFIC_PATTERN.match(remaining)
        if match:
            titles.append(match.group(1))
            remaining = remaining[match.end():].strip()
        else:
            break

    return titles, remaining


def extract_honors_and_quals(text: str) -> tuple[list[str], list[str], str]:
    """Extract honors and qualifications from text. Returns (honors, quals, clean_text)."""
    honors = HONOR_PATTERN.findall(text)
    quals = QUAL_PATTERN.findall(text)

    # Remove found items from text
    clean = text
    for h in honors:
        clean = clean.replace(h, '')
    for q in quals:
        clean = clean.replace(q, '')

    # Clean up extra commas and spaces
    clean = re.sub(r',\s*,', ',', clean)
    clean = re.sub(r'\s+', ' ', clean)
    clean = clean.strip().strip(',').strip()

    return honors, quals, clean


def parse_name(name_text: str) -> tuple[str, str, str, Optional[str], list[str], list[str]]:
    """
    Parse a name string into components.
    Returns (full_name, given_names, surname, military_rank, honors, qualifications)
    """
    original = name_text.strip()

    # Extract military rank
    military_rank, remaining = extract_military_rank(original)

    # Extract honorifics (we note them but don't use them for canonical name)
    honorifics, remaining = extract_honorifics(remaining)

    # Extract honors and qualifications
    honors, quals, remaining = extract_honors_and_quals(remaining)

    # Clean up the name
    name = remaining.strip().strip(',').strip()

    # Handle name abbreviations
    name = name.replace('Wm.', 'William')
    name = name.replace('Chas.', 'Charles')
    name = name.replace('Jas.', 'James')
    name = name.replace('Thos.', 'Thomas')
    name = name.replace('Geo.', 'George')
    name = name.replace('Robt.', 'Robert')
    name = name.replace('Jno.', 'John')

    # Parse into given names and surname
    # Assume last word is surname unless it looks like an initial
    parts = name.split()
    if len(parts) >= 2:
        # Check if last part is initial-like (e.g., "J." or single letter)
        if len(parts[-1]) <= 2 and parts[-1].endswith('.'):
            # Unusual - might be reversed, keep as-is
            surname = parts[-1].rstrip('.')
            given_names = ' '.join(parts[:-1])
        else:
            surname = parts[-1]
            given_names = ' '.join(parts[:-1])
    elif len(parts) == 1:
        surname = parts[0]
        given_names = ''
    else:
        surname = name
        given_names = ''

    # Canonical name: Surname, Given Names
    canonical = f"{surname}, {given_names}" if given_names else surname

    return name, given_names, surname, military_rank, honors, quals


def extract_location_from_position(position: str) -> tuple[str, Optional[str]]:
    """Extract location from position title if present."""
    # Pattern: position ending with location name
    location_pattern = re.compile(r'^(.+?),?\s+(at\s+)?(\w+(?:\s+\w+)?)$')

    # Known locations in Sierra Leone
    known_locations = [
        "Freetown", "Sherbro", "Sulymah", "Waterloo", "Hastings", "York",
        "Kent", "Regent", "Kissy", "Goderich", "Falaba", "Mongheri",
        "Kikoniak", "Isles de Los", "Manoh Salijah", "Lavanak", "Back Papelle",
        "Bassia", "Kembia", "Robat"
    ]

    for loc in known_locations:
        if position.endswith(loc) or f", {loc}" in position or f" at {loc}" in position:
            # Remove location from position
            clean_pos = position.replace(f", {loc}", "").replace(f" at {loc}", "").replace(loc, "").strip().rstrip(',')
            return clean_pos, loc

    return position, None


def parse_entry_line(line: str, current_dept: str, previous_position: Optional[str]) -> list[Official]:
    """
    Parse a single entry line into Official records.
    Handles multiple people on one line, ditto references, etc.
    """
    officials = []
    line = line.strip()

    if not line:
        return officials

    # Skip department headers and non-data lines
    if detect_department(line):
        return officials

    # Check for ditto - expand to previous position type
    if DITTO_PATTERN.match(line):
        # Extract the ordinal if present (e.g., "2nd ditto")
        ditto_match = DITTO_PATTERN.match(line)
        prefix = ditto_match.group(1) or ""
        line = line[ditto_match.end():].strip().lstrip(',').strip()

        # Reconstruct with previous position
        if previous_position:
            # For numbered positions like "2nd Clerk"
            if prefix:
                line = f"{prefix.strip()} {previous_position.split()[0] if previous_position else 'Clerk'}, {line}"
            else:
                line = f"{previous_position}, {line}"

    # Check if no salary - might be incomplete entry
    if not re.search(r'\d+l\.', line):
        return officials

    # Handle multiple people on one line (semicolon-separated)
    if ';' in line and line.count(';') >= 1:
        # Split by semicolon for multiple entries
        entries = line.split(';')

        # First entry has the position
        first_entry = entries[0].strip()

        # Find position (text before first name-like pattern)
        pos_match = re.match(r'^([A-Za-z\s\-,]+?),\s+(?=[A-Z])', first_entry)
        if pos_match:
            base_position = pos_match.group(1).strip().rstrip(',')
            # Process first entry
            remainder = first_entry[pos_match.end()-1:].strip()
            officials.extend(parse_single_entry(remainder, base_position, current_dept))

            # Process subsequent entries (position implied)
            for entry in entries[1:]:
                entry = entry.strip()
                if entry:
                    officials.extend(parse_single_entry(entry, base_position, current_dept))
        else:
            # Fallback - treat as single entry
            officials.extend(parse_single_entry(first_entry, "", current_dept))
    else:
        # Single entry line
        officials.extend(parse_single_entry(line, "", current_dept))

    return officials


def parse_single_entry(text: str, known_position: str, current_dept: str) -> list[Official]:
    """Parse a single person entry."""
    officials = []
    text = text.strip()

    if not text:
        return officials

    # Parse salary first (anchor point)
    salary_min, salary_max, allowances = parse_salary(text)

    if salary_min is None:
        # No salary found - might be incomplete
        return officials

    # Find everything before salary
    salary_match = SALARY_RANGE.search(text) or SALARY_SIMPLE.search(text)
    if salary_match:
        before_salary = text[:salary_match.start()].strip().rstrip(',')
    else:
        before_salary = text

    # Split into position and name
    if known_position:
        position = known_position
        name_part = before_salary
    else:
        # Try to find position/name boundary
        # Position comes first, then name (usually marked by initials or known pattern)
        parts = before_salary.split(',')

        if len(parts) >= 2:
            # Heuristics:
            # - Position words are typically lowercase or title case common words
            # - Names have initials (X.) or are proper names
            position_parts = []
            name_parts = []
            found_name = False

            for i, part in enumerate(parts):
                part = part.strip()
                if not part:
                    continue

                # Check if this looks like a name (has initials, military rank, or is capitalized single word)
                has_initial = bool(re.search(r'\b[A-Z]\.\s*[A-Z]', part))
                has_rank = bool(MILITARY_RANK_PATTERN.match(part))
                is_name_like = has_initial or has_rank

                # Check for honorifics
                has_honorific = bool(HONORIFIC_PATTERN.match(part))

                if not found_name and (is_name_like or has_honorific):
                    found_name = True

                if found_name:
                    name_parts.append(part)
                else:
                    position_parts.append(part)

            position = ', '.join(position_parts) if position_parts else ""
            name_part = ', '.join(name_parts) if name_parts else before_salary
        else:
            position = ""
            name_part = before_salary

    # Parse the name
    if name_part:
        name, given_names, surname, military_rank, honors, quals = parse_name(name_part)

        # Extract location from position if present
        clean_position, location = extract_location_from_position(position)

        # Build canonical name
        canonical_name = f"{surname}, {given_names}" if given_names else surname

        official = Official(
            name=name,
            canonical_name=canonical_name,
            given_names=given_names,
            surname=surname,
            position=clean_position,
            department=current_dept,
            salary_min=salary_min,
            salary_max=salary_max,
            allowances=allowances,
            honors=honors,
            qualifications=quals,
            military_rank=military_rank,
            location=location
        )
        officials.append(official)

    return officials


def extract_from_text(text: str) -> list[Official]:
    """Main extraction function."""
    officials = []
    current_dept = "Unknown"
    previous_position = None

    lines = text.split('\n')

    for line in lines:
        line = line.strip()

        # Check for department header
        dept = detect_department(line)
        if dept:
            current_dept = dept
            continue

        # Skip empty lines and comments
        if not line or line.startswith('#'):
            continue

        # Parse entry
        new_officials = parse_entry_line(line, current_dept, previous_position)

        # Update previous position for ditto tracking
        if new_officials:
            previous_position = new_officials[0].position
            officials.extend(new_officials)

    return officials


# =============================================================================
# EVALUATION FUNCTIONS
# =============================================================================

def load_gold_standard(filepath: str) -> list[dict]:
    """Load gold standard annotations."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data['officials']


def compare_name(extracted: str, gold: str) -> bool:
    """Compare names with fuzzy matching."""
    # Normalize
    e = extracted.lower().replace(',', '').replace('.', '').strip()
    g = gold.lower().replace(',', '').replace('.', '').strip()

    # Exact match
    if e == g:
        return True

    # Check if all parts present
    e_parts = set(e.split())
    g_parts = set(g.split())

    # If most parts match, consider it a match
    if len(e_parts & g_parts) >= min(len(e_parts), len(g_parts)) * 0.7:
        return True

    return False


def evaluate_extraction(extracted: list[Official], gold: list[dict]) -> dict:
    """Evaluate extraction against gold standard."""
    results = {
        'total_gold': len(gold),
        'total_extracted': len(extracted),
        'matched': 0,
        'precision': 0.0,
        'recall': 0.0,
        'field_accuracy': {
            'name': {'correct': 0, 'total': 0},
            'position': {'correct': 0, 'total': 0},
            'salary_min': {'correct': 0, 'total': 0},
            'salary_max': {'correct': 0, 'total': 0},
            'honors': {'correct': 0, 'total': 0},
            'qualifications': {'correct': 0, 'total': 0},
            'location': {'correct': 0, 'total': 0},
        },
        'matches': [],
        'missed': [],
        'extra': []
    }

    # Try to match each gold standard entry
    used_extracted = set()

    for g in gold:
        best_match = None
        best_score = 0

        for i, e in enumerate(extracted):
            if i in used_extracted:
                continue

            # Score based on name match
            if compare_name(e.canonical_name, g.get('canonical_name', g['name'])):
                score = 1.0
                if best_score < score:
                    best_score = score
                    best_match = i

        if best_match is not None:
            used_extracted.add(best_match)
            results['matched'] += 1
            e = extracted[best_match]

            # Field accuracy
            results['field_accuracy']['name']['total'] += 1
            if compare_name(e.canonical_name, g.get('canonical_name', g['name'])):
                results['field_accuracy']['name']['correct'] += 1

            results['field_accuracy']['position']['total'] += 1
            if e.position and g.get('position') and e.position.lower() in g['position'].lower():
                results['field_accuracy']['position']['correct'] += 1

            results['field_accuracy']['salary_min']['total'] += 1
            if e.salary_min == g.get('salary_min'):
                results['field_accuracy']['salary_min']['correct'] += 1

            results['field_accuracy']['salary_max']['total'] += 1
            if e.salary_max == g.get('salary_max'):
                results['field_accuracy']['salary_max']['correct'] += 1

            if g.get('honors'):
                results['field_accuracy']['honors']['total'] += 1
                if set(e.honors) == set(g['honors']):
                    results['field_accuracy']['honors']['correct'] += 1

            if g.get('qualifications'):
                results['field_accuracy']['qualifications']['total'] += 1
                if set(e.qualifications) == set(g['qualifications']):
                    results['field_accuracy']['qualifications']['correct'] += 1

            if g.get('location'):
                results['field_accuracy']['location']['total'] += 1
                if e.location and e.location.lower() == g['location'].lower():
                    results['field_accuracy']['location']['correct'] += 1

            results['matches'].append({
                'gold': g['name'],
                'extracted': e.name,
                'position_match': e.position == g.get('position', ''),
                'salary_match': e.salary_min == g.get('salary_min')
            })
        else:
            results['missed'].append(g['name'])

    # Track extra extractions
    for i, e in enumerate(extracted):
        if i not in used_extracted:
            results['extra'].append(e.name)

    # Calculate metrics
    if results['total_extracted'] > 0:
        results['precision'] = results['matched'] / results['total_extracted']
    if results['total_gold'] > 0:
        results['recall'] = results['matched'] / results['total_gold']

    # Calculate field accuracy percentages
    for field, counts in results['field_accuracy'].items():
        if counts['total'] > 0:
            counts['accuracy'] = counts['correct'] / counts['total']
        else:
            counts['accuracy'] = None

    return results


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Main entry point."""
    # Default paths
    input_file = Path(__file__).parent / "test_data" / "sierra_leone_1896_test.txt"
    gold_file = Path(__file__).parent / "test_data" / "gold_standard.json"
    output_file = Path(__file__).parent / "test_data" / "regex_extraction_results.json"

    # Override with command line args
    if len(sys.argv) > 1:
        input_file = Path(sys.argv[1])

    print("=" * 60)
    print("COLONIAL OFFICE LIST - REGEX EXTRACTION")
    print("=" * 60)

    # Read input
    print(f"\nReading: {input_file}")
    with open(input_file, 'r') as f:
        text = f.read()

    # Extract
    print("Extracting officials...")
    officials = extract_from_text(text)
    print(f"Extracted {len(officials)} officials")

    # Show sample
    print("\nSample extractions:")
    for o in officials[:5]:
        print(f"  {o.position}: {o.name}")
        print(f"    Salary: {o.salary_min}-{o.salary_max}l., Dept: {o.department}")
        if o.honors:
            print(f"    Honors: {', '.join(o.honors)}")
        if o.qualifications:
            print(f"    Qualifications: {', '.join(o.qualifications)}")

    # Evaluate against gold standard if available
    if gold_file.exists():
        print(f"\nEvaluating against: {gold_file}")
        gold = load_gold_standard(gold_file)
        results = evaluate_extraction(officials, gold)

        print(f"\n--- EVALUATION RESULTS ---")
        print(f"Gold standard: {results['total_gold']} officials")
        print(f"Extracted: {results['total_extracted']} officials")
        print(f"Matched: {results['matched']}")
        print(f"Precision: {results['precision']:.2%}")
        print(f"Recall: {results['recall']:.2%}")

        print(f"\nField Accuracy:")
        for field, counts in results['field_accuracy'].items():
            if counts['accuracy'] is not None:
                print(f"  {field}: {counts['accuracy']:.2%} ({counts['correct']}/{counts['total']})")

        if results['missed']:
            print(f"\nMissed ({len(results['missed'])}):")
            for name in results['missed'][:10]:
                print(f"  - {name}")

        if results['extra']:
            print(f"\nExtra extractions ({len(results['extra'])}):")
            for name in results['extra'][:10]:
                print(f"  - {name}")
    else:
        results = None

    # Save results
    output = {
        'metadata': {
            'source': str(input_file),
            'method': 'regex',
            'total_extracted': len(officials)
        },
        'officials': [asdict(o) for o in officials],
        'evaluation': results
    }

    print(f"\nSaving results to: {output_file}")
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print("\nDone!")
    return officials, results


if __name__ == "__main__":
    main()
