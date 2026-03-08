# Sierra Leone Extraction — Status Report

**Date**: 11 February 2026
**Status**: COMPLETE (post-processing fixes applied)

---

## 1. Coverage Summary

| Metric | Value |
|--------|-------|
| Years extracted | 55 of 61 in corpus (90.2%) |
| Year range | 1878–1960 |
| Total records | 10,982 officials |
| Records with salary | 9,647 (87.8%) |
| Records with honors | 670 (6.1%) |
| Schema errors | 4 (0.04%) — all pre-existing salary inversions |
| Gold standard F1 | 98.8% (1896, 42-official benchmark) |

### Files Generated

| Directory | Files | Purpose |
|-----------|-------|---------|
| `json/` | 55 | Final extraction output (1 per year) |
| `generated/` | 685 | Python extraction scripts (per-section) |
| `rag/` | 1,174 | Narrative text sections for RAG indexing |
| `section_maps/` | 61 | Gemini section maps |

---

## 2. Year-by-Year Data

```
Year    N  Sal%   Scl  Hon  Vac  Notes
────────────────────────────────────────────
1878  108  93.5     0    3    8
1879   82  91.5     0    2   13
1880   89  93.3     0    3   13
1883   94  90.4     0    1   13
1888  142  91.5     0    2    0
1889  117  94.0     0    1    6
1894  147  93.9     0    3    3
1896  180  90.6     0    1    2  ← gold standard year
1898  203  96.6     0    1   21
1899  215  96.7     0    1    8
1900  236  95.8     0    4   21
1905  274  98.9     0    3    3
1906  290  97.9     0    7    3
1907  296  97.6     0    7    1
1908  315  98.4     0    6    5
1909  322  99.1     0    4    3
1910  380  96.1     0   12    2  ← peak year
1911  365  95.9     0    5    3
1912  221  98.2     0    5    4
1913  198 100.0     0    6    3
1914  236  97.0     0    6    4
1915  277 100.0     0    5   11
1917  266 100.0     0    5   10
1918  258 100.0     0    5    8
1919  246 100.0     0    5   11
1920  204  98.5     0    3   13
1921  269  98.9     2   25    4
1922  241  98.8     0    9   13
1923  212  99.1     0   10    5
1924  220  99.1    71   10    5  ← scales begin
1925  225  99.6    73   12    3
1927  309  98.4    90   31    6
1928  333  98.2    99   30    6
1929  353  98.6   104   35   11
1930  324  99.1   109   22   11
1931  367  98.9   106   31   10
1932   18 100.0     7    0    3  ⚠ TRUNCATED
1933  166  97.0    69   16   12
1934  155  94.8    65   18    7
1936  157  98.7    63   21    9
1937  170  96.5    64   19    5
1939  185  97.3    50   17    8
1940  192  99.0    58   16    9  ← scales end
1949  240  22.1   183   32    1  ← post-war scales
1950  271  22.1   188   31    7
1951  313  22.7   232   31    8
1952   38  89.5     3    9    2  ← format change
1953   54   0.0     0   16    5
1954   54   0.0     0   15    5
1955   45   0.0     0   14    0
1956   56   0.0     0    9    7
1957   61   0.0     0   15    4
1958   67   0.0     0   24    1
1959   65   0.0     0   23    3
1960   61   0.0     0   23    0
```

**Key**: N = officials, Sal% = with salary, Scl = salary-scale records, Hon = with honors, Vac = VACANT positions.

---

## 3. Post-Processing Fixes Applied

| # | Fix | Records | Years |
|---|-----|---------|-------|
| 1 | Removed 28 historical governors from "Governors since..." list | 28 removed | 1950 |
| 2 | Resolved salary scales A–F to numeric min/max ranges | 986 enriched | 1924–1940 |
| 3 | Fixed null-name records → VACANT | 8 fixed | 1900, 1930 |
| 4 | Fixed garbled governor name → Sir Arnold W. Hodson | 1 fixed | 1931 |
| 5 | Corrected OCR: Cardow→Cardew | 1 fixed | 1899 |
| 6 | Corrected OCR: Drawshtman→Draughtsman | 3 fixed | 1919 |
| 7 | Corrected OCR: Pritohard→Pritchard | 1 fixed | 1932 |
| 8 | Added truncation note to 1932 | metadata | 1932 |
| 9 | Added format-change note to 1952–1959 | metadata | 1952–1959 |

All fixes are in `fix_extractions.py` — re-runnable and idempotent.

---

## 4. Known Limitations

### 4a. 1932 Source Truncation (CRITICAL)

Only Railway and WAFF Battalion sections survive in the source text (329 lines vs ~900 expected). 18 of ~350 officials extracted. Requires re-OCR from the original ColonialOfficeList1932.pdf to recover.

### 4b. Post-1951 Format Change (DOCUMENTED)

The Colonial Office List itself changed scope after 1951. Post-1951 editions list only department heads and senior officials — not full civil establishments. Salary data disappears for most positions. This is a publication change, not a parsing error. Record counts drop from ~300 (1951) to 38–67 (1952–1959).

### 4c. Missing Years (28 gaps)

| Gap | Years | Likely Cause |
|-----|-------|-------------|
| 1881–82, 1884–87 | 6 | Not in OCR'd corpus |
| 1890–93, 1895, 1897 | 6 | Not in OCR'd corpus |
| 1901–04 | 4 | Not in OCR'd corpus |
| 1916 | 1 | Wartime publication gap? |
| 1926, 1935, 1938 | 3 | Not in OCR'd corpus |
| 1941–48 | 8 | WWII; 1946/1948 narrative-only |

### 4d. Unresolved Post-War Salary Scales (1949–1951)

Years 1949–1951 use salary scale designations (A, B, M.3, N.1, C.1, etc.) from a post-war system whose definitions differ from the 1924–1940 scales. These 603 records have scale codes but no resolved min/max. Salary coverage for these years is ~22%.

### 4e. Remaining Schema Errors (4 records)

Pre-existing salary_min > salary_max in 1899 (1), 1914 (2), 1917 (1). These are OCR artifacts in the source text and would need manual correction.

---

## 5. Data Highlights

### Civil Service Growth Trajectory

```
1878: ████████████ 108
1900: ████████████████████████████ 236
1910: █████████████████████████████████████████████ 380  ← peak
1920: ████████████████████████ 204
1931: ██████████████████████████████████████████████ 367
1950: ██████████████████████████████████ 271
1960: ████████ 61  (dept heads only)
```

### Salary Scale Distribution (1924–1940, resolved)

| Scale | Min £ | Max £ | Records | Share |
|-------|-------|-------|---------|-------|
| A | 400 | 920 | 594 | 36% |
| B | 400 | 960 | 546 | 34% |
| C | 450 | 920 | 249 | 15% |
| F | 400 | 500 | 150 | 9% |
| D | 360 | 460 | — | rare |
| E | 390 | 460 | — | rare |

### VACANT Positions

362 VACANT records across all years. Vacancy rates peak in the 1870s–1880s (~15%) and decline steadily to <3% by the 1930s, reflecting the maturation of colonial administration.
