#!/usr/bin/env python3
"""
Colonial Office List — History-Narrative Extraction Schema
==========================================================

Canonical record shapes for the History-narrative track
(HISTORY_NARRATIVE_EXTRACTION_PLAN.md). Used now as the deterministic record
shape (col_frame_histories.py) and later as the `response_model` for LLM
extraction (col_extract_histories.py), mirroring guides/schema.py's role for the
personnel track.

CRITICAL stance — the histories are *claims asserted by the Colonial Office*, not
objective fact. They are imperial self-narratives (e.g. Sierra Leone's
scare-quoted `"King" Naimbana`; New Zealand "discovered in 1642 by Tasman").
Therefore every extracted record:
  * attributes itself to the source: `asserted_by = "Colonial Office List"` with
    the `edition_years` it was printed in;
  * is flagged a claim, never a fact: `asserted_as_claim` is hard-coded True;
  * preserves the verbatim surface form (incl. scare-quotes) and a `source_span`
    back to the page;
  * promotes the colonial FRAMING to a first-class, queryable object rather than
    discarding it.

The Neo4j projection of these records (col_load_histories_neo4j.py) is documented
in NODE_SCHEMA / EDGE_SCHEMA below.
"""

from typing import Optional, Literal

from pydantic import BaseModel, Field

# Canonical vocabularies (the contract; detectors live in col_frame_histories.py).
FRAMING_CATEGORIES = [
    "discovery",            # "discovered", "uninhabited", "first settled" — erases prior presence
    "cession_acquisition",  # "ceded", "annexed", "took possession", "acquired"
    "conflict",             # "rebellion", "punitive", "pacified", "subdued", "war"
    "civilising",           # "natives", "tribes", "savage", "protection", "civilise"
    "sovereignty",          # "crown colony", "protectorate", "Her Majesty", "imperial"
]
ENTITY_TYPES = ["person", "place", "event"]


class EntityFraming(BaseModel):
    """One piece of loaded colonial framing, tied to a verbatim span."""
    framing_type: Literal["discovery", "cession_acquisition", "conflict",
                          "civilising", "sovereignty"] = Field(
        description="Imperial framing category this phrasing exhibits")
    loaded_terms: list[str] = Field(
        description="Verbatim trigger words, e.g. ['discovered','uninhabited']")
    verbatim_span: str = Field(
        description="Exact phrase/sentence carrying the framing, copied verbatim")
    char_start: int
    char_end: int
    confidence: float = Field(ge=0.0, le=1.0)


class HistoricalEntityMention(BaseModel):
    """One assertion of one historical entity inside one history version."""
    surface_text: str = Field(
        description='Name EXACTLY as written, incl. scare-quotes/titles, '
                    'e.g. \'"King" Naimbana\'')
    entity_type: Literal["person", "place", "event"]
    entity_subtype: Optional[str] = Field(
        default=None,
        description="e.g. governor/explorer/monarch/chief; river/settlement/"
                    "region/island; treaty/war/charter/annexation")
    source_span: str = Field(
        description="The enclosing clause/sentence, verbatim — the audit anchor")
    char_start: int
    char_end: int
    year_reference: Optional[int] = Field(
        default=None,
        description="A datable year tied to this mention if stated, e.g. 1788")
    asserted_as_claim: Literal[True] = Field(
        default=True,
        description="ALWAYS true — a Colonial-Office assertion, never a fact")
    framings: list[EntityFraming] = Field(
        default_factory=list,
        description="Framing(s) applied TO this entity (may be empty)")
    confidence: float = Field(ge=0.0, le=1.0)
    extractor: str = Field(
        default="deterministic_baseline",
        description="'deterministic_baseline' (Phase 0) or 'llm' (Phase C)")


class HistoryExtraction(BaseModel):
    """All entities + section-level framing for one distinct history version."""
    colony: str
    section_slug: str = "history"
    version_hash: str
    asserted_by: Literal["Colonial Office List"] = "Colonial Office List"
    edition_years: list[int] = Field(
        description="Every edition this version's text was printed in")
    entities: list[HistoricalEntityMention] = Field(default_factory=list)
    section_framings: list[EntityFraming] = Field(
        default_factory=list,
        description="Framing of the passage NOT tied to one entity "
                    "(e.g. a stand-alone 'uninhabited')")


# ---------------------------------------------------------------------------
# Neo4j projection (documented; loaded by col_load_histories_neo4j.py, Phase E)
# ---------------------------------------------------------------------------
NODE_SCHEMA = {
    "COL_HistoricalEntity": {
        "uri": "col:hentity/<type>/<slug>",
        "persistent": True,
        "props": ["entity_type", "canonical_label", "aliases", "entity_subtype",
                  "wikidata_qid", "wd_confidence", "pipeline_version",
                  "date_created", "quarantined"],
    },
    "COL_FramingType": {
        "uri": "col:framing/<slug>",
        "persistent": True,
        "props": ["slug", "description"],
    },
    "COL_HistoryVersion": {
        "uri": "col:hversion/<colony>/history/<version_hash>",
        "slice": True,
        "props": ["colony", "section_slug", "version_hash", "asserted_by",
                  "text", "edition_years", "first_edition_year",
                  "last_edition_year", "n_editions", "representative_source_file",
                  "char_start", "char_end", "intra_cluster_min_sim",
                  "source_flags", "quarantined"],
    },
    "COL_EntityMention": {
        "uri": "col:hmention/<hversion_tail>/<idx>",
        "slice": True,
        "props": ["surface_text", "entity_type", "entity_subtype", "source_span",
                  "char_start", "char_end", "year_reference", "asserted_by",
                  "asserted_as_claim", "edition_years", "confidence", "extractor",
                  "quarantined"],
    },
    "COL_FramingAnnotation": {
        "uri": "col:hframing/<hversion_tail>/<idx>",
        "slice": True,
        "props": ["framing_type", "loaded_terms", "verbatim_span", "char_start",
                  "char_end", "asserted_by", "edition_years", "confidence",
                  "extractor"],
    },
}

EDGE_SCHEMA = [
    "(COL_HistoryVersion)-[:OF_SECTION]->(COL_ReportSectionType {slug:'history'})",
    "(COL_HistoryVersion)-[:VERSION_IN]->(COL_TerritoryYear)",   # one per edition_year
    "(COL_HistoryVersion)-[:SAME_PROSE_AS]->(COL_NarrativeChunk)",
    "(COL_EntityMention)-[:IN_VERSION]->(COL_HistoryVersion)",
    "(COL_EntityMention)-[:MENTIONS]->(COL_HistoricalEntity)",
    "(COL_FramingAnnotation)-[:IN_VERSION]->(COL_HistoryVersion)",
    "(COL_FramingAnnotation)-[:OF_FRAMING]->(COL_FramingType)",
    "(COL_FramingAnnotation)-[:FRAMES]->(COL_HistoricalEntity)",  # optional
    "(COL_HistoricalEntity)-[:SAME_AS]->(WD_Person)",             # Phase D
    "(COL_HistoricalEntity)-[:IS_HISTORICAL_SELF_OF]->(COL_Person)",  # governor bridge
]

# Neo4j constraints/indexes (mirrors plan §4.4 and col_scaffold_neo4j.py).
CONSTRAINTS_CYPHER = """
CREATE CONSTRAINT col_hentity_uri    IF NOT EXISTS FOR (e:COL_HistoricalEntity)  REQUIRE e.uri IS UNIQUE;
CREATE CONSTRAINT col_framingtype_uri IF NOT EXISTS FOR (f:COL_FramingType)      REQUIRE f.uri IS UNIQUE;
CREATE CONSTRAINT col_hversion_uri   IF NOT EXISTS FOR (v:COL_HistoryVersion)    REQUIRE v.uri IS UNIQUE;
CREATE CONSTRAINT col_hmention_uri   IF NOT EXISTS FOR (m:COL_EntityMention)     REQUIRE m.uri IS UNIQUE;
CREATE CONSTRAINT col_hframing_uri   IF NOT EXISTS FOR (a:COL_FramingAnnotation) REQUIRE a.uri IS UNIQUE;
CREATE INDEX col_hentity_type  IF NOT EXISTS FOR (e:COL_HistoricalEntity)  ON (e.entity_type);
CREATE INDEX col_hentity_qid   IF NOT EXISTS FOR (e:COL_HistoricalEntity)  ON (e.wikidata_qid);
CREATE INDEX col_hversion_col  IF NOT EXISTS FOR (v:COL_HistoryVersion)    ON (v.colony, v.section_slug);
CREATE INDEX col_hframing_type IF NOT EXISTS FOR (a:COL_FramingAnnotation) ON (a.framing_type);
CREATE INDEX col_hmention_year IF NOT EXISTS FOR (m:COL_EntityMention)     ON (m.year_reference);
""".strip()


if __name__ == "__main__":
    # Smoke test: the schema validates and round-trips.
    ex = HistoryExtraction(
        colony="sierra_leone", version_hash="abc123", edition_years=[1925, 1927],
        entities=[HistoricalEntityMention(
            surface_text='"King" Naimbana', entity_type="person",
            entity_subtype="chief", source_span='ceded ... by "King" Naimbana',
            char_start=10, char_end=25, year_reference=1788, confidence=0.6,
            framings=[EntityFraming(
                framing_type="cession_acquisition", loaded_terms=["ceded"],
                verbatim_span="ceded to Great Britain", char_start=0, char_end=22,
                confidence=0.9)])])
    print(ex.model_dump_json(indent=2))
