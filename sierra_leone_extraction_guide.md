# Sierra Leone Colonial Office List - Extraction Guide for Gemini

## Overview

This guide provides instructions for extracting personnel data from Sierra Leone Colonial Office List files using Google AI Studio (Gemini). The goal is to produce structured JSON output that can be loaded into a Neo4j knowledge graph.

**Target Model**: Gemini 1.5 Pro or Gemini 2.0 Flash (via AI Studio - free tier)

---

## Source Files

### Test Data
```
/home/jic823/textasdatacolonialofficelist/1896_manual_parsed/sierra_leone.txt
```

### Full Collection Years
- 1896, 1897, 1898, 1899, 1900 (available in repository)

---

## Neo4j Schema

### Node Types

#### Person
```
(:Person {
    uuid: String,
    canonical_name: String,    # "Surname, Given Names" - PRIMARY KEY
    surname: String,
    given_names: String,
    titles: [String],          # ["Sir", "Colonel", "Rev."]
    qualifications: [String],  # ["C.M.G.", "M.D.", "M.R.C.S."]
    source_years: [Integer],   # [1896, 1897]
    colony: String             # "Sierra Leone"
})
```

#### Position
```
(:Position {
    uuid: String,
    title: String,             # "Colonial Secretary"
    department: String         # "Colonial Secretary's Department - Sierra Leone"
})
```

#### Department (Colony-qualified to avoid conflicts)
```
(:Department {
    name: String               # "Colonial Secretary's Department - Sierra Leone"
})
```

#### YearRecord
```
(:YearRecord {
    year: Integer,
    colony: String             # "Sierra Leone"
})
```

#### Location
```
(:Location {
    uuid: String,
    name: String,              # "Freetown", "Sherbro", "Sulymah"
    type: String               # "capital", "town", "district"
})
```

### Relationships
- `(Person)-[:HELD_POSITION {year, salary_min, salary_max, allowances, tenure_type}]->(Position)`
- `(Position)-[:POSITION_IN]->(Department)`
- `(Person)-[:APPEARED_IN]->(YearRecord)`
- `(Position)-[:BASED_AT]->(Location)`

---

## Department List (Sierra Leone)

Standard departments to use (colony-qualified):
- Civil Establishment - Sierra Leone
- Executive Council - Sierra Leone
- Legislative Council - Sierra Leone
- Colonial Secretary's Department - Sierra Leone
- Treasury Department - Sierra Leone
- Audit Department - Sierra Leone
- Department for Native Affairs - Sierra Leone
- Port and Marine Department - Sierra Leone
- Printing Department - Sierra Leone
- Surveyor's Department - Sierra Leone
- Customs Department - Sierra Leone
- Post Office Department - Sierra Leone
- Legal Departments - Sierra Leone
- Ecclesiastical Department - Sierra Leone
- Educational Department - Sierra Leone
- Medical Department - Sierra Leone
- Sanitary Department - Sierra Leone
- Police Department - Sierra Leone
- Prison Department - Sierra Leone
- Eastern District - Sierra Leone
- Western District - Sierra Leone
- Sherbro District - Sierra Leone

---

## Extraction Patterns

### Title Patterns (appear BEFORE name)
```
Military: Colonel, Lt.-Col., Lieut.-Col., Major-General, Major, Captain, Capt.
Honorific: Sir, The Right Hon., The Hon., Right Rev., Rev., Ven., Dr.
```

### Honors (appear AFTER name) - Post-nominal letters for service/achievement
```
K.C.M.G., G.C.M.G., C.M.G., K.C.B., G.C.B., C.B., K.C.S.I., D.S.O., Kt., Knt.
```

### Qualifications (appear AFTER name) - Academic/professional credentials
```
Medical: M.D., M.B., M.R.C.S., F.R.C.S., L.R.C.S., L.R.C.P., F.R.C.P.
Academic: B.A., M.A., B.Sc., M.Sc., LL.D., D.D., Ph.D., B.L.
Engineering: R.E., C.E., M.I.C.E., A.I.C.E.
Other: F.R.S., F.R.G.S.
```

### Salary Formats
```
Simple: 200l.                    → salary_min: 200, salary_max: 200
Range: 300l. to 400l.           → salary_min: 300, salary_max: 400
With shillings: 91l. 5s.        → salary_min: 91 (note shillings in allowances)
With allowances: 500l. and quarters → salary_min: 500, allowances: "quarters"
```

### Special Patterns

#### "Ditto" - References previous position type
```
Chief Clerk, J. E. Dawson, 200l.
2nd ditto, E. W. Cole, 100l.        → Position: "2nd Clerk"
3rd ditto, J. W. Paris, 100l.       → Position: "3rd Clerk"
```

#### Multiple people on one line (semicolon-separated)
```
Assistant ditto, Wm. Renner, M.R.C.S., 300l.; M. L. Jarrett, M.R.C.S., 250l.; I. N. Paris, M.B., 200l.
```
Extract as THREE separate officials with same position type.

#### Location in position title
```
Dispenser, Waterloo, W. Z. Young, 50l.
```
Extract: position="Dispenser", location="Waterloo"

---

## Gemini Prompt Template

Copy this prompt into AI Studio with the source text:

```
You are extracting personnel records from a British Colonial Office List. Output structured JSON.

## Task
Extract ALL officials from this Sierra Leone Colonial Office List (1896).

## Output Format
Return a JSON object with this structure:
{
  "colony": "Sierra Leone",
  "year": 1896,
  "officials": [
    {
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
      "location": null
    }
  ]
}

## Rules
1. Extract EVERY person, even multiple on one line
2. "ditto" = same position type as line above (2nd ditto = 2nd Clerk if previous was Chief Clerk)
3. Salaries: "300l. to 400l." → min=300, max=400; "200l." → min=max=200
4. Honors (C.M.G., K.C.M.G.) go in "honors" array
5. Qualifications (M.D., M.B., M.R.C.S., B.A.) go in "qualifications" array
6. Military ranks (Colonel, Lt.-Col.) go in "military_rank" field
7. Extract location from position if mentioned (e.g., "Dispenser, Waterloo")
8. Expand ONLY these known abbreviations: Wm.=William, Chas.=Charles, Thos.=Thomas, Jas.=James, Jno.=John, Robt.=Robert, Geo.=George
9. Do NOT expand single initials (C., G., J., etc.) - keep them exactly as written. "C. George" stays "C. George", NOT "Charles George"
10. Skip lines with no name (vacant positions like "Kent, 40l.")
11. Department names should include " - Sierra Leone" suffix

## Source Text
[PASTE THE COLONIAL OFFICE LIST TEXT HERE]
```

---

## Processing Workflow

### Step 1: Prepare Source Text
Read the source file and prepare sections for extraction.

### Step 2: Extract in Chunks
For large files, process by department section to stay within context limits:
1. Civil Establishment + Executive/Legislative Councils
2. Colonial Secretary's + Treasury + Audit Departments
3. Native Affairs + Port + Printing + Surveyor's
4. Customs + Post Office + Legal
5. Education + Medical + Sanitary
6. Police + Prison + Districts

### Step 3: Combine Results
Merge JSON outputs from each chunk into a single file.

### Step 4: Validate
Check counts and spot-check entries for accuracy.

### Step 5: Load to Neo4j
Use Python script to load validated JSON to Neo4j database.

---

## Validation Checklist

After extraction, verify:
- [ ] Governor and top officials captured
- [ ] All departments have entries
- [ ] Salary formats parsed correctly (no "None" for valid salaries)
- [ ] Honors and qualifications extracted (check Medical dept for M.R.C.S., M.B.)
- [ ] Military ranks captured (check Governor: Colonel)
- [ ] Locations extracted for Dispensers, District Officers
- [ ] "Ditto" entries expanded to proper position names
- [ ] Multi-person lines split correctly (check Medical dept: 3 Assistant Colonial Surgeons)

---

## Expected Counts (1896)

| Department | Expected Officials |
|------------|-------------------|
| Civil Establishment | 3 |
| Colonial Secretary's Dept | 9 |
| Treasury | 9 |
| Audit | 4 |
| Native Affairs | 4 |
| Customs | 30+ |
| Post Office | 9 |
| Legal | 15 |
| Medical | 20+ |
| Police | 15+ |
| Prison | 6 |
| Districts | 10+ |
| **TOTAL** | ~150-170 |

---

## Sample Python Loading Script

After Gemini extraction, use this to load to Neo4j:

```python
import json
from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "password")
DATABASE = "colonialoffice"

def load_extraction(json_file: str):
    with open(json_file) as f:
        data = json.load(f)

    driver = GraphDatabase.driver(URI, auth=AUTH)

    with driver.session(database=DATABASE) as session:
        # Ensure YearRecord exists
        session.run("""
            MERGE (y:YearRecord {year: $year, colony: $colony})
        """, year=data['year'], colony=data['colony'])

        for official in data['officials']:
            # Create/merge Person
            session.run("""
                MERGE (p:Person {canonical_name: $canonical_name})
                ON CREATE SET
                    p.uuid = randomUUID(),
                    p.surname = $surname,
                    p.given_names = $given_names,
                    p.colony = $colony,
                    p.source_years = [$year]
                ON MATCH SET
                    p.source_years = CASE
                        WHEN NOT $year IN p.source_years
                        THEN p.source_years + $year
                        ELSE p.source_years
                    END
            """,
                canonical_name=official['canonical_name'],
                surname=official['surname'],
                given_names=official['given_names'],
                colony=data['colony'],
                year=data['year']
            )

            # Create Position and relationship
            session.run("""
                MERGE (pos:Position {title: $title, department: $department})
                ON CREATE SET pos.uuid = randomUUID()
                WITH pos
                MATCH (p:Person {canonical_name: $canonical_name})
                MERGE (p)-[r:HELD_POSITION {year: $year}]->(pos)
                SET r.salary_min = $salary_min,
                    r.salary_max = $salary_max,
                    r.allowances = $allowances
            """,
                title=official['position'],
                department=official['department'],
                canonical_name=official['canonical_name'],
                year=data['year'],
                salary_min=official['salary_min'],
                salary_max=official['salary_max'],
                allowances=official.get('allowances')
            )

            # Link to YearRecord
            session.run("""
                MATCH (p:Person {canonical_name: $canonical_name})
                MATCH (y:YearRecord {year: $year, colony: $colony})
                MERGE (p)-[:APPEARED_IN]->(y)
            """,
                canonical_name=official['canonical_name'],
                year=data['year'],
                colony=data['colony']
            )

    driver.close()
    print(f"Loaded {len(data['officials'])} officials")

if __name__ == "__main__":
    load_extraction("gemini_extraction_results.json")
```

---

## Cost Comparison Notes

| Approach | Est. Cost per Colony |
|----------|---------------------|
| Gemini (AI Studio) | $0 (free tier) |
| Claude API (Sonnet) | ~$0.10-0.50 |
| Claude API (Opus) | ~$0.50-2.00 |
| OpenAI GPT-4o | ~$0.20-1.00 |
| Regex (rule-based) | $0 |

---

## Next Steps

1. Run extraction on 1896 test data using Gemini
2. Compare output with gold standard (test_data/gold_standard.json)
3. If accuracy is acceptable (>90%), scale to full years
4. Document any failure modes for iterative prompt improvement
