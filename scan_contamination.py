"""
Cross-Colony Contamination Scanner
====================================

Scans source text files for content that belongs to a different colony.
Detects cases where the PDF-to-text parser merged multiple colonies into
one file (e.g., Fiji 1896 containing Ceylon + Cape of Good Hope content).

Usage:
    python scan_contamination.py                    # scan all source files
    python scan_contamination.py --year 1896        # scan one year
    python scan_contamination.py --completed-only   # only scan files we've extracted
    python scan_contamination.py --verbose          # show matched lines

Output:
    Reports files with suspected cross-colony contamination, including
    which foreign colonies were detected and at which line numbers.
    Results saved to generated/contamination_report.json for tracking.
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from scaffold_neo4j import scan_corpus, normalize_colony_name

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "generated"
STATE_FILE = OUTPUT_DIR / "corpus_state.json"
REPORT_FILE = OUTPUT_DIR / "contamination_report.json"

# ---------------------------------------------------------------------------
# Colony name patterns for detection
# ---------------------------------------------------------------------------

# Canonical colony names that could appear as section headers in source files.
# These are checked against lines in files that DON'T belong to that colony.
COLONY_HEADERS = [
    "Antigua", "Bahamas", "Barbados", "Basutoland", "Bermuda",
    "British Bechuanaland", "British Central Africa",
    "British East Africa", "British Guiana", "British Honduras",
    "British New Guinea", "Cape of Good Hope", "Ceylon", "Cyprus",
    "Dominica", "Dominion of Canada", "Falkland Islands", "Fiji",
    "Gambia", "Gibraltar", "Gold Coast", "Grenada",
    "Heligoland", "Hong Kong", "Jamaica", "Labuan", "Lagos",
    "Leeward Islands", "Malta", "Mauritius", "Montserrat",
    "Natal", "New South Wales", "New Zealand", "Newfoundland",
    "Niger Coast Protectorate", "Queensland",
    "St Helena", "St Lucia", "St Vincent",
    "Seychelles", "Sierra Leone", "South Australia",
    "Straits Settlements", "Tasmania", "Tobago",
    "Trinidad", "Turks and Caicos Islands",
    "Victoria", "Western Australia", "Zanzibar",
]

# Build regex: match colony name as a standalone header line (possibly with
# markdown, caps, trailing punctuation). Must be close to a full-line match
# to avoid false positives like "Victoria Cross" or "Malta fever".
def _build_header_re(name: str) -> re.Pattern:
    """Build a regex that matches a colony name as a section header."""
    escaped = re.escape(name)
    # Allow markdown prefixes (###), bold (**), caps, trailing period/colon
    return re.compile(
        r'^\s*(?:#{1,6}\s+)?(?:\*\*)?'
        + escaped +
        r'(?:\*\*)?[\s.:]*$',
        re.IGNORECASE
    )

HEADER_PATTERNS = {name: _build_header_re(name) for name in COLONY_HEADERS}

# Additional content signatures: unique phrases that strongly indicate a
# specific colony's preamble/descriptive text was pasted in.
CONTENT_SIGNATURES = {
    "Ceylon": [
        re.compile(r'Ceylon\s+Savings\s+Bank', re.IGNORECASE),
        re.compile(r'Ceylon\s+Medical\s+College', re.IGNORECASE),
        re.compile(r'Ceylon\s+rupee\s+currency', re.IGNORECASE),
        re.compile(r'Colombo', re.IGNORECASE),
        re.compile(r'Kandyan\s+King', re.IGNORECASE),
    ],
    "Cape of Good Hope": [
        re.compile(r'Cape\s+Mounted\s+Riflemen', re.IGNORECASE),
        re.compile(r'Cape\s+of\s+Good\s+Hope\s+Station', re.IGNORECASE),
        re.compile(r'Griqualand', re.IGNORECASE),
    ],
    "Mauritius": [
        re.compile(r'Mauritius\s+rupee', re.IGNORECASE),
        re.compile(r'Port\s+Louis', re.IGNORECASE),
    ],
    "Jamaica": [
        re.compile(r'Kingston,?\s+Jamaica', re.IGNORECASE),
    ],
    "Malta": [
        re.compile(r'Valletta', re.IGNORECASE),
    ],
    "Hong Kong": [
        re.compile(r'Hong\s+Kong\s+dollar', re.IGNORECASE),
    ],
}

# Colonies that commonly appear as sub-sections within other files
# (e.g., "Victoria" in Leeward Islands refers to Victoria Barracks, not the colony)
# We handle these by requiring additional evidence beyond a header match.
AMBIGUOUS_NAMES = {"Victoria", "Dominica", "Grenada", "Montserrat", "Tobago",
                   "Antigua", "Bermuda", "Gibraltar", "Malta", "Labuan",
                   "Fiji", "Tasmania", "Queensland"}

# ---------------------------------------------------------------------------
# Legitimate sub-territory references (false positive suppression)
# ---------------------------------------------------------------------------
# Maps parent colonies to sub-territories whose mentions are expected and
# should NOT be flagged as contamination.
LEGITIMATE_SUB_TERRITORIES = {
    # Federation / multi-territory colonies
    'Leeward Islands': {'Antigua', 'Dominica', 'Montserrat', 'St Kitts', 'Nevis', 'Virgin Islands'},
    'Windward Islands': {'Grenada', 'St Lucia', 'St Vincent', 'Tobago', 'Barbados'},
    'Trinidad and Tobago': {'Trinidad', 'Tobago'},
    'Trinidad': {'Tobago', 'Turks and Caicos Islands'},
    'Tobago': {'Trinidad'},

    # Dominions with provinces/states
    'Dominion of Canada': {'Nova Scotia', 'New Brunswick', 'Manitoba', 'British Columbia',
                           'Prince Edward Island', 'Saskatchewan', 'Alberta', 'Ontario', 'Quebec'},
    'Canada': {'Nova Scotia', 'New Brunswick', 'Manitoba', 'British Columbia',
               'Prince Edward Island', 'Saskatchewan', 'Alberta', 'Ontario', 'Quebec'},
    'Australia': {'New South Wales', 'Victoria', 'Queensland', 'South Australia',
                  'Tasmania', 'Western Australia'},
    'Commonwealth of Australia': {'New South Wales', 'Victoria', 'Queensland',
                                  'South Australia', 'Tasmania', 'Western Australia'},
    'New Zealand': {'Fiji'},

    # Dependencies
    'Mauritius': {'Seychelles'},

    # South Africa (pre/post union)
    'Cape of Good Hope': {'Basutoland', 'British Bechuanaland', 'Griqualand West'},
    'South Africa': {'Cape of Good Hope', 'Natal', 'Basutoland', 'British Bechuanaland',
                     'Transvaal', 'Orange River Colony'},
    'Griqualand West': {'Cape of Good Hope'},

    # High Commission Territories
    'High Commission Territories': {'Basutoland', 'British Bechuanaland', 'Swaziland'},

    # West Indies Federation
    'West Indies Federation': {'Barbados', 'Jamaica', 'Trinidad', 'Tobago',
                                'Turks and Caicos Islands', 'Antigua', 'Dominica',
                                'Montserrat', 'St Kitts', 'Grenada', 'St Lucia', 'St Vincent'},
    'West Indies': {'Barbados', 'Jamaica', 'Trinidad', 'Tobago', 'Turks and Caicos Islands'},

    # Straits Settlements
    'Straits Settlements': {'Labuan'},

    # East Africa
    'British East Africa': {'Zanzibar'},
    'British East Africa and Zanzibar': {'Zanzibar', 'British East Africa'},
}


def scan_file(filepath: Path, expected_colony: str, verbose: bool = False) -> dict | None:
    """Scan a single source file for cross-colony contamination.

    Returns a dict with contamination details, or None if clean.
    """
    text = filepath.read_text(errors='replace')
    lines = text.split('\n')
    total_lines = len(lines)

    # Normalize expected colony for comparison
    expected_lower = expected_colony.lower().strip()
    # Also build set of acceptable colony references (the file's own colony
    # plus common sub-references like province names within that colony)
    acceptable = {expected_lower}
    # "Dominion of Canada" files can reference provinces
    if 'canada' in expected_lower:
        acceptable.update(['dominion of canada', 'canada'])
    if 'cape' in expected_lower:
        acceptable.add('cape of good hope')

    foreign_hits = {}  # {colony_name: [(line_num, line_text), ...]}

    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            continue

        # Check colony header patterns
        for colony_name, pattern in HEADER_PATTERNS.items():
            if colony_name.lower() in acceptable:
                continue
            if pattern.match(stripped):
                # For ambiguous names, require the match to be in ALL CAPS
                # or have markdown header prefix to reduce false positives
                if colony_name in AMBIGUOUS_NAMES:
                    clean = re.sub(r'^#{1,6}\s+', '', stripped).strip('*. ')
                    if not (clean == clean.upper() and len(clean) > 3):
                        continue
                    # Additional check: ambiguous names must appear as
                    # standalone headers (not part of a longer phrase)
                    if len(clean.split()) > len(colony_name.split()) + 1:
                        continue

                if colony_name not in foreign_hits:
                    foreign_hits[colony_name] = []
                foreign_hits[colony_name].append((line_num, stripped[:120]))

        # Check content signatures
        for colony_name, signatures in CONTENT_SIGNATURES.items():
            if colony_name.lower() in acceptable:
                continue
            for sig in signatures:
                if sig.search(stripped):
                    if colony_name not in foreign_hits:
                        foreign_hits[colony_name] = []
                    foreign_hits[colony_name].append((line_num, f'[SIG] {stripped[:100]}'))
                    break  # one signature match per line is enough

    if not foreign_hits:
        return None

    # Filter out legitimate sub-territory references
    legit_subs = LEGITIMATE_SUB_TERRITORIES.get(expected_colony, set())
    if legit_subs:
        foreign_hits = {
            colony: hits for colony, hits in foreign_hits.items()
            if colony not in legit_subs
        }
    if not foreign_hits:
        return None

    # Score severity: header matches count more than content signatures
    severity_score = 0
    for colony, hits in foreign_hits.items():
        header_hits = [h for h in hits if not h[1].startswith('[SIG]')]
        sig_hits = [h for h in hits if h[1].startswith('[SIG]')]
        # A colony header match is strong evidence
        severity_score += len(header_hits) * 10
        # Content signatures are weaker
        severity_score += len(sig_hits) * 2

    # Estimate contaminated line range
    all_hit_lines = []
    for hits in foreign_hits.values():
        all_hit_lines.extend(h[0] for h in hits)
    if all_hit_lines:
        contam_start = min(all_hit_lines)
        contam_end = max(all_hit_lines)
        contam_pct = (contam_end - contam_start + 1) / total_lines * 100
    else:
        contam_start = contam_end = 0
        contam_pct = 0

    result = {
        'file': str(filepath),
        'expected_colony': expected_colony,
        'total_lines': total_lines,
        'foreign_colonies': {},
        'severity_score': severity_score,
        'contaminated_range': f'L{contam_start}-L{contam_end}',
        'contaminated_pct': round(contam_pct, 1),
    }

    for colony, hits in foreign_hits.items():
        result['foreign_colonies'][colony] = {
            'hit_count': len(hits),
            'lines': [(ln, txt) for ln, txt in hits[:10]],  # cap for report size
        }

    return result


def main():
    parser = argparse.ArgumentParser(description='Scan source files for cross-colony contamination')
    parser.add_argument('--year', type=int, help='Scan only this year')
    parser.add_argument('--completed-only', action='store_true',
                        help='Only scan files that have been extracted')
    parser.add_argument('--verbose', action='store_true',
                        help='Show matched lines in output')
    parser.add_argument('--min-severity', type=int, default=5,
                        help='Minimum severity score to report (default: 5)')
    args = parser.parse_args()

    # Scan corpus structure
    corpus = scan_corpus(SCRIPT_DIR)

    # Optionally filter to completed files only
    completed_files = set()
    if args.completed_only and STATE_FILE.exists():
        state = json.loads(STATE_FILE.read_text())
        for entry in state.get('completed', {}).values():
            sf = entry.get('source_file', '')
            if sf:
                completed_files.add(sf)

    contaminated = []
    total_scanned = 0

    years = [args.year] if args.year else sorted(corpus.keys())
    for year in years:
        if year not in corpus:
            continue
        year_dir = SCRIPT_DIR / f"{year}_manual_parsed"
        for filename, stem, canonical in corpus[year]:
            filepath = year_dir / filename
            if not filepath.exists():
                continue
            if args.completed_only and str(filepath) not in completed_files:
                continue

            total_scanned += 1
            result = scan_file(filepath, canonical, verbose=args.verbose)
            if result and result['severity_score'] >= args.min_severity:
                result['key'] = f'{canonical}_{year}'
                result['year'] = year
                contaminated.append(result)

    # Sort by severity
    contaminated.sort(key=lambda x: -x['severity_score'])

    # Print report
    print(f"Scanned {total_scanned} files across {len(years)} years")
    print(f"Found {len(contaminated)} contaminated files (severity >= {args.min_severity})")
    print(f"{'='*80}\n")

    for entry in contaminated:
        foreign = ', '.join(
            f"{c} ({d['hit_count']} hits)"
            for c, d in entry['foreign_colonies'].items()
        )
        print(f"  {entry['key']} (severity {entry['severity_score']})")
        print(f"    File: {entry['file']}")
        print(f"    Foreign content: {foreign}")
        print(f"    Contaminated range: {entry['contaminated_range']} "
              f"(~{entry['contaminated_pct']}% of {entry['total_lines']} lines)")

        if args.verbose:
            for colony, data in entry['foreign_colonies'].items():
                print(f"    --- {colony} ---")
                for ln, txt in data['lines']:
                    print(f"      L{ln}: {txt}")
        print()

    # Save report
    REPORT_FILE.parent.mkdir(exist_ok=True)
    report = {
        'scan_date': __import__('datetime').datetime.now().isoformat(),
        'total_scanned': total_scanned,
        'contaminated_count': len(contaminated),
        'files': contaminated,
    }
    REPORT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"Report saved to {REPORT_FILE}")


if __name__ == '__main__':
    main()
