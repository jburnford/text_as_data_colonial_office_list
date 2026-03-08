# Gambia — Extraction Status Report

**Date**: 11 February 2026
**Phase**: 2a (BWA Expansion)
**Pipeline**: `extraction/batch_extract.py` + Gemini 2.0 Flash

---

## Summary

| Metric | Value |
|--------|-------|
| Total files | 65 |
| Successful extractions | 59 |
| Skipped (already done) | 2 |
| Narrative-only | 4 |
| Errors | 0 |
| **Total officials extracted** | **4,600** |
| Coverage | 1867–1965 (61 years with data) |

---

## Known Issues

### Critical: Multi-Colony File Contamination

Two source files contain personnel data for other colonies mixed in with Gambia. The extraction picked up non-Gambia officials.

| Year | Officials | Problem | Action Needed |
|------|-----------|---------|---------------|
| **1883** | 254 | File contains Western Australia departments (Rottnest Prison, Water Police, Inspectors of Sheep, Diocese of Perth W.A.). Only ~35 are Gambia. | Filter to departments matching Gambia pattern; remove WA officials |
| **1928** | 255 | File contains Fiji departments (Education, Post and Telegraph, Transport, Works, Fiji Defence Force). Only ~91 are Gambia. | Filter to departments matching Gambia pattern; remove Fiji officials |

**Root cause**: The 1883 and 1928 source files in the corpus appear to be multi-colony concatenations. Gemini's section map correctly identified all sections, but the extraction prompt doesn't filter by colony — it extracts everything in the personnel sections.

**Fix approach**: Post-processing script to remove officials whose departments don't match known Gambia department patterns (e.g., departments containing "Gambia", "Protectorate", "West African Frontier Force", or matching the typical Gambia department list).

### Narrative-Only Files (No Personnel Extracted)

| Year | File Size | Likely Cause |
|------|-----------|-------------|
| **1886** | 23,258 bytes | Gemini classified all sections as narrative. File likely has personnel data that was misclassified. Should re-extract with `--force`. |
| **1946** | 42,527 bytes | Large file, likely has personnel data. Same pattern as Sierra Leone 1946. |
| **1948** | 30,631 bytes | Same pattern — narrative classification error. |
| **1966** | 646 bytes | Genuine stub — only a brief entry. Expected. |

**Fix approach**: Re-extract 1886, 1946, 1948 with `--force` flag. If still narrative-only, manually inspect the source files.

### Under-Counted Years

| Year | Officials | Issue |
|------|-----------|-------|
| **1878** | 7 | File is only 1,222 bytes — very small. Only "Ecclesiastical Establishment" and "Convict Department" sections found. The file may be a fragment (WEST_AFRICA_GAMBIA.txt — possibly a shared West Africa section, not Gambia-specific). |
| **1912** | 40 | Gemini section map failed (429 rate limit), fell back to regex. Regex only found 6 departments. Should re-extract with `--force`. |
| **1897** | 25 | Section map over-split into individual positions instead of departments. Lost some officials in tiny slices. |
| **1922** | 141 | One section ("Secretariat / Printing Branch") failed due to rate limiting — Gemini returned None. Lost ~10–15 officials. |

### Post-1952 Format Change

Years 1952–1965 show 16–32 officials per year, down from 67–181 in earlier decades. This is expected: the Colonial Office List format changed after 1951 to list only senior staff, not the full establishment. This is a known limitation across all colonies, not a data quality issue.

---

## Officials Per Year

```
1867:  13    1905:  74    1925: 181    1952:  22
1878:   7    1906:  75    1927:  92    1953:  16
1879:  40    1907:  72    1928: 255*   1954:  21
1880:  38    1908:  74    1929:  94    1955:  21
1883: 254*   1909:  77    1930:  93    1956:  23
1889:  30    1910:  77    1931:  88    1957:  24
1890:  32    1912:  40†   1932:  75    1958:  25
1894:  37    1913:  97    1933:  69    1959:  24
1896:  41    1914: 144    1934:  71    1960:  24
1897:  25†   1915: 170    1936:  70    1961:  24
1898:  42    1917: 130    1937:  71    1962:  23
1899:  93    1918: 129    1939:  73    1963:  30
1900:  46    1919: 128    1940:  67    1964:  32
              1920: 119    1949:  78    1965:  31
              1921: 142    1950:  81
              1922: 141†   1951:  82
              1923: 161
              1924: 172

* Multi-colony contamination — count includes non-Gambia officials
† Under-counted — rate limiting or section map issues
Missing: 1886, 1946, 1948 (narrative-only), 1966 (stub)
```

---

## Post-Processing TODO

1. **Filter 1883**: Remove Western Australia officials (departments with "Perth", "Rottnest", "Water Police", "Sheep", "Convict")
2. **Filter 1928**: Remove Fiji officials (departments with "Fiji", "Transport Department", "Stores Department")
3. **Re-extract 1886, 1946, 1948**: Run with `--force` flag
4. **Re-extract 1912**: Run with `--force` to get proper section map
5. **Validate department names**: Ensure all department suffixes are " - Gambia"
6. **Cross-check governor list**: Verify against RAG narrative sections
7. **Build `known_gaps.json`**: Document 1878 (fragment), 1966 (stub), narrative-only years

---

## Files Produced

```
extraction/gambia/
├── json/                   # 61 JSON files (gambia_1867.json ... gambia_1965.json)
├── generated/              # Python extraction scripts per year/section
├── rag/                    # Narrative sections for RAG indexing
├── section_maps/           # Gemini section maps per year
└── STATUS_REPORT.md        # This file
```
