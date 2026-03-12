"""
Scan completed source files for unrecognized department headers.
Identifies files that need re-extraction after chunking pattern updates.

Usage:
    python rerun_colonies.py --scan                                        # report affected files
    python rerun_colonies.py --evict                                       # evict all affected files
    python rerun_colonies.py --evict --keys "Canada_1896,Cape of Good Hope_1896"  # specific files only
"""

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
STATE_FILE = SCRIPT_DIR / "generated" / "corpus_state.json"

# ---------------------------------------------------------------------------
# OLD patterns (before dominion fix) — used to count what the chunker USED to match
# ---------------------------------------------------------------------------
OLD_DEPT_HEADER_NAMES = [
    r'Civil Establishment',
    r'Colonial Secretary.s (?:Department|Office)',
    r'Treasury Department',
    r'Audit (?:Department|Office)',
    r'Medical (?:Department|Establishment)',
    r'Police (?:Department|Establishment)',
    r'Public Works Department',
    r'Education(?:al)? (?:Department|Establishment)',
    r'Judicial (?:Department|Establishment)',
    r'Customs Department',
    r'Post Office(?: Department)?',
    r'Survey(?:or.s)? Department',
    r'Forest Department',
    r'Harbour Department',
    r'Printing (?:Office|Department|Branch)',
    r'Prisons? Department',
    r'Railway Department',
    r'Sanitary Department',
    r'Gaol (?:Department|Establishment)',
    r'Legal Departments?',
    r'Ecclesiastical (?:Department|Establishment)',
    r'Board of Education',
    r'Secretariat and Treasury',
    r'Aborigines Branch',
    r'Harbour Master and Boat Establishment',
    r'Police and Gaols',
    r'Rural Districts',
    r'British Sherbro',
    r'Isles de Los',
    r'Department for Native Affairs',
    r'Port and Marine Department',
    r'Colonial Steamer',
    r'Savings Bank',
    r'Registrar of Births.+',
    r'Governor.s Office',
    r'Provincial Administration',
    r'Civil Police',
    r'Agricultural (?:Development )?Branch',
    r'Preventive Service',
    r'Sierra Leone Battalion.+',
    r'GOVERNOR AND PERSONAL STAFF',
    r'ADMINISTRATION',
    r'ACCOUNTANT.GENERAL',
    r'AGRICULTURAL',
    r'COMMERCE AND INDUSTRY',
    r'INCOME TAX',
    r'LABOUR',
    r'LEGAL',
    r'GEOLOGICAL',
    r'BROADCASTING',
    r'CIVIL AVIATION',
    r'CO.OPERATIVE',
    r'CUSTOMS',
    r'EDUCATION',
    r'FORESTRY',
    r'MEDICAL',
    r'METEOROLOGICAL',
    r'MINES',
    r'POLICE',
    r'PORT',
    r'POSTAL',
    r'PRINTING',
    r'PRISONS',
    r'PUBLIC RELATIONS',
    r'PUBLIC WORKS',
    r'RAILWAY',
    r'SURVEYS? AND LANDS',
    r'VETERINARY',
    r'PUBLIC SERVICE COMMISSION',
    r'Forestry Department',
    r'Veterinary Department',
    r'Immigration (?:Department|Office)',
    r'Land(?:s)? (?:Department|Office)',
    r'Supreme Court',
    r'Fire Brigade',
    r'Water Works',
    r'District Commissioners?',
    r'Native Affairs? Department',
    r'Transport Department',
    r'Marine Department',
    r'Lands and Mines Department',
    r'Inspector.General.s (?:Department|Office)',
    r'Registrar.General.s (?:Department|Office)',
    r'Crown Agents?',
    r'Militia',
    r'Botanical (?:Department|Gardens?)',
    r'Government Analyst',
    r'Government Printer',
    r'Constabulary',
    r'Frontier (?:Force|Police)',
    r'[A-Z][A-Za-z\s\-\']+(?:Department|Office|Establishment|Board|Court|Brigade|Commission|Service|Branch|Administration)',
]

OLD_HEADERS_RE = re.compile(
    r'^(?:' + '|'.join(OLD_DEPT_HEADER_NAMES) + r')[\s.]*$',
    re.MULTILINE | re.IGNORECASE
)

# ---------------------------------------------------------------------------
# NEW patterns — import from the updated module
# ---------------------------------------------------------------------------
from extraction_ollama import DEPT_HEADERS as NEW_HEADERS_RE


def _strip_markdown(text: str) -> str:
    """Remove markdown formatting (headers, bold) from a line."""
    text = re.sub(r'^#{1,6}\s+', '', text)
    text = text.replace('**', '').replace('__', '')
    return text.strip()


def count_header_matches(text: str, pattern: re.Pattern) -> tuple[int, list[str]]:
    """Count how many lines in text match a header pattern.

    Returns (count, list_of_matched_lines).
    """
    matched = []
    for line in text.split('\n'):
        clean = _strip_markdown(line).rstrip('.')
        if (clean and
            not re.search(r'\d+l\.|£\d', line) and
            not re.search(r'—.*[,.]', line) and
            len(clean) < 80 and
            pattern.match(clean + '.')):
            matched.append(clean)
    return len(matched), matched


def scan_affected(state: dict, threshold: int = 2) -> list[dict]:
    """Scan completed entries and find files where new patterns match more headers.

    Args:
        state: The corpus state dict.
        threshold: Minimum difference in header count to flag a file.

    Returns:
        List of dicts with key, colony, year, old_count, new_count, new_headers.
    """
    affected = []
    completed = state.get('completed', {})

    for key, entry in sorted(completed.items()):
        source_file = entry.get('source_file', '')
        if not source_file or not Path(source_file).exists():
            continue

        text = Path(source_file).read_text(errors='replace')
        old_count, old_matches = count_header_matches(text, OLD_HEADERS_RE)
        new_count, new_matches = count_header_matches(text, NEW_HEADERS_RE)

        diff = new_count - old_count
        if diff > threshold:
            # Find the newly-matched headers
            new_only = [h for h in new_matches if h not in old_matches]
            affected.append({
                'key': key,
                'colony': entry.get('colony', ''),
                'year': entry.get('year', ''),
                'source_file': source_file,
                'old_headers': old_count,
                'new_headers': new_count,
                'diff': diff,
                'total_officials': entry.get('total_officials', 0),
                'new_header_names': new_only[:20],  # cap display
            })

    return affected


def evict_keys(state: dict, keys: list[str]) -> int:
    """Remove entries from state['completed'], returning count evicted."""
    evicted = 0
    for key in keys:
        if key in state.get('completed', {}):
            del state['completed'][key]
            evicted += 1
        else:
            print(f"  WARNING: '{key}' not found in completed entries")
    return evicted


def main():
    parser = argparse.ArgumentParser(
        description='Scan/evict colony files needing re-extraction after chunking pattern updates')
    parser.add_argument('--scan', action='store_true',
                        help='Scan completed files and report which need re-extraction')
    parser.add_argument('--evict', action='store_true',
                        help='Evict affected files from corpus_state.json')
    parser.add_argument('--keys', type=str, default=None,
                        help='Comma-separated list of specific keys to evict (e.g. "Canada_1896,Cape of Good Hope_1896")')
    parser.add_argument('--threshold', type=int, default=2,
                        help='Minimum new-header difference to flag a file (default: 2)')
    args = parser.parse_args()

    if not args.scan and not args.evict:
        parser.print_help()
        sys.exit(1)

    if not STATE_FILE.exists():
        print(f"ERROR: State file not found: {STATE_FILE}")
        sys.exit(1)

    state = json.loads(STATE_FILE.read_text())
    print(f"Loaded state: {len(state.get('completed', {}))} completed entries")

    # Scan
    affected = scan_affected(state, threshold=args.threshold)

    if args.scan or (args.evict and not args.keys):
        print(f"\n{'='*80}")
        print(f"Files with >{args.threshold} newly-recognized headers: {len(affected)}")
        print(f"{'='*80}\n")

        for entry in sorted(affected, key=lambda x: -x['diff']):
            print(f"  {entry['key']} (+{entry['diff']} headers, "
                  f"{entry['old_headers']} old -> {entry['new_headers']} new, "
                  f"{entry['total_officials']} officials extracted)")
            for h in entry['new_header_names'][:10]:
                print(f"    NEW: {h}")
            print()

        if not affected:
            print("  No files need re-extraction.")

    if args.evict:
        if args.keys:
            keys_to_evict = [k.strip() for k in args.keys.split(',')]
        else:
            keys_to_evict = [e['key'] for e in affected]

        if not keys_to_evict:
            print("\nNo files to evict.")
            return

        print(f"\nEvicting {len(keys_to_evict)} entries from completed state...")
        evicted = evict_keys(state, keys_to_evict)

        # Save updated state
        state['last_updated'] = __import__('datetime').datetime.now().isoformat()
        STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))
        print(f"Evicted {evicted} entries. State saved to {STATE_FILE}")
        print(f"Remaining completed: {len(state.get('completed', {}))}")


if __name__ == '__main__':
    main()
