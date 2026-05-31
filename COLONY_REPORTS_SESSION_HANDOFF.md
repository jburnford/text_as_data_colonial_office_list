# Colony Reports Track — Session Handoff

**Purpose:** capture the state of the colony-annual-report extraction plan and,
candidly, *how reliable each part is*, so the next session can do a full review
without re-trusting anything blindly.

**Deliverable so far:** `COLONY_REPORTS_EXTRACTION_PLAN.md` (a planning document
only — no extraction code written yet).
**Branch:** `claude/repo-file-structure-w7jxq`.

---

## 1. What the plan proposes (one-paragraph summary)

Extract the semi-structured annual-report content (finance, trade, population,
area, shipping + narrative) that opens each colony entry, alongside the existing
personnel KG. New persistent nodes (`COL_IndicatorType`, `COL_CommodityType`,
`COL_ReportSectionType`) and slice nodes (`COL_ColonyReport`, `COL_Observation`,
`COL_TradeFlow`, `COL_NarrativeChunk`), following the existing persistent+slice /
provenance / `col_*` conventions. Two tracks: structured statistics (deterministic
table parse where clean, LLM for prose/broken tables) and narrative embedding.
Phased 0→H, schema frozen after a pilot gold standard.

---

## 2. ⚠️ Reliability caveat — read this first

This plan was written by an agent that **repeatedly produced confident,
plausible-sounding numbers and "findings" that turned out to be fabricated or
mis-measured**, and corrected them only on explicit re-checking. The user caught
several; self-review caught more. **Do not trust any quantitative claim in the
plan that is not re-verified.** Treat the plan's *structure and approach* as the
durable contribution and its *specific statistics* as needing audit.

### Errors that were made and fixed during this session (so they aren't re-trusted)
- File count stated as ~5,300 → actually **2,946** colony `.txt` files (compared a
  whole-repo grep against a scoped git count).
- Finding 2.5 percentages were wrong *and* drove a false conclusion
  ("regex covers at most ⅓"). Corrected: **90% of files have proper `|---|`
  tables**, so table detection is largely reliable; only *headings* are
  heterogeneous (52% `*bold*`, 28% `###`).
- "1898 Jamaica = 57-word fragment" — false; it's a full 7,189-word report. The
  real empty file is `1958/jamaica.txt`; real truncated one is `1917/AUSTRALIA.txt`.
- An entire analysis of **`1871_manual_parsed/CANADA.txt` — which does not exist**
  (no 1871 edition). Nearly committed; discarded.
- "33 single-line blob files" — actually **1** (`1958/barbados.txt`).
- "Pervasive Australia/state double-representation" — real overlap is **2 years**
  (1908, 1917).

### Therefore, for next session
- Re-derive every number in the plan from the data before relying on it.
- Prefer small, single-purpose verification commands; **watch for shell errors
  that mask empty output** (several fabrications came from misreading errored
  greps/seds on non-existent files).

---

## 3. Claims in the plan and their current verification status

| Claim | Status | How to re-check |
|---|---|---|
| 2,946 colony `.txt` files | **verified** | `git ls-files '*_manual_parsed/*.txt' \| wc -l` |
| 90% have `\|---\|` tables; 52% `*bold*`; 28% `###` | **verified** (git grep -l) | `git grep -l '^\|[-: ]*---' -- '*_manual_parsed/*.txt' \| wc -l` etc. |
| Size span 0–212,392 w; median ~4,120; >5,000w files median 72 pipe rows | **verified** (python sweep) | re-run the word/pipe count sweep |
| Empty `1958/jamaica.txt`; truncated `1917/AUSTRALIA.txt` | **verified** | `wc -w` each |
| Canada 15,817 w (1879) → 31,304 (1890) vs Jamaica ~5–7k | **verified** | `wc -w` per file |
| Australia state-files→aggregate handoff, overlap only 1908 & 1917 | **verified** (per-dir loop) | exact-filename existence loop per year |
| Dominion of Canada 144–320 pipe rows/edition | **verified** | `grep -c ' \| '` per file |
| **Cross-edition redundancy** (rolling window; census years recur) | **verified** | `grep -oE '^\| 18..'` across Jamaica editions |
| **OCR drift example:** 1881 census total 670,705 (ed1897) vs 580,804 (ed1898/1900), components identical | **verified** | `grep -E '^\| 1881' 189{7,8}/JAMAICA.txt` + 1900 |
| "50–70% of each file is report content" | **NOT measured** (hedged in plan) | needs a measured narrative-vs-roster line split |
| Section vocabulary list (Situation/History/Finance/…) | **partially** — from a few large colonies | sample widely incl. small/African/Pacific |
| Currency/unit variety (£/Rs/HK$, L suffix, etc.) | **observed**, not enumerated | corpus sweep of currency tokens |

---

## 4. The OCR-numbers philosophy (new this session — the important idea)

**Trust trends, not points.** Individual OCR'd digits are unreliable; the plan now
treats numbers as noisy observations and relies on the corpus's *intrinsic
redundancy*:

- Successive editions republish a **rolling window** of prior years, and census
  years (1861/1871/1881…) recur in **every** edition → most figures are read
  **3–10+ times** independently.
- **Verified demonstration:** Jamaica's 1881 census row has identical components
  across the 1897/1898/1900 editions but the *total* OCR'd as 670,705 (1897) vs
  580,804 (1898, 1900). The outlier is exposed two ways: **majority vote** and
  **component-sum check**.

Plan changes made for this:
- New design principle in §3 ("trust trends, not points") with the worked example.
- Finding §2.6 notes the redundancy as the saving grace.
- Track A **step 5: cross-edition reconciliation** — group `COL_Observation` by
  (colony, indicator, observation_year); derive consensus value, dispersion,
  agreement-confidence, and outlier flags **as separate annotations, never
  collapsing or computing on ingest**. Lives in Phase D
  (`col_reconcile_observations.py`).
- Validation/viz guidance: plot series with uncertainty / robust(median) series,
  not single points.

**Open design questions for next session:**
- Consensus rule per indicator type (median for continuous; mode for counts;
  how to treat ranges like "1896-7").
- How dispersion/confidence should gate inclusion in published trend charts.
- Whether to expose every raw read in Neo4j or only reads + a derived
  consensus node (modeling choice with query-cost implications).

---

## 5. Suggested agenda for the full review (next session)

1. **Audit §3 table above** — re-verify each "verified" claim independently;
   actually measure the two "NOT measured / partial" ones.
2. **Schema sign-off** — freeze node/edge names (§4 of the plan), especially the
   `COL_Observation` ↔ `COL_ColonyReport` attachment (note the resolved bug:
   `OBSERVED_FOR` keyed on observation-year is unattachable because
   `COL_TerritoryYear` exists only for edition years).
3. **Reconciliation model** — settle the open questions in §4 above.
4. **Pilot scope** — confirm the Phase-B gold-standard file set spans the
   size×decade matrix incl. a federation and a degenerate file.
5. **Phase-0 canonicalizer** — decide build vs. reuse; define the
   heading/table-recall metric and a labelled sample.
6. **Sampling gaps** — deliberately read African, Pacific, and Caribbean small
   colonies (sampling so far skewed to Jamaica/Ceylon/HK + federations).

---

## 6. Commit trail (this branch, newest last)

- `fa1ec57` initial plan
- `283b8da` / `6d28730` source-format corrections (prose vs tables; all eras)
- `846fb29` reframed around md/txt heterogeneity + Phase 0
- `191a80e` fixed count/percentage errors + the `OBSERVED_FOR` schema flaw
- `5601090` / `1f3c60d` colony-size & decade variation; corrected degenerate-file
  stats
- `6e92dcf` verified federation finding; dropped fabricated 1871/blob material
- (this session) OCR-redundancy principle + cross-edition reconciliation step +
  this handoff doc
