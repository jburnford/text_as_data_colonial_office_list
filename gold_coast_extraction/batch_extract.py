#!/usr/bin/env python3
"""
Gold Coast Colonial Office List - Batch Extraction via Gemini Code Generation
==============================================================================

Processes all Gold Coast files (1867-1957) chronologically using Gemini to
generate Python extraction code for each year.

Usage:
    export GOOGLE_API_KEY="..."
    python batch_extract.py                    # Process all years
    python batch_extract.py --start 1867 --end 1900  # Process range
    python batch_extract.py --year 1896        # Process single year
    python batch_extract.py --test             # Test run (1867, 1899, 1923)

Output:
    generated/gold_coast_YYYY_extraction.py    # Python code with OFFICIALS list
    json/gold_coast_YYYY.json                  # Final JSON output
    logs/extraction_log.json                   # Processing log
"""

import os
import sys
import json
import re
import subprocess
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Tuple

# Load .env file if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


# =============================================================================
# CONFIGURATION
# =============================================================================

BASE_DIR = Path(__file__).parent.parent
EXTRACTION_DIR = Path(__file__).parent
GENERATED_DIR = EXTRACTION_DIR / "generated"
JSON_DIR = EXTRACTION_DIR / "json"
LOG_DIR = EXTRACTION_DIR / "logs"

# Ensure directories exist
GENERATED_DIR.mkdir(exist_ok=True)
JSON_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# Load the extraction guide
GUIDE_PATH = EXTRACTION_DIR / "gold_coast_guide.md"


# =============================================================================
# FIND SOURCE FILES
# =============================================================================

def find_gold_coast_files() -> Dict[int, Path]:
    """Find all Gold Coast source files, return dict of year -> path."""
    files = {}

    for year_dir in sorted(BASE_DIR.glob("*_manual_parsed")):
        year_match = re.match(r"(\d{4})_manual_parsed", year_dir.name)
        if not year_match:
            continue
        year = int(year_match.group(1))

        # Look for Gold Coast files with various naming patterns
        patterns = [
            "gold_coast.txt", "gold_coast_colony.txt",
            "the_gold_coast.txt", "the_gold_coast_colony.txt",
            "GOLD_COAST.txt", "GOLD_COAST.md",
            "THE_GOLD_COAST.txt", "THE_GOLD_COAST.md",
            "THE_GOLD_COAST_COLONY.txt", "THE_GOLD_COAST_COLONY.md",
            "GOLD_COAST_COLONY.txt", "Gold_Coast.txt",
            "the_gold_coast.md", "GOLD_COAST_GHANA.txt"
        ]

        for pattern in patterns:
            candidate = year_dir / pattern
            if candidate.exists():
                files[year] = candidate
                break

        # Fallback: case-insensitive search
        if year not in files:
            for f in year_dir.iterdir():
                if "gold" in f.name.lower() and "coast" in f.name.lower():
                    if not f.name.endswith(":Zone.Identifier"):
                        files[year] = f
                        break

    return files


# =============================================================================
# CHUNKING - Split large files by section
# =============================================================================

# Section header patterns (department/office names, regional sections)
SECTION_PATTERNS = [
    r"^[A-Z][a-z]+(?:'s)?\s+(?:Office|Department)\.$",  # "Governor's Office.", "Medical Department."
    r"^(?:ASHANTI|NORTHERN TERRITORIES|TOGOLAND)\.$",    # Regional sections
    r"^[A-Z][a-z]+\s+[A-Z][a-z]+\s+(?:Office|Department)\.$",  # "Colonial Secretary's Office."
    r"^(?:Police|Prisons|Education|Customs|Treasury|Audit|Survey|Railway)\.$",  # Single-word sections
]

def find_section_headers(text: str) -> List[Tuple[int, str, int]]:
    """Find section headers in source text.

    Returns list of (line_number, header_text, char_position).
    """
    import re
    headers = []
    lines = text.split('\n')
    char_pos = 0

    for i, line in enumerate(lines):
        line_stripped = line.strip()
        for pattern in SECTION_PATTERNS:
            if re.match(pattern, line_stripped):
                headers.append((i, line_stripped, char_pos))
                break
        char_pos += len(line) + 1  # +1 for newline

    return headers


def split_into_chunks(text: str, max_chars: int = 15000) -> List[Tuple[str, str]]:
    """Split source text into chunks based on section headers.

    Returns list of (section_name, section_text) tuples.
    Each chunk is at most max_chars to keep output within token limits.
    """
    headers = find_section_headers(text)
    lines = text.split('\n')

    # If no headers found or small file, return as single chunk
    if len(headers) < 2 or len(text) < max_chars:
        return [("Full Document", text)]

    chunks = []

    # Add intro section (everything before first department header)
    first_header_line = headers[0][0]
    if first_header_line > 10:  # Significant intro content
        intro_text = '\n'.join(lines[:first_header_line])
        if len(intro_text.strip()) > 100:
            chunks.append(("Introduction", intro_text))

    # Group sections into chunks that don't exceed max_chars
    current_chunk_name = None
    current_chunk_lines = []
    current_chunk_size = 0

    for i, (line_num, header, _) in enumerate(headers):
        # Determine end of this section
        if i + 1 < len(headers):
            end_line = headers[i + 1][0]
        else:
            end_line = len(lines)

        section_lines = lines[line_num:end_line]
        section_text = '\n'.join(section_lines)
        section_size = len(section_text)

        # If adding this section would exceed limit, save current chunk and start new one
        if current_chunk_size + section_size > max_chars and current_chunk_lines:
            chunks.append((current_chunk_name, '\n'.join(current_chunk_lines)))
            current_chunk_name = header
            current_chunk_lines = section_lines
            current_chunk_size = section_size
        else:
            # Add to current chunk
            if current_chunk_name is None:
                current_chunk_name = header
            current_chunk_lines.extend(section_lines)
            current_chunk_size += section_size

    # Don't forget the last chunk
    if current_chunk_lines:
        chunks.append((current_chunk_name, '\n'.join(current_chunk_lines)))

    return chunks


# =============================================================================
# CODE GENERATION PROMPT
# =============================================================================

def build_prompt(source_text: str, year: int, guide_text: str,
                 previous_year_summary: Optional[str] = None,
                 section_name: Optional[str] = None) -> str:
    """Build the extraction prompt for Gemini."""

    context = ""
    if previous_year_summary:
        context = f"""
## Context from Previous Year
{previous_year_summary}

Use this to understand patterns and help identify continuing officials.
"""

    section_context = ""
    if section_name and section_name != "Full Document":
        section_context = f"""
## CRITICAL INSTRUCTION - EXTRACT ONE SECTION ONLY
The full document is provided below, but you must ONLY extract officials from the "{section_name}" section.

- Find the "{section_name}" section header in the text
- Extract ONLY the officials listed under that section
- STOP when you reach the next section header
- Do NOT extract officials from other sections
- Output should be small - just officials from "{section_name}"
"""

    prompt = f'''You are a code generator extracting personnel records from a British Colonial Office List.
{section_context}

## Task
Generate a Python file containing extracted data from the Gold Coast Colonial Office List for {year}.

{context}

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
Gold Coast Colonial Office List {year} - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = {year}

OFFICIALS = [
    {{"name": "F. M. Hodgson", "canonical_name": "Hodgson, F. M.", "given_names": "F. M.", "surname": "Hodgson",
     "position": "Governor", "department": "Civil Establishment - Gold Coast", "salary_min": 3000, "salary_max": 3000,
     "honors": ["C.M.G."], "military_rank": "Colonel"}},
    {{"name": "J. Smith", "canonical_name": "Smith, J.", "given_names": "J.", "surname": "Smith",
     "position": "Clerk", "department": "Treasury - Gold Coast", "salary_min": 200, "salary_max": 200}},
    {{"name": "Dr. W. Jones", "canonical_name": "Jones, W.", "given_names": "W.", "surname": "Jones",
     "position": "Medical Officer", "department": "Medical Department - Gold Coast", "salary_min": 500, "salary_max": 600,
     "qualifications": ["M.D.", "M.R.C.S."], "location": "Accra"}},
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
9. For 1940s-1950s with explicit salary + "plus duty allowance": extract both separately

### Classification
10. Honors (C.M.G., K.C.M.G., O.B.E., M.B.E., C.I.E., E.D.) go in "honors" list
11. Qualifications (M.D., M.B., M.R.C.S., B.A., LL.B.) go in "qualifications" list
12. Military ranks (Colonel, Lt.-Col., Major, Captain, Brigadier) go in "military_rank" field

### Status
13. ALWAYS capture acting/temporary status: "Acting Administrator" → acting_status="Acting"
    - Look for: Acting, Temporary, Officiating, Relief

### Locations - CRITICAL
14. Extract LOCATIONS from position titles:
    - "District Commissioner, Accra" → position="District Commissioner", location="Accra"
    - "Dispenser, Waterloo" → position="Dispenser", location="Waterloo"
    - "Keeper of Prison, Elmina" → position="Keeper of Prison", location="Elmina"
    - "Sub-Accountant at Sulymah" → position="Sub-Accountant", location="Sulymah"
15. Extract LOCATIONS from section headers (e.g., "Accra Government School:" means following staff have location="Accra")
16. Common locations: Accra, Cape Coast, Elmina, Kumasi/Coomassie, Sekondi, Takoradi, Axim, Tarquah/Tarkwa, Christiansborg, Winneba, Saltpond, Keta, Ada, Tamale, Gambaga, Wa, Koforidua, Ho

### Regions
17. Set region field for regional administration sections:
    - Ashanti section → region="Ashanti"
    - Northern Territories section → region="Northern Territories"
    - Togoland section → region="Togoland"

### Vacancies
18. For pre-1940: Skip vacant positions (lines with "(vacant)" or no name)
19. For 1940s-1950s: If vacancy has salary listed (e.g., "Director—Vacant. £1,400"), create entry with name=None to preserve salary data

### Departments
20. Department names should include regional suffix: " - Gold Coast", " - Ashanti", " - Northern Territories", " - Togoland"

### Multi-person lines
21. Split lines with multiple people (connected by "and" or comma-separated) into separate entries, each with same position/salary

## Source Text to Extract ({year})
{source_text}

Generate the complete Python file now:
'''
    return prompt


# =============================================================================
# GEMINI API
# =============================================================================

def generate_extraction_code(source_text: str, year: int, guide_text: str,
                             previous_summary: Optional[str] = None,
                             section_name: Optional[str] = None) -> str:
    """Use Gemini to generate Python extraction code."""
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

    # Use Gemini 3 Flash Preview
    model = genai.GenerativeModel('gemini-3-flash-preview')

    prompt = build_prompt(source_text, year, guide_text, previous_summary, section_name)

    print(f"  Sending to Gemini ({len(source_text):,} chars source)...")

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.1,  # Low temperature for consistency
            "max_output_tokens": 32000,
        }
    )

    # Extract code from response (remove markdown if present)
    code = response.text
    if code.startswith("```python"):
        code = code[9:]
    if code.startswith("```"):
        code = code[3:]
    if code.endswith("```"):
        code = code[:-3]

    return code.strip()


# =============================================================================
# VALIDATION
# =============================================================================

def validate_generated_code(code_path: Path) -> Tuple[bool, str, int]:
    """Validate generated Python code. Returns (valid, message, official_count)."""

    # Check syntax
    try:
        with open(code_path) as f:
            code = f.read()
        compile(code, code_path, 'exec')
    except SyntaxError as e:
        return False, f"Syntax error: {e}", 0

    # Try to import and check OFFICIALS
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

        # Check structure of first entry
        required_fields = ['name', 'position', 'department']
        first = officials[0]
        for field in required_fields:
            if field not in first:
                return False, f"Missing required field: {field}", 0

        return True, f"Valid: {len(officials)} officials", len(officials)

    except Exception as e:
        return False, f"Import error: {e}", 0


def run_extraction(code_path: Path, json_path: Path) -> bool:
    """Run the generated code to produce JSON output."""
    try:
        result = subprocess.run(
            [sys.executable, str(code_path)],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            print(f"  ERROR running code: {result.stderr}")
            return False

        # Validate JSON output
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            print(f"  ERROR: Invalid JSON output: {e}")
            return False

        # Save JSON
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=2)

        return True

    except subprocess.TimeoutExpired:
        print("  ERROR: Execution timed out")
        return False
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


# =============================================================================
# SUMMARY GENERATION
# =============================================================================

def generate_year_summary(json_path: Path) -> str:
    """Generate a brief summary of extracted data for context in next year."""
    try:
        with open(json_path) as f:
            data = json.load(f)

        officials = data.get('officials', [])

        # Get department counts
        dept_counts = {}
        for off in officials:
            dept = off.get('department', 'Unknown')
            dept_counts[dept] = dept_counts.get(dept, 0) + 1

        # Get top positions
        top_positions = []
        for off in officials[:10]:
            name = off.get('name', 'Unknown')
            pos = off.get('position', 'Unknown')
            top_positions.append(f"- {name}: {pos}")

        summary = f"""Year {data.get('year')}: {len(officials)} officials extracted

Top officials:
{chr(10).join(top_positions)}

Departments: {', '.join(sorted(dept_counts.keys())[:10])}
"""
        return summary

    except Exception as e:
        return f"Error generating summary: {e}"


# =============================================================================
# MAIN PROCESSING
# =============================================================================

def process_year(year: int, source_path: Path, guide_text: str,
                 previous_summary: Optional[str] = None,
                 force: bool = False) -> Dict:
    """Process a single year. Returns result dict."""

    print(f"\n{'='*60}")
    print(f"Processing {year}: {source_path.name}")
    print(f"{'='*60}")

    code_path = GENERATED_DIR / f"gold_coast_{year}_extraction.py"
    json_path = JSON_DIR / f"gold_coast_{year}.json"

    result = {
        "year": year,
        "source_file": str(source_path),
        "code_file": str(code_path),
        "json_file": str(json_path),
        "status": "pending",
        "official_count": 0,
        "errors": [],
        "timestamp": datetime.now().isoformat()
    }

    # Check if already processed
    if json_path.exists() and not force:
        print(f"  Already processed (use --force to reprocess)")
        result["status"] = "skipped"
        # Try to get official count
        try:
            with open(json_path) as f:
                data = json.load(f)
                result["official_count"] = len(data.get("officials", []))
        except:
            pass
        return result

    # Read source
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            source_text = f.read()
    except Exception as e:
        result["status"] = "error"
        result["errors"].append(f"Failed to read source: {e}")
        return result

    print(f"  Source: {len(source_text):,} characters, {source_text.count(chr(10)):,} lines")

    # Threshold for section-by-section extraction (based on expected output size)
    LARGE_FILE_THRESHOLD = 40000  # Files larger than this need section-by-section extraction
    all_officials = []

    if len(source_text) > LARGE_FILE_THRESHOLD:
        # Large file - extract section by section (full text sent each time, but limited output)
        sections = find_section_headers(source_text)
        section_names = [name for _, name, _ in sections]

        if not section_names:
            section_names = ["Full Document"]

        print(f"  Large file - extracting {len(section_names)} sections separately")

        import time
        for i, section_name in enumerate(section_names):
            print(f"  Section {i+1}/{len(section_names)}: {section_name}")

            # Small delay between API calls to avoid rate limiting
            if i > 0:
                time.sleep(2)

            try:
                # Send FULL text but ask to extract only this section
                code = generate_extraction_code(source_text, year, guide_text, previous_summary, section_name)

                # Save section code
                safe_name = section_name.replace(" ", "_").replace(".", "").replace("'", "")[:30]
                section_code_path = GENERATED_DIR / f"gold_coast_{year}_{safe_name}_extraction.py"
                with open(section_code_path, 'w') as f:
                    f.write(code)

                # Validate and extract officials from this section
                valid, message, count = validate_generated_code(section_code_path)
                if valid:
                    # Import and get officials from section
                    import importlib.util
                    spec = importlib.util.spec_from_file_location("extraction", section_code_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    all_officials.extend(module.OFFICIALS)
                    print(f"    -> {count} officials extracted")
                else:
                    print(f"    -> Section failed: {message}")
                    result["errors"].append(f"Section '{section_name}': {message}")

            except Exception as e:
                print(f"    -> Section error: {e}")
                result["errors"].append(f"Section '{section_name}' error: {e}")

        # Create merged code file
        if all_officials:
            merged_code = f'''"""
Gold Coast Colonial Office List {year} - Extracted Data (Merged from {len(section_names)} sections)
"""
COLONY = "Gold Coast"
YEAR = {year}

OFFICIALS = {repr(all_officials)}

def get_extraction():
    return {{"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
'''
            with open(code_path, 'w') as f:
                f.write(merged_code)
            print(f"  Merged: {code_path.name} ({len(all_officials)} total officials)")

    else:
        # Small file - process entire document at once
        try:
            code = generate_extraction_code(source_text, year, guide_text, previous_summary)

            # Save code
            with open(code_path, 'w') as f:
                f.write(code)
            print(f"  Generated: {code_path.name}")

        except Exception as e:
            result["status"] = "error"
            result["errors"].append(f"Code generation failed: {e}")
            return result

    # Validate final code
    valid, message, count = validate_generated_code(code_path)
    print(f"  Validation: {message}")

    if not valid:
        result["status"] = "invalid"
        result["errors"].append(message)
        return result

    result["official_count"] = count

    # Run extraction
    if run_extraction(code_path, json_path):
        print(f"  JSON saved: {json_path.name}")
        result["status"] = "success"
    else:
        result["status"] = "run_error"
        result["errors"].append("Failed to run extraction code")

    return result


def main():
    parser = argparse.ArgumentParser(description="Batch extract Gold Coast Colonial Office Lists")
    parser.add_argument("--start", type=int, help="Start year")
    parser.add_argument("--end", type=int, help="End year")
    parser.add_argument("--year", type=int, help="Single year to process")
    parser.add_argument("--test", action="store_true", help="Test run (1867, 1899, 1923)")
    parser.add_argument("--force", action="store_true", help="Force reprocessing")
    parser.add_argument("--list", action="store_true", help="List available years")
    args = parser.parse_args()

    # Find all source files
    files = find_gold_coast_files()
    years = sorted(files.keys())

    print(f"Found {len(files)} Gold Coast files: {min(years)}-{max(years)}")

    if args.list:
        for year in years:
            print(f"  {year}: {files[year].name}")
        return

    # Load guide
    if GUIDE_PATH.exists():
        with open(GUIDE_PATH) as f:
            guide_text = f.read()
    else:
        print(f"WARNING: Guide not found at {GUIDE_PATH}")
        guide_text = "Extract all officials with their positions and salaries."

    # Determine which years to process
    if args.test:
        process_years = [1867, 1899, 1923]
    elif args.year:
        process_years = [args.year]
    else:
        start = args.start or min(years)
        end = args.end or max(years)
        process_years = [y for y in years if start <= y <= end]

    # Filter to available years
    process_years = [y for y in process_years if y in files]

    print(f"\nProcessing {len(process_years)} years: {process_years[0]}-{process_years[-1]}")
    print(f"Output directories:")
    print(f"  Generated code: {GENERATED_DIR}")
    print(f"  JSON output: {JSON_DIR}")
    print(f"  Logs: {LOG_DIR}")

    # Process each year
    results = []
    previous_summary = None

    for year in process_years:
        result = process_year(
            year,
            files[year],
            guide_text,
            previous_summary,
            args.force
        )
        results.append(result)

        # Generate summary for next year (if successful)
        if result["status"] == "success":
            json_path = Path(result["json_file"])
            previous_summary = generate_year_summary(json_path)

    # Save log
    log_file = LOG_DIR / f"extraction_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(log_file, 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "years_processed": len(process_years),
            "results": results
        }, f, indent=2)

    # Print summary
    print(f"\n{'='*60}")
    print("EXTRACTION SUMMARY")
    print(f"{'='*60}")

    success = sum(1 for r in results if r["status"] == "success")
    skipped = sum(1 for r in results if r["status"] == "skipped")
    errors = sum(1 for r in results if r["status"] in ("error", "invalid", "run_error"))
    total_officials = sum(r["official_count"] for r in results)

    print(f"Total years: {len(results)}")
    print(f"  Success: {success}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors: {errors}")
    print(f"Total officials extracted: {total_officials:,}")
    print(f"\nLog saved: {log_file}")

    # Show errors
    if errors > 0:
        print(f"\nErrors:")
        for r in results:
            if r["errors"]:
                print(f"  {r['year']}: {'; '.join(r['errors'])}")


if __name__ == "__main__":
    main()
