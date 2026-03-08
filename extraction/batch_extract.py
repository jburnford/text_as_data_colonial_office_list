#!/usr/bin/env python3
"""
Universal Colonial Office List — Batch Extraction via Gemini
=============================================================

Generalized extraction orchestrator. Works with any colony + guide pair.
Gemini generates compact Python extraction code; this script orchestrates,
validates, and logs the process.

Usage:
    export GOOGLE_API_KEY="..."

    # Extract a single colony group using its guide
    python extraction/batch_extract.py --colony "Sierra Leone" --guide guides/west_africa_guide.md

    # Extract a year range
    python extraction/batch_extract.py --colony "Jamaica" --guide guides/caribbean_guide.md --start 1867 --end 1900

    # Single year
    python extraction/batch_extract.py --colony "Ceylon" --guide guides/south_southeast_asia_guide.md --year 1896

    # Test run (first, middle, last available year)
    python extraction/batch_extract.py --colony "Sierra Leone" --guide guides/west_africa_guide.md --test

    # List available files for a colony
    python extraction/batch_extract.py --colony "Sierra Leone" --list

    # Process ALL colonies in a group
    python extraction/batch_extract.py --group "West Africa" --guide guides/west_africa_guide.md

Output:
    extraction/{colony_slug}/{year}_extraction.py     # Extraction code
    extraction/{colony_slug}/json/{colony}_{year}.json # JSON output
    extraction/{colony_slug}/logs/extraction_log.json  # Processing log
"""

import os
import sys
import json
import re
import subprocess
import argparse
import time
import gc
import tempfile
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Tuple

# Load .env from project root
_project_root = Path(__file__).resolve().parent.parent
try:
    from dotenv import load_dotenv
    load_dotenv(_project_root / '.env')
except ImportError:
    pass

BASE_DIR = _project_root


def _get_rss_mb() -> float:
    """Get current process RSS in MB (Linux only)."""
    try:
        with open('/proc/self/status') as f:
            for line in f:
                if line.startswith('VmRSS:'):
                    return int(line.split()[1]) / 1024
    except Exception:
        pass
    return 0.0

# =============================================================================
# CORPUS INVENTORY INTEGRATION
# =============================================================================

def load_corpus_inventory() -> dict:
    """Load corpus inventory for file discovery."""
    inv_path = BASE_DIR / "scaffolding" / "corpus_inventory.json"
    if not inv_path.exists():
        print("ERROR: Run scaffolding/build_corpus_inventory.py first")
        sys.exit(1)
    with open(inv_path) as f:
        return json.load(f)


def find_colony_files(colony_name: str, inventory: dict = None) -> Dict[int, Path]:
    """Find all source files for a colony, return dict of year -> path."""
    if inventory is None:
        inventory = load_corpus_inventory()

    files = {}
    for entry in inventory["files"]:
        if entry["canonical_name"] == colony_name and entry["file_size"] > 0:
            year = entry["year"]
            filepath = BASE_DIR / entry["filepath"]
            if filepath.exists():
                files[year] = filepath

    return files


def find_group_colonies(group_name: str, inventory: dict = None) -> List[str]:
    """Find all colonies belonging to a colony group."""
    if inventory is None:
        inventory = load_corpus_inventory()

    colonies = set()
    for entry in inventory["files"]:
        if entry["colony_group"] == group_name:
            colonies.add(entry["canonical_name"])

    return sorted(colonies)


def colony_slug(colony_name: str) -> str:
    """Convert colony name to filesystem-safe slug."""
    return colony_name.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")


# =============================================================================
# SECTION MAP VIA GEMINI
# =============================================================================

SECTION_MAP_PROMPT = '''Analyze this Colonial Office List document and identify the major SECTIONS (departments and topics).

Each section should have:
- "name": Section/department heading as it appears in the text
- "type": One of "narrative", "personnel", "statistics", "council"
  - "narrative" = descriptive text (history, geography, trade, climate, etc.)
  - "personnel" = a DEPARTMENT listing officials with names, positions, salaries
  - "statistics" = tables of finances, population, imports/exports
  - "council" = lists of council members (Executive Council, Legislative Council)
- "start_line": First line number (1-indexed) of this section
- "end_line": Last line number (1-indexed) before the next section starts

CRITICAL RULES:
- A "personnel" section is an ENTIRE DEPARTMENT, not an individual person
- Department headers are things like "Colonial Secretary's Office.", "Medical Department.", "Treasury.", "Police Department."
- ALL the officials listed under a department header belong to that ONE section
- A personnel section starts at the department header and ends where the NEXT department header begins
- Do NOT create separate sections for individual officials or sub-headings within a department
- Typical personnel sections span 5-50+ lines and contain multiple officials
- If a section has only 1-2 lines, it is probably NOT a separate section — merge it with the surrounding department
- Return ONLY valid JSON, no markdown fences, no explanation

Example output for a typical Colonial Office List:
[
  {"name": "THE GOLD COAST.", "type": "narrative", "start_line": 1, "end_line": 3},
  {"name": "History.", "type": "narrative", "start_line": 4, "end_line": 39},
  {"name": "Statistics of the Colony.", "type": "statistics", "start_line": 40, "end_line": 55},
  {"name": "Executive Council.", "type": "council", "start_line": 56, "end_line": 60},
  {"name": "Civil Establishment.", "type": "personnel", "start_line": 61, "end_line": 75},
  {"name": "Colonial Secretary's Office.", "type": "personnel", "start_line": 76, "end_line": 95},
  {"name": "Treasury.", "type": "personnel", "start_line": 96, "end_line": 115},
  {"name": "Medical Department.", "type": "personnel", "start_line": 116, "end_line": 160},
  {"name": "Police Department.", "type": "personnel", "start_line": 161, "end_line": 185}
]

Document text:
'''


def get_section_map(model, source_text: str) -> Optional[List[dict]]:
    """Use Gemini to produce a structured section map of the document.

    Returns list of {"name", "type", "start_line", "end_line"} dicts,
    or None if the call fails.
    """
    # Prepend line numbers so Gemini can reference exact positions
    lines = source_text.split('\n')
    numbered_text = '\n'.join(f'{i+1:4d}| {line}' for i, line in enumerate(lines))
    prompt = SECTION_MAP_PROMPT + numbered_text

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.0,
                "max_output_tokens": 8000,
            }
        )
        text = response.text.strip()
        # Strip markdown fences if present
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        sections = json.loads(text.strip())
        if isinstance(sections, list) and len(sections) > 0:
            # Filter out sections with None/missing names (Gemini sometimes returns these)
            sections = [s for s in sections if s.get("name") is not None]
            return sections if sections else None
    except Exception as e:
        print(f"  Section map failed ({e}), falling back to regex")
    return None


def save_narrative_sections(section_map: List[dict], source_text: str,
                            output_dir: Path, colony: str, year: int):
    """Save narrative/statistics/council sections to separate files for RAG indexing."""
    rag_dir = output_dir / "rag"
    rag_dir.mkdir(parents=True, exist_ok=True)

    lines = source_text.split('\n')
    slug = colony_slug(colony)
    saved = []

    for sec in section_map:
        if sec["type"] in ("narrative", "statistics", "council"):
            start = max(0, sec["start_line"] - 1)  # Convert 1-indexed to 0-indexed
            end = min(len(lines), sec["end_line"])
            section_text = '\n'.join(lines[start:end])

            if len(section_text.strip()) < 20:
                continue

            safe_name = re.sub(r'[^a-zA-Z0-9_]', '', sec["name"].replace(" ", "_"))[:40]
            filename = f"{slug}_{year}_{safe_name}.txt"
            filepath = rag_dir / filename
            with open(filepath, 'w') as f:
                f.write(f"Colony: {colony}\n")
                f.write(f"Year: {year}\n")
                f.write(f"Section: {sec['name']}\n")
                f.write(f"Type: {sec['type']}\n")
                f.write(f"---\n")
                f.write(section_text)
            saved.append(filename)

    return saved


MAX_LINES_PER_GROUP = 25  # Max source lines in a grouped extraction call


def get_personnel_sections_from_map(section_map: List[dict]) -> List[tuple]:
    """Extract personnel section names from a Gemini section map.

    Uses line counts to group small ADJACENT sections together while keeping
    large sections solo. Non-contiguous sections (with narrative/statistics
    gaps between them) are never grouped together.

    Returns list of (label, min_start_line) tuples. The start_line is used
    to disambiguate duplicate section names (e.g., two "Civil Establishment."
    sections when a file covers multiple colonies).
    """
    # Sort all sections by start_line to determine adjacency
    sorted_all = sorted(section_map, key=lambda s: s["start_line"])
    personnel = [s for s in sorted_all if s["type"] == "personnel"]

    if not personnel:
        return [("Full Document", 1)]

    # Build adjacency info: which personnel sections are directly next to each other
    # (no non-personnel section between them)
    is_adjacent_to_prev = [False] * len(personnel)

    for i in range(1, len(personnel)):
        prev = personnel[i - 1]
        curr = personnel[i]
        # Check if there's any non-personnel section between prev and curr
        gap = False
        for s in sorted_all:
            if s["start_line"] > prev["end_line"] and s["start_line"] < curr["start_line"]:
                if s["type"] != "personnel":
                    gap = True
                    break
        is_adjacent_to_prev[i] = not gap

    # If few sections and all contiguous, no grouping needed
    if len(personnel) <= 15 and all(is_adjacent_to_prev[1:]):
        return [(s["name"], s["start_line"]) for s in personnel]

    # Smart grouping: bin-pack only ADJACENT sections by line count
    grouped = []
    current_group = []
    current_start = None
    current_lines = 0

    for i, sec in enumerate(personnel):
        sec_lines = sec["end_line"] - sec["start_line"] + 1

        # Break group if this section is not adjacent to previous
        if i > 0 and not is_adjacent_to_prev[i] and current_group:
            grouped.append((" / ".join(current_group), current_start))
            current_group = []
            current_start = None
            current_lines = 0

        # Large sections always go solo
        if sec_lines > MAX_LINES_PER_GROUP:
            if current_group:
                grouped.append((" / ".join(current_group), current_start))
                current_group = []
                current_start = None
                current_lines = 0
            grouped.append((sec["name"], sec["start_line"]))
            continue

        # Would adding this section exceed the limit?
        if current_lines + sec_lines > MAX_LINES_PER_GROUP and current_group:
            grouped.append((" / ".join(current_group), current_start))
            current_group = []
            current_start = None
            current_lines = 0

        current_group.append(sec["name"])
        if current_start is None:
            current_start = sec["start_line"]
        current_lines += sec_lines

    if current_group:
        grouped.append((" / ".join(current_group), current_start))

    return grouped


# --- Regex fallback (used when Gemini section map fails) ---

PERSONNEL_START_PATTERNS = [
    r"Governor'?s?\s+Office",
    r"Executive\s+Council",
    r"Governor\s+and\s+Commander",
    r"Governor,?\s+(?:His|Her)\s+Excellency",
    r"^Governor[,.]",
    r"Civil\s+Establishment",
    r"ESTABLISHMENT",
]

DEPARTMENT_PATTERNS = [
    r"^[A-Z][a-z]+(?:'s)?\s+(?:Office|Department|Service|Branch)\s*[.:]?\s*$",
    r"^(?:[A-Z][a-z]+\s+)+(?:Office|Department|Service|Branch)\s*[.:]?\s*$",
    r"^(?:PROVINCE|DISTRICT|DIVISION|PRESIDENCY)\s+OF\s+",
    r"^(?:Police|Prisons|Education|Customs|Treasury|Audit|Survey[s]?|Railway[s]?|Medical|Judicial|Ecclesiastical|Military|Postal|Harbour[s]?|Agriculture|Forestry|Veterinary|Mines|Printing|Public\s+Works|Posts?\s+and\s+Telegraphs?|Law\s+Officers'?|Native\s+Affairs|Land\s+Registry|Volunteers?|Geological\s+Survey)\s+(?:Department|Office|Branch)?\s*[.:]?\s*$",
    r"^[A-Z][A-Z\s]{4,50}(?:DEPARTMENT|OFFICE|SERVICE|BRANCH)\s*[.:]?\s*$",
]


def _regex_find_personnel_start(text: str) -> int:
    """Regex fallback: find line where personnel data begins."""
    lines = text.split('\n')
    for i, line in enumerate(lines):
        stripped = line.strip()
        if len(stripped) > 80 or len(stripped) < 5:
            continue
        for pattern in PERSONNEL_START_PATTERNS:
            if re.search(pattern, stripped, re.IGNORECASE):
                return i
    return 0


def _regex_get_sections(text: str) -> List[str]:
    """Regex fallback: get personnel section names from text."""
    start = _regex_find_personnel_start(text)
    headers = []
    lines = text.split('\n')
    for i in range(start, len(lines)):
        stripped = lines[i].strip()
        if not stripped or len(stripped) < 3 or len(stripped) > 60:
            continue
        for pattern in DEPARTMENT_PATTERNS:
            if re.match(pattern, stripped, re.IGNORECASE):
                headers.append(stripped)
                break

    if len(headers) < 2:
        return ["Full Document"]

    if len(headers) > 20:
        grouped = []
        for i in range(0, len(headers), 3):
            chunk = headers[i:i+3]
            grouped.append(" / ".join(chunk))
        return grouped

    return headers


# =============================================================================
# PROMPT BUILDING
# =============================================================================

LARGE_FILE_THRESHOLD = 20000  # Characters — files larger than this need section-by-section


def _get_true_end_line(section_map: List[dict], target_sec: dict) -> int:
    """Get the true end line for a section by looking at the next section's start.

    Don't trust end_line from Gemini — derive it from the next section's start_line.
    This ensures no gaps between sections and no lost officials.
    """
    # Sort sections by start_line
    sorted_secs = sorted(section_map, key=lambda s: s["start_line"])
    for i, sec in enumerate(sorted_secs):
        if sec["start_line"] == target_sec["start_line"] and sec["name"] == target_sec["name"]:
            if i + 1 < len(sorted_secs):
                # End at next section's start - 1
                return sorted_secs[i + 1]["start_line"] - 1
            else:
                # Last section: use its end_line (or a large number)
                return sec["end_line"]
    return target_sec["end_line"]


def slice_section_text(source_text: str, section_map: List[dict],
                       section_name: str, start_line_hint: int = 0) -> str:
    """Slice source text to just the lines for the given section(s).

    For grouped sections ("Dept A / Dept B"), extracts the combined range.
    Uses next section's start_line to derive true end boundaries.
    start_line_hint disambiguates when multiple sections share the same name
    (e.g., two "Civil Establishment." for Sierra Leone + Gambia).
    Returns the sliced text, or the full text if section not found.
    """
    lines = source_text.split('\n')

    if " / " in section_name:
        # Grouped section: find range spanning all sub-sections
        sub_names = [s.strip() for s in section_name.split(" / ")]
        matching_secs = [sec for sec in section_map if sec["name"] in sub_names]
        # If start_line_hint provided, filter to sections near the hint
        if start_line_hint and len(matching_secs) > len(sub_names):
            matching_secs = [sec for sec in matching_secs
                             if sec["start_line"] >= start_line_hint]
            # Keep only the closest matches (same count as sub_names)
            matching_secs = sorted(matching_secs, key=lambda s: s["start_line"])[:len(sub_names)]
        if matching_secs:
            start_line = min(sec["start_line"] for sec in matching_secs)
            # For end: use the true end of the LAST matching section
            last_sec = max(matching_secs, key=lambda s: s["start_line"])
            end_line = _get_true_end_line(section_map, last_sec)
            return '\n'.join(lines[max(0, start_line - 1):min(len(lines), end_line)])
    else:
        # Single section — use start_line_hint to disambiguate duplicates
        best_match = None
        for sec in section_map:
            if sec["name"] == section_name:
                if start_line_hint and sec["start_line"] == start_line_hint:
                    best_match = sec
                    break  # Exact match on start_line
                elif not best_match:
                    best_match = sec  # First match as fallback
        if best_match:
            start = max(0, best_match["start_line"] - 1)
            end = _get_true_end_line(section_map, best_match)
            return '\n'.join(lines[start:min(len(lines), end)])

    # Fallback: return full text if section not found in map
    return source_text


def build_prompt(section_text: str, colony: str, year: int, guide_text: str,
                 section_name: Optional[str] = None) -> str:
    """Build the extraction prompt for Gemini.

    Args:
        section_text: Text to extract from (sliced to relevant section)
        colony: Canonical colony name
        year: Year being extracted
        guide_text: Full text of the colony group's extraction guide
        section_name: Section being extracted (for context)
    """
    section_context = ""
    if section_name and section_name != "Full Document":
        section_context = f"""
## Section Being Extracted
You are extracting officials from: "{section_name}"
The text below contains ONLY this section. Extract ALL officials listed.
"""

    prompt = f'''You are a code generator extracting personnel records from a British Colonial Office List.
{section_context}

## Task
Generate a Python file containing extracted data from the {colony} Colonial Office List for {year}.

## Domain Knowledge
{guide_text}

## Output Format - COMPACT
Generate ONLY valid Python code. No markdown, no explanations.

CRITICAL: Use COMPACT format to minimize output size:
- Put multiple fields on each line
- OMIT any field that would be None or []
- Only include fields with actual values

Example of COMPACT format:
"""
{colony} Colonial Office List {year} - Extracted Data
"""
COLONY = "{colony}"
YEAR = {year}

OFFICIALS = [
    {{"name": "F. M. Hodgson", "canonical_name": "Hodgson, F. M.", "given_names": "F. M.", "surname": "Hodgson",
     "position": "Governor", "department": "Civil Establishment - {colony}", "salary_min": 3000, "salary_max": 3000,
     "honors": ["C.M.G."], "military_rank": "Colonel"}},
    {{"name": "J. Smith", "canonical_name": "Smith, J.", "given_names": "J.", "surname": "Smith",
     "position": "Clerk", "department": "Treasury - {colony}", "salary_min": 200, "salary_max": 200}},
]

def get_extraction():
    return {{"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()

## Available fields (only include if value exists):
- name, canonical_name, given_names, surname (REQUIRED)
- position, department (REQUIRED)
- salary_min, salary_max (if salary mentioned)
- salary_currency (if NOT GBP — e.g., "Rs" for rupees, "HKD" for Hong Kong dollars)
- salary_scale (for 1940s-50s scale format: "A", "B", "C.1")
- allowances, duty_allowance, expatriation_pay, per_diem (if mentioned)
- acting_status (if "Acting", "Temporary", etc.)
- honors (list like ["C.M.G.", "O.B.E."])
- qualifications (list like ["M.D.", "B.A."])
- military_rank (if "Colonel", "Major", etc.)
- location, region (if mentioned)

## Extraction Rules

### Basic Extraction
1. Extract EVERY person with a name mentioned in an official position
2. "ditto" = same position type as line above (2nd ditto after Chief Clerk = 2nd Clerk)
3. Expand ONLY known abbreviations: Wm.=William, Chas.=Charles, Thos.=Thomas, Jas.=James, Jno.=John, Robt.=Robert, Geo.=George
4. Do NOT expand single initials: C. stays C., G. stays G.

### Salary Extraction
5. Early format: "300l. to 400l." → salary_min=300, salary_max=400; "200l." → both=200
6. Per diem: "5s. 6d. per diem" → per_diem="5s. 6d.", salary_min=None
7. Scale format (1940s-50s): "Scale A" → salary_scale="A"; "Scale C.1.2" → salary_scale="C.1.2"
8. Duty allowances: "£1,800, and duty allowance 360l." → salary_min=1800, duty_allowance=360
9. Non-GBP currencies: "Rs. 36,000" → salary_min=36000, salary_currency="Rs"

### Classification
10. Honors (C.M.G., K.C.M.G., O.B.E., M.B.E., C.I.E., E.D.) go in "honors" list
11. Qualifications (M.D., M.B., M.R.C.S., B.A., LL.B.) go in "qualifications" list
12. Military ranks (Colonel, Lt.-Col., Major, Captain, Brigadier) go in "military_rank" field

### Status
13. ALWAYS capture acting/temporary status: "Acting Administrator" → acting_status="Acting"

### Locations
14. Extract LOCATIONS from position titles: "District Commissioner, Accra" → location="Accra"
15. Extract LOCATIONS from section headers

### Departments
16. Department names should include colony suffix: " - {colony}"

### Vacancies
17. For pre-1940: Skip vacant positions
18. For 1940s-1950s: If vacancy has salary, create entry with name=None

### Multi-person lines
19. Split lines with multiple people into separate entries, each with same position/salary

## Source Text to Extract ({colony}, {year})
{section_text}

Generate the complete Python file now:
'''
    return prompt


# =============================================================================
# GEMINI API
# =============================================================================

def get_gemini_model():
    """Initialize and return Gemini model."""
    try:
        import google.generativeai as genai
    except ImportError:
        print("ERROR: google-generativeai not installed")
        print("Run: pip install google-generativeai")
        sys.exit(1)

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: GOOGLE_API_KEY environment variable not set")
        print("Get a free key at: https://makersuite.google.com/app/apikey")
        sys.exit(1)

    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash')


def generate_extraction_code(model, source_text: str, colony: str, year: int,
                             guide_text: str, section_name: Optional[str] = None,
                             ultra_compact: bool = False) -> str:
    """Use Gemini to generate Python extraction code.

    Args:
        ultra_compact: If True, use minimal prompt to reduce output size (retry mode).
    """
    if ultra_compact:
        prompt = build_prompt(source_text, colony, year, "", section_name)
        # Prepend aggressive compaction instruction
        prompt = ("CRITICAL: Output was truncated last time. Be EXTREMELY compact:\n"
                  "- OMIT allowances, qualifications, honors unless they are the ONLY data\n"
                  "- Use single-line dicts, no line breaks within entries\n"
                  "- OMIT salary fields if unsure\n"
                  "- Keep ONLY: name, canonical_name, surname, position, department\n\n"
                  + prompt)
    else:
        prompt = build_prompt(source_text, colony, year, guide_text, section_name)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.1,
                    "max_output_tokens": 32000,
                }
            )

            code = response.text
            # Strip markdown fences if present
            if code.startswith("```python"):
                code = code[9:]
            if code.startswith("```"):
                code = code[3:]
            if code.endswith("```"):
                code = code[:-3]

            return code.strip()

        except Exception as e:
            err_str = str(e).lower()
            if "429" in err_str or "quota" in err_str or "rate" in err_str:
                wait = 30 * (attempt + 1)
                print(f"    Rate limited — waiting {wait}s (attempt {attempt+1}/{max_retries})")
                time.sleep(wait)
            elif "safety" in err_str or "blocked" in err_str:
                print(f"    Safety filter triggered — skipping")
                raise
            else:
                if attempt < max_retries - 1:
                    print(f"    API error: {e} — retrying in 10s")
                    time.sleep(10)
                else:
                    raise


# =============================================================================
# VALIDATION
# =============================================================================

def validate_generated_code(code_path: Path) -> Tuple[bool, str, int]:
    """Validate generated Python code. Returns (valid, message, official_count)."""
    try:
        with open(code_path) as f:
            code = f.read()
        compile(code, str(code_path), 'exec')
    except SyntaxError as e:
        return False, f"Syntax error: {e}", 0

    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("extraction", code_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if not hasattr(module, 'OFFICIALS'):
            return False, "Missing OFFICIALS list", 0

        officials = module.OFFICIALS
        if not isinstance(officials, list):
            return False, "OFFICIALS is not a list", 0
        if len(officials) == 0:
            return False, "OFFICIALS list is empty", 0

        required_fields = ['name', 'position', 'department']
        first = officials[0]
        for field in required_fields:
            if field not in first:
                return False, f"Missing required field: {field}", 0

        return True, f"Valid: {len(officials)} officials", len(officials)

    except Exception as e:
        return False, f"Import error: {e}", 0


def run_extraction_to_json(code_path: Path, json_path: Path) -> bool:
    """Run generated code to produce JSON output."""
    try:
        result = subprocess.run(
            [sys.executable, str(code_path)],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            print(f"  ERROR running code: {result.stderr[:200]}")
            return False

        data = json.loads(result.stdout)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=2)
        return True

    except subprocess.TimeoutExpired:
        print("  ERROR: Execution timed out")
        return False
    except json.JSONDecodeError as e:
        print(f"  ERROR: Invalid JSON output: {e}")
        return False
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


# =============================================================================
# MAIN PROCESSING
# =============================================================================

def _extract_sub_sections(model, source_text: str, colony: str, year: int,
                          guide_text: str, grouped_name: str,
                          generated_dir: Path, result: dict,
                          section_map: Optional[List[dict]] = None,
                          group_start_line: int = 0) -> list:
    """Extract individual sub-sections from a failed grouped section.

    When "Dept A / Dept B / Dept C" fails as a group, this tries each
    department individually with its own Gemini call + retry.

    group_start_line: start_line of the parent group, used to disambiguate
    duplicate section names (e.g., same dept name in two colonies within one file).

    Returns list of extracted official dicts.
    """
    sub_sections = [s.strip() for s in grouped_name.split(" / ")]
    all_sub_officials = []

    # Find the actual start_line for each sub-section near the group's location
    sub_start_hints = {}
    if section_map and group_start_line:
        nearby = sorted(
            [s for s in section_map if s["type"] == "personnel"
             and s["start_line"] >= group_start_line],
            key=lambda s: s["start_line"]
        )
        for sub_name in sub_sections:
            for s in nearby:
                if s["name"] == sub_name:
                    sub_start_hints[sub_name] = s["start_line"]
                    break

    for sub_sec in sub_sections:
        time.sleep(2)
        print(f"      Sub-section: {sub_sec}")

        # Slice text if we have a section map
        hint = sub_start_hints.get(sub_sec, group_start_line)
        if section_map:
            sub_text = slice_section_text(source_text, section_map, sub_sec,
                                          start_line_hint=hint)
        else:
            sub_text = source_text

        try:
            sub_code = generate_extraction_code(
                model, sub_text, colony, year, guide_text, sub_sec
            )
            sub_safe = re.sub(r'[^a-zA-Z0-9_]', '', sub_sec.replace(" ", "_"))[:30]
            sub_path = generated_dir / f"{year}_{sub_safe}_extraction.py"
            with open(sub_path, 'w') as f:
                f.write(sub_code)
            sub_valid, sub_msg, sub_count = validate_generated_code(sub_path)

            # Retry ultra-compact if syntax error on individual section
            if not sub_valid and "syntax" in sub_msg.lower():
                print(f"        -> Syntax error, retrying ultra-compact...")
                time.sleep(3)
                sub_code = generate_extraction_code(
                    model, sub_text, colony, year, guide_text,
                    sub_sec, ultra_compact=True
                )
                sub_retry = generated_dir / f"{year}_{sub_safe}_retry_extraction.py"
                with open(sub_retry, 'w') as f:
                    f.write(sub_code)
                sub_valid, sub_msg, sub_count = validate_generated_code(sub_retry)
                if sub_valid:
                    sub_path = sub_retry

            if sub_valid:
                import importlib.util
                spec = importlib.util.spec_from_file_location("extraction", sub_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                all_sub_officials.extend(module.OFFICIALS)
                print(f"        -> {sub_count} officials")
            else:
                print(f"        -> FAILED: {sub_msg}")
                result["errors"].append(f"Sub-section '{sub_sec}': {sub_msg}")
        except Exception as e:
            print(f"        -> ERROR: {e}")
            result["errors"].append(f"Sub-section '{sub_sec}': {e}")

    return all_sub_officials


def process_year(model, colony: str, year: int, source_path: Path,
                 guide_text: str, output_dir: Path, force: bool = False) -> dict:
    """Process a single colony-year file.

    For small files: one Gemini call.
    For large files: one call per section, then merge.
    """
    slug = colony_slug(colony)
    generated_dir = output_dir / "generated"
    json_dir = output_dir / "json"
    generated_dir.mkdir(parents=True, exist_ok=True)
    json_dir.mkdir(parents=True, exist_ok=True)

    code_path = generated_dir / f"{year}_extraction.py"
    json_path = json_dir / f"{slug}_{year}.json"

    result = {
        "colony": colony,
        "year": year,
        "source_file": str(source_path),
        "code_file": str(code_path),
        "json_file": str(json_path),
        "status": "pending",
        "official_count": 0,
        "sections_extracted": 0,
        "errors": [],
        "timestamp": datetime.now().isoformat(),
    }

    # Check if already processed
    if json_path.exists() and not force:
        print(f"  Already processed (use --force to reprocess)")
        result["status"] = "skipped"
        try:
            with open(json_path) as f:
                data = json.load(f)
                result["official_count"] = len(data.get("officials", []))
        except Exception:
            pass
        return result

    # Read source
    try:
        with open(source_path, 'r', encoding='utf-8', errors='replace') as f:
            source_text = f.read()
    except Exception as e:
        result["status"] = "error"
        result["errors"].append(f"Failed to read source: {e}")
        return result

    print(f"  Source: {len(source_text):,} chars, {source_text.count(chr(10)):,} lines")

    all_officials = []

    # --- Two-pass architecture: section map first, then sliced extraction ---
    # Always try to get a section map via Gemini (even for smaller files)
    print(f"  Getting section map from Gemini...")
    section_map = get_section_map(model, source_text)

    if section_map:
        # Save narrative sections for RAG
        rag_files = save_narrative_sections(section_map, source_text,
                                            output_dir, colony, year)
        if rag_files:
            print(f"  Saved {len(rag_files)} narrative sections for RAG")

        # Save the full section map as JSON
        map_path = output_dir / "section_maps" / f"{slug}_{year}_sections.json"
        map_path.parent.mkdir(parents=True, exist_ok=True)
        with open(map_path, 'w') as f:
            json.dump({"colony": colony, "year": year, "sections": section_map}, f, indent=2)

        personnel_sections = [s for s in section_map if s["type"] == "personnel"]

        if not personnel_sections:
            print(f"  No personnel sections found — narrative-only file")
            result["status"] = "narrative_only"
            result["errors"].append("No personnel sections in section map")
            return result

        sections = get_personnel_sections_from_map(section_map)
        print(f"  Section map: {len(section_map)} total, {len(personnel_sections)} personnel, {len(sections)} groups")

    elif len(source_text) > LARGE_FILE_THRESHOLD:
        # Regex fallback for large files only
        sections = _regex_get_sections(source_text)
        print(f"  Regex fallback — {len(sections)} sections detected")

    else:
        # Small file, no section map: single-pass extraction
        sections = None

    if sections is not None:
        for i, section_entry in enumerate(sections):
            # Unpack (label, start_line) tuple or handle legacy string
            if isinstance(section_entry, tuple):
                section_name, section_start = section_entry
            else:
                section_name, section_start = section_entry, 0
            print(f"  Section {i+1}/{len(sections)}: {section_name}")

            if i > 0:
                time.sleep(2)  # Rate limit

            # Slice text to just this section using the section map
            if section_map:
                section_text = slice_section_text(source_text, section_map, section_name,
                                                  start_line_hint=section_start)
                chars = len(section_text)
                print(f"    Sliced: {chars:,} chars")
            else:
                section_text = source_text  # Regex fallback sends full text

            try:
                code = generate_extraction_code(
                    model, section_text, colony, year, guide_text, section_name
                )

                safe_name = re.sub(r'[^a-zA-Z0-9_]', '', section_name.replace(" ", "_"))[:30]
                section_code_path = generated_dir / f"{year}_{safe_name}_extraction.py"
                with open(section_code_path, 'w') as f:
                    f.write(code)

                valid, message, count = validate_generated_code(section_code_path)

                # --- Retry cascade for failed sections ---
                # Step 1: Ultra-compact retry
                if not valid and "syntax" in message.lower():
                    print(f"    -> Syntax error, retrying ultra-compact...")
                    time.sleep(3)
                    code = generate_extraction_code(
                        model, section_text, colony, year, guide_text,
                        section_name, ultra_compact=True
                    )
                    retry_path = generated_dir / f"{year}_{safe_name}_retry_extraction.py"
                    with open(retry_path, 'w') as f:
                        f.write(code)
                    valid, message, count = validate_generated_code(retry_path)
                    if valid:
                        section_code_path = retry_path

                # Step 2: If still failing and this is a grouped section, split into individuals
                if not valid and " / " in section_name:
                    print(f"    -> Group still failed, splitting into individual sections...")
                    sub_officials = _extract_sub_sections(
                        model, source_text, colony, year, guide_text,
                        section_name, generated_dir, result,
                        section_map=section_map,
                        group_start_line=section_start
                    )
                    all_officials.extend(sub_officials)
                    if sub_officials:
                        result["sections_extracted"] += 1
                        print(f"    -> Recovered {len(sub_officials)} officials from split")
                    continue  # Skip to next section

                # --- Success path ---
                if valid:
                    import importlib.util
                    spec = importlib.util.spec_from_file_location("extraction", section_code_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    all_officials.extend(module.OFFICIALS)
                    result["sections_extracted"] += 1
                    print(f"    -> {count} officials")
                else:
                    print(f"    -> FAILED: {message}")
                    result["errors"].append(f"Section '{section_name}': {message}")

            except Exception as e:
                print(f"    -> ERROR: {e}")
                result["errors"].append(f"Section '{section_name}': {e}")

        # Deduplicate before merging — same (name, position, department) = duplicate
        if all_officials:
            seen = set()
            deduped = []
            for off in all_officials:
                key = (off.get("name"), off.get("position"), off.get("department"))
                if key not in seen:
                    seen.add(key)
                    deduped.append(off)
            if len(deduped) < len(all_officials):
                print(f"  Deduplication: {len(all_officials)} -> {len(deduped)} "
                      f"(removed {len(all_officials) - len(deduped)} duplicates)")
            all_officials = deduped

        # Write merged file from section-based extraction
        if all_officials:
            merged_code = f'"""\n{colony} Colonial Office List {year} - Extracted Data (Merged from {len(sections)} sections)\n"""\nCOLONY = "{colony}"\nYEAR = {year}\n\nOFFICIALS = {repr(all_officials)}\n\ndef get_extraction():\n    return {{"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}}\n\ndef main():\n    import json\n    print(json.dumps(get_extraction(), indent=2))\n\nif __name__ == "__main__":\n    main()\n'
            with open(code_path, 'w') as f:
                f.write(merged_code)
            # Validate merged file
            valid, message, count = validate_generated_code(code_path)
            print(f"  Merged validation: {message}")
        else:
            result["status"] = "error"
            result["errors"].append("No officials extracted from any section")
            return result

    else:
        # --- Small file without section map: single extraction ---
        try:
            code = generate_extraction_code(model, source_text, colony, year, guide_text)
            with open(code_path, 'w') as f:
                f.write(code)
            print(f"  Generated: {code_path.name}")
        except Exception as e:
            result["status"] = "error"
            result["errors"].append(f"Code generation failed: {e}")
            return result

        # Validate single-file extraction
        valid, message, count = validate_generated_code(code_path)
        print(f"  Validation: {message}")

    if not valid:
        result["status"] = "invalid"
        result["errors"].append(message)
        return result

    result["official_count"] = count

    # Run to JSON
    if run_extraction_to_json(code_path, json_path):
        print(f"  JSON saved: {json_path.name}")
        result["status"] = "success"
    else:
        result["status"] = "run_error"
        result["errors"].append("Failed to run extraction code")

    return result


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Batch extract Colonial Office List personnel data via Gemini"
    )
    parser.add_argument("--colony", type=str, help="Canonical colony name (e.g., 'Sierra Leone')")
    parser.add_argument("--group", type=str, help="Colony group name (e.g., 'West Africa')")
    parser.add_argument("--guide", type=str, required=True, help="Path to extraction guide .md file")
    parser.add_argument("--start", type=int, help="Start year")
    parser.add_argument("--end", type=int, help="End year")
    parser.add_argument("--year", type=int, help="Single year to process")
    parser.add_argument("--test", action="store_true", help="Test run (first, middle, last year)")
    parser.add_argument("--force", action="store_true", help="Force reprocessing")
    parser.add_argument("--list", action="store_true", help="List available files and exit")
    parser.add_argument("--delay", type=float, default=2.0, help="Seconds between API calls (default: 2)")
    parser.add_argument("--_result-file", type=str, dest="_result_file",
                        help=argparse.SUPPRESS)  # Internal: subprocess writes result JSON here
    args = parser.parse_args()

    if not args.colony and not args.group:
        parser.error("Either --colony or --group is required")

    # Load guide
    guide_path = Path(args.guide)
    if not guide_path.is_absolute():
        guide_path = BASE_DIR / guide_path
    if not guide_path.exists():
        print(f"ERROR: Guide not found: {guide_path}")
        sys.exit(1)
    with open(guide_path) as f:
        guide_text = f.read()

    # Load inventory
    inventory = load_corpus_inventory()

    # Determine colonies to process
    if args.group:
        colonies = find_group_colonies(args.group, inventory)
        print(f"Colony group '{args.group}': {len(colonies)} colonies")
        for c in colonies:
            print(f"  - {c}")
    else:
        colonies = [args.colony]

    all_results = []

    # --- Single-year subprocess mode: do the work and exit ---
    if args._result_file and args.year:
        model = get_gemini_model()
        colony = colonies[0]
        files = find_colony_files(colony, inventory)
        if args.year not in files:
            print(f"  Year {args.year} not found for {colony}")
            sys.exit(1)
        slug = colony_slug(colony)
        output_dir = BASE_DIR / "extraction" / slug
        result = process_year(model, colony, args.year, files[args.year],
                              guide_text, output_dir, args.force)
        with open(args._result_file, 'w') as f:
            json.dump(result, f)
        print(f"  [RSS: {_get_rss_mb():.0f} MB at exit]")
        sys.exit(0)

    # Initialize Gemini only for single-year or --list modes
    if not args.list and args.year:
        model = get_gemini_model()

    for colony in colonies:
        files = find_colony_files(colony, inventory)
        if not files:
            print(f"\nNo files found for '{colony}'")
            continue

        years = sorted(files.keys())
        print(f"\n{'=' * 60}")
        print(f"{colony}: {len(files)} files ({min(years)}-{max(years)})")
        print(f"{'=' * 60}")

        if args.list:
            for year in years:
                size = files[year].stat().st_size
                tier = "LARGE" if size > LARGE_FILE_THRESHOLD else ""
                print(f"  {year}: {files[year].name} ({size:,} bytes) {tier}")
            continue

        # Determine which years to process
        if args.test:
            mid = years[len(years) // 2]
            process_years = sorted(set([years[0], mid, years[-1]]))
        elif args.year:
            process_years = [args.year] if args.year in files else []
        else:
            start = args.start or min(years)
            end = args.end or max(years)
            process_years = [y for y in years if start <= y <= end]

        if not process_years:
            print(f"  No years to process in range")
            continue

        # Setup output directory
        slug = colony_slug(colony)
        output_dir = BASE_DIR / "extraction" / slug

        print(f"  Processing {len(process_years)} years")
        print(f"  Output: {output_dir}")

        # --- Single year: run in-process (no subprocess overhead) ---
        if args.year and len(process_years) == 1:
            year = process_years[0]
            print(f"\n--- {colony} {year} (1/1) ---")
            result = process_year(model, colony, year, files[year],
                                  guide_text, output_dir, args.force)
            all_results.append(result)
            continue

        # --- Multiple years: fork a subprocess per year for memory isolation ---
        for i, year in enumerate(process_years):
            print(f"\n--- {colony} {year} ({i+1}/{len(process_years)}) ---")

            with tempfile.NamedTemporaryFile(mode='w', suffix='.json',
                                             delete=False, dir='/tmp') as tf:
                result_file = tf.name

            cmd = [
                sys.executable, str(Path(__file__).resolve()),
                '--colony', colony,
                '--guide', str(guide_path),
                '--year', str(year),
                '--_result-file', result_file,
            ]
            if args.force:
                cmd.append('--force')

            try:
                proc = subprocess.run(cmd, timeout=600)
                if proc.returncode == 0 and os.path.exists(result_file):
                    with open(result_file) as f:
                        result = json.load(f)
                    all_results.append(result)
                else:
                    print(f"  Subprocess failed (exit code {proc.returncode})")
                    all_results.append({
                        "colony": colony, "year": year,
                        "status": "error", "official_count": 0,
                        "errors": [f"Subprocess exit code {proc.returncode}"],
                    })
            except subprocess.TimeoutExpired:
                print(f"  Subprocess timed out (600s)")
                all_results.append({
                    "colony": colony, "year": year,
                    "status": "error", "official_count": 0,
                    "errors": ["Subprocess timed out"],
                })
            finally:
                try:
                    os.unlink(result_file)
                except OSError:
                    pass

            # Rate limiting between years
            if i < len(process_years) - 1:
                time.sleep(args.delay)

    # Save log
    if all_results and not args.list:
        log_dir = BASE_DIR / "extraction" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / f"extraction_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(log_file, 'w') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "guide": str(guide_path),
                "results": all_results,
            }, f, indent=2)

        # Summary
        success = sum(1 for r in all_results if r["status"] == "success")
        skipped = sum(1 for r in all_results if r["status"] == "skipped")
        narrative = sum(1 for r in all_results if r["status"] == "narrative_only")
        errors = sum(1 for r in all_results if r["status"] in ("error", "invalid", "run_error"))
        total_officials = sum(r["official_count"] for r in all_results)

        print(f"\n{'=' * 60}")
        print("EXTRACTION SUMMARY")
        print(f"{'=' * 60}")
        print(f"  Total files: {len(all_results)}")
        print(f"  Success: {success}")
        print(f"  Skipped: {skipped}")
        if narrative:
            print(f"  Narrative-only: {narrative}")
        print(f"  Errors: {errors}")
        print(f"  Total officials: {total_officials:,}")
        print(f"  Log: {log_file}")

        if errors:
            print(f"\nFailed files:")
            for r in all_results:
                if r["errors"]:
                    print(f"  {r['colony']} {r['year']}: {'; '.join(r['errors'][:2])}")

        # Append to re-extraction list for files that need attention
        needs_reextract = [r for r in all_results
                          if r["status"] in ("error", "invalid", "run_error", "narrative_only")
                          or (r["status"] == "success" and r["official_count"] < 5 and r["year"] > 1880)]
        if needs_reextract:
            reextract_path = BASE_DIR / "extraction" / "needs_reextraction.jsonl"
            with open(reextract_path, 'a') as f:
                for r in needs_reextract:
                    entry = {
                        "colony": r["colony"],
                        "year": r["year"],
                        "status": r["status"],
                        "official_count": r["official_count"],
                        "reason": r["errors"][0] if r["errors"] else f"Low count ({r['official_count']})",
                        "source_file": r["source_file"],
                        "timestamp": datetime.now().isoformat(),
                    }
                    f.write(json.dumps(entry) + "\n")
            print(f"\n  {len(needs_reextract)} file(s) flagged in needs_reextraction.jsonl")


if __name__ == "__main__":
    main()
