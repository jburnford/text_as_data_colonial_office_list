"""
Colonial Office List Extraction Demo
HIST 496 - Text as Data
=====================================

This script demonstrates extraction challenges and approaches
for semi-structured historical administrative documents.

Requirements:
    pip install pydantic

Optional (for LLM extraction):
    pip install instructor openai
"""

import re
from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, Field

# =============================================================================
# PART 1: THE RAW DATA
# =============================================================================

# Sample staff list from Jamaica Colonial Office List, 1896
SAMPLE_DATA = """
Colonial Secretary's Office.

Colonial Secretary, Fred. Evans, C.M.G., 1,300l.
Assistant Secretary, J. Allwood, 700l.
Chief Clerk, S. P. Musson, 500l.
Clerks, 1st Class, F. S. Sanguinetti, T. L. Roxburgh, and J. B. Lucie Smith, 300l. to 400l.
Clerks, 2nd Class, A. Cork, J. M. Casserly, and G. M. Wortley, 150l. to 300l.
Clerks, 3rd Class, F. L. Pearce, J. F. Osmond, A. C. Finlay, 80l. to 150l.
Permanent Copyist, D. Hall 78l.

Department of Public Works.

Director, Valentine Greame Bell, 1,200l., and actual travelling expenses.
Assistant Director, James Richmond, 800l., and actual travelling expenses.
Ditto, Southern District, J. D'Aeth, 350l. to 450l., and actual travelling expenses.
Engineer, Eastern District, D. A. P. Sanftleben, 350l. to 450l., and actual travelling expenses.
Chief Draughtsman, R. R. Williams, 200l. to 350l.

Audit Office.

Auditor-General, John C. Macglashan, 1,000l.
Chief Clerk, W. G. C. Arrowsmith, 300l. to 400l.
Senior Clerk, G. M. Livingston, 300l. to 400l.
Clerks, 1st Class, W. Duff, H. E. Laidman, and A. A. Samuel, 250l. to 300l.
Clerks, 2nd Class, E. du Mont, A. S. Finzi, G. W. Taylor, J. L. Pietersz, C. C. Kelly, 100l. to 200l.
"""

# More complex example: Sierra Leone with honors and qualifications
COMPLEX_SAMPLE = """
Governor, Commander-in-Chief; and Vice-Admiral, Colonel F. Cardew, C.M.G., 2,000l. and 500l. allowances.

Colonial Secretary's Department.

Colonial Secretary, Lt.-Col. J. O. Gore, 710l. to 800l., and quarters.
Assistant Colonial Secretary, E. Faulkner, 300l. to 350l.
Chief Clerk, J. E. Dawson, 200l.

Medical Department.

Colonial Surgeon, W. T. Prout, M.B., 50l., travelling allowance, 91l. 5s.
Assistant ditto, Wm. Renner, M.R.C.S., 300l. to 350l., and allowance 45l. 12s. 6d.; M. L. Jarrett, M.R.C.S., 250l.; I. N. Paris, M.B., 200l., and allowance 45l. 12s. 6d.
"""

print("=" * 60)
print("COLONIAL OFFICE LIST EXTRACTION DEMO")
print("=" * 60)
print("\n📜 Sample data loaded. Let's explore extraction challenges.\n")


# =============================================================================
# PART 2: NAIVE REGEX EXTRACTION
# =============================================================================

def extract_with_regex(text: str) -> list[dict]:
    """
    Attempt to extract person-position-salary using regex.
    This works for SIMPLE cases but fails on complexity.
    """
    results = []

    # Pattern: Position, Name, optional honors, Salary
    # This is a simplified pattern that handles some common cases
    pattern = r'^([A-Za-z][A-Za-z\s\-,]+?),\s+([A-Z][a-z]*\.?\s+[A-Za-z\'\-]+(?:\s+[A-Za-z\'\-]+)?),?\s*([A-Z\.]+(?:,\s*[A-Z\.]+)*)?,?\s*(\d+l\.|\d+l\.\s+to\s+\d+l\.)'

    for line in text.strip().split('\n'):
        line = line.strip()
        if not line or line.endswith('.') and len(line) < 50:  # Skip headers
            continue

        match = re.match(pattern, line)
        if match:
            results.append({
                'position': match.group(1).strip(),
                'name': match.group(2).strip(),
                'honors': match.group(3).strip() if match.group(3) else None,
                'salary': match.group(4).strip()
            })

    return results


print("\n" + "=" * 60)
print("PART 2: NAIVE REGEX EXTRACTION")
print("=" * 60)

regex_results = extract_with_regex(SAMPLE_DATA)
print(f"\n✓ Extracted {len(regex_results)} records with regex:\n")
for r in regex_results[:5]:
    print(f"  {r['position']}: {r['name']} ({r['salary']})")

if len(regex_results) < 15:
    print(f"\n⚠️  Problem: We should have ~20+ people, only got {len(regex_results)}")
    print("   Regex failed on:")
    print("   - Multiple people on one line ('Clerks, 1st Class, A, B, and C')")
    print("   - 'Ditto' references")
    print("   - Complex salary formats ('300l. to 400l., and travelling')")


# =============================================================================
# PART 3: IMPROVED REGEX (still incomplete)
# =============================================================================

def extract_with_better_regex(text: str) -> list[dict]:
    """
    Improved extraction that handles some edge cases.
    Still not complete - demonstrates the complexity.
    """
    results = []
    current_department = None
    previous_position_type = None

    for line in text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue

        # Detect department headers
        if line.endswith('.') and len(line) < 60 and not re.search(r'\d+l\.', line):
            current_department = line.rstrip('.')
            continue

        # Handle "Ditto" - means same position type as previous
        if line.startswith('Ditto,'):
            line = line.replace('Ditto,', previous_position_type + ',', 1)

        # Try to extract salary first (anchor point)
        salary_match = re.search(r'(\d+l\.(?:\s+to\s+\d+l\.)?)', line)
        if not salary_match:
            continue

        salary = salary_match.group(1)
        before_salary = line[:salary_match.start()].strip().rstrip(',')

        # Split into position and people
        # This is tricky because position can contain commas
        parts = before_salary.split(',')

        if len(parts) >= 2:
            # First part(s) are position, rest are names
            # Heuristic: position words are lowercase or title case
            position_parts = []
            name_parts = []
            found_name = False

            for part in parts:
                part = part.strip()
                # Names typically start with capital initial or title
                if not found_name and (part[0].isupper() and '.' in part[:3] or
                                       part.split()[0] in ['and', 'the']):
                    found_name = True
                if found_name:
                    name_parts.append(part)
                else:
                    position_parts.append(part)

            position = ', '.join(position_parts)
            previous_position_type = position_parts[0] if position_parts else previous_position_type

            # Handle multiple names (split on 'and')
            names_str = ', '.join(name_parts)
            names = re.split(r',\s*and\s*|,\s*', names_str)
            names = [n.strip() for n in names if n.strip() and n.strip() != 'and']

            for name in names:
                # Extract honors (uppercase abbreviations with periods)
                honors_match = re.findall(r'\b([A-Z]\.(?:[A-Z]\.)*[A-Z]?\.?)\b', name)
                clean_name = re.sub(r'\b[A-Z]\.[A-Z\.]+\b', '', name).strip().strip(',')

                results.append({
                    'department': current_department,
                    'position': position,
                    'name': clean_name,
                    'honors': honors_match if honors_match else None,
                    'salary': salary
                })

    return results


print("\n" + "=" * 60)
print("PART 3: IMPROVED REGEX EXTRACTION")
print("=" * 60)

better_results = extract_with_better_regex(SAMPLE_DATA)
print(f"\n✓ Extracted {len(better_results)} records with improved regex:\n")
for r in better_results[:8]:
    honors = ', '.join(r['honors']) if r['honors'] else 'None'
    print(f"  [{r['department']}] {r['position']}: {r['name']} - {r['salary']}")

print(f"\n📊 Improvement: {len(regex_results)} → {len(better_results)} records")
print("   But still missing some edge cases...")


# =============================================================================
# PART 4: PYDANTIC SCHEMA FOR LLM EXTRACTION
# =============================================================================

class OfficialRecord(BaseModel):
    """Schema for a single official's record."""
    name: str = Field(description="Full name of the official")
    position: str = Field(description="Position/title held")
    department: str = Field(description="Department name")
    salary_min: Optional[int] = Field(description="Minimum salary in pounds")
    salary_max: Optional[int] = Field(description="Maximum salary in pounds (if range)")
    allowances: Optional[str] = Field(description="Any allowances mentioned")
    honors: list[str] = Field(default_factory=list, description="Honors like C.M.G., K.C.M.G.")
    qualifications: list[str] = Field(default_factory=list, description="Qualifications like M.D., B.A.")
    military_rank: Optional[str] = Field(description="Military rank if any")
    notes: Optional[str] = Field(description="Any other relevant notes")


class ExtractionResult(BaseModel):
    """Schema for extraction from a Colonial Office List section."""
    colony: str
    year: int
    officials: list[OfficialRecord]


print("\n" + "=" * 60)
print("PART 4: PYDANTIC SCHEMA FOR LLM EXTRACTION")
print("=" * 60)
print("\nSchema defined for structured extraction:")
print(ExtractionResult.model_json_schema())


# =============================================================================
# PART 5: LLM-BASED EXTRACTION (requires API key)
# =============================================================================

def extract_with_llm(text: str, colony: str = "Jamaica", year: int = 1896):
    """
    Extract using LLM with Instructor for schema validation.

    Requires:
        pip install instructor openai
        export OPENAI_API_KEY=your-key-here
    """
    try:
        import instructor
        from openai import OpenAI
    except ImportError:
        print("\n⚠️  LLM extraction requires: pip install instructor openai")
        print("   Also set OPENAI_API_KEY environment variable")
        return None

    import os
    if not os.getenv("OPENAI_API_KEY"):
        print("\n⚠️  Set OPENAI_API_KEY environment variable to use LLM extraction")
        return None

    client = instructor.from_openai(OpenAI())

    prompt = f"""Extract all officials from this Colonial Office List excerpt.

Colony: {colony}
Year: {year}

For each person, extract:
- Full name (expand abbreviations like "Wm." to "William" if confident)
- Position/title
- Department
- Salary (min and max if a range)
- Any allowances mentioned
- Honors (C.M.G., K.C.M.G., etc.)
- Qualifications (M.D., M.B., B.A., etc.)
- Military rank if present

Handle special cases:
- "Ditto" means same position type as the line above
- Multiple names on one line = multiple people with same position
- Salary ranges like "300l. to 400l." = min 300, max 400

TEXT:
{text}
"""

    result = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4" for better accuracy
        response_model=ExtractionResult,
        messages=[{"role": "user", "content": prompt}],
    )

    return result


print("\n" + "=" * 60)
print("PART 5: LLM-BASED EXTRACTION")
print("=" * 60)

# Uncomment to run LLM extraction:
# llm_result = extract_with_llm(SAMPLE_DATA)
# if llm_result:
#     print(f"\n✓ LLM extracted {len(llm_result.officials)} officials:\n")
#     for official in llm_result.officials[:10]:
#         print(f"  {official.position}: {official.name}")
#         print(f"    Salary: £{official.salary_min}-{official.salary_max or official.salary_min}")
#         if official.honors:
#             print(f"    Honors: {', '.join(official.honors)}")
#         print()

print("\n💡 To run LLM extraction:")
print("   1. pip install instructor openai")
print("   2. export OPENAI_API_KEY=your-key")
print("   3. Uncomment the extraction code above")


# =============================================================================
# PART 6: THE ENTITY RESOLUTION CHALLENGE
# =============================================================================

print("\n" + "=" * 60)
print("PART 6: THE ENTITY RESOLUTION CHALLENGE")
print("=" * 60)

# Simulated data showing the same person across years
person_appearances = [
    {"year": 1881, "name": "Samuel Rowe", "position": "Governor", "colony": "Sierra Leone"},
    {"year": 1885, "name": "Sir Samuel Rowe, K.C.M.G.", "position": "Governor", "colony": "Sierra Leone"},
    {"year": 1888, "name": "Sir Saml. Rowe, K.C.M.G.", "position": "Administrator", "colony": "Sierra Leone"},
    {"year": 1889, "name": "Samuel Rowe", "position": "Administrator", "colony": "Gold Coast"},  # Different person? Same?
]

print("\n🔍 Entity Resolution Problem:\n")
print("   These records appear in different years:\n")
for p in person_appearances:
    print(f"   {p['year']}: {p['name']} - {p['position']} ({p['colony']})")

print("\n   Questions:")
print("   - Are rows 1-3 the same person? (Probably yes - same colony, honors accumulate)")
print("   - Is row 4 the same person? (Maybe - moved colonies? Or different Samuel Rowe?)")
print("\n   Signals for matching:")
print("   - Name similarity (fuzzy matching)")
print("   - Colony continuity")
print("   - Honor accumulation (never lose a K.C.M.G.)")
print("   - Career plausibility (Governor → Administrator is demotion?)")


# =============================================================================
# PART 7: DISCUSSION QUESTIONS
# =============================================================================

print("\n" + "=" * 60)
print("DISCUSSION QUESTIONS")
print("=" * 60)
print("""
1. What other historical sources have similar structure?
   (Army Lists, India Office Lists, Crockford's Clerical Directory...)

2. How would you measure extraction accuracy?
   (Gold standard annotation, sampling, downstream task performance...)

3. What's the minimum viable proof-of-concept?
   (One colony, 5 years? One year, all colonies?)

4. When is "good enough" good enough?
   (80% accuracy? 95%? Depends on research question?)

5. What would a human-in-the-loop workflow look like?
   (LLM extracts, human reviews flagged cases, system learns...)
""")


# =============================================================================
# EXERCISES FOR STUDENTS
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)
print("""
EXERCISE 1: Regex Challenge
   Modify extract_with_better_regex() to handle the COMPLEX_SAMPLE
   (Sierra Leone data with military ranks and qualifications)

EXERCISE 2: Schema Design
   Extend OfficialRecord to handle:
   - Geographic location (e.g., "Eastern District")
   - Acting vs permanent appointments
   - Quarters/housing benefits

EXERCISE 3: Entity Resolution
   Write a function that takes two person records and returns
   a similarity score (0-1) based on:
   - Name similarity (try difflib.SequenceMatcher)
   - Honor compatibility (honors should only accumulate)
   - Colony match

EXERCISE 4: Cost Estimation
   If GPT-4o-mini costs $0.15/1M input tokens:
   - Estimate tokens per colony entry (~2000 words?)
   - Calculate cost to process entire corpus
   - Compare to human annotation cost
""")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("END OF DEMO")
    print("=" * 60)
    print("\nRun this script to see extraction approaches in action.")
    print("Modify and experiment with the code!")
