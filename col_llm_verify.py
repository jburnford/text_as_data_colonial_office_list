"""
COL Layer 2: LLM Career Verification
======================================

Matches LLM-identified career chains (from Gemini narrative analysis)
against existing COL_Official nodes in Neo4j. Produces:
  - Edge audit: which POSSIBLE_MATCH edges are confirmed by the LLM
  - Missing link report: careers LLM found that our pipeline missed
  - Hallucination report: LLM claims that don't match graph reality
  - Training labels: verified (official_a, official_b, label) for ML scorer

Input: JSON file with career records:
[
  {"name": "Twynam, W. C.", "colony": "Ceylon", "stints": [
    {"years": [1867], "position": "Asst Govt Agent, Manaar"},
    {"years": [1879, 1880, 1883], "position": "Govt Agent, Northern Province"}
  ]},
  ...
]

Usage:
    python col_llm_verify.py llm_careers/ceylon.json
    python col_llm_verify.py llm_careers/ceylon.json --dry-run
    python col_llm_verify.py llm_careers/ceylon.json --write-notes
    python col_llm_verify.py llm_careers/ceylon.json --create-missing

Requires:
    pip install neo4j sentence-transformers
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

try:
    from neo4j import GraphDatabase
except ImportError:
    print("ERROR: neo4j driver not installed. Run: pip install neo4j")
    sys.exit(1)

# =============================================================================
# CONFIGURATION
# =============================================================================

REPO_DIR = Path(__file__).parent
OUTPUT_DIR = REPO_DIR / "llm_output"

# Similarity threshold for position matching
POSITION_SIM_THRESHOLD = 0.45
# Year tolerance for matching LLM stints to graph officials
YEAR_TOLERANCE = 3
# Name match: require surname exact, initials compatible
NAME_MATCH_STRICT = True


def _load_dotenv():
    """Load .env file from repo root."""
    env_path = REPO_DIR / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())


_load_dotenv()

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://206.12.90.118:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "")


# =============================================================================
# EMBEDDING SUPPORT (lazy-loaded)
# =============================================================================

_model = None


def _get_model():
    """Lazy-load sentence-transformers model."""
    global _model
    if _model is None:
        try:
            from sentence_transformers import SentenceTransformer
            _model = SentenceTransformer("all-MiniLM-L6-v2")
            print("  Loaded sentence-transformers model")
        except ImportError:
            print("  WARNING: sentence-transformers not installed, position similarity disabled")
            return None
    return _model


def position_similarity(text_a: str, text_b: str) -> float:
    """Compute cosine similarity between two position descriptions."""
    model = _get_model()
    if model is None or not text_a or not text_b:
        return 0.0
    import numpy as np
    embeddings = model.encode([text_a, text_b], normalize_embeddings=True)
    return float(np.dot(embeddings[0], embeddings[1]))


# =============================================================================
# GRAPH QUERIES
# =============================================================================

def fetch_officials_by_surname(session, surname: str, colony: str) -> list[dict]:
    """Fetch COL_Officials matching surname in a colony, with PersonRecord details."""
    result = session.run("""
        MATCH (o:COL_Official)
        WHERE toLower(o.name) CONTAINS toLower($surname)
          AND o.colony = $colony
        OPTIONAL MATCH (pr:COL_PersonRecord)-[:RECORD_OF]->(o)
        WHERE (pr.quarantined IS NULL OR pr.quarantined = false)
        WITH o, collect({
            year: pr.year,
            position: pr.position_raw,
            department: pr.department,
            honours: pr.honours,
            given_names: pr.given_names
        }) AS records
        RETURN o.id AS id, o.name AS name, o.colony AS colony,
               o.first_year AS first_year, o.last_year AS last_year,
               o.editions AS editions, records
        ORDER BY o.first_year
    """, surname=surname, colony=colony)
    return [dict(r) for r in result]


def fetch_existing_edges(session, official_ids: list[str]) -> list[dict]:
    """Fetch POSSIBLE_MATCH edges between a set of official IDs."""
    if len(official_ids) < 2:
        return []
    result = session.run("""
        MATCH (a:COL_Official)-[r:POSSIBLE_MATCH]-(b:COL_Official)
        WHERE a.id IN $ids AND b.id IN $ids
          AND id(a) < id(b)
        RETURN a.id AS a_id, b.id AS b_id,
               r.uncertainty AS uncertainty,
               r.domain_match AS domain_match,
               r.method AS method
    """, ids=official_ids)
    return [dict(r) for r in result]


def create_missing_edge(session, a_id: str, b_id: str, source: str):
    """Create a POSSIBLE_MATCH edge flagged as LLM-identified."""
    session.run("""
        MATCH (a:COL_Official {id: $a_id}), (b:COL_Official {id: $b_id})
        WHERE NOT EXISTS {
            MATCH (a)-[:POSSIBLE_MATCH]-(b)
        }
        CREATE (a)-[:POSSIBLE_MATCH {
            uncertainty: 0.15,
            method: 'llm_verified',
            source: $source,
            score_version: 'llm_1.0',
            date_created: $today
        }]->(b)
    """, a_id=a_id, b_id=b_id, source=source, today=date.today().isoformat())


def write_llm_notes(session, official_id: str, notes: str):
    """Write LLM-derived notes to a COL_Official node."""
    session.run("""
        MATCH (o:COL_Official {id: $id})
        SET o.llm_notes = $notes
    """, id=official_id, notes=notes)


# =============================================================================
# NAME PARSING
# =============================================================================

def parse_surname(name: str) -> str:
    """Extract surname from 'Surname, Initials' format."""
    if "," in name:
        return name.split(",")[0].strip()
    # Space-separated: last token is surname? No — COL uses Surname, Given
    # Just return the whole thing if no comma
    return name.strip()


def parse_initials(name: str) -> str:
    """Extract initials/given names from 'Surname, Initials' format."""
    if "," in name:
        return name.split(",", 1)[1].strip()
    return ""


def names_compatible(llm_name: str, graph_name: str) -> bool:
    """Check if LLM career name matches a graph official name."""
    llm_surname = parse_surname(llm_name).lower()
    graph_surname = parse_surname(graph_name).lower()

    # Surname must match
    if llm_surname != graph_surname:
        # Try substring match for hyphenated/variant surnames
        if llm_surname not in graph_surname and graph_surname not in llm_surname:
            return False

    # Check initials compatibility if both have given names
    llm_given = parse_initials(llm_name)
    graph_given = parse_initials(graph_name)

    if not llm_given or not graph_given:
        return True  # bare surname matches anything

    try:
        from col_normalize_names import initials_compatible, clean_given_names
        return initials_compatible(
            clean_given_names(llm_given),
            clean_given_names(graph_given)
        )
    except ImportError:
        # Fallback: compare first initials
        llm_init = llm_given.strip()[0].upper() if llm_given.strip() else ""
        graph_init = graph_given.strip()[0].upper() if graph_given.strip() else ""
        if llm_init and graph_init:
            return llm_init == graph_init
        return True


# =============================================================================
# MATCHING ENGINE
# =============================================================================

def match_stint_to_officials(stint: dict, officials: list[dict]) -> list[dict]:
    """
    Match a single LLM stint to candidate COL_Officials.

    Returns list of (official, score, details) sorted by score descending.
    """
    stint_years = set(stint.get("years", []))
    stint_position = stint.get("position", "")
    if not stint_years:
        return []

    stint_min = min(stint_years)
    stint_max = max(stint_years)

    candidates = []
    for off in officials:
        first_year = off.get("first_year", 9999)
        last_year = off.get("last_year", 0)

        # Year overlap or proximity check
        year_overlap = len(stint_years & set(range(first_year, last_year + 1)))
        year_gap = max(0, stint_min - last_year, first_year - stint_max)

        if year_gap > YEAR_TOLERANCE and year_overlap == 0:
            continue

        # Position similarity
        records = off.get("records", [])
        best_pos_sim = 0.0
        best_record_pos = ""
        for rec in records:
            rec_pos = rec.get("position") or ""
            if rec_pos and stint_position:
                sim = position_similarity(stint_position, rec_pos)
                if sim > best_pos_sim:
                    best_pos_sim = sim
                    best_record_pos = rec_pos

        # Score: year overlap dominates, position similarity helps disambiguate
        score = year_overlap * 2.0 + best_pos_sim - year_gap * 0.5

        candidates.append({
            "official": off,
            "score": score,
            "year_overlap": year_overlap,
            "year_gap": year_gap,
            "position_sim": best_pos_sim,
            "best_record_pos": best_record_pos,
        })

    candidates.sort(key=lambda x: x["score"], reverse=True)
    return candidates


def match_career_to_graph(career: dict, session) -> dict:
    """
    Match an LLM career (name + stints) against COL_Official nodes.

    Returns a match report with:
      - matched_stints: list of (stint, best_official, score)
      - unmatched_stints: stints with no graph match
      - matched_official_ids: set of official IDs matched
    """
    name = career["name"]
    colony = career["colony"]
    surname = parse_surname(name)

    # Fetch all officials with matching surname in this colony
    officials = fetch_officials_by_surname(session, surname, colony)

    # Filter by name compatibility (initials)
    compatible_officials = [o for o in officials if names_compatible(name, o["name"])]

    report = {
        "career_name": name,
        "colony": colony,
        "num_stints": len(career.get("stints", [])),
        "officials_found": len(compatible_officials),
        "matched_stints": [],
        "unmatched_stints": [],
        "matched_official_ids": set(),
        "all_officials": compatible_officials,
    }

    # Track which officials are already claimed
    claimed_officials = set()

    for stint in career.get("stints", []):
        candidates = match_stint_to_officials(stint, compatible_officials)

        # Filter out already-claimed officials (prefer best unclaimed)
        best = None
        for c in candidates:
            oid = c["official"]["id"]
            if oid not in claimed_officials:
                best = c
                break

        if best and best["score"] > 0:
            claimed_officials.add(best["official"]["id"])
            report["matched_stints"].append({
                "stint": stint,
                "official_id": best["official"]["id"],
                "official_name": best["official"]["name"],
                "official_years": f"{best['official']['first_year']}-{best['official']['last_year']}",
                "score": best["score"],
                "year_overlap": best["year_overlap"],
                "year_gap": best["year_gap"],
                "position_sim": best["position_sim"],
                "best_record_pos": best["best_record_pos"],
            })
            report["matched_official_ids"].add(best["official"]["id"])
        else:
            report["unmatched_stints"].append({
                "stint": stint,
                "reason": "no_match" if not candidates else "low_score",
                "best_score": candidates[0]["score"] if candidates else None,
            })

    return report


# =============================================================================
# AUDIT ENGINE
# =============================================================================

def audit_career(report: dict, session) -> dict:
    """
    Audit a matched career against existing graph edges.

    Returns:
      - confirmed_edges: existing POSSIBLE_MATCH edges that LLM agrees with
      - missing_edges: official pairs LLM says are same person but no edge exists
      - hallucinations: issues detected
    """
    matched_ids = list(report["matched_official_ids"])
    existing_edges = fetch_existing_edges(session, matched_ids)
    existing_pairs = {(e["a_id"], e["b_id"]) for e in existing_edges}
    existing_pairs |= {(e["b_id"], e["a_id"]) for e in existing_edges}

    confirmed = []
    missing = []
    hallucinations = []

    # Check all consecutive matched stints — LLM says these are the same person
    matched_stints = report["matched_stints"]
    for i in range(len(matched_stints) - 1):
        a_id = matched_stints[i]["official_id"]
        b_id = matched_stints[i + 1]["official_id"]

        if a_id == b_id:
            continue  # same official node, no edge needed

        pair = (a_id, b_id)
        reverse = (b_id, a_id)

        if pair in existing_pairs or reverse in existing_pairs:
            # Find the edge details
            edge = next(
                (e for e in existing_edges
                 if (e["a_id"], e["b_id"]) in {pair, reverse}),
                None
            )
            confirmed.append({
                "a_id": a_id,
                "b_id": b_id,
                "a_name": matched_stints[i]["official_name"],
                "b_name": matched_stints[i + 1]["official_name"],
                "a_years": matched_stints[i]["official_years"],
                "b_years": matched_stints[i + 1]["official_years"],
                "uncertainty": edge["uncertainty"] if edge else None,
                "method": edge["method"] if edge else None,
            })
        else:
            missing.append({
                "a_id": a_id,
                "b_id": b_id,
                "a_name": matched_stints[i]["official_name"],
                "b_name": matched_stints[i + 1]["official_name"],
                "a_years": matched_stints[i]["official_years"],
                "b_years": matched_stints[i + 1]["official_years"],
                "a_position": matched_stints[i].get("best_record_pos", ""),
                "b_position": matched_stints[i + 1].get("best_record_pos", ""),
            })

    # Check for hallucinations: unmatched stints
    for um in report["unmatched_stints"]:
        stint = um["stint"]
        hallucinations.append({
            "type": "unmatched_stint",
            "career_name": report["career_name"],
            "colony": report["colony"],
            "years": stint.get("years", []),
            "position": stint.get("position", ""),
            "reason": um["reason"],
            "best_score": um.get("best_score"),
        })

    # Check for year mismatches in matched stints
    for ms in matched_stints:
        stint = ms["stint"]
        stint_years = set(stint.get("years", []))
        off_years = ms["official_years"]
        if off_years and "-" in off_years:
            fy, ly = off_years.split("-")
            off_range = set(range(int(fy), int(ly) + 1))
            if stint_years and not stint_years & off_range:
                gap = ms["year_gap"]
                if gap > YEAR_TOLERANCE:
                    hallucinations.append({
                        "type": "year_mismatch",
                        "career_name": report["career_name"],
                        "official_id": ms["official_id"],
                        "llm_years": sorted(stint_years),
                        "graph_years": off_years,
                        "gap": gap,
                    })

    return {
        "career_name": report["career_name"],
        "colony": report["colony"],
        "confirmed_edges": confirmed,
        "missing_edges": missing,
        "hallucinations": hallucinations,
    }


# =============================================================================
# OUTPUT
# =============================================================================

def write_verification_report(colony: str, match_reports: list, audit_results: list):
    """Write human-readable verification report."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    report_path = OUTPUT_DIR / f"{colony}_verification.txt"

    total_careers = len(match_reports)
    total_stints = sum(r["num_stints"] for r in match_reports)
    total_matched = sum(len(r["matched_stints"]) for r in match_reports)
    total_unmatched = sum(len(r["unmatched_stints"]) for r in match_reports)
    total_confirmed = sum(len(a["confirmed_edges"]) for a in audit_results)
    total_missing = sum(len(a["missing_edges"]) for a in audit_results)
    total_hallucinations = sum(len(a["hallucinations"]) for a in audit_results)

    lines = []
    lines.append(f"LLM Career Verification Report: {colony}")
    lines.append("=" * 60)
    lines.append(f"Date: {date.today().isoformat()}")
    lines.append(f"Careers analyzed: {total_careers}")
    lines.append(f"Total stints: {total_stints}")
    lines.append(f"Stints matched to graph: {total_matched} ({total_matched/max(total_stints,1)*100:.1f}%)")
    lines.append(f"Stints unmatched: {total_unmatched}")
    lines.append(f"Edges confirmed: {total_confirmed}")
    lines.append(f"Missing edges found: {total_missing}")
    lines.append(f"Hallucinations flagged: {total_hallucinations}")
    lines.append("")

    # Per-career details
    for mr, ar in zip(match_reports, audit_results):
        lines.append(f"\n--- {mr['career_name']} ({mr['colony']}) ---")
        lines.append(f"  Officials found in graph: {mr['officials_found']}")
        lines.append(f"  Stints matched: {len(mr['matched_stints'])}/{mr['num_stints']}")

        for ms in mr["matched_stints"]:
            stint = ms["stint"]
            years_str = ",".join(str(y) for y in stint.get("years", []))
            lines.append(f"    [{years_str}] {stint.get('position', '?')}")
            lines.append(f"      -> {ms['official_id']} ({ms['official_years']}) sim={ms['position_sim']:.2f}")
            if ms.get("best_record_pos"):
                lines.append(f"         graph pos: {ms['best_record_pos']}")

        if ar["confirmed_edges"]:
            lines.append(f"  CONFIRMED edges ({len(ar['confirmed_edges'])}):")
            for ce in ar["confirmed_edges"]:
                lines.append(f"    {ce['a_id']} ({ce['a_years']}) -> {ce['b_id']} ({ce['b_years']}) unc={ce['uncertainty']}")

        if ar["missing_edges"]:
            lines.append(f"  MISSING edges ({len(ar['missing_edges'])}):")
            for me in ar["missing_edges"]:
                lines.append(f"    {me['a_id']} ({me['a_years']}) -> {me['b_id']} ({me['b_years']})")
                if me.get("a_position") or me.get("b_position"):
                    lines.append(f"      positions: {me.get('a_position', '?')} -> {me.get('b_position', '?')}")

        if ar["hallucinations"]:
            lines.append(f"  ISSUES ({len(ar['hallucinations'])}):")
            for h in ar["hallucinations"]:
                if h["type"] == "unmatched_stint":
                    lines.append(f"    No graph match: years={h['years']} pos='{h['position']}' ({h['reason']})")
                elif h["type"] == "year_mismatch":
                    lines.append(f"    Year mismatch: LLM={h['llm_years']} graph={h['graph_years']} gap={h['gap']}")

    with open(report_path, "w") as f:
        f.write("\n".join(lines))
    print(f"  Report written: {report_path}")


def write_confirmed_csv(colony: str, audit_results: list):
    """Write confirmed edges as training data CSV."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    csv_path = OUTPUT_DIR / f"{colony}_confirmed.csv"
    rows = []
    for ar in audit_results:
        for ce in ar["confirmed_edges"]:
            rows.append({
                "official_a_id": ce["a_id"],
                "official_b_id": ce["b_id"],
                "label": 1,
                "source": f"llm_{colony}",
                "uncertainty": ce.get("uncertainty", ""),
                "career_name": ar["career_name"],
            })
    if rows:
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"  Confirmed CSV: {csv_path} ({len(rows)} rows)")
    else:
        print(f"  No confirmed edges to write")


def write_missing_links_csv(colony: str, audit_results: list):
    """Write missing link edges CSV."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    csv_path = OUTPUT_DIR / f"{colony}_missing_links.csv"
    rows = []
    for ar in audit_results:
        for me in ar["missing_edges"]:
            rows.append({
                "official_a_id": me["a_id"],
                "official_b_id": me["b_id"],
                "career_name": ar["career_name"],
                "colony": ar["colony"],
                "a_years": me["a_years"],
                "b_years": me["b_years"],
                "a_position": me.get("a_position", ""),
                "b_position": me.get("b_position", ""),
            })
    if rows:
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"  Missing links CSV: {csv_path} ({len(rows)} rows)")
    else:
        print(f"  No missing links found")


def write_hallucinations_csv(colony: str, audit_results: list):
    """Write hallucination report CSV."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    csv_path = OUTPUT_DIR / f"{colony}_hallucinations.csv"
    rows = []
    for ar in audit_results:
        for h in ar["hallucinations"]:
            rows.append({
                "type": h["type"],
                "career_name": ar["career_name"],
                "colony": ar["colony"],
                "details": json.dumps({k: v for k, v in h.items()
                                       if k not in ("type", "career_name", "colony")}),
            })
    if rows:
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"  Hallucinations CSV: {csv_path} ({len(rows)} rows)")
    else:
        print(f"  No hallucinations flagged")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Verify LLM career chains against Neo4j graph")
    parser.add_argument("input_file", help="JSON file with LLM career records")
    parser.add_argument("--dry-run", action="store_true", help="Match only, no graph writes")
    parser.add_argument("--write-notes", action="store_true",
                        help="Write career notes to COL_Official nodes")
    parser.add_argument("--create-missing", action="store_true",
                        help="Create POSSIBLE_MATCH edges for missing links")
    parser.add_argument("--colony", help="Override colony name (default: from JSON)")
    args = parser.parse_args()

    # Load careers
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"ERROR: File not found: {input_path}")
        sys.exit(1)

    with open(input_path) as f:
        careers = json.load(f)

    if not isinstance(careers, list):
        print("ERROR: JSON must be a list of career objects")
        sys.exit(1)

    # Override colony if specified
    if args.colony:
        for c in careers:
            c["colony"] = args.colony

    # Determine colony name for output files
    colonies = {c.get("colony", "unknown") for c in careers}
    colony_slug = "_".join(sorted(colonies)).lower().replace(" ", "_")

    print(f"LLM Career Verification")
    print(f"  Input: {input_path}")
    print(f"  Careers: {len(careers)}")
    print(f"  Colonies: {', '.join(sorted(colonies))}")
    print()

    # Connect to Neo4j
    if not NEO4J_PASSWORD:
        print("ERROR: Set NEO4J_PASSWORD environment variable")
        sys.exit(1)

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    match_reports = []
    audit_results = []

    with driver.session() as session:
        # Phase 1: Match careers to graph
        print("Phase 1: Matching careers to graph...")
        for i, career in enumerate(careers):
            name = career.get("name", "?")
            colony = career.get("colony", "?")
            n_stints = len(career.get("stints", []))
            print(f"  [{i+1}/{len(careers)}] {name} ({colony}, {n_stints} stints)")

            report = match_career_to_graph(career, session)
            match_reports.append(report)

            matched = len(report["matched_stints"])
            unmatched = len(report["unmatched_stints"])
            print(f"    -> {matched} matched, {unmatched} unmatched, "
                  f"{report['officials_found']} officials in graph")

        # Phase 2: Audit edges
        print(f"\nPhase 2: Auditing edges...")
        for report in match_reports:
            audit = audit_career(report, session)
            audit_results.append(audit)

        # Phase 3: Write outputs
        print(f"\nPhase 3: Writing outputs...")
        write_verification_report(colony_slug, match_reports, audit_results)
        write_confirmed_csv(colony_slug, audit_results)
        write_missing_links_csv(colony_slug, audit_results)
        write_hallucinations_csv(colony_slug, audit_results)

        # Phase 4: Optional graph writes
        if args.create_missing and not args.dry_run:
            print(f"\nPhase 4: Creating missing edges...")
            created = 0
            for ar in audit_results:
                for me in ar["missing_edges"]:
                    create_missing_edge(session, me["a_id"], me["b_id"],
                                        f"llm_{colony_slug}")
                    created += 1
            print(f"  Created {created} missing POSSIBLE_MATCH edges")

        if args.write_notes and not args.dry_run:
            print(f"\nPhase 4b: Writing career notes...")
            notes_written = 0
            for mr in match_reports:
                if len(mr["matched_stints"]) < 2:
                    continue
                # Build career summary
                positions = []
                for ms in mr["matched_stints"]:
                    stint = ms["stint"]
                    years = stint.get("years", [])
                    pos = stint.get("position", "?")
                    year_str = f"{min(years)}-{max(years)}" if years else "?"
                    positions.append(f"{pos} ({year_str})")
                note = f"LLM career: {' -> '.join(positions)}"
                # Write to first official
                first_id = mr["matched_stints"][0]["official_id"]
                write_llm_notes(session, first_id, note)
                notes_written += 1
            print(f"  Wrote notes to {notes_written} officials")

    driver.close()

    # Summary
    total_confirmed = sum(len(a["confirmed_edges"]) for a in audit_results)
    total_missing = sum(len(a["missing_edges"]) for a in audit_results)
    total_matched = sum(len(r["matched_stints"]) for r in match_reports)
    total_stints = sum(r["num_stints"] for r in match_reports)
    total_hallucinations = sum(len(a["hallucinations"]) for a in audit_results)

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"  Graph match rate: {total_matched}/{total_stints} stints "
          f"({total_matched/max(total_stints,1)*100:.1f}%)")
    print(f"  Confirmed edges: {total_confirmed}")
    print(f"  Missing edges found: {total_missing}")
    print(f"  Hallucinations: {total_hallucinations}")
    print(f"  Output: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
