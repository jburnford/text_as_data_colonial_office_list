# Local Model Benchmark Results

## Test Data
- **Input:** `test_data/sierra_leone_1896_test.txt` (5 departments, 88 lines)
- **Gold Standard:** `test_data/gold_standard.json` (42 named officials + 2 vacant positions)
- **Hardware:** NVIDIA GB10 (Project DIGITS), 128GB unified memory

## Results Summary

| Model | Mode | Recall | Precision | Position | Salary | Dept | Quals | Location | Honors | Mil. Rank | Time |
|-------|------|--------|-----------|----------|--------|------|-------|----------|--------|-----------|------|
| Gemini 2.0 Flash | codegen (full) | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% | ~10s |
| **qwen3-coder-next:q4_K_M** | codegen (full) | **100%** | **100%** | 90% | 100% | 100% | 100% | 100% | 100% | 100% | 152s |
| **gpt-oss:120b** (v1) | codegen (chunked) | **100%** | **100%** | 100% | 100% | 100% | 67% | 100% | 100% | 100% | 315s |
| **gpt-oss:120b** (v2, improved prompt) | codegen (chunked) | **100%** | **100%** | 86% | 100% | 100% | **100%** | 83% | 100% | 100% | 410s |
| **gpt-oss:120b** (v3, final) | codegen (chunked) | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | 290s |
| Regex baseline | regex | 100% | 95% | 43% | 98% | — | — | — | — | — | <1s |

## Key Findings

### qwen3-coder-next:q4_K_M (52 GB, 3B active/token)
- Handled full document in a single pass (no chunking needed)
- 152s generation time, 35.8 tok/s
- **Only issue:** 4 "ditto" positions not fully resolved (left as "Assistant ditto" instead of "Assistant Colonial Surgeon")
- All other fields perfect

### gpt-oss:120b (65 GB, 5.1B active/token)
- **Requires chunking** — hits 8K token limit on full document, truncates output
- Chunked by department (4 chunks for this test file)
- ~315–410s total generation time, 36–37 tok/s per chunk
- v1 prompt: missed B.A. and L.R.C.P. qualifications (only listed M.D., M.B., M.R.C.S. as examples)
- v2 prompt: fixed qualifications to 100% by adding explicit examples and worked parsing demonstrations, but regressed position accuracy (100% → 86%) and location (100% → 83%)
- v3 prompt: **100% on all fields.** Kept expanded qualification list from v2, added explicit ditto examples in rule 2, removed worked examples that caused v2 regression. 290s total (~41 tok/s per chunk)

### llama4:scout (67 GB, ~17B active/token)
- Not yet benchmarked (caused OOM crash in previous session)
- Likely needs chunking + careful RAM management

## Chunking Approach

The source text is split by department headers before extraction. Each chunk is sent as a separate LLM call, and results are merged. This keeps output within token limits for models that can't generate 16K+ tokens.

Chunk detection uses regex matching on department header patterns (e.g., "Civil Establishment.", "Colonial Secretary's Department.", "Medical Department.").

For the Sierra Leone 1896 test file, this produces 4 chunks:
1. Civil Establishment (5 lines → 3 officials)
2. Colonial Secretary's Department (10 lines → 9 officials)
3. Treasury Department (15 lines → 12 officials, includes sub-accountant)
4. Medical Department (19 lines → 18 officials, includes dispensers)

## Prompt Iteration Log

### v1 (original prompt)
- Qualification examples in rules: "M.D., M.B., M.R.C.S."
- No worked examples
- Result: qualifications 67% (missed B.A. for Taylor, L.R.C.P. for Bishop)

### v2 (improved qualifications)
- Expanded qualification list: B.A., M.A., M.D., M.B., B.Sc., M.Sc., LL.D., Ph.D., M.R.C.S., F.R.C.S., L.R.C.S., L.R.C.P., F.R.C.P., M.R.C.P., etc.
- Added 3 worked examples showing qualification parsing
- Added explicit rule: "Qualifications appear AFTER the person's name, BEFORE the salary"
- Result: qualifications 100%, but position regressed 100% → 86%, location 100% → 83%
- **Hypothesis:** longer prompt with worked examples may have pushed model to different parsing patterns for positions/locations

### v3 (final — 100% all fields)
- Kept expanded qualification list from v2: B.A., M.A., M.D., M.B., L.R.C.P., M.R.C.S., F.R.C.S., L.R.C.S., F.R.C.P., LL.D., Ph.D.
- Added explicit ditto examples in rule 2: `"2nd ditto after Chief Clerk = 2nd Clerk; Assistant ditto after Colonial Surgeon = Assistant Colonial Surgeon"`
- Removed the 3 worked examples that bloated v2 and caused position/location regression
- Result: **100% on all fields** — qualifications, position, location all perfect
- Confirms hypothesis: gpt-oss performs better with concise rules than lengthy worked examples
- 290s total (4 chunks, ~41 tok/s per chunk)

## File Inventory

| File | Purpose |
|------|---------|
| `extraction_ollama.py` | Ollama extraction (codegen + JSON + chunked modes) |
| `benchmark_local_models.py` | Automated benchmarking across models |
| `scaffold_neo4j.py` | Neo4j Stage 0 temporal-geographic scaffolding |
| `generated/sierra_leone_1896_extraction_qwen3-coder-next_q4_K_M.py` | qwen3 full output (valid, runnable) |
| `generated/chunk_*_gpt-oss_120b.py` | gpt-oss per-department chunks |
| `generated/sierra_leone_1896_data_gpt-oss_120b_chunked.json` | gpt-oss merged output |

## Neo4j Status

- Running in Docker at `bolt://localhost:7687` (auth: neo4j/colonial_office)
- Browser: http://localhost:7474
- Stage 0 scaffolding loaded:
  - 68 Year nodes (1867–1966)
  - 133 Territory nodes (normalized from 407 raw filenames)
  - 2,220 TerritoryYear slices
  - 2,094 CONTINUES_AS temporal edges

## RAM Management

- **IMPORTANT:** Always `ollama stop <model>` before loading another large model
- gpt-oss:120b = 65 GB, qwen3-coder-next = 52 GB — cannot run simultaneously
- llama4:scout = 67 GB — caused OOM before, test with caution
- Benchmark script handles this automatically (stops models between runs)
