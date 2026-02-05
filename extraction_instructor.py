"""
Colonial Office List Extraction with Instructor + Pydantic
==========================================================

Schema-validated LLM extraction using Instructor library.
Uses Claude API (Anthropic) with automatic validation and retry.

Features:
- Pydantic schema for structured extraction
- Department chunking for context management
- Automatic retry on validation failure
- Token usage tracking for cost comparison
- JSON/CSV output aggregation

Requirements:
    pip install instructor anthropic pydantic

Usage:
    export ANTHROPIC_API_KEY="..."
    python extraction_instructor.py test_data/sierra_leone_1896_test.txt

Output:
    test_data/instructor_extraction_results.json
"""

import os
import json
import sys
import time
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field
from dataclasses import dataclass


# =============================================================================
# PYDANTIC SCHEMAS
# =============================================================================

class OfficialRecord(BaseModel):
    """Schema for a single official's record."""
    name: str = Field(description="Full name as written in source (e.g., 'J. O. Gore')")
    canonical_name: str = Field(description="Standardized name format: 'Surname, Given Names' (e.g., 'Gore, J. O.')")
    given_names: str = Field(description="First names and initials (e.g., 'J. O.')")
    surname: str = Field(description="Family name (e.g., 'Gore')")
    position: str = Field(description="Position/title held (e.g., 'Colonial Secretary')")
    department: str = Field(description="Department name (e.g., 'Colonial Secretary's Department')")
    salary_min: Optional[int] = Field(default=None, description="Minimum salary in pounds (integer). For '300l. to 400l.', this is 300.")
    salary_max: Optional[int] = Field(default=None, description="Maximum salary in pounds. For '300l. to 400l.', this is 400. For fixed salary '200l.', same as min.")
    allowances: Optional[str] = Field(default=None, description="Any allowances mentioned (e.g., 'quarters', '91l. 5s. travelling allowance')")
    honors: list[str] = Field(default_factory=list, description="Honors like C.M.G., K.C.M.G., K.C.B. (appear after name)")
    qualifications: list[str] = Field(default_factory=list, description="Professional/academic qualifications like M.D., M.B., B.A., M.R.C.S., L.R.C.P.")
    military_rank: Optional[str] = Field(default=None, description="Military rank if present (e.g., 'Colonel', 'Lt.-Col.', 'Captain')")
    location: Optional[str] = Field(default=None, description="Location/station if mentioned in position (e.g., 'Waterloo', 'Sherbro')")


class DepartmentExtraction(BaseModel):
    """Schema for extraction from a single department section."""
    department: str = Field(description="Name of the department")
    officials: list[OfficialRecord] = Field(description="List of officials in this department")


class ColonyExtraction(BaseModel):
    """Schema for extraction from entire colony file."""
    colony: str = Field(description="Colony name (e.g., 'Sierra Leone')")
    year: int = Field(description="Year of the Colonial Office List")
    total_officials: int = Field(description="Total number of officials extracted")
    departments: list[DepartmentExtraction] = Field(description="Extraction results by department")


# =============================================================================
# CHUNKING
# =============================================================================

def chunk_by_department(text: str) -> list[tuple[str, str]]:
    """
    Split text into chunks by department.
    Returns list of (department_name, department_text) tuples.
    """
    chunks = []
    current_dept = "Unknown"
    current_lines = []

    # Department header patterns
    dept_keywords = [
        "Department", "Office", "Establishment", "Council", "Bank"
    ]

    lines = text.split('\n')

    for line in lines:
        stripped = line.strip()

        # Check if this is a department header
        is_header = False
        if stripped and not any(c.isdigit() for c in stripped[:20]) or 'l.' not in stripped:
            # Might be a header - check for keywords
            if any(kw in stripped for kw in dept_keywords) or stripped.endswith('.'):
                # Clean up
                potential_dept = stripped.rstrip('.').rstrip('-').strip()
                if len(potential_dept) < 60 and 'l.' not in stripped:
                    is_header = True
                    # Save previous chunk
                    if current_lines:
                        chunks.append((current_dept, '\n'.join(current_lines)))
                    current_dept = potential_dept
                    current_lines = []
                    continue

        current_lines.append(line)

    # Don't forget last chunk
    if current_lines:
        chunks.append((current_dept, '\n'.join(current_lines)))

    return chunks


# =============================================================================
# LLM EXTRACTION
# =============================================================================

@dataclass
class TokenUsage:
    """Track token usage for cost estimation."""
    input_tokens: int = 0
    output_tokens: int = 0

    def add(self, input_t: int, output_t: int):
        self.input_tokens += input_t
        self.output_tokens += output_t

    def cost_usd(self, model: str = "claude-sonnet-4-20250514") -> float:
        """Estimate cost in USD."""
        # Anthropic pricing (as of 2024)
        if "haiku" in model.lower():
            input_cost = 0.25 / 1_000_000  # $0.25 per 1M input
            output_cost = 1.25 / 1_000_000  # $1.25 per 1M output
        elif "sonnet" in model.lower():
            input_cost = 3.0 / 1_000_000  # $3 per 1M input
            output_cost = 15.0 / 1_000_000  # $15 per 1M output
        else:  # opus
            input_cost = 15.0 / 1_000_000
            output_cost = 75.0 / 1_000_000

        return (self.input_tokens * input_cost) + (self.output_tokens * output_cost)


def extract_department_with_llm(
    department_name: str,
    department_text: str,
    colony: str,
    year: int,
    client,
    model: str,
    token_usage: TokenUsage
) -> DepartmentExtraction:
    """Extract officials from a single department using LLM."""

    prompt = f"""Extract all officials from this Colonial Office List department section.

Colony: {colony}
Year: {year}
Department: {department_name}

INSTRUCTIONS:
1. Extract EVERY person mentioned, even if they share a line with others
2. Handle "ditto" - it means same position type as the line above
3. Parse salaries: "300l. to 400l." means min=300, max=400; "200l." means min=max=200
4. Honors (C.M.G., K.C.M.G., etc.) appear AFTER the name
5. Qualifications (M.D., M.B., M.R.C.S., B.A.) are professional credentials
6. Military ranks (Colonel, Lt.-Col., Captain) appear BEFORE the name
7. Extract location if position mentions a place (e.g., "Dispenser, Waterloo")
8. For lines with multiple people separated by semicolons, extract EACH person
9. Expand name abbreviations: Wm. = William, Chas. = Charles, etc.

IMPORTANT - Handle these special patterns:
- "2nd ditto, E. W. Cole, 100l." means 2nd Clerk (if previous was Chief Clerk)
- "Assistant ditto, Wm. Renner, M.R.C.S., 300l.; M. L. Jarrett, M.R.C.S., 250l." = TWO people
- "Kent, 40l., and quarters" = position with NO NAME (skip this, note as vacant)

TEXT:
{department_text}
"""

    response = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
        response_model=DepartmentExtraction,
    )

    # Track usage
    if hasattr(response, '_raw_response'):
        usage = response._raw_response.usage
        token_usage.add(usage.input_tokens, usage.output_tokens)

    return response


def extract_full_document(
    text: str,
    colony: str = "Sierra Leone",
    year: int = 1896,
    model: str = "claude-sonnet-4-20250514"
) -> tuple[ColonyExtraction, TokenUsage]:
    """Extract all officials from a full document."""

    try:
        import instructor
        import anthropic
    except ImportError:
        print("ERROR: Required packages not installed.")
        print("Run: pip install instructor anthropic")
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("Export your API key: export ANTHROPIC_API_KEY='...'")
        sys.exit(1)

    # Initialize client with instructor
    client = instructor.from_anthropic(anthropic.Anthropic())
    token_usage = TokenUsage()

    # Chunk by department
    chunks = chunk_by_department(text)
    print(f"Split into {len(chunks)} department chunks")

    all_departments = []
    total_officials = 0

    for dept_name, dept_text in chunks:
        if not dept_text.strip():
            continue

        print(f"  Processing: {dept_name}...")
        try:
            result = extract_department_with_llm(
                dept_name, dept_text, colony, year, client, model, token_usage
            )
            all_departments.append(result)
            total_officials += len(result.officials)
            print(f"    Found {len(result.officials)} officials")
        except Exception as e:
            print(f"    ERROR: {e}")

        # Small delay to avoid rate limiting
        time.sleep(0.5)

    return ColonyExtraction(
        colony=colony,
        year=year,
        total_officials=total_officials,
        departments=all_departments
    ), token_usage


# =============================================================================
# EVALUATION
# =============================================================================

def flatten_extraction(extraction: ColonyExtraction) -> list[dict]:
    """Flatten nested extraction to list of official dicts."""
    officials = []
    for dept in extraction.departments:
        for official in dept.officials:
            d = official.model_dump()
            d['department'] = dept.department
            officials.append(d)
    return officials


def load_gold_standard(filepath: str) -> list[dict]:
    """Load gold standard annotations."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data['officials']


def compare_name(extracted: str, gold: str) -> bool:
    """Compare names with fuzzy matching."""
    e = extracted.lower().replace(',', '').replace('.', '').strip()
    g = gold.lower().replace(',', '').replace('.', '').strip()

    if e == g:
        return True

    e_parts = set(e.split())
    g_parts = set(g.split())

    if len(e_parts & g_parts) >= min(len(e_parts), len(g_parts)) * 0.7:
        return True

    return False


def evaluate_extraction(extracted: list[dict], gold: list[dict]) -> dict:
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

    used_extracted = set()

    for g in gold:
        best_match = None
        best_score = 0

        for i, e in enumerate(extracted):
            if i in used_extracted:
                continue

            if compare_name(e.get('canonical_name', e['name']), g.get('canonical_name', g['name'])):
                score = 1.0
                if best_score < score:
                    best_score = score
                    best_match = i

        if best_match is not None:
            used_extracted.add(best_match)
            results['matched'] += 1
            e = extracted[best_match]

            results['field_accuracy']['name']['total'] += 1
            if compare_name(e.get('canonical_name', e['name']), g.get('canonical_name', g['name'])):
                results['field_accuracy']['name']['correct'] += 1

            results['field_accuracy']['position']['total'] += 1
            if e.get('position') and g.get('position'):
                if e['position'].lower() == g['position'].lower() or e['position'].lower() in g['position'].lower():
                    results['field_accuracy']['position']['correct'] += 1

            results['field_accuracy']['salary_min']['total'] += 1
            if e.get('salary_min') == g.get('salary_min'):
                results['field_accuracy']['salary_min']['correct'] += 1

            results['field_accuracy']['salary_max']['total'] += 1
            if e.get('salary_max') == g.get('salary_max'):
                results['field_accuracy']['salary_max']['correct'] += 1

            if g.get('honors'):
                results['field_accuracy']['honors']['total'] += 1
                if set(e.get('honors', [])) == set(g['honors']):
                    results['field_accuracy']['honors']['correct'] += 1

            if g.get('qualifications'):
                results['field_accuracy']['qualifications']['total'] += 1
                if set(e.get('qualifications', [])) == set(g['qualifications']):
                    results['field_accuracy']['qualifications']['correct'] += 1

            if g.get('location'):
                results['field_accuracy']['location']['total'] += 1
                if e.get('location') and e['location'].lower() == g['location'].lower():
                    results['field_accuracy']['location']['correct'] += 1

            results['matches'].append({
                'gold': g['name'],
                'extracted': e['name'],
                'position_match': e.get('position', '').lower() == g.get('position', '').lower(),
                'salary_match': e.get('salary_min') == g.get('salary_min')
            })
        else:
            results['missed'].append(g['name'])

    for i, e in enumerate(extracted):
        if i not in used_extracted:
            results['extra'].append(e['name'])

    if results['total_extracted'] > 0:
        results['precision'] = results['matched'] / results['total_extracted']
    if results['total_gold'] > 0:
        results['recall'] = results['matched'] / results['total_gold']

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
    input_file = Path(__file__).parent / "test_data" / "sierra_leone_1896_test.txt"
    gold_file = Path(__file__).parent / "test_data" / "gold_standard.json"
    output_file = Path(__file__).parent / "test_data" / "instructor_extraction_results.json"

    # Parse args
    model = "claude-sonnet-4-20250514"
    if len(sys.argv) > 1:
        input_file = Path(sys.argv[1])
    if len(sys.argv) > 2:
        model = sys.argv[2]

    print("=" * 60)
    print("COLONIAL OFFICE LIST - INSTRUCTOR EXTRACTION")
    print("=" * 60)
    print(f"Model: {model}")

    # Read input
    print(f"\nReading: {input_file}")
    with open(input_file, 'r') as f:
        text = f.read()

    # Extract
    print("\nExtracting officials with LLM...")
    start_time = time.time()
    extraction, token_usage = extract_full_document(text, model=model)
    elapsed = time.time() - start_time

    print(f"\nExtracted {extraction.total_officials} officials in {elapsed:.1f}s")
    print(f"Token usage: {token_usage.input_tokens:,} input, {token_usage.output_tokens:,} output")
    print(f"Estimated cost: ${token_usage.cost_usd(model):.4f}")

    # Flatten for evaluation
    officials = flatten_extraction(extraction)

    # Show sample
    print("\nSample extractions:")
    for o in officials[:5]:
        print(f"  {o['position']}: {o['name']}")
        print(f"    Salary: {o['salary_min']}-{o['salary_max']}l., Dept: {o['department']}")

    # Evaluate against gold standard
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
            'method': 'instructor',
            'model': model,
            'total_extracted': extraction.total_officials,
            'token_usage': {
                'input_tokens': token_usage.input_tokens,
                'output_tokens': token_usage.output_tokens,
                'estimated_cost_usd': token_usage.cost_usd(model)
            },
            'extraction_time_seconds': elapsed
        },
        'extraction': extraction.model_dump(),
        'officials_flat': officials,
        'evaluation': results
    }

    print(f"\nSaving results to: {output_file}")
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print("\nDone!")
    return extraction, results


if __name__ == "__main__":
    main()
