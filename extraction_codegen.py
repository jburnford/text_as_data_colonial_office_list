"""
Colonial Office List Extraction via Code Generation
====================================================

This approach uses Gemini to GENERATE Python code containing extracted data,
rather than extracting data directly. Benefits:

1. Reviewable: You can inspect the generated code for hallucinations
2. Deterministic: Once generated, code always produces same output
3. Versionable: Commit generated code to git
4. Fixable: Edit code to correct errors before running

Workflow:
1. Feed source text to Gemini
2. Gemini generates Python file with extracted data as dict/list
3. Human reviews generated code (optional but recommended)
4. Run generated code to produce final JSON

Requirements:
    pip install google-generativeai

Usage:
    export GOOGLE_API_KEY="..."
    python extraction_codegen.py test_data/sierra_leone_1896_test.txt

Output:
    generated/sierra_leone_1896_extraction.py  (reviewable code)
    generated/sierra_leone_1896_data.json      (final output after running)
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Load .env file if present (keeps API key out of git)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not required if env var set directly


# =============================================================================
# CODE GENERATION PROMPT
# =============================================================================

CODEGEN_PROMPT = '''You are a code generator. Given a Colonial Office List excerpt, generate a Python file that contains the extracted data as a Python data structure.

## Task
Generate a Python file that:
1. Defines OFFICIALS as a list of dictionaries
2. Includes a main() function that outputs JSON
3. Is deterministic and self-contained

## Output Format
Generate ONLY valid Python code. No markdown, no explanation, just the .py file contents.

The generated code should look like this structure:

```python
"""
Sierra Leone Colonial Office List 1896 - Extracted Data
Generated: {timestamp}
Source: {source_file}

This file contains extracted personnel data. Review before running.
To regenerate JSON: python {output_filename}
"""

COLONY = "Sierra Leone"
YEAR = 1896

# Extracted officials - REVIEW THIS DATA FOR ACCURACY
OFFICIALS = [
    {{
        "name": "F. Cardew",
        "canonical_name": "Cardew, F.",
        "given_names": "F.",
        "surname": "Cardew",
        "position": "Governor, Commander-in-Chief; and Vice-Admiral",
        "department": "Civil Establishment - Sierra Leone",
        "salary_min": 2000,
        "salary_max": 2000,
        "allowances": "500l. allowances",
        "honors": ["C.M.G."],
        "qualifications": [],
        "military_rank": "Colonel",
        "location": None,
    }},
    # ... more officials ...
]

def get_extraction():
    """Return structured extraction result."""
    return {{
        "colony": COLONY,
        "year": YEAR,
        "generated": "{timestamp}",
        "total_officials": len(OFFICIALS),
        "officials": OFFICIALS,
    }}

def main():
    """Output extraction as JSON."""
    import json
    result = get_extraction()
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
```

## Extraction Rules
1. Extract EVERY person mentioned
2. "ditto" = same position type as line above (2nd ditto after Chief Clerk = 2nd Clerk)
3. Salaries: "300l. to 400l." → salary_min=300, salary_max=400
4. Expand ONLY known abbreviations: Wm.=William, Chas.=Charles, Thos.=Thomas
5. Do NOT expand single initials: C. stays C., G. stays G.
6. Honors (C.M.G., K.C.M.G.) go in "honors" list
7. Qualifications (M.D., M.B., M.R.C.S.) go in "qualifications" list
8. Military ranks (Colonel, Lt.-Col.) go in "military_rank" field
9. Extract location if mentioned (e.g., "Dispenser, Waterloo" → location="Waterloo")
10. Skip vacant positions (lines with salary but no name)
11. Department names should include " - Sierra Leone" suffix

## Source Text to Extract
{source_text}

Generate the complete Python file now:
'''


# =============================================================================
# GEMINI API
# =============================================================================

def generate_extraction_code(source_text: str, colony: str, year: int, source_file: str) -> str:
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

    # Use Gemini 2.0 Flash
    model = genai.GenerativeModel('gemini-2.0-flash')

    timestamp = datetime.now().isoformat()
    output_filename = f"{colony.lower().replace(' ', '_')}_{year}_extraction.py"

    prompt = CODEGEN_PROMPT.format(
        source_text=source_text,
        timestamp=timestamp,
        source_file=source_file,
        output_filename=output_filename,
    )

    print(f"Generating extraction code with Gemini 2.0 Flash...")
    response = model.generate_content(prompt)

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
# MAIN
# =============================================================================

def main():
    # Default test file
    input_file = Path(__file__).parent / "test_data" / "sierra_leone_1896_test.txt"
    output_dir = Path(__file__).parent / "generated"

    if len(sys.argv) > 1:
        input_file = Path(sys.argv[1])

    # Parse colony and year from filename
    colony = "Sierra Leone"
    year = 1896

    print("=" * 60)
    print("COLONIAL OFFICE LIST - CODE GENERATION EXTRACTION")
    print("=" * 60)
    print(f"Input: {input_file}")
    print(f"Colony: {colony}, Year: {year}")

    # Read source
    with open(input_file, 'r') as f:
        source_text = f.read()

    # Generate code
    code = generate_extraction_code(source_text, colony, year, str(input_file))

    # Save generated code
    output_dir.mkdir(exist_ok=True)
    code_file = output_dir / f"{colony.lower().replace(' ', '_')}_{year}_extraction.py"

    print(f"\nSaving generated code to: {code_file}")
    with open(code_file, 'w') as f:
        f.write(code)

    print(f"\n{'=' * 60}")
    print("NEXT STEPS:")
    print("=" * 60)
    print(f"1. REVIEW the generated code: {code_file}")
    print(f"2. Check for hallucinations or errors in OFFICIALS list")
    print(f"3. Run to generate JSON: python {code_file}")
    print(f"4. Or import: from {code_file.stem} import OFFICIALS, get_extraction")

    # Show preview
    print(f"\n{'=' * 60}")
    print("CODE PREVIEW (first 50 lines):")
    print("=" * 60)
    for i, line in enumerate(code.split('\n')[:50]):
        print(f"{i+1:3}: {line}")
    if len(code.split('\n')) > 50:
        print(f"... ({len(code.split(chr(10)))} total lines)")

    return code_file


if __name__ == "__main__":
    main()
