# Local Extraction Pipeline — Development Status

**Date:** 19 February 2026
**Machine:** Project DIGITS (NVIDIA GB10, 128 GB unified memory)
**Model:** gpt-oss:120b via Ollama

---

## Summary

We have a working, benchmarked local extraction pipeline that converts OCR-parsed Colonial Office List text into structured JSON. On the Sierra Leone 1896 test case, the pipeline achieves **100% accuracy across all fields** against a Gemini 3.0 Flash reference.

**Sierra Leone (17 years)** — complete. 2,747 officials extracted, 99.5% HIGH confidence.

**Full corpus infrastructure** — ready to go. New orchestrator (`extraction_corpus.py`) handles all ~2,200 colony-year files with checkpointing, source-text validation, and automatic resume.

---

## What exists

### Source data
- **68 year-directories** (1867–1966), each containing manually parsed `.txt`/`.md` files per colony
- Up to **49 colonies per year** (e.g. 1896), covering the full British Empire
- **17 usable Sierra Leone files** selected for initial pipeline development
- **2,227 total colony-year files** across 133 colonies and 53 years

### Extraction pipeline (`extraction_ollama.py`)
- Sends source text to gpt-oss:120b via Ollama's local API
- **Chunking by department** — splits text on department headers to stay within the model's 8K output token limit
- Code-generation mode: model writes a Python file containing an `OFFICIALS` list, which is then executed to produce JSON
- Extracts: name, position, department, salary (min/max), honors, qualifications, military rank, location, allowances
- **~90 department header patterns** covering all eras and cross-colony departments
- **Large-file fallback** — headerless files > 100 lines split into 50-line overlapping chunks

### Batch runner (`extraction_batch.py`)
- Processes multiple years sequentially with automatic preamble stripping
- **Cascading marker search** — 5 strategies to find staff list start: Civil Establishment → Executive Council → Legislative Council → Governor/Commander → salary-line heuristic
- Generalized `find_source_file(year, colony)` — handles filename variants, uses `normalize_colony_name()` fallback
- Skips already-completed years, so safe to re-run after interruption

### Source-text validation (`validation.py`)
- **Name anchoring** — confirms each extracted surname appears in the source text
  - HIGH: surname + initials found, MEDIUM: surname only, LOW: not found
  - Common surnames (Smith, Williams, etc.) require initial confirmation
- **Salary anchoring** — verifies salary figures appear within 200 chars of the surname
- **Cross-year consistency** — flags single-year-only officials, missing departments, 50%+ count drops
- **Anomaly detection** — salary range, duplicate names, oversized departments
- **Quarantine threshold 0.4** — LOW records never enter Neo4j
- Validated: 185/186 Sierra Leone 1896 officials score HIGH against full source; 42/42 gold standard score HIGH

### Full corpus orchestrator (`extraction_corpus.py`)
- Discovers all ~2,227 colony-year files, classifies into quality tiers by size
- **Processing order**: 1896 reference year first, then STANDARD → LARGE → SMALL → XLARGE
- **Checkpointing** — saves state to `corpus_state.json` after every file; auto-resumes
- **SIGINT handling** — Ctrl+C finishes current file, saves state, exits cleanly
- **Validation integrated** — every extraction validated before saving; quarantined records saved separately
- Built-in `--report` to generate summary from checkpoint state

### Human review tool (`review_extraction.py`)
- CLI showing source text + extracted JSON + validation flags
- APPROVE / REJECT / FLAG workflow with notes
- Auto-identifies mandatory review targets (first year per colony, XLARGE, high quarantine rate)
- Random sampling (10% STANDARD, 20% LARGE per decade)

### Benchmarking (`benchmark_local_models.py`)
- Automated field-by-field evaluation against reference data
- Manages GPU memory (stops models between runs to avoid OOM)

### Neo4j graph scaffold (`scaffold_neo4j.py`)
- Stage 0 loaded: 68 Year nodes, 133 Territory nodes, 2,220 TerritoryYear slices, 2,094 CONTINUES_AS edges
- Docker at `bolt://localhost:7687`

### Live monitor (`monitor.py`)
- Real-time progress display for running extractions
- `python monitor.py` — live updating every 10s
- `python monitor.py --once` — snapshot

---

## Prompt iteration — what we learned

Three iterations to reach 100% on gpt-oss:120b:

| Version | Change | Qualifications | Position | Location |
|---------|--------|---------------|----------|----------|
| v1 | Original prompt | 67% | 100% | 100% |
| v2 | + expanded qual list + 3 worked examples | **100%** | 86% | 83% |
| v3 | + expanded qual list + ditto rules, NO worked examples | **100%** | **100%** | **100%** |

**Key insight:** gpt-oss performs better with concise rules than lengthy worked examples. The worked examples in v2 improved qualifications but caused regressions in position and location parsing. Removing them and adding a one-line ditto resolution rule fixed everything.

---

## Completed — Sierra Leone (all 17 years)

**Finished:** 19 Feb 2026
**Total:** 2,747 officials across 17 years (1879–1960)
**Validation:** 99.5% HIGH confidence (2,734/2,747), 1 quarantined record
**Log:** `generated/overnight_run_20260219_084258.log`

### Per-year breakdown

| Year | Officials | Notes |
|------|-----------|-------|
| 1879 | 65 | Earliest year |
| 1880 | 63 | |
| 1883 | 74 | |
| 1894 | 156 | |
| 1896 | 186 | Validated against Gemini reference — 100% match |
| 1899 | 228 | |
| 1909 | 328 | |
| 1911 | 362 | |
| 1921 | 290 | |
| 1923 | 377 | |
| 1946 | 15 | War-era edition — council members only, no staff list |
| 1948 | 36 | Post-war recovery — thin staff list |
| 1950 | 233 | Staff lists return |
| 1951 | 254 | |
| 1953 | 20 | Condensed summary format |
| 1958 | 28 | Condensed summary format |
| 1960 | 32 | Final year before independence |

### Known issues from review

- **1946–1948 thin extractions** are genuine: the Colonial Office List war-era editions dropped detailed staff lists. Only council membership was published. Staff lists return ~1950.
- **1953/1958/1960 low counts** are genuine: later editions switched to condensed summary format for Sierra Leone.
- **Late-era salary extraction**: 1950+ entries sometimes use em-dash format (`Colonial Secretary—R. O. Ramage, C.M.G. £1,650.`). The model occasionally returns `null` for salaries in this format. May need a prompt hint for corpus runs — low priority since most data is captured.
- **1946 parser issue**: some colony files in the source corpus contain multiple colonies concatenated (e.g. Jamaica includes Kenya). This is an upstream OCR/parsing problem, not an extraction bug. The validation layer will quarantine misattributed records.

---

## Next steps — full corpus extraction

### Prerequisites

- gpt-oss:120b must be loaded in Ollama (`ollama run gpt-oss:120b` to verify)
- No other GPU-heavy processes running (the model uses ~65 GB of 128 GB unified memory)

### Step 1: 1896 reference year (~48 colonies, ~4-5 hours)

Start here. This is the reference year with the most colonies, and gives immediate quality signal.

```bash
nohup python -u extraction_corpus.py --year 1896 > generated/corpus_1896.log 2>&1 &
```

**Check progress:**
```bash
tail -20 generated/corpus_1896.log
python extraction_corpus.py --report
```

### Step 2: Review 1896 results

After 1896 finishes, spot-check before committing to the full run:

```bash
# Quick quality report
python extraction_corpus.py --report

# Spot-check a few colonies
python review_extraction.py

# Look at quarantine rate — if >5% of records are quarantined,
# investigate before proceeding
```

### Step 3: Full corpus run (~8 days wall-clock)

The orchestrator auto-resumes from checkpoint, so it's safe across machine restarts.

```bash
nohup python -u extraction_corpus.py > generated/corpus_full.log 2>&1 &
```

It can be stopped and restarted at any time — Ctrl+C or kill the process. On restart, it skips all completed files.

**Monitor:**
```bash
tail -20 generated/corpus_full.log          # live log
python extraction_corpus.py --report         # summary stats
python monitor.py                            # live dashboard
```

**Retry failures:**
```bash
python extraction_corpus.py --retry-failed
```

### Corpus tier breakdown

| Tier | Size | Files | Time/file | Total |
|------|------|-------|-----------|-------|
| SKIP | < 500 B | 63 | — | — |
| SMALL | 500 B–5 KB | 196 | ~1 min | ~3 hr |
| STANDARD | 5–50 KB | 1,537 | ~5 min | ~128 hr |
| LARGE | 50–200 KB | 388 | ~8 min | ~52 hr |
| XLARGE | > 200 KB | 43 | ~15 min | ~11 hr |
| **Total** | | **2,227** | | **~194 hr (~8 days)** |

### After extraction: human review

Mandatory review targets (~200 files):
- First year of each colony (~133 files) — establishes colony-specific patterns
- All XLARGE files (~43 files)
- Any file where >10% of names fail source-text anchoring

```bash
python review_extraction.py      # interactive review CLI
```

### After review: Neo4j loading

Once extraction and review are complete, load into the graph:
- Only records that passed validation (not quarantined) and passed review (APPROVED or not reviewed)
- Stage 1 of the GraphRAG pipeline (see `GRAPHRAG_PIPELINE_DESIGN.md`)

---

## Model notes

| Model | Size | Speed | Chunking needed | Quality |
|-------|------|-------|-----------------|---------|
| gpt-oss:120b | 65 GB | ~41 tok/s | Yes (8K limit) | 100% all fields (v3 prompt) |
| qwen3-coder-next:q4_K_M | 52 GB | ~36 tok/s | No (single pass) | 100% recall, but leaves "ditto" unresolved |
| llama4:scout | 67 GB | untested | Likely | OOM in previous session |

Only one large model can be loaded at a time (128 GB total, models are 52–67 GB each).

---

## File inventory

| File | Purpose |
|------|---------|
| `extraction_ollama.py` | Main extraction script (codegen + JSON + chunked modes) |
| `extraction_batch.py` | Multi-year batch runner with cascading preamble stripping |
| `extraction_corpus.py` | **Full-corpus orchestrator** with tiers, checkpointing, validation |
| `validation.py` | **Source-text validation** — name/salary anchoring, anomaly detection |
| `review_extraction.py` | **Human review CLI** — APPROVE/REJECT/FLAG workflow |
| `monitor.py` | **Live progress monitor** |
| `benchmark_local_models.py` | Automated benchmarking against reference |
| `scaffold_neo4j.py` | Neo4j Stage 0 graph scaffolding |
| `BENCHMARK_RESULTS.md` | Prompt iteration log and model comparison |
| `GRAPHRAG_PIPELINE_DESIGN.md` | Full GraphRAG schema (Stages 0–4) |
| `test_data/gold_standard.json` | Gemini 3.0 Flash reference (44 officials, Sierra Leone 1896) |
| `test_data/sierra_leone_1896_test.txt` | Benchmark source text (5 depts, 88 lines) |
| `generated/sierra_leone_{year}_data_*.json` | Per-year Sierra Leone extraction output |
| `generated/corpus_state.json` | Full-corpus checkpoint state (created on first run) |
| `generated/review_state.json` | Human review state (created on first review) |
