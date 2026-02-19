"""
Colonial Office List Extraction via Local Ollama Models
========================================================

Adapted from extraction_codegen.py to use local Ollama models instead of
Gemini. Uses the same code-generation approach: LLM generates Python code
containing structured personnel data as a list of dictionaries.

Supports all Ollama models via --model flag. Calls the Ollama REST API
at localhost:11434.

Usage:
    python extraction_ollama.py test_data/sierra_leone_1896_test.txt
    python extraction_ollama.py --model gpt-oss:120b test_data/sierra_leone_1896_test.txt
    python extraction_ollama.py --model qwen3-coder-next:q4_K_M --json-mode test_data/sierra_leone_1896_test.txt

Output:
    generated/sierra_leone_1896_extraction_<model>.py  (reviewable code)
    generated/sierra_leone_1896_data_<model>.json      (final output after running)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
import requests
from pathlib import Path
from datetime import datetime


# =============================================================================
# OLLAMA API
# =============================================================================

OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")


class OllamaError(Exception):
    """Raised when Ollama API call fails (connection, timeout, etc.)."""
    pass


def ollama_generate(model: str, prompt: str, timeout: int = 600,
                    json_mode: bool = False, num_predict: int = 16384) -> str:
    """Call Ollama REST API to generate a response.

    Args:
        model: Ollama model name (e.g. 'gpt-oss:120b')
        prompt: The full prompt to send
        timeout: Request timeout in seconds (default 10 minutes for large models)
        json_mode: If True, request JSON output format
        num_predict: Max tokens to generate (default 16384)

    Returns:
        The generated text response

    Raises:
        OllamaError: On connection failure or timeout (does NOT sys.exit,
                     so callers can catch and continue in batch mode).
    """
    url = f"{OLLAMA_BASE_URL}/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": num_predict,
            "temperature": 0.1,
        },
    }

    if json_mode:
        payload["format"] = "json"

    print(f"Sending request to Ollama ({model}, max {num_predict} tokens)...")
    start = time.time()

    # Use streaming mode with a total wall-clock timeout.
    # Non-streaming mode's timeout only bounds time between response bytes,
    # which doesn't work when Ollama holds the connection during generation.
    payload["stream"] = True

    try:
        response = requests.post(url, json=payload, timeout=(10, 30), stream=True)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise OllamaError(
            f"Cannot connect to Ollama at {OLLAMA_BASE_URL}. "
            "Is Ollama running? Try: ollama serve"
        )
    except requests.exceptions.Timeout:
        raise OllamaError(f"Connection timed out")

    # Read streaming response with wall-clock timeout
    text_parts = []
    total_tokens = 0
    try:
        for line in response.iter_lines():
            if time.time() - start > timeout:
                response.close()
                raise OllamaError(f"Generation exceeded {timeout}s wall-clock timeout")
            if line:
                chunk = json.loads(line)
                text_parts.append(chunk.get("response", ""))
                if chunk.get("done"):
                    total_tokens = chunk.get("eval_count", 0)
                    break
    except requests.exceptions.ChunkedEncodingError:
        raise OllamaError("Connection lost during streaming")

    elapsed = time.time() - start
    text = "".join(text_parts)
    tok_per_sec = total_tokens / elapsed if elapsed > 0 else 0

    print(f"Generated in {elapsed:.1f}s ({total_tokens} tokens, {tok_per_sec:.1f} tok/s)")

    return text


# =============================================================================
# CODE GENERATION PROMPT (same rules as Gemini pipeline)
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
{colony} Colonial Office List {year} - Extracted Data
Generated: {timestamp}
Source: {source_file}

This file contains extracted personnel data. Review before running.
To regenerate JSON: python {output_filename}
"""

COLONY = "{colony}"
YEAR = {year}

# Extracted officials - REVIEW THIS DATA FOR ACCURACY
OFFICIALS = [
    {{
        "name": "F. Cardew",
        "canonical_name": "Cardew, F.",
        "given_names": "F.",
        "surname": "Cardew",
        "position": "Governor, Commander-in-Chief; and Vice-Admiral",
        "department": "Civil Establishment",
        "salary_min": 2000,
        "salary_max": 2000,
        "allowances": "500l. allowances",
        "honors": ["C.M.G."],
        "qualifications": [],
        "military_rank": "Colonel",
        "salary_scale": None,
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
2. "ditto" = same position type as line above (2nd ditto after Chief Clerk = 2nd Clerk; "Assistant ditto" after Colonial Surgeon = Assistant Colonial Surgeon)
3. Salaries: "300l. to 400l." → salary_min=300, salary_max=400
4. Expand ONLY known abbreviations: Wm.=William, Chas.=Charles, Thos.=Thomas
5. Do NOT expand single initials: C. stays C., G. stays G.
6. Honors (C.M.G., K.C.M.G., G.C.M.G., K.C.B., C.B., D.S.O.) go in "honors" list
7. Qualifications (B.A., M.A., M.D., M.B., L.R.C.P., M.R.C.S., F.R.C.S., L.R.C.S., F.R.C.P., LL.D., Ph.D.) go in "qualifications" list
8. Military ranks (Colonel, Lt.-Col., Major, Captain) go in "military_rank" field
9. Extract location if mentioned (e.g., "Dispenser, Waterloo" → location="Waterloo")
10. Skip vacant positions (lines with salary but no name)
11. Department names should match the section header (e.g., "Civil Establishment", "Colonial Secretary's Department")
12. If salary is a named scale (e.g. "Scale A", "Scale B", "Scale N"), record the scale name in "salary_scale" field and set salary_min/salary_max to null. If salary is a numeric value, set salary_scale to null.
13. Currency may be "l." (pounds) or "£". Both mean pounds sterling.
14. Em-dashes (—) separate name from position in late-era entries (e.g., "Colonial Secretary—R. O. Ramage, C.M.G. £1,650.")

## Source Text to Extract
{source_text}

Generate the complete Python file now:
'''


JSON_PROMPT = '''You are a data extraction engine. Given a Colonial Office List excerpt, extract all officials into a JSON array.

## Output Format
Return ONLY valid JSON. No markdown, no explanation.

Return a JSON object with this structure:
{{
  "colony": "{colony}",
  "year": {year},
  "officials": [
    {{
      "name": "F. Cardew",
      "canonical_name": "Cardew, F.",
      "given_names": "F.",
      "surname": "Cardew",
      "position": "Governor, Commander-in-Chief; and Vice-Admiral",
      "department": "Civil Establishment",
      "salary_min": 2000,
      "salary_max": 2000,
      "allowances": "500l. allowances",
      "honors": ["C.M.G."],
      "qualifications": [],
      "military_rank": "Colonel",
      "salary_scale": null,
      "location": null
    }}
  ]
}}

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
11. Department names should match the section header
12. If salary is a named scale (e.g. "Scale A", "Scale B"), record in "salary_scale" and set salary_min/salary_max to null
13. Currency may be "l." (pounds) or "£". Both mean pounds sterling.
14. Em-dashes (—) separate name from position in late-era entries

## Source Text to Extract
{source_text}

Return the JSON now:
'''


# =============================================================================
# EXTRACTION
# =============================================================================

def extract_codegen(source_text: str, model: str, colony: str, year: int,
                    source_file: str, timeout: int = 600) -> str:
    """Generate Python extraction code using an Ollama model."""
    timestamp = datetime.now().isoformat()
    output_filename = f"{colony.lower().replace(' ', '_')}_{year}_extraction.py"

    prompt = CODEGEN_PROMPT.format(
        source_text=source_text,
        timestamp=timestamp,
        source_file=source_file,
        output_filename=output_filename,
        colony=colony,
        year=year,
    )

    code = ollama_generate(model, prompt, timeout=timeout)

    # Strip markdown fences if present
    if code.startswith("```python"):
        code = code[len("```python"):]
    if code.startswith("```"):
        code = code[3:]
    if code.endswith("```"):
        code = code[:-3]

    return code.strip()


def extract_json_mode(source_text: str, model: str, colony: str, year: int,
                      timeout: int = 600) -> dict:
    """Extract directly to JSON using Ollama's JSON mode."""
    prompt = JSON_PROMPT.format(
        source_text=source_text,
        colony=colony,
        year=year,
    )

    text = ollama_generate(model, prompt, timeout=timeout, json_mode=True)

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"ERROR: Model returned invalid JSON: {e}")
        print(f"Raw output (first 500 chars): {text[:500]}")
        return None


# =============================================================================
# CHUNKING
# =============================================================================

# Department header patterns that mark section boundaries.
# Matches explicit department names across all eras (early/middle/transitional/late).
DEPT_HEADER_NAMES = [
    # Core departments (all eras)
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
    # Early era (1879, 1880, 1883)
    r'Secretariat and Treasury',
    r'Aborigines Branch',
    r'Harbour Master and Boat Establishment',
    r'Police and Gaols',
    r'Rural Districts',
    r'British Sherbro',
    r'Isles de Los',
    # Middle era (1894, 1896, 1899)
    r'Department for Native Affairs',
    r'Port and Marine Department',
    r'Colonial Steamer',
    r'Savings Bank',
    r'Registrar of Births.+',
    # Transitional era (1909, 1911, 1921, 1923)
    r'Governor.s Office',
    r'Provincial Administration',
    r'Civil Police',
    r'Agricultural (?:Development )?Branch',
    r'Preventive Service',
    r'Sierra Leone Battalion.+',
    # Late era (1946, 1948, 1950, 1951, 1953, 1958, 1960)
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
    # Cross-colony departments (seen across multiple colonies)
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
    # Generic fallback for any "Foo Department/Office/Establishment/Board/Court/
    # Brigade/Commission/Service/Branch/Administration"
    r'[A-Z][A-Za-z\s\-\']+(?:Department|Office|Establishment|Board|Court|Brigade|Commission|Service|Branch|Administration)',
]

DEPT_HEADERS = re.compile(
    r'^(?:' + '|'.join(DEPT_HEADER_NAMES) + r')[\s.]*$',
    re.MULTILINE | re.IGNORECASE
)


def _strip_markdown(text: str) -> str:
    """Remove markdown formatting (headers, bold) from a line."""
    # Strip markdown header prefixes: ### , #### , etc.
    text = re.sub(r'^#{1,6}\s+', '', text)
    # Strip bold markers: **text** or __text__
    text = text.replace('**', '').replace('__', '')
    return text.strip()


def chunk_by_department(source_text: str) -> list[tuple[str, str]]:
    """Split source text into (department_name, section_text) chunks.

    Each chunk contains a department header and all the lines beneath it
    until the next department header. Handles markdown headers (###),
    bold (**), and UPPERCASE headers across all eras.
    """
    lines = source_text.split('\n')
    chunks = []
    current_dept = None
    current_lines = []

    for line in lines:
        # Strip markdown/bold formatting for matching
        clean = _strip_markdown(line).rstrip('.')
        # Check if this line looks like a department header
        if (clean and
            not re.search(r'\d+l\.|£\d', line) and  # no salary = not a data line
            not re.search(r'—.*[,.]', line) and  # not a "Name—Position" data line
            len(clean) < 80 and
            DEPT_HEADERS.match(clean + '.')):

            # Save previous chunk
            if current_dept and current_lines:
                text = '\n'.join(current_lines)
                if text.strip():
                    chunks.append((current_dept, text))

            current_dept = clean
            current_lines = [line]
        else:
            current_lines.append(line)

    # Save final chunk
    if current_dept and current_lines:
        text = '\n'.join(current_lines)
        if text.strip():
            chunks.append((current_dept, text))

    # If no departments detected, check if the file is large enough to need splitting
    if not chunks:
        non_empty = [l for l in lines if l.strip()]
        if len(non_empty) > 100:
            # Large headerless file — split into ~50-line chunks with 5-line overlap
            # to stay within gpt-oss:120b's 8K output token limit
            print(f"  No department headers found in {len(non_empty)} non-empty lines — "
                  f"using line-count fallback")
            chunk_size = 50
            overlap = 5
            chunk_num = 0
            i = 0
            while i < len(lines):
                end = min(i + chunk_size, len(lines))
                chunk_text = '\n'.join(lines[i:end])
                if chunk_text.strip():
                    chunk_num += 1
                    chunks.append((f"Section {chunk_num}", chunk_text))
                # Advance by chunk_size - overlap, but at least 1
                i += max(1, chunk_size - overlap)
        else:
            chunks = [("Full Document", source_text)]

    return chunks


def extract_chunked(source_text: str, model: str, colony: str, year: int,
                    source_file: str, timeout: int = 600,
                    json_mode: bool = False) -> list[dict]:
    """Extract by chunking source text into department sections.

    Each department section is sent separately to the model, keeping output
    within token limits. Results are merged into a single officials list.

    Chunks that fail (timeout, OllamaError, bad code) are skipped with a
    warning rather than crashing the entire pipeline.
    """
    chunks = chunk_by_department(source_text)
    print(f"Split into {len(chunks)} department chunks:")
    for dept, text in chunks:
        line_count = len([l for l in text.split('\n') if l.strip()])
        print(f"  {dept} ({line_count} lines)")

    all_officials = []
    failed_chunks = []

    for i, (dept, chunk_text) in enumerate(chunks):
        print(f"\n--- Chunk {i+1}/{len(chunks)}: {dept} ---")

        # Scale num_predict by chunk size: ~200 tokens per official,
        # estimate ~1 official per 2 source lines, with generous buffer
        source_lines = len([l for l in chunk_text.split('\n') if l.strip()])
        num_predict = min(16384, max(2048, source_lines * 300))

        try:
            if json_mode:
                data = extract_json_mode(chunk_text, model, colony, year, timeout=timeout)
                if data and "officials" in data:
                    officials = data["officials"]
                else:
                    print(f"  WARNING: Failed to extract chunk '{dept}'")
                    failed_chunks.append(dept)
                    continue
            else:
                code = extract_codegen(
                    chunk_text, model, colony, year, source_file, timeout=timeout
                )
                # Save chunk code
                model_slug = model.replace(":", "_").replace("/", "_")
                chunk_file = (Path(source_file).parent.parent / "generated" /
                             f"chunk_{i}_{dept.lower().replace(' ', '_')}_{model_slug}.py")
                chunk_file.parent.mkdir(exist_ok=True)
                with open(chunk_file, 'w') as f:
                    f.write(code)

                data = run_generated_code(chunk_file)
                if data and "officials" in data:
                    officials = data["officials"]
                else:
                    print(f"  WARNING: Chunk '{dept}' code failed, trying to parse OFFICIALS directly...")
                    try:
                        namespace = {}
                        exec(code, namespace)
                        officials = namespace.get("OFFICIALS", [])
                    except Exception as e:
                        print(f"  ERROR: Could not parse chunk: {e}")
                        failed_chunks.append(dept)
                        continue

        except OllamaError as e:
            print(f"  ERROR: Ollama failed on chunk '{dept}': {e}")
            print(f"  Skipping chunk and continuing...")
            failed_chunks.append(dept)
            continue

        named = [o for o in officials if o.get("name")]
        print(f"  Extracted {len(named)} officials")
        all_officials.extend(named)

    if failed_chunks:
        print(f"\nWARNING: {len(failed_chunks)} chunk(s) failed: {', '.join(failed_chunks)}")

    return all_officials


def run_generated_code(code_file: Path) -> dict | None:
    """Run the generated Python file and capture its JSON output."""
    try:
        result = subprocess.run(
            [sys.executable, str(code_file)],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            print(f"ERROR running generated code: {result.stderr}")
            return None
        return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        print("ERROR: Generated code timed out")
        return None
    except json.JSONDecodeError as e:
        print(f"ERROR: Generated code output is not valid JSON: {e}")
        return None


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Extract Colonial Office List data using local Ollama models"
    )
    parser.add_argument("input_file", nargs="?",
                        default="test_data/sierra_leone_1896_test.txt",
                        help="Input text file to extract from")
    parser.add_argument("--model", default="gpt-oss:120b",
                        help="Ollama model name (default: gpt-oss:120b)")
    parser.add_argument("--colony", default="Sierra Leone",
                        help="Colony name (default: Sierra Leone)")
    parser.add_argument("--year", type=int, default=1896,
                        help="Year (default: 1896)")
    parser.add_argument("--json-mode", action="store_true",
                        help="Use direct JSON extraction instead of code generation")
    parser.add_argument("--timeout", type=int, default=600,
                        help="API timeout in seconds (default: 600)")
    parser.add_argument("--chunked", action="store_true",
                        help="Split input by department and extract each chunk separately")
    parser.add_argument("--output-dir", default="generated",
                        help="Output directory (default: generated)")

    args = parser.parse_args()

    # Resolve paths relative to script location
    script_dir = Path(__file__).parent
    input_file = Path(args.input_file)
    if not input_file.is_absolute():
        input_file = script_dir / input_file
    output_dir = script_dir / args.output_dir

    # Sanitize model name for filenames
    model_slug = args.model.replace(":", "_").replace("/", "_")

    print("=" * 60)
    print("COLONIAL OFFICE LIST - OLLAMA EXTRACTION")
    print("=" * 60)
    print(f"Input:  {input_file}")
    print(f"Model:  {args.model}")
    print(f"Colony: {args.colony}, Year: {args.year}")
    mode_str = "Chunked " if args.chunked else ""
    mode_str += "JSON" if args.json_mode else "Code Generation"
    print(f"Mode:   {mode_str}")
    print()

    # Read source text
    with open(input_file, 'r') as f:
        source_text = f.read()

    output_dir.mkdir(exist_ok=True)

    if args.chunked:
        # Chunked extraction — split by department, extract each separately
        print("Using chunked extraction (one department at a time)...")
        all_officials = extract_chunked(
            source_text, args.model, args.colony, args.year,
            str(input_file), timeout=args.timeout,
            json_mode=args.json_mode
        )

        data = {
            "colony": args.colony,
            "year": args.year,
            "generated": datetime.now().isoformat(),
            "total_officials": len(all_officials),
            "officials": all_officials,
        }

        json_file = output_dir / f"{args.colony.lower().replace(' ', '_')}_{args.year}_data_{model_slug}_chunked.json"
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\nSaved merged JSON to: {json_file}")
        print(f"Total extracted: {len(all_officials)} officials")
        print("\nDone!")
        return

    if args.json_mode:
        # Direct JSON extraction
        print("Extracting directly to JSON...")
        data = extract_json_mode(
            source_text, args.model, args.colony, args.year,
            timeout=args.timeout
        )
        if data is None:
            print("Extraction failed.")
            sys.exit(1)

        json_file = output_dir / f"{args.colony.lower().replace(' ', '_')}_{args.year}_data_{model_slug}.json"
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\nSaved JSON to: {json_file}")

        n = len(data.get("officials", []))
        print(f"Extracted {n} officials")

    else:
        # Code generation approach
        print("Generating extraction code...")
        code = extract_codegen(
            source_text, args.model, args.colony, args.year,
            str(input_file), timeout=args.timeout
        )

        code_file = output_dir / f"{args.colony.lower().replace(' ', '_')}_{args.year}_extraction_{model_slug}.py"
        with open(code_file, 'w') as f:
            f.write(code)
        print(f"\nSaved code to: {code_file}")

        # Preview
        lines = code.split('\n')
        print(f"\nCode preview (first 30 lines of {len(lines)} total):")
        print("-" * 40)
        for i, line in enumerate(lines[:30]):
            print(f"{i+1:3}: {line}")
        if len(lines) > 30:
            print(f"... ({len(lines)} total lines)")

        # Try running the generated code
        print(f"\nRunning generated code...")
        data = run_generated_code(code_file)

        if data:
            json_file = output_dir / f"{args.colony.lower().replace(' ', '_')}_{args.year}_data_{model_slug}.json"
            with open(json_file, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"Saved JSON to: {json_file}")

            n = len(data.get("officials", []))
            print(f"Extracted {n} officials")
        else:
            print("Generated code did not produce valid output.")
            print(f"Review and fix: {code_file}")

    print("\nDone!")


if __name__ == "__main__":
    main()
