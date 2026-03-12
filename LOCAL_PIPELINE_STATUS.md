# Local Extraction Pipeline — Development Status

**Last updated:** 22 February 2026
**Machine:** Project DIGITS (NVIDIA GB10, 128 GB unified memory)
**Model:** gpt-oss:120b via Ollama

---

## Summary

We have a working, benchmarked local extraction pipeline that converts OCR-parsed Colonial Office List text into structured JSON. On the Sierra Leone 1896 test case, the pipeline achieves **100% accuracy across all fields** against a Gemini 3.0 Flash reference.

**Full corpus extraction is IN PROGRESS** — 239/2,164 files (11%), 32,416 officials, 99.65% pass rate, zero failures.

---

## ACTIVE BACKGROUND PROCESSES

**These processes are running unattended and must not be interrupted.**

### 1. Corpus extraction (PID 137627)

```
Started:  19 Feb 2026, 16:47 UTC
Command:  nohup python -u extraction_corpus.py > generated/corpus_full.log 2>&1 &
PID:      137627
Log:      generated/corpus_full.log
State:    generated/corpus_state.json
```

- Processes all ~2,164 colony-year files (excluding 63 SKIP-tier stubs)
- Checkpoints to `corpus_state.json` after every file — safe to restart
- SIGINT-safe: Ctrl+C finishes current file, saves state, exits cleanly
- To restart if it dies: `nohup python -u extraction_corpus.py > generated/corpus_full.log 2>&1 &`
- Current rate: ~3.5 files/hour, estimated ~22 days total

**Check progress:**
```bash
ps -p 137627 -o etime                                          # uptime
tail -20 generated/corpus_full.log                             # live log
python -c "
import json
with open('generated/corpus_state.json') as f:
    state = json.load(f)
done = state.get('completed', {})
failed = state.get('failed', {})
total_off = sum(v.get('total_officials',0) for v in done.values())
total_q = sum(v.get('quarantined_officials',0) for v in done.values())
print(f'Completed: {len(done)}/2164 ({len(done)/2164*100:.1f}%)')
print(f'Failed: {len(failed)}')
print(f'Officials: {total_off:,} ({total_q} quarantined)')
"
```

### 2. Auto-push to GitHub (PID 161301)

```
Started:  21 Feb 2026, 17:42 UTC
Command:  nohup bash auto_push.sh > generated/auto_push.log 2>&1 &
PID:      161301
Log:      generated/auto_push.log
```

- Commits and pushes new extraction JSONs to GitHub every hour
- Stages: `generated/*_data_*.json`, `generated/*_quarantined_*.json`, `generated/corpus_state.json`
- To restart if it dies: `nohup bash auto_push.sh > generated/auto_push.log 2>&1 &`

**Check status:**
```bash
ps -p 161301                          # is it running?
tail -5 generated/auto_push.log       # last push
git log --oneline -5                  # recent commits
```

### If the machine reboots

Both processes will need to be restarted manually:

```bash
cd /home/jic823/Documents/text_as_data_colonial_office_list

# 1. Restart extraction (auto-resumes from checkpoint)
nohup python -u extraction_corpus.py > generated/corpus_full.log 2>&1 &

# 2. Restart auto-push
nohup bash auto_push.sh > generated/auto_push.log 2>&1 &
```

### GPU usage

The extraction uses gpt-oss:120b (~65 GB) via Ollama. **Do not load other large models or run GPU-heavy tasks while the extraction is running.** Ollama will keep the model loaded between requests. If the model gets evicted, the extraction script will reload it automatically (adds ~60s delay).

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

## Current extraction progress

**Started:** 19 Feb 2026 (1896 reference year), expanded to full corpus 20 Feb 2026

| Milestone | Status |
|-----------|--------|
| 1896 reference year (48 colonies) | **Complete** — 9,483 officials, 15 quarantined, 0 failures |
| Full corpus (2,164 files) | **In progress** — 239 done (11%), ~22 days remaining |

### Completed years so far

1867, 1877, 1878, 1879, 1880, 1883, 1886, 1896 — across 61 unique colonies.

### Quality metrics (cumulative)

| Metric | Value |
|--------|-------|
| Total officials extracted | 32,416 |
| Quarantined | 114 (0.35%) |
| Pass rate | 99.65% |
| Failed files | 0 |

### Known issues

- **Fiji 1896** — source file contains Ceylon + Cape of Good Hope content (upstream OCR/parsing). 1,524 officials extracted but ~11% are from wrong colonies. Flagged as XLARGE/mandatory review.
- **Source duplication** — some colony files repeat text blocks (OCR artefact). Deduplication in `extract_chunked()` handles this automatically.
- **Repetition collapse** — model occasionally fills output with repeated tokens on complex chunks (e.g. Barbados Mounted Police). Chunk is skipped, pipeline continues.
- **Late-era salaries** — 1950+ em-dash format sometimes yields null salaries. Low priority.

---

## Next steps

### 1. Neo4j loading (can start now)

32K+ officials are ready to load. Stage 0 scaffold (Years, Territories, TerritoryYear slices) already exists. Next: Stage 1 — Official nodes linked to TerritoryYear slices. Can load incrementally as extraction continues.

- See `GRAPHRAG_PIPELINE_DESIGN.md` for full schema
- Neo4j Docker: `bolt://localhost:7687`, auth: `neo4j/colonial_office`

### 2. Human review (after extraction completes)

```bash
python review_extraction.py      # interactive review CLI
```

Mandatory review targets (~200 files):
- First year of each colony (~133 files)
- All XLARGE files (~27 files)
- Any file where >10% of names fail source-text anchoring

### 3. Retry failures (if any)

```bash
python extraction_corpus.py --retry-failed
```

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
| `auto_push.sh` | Hourly git commit+push of extraction results |
| `generated/{colony}_{year}_data_gpt-oss_120b.json` | Extraction output (passed validation) |
| `generated/{colony}_{year}_quarantined_gpt-oss_120b.json` | Quarantined records (failed validation) |
| `generated/corpus_state.json` | Full-corpus checkpoint state |
| `generated/corpus_full.log` | Current extraction run log |
| `generated/auto_push.log` | Auto-push log |
| `generated/review_state.json` | Human review state (created on first review) |
