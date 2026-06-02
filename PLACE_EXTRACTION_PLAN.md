# Place-Name Extraction → KG Geography (Geography Track)

**Status:** Phase 0-1 (deterministic foundation) **built & validated**; grounding +
KG load designed and staged.
**Relationship:** Extends the colony-reports work. Consumes the Phase-0
canonicalizer (`col_canonicalize_reports.py`); reuses the Wikidata-grounding stack
(`col_link_wikidata.py`, `wikidata-mcp`) for the staged grounding phase.

---

## 1. Goal

Extract every place-name *mention* across the corpus to flesh out the knowledge
graph's geography: a temporal **index** (place → the years/colonies it appears in,
to surface places appearing and growing in prominence over time), **KWIC**
concordance to ground/locate each place, and a **local-vs-external** judgement so
"London" in a Ceylon file isn't filed as a Ceylon village and "Singapore" is read
as a trading partner where it is one and a home colony where it is one.

These are the source's *references*, not asserted geographic fact; grounding to
coordinates is a later phase.

## 2. The disambiguation problem (and the four signals)

No single signal separates local toponyms from external references / trading
partners — cross-colony frequency alone fails (Galle is a Ceylon town but appears
in 22 colonies as an imperial coaling port). So **role is per (place, colony)**,
from four combined signals:

1. **Home share** — the colony holding the bulk of a place's mentions owns it
   (Colombo→Ceylon, Singapore→Straits, Port Louis→Mauritius are `local` there even
   though they also appear elsewhere as ports).
2. **Family / self** — the colony's own name or a federation sub-unit → `local`.
3. **Section context** — geography/population → leans local; trade/shipping → partner.
4. **Cross-colony ubiquity** — a place in many colonies with no home → external hub
   (London, Great Britain, England, Europe, India).

## 3. Detection (deterministic, report-content only)

Bounded to report content (before `roster_start_block`, misparses/dumps skipped) so
roster surnames aren't harvested as places. Candidates from:

- **Geographic cues** (high precision). Feature words that are PART of a name yield
  the FULL toponym — `Cape Coast`, `Cape of Good Hope`, `Port Louis`, `Mount
  Lavinia`, `St Lucia`, `Gambia River`, `Lake Victoria`; descriptive `district of
  X` / `island of X` yields the proper noun (`Kandy`, `Ceylon`).
- **Trade-direction cues** — `shipped to X`, `imports from X` → partner candidates.
- **Filtered capitalized spans** — proper nouns minus a noise filter: demonyms
  (Sinhalese, Dyaks), months, function words, administrative titles/ranks
  (Governor, President, Col, Sir), institutions, and **standalone generic feature
  words** (`hill`, `field`, `cape`, `island` alone are dropped; `Snake Hill`,
  `Christmas Island` are kept). Person-title spans are subtracted.

**Two-gazetteer validation:** a bare token is kept only if corroborated — it
appears with a cue somewhere, OR is a known colony / sub-unit / curated hub, OR is
strongly geography-concentrated in one colony (recovers bare local toponyms like
Galle without admitting recurring surnames/institutions, which cluster in
history/finance prose).

## 4. Outputs (built)

- `generated/places_index.json` — per place: `canonical`, `aliases`, `n_colonies`,
  `n_mentions_total`, `first_year`/`last_year`, `global_role`, `has_geo_cue`, and
  per colony `{years[], first/last_year, n_mentions, sections, trade_cues, role,
  kwic[]}` (≤3 KWIC lines/colony, from distinct editions). `asserted_by` stamped.
- `generated/places_index.csv` — browsable: place, n_colonies, mentions, span, role.

## 5. Validation (corpus, deterministic foundation)

| Metric | Value |
|---|---|
| Distinct places kept | 3,821 |
| Role mix | 3,455 local · 37 trading_partner · 70 external_reference · 259 ambiguous |
| Top external hubs | London (139 colonies), Great Britain (136), United Kingdom (124), England (123), Europe, India, France |
| Your test cases | **Cape Coast** (657 mentions, Gold Coast) and **Cape of Good Hope** (local in its home colony) both captured |
| Home-role fixes | Colombo→local in Ceylon, Singapore→local in Straits, Port Louis→local in Mauritius |
| Generic terms | standalone `hill`/`field`/`cape`/`island` excluded; `Cape Coast`/`Gambia River` kept |
| Temporal index | 274 places first appear ≥1946 (Belize City, Brunei Town, Hong Kong Island, Tongatapu) |
| KWIC | e.g. "Lagos to [Cape Coast] is 288 [miles]"; London-from-Ceylon shown in banking/shipping context |

Known recall gap: bare-only toponyms never appearing with a cue, in a gazetteer, or
concentrated in one geography section are missed — the gazetteer-grounding phase
(GeoNames/Wikidata) is the proper tool to close this, and will also drop the
residual non-place candidates (a few surnames/institutions) deterministic rules let
through. I/O note: the FS intermittently times out a handful of the newest-edition
files; reads retry once then skip (≤20 files), logged.

## 6. Staged (designed, not built)

| Phase | File | Reuse |
|---|---|---|
| 2 — Ground places to Wikidata/GeoNames (coords); coordinate-vs-colony-bbox local/external test; confirm/repair roles | `col_ground_places.py` | `col_link_wikidata.py` (matcher/confidence), `wikidata-mcp`, `princely_states_wikidata.json`, `qid_resolutions.csv` |
| 3 — KG load: `COL_Place` (canonical, QID, coords) + `COL_PlaceMention` (per colony-year, role, KWIC); edges `MENTIONED_IN`→`COL_TerritoryYear`, `LOCATED_IN`/`TRADES_WITH`/`REFERENCES`, `SAME_AS`→WD | `col_load_places_neo4j.py` | `col_load_neo4j.py`, `col_scaffold_neo4j.py` |
| opt — LLM NER pass for hard cases / disambiguation | `col_extract_places_llm.py` | `extraction_corpus.py`, `extraction_instructor.py` |

## 7. Usage
```
python col_extract_places.py            # write index + csv
python col_extract_places.py --stats    # summary only
python col_extract_places.py --place galle   # inspect one place
```
