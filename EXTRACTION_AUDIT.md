# COL Extraction Audit

**Purpose**: Track data quality issues in the extraction pipeline, especially colony attribution errors from the COL's multi-section structure.

**Status**: IN PROGRESS — full audit pending completion of .md file extractions

---

## The Core Challenge

The Colonial Office List is a single volume with multiple sections:
1. **Colony staff lists** — the target data (officials by colony, with positions/departments)
2. **Order of St Michael and St George** — honours list (Knights Grand Cross, Commanders, etc.)
3. **General Colonial Service List** — cross-colony directory of all officials
4. **Miscellaneous appendices** — regulations, salary scales, pension rules

The extraction pipeline must correctly attribute each section to its colony. When it fails, appendix data gets loaded as if it were colony staff, creating phantom officials.

---

## Known Contaminated Files

### Aden 1922 — HONOURS LIST CONTAMINATION
- **File**: `aden_1922_data_gpt-oss_120b.json`
- **Records**: 921 (should be ~20-40 for Aden)
- **Issue**: Entire Order of St Michael and St George honours list extracted as Aden officials
- **Evidence**: 88% have `position=None`, departments are "Knights Grand Cross", "Commanders", "Members"
- **Impact**: 810+ phantom PersonRecords in Neo4j attributed to Aden
- **Affected officials**: Guggisberg (listed as Aden 1922, was actually Governor of Gold Coast), plus hundreds of governors, generals, knights from across the empire
- **Fix**: Re-extract with colony boundary detection, or quarantine/delete these records

### Candidates for Review
- Any colony-year with unusually high official counts relative to colony size
- Files where >30% of records have `position=None`

---

## Systematic Checks Needed (post-extraction)

### 1. Official Count Reasonableness
Compare official counts per colony-year against expected ranges:
- Small colonies (Aden, Gambia, Falklands): 10-60 officials
- Medium colonies (Gold Coast, Sierra Leone, Fiji): 50-300
- Large colonies (Nigeria, India, Canada): 200-1000+

Flag any colony-year >3x the median for that colony.

### 2. Position Coverage
Flag files where >50% of records have `position=None` AND the colony isn't expected to have that many officials.

### 3. Honours List Markers
Detect records with these patterns (likely honours list contamination):
- Department contains: "Knights Grand Cross", "Knights Commander", "Commanders", "Members"
- Position contains: "Knights Grand Cross", "Prelate", "Chancellor", "King of Arms"
- Name contains full honours string with no position (e.g., "Guggisberg, D.S.O., Brigadier-General Sir...")

### 4. Cross-Colony Directory Detection
Detect when the General Colonial Service List was extracted as a colony:
- Very high official count
- Officials whose names appear in many other colonies
- No department structure typical of a single colony

### 5. Year-over-Year Consistency
For each colony, compare official counts across years. A sudden spike (e.g., Aden going from 30 to 921) indicates contamination.

---

## Impact on Knowledge Graph

Contaminated records create:
1. **Phantom COL_Official nodes** — people who never served in that colony
2. **False cross-colony links** — the phantom official "transfers" to a colony they were actually always in
3. **Inflated statistics** — colony official counts become unreliable
4. **Name pollution** — bare surnames from honours lists (no given names, no position) add noise

### Mitigation
- Stage 1.5 normalization handles some noise (bare surnames unified where unambiguous)
- Stage 4c cross-colony linking can produce false positives from phantom records
- Once identified, contaminated records should be quarantined (not deleted — preserve audit trail)

---

## Quarantine Protocol (proposed)

```cypher
-- Mark contaminated records
MATCH (pr:COL_PersonRecord)
WHERE pr.colony = "Aden" AND pr.year = 1922
  AND pr.position_raw IS NULL AND pr.department_raw IS NULL
SET pr.quarantined = true, pr.quarantine_reason = "honours_list_contamination"

-- Exclude from pipeline
-- All pipeline queries should add: WHERE pr.quarantined IS NULL OR pr.quarantined = false
```

---

## Audit Results (to be completed)

| Colony | Year | File | Officials | Expected | Issue | Status |
|--------|------|------|-----------|----------|-------|--------|
| Aden | 1922 | aden_1922_data_gpt-oss_120b.json | 921 | ~30 | Honours list | CONFIRMED |
| | | | | | | |

*Table to be populated after full corpus extraction is complete.*
