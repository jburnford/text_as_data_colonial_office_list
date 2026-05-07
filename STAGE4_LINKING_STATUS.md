# COL Knowledge Graph Pipeline Status

**Date**: 2026-03-12
**Data coverage**: 313,291 PersonRecords from 2,184/2,939 TerritoryYears (74.3%)

## Full Pipeline

| Stage | Script | Purpose |
|-------|--------|---------|
| 0 | `col_build_kg.py` | Scaffold: COL_Year, COL_Territory, COL_TerritoryYear nodes |
| 1 | `col_build_kg.py --load-only` | Load PersonRecords from `generated/` into Neo4j |
| 1.5 | `col_normalize_names.py` | Normalize canonical_name: strip titles/honours/ranks, unify variants |
| 2 | `col_build_officials.py` | Group PersonRecords into COL_Official career stints |
| 4a | `col_link_officials.py` | Link broken stints within same colony (POSSIBLE_MATCH) |
| 4c | `col_link_cross_colony.py` | Link officials across different colonies (POSSIBLE_MATCH) |

### Rebuild Sequence (after new extractions)

```bash
# Stage 1: Load new PersonRecords (incremental, safe)
python col_build_kg.py --load-only

# Stage 1.5: Normalize names (strips titles/honours, unifies initials→full names)
python col_normalize_names.py

# Stage 2: Rebuild Officials (clear + recreate — gaps change with new data)
python col_build_officials.py --clear
python col_build_officials.py

# Stage 4a: Recompute within-colony links
python col_link_officials.py --clear
python col_link_officials.py

# Stage 4c: Recompute cross-colony links
python col_link_cross_colony.py --clear
python col_link_cross_colony.py
```

---

## Stage 1.5: Name Normalization ✅

**Script**: `col_normalize_names.py`
**Result**: 281,982 PersonRecords normalized (of 313,291 total).

Three normalization steps:
1. **Title stripping**: "Sir Anthony" → "Anthony" (2,537 records)
2. **Honour/rank stripping**: "D.S.O., Brigadier-General Sir Frederic Gordon" → "Frederic Gordon" (204 records)
3. **Variant unification**: Within (surname, colony) groups, initial-compatible names unified to most specific form (42,735 records)
4. **Trailing period normalization**: "E. W. T." → "E. W. T" for consistency (237,997 records)

### Initial Compatibility Rules
- Both initials: first letters must match ("F." = "F.")
- One initial + one full word: first letters must match ("F." = "Frederick")
- Both full words: must match exactly ("Elizabeth" ≠ "Edwin")
- Bare surname matches anything ("Guggisberg" = "Guggisberg, F. Gordon")

### Guggisberg Case Study
Before: 5 variants (`Guggisberg`, `Guggisberg, F. G.`, `Guggisberg, F. Gordon`, `Guggisberg, Sir F. Gordon`, `Guggisberg, D.S.O., Brigadier-General Sir Frederic Gordon`)
After: Unified to `Guggisberg, F. Gordon` within each colony → 2 COL_Officials (Gold Coast + Togoland), cross-colony linked at 0.395

### Known Limitations
- OCR variants like "Julien"/"Julian" or "Thos"/"Thomas" are NOT unified (strict full-word matching to avoid false merges)
- ~589 remaining false-positive-risk groups (e.g., "Taylor, E. Godman" matches "Taylor, Edwin" via initial "E.")
- Records with empty `given_names` stay as bare surname (cannot be unified further without data)

---

## Stage 4a: Within-Colony Linking ✅

**Script**: `col_link_officials.py`
**Result**: 2,005 POSSIBLE_MATCH edges linking broken career stints within the same colony.

Publication gaps in the COL corpus (1890→1894, 1900→1905, 1912→1921, 1940→1946) split continuous careers into fragments. Stage 4a bridges those gaps with scored hypotheses.

Scoring: base(0.03) + missed_editions_penalty + gap_penalty + domain_mod + name_mod - tenure_bonus.

## Stage 4c: Cross-Colony Linking ✅

**Script**: `col_link_cross_colony.py`
**Result**: 2,087 POSSIBLE_MATCH edges linking officials across different colonies.

| Metric | Count |
|--------|-------|
| Raw candidate pairs | 3,941 |
| Under threshold (≤0.70) | 2,837 |
| Edges written (after MERGE) | 2,087 |
| High confidence (<0.20) | 1,245 |
| Federal duplicates detected | 252 |
| Sequential transfers | 1,594 |
| Transition year | 84 |
| Multi-year overlap | 157 |

### Scoring Formula

10 components, base 0.15, floor 0.10, ceiling 1.0, threshold 0.70:

- **Name specificity** (primary signal): high -0.10, low +0.20
- **Honours matching** with upgrade detection (C.M.G.→K.C.M.G.): exact -0.12, mismatch +0.15
- **Military rank**: exact -0.06, mismatch +0.10
- **Regional transfer circuits** (12 curated): circuit -0.10, distant +0.12
- **Domain match** (reused from 4a): exact -0.08, implausible +0.20
- **Seniority direction**: promotion -0.04, demotion +0.10
- **Gap penalty**: 1-2y -0.03 (ideal), 6-10y +0.05
- **Colony count penalty**: 4+ colonies +0.15
- **Tenure bonus**: up to -0.08
- **Overlap handling**: federal duplicate -0.10, multi-year +0.25/year

### Concurrent Posting Classification

Temporal overlaps are classified, not filtered:

1. **Federal duplicates** — same person listed under both sub-colony and federation (e.g., St Vincent AND Windward Islands). 252 detected. Treated as identity signal.
2. **1-year transition** — scored normally (neutral). 84 detected.
3. **Multi-year overlap** — heavy penalty (+0.25/year beyond 1). 157 detected.

### Top Colony Pairs

| Pair | Count | Avg Uncertainty |
|------|-------|----------------|
| Windward Islands → Grenada | 64 | 0.104 |
| Windward Islands → St Lucia | 45 | 0.104 |
| Trinidad → Trinidad and Tobago | 45 | 0.154 |
| British Central Africa → Nyasaland | 34 | 0.136 |
| Togoland → Gold Coast | 33 | 0.628 |
| Leeward Islands → St Christopher and Nevis | 30 | 0.122 |

### Validation Against Wikipedia

**Allardyce, W. L.** (Sir William Lamond Allardyce, GCMG, 1861–1930):
- ✅ Colony sequence Fiji→Falkland Islands→Bahamas correctly identified
- ⚠️ Bahamas dates wrong: COL lists him 1927–1940 but he died 1930 (ghost/posthumous entries)
- ❌ Missing Tasmania and Newfoundland (dominion/settler colonies not in COL)
- ✅ Brother Kenneth Allardyce correctly kept separate (different initials)

**Guggisberg, F. Gordon** (Brigadier-General Sir Frederick Gordon Guggisberg, KCMG, DSO, 1869–1930):
- ✅ Name normalization unified 5 variants → `Guggisberg, F. Gordon`
- ✅ 2 COL_Officials created (Gold Coast 1922-1927, Togoland 1920-1925)
- ✅ Cross-colony link: Togoland→Gold Coast at uncertainty 0.395
- ⚠️ Southern Nigeria (1911-1912) and Aden (1922) below 3-edition threshold
- ❌ Gold Coast 1919-1921 in extraction gap (only 3 Gold Coast years extracted from .md files so far)

## Pipeline Numbers Summary

| Metric | Before Normalization | After Normalization |
|--------|---------------------|---------------------|
| PersonRecords | 313,291 | 313,291 (unchanged) |
| COL_Official nodes | 33,244 | 32,824 (-420) |
| RECORD_OF edges | 197,625 | 209,171 (+11,546) |
| Within-colony links (4a) | 1,633 | 2,005 (+23%) |
| Cross-colony links (4c) | 2,283 | 2,087 (-9%) |

The cross-colony count dropped because normalization eliminated spurious name variant matches. More records now chain into existing COL_Officials (RECORD_OF +11,546), and more broken stints now link within-colony (+23%).

## Blocking Issue: .md File Extraction Gap

**The extraction pipeline skipped all 719 .md source files**, processing only the 2,227 .txt files. This affects ~24% of the corpus across all colonies.

### Impact
- Gold Coast: 15/58 years extracted (entire 1900–1950 missing)
- Similar gaps across hundreds of colony-years
- Many high-profile officials (governors, senior administrators) invisible to linking

### Fix Required
1. Update extraction pipeline glob to include `*.md` files
2. Extract the 719 missing files
3. Reload: `python col_build_kg.py --load-only --force`
4. Rerun full pipeline (Stage 1.5 → 2 → 4a → 4c)

### Expected After Fix
- ~25-30% more PersonRecords
- COL_Official count should grow from 32,824 to ~40,000+
- Cross-colony edges should increase significantly
- Guggisberg's full Gold Coast governorship should become visible

## Stages Not Yet Started

- **Stage 3** (Normalization): 12 CareerTrack categories defined but not implemented
- **Stage 4b** (Person nodes): Depends on 4a/4c analysis
- **Stage 5** (Wikidata verification): Use Wikidata P39 (position held) to anchor/verify careers — proposed but not scoped
