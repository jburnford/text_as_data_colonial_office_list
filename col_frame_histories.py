#!/usr/bin/env python3
"""
COL History Track (Phase 0 cont.): Framing baseline + entity candidates
=======================================================================

Consumes the deduplicated history versions (col_segment_histories.py) and emits,
per DISTINCT version (not per edition — the 81%-verbatim dividend), two
deterministic, auditable record sets:

  1. **Framing annotations** (the first-class research object). A curated lexicon
     of imperial framing markers — discovery / cession_acquisition / conflict /
     civilising / sovereignty — is matched against each version; every hit yields
     a COL_FramingAnnotation with the verbatim loaded term(s), the enclosing
     sentence (verbatim_span), char offsets, and source attribution. This makes
     "how did the Colonial Office narrate conquest, land, and indigenous peoples?"
     directly queryable. It is a transparent BASELINE the later LLM pass refines
     (e.g. disambiguating a metaphorical "war" from a real one).

  2. **Entity candidates** (a recall floor + taxonomy seed). Titled persons,
     gazetteer place references (to other colonies), and datable year references.
     Deliberately high-precision / limited-recall — flagged extractor=
     "deterministic_baseline"; the LLM NER pass (col_extract_histories.py)
     supersedes it. Used to seed the entity taxonomy at scale (derive-from-scale).

EVERYTHING is attributed, never asserted as fact: each record carries
`asserted_by="Colonial Office List"` and the `edition_years` it was printed in.
The verbatim surface forms — including scare-quotes like `"King" Naimbana` — are
preserved, because the framing is the signal.

Outputs:
    generated/histories_framed/<colony>.json          (versions + framings + entities)
    taxonomy/framing_taxonomy.json                     (with --emit-taxonomy)

Usage:
    python col_frame_histories.py                      # frame all segmented colonies
    python col_frame_histories.py --stats              # framing prevalence summary
    python col_frame_histories.py --emit-taxonomy      # (re)write taxonomy/framing_taxonomy.json
    python col_frame_histories.py --colony sierra_leone
"""

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import col_canonicalize_reports as canon

PIPELINE_VERSION = "col_frame_histories/0.1"
SEGMENTED_DIR = "generated/histories_segmented"
FRAMED_DIR = "generated/histories_framed"

FRAMING_CONFIDENCE = 0.65   # deterministic lexical match; LLM refines context
PERSON_CONFIDENCE = 0.45
PLACE_CONFIDENCE = 0.40

# ---------------------------------------------------------------------------
# Framing lexicon — curated markers of imperial perspective (verbatim triggers).
# Overlap across categories is intentional: one sentence may carry several frames.
# ---------------------------------------------------------------------------
FRAMING_LEXICON = {
    "discovery": [
        r"discover(?:ed|y)", r"first visited", r"first sighted", r"first traced",
        r"first settled", r"uninhabited", r"unexplored", r"unknown to europeans",
    ],
    "cession_acquisition": [
        r"ceded", r"cession", r"annex(?:ed|ation)", r"took possession",
        r"taken possession", r"acquired", r"acquisition", r"purchased",
        r"came under british", r"placed under british", r"transferred to",
        r"brought under british", r"became a british", r"ceded to",
    ],
    "conflict": [
        r"rebellion", r"rebels?", r"insurrection", r"\brising\b", r"mutiny",
        r"punitive", r"expedition", r"massacre", r"hostilities", r"subdued",
        r"pacif\w+", r"suppress\w+", r"\bwar\b", r"conquest", r"conquered",
        r"defeated", r"revolt", r"disturbances", r"native war",
    ],
    "civilising": [
        r"civilis\w+", r"civiliz\w+", r"savages?", r"barbarous", r"heathen",
        r"\bprotection\b", r"backward", r"primitive", r"natives?\b",
        r"native population", r"native tribes?", r"tribes?\b", r"aboriginal",
        r"uncivilised", r"semi-civilised",
    ],
    "sovereignty": [
        r"sovereignty", r"crown colony", r"protectorate", r"\bmandate\b",
        r"her majesty", r"his majesty", r"\bimperial\b", r"british rule",
        r"british crown", r"under british protection", r"british sovereignty",
    ],
}
FRAMING_RE = {cat: [re.compile(p, re.I) for p in pats]
              for cat, pats in FRAMING_LEXICON.items()}

# ---------------------------------------------------------------------------
# Entity-candidate detectors (high precision, limited recall — a baseline).
# ---------------------------------------------------------------------------
_PERSON_TITLE = (r"Sir|Lord|Lady|Captain|Capt\.|Admiral|General|Colonel|Col\.|"
                 r"Commodore|Major|Lieutenant|Lieut\.|Mr|Dr|Duke|Earl|Count|"
                 r"Baron|King|Queen|Emperor|Sultan|Rajah|Rajah|Governor|"
                 r"President|Commander|Bishop|Rev\.?|Chief")
# Title may be scare-quoted ("King" Naimbana) — the scare-quote is preserved.
RE_PERSON = re.compile(
    rf'["“]?\b({_PERSON_TITLE})\b["”]?\.?\s+'
    r"([A-Z][a-z]+(?:\s+[A-Z][a-z'’.]+){0,2})")
RE_YEAR = re.compile(r"\b1[5-9]\d{2}\b")
RE_CAPWORD = re.compile(r"\b([A-Z][a-z]{2,})\b")
# Function words / sentence-starters that follow a title across a sentence break
# ("Governor. In ...") or a bare title ("Governor Mr") — not personal names.
NAME_STOPWORDS = {"In", "The", "A", "An", "His", "Her", "On", "At", "By", "For",
                  "It", "This", "That", "These", "Those", "As", "And", "But",
                  "He", "She", "They", "Of", "From", "Was", "Is", "Were", "Are",
                  "Their", "Its", "Our", "All", "No", "Not", "Mr", "Mrs", "Dr"}

_SUBTYPE = {
    "king": "monarch", "queen": "monarch", "emperor": "monarch",
    "sultan": "monarch", "rajah": "monarch", "chief": "chief",
    "governor": "governor", "president": "official", "bishop": "cleric",
    "rev": "cleric", "captain": "military", "capt": "military",
    "admiral": "military", "general": "military", "colonel": "military",
    "col": "military", "commodore": "military", "major": "military",
    "lieutenant": "military", "lieut": "military", "commander": "military",
}


def enclosing_sentence(text, start, end):
    left = text.rfind(". ", 0, start)
    ls = 0 if left == -1 else left + 2
    right = text.find(". ", end)
    rs = len(text) if right == -1 else right + 1
    return text[ls:rs].strip(), ls, rs


def detect_framing(text, edition_years):
    grouped = {}  # (cat, sentence_start) -> annotation dict
    for cat, regexes in FRAMING_RE.items():
        for rx in regexes:
            for m in rx.finditer(text):
                sent, ss, se = enclosing_sentence(text, m.start(), m.end())
                key = (cat, ss)
                a = grouped.get(key)
                if a is None:
                    a = grouped[key] = {
                        "framing_type": cat, "loaded_terms": set(),
                        "verbatim_span": sent, "char_start": ss, "char_end": se,
                        "confidence": FRAMING_CONFIDENCE,
                        "asserted_by": "Colonial Office List",
                        "edition_years": edition_years,
                        "extractor": "deterministic_baseline",
                    }
                a["loaded_terms"].add(m.group(0).lower())
    out = []
    for a in grouped.values():
        a["loaded_terms"] = sorted(a["loaded_terms"])
        out.append(a)
    out.sort(key=lambda x: x["char_start"])
    return out


def detect_entities(text, edition_years, gazetteer, self_slug):
    mentions = []
    seen = set()
    # Persons (titled)
    for m in RE_PERSON.finditer(text):
        surface = m.group(0).strip()
        if m.group(2).split()[0] in NAME_STOPWORDS:
            continue  # title followed by a function word / sentence start, not a name
        if surface.lower() in seen:
            continue
        seen.add(surface.lower())
        title = re.sub(r'[^a-z.]', "", m.group(1).lower()).rstrip(".")
        sent, ss, se = enclosing_sentence(text, m.start(), m.end())
        yr = RE_YEAR.search(sent)
        mentions.append({
            "surface_text": surface, "entity_type": "person",
            "entity_subtype": _SUBTYPE.get(title), "source_span": sent,
            "char_start": m.start(), "char_end": m.end(),
            "year_reference": int(yr.group(0)) if yr else None,
            "asserted_by": "Colonial Office List", "asserted_as_claim": True,
            "edition_years": edition_years, "confidence": PERSON_CONFIDENCE,
            "extractor": "deterministic_baseline",
        })
    # Places: capitalized words whose normalized form names another colony
    # (high precision; the histories' cross-colony references). Real place NER is
    # the LLM pass; this is a baseline that also wires up inter-colony links.
    for m in RE_CAPWORD.finditer(text):
        nm = canon._norm(m.group(1))
        if nm in gazetteer and nm != self_slug and ("place:" + nm) not in seen:
            seen.add("place:" + nm)
            sent, ss, se = enclosing_sentence(text, m.start(), m.end())
            mentions.append({
                "surface_text": m.group(1), "entity_type": "place",
                "entity_subtype": "territory", "source_span": sent,
                "char_start": m.start(), "char_end": m.end(),
                "year_reference": None, "asserted_by": "Colonial Office List",
                "asserted_as_claim": True, "edition_years": edition_years,
                "confidence": PLACE_CONFIDENCE,
                "extractor": "deterministic_baseline",
            })
    return mentions


def frame_colony(data, gazetteer):
    self_slug = data["colony"]
    for v in data["versions"]:
        if v.get("quarantined"):
            v["framings"] = []
            v["entity_candidates"] = []
            v["year_references"] = []
            continue
        text = v["text"]
        v["framings"] = detect_framing(text, v["edition_years"])
        v["entity_candidates"] = detect_entities(text, v["edition_years"],
                                                 gazetteer, self_slug)
        v["year_references"] = sorted({int(y) for y in RE_YEAR.findall(text)})
    return data


def main():
    ap = argparse.ArgumentParser(description="Framing baseline + entity candidates")
    ap.add_argument("--colony", help="process only this colony slug")
    ap.add_argument("--stats", action="store_true", help="prevalence summary, no write")
    ap.add_argument("--emit-taxonomy", action="store_true",
                    help="(re)write taxonomy/framing_taxonomy.json from the corpus")
    ap.add_argument("--seg-dir", default=SEGMENTED_DIR)
    ap.add_argument("--out-dir", default=FRAMED_DIR)
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    gazetteer = canon.build_gazetteer(canon.list_corpus_files(root))
    seg_dir = root / args.seg_dir
    files = sorted(seg_dir.glob("*.json"))
    if args.colony:
        files = [f for f in files if f.stem == args.colony]
    if not files:
        print(f"no segmented colony files in {args.seg_dir}/ — run "
              f"col_segment_histories.py first")
        return

    # term-level + category-level prevalence, counted over DISTINCT versions
    cat_versions = Counter()      # category -> n versions using it
    term_versions = defaultdict(Counter)  # category -> Counter(term -> n versions)
    n_versions = 0
    n_colonies_using = Counter()  # category -> n colonies using it
    out_dir = root / args.out_dir

    for f in files:
        data = json.loads(f.read_text(encoding="utf-8"))
        data = frame_colony(data, gazetteer)
        colony_cats = set()
        for v in data["versions"]:
            if v.get("quarantined"):
                continue
            n_versions += 1
            cats_here = {a["framing_type"] for a in v["framings"]}
            for cat in cats_here:
                cat_versions[cat] += 1
                colony_cats.add(cat)
            for a in v["framings"]:
                for t in a["loaded_terms"]:
                    term_versions[a["framing_type"]][t] += 1
        for cat in colony_cats:
            n_colonies_using[cat] += 1
        if not (args.stats or args.emit_taxonomy):
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / f.name).write_text(
                json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    n_colonies = len(files)
    print(f"\n=== Framing prevalence ({n_colonies} colonies, {n_versions} distinct versions) ===")
    print(f"{'frame':20s} {'%versions':>9s} {'%colonies':>10s}")
    for cat in FRAMING_LEXICON:
        pv = 100 * cat_versions[cat] // n_versions if n_versions else 0
        pc = 100 * n_colonies_using[cat] // n_colonies if n_colonies else 0
        print(f"  {cat:18s} {pv:8d}% {pc:9d}%")

    if not (args.stats or args.emit_taxonomy):
        print(f"\nwrote {n_colonies} framed colony files under {args.out_dir}/")

    if args.emit_taxonomy:
        tax = {
            "version": "0.1",
            "generated": date.today().isoformat(),
            "status": "DRAFT",
            "description": ("Imperial framing categories detected in Colonial "
                            "Office List History sections. Counts are over "
                            "DISTINCT history versions (the 81%-verbatim repeats "
                            "collapsed). These describe the SOURCE's perspective, "
                            "not historical fact."),
            "pipeline_version": PIPELINE_VERSION,
            "framing_types": [],
        }
        for cat in FRAMING_LEXICON:
            members = [{"raw": t, "count": n, "confidence": "HIGH", "method": "rule"}
                       for t, n in term_versions[cat].most_common()]
            tax["framing_types"].append({
                "id": f"frame_{cat}",
                "uri": f"col:framing/{cat}",
                "canonical_name": cat,
                "n_versions": cat_versions[cat],
                "n_colonies": n_colonies_using[cat],
                "members": members,
                "reviewer_decision": None,
            })
        out_path = root / "taxonomy" / "framing_taxonomy.json"
        out_path.write_text(json.dumps(tax, indent=2, ensure_ascii=False),
                            encoding="utf-8")
        print(f"\nwrote taxonomy/framing_taxonomy.json "
              f"({sum(len(t['members']) for t in tax['framing_types'])} terms)")


if __name__ == "__main__":
    main()
