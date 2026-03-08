# British West Africa — Extraction Expansion Plan

**Date**: 11 February 2026
**Scope**: Expand Colonial Office List personnel extraction from Sierra Leone to all British West Africa territories.

---

## 1. Current State

### Completed
- **Sierra Leone**: 55 years, 10,982 records (post-processing fixes applied)

### In Progress
- **Gold Coast**: 3 years extracted (1867, 1899, 1923), dedicated guide written, pipeline validated

### Not Started
- Gambia, Lagos, Northern Nigeria, Southern Nigeria, Nigeria (unified), and 7 minor territories

---

## 2. Scope of Work

| Territory | Unique Years | Source KB | Avg KB/yr | Guide |
|-----------|-------------|-----------|-----------|-------|
| **Gold Coast** | 58 | 3,678 | 63 | `gold_coast_guide.md` |
| **Nigeria (unified)** | 48 | 4,051 | 84 | `west_africa_guide.md` |
| **Gambia** | 65 | 1,595 | 25 | `west_africa_guide.md` |
| **Lagos** | 13 | 392 | 30 | `west_africa_guide.md` |
| **Southern Nigeria** | 10 | 573 | 57 | `west_africa_guide.md` |
| **Northern Nigeria** | 10 | 285 | 29 | `west_africa_guide.md` |
| **Togoland** | 3 | 109 | 36 | `west_africa_guide.md` |
| **Niger Coast Prot.** | 3 | 44 | 15 | `west_africa_guide.md` |
| **Cameroons** | 2 | 1 | <1 | `west_africa_guide.md` |
| **Ashanti** | 1 | 4 | 4 | `gold_coast_guide.md` |
| **N. Territories (GC)** | 1 | 16 | 16 | `gold_coast_guide.md` |
| **Niger Territories** | 1 | 41 | 41 | `west_africa_guide.md` |
| **W. African Settlements** | 1 | 7 | 7 | `west_africa_guide.md` |
| **TOTAL** | **216** | **10,796** | — | — |

Plus 6 remaining Sierra Leone years (1867, 1946, 1948 failed as narrative-only; 3 others uncovered).

---

## 3. Infrastructure Ready

All tooling is in place:

- **`extraction/batch_extract.py`** — universal extraction orchestrator (Gemini 2.0 Flash generates Python, Claude coordinates)
- **`guides/west_africa_guide.md`** (606 lines) — covers all BWA except Gold Coast
- **`gold_coast_extraction/gold_coast_guide.md`** (531 lines) — Gold Coast-specific
- **`guides/schema.py`** — 20-field schema, validation functions
- **`validation/validate_extractions.py`** — per-file validation + gold standard comparison
- **`extraction/sierra_leone/fix_extractions.py`** — reference template for post-processing

**Only requirement to run**: `GOOGLE_API_KEY` environment variable for Gemini API.

---

## 4. Recommended Extraction Order

### Phase 2a: Gambia (FIRST)

**Why**: Smallest files (avg 25 KB), longest coverage (65 years, 1867–1966), low complexity. Good validation that the pipeline generalizes beyond Sierra Leone.

```bash
python extraction/batch_extract.py \
  --colony "Gambia" \
  --guide guides/west_africa_guide.md \
  --test   # first: 3 sample years
```

- **Files**: 65 years
- **Expected records**: ~6,000–8,000 (smaller colony than Sierra Leone)
- **Estimated API time**: 2–4 hours
- **Challenges**: Small civil establishment means fewer officials per year; early years (1867–1880s) may have very sparse formatting

### Phase 2b: Gold Coast (RESUME)

**Why**: Dedicated guide exists, 3 years already validated, largest colony in BWA after Nigeria. High research value.

```bash
python extraction/batch_extract.py \
  --colony "Gold Coast" \
  --guide gold_coast_extraction/gold_coast_guide.md
```

- **Files**: 55 remaining (of 58)
- **Expected records**: ~15,000–20,000 (larger administration than Sierra Leone)
- **Estimated API time**: 6–10 hours (large files in 1930s–1950s, avg 63 KB)
- **Challenges**: Sub-territories (Ashanti, Northern Territories, Togoland) appear as sections within Gold Coast files in some years and as separate files in others. The guide handles this, but post-processing may need deduplication.

### Phase 2c: Pre-Unification Nigeria (Lagos + Northern + Southern)

**Why**: Historically important transition period. Moderate complexity. 33 years across 3 territories that merge in 1914.

```bash
# Run all three in sequence
python extraction/batch_extract.py --colony "Lagos" --guide guides/west_africa_guide.md
python extraction/batch_extract.py --colony "Northern Nigeria" --guide guides/west_africa_guide.md
python extraction/batch_extract.py --colony "Southern Nigeria" --guide guides/west_africa_guide.md
```

- **Files**: 33 years (13 + 10 + 10)
- **Expected records**: ~5,000–8,000
- **Estimated API time**: 4–6 hours
- **Challenges**: Southern Nigeria files average 57 KB (complex administration). Northern Nigeria uses "Residents" and "Assistant Residents" by province — different structure from typical colonial departments. Lagos is small and straightforward.

### Phase 2d: Unified Nigeria

**Why**: Largest and most complex territory. Leave for last to benefit from lessons learned.

```bash
python extraction/batch_extract.py \
  --colony "Nigeria" \
  --guide guides/west_africa_guide.md
```

- **Files**: 48 years (1914–1961)
- **Expected records**: ~25,000–35,000 (massive administration)
- **Estimated API time**: 10–16 hours (files avg 84 KB, 11 files >100 KB)
- **Challenges**:
  - Files are the largest in BWA (up to 95 KB)
  - Complex provincial structure (Northern Provinces, Southern Provinces, each with lieutenant-governors)
  - Cameroons mandate sections appear within Nigeria files after 1922
  - Post-1945 salary scales and format changes (same issues as Sierra Leone 1949–1960)

### Phase 2e: Minor Territories

**Why**: Small files, low effort, historical completeness.

```bash
# Can run these quickly
python extraction/batch_extract.py --colony "Niger Coast Protectorate" --guide guides/west_africa_guide.md
python extraction/batch_extract.py --colony "Togoland" --guide guides/west_africa_guide.md
# etc.
```

- **Files**: 12 years across 7 territories
- **Expected records**: ~1,000–2,000
- **Estimated API time**: 1–2 hours
- **Note**: West African Settlements (1867) is the umbrella administration that preceded separate colonies — historically interesting but only 1 file.

---

## 5. Post-Processing Strategy

Apply the Sierra Leone fix pattern to each colony after extraction:

### 5a. Create `fix_extractions.py` per colony

Each colony will likely need fixes for:
- **Historical governor lists** (same pattern as Sierra Leone 1950)
- **Salary scale resolution** (scales may differ between colonies — need to check RAG narratives)
- **OCR misspellings** (colony-specific, identified during QA)
- **Null-name VACANT positions** (universal)
- **1952+ format change** (universal across all BWA colonies)

### 5b. Create `known_gaps.json` per colony

Document truncated sources, missing years, and format changes for downstream analysis.

### 5c. Cross-colony validation

After all BWA colonies are extracted:
- Officials who served in multiple colonies should have consistent names
- Governor lists can be cross-validated against RAG "Governors since..." narratives
- Department naming should be reasonably consistent within eras

---

## 6. Expected Outputs

### Total Estimated Records

| Territory | Est. Records | Years |
|-----------|-------------|-------|
| Sierra Leone | 10,982 | 55 ✓ |
| Gold Coast | ~17,000 | 58 |
| Nigeria (unified) | ~30,000 | 48 |
| Gambia | ~7,000 | 65 |
| Lagos | ~2,000 | 13 |
| Southern Nigeria | ~3,000 | 10 |
| Northern Nigeria | ~2,000 | 10 |
| Minor territories | ~1,500 | 12 |
| **BWA TOTAL** | **~73,500** | **271** |

### Deliverables per Colony

```
extraction/{colony_slug}/
├── json/                    # Final extraction (1 JSON per year)
├── generated/               # Python extraction scripts
├── rag/                     # Narrative sections for RAG
├── section_maps/            # Gemini section maps
├── salary_scales.json       # Scale definitions (if applicable)
├── known_gaps.json          # Documented data gaps
├── fix_extractions.py       # Post-processing script
└── STATUS_REPORT.md         # Colony-level report
```

---

## 7. Timeline Estimate

| Phase | Territory | Est. Time | Depends On |
|-------|-----------|-----------|-----------|
| 2a | Gambia | 2–4 hrs | API key |
| 2b | Gold Coast | 6–10 hrs | API key |
| 2c | Lagos/N.Nigeria/S.Nigeria | 4–6 hrs | API key |
| 2d | Nigeria (unified) | 10–16 hrs | Phase 2c learnings |
| 2e | Minor territories | 1–2 hrs | Any time |
| QA | Post-processing all | 2–4 hrs | All phases |
| **Total** | | **25–42 hrs API time** | |

All phases can run overnight as batch jobs. The main bottleneck is Gemini API throughput and rate limits.

---

## 8. Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Nigeria files too large for single-section extraction | Extraction fails or times out | `batch_extract.py` already handles section splitting; validated on Sierra Leone files up to 45 KB per section |
| Salary scale definitions differ between colonies | Inaccurate min/max | Extract RAG narrative sections first, build per-colony scale lookup |
| Cameroons/Togoland sections embedded in parent colony files | Double-counting or missed records | West Africa guide addresses this; post-processing deduplication |
| Gemini API rate limits during batch runs | Slow extraction | Built-in retry + backoff in `batch_extract.py`; can split into multi-day runs |
| Post-1951 format change reduces data value | Fewer records for 1952–1966 | Document as known limitation (not a bug); pre-1952 data is the primary research corpus |

---

## 9. Next Step

Run Gambia as the pilot:

```bash
# Test run (3 sample years)
GOOGLE_API_KEY=<key> python extraction/batch_extract.py \
  --colony "Gambia" \
  --guide guides/west_africa_guide.md \
  --test

# If test passes, full run:
GOOGLE_API_KEY=<key> python extraction/batch_extract.py \
  --colony "Gambia" \
  --guide guides/west_africa_guide.md
```
