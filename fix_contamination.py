"""
Fix Contaminated Source Files — Two-Tier Approach
===================================================

Tier 1 (Truncation): For files where foreign content is APPENDED after the
colony's own content. Find the first foreign colony header and cut there.

Tier 2 (Raw OCR Re-extraction): For files where foreign content starts very
early (<10%) and is interleaved. Re-extract from raw OCR source.

Usage:
    python fix_contamination.py --scan                        # report: which files, which tier
    python fix_contamination.py --all --dry-run                # preview all changes
    python fix_contamination.py --year 1896                    # fix all for 1896
    python fix_contamination.py --year 1896 --colony Fiji      # fix just Fiji 1896
    python fix_contamination.py --all                          # fix everything
    python fix_contamination.py --tier1-only --all             # only truncation fixes
    python fix_contamination.py --tier2-only --all             # only raw OCR fixes
    python fix_contamination.py --evict                        # evict fixed files from corpus state

Requires:
    - generated/contamination_report.json (from scan_contamination.py)
    - Raw OCR files at /tmp/colonial_office_list/historical_document_pipeline/processed_pdfs/
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from scaffold_neo4j import scan_corpus, normalize_colony_name
from scan_contamination import (
    scan_file, LEGITIMATE_SUB_TERRITORIES, COLONY_HEADERS, HEADER_PATTERNS,
)
from rerun_colonies import evict_keys

SCRIPT_DIR = Path(__file__).parent
STATE_FILE = SCRIPT_DIR / "generated" / "corpus_state.json"
REPORT_FILE = SCRIPT_DIR / "generated" / "contamination_report.json"
RAW_OCR_BASE = Path("/tmp/colonial_office_list/historical_document_pipeline/processed_pdfs")

# Threshold: if the first foreign header appears before this % of the file,
# classify as Tier 2 (needs raw OCR re-extraction)
TIER2_THRESHOLD_PCT = 10.0

# Minimum file content to retain (lines). Don't truncate if we'd keep less than this.
MIN_LINES_AFTER_TRUNCATION = 20

# ---------------------------------------------------------------------------
# Known colony header patterns for raw OCR section detection
# ---------------------------------------------------------------------------

# ALL-CAPS colony names as they appear in raw OCR section headers.
# Maps canonical name -> set of OCR header variants.
COLONY_OCR_HEADERS = {}

def _build_ocr_header_variants():
    """Build mapping of canonical colony name -> ALL-CAPS header variants."""
    for name in COLONY_HEADERS:
        upper = name.upper()
        variants = {upper, upper + '.', upper + ':'}
        # Handle multi-word variants
        if 'and' in name.lower():
            # "Trinidad and Tobago" -> "TRINIDAD AND TOBAGO."
            pass  # already handled by upper
        COLONY_OCR_HEADERS[name] = variants
    # Add additional aliases
    COLONY_OCR_HEADERS.setdefault('Ascension', set()).update({'ASCENSION.', 'ASCENSION'})
    COLONY_OCR_HEADERS.setdefault('St Helena', set()).update(
        {"ST. HELENA.", "ST HELENA.", "SAINT HELENA."})
    COLONY_OCR_HEADERS.setdefault('St Lucia', set()).update(
        {"ST. LUCIA.", "ST LUCIA.", "SAINT LUCIA."})
    COLONY_OCR_HEADERS.setdefault('St Vincent', set()).update(
        {"ST. VINCENT.", "ST VINCENT.", "SAINT VINCENT."})
    COLONY_OCR_HEADERS.setdefault('St Kitts', set()).update(
        {"ST. KITTS.", "ST KITTS.", "ST. CHRISTOPHER.", "ST CHRISTOPHER.",
         "ST. KITTS-NEVIS.", "ST KITTS-NEVIS."})
    COLONY_OCR_HEADERS.setdefault('Cape of Good Hope', set()).update(
        {"CAPE OF GOOD HOPE.", "THE CAPE OF GOOD HOPE.", "CAPE COLONY."})
    COLONY_OCR_HEADERS.setdefault('Dominion of Canada', set()).update(
        {"DOMINION OF CANADA.", "CANADA."})
    COLONY_OCR_HEADERS.setdefault('Canada', set()).update(
        {"CANADA.", "DOMINION OF CANADA."})
    COLONY_OCR_HEADERS.setdefault('British Bechuanaland', set()).update(
        {"BRITISH BECHUANALAND.", "BECHUANALAND.", "BECHUANALAND PROTECTORATE."})
    COLONY_OCR_HEADERS.setdefault('British Guiana', set()).update(
        {"BRITISH GUIANA.", "GUIANA."})
    COLONY_OCR_HEADERS.setdefault('British Honduras', set()).update(
        {"BRITISH HONDURAS.", "HONDURAS."})
    COLONY_OCR_HEADERS.setdefault('Windward Islands', set()).update(
        {"WINDWARD ISLANDS.", "THE WINDWARD ISLANDS."})
    COLONY_OCR_HEADERS.setdefault('Trinidad and Tobago', set()).update(
        {"TRINIDAD AND TOBAGO.", "TRINIDAD."})
    COLONY_OCR_HEADERS.setdefault('West Indies - Cayman, Turks and Caicos', set()).update(
        {"WEST INDIES.", "CAYMAN ISLANDS.", "TURKS AND CAICOS ISLANDS."})

_build_ocr_header_variants()

# Reverse lookup: ALL-CAPS text -> canonical name
_OCR_HEADER_TO_COLONY = {}
for _canon, _variants in COLONY_OCR_HEADERS.items():
    for _v in _variants:
        _OCR_HEADER_TO_COLONY[_v.strip().rstrip('.:')] = _canon


# ---------------------------------------------------------------------------
# Contamination report analysis
# ---------------------------------------------------------------------------

def load_report() -> list[dict]:
    """Load contamination report and return list of contaminated file entries."""
    if not REPORT_FILE.exists():
        print(f"ERROR: Contamination report not found: {REPORT_FILE}")
        print("Run: python scan_contamination.py")
        sys.exit(1)
    report = json.loads(REPORT_FILE.read_text())
    return report.get('files', [])


def filter_false_positives(entries: list[dict]) -> list[dict]:
    """Apply LEGITIMATE_SUB_TERRITORIES filtering to report entries."""
    filtered = []
    for entry in entries:
        colony = entry['expected_colony']
        legit = LEGITIMATE_SUB_TERRITORIES.get(colony, set())
        remaining = {
            c: d for c, d in entry['foreign_colonies'].items()
            if c not in legit
        }
        if not remaining:
            continue
        # Recalculate severity
        sev = 0
        for c, d in remaining.items():
            for ln, txt in d['lines']:
                sev += 2 if txt.startswith('[SIG]') else 10
        if sev < 5:
            continue
        entry = dict(entry)
        entry['foreign_colonies'] = remaining
        entry['severity_score'] = sev
        filtered.append(entry)
    return filtered


def classify_tier(entry: dict) -> tuple[int, int | None, float]:
    """Classify a contaminated file as Tier 1 or Tier 2.

    Returns (tier, first_foreign_header_line, first_header_pct).
    """
    first_header_line = None
    for colony, data in entry['foreign_colonies'].items():
        for ln, txt in data['lines']:
            if not txt.startswith('[SIG]'):
                if first_header_line is None or ln < first_header_line:
                    first_header_line = ln

    if first_header_line is None:
        # Only signature hits, no headers — treat as Tier 1 (likely minor)
        return 1, None, 0.0

    pct = first_header_line / entry['total_lines'] * 100
    # Tier 2 if foreign content starts early, or if the file is too small to truncate
    if pct < TIER2_THRESHOLD_PCT or first_header_line <= MIN_LINES_AFTER_TRUNCATION:
        return 2, first_header_line, pct
    return 1, first_header_line, pct


# ---------------------------------------------------------------------------
# Tier 1: Truncation
# ---------------------------------------------------------------------------

def find_truncation_point(filepath: Path, entry: dict) -> int | None:
    """Find the line number at which to truncate the file.

    Scans backward from the first foreign header to find the actual section
    break — an ALL-CAPS colony name on its own line.

    Returns 0-indexed line number to truncate AT (exclusive), or None if
    no good truncation point found.
    """
    lines = filepath.read_text(errors='replace').split('\n')
    total = len(lines)

    # Find the first foreign colony header line number (1-indexed from report)
    first_foreign = None
    for colony, data in entry['foreign_colonies'].items():
        for ln, txt in data['lines']:
            if not txt.startswith('[SIG]'):
                if first_foreign is None or ln < first_foreign:
                    first_foreign = ln

    if first_foreign is None:
        return None

    # Convert to 0-indexed
    first_idx = first_foreign - 1

    # Scan backward from the first foreign header to find the section break.
    # Look for an ALL-CAPS line that matches a colony name pattern.
    # The break should be within ~50 lines before the header.
    search_start = max(0, first_idx - 50)
    best_break = first_idx  # default: truncate at the foreign header itself

    for i in range(first_idx, search_start - 1, -1):
        line = lines[i].strip()
        if not line:
            continue
        # Check if this line is a colony header (ALL-CAPS, title-case, or markdown)
        clean = re.sub(r'^#{1,6}\s+', '', line).strip('*. :')
        if not clean or len(clean) < 3:
            continue
        # Try the cleaned text in UPPER form against our lookup
        upper_clean = clean.upper()
        if upper_clean in _OCR_HEADER_TO_COLONY:
            # Verify it looks like a standalone header line (not embedded in prose)
            # Must be short and not contain typical prose indicators
            if len(clean.split()) <= 8 and not re.search(r'[,;].*[a-z]', line):
                best_break = i
                break

    # Validate: don't truncate if we'd lose most of the content
    if best_break < MIN_LINES_AFTER_TRUNCATION:
        return None

    # Also scan backward from break point to skip any blank lines / separators
    while best_break > 0 and not lines[best_break - 1].strip():
        best_break -= 1

    return best_break


def apply_truncation(filepath: Path, truncation_line: int, dry_run: bool = False) -> dict:
    """Truncate a file at the given line (0-indexed, exclusive).

    Returns a dict with before/after stats.
    """
    text = filepath.read_text(errors='replace')
    lines = text.split('\n')
    original_count = len(lines)

    truncated = lines[:truncation_line]

    # Strip trailing blank lines
    while truncated and not truncated[-1].strip():
        truncated.pop()

    new_count = len(truncated)
    removed = original_count - new_count

    result = {
        'original_lines': original_count,
        'new_lines': new_count,
        'removed_lines': removed,
        'truncated_at': truncation_line,
    }

    if not dry_run:
        filepath.write_text('\n'.join(truncated) + '\n')
        result['written'] = True
    else:
        result['written'] = False

    return result


# ---------------------------------------------------------------------------
# Tier 2: Raw OCR Re-extraction
# ---------------------------------------------------------------------------

def get_raw_ocr_path(year: int) -> Path:
    """Get path to raw OCR file for a given year."""
    return RAW_OCR_BASE / f"colonial-office-list-{year}" / "olmocr_results.md"


def find_colony_section_in_ocr(ocr_text: str, target_colony: str,
                                all_colonies_in_year: list[str]) -> tuple[int, int] | None:
    """Find the start and end line of a colony's section in raw OCR text.

    Returns (start_line, end_line) as 0-indexed inclusive/exclusive, or None.
    """
    lines = ocr_text.split('\n')
    total = len(lines)

    target_variants = COLONY_OCR_HEADERS.get(target_colony, set())
    if not target_variants:
        # Fallback: use uppercase name
        target_variants = {target_colony.upper(), target_colony.upper() + '.'}

    # Build set of all colony header variants for end-boundary detection
    all_colony_variants = {}
    for colony in all_colonies_in_year:
        if colony == target_colony:
            continue
        variants = COLONY_OCR_HEADERS.get(colony, set())
        if not variants:
            variants = {colony.upper(), colony.upper() + '.'}
        for v in variants:
            clean = v.strip().strip('*_').rstrip('.').rstrip(':').strip()
            all_colony_variants[clean] = colony
            all_colony_variants[f'THE {clean}'] = colony

    def _clean_ocr_line(s: str) -> str:
        """Strip markdown, punctuation, and whitespace for header matching."""
        s = s.strip()
        s = re.sub(r'^#{1,6}\s+', '', s)  # markdown headers
        s = s.strip('*_')  # bold/italic markers
        s = s.rstrip('.').rstrip(':').strip()
        return s

    # Normalize target variants for matching
    target_clean = {_clean_ocr_line(v) for v in target_variants}
    # Also add "THE {colony}" variants
    for v in list(target_clean):
        target_clean.add(f'THE {v}')

    # Find all occurrences of the target colony header
    target_starts = []
    for i, line in enumerate(lines):
        stripped = _clean_ocr_line(line)
        if not stripped:
            continue
        if stripped in target_clean:
            # Verify this is a real section header, not a ToC entry:
            # Check that the next ~10 lines aren't densely packed with other colony names
            toc_density = 0
            for j in range(i + 1, min(i + 10, total)):
                check = _clean_ocr_line(lines[j])
                if check in all_colony_variants:
                    toc_density += 1
            if toc_density >= 3:
                continue  # Likely a ToC entry, skip
            # Skip entries in appendix/index sections (parliamentary papers, etc.)
            in_appendix = False
            for j in range(max(0, i - 200), i):
                line_check = lines[j].upper()
                if any(kw in line_check for kw in [
                    'PARLIAMENTARY PAPERS', 'LIST OF PAPERS',
                    'INDEX TO COLONIAL', 'GENERAL INDEX',
                    'BIOGRAPHICAL INDEX', 'INDEX OF NAMES',
                ]):
                    in_appendix = True
                    break
            if in_appendix:
                continue
            target_starts.append(i)

    if not target_starts:
        return None

    def _find_section_end(sec_start: int) -> int:
        """Find the end boundary for a section starting at sec_start."""
        sec_end = total
        for i in range(sec_start + 5, total):
            stripped = _clean_ocr_line(lines[i])
            if not stripped:
                continue
            if stripped in all_colony_variants:
                toc_density = 0
                for j in range(i + 1, min(i + 10, total)):
                    check = _clean_ocr_line(lines[j])
                    if check in all_colony_variants:
                        toc_density += 1
                if toc_density >= 3:
                    continue  # ToC entry
                sec_end = i
                break
        return sec_end

    # If multiple occurrences, pick the LONGEST section (main content, not appendix)
    best_start = target_starts[0]
    best_end = _find_section_end(best_start)
    best_len = best_end - best_start

    for s in target_starts[1:]:
        e = _find_section_end(s)
        span = e - s
        if span > best_len:
            best_start, best_end, best_len = s, e, span

    return (best_start, best_end)


def apply_ocr_extraction(filepath: Path, year: int, colony: str,
                          all_colonies_in_year: list[str],
                          dry_run: bool = False) -> dict:
    """Re-extract a colony's section from raw OCR and replace the source file.

    Returns a dict with extraction stats.
    """
    ocr_path = get_raw_ocr_path(year)
    if not ocr_path.exists():
        return {'error': f'Raw OCR not found: {ocr_path}', 'written': False}

    ocr_text = ocr_path.read_text(errors='replace')
    bounds = find_colony_section_in_ocr(ocr_text, colony, all_colonies_in_year)

    if bounds is None:
        return {'error': f'Colony section not found in OCR: {colony} ({year})', 'written': False}

    start, end = bounds
    ocr_lines = ocr_text.split('\n')
    section = ocr_lines[start:end]

    # Strip trailing blank lines
    while section and not section[-1].strip():
        section.pop()

    original_lines = len(filepath.read_text(errors='replace').split('\n')) if filepath.exists() else 0
    new_lines = len(section)

    result = {
        'original_lines': original_lines,
        'new_lines': new_lines,
        'ocr_section': f'L{start+1}-L{end}',
        'first_5_lines': [l[:120] for l in section[:5]],
    }

    if not dry_run:
        filepath.write_text('\n'.join(section) + '\n')
        result['written'] = True
    else:
        result['written'] = False

    return result


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_fix(filepath: Path, colony: str) -> dict:
    """Re-scan a fixed file and return validation result."""
    if not filepath.exists():
        return {'valid': False, 'error': 'File does not exist'}
    result = scan_file(filepath, colony)
    if result is None:
        return {'valid': True, 'residual_severity': 0}
    return {
        'valid': result['severity_score'] < 5,
        'residual_severity': result['severity_score'],
        'residual_colonies': list(result['foreign_colonies'].keys()),
    }


# ---------------------------------------------------------------------------
# CLI Commands
# ---------------------------------------------------------------------------

def cmd_scan(args):
    """Report which files need fixing and which tier."""
    entries = load_report()
    entries = filter_false_positives(entries)

    if args.year:
        entries = [e for e in entries if e.get('year') == args.year]
    if args.colony:
        entries = [e for e in entries if e['expected_colony'] == args.colony]

    tier1 = []
    tier2 = []

    for entry in entries:
        tier, first_line, pct = classify_tier(entry)
        info = {
            'key': entry.get('key', f"{entry['expected_colony']}_{entry.get('year', '?')}"),
            'file': entry['file'],
            'colony': entry['expected_colony'],
            'year': entry.get('year'),
            'severity': entry['severity_score'],
            'first_foreign_line': first_line,
            'first_foreign_pct': round(pct, 1),
            'foreign_colonies': list(entry['foreign_colonies'].keys()),
            'total_lines': entry['total_lines'],
        }
        if tier == 1:
            tier1.append(info)
        else:
            tier2.append(info)

    print(f"After false-positive filtering: {len(entries)} contaminated files")
    print(f"  Tier 1 (truncation): {len(tier1)}")
    print(f"  Tier 2 (raw OCR):    {len(tier2)}")
    print(f"{'='*80}\n")

    if tier1:
        print("TIER 1 — Truncation (foreign content appended):")
        print("-" * 60)
        for info in sorted(tier1, key=lambda x: -x['severity']):
            print(f"  {info['key']:40s} sev={info['severity']:4d}  "
                  f"foreign_at={info['first_foreign_pct']:>5.1f}%  "
                  f"cols={info['foreign_colonies']}")
        print()

    if tier2:
        print("TIER 2 — Raw OCR Re-extraction (foreign content interleaved):")
        print("-" * 60)
        for info in sorted(tier2, key=lambda x: -x['severity']):
            print(f"  {info['key']:40s} sev={info['severity']:4d}  "
                  f"foreign_at={info['first_foreign_pct']:>5.1f}%  "
                  f"cols={info['foreign_colonies']}")
        print()


def cmd_fix(args):
    """Apply fixes to contaminated files."""
    entries = load_report()
    entries = filter_false_positives(entries)

    if args.year:
        entries = [e for e in entries if e.get('year') == args.year]
    if args.colony:
        entries = [e for e in entries if e['expected_colony'] == args.colony]

    # Build colony-per-year lookup for Tier 2
    corpus = scan_corpus(SCRIPT_DIR)

    dry_run = args.dry_run
    tier1_only = args.tier1_only
    tier2_only = args.tier2_only

    results = {'tier1': [], 'tier2': [], 'skipped': [], 'errors': []}

    for entry in entries:
        tier, first_line, pct = classify_tier(entry)
        key = entry.get('key', f"{entry['expected_colony']}_{entry.get('year', '?')}")
        filepath = Path(entry['file'])
        colony = entry['expected_colony']
        year = entry.get('year')

        if tier == 1 and tier2_only:
            results['skipped'].append({'key': key, 'reason': 'tier1 skipped (--tier2-only)'})
            continue
        if tier == 2 and tier1_only:
            results['skipped'].append({'key': key, 'reason': 'tier2 skipped (--tier1-only)'})
            continue

        if tier == 1:
            # Tier 1: Truncation
            trunc_point = find_truncation_point(filepath, entry)
            if trunc_point is None:
                # Check if this is a signature-only file (no actual headers)
                has_headers = any(
                    not txt.startswith('[SIG]')
                    for data in entry['foreign_colonies'].values()
                    for _, txt in data['lines']
                )
                if not has_headers:
                    results['skipped'].append({
                        'key': key,
                        'reason': f'signature-only hits (sev={entry["severity_score"]}), no fix needed'
                    })
                    print(f"  [SKIP]  TIER1 {key}: signature-only hits "
                          f"(sev={entry['severity_score']}), likely false positive")
                    continue
                results['errors'].append({
                    'key': key, 'tier': 1,
                    'error': 'No valid truncation point found'
                })
                continue

            result = apply_truncation(filepath, trunc_point, dry_run=dry_run)
            result['key'] = key
            result['tier'] = 1

            # Validate if we actually wrote
            if result['written']:
                val = validate_fix(filepath, colony)
                result['validation'] = val

            results['tier1'].append(result)

            status = "DRY-RUN" if dry_run else ("OK" if result.get('validation', {}).get('valid', True) else "RESIDUAL")
            print(f"  [{status}] TIER1 {key}: truncated at L{trunc_point} "
                  f"({result['original_lines']} -> {result['new_lines']} lines, "
                  f"-{result['removed_lines']})")

        else:
            # Tier 2: Raw OCR re-extraction
            if year is None:
                results['errors'].append({
                    'key': key, 'tier': 2, 'error': 'No year in report entry'
                })
                continue

            all_colonies = [canonical for _, _, canonical in corpus.get(year, [])]
            result = apply_ocr_extraction(
                filepath, year, colony, all_colonies, dry_run=dry_run
            )
            result['key'] = key
            result['tier'] = 2

            if result.get('error'):
                results['errors'].append({
                    'key': key, 'tier': 2, 'error': result['error']
                })
                print(f"  [ERROR] TIER2 {key}: {result['error']}")
                continue

            if result['written']:
                val = validate_fix(filepath, colony)
                result['validation'] = val

            results['tier2'].append(result)

            status = "DRY-RUN" if dry_run else ("OK" if result.get('validation', {}).get('valid', True) else "RESIDUAL")
            print(f"  [{status}] TIER2 {key}: OCR section {result['ocr_section']} "
                  f"({result['original_lines']} -> {result['new_lines']} lines)")
            if dry_run and result.get('first_5_lines'):
                for line in result['first_5_lines']:
                    print(f"          | {line}")

    # Summary
    print(f"\n{'='*80}")
    print(f"Summary {'(DRY RUN)' if dry_run else ''}:")
    print(f"  Tier 1 fixed: {len(results['tier1'])}")
    print(f"  Tier 2 fixed: {len(results['tier2'])}")
    print(f"  Skipped:      {len(results['skipped'])}")
    print(f"  Errors:       {len(results['errors'])}")

    if results['errors']:
        print(f"\nErrors:")
        for err in results['errors']:
            print(f"  {err['key']}: {err['error']}")

    # Check for residual contamination
    residuals = []
    for r in results['tier1'] + results['tier2']:
        val = r.get('validation', {})
        if not val.get('valid', True):
            residuals.append(r)
    if residuals and not dry_run:
        print(f"\nResidual contamination ({len(residuals)} files):")
        for r in residuals:
            val = r['validation']
            print(f"  {r['key']}: severity={val.get('residual_severity', '?')} "
                  f"cols={val.get('residual_colonies', [])}")

    return results


def cmd_evict(args):
    """Evict fixed files from corpus state for re-extraction."""
    if not STATE_FILE.exists():
        print(f"ERROR: State file not found: {STATE_FILE}")
        sys.exit(1)

    entries = load_report()
    entries = filter_false_positives(entries)

    # Only evict files that exist and are now clean (or at least attempted)
    keys_to_evict = []
    for entry in entries:
        key = entry.get('key')
        if not key:
            continue
        filepath = Path(entry['file'])
        if filepath.exists():
            keys_to_evict.append(key)

    if not keys_to_evict:
        print("No files to evict.")
        return

    state = json.loads(STATE_FILE.read_text())
    print(f"Loaded state: {len(state.get('completed', {}))} completed entries")
    print(f"Evicting {len(keys_to_evict)} contaminated-file entries...")

    evicted = evict_keys(state, keys_to_evict)

    state['last_updated'] = datetime.now().isoformat()
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))
    print(f"Evicted {evicted} entries. Remaining: {len(state.get('completed', {}))}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Fix contaminated source files (two-tier approach)')
    parser.add_argument('--scan', action='store_true',
                        help='Report which files need fixing and which tier')
    parser.add_argument('--all', action='store_true',
                        help='Fix all contaminated files')
    parser.add_argument('--year', type=int, help='Fix only this year')
    parser.add_argument('--colony', type=str, help='Fix only this colony')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing files')
    parser.add_argument('--tier1-only', action='store_true',
                        help='Only apply Tier 1 (truncation) fixes')
    parser.add_argument('--tier2-only', action='store_true',
                        help='Only apply Tier 2 (raw OCR) fixes')
    parser.add_argument('--evict', action='store_true',
                        help='Evict fixed files from corpus state')
    args = parser.parse_args()

    if not any([args.scan, args.all, args.year, args.colony, args.evict]):
        parser.print_help()
        sys.exit(1)

    if args.evict:
        cmd_evict(args)
        return

    if args.scan:
        cmd_scan(args)
        return

    # Fix mode
    if not args.all and not args.year and not args.colony:
        print("ERROR: Specify --all, --year, or --colony to fix files")
        sys.exit(1)

    cmd_fix(args)


if __name__ == '__main__':
    main()
