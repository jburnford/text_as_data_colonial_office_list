#!/usr/bin/env python3
"""
COL Geography Track (Phase 0-1): Place-name extraction, KWIC + temporal index
=============================================================================

Extracts place-name *mentions* from the report content of every colony-year file
to flesh out the knowledge graph's geography. Deterministic (no LLM): geographic
cue patterns + filtered capitalized spans, bounded to report content (before the
personnel roster, misparses skipped) so we harvest places, not roster surnames.

Three outputs the geography work needs:
  1. **Temporal index** — place -> {colony -> {years, sections, n_mentions, role}},
     plus global ubiquity. Surfaces places appearing / growing in prominence over
     time, and the heavy cross-edition repetition.
  2. **KWIC concordance** — a few keyword-in-context lines per (place, colony),
     captured once per distinct edition text, to ground/disambiguate each place.
  3. **Role heuristic** — per (place, colony): local / trading_partner /
     external_reference / ambiguous, from THREE signals because no single one
     suffices (Galle is a Ceylon town BUT appears in 22 colonies as a coaling
     port): cross-colony ubiquity + section context + grammatical cue. Role is
     per-(place, colony), never global — Singapore is local in the Straits, a
     trading partner in Ceylon. These are the source's references, not asserted
     geographic fact; grounding to Wikidata/GeoNames coordinates is a later phase.

Outputs:
    generated/places_index.json    (temporal index + roles + KWIC)
    generated/places_index.csv     (compact: place, n_colonies, mentions, span, role)

Usage:
    python col_extract_places.py            # extract, write index + csv
    python col_extract_places.py --stats    # summary only
    python col_extract_places.py --place galle   # inspect one place
"""

import argparse
import csv
import json
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import col_canonicalize_reports as canon

PIPELINE_VERSION = "col_extract_places/0.1"
MIN_TOTAL_MENTIONS = 3      # prune one-off OCR garble (unless geo-cued)
KWIC_PER_COLONY = 3         # concordance lines kept per (place, colony)
KWIC_WINDOW = 55            # chars of context each side
HUB_UBIQUITY = 25           # appears in >= this many colonies => external hub
LOCAL_UBIQUITY = 6          # appears in <= this many colonies => leans local
SKIP_FLAGS = {"volume_dump", "multi_colony_misparse", "appendix_contamination"}

# Section slugs that lean LOCAL (the colony's own geography) vs PARTNER (trade).
LOCAL_SECTIONS = {"geography", "population"}
TRADE_SECTIONS = {"trade", "shipping"}

# ---------------------------------------------------------------------------
# Noise filters — peoples/languages/religions, calendar, institution & function
# words are not places. Kept lowercase.
# ---------------------------------------------------------------------------
DEMONYMS = {
    "sinhalese", "singhalese", "tamil", "tamils", "moor", "moors", "malay", "malays",
    "european", "europeans", "burgher", "burghers", "eurasian", "eurasians",
    "chinese", "indian", "indians", "hindu", "hindus", "buddhist", "buddhists",
    "christian", "christians", "catholic", "catholics", "protestant", "protestants",
    "mohammedan", "mohammedans", "muslim", "muslims", "moslem", "arab", "arabs",
    "african", "africans", "english", "englishmen", "dutch", "portuguese", "french",
    "german", "germans", "spanish", "italian", "native", "natives", "aboriginal",
    "aborigines", "asiatic", "asiatics", "creole", "creoles", "negro", "negroes",
    "kaffir", "kaffirs", "kafir", "boer", "boers", "europeans", "polynesian",
    "melanesian", "papuan", "papuans", "jew", "jews", "jewish", "americans",
    "american", "russian", "japanese", "siamese", "burmese", "persian",
}
MONTHS = {"january", "february", "march", "april", "may", "june", "july", "august",
          "september", "october", "november", "december",
          "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
INSTITUTION = {
    "council", "office", "department", "government", "establishment", "colony",
    "company", "bank", "church", "society", "committee", "board", "court", "college",
    "school", "hospital", "prison", "railway", "service", "commission", "protectorate",
    "settlement", "dominion", "empire", "crown", "majesty", "parliament", "assembly",
    "legislature", "legislative", "executive", "treasury", "customs", "secretary",
    "governor", "governors", "administration", "act", "ordinance", "charter",
    "constitution", "regiment", "battalion", "police", "militia", "volunteers",
    "university", "mission", "gazette", "list", "edition", "table", "total", "rs",
    "year", "january", "association", "department", "department",
}
FUNCTION_WORDS = {
    "the", "a", "an", "this", "that", "these", "those", "according", "among",
    "although", "during", "since", "while", "when", "where", "which", "after",
    "before", "until", "between", "from", "into", "upon", "under", "over", "about",
    "his", "her", "its", "their", "our", "all", "no", "not", "and", "but", "for",
    "with", "without", "such", "they", "there", "here", "then", "thus", "also",
    "in", "on", "at", "by", "to", "of", "as", "is", "was", "were", "are", "be",
    "it", "he", "she", "we", "i", "first", "second", "chief", "principal", "north",
    "south", "east", "west", "northern", "southern", "eastern", "western", "central",
    "upper", "lower", "great", "little", "new", "old", "high", "low", "his",
}
# Administrative titles, ranks, abbreviations and adjectives that are capitalized
# in report prose ("the Governor is President of the Council", "Col.", "British")
# but are not places. The most frequent leakage from bare-token detection.
NON_PLACE = {
    "british", "english", "president", "state", "states", "col", "lieut", "sir",
    "hon", "honourable", "excellency", "education", "works", "public", "secretary",
    "governor", "commander", "deputy", "acting", "assistant", "clerk", "registrar",
    "treasurer", "auditor", "collector", "magistrate", "judge", "commissioner",
    "resident", "agent", "consul", "vice", "chief", "majesty", "right", "late",
    "present", "senior", "junior", "captain", "major", "colonel", "general",
    "admiral", "bishop", "archdeacon", "reverend", "messrs", "esq", "esquire",
    "imperial", "royal", "central", "general", "superintendent", "inspector",
    "director", "controller", "comptroller", "postmaster", "surveyor", "warden",
    "speaker", "member", "members", "minister", "attorney", "solicitor", "crown",
    "his", "her", "appendix", "schedule", "section", "chapter", "appendices",
    "monday", "session", "annual", "report", "appointed", "established", "act",
    "king", "queen", "colonies", "revenue", "expenditure", "limited", "total",
    "province", "provinces", "territory", "territories", "dependency",
    "dependencies", "society", "company", "majesty's", "excellency's",
    "trade", "health", "officer", "officers", "sanitary", "medical", "agriculture",
    "finance", "import", "imports", "export", "exports", "population", "area",
}
# Generic geographic / landform common nouns. Real only as part of a proper name
# ("Christmas Island"); never kept standalone — we want groundable, locatable
# NAMED places, not generic terms like "hill" or "field".
FEATURE_WORDS = {
    "island", "islands", "district", "districts", "province", "territory",
    "harbour", "harbor", "bay", "river", "mount", "mountain", "mountains", "lake",
    "cape", "port", "gulf", "point", "hill", "hills", "valley", "valleys", "plain",
    "plains", "channel", "strait", "straits", "peninsula", "reef", "reefs",
    "settlement", "town", "city", "village", "country", "coast", "colony",
    "protectorate", "field", "fields", "creek", "downs", "forest", "swamp",
    "lagoon", "estuary", "delta", "ridge", "range", "pass", "ford", "falls",
    "spring", "springs", "well", "wells", "rock", "rocks", "islet", "islets",
    "shoal", "sound", "inlet", "cove", "head", "headland", "promontory", "ferry",
    "bridge", "road", "street", "square", "park", "garden", "gardens",
}
# Person titles: a capitalized word right after one is a person, not a place.
PERSON_TITLE = re.compile(
    r"\b(?:Sir|Lord|Lady|Captain|Capt|Admiral|General|Colonel|Col|Commodore|Major|"
    r"Lieut|Lieutenant|Mr|Mrs|Dr|Duke|Earl|Count|Baron|King|Queen|Emperor|Sultan|"
    r"Rajah|Governor|President|Commander|Bishop|Rev|Hon|Messrs)\.?\s*$")

# ---------------------------------------------------------------------------
# Detection
# ---------------------------------------------------------------------------
PROPER = r"[A-Z][a-z]+(?:[ -][A-Z][a-z]+){0,2}"
# A feature word can be PART of a proper toponym ("Cape Coast", "Port Louis",
# "Mount Lavinia", "Cape of Good Hope", "St Lucia") or merely DESCRIPTIVE ("the
# district of Kandy", "island of Ceylon"). We capture the FULL name in the first
# case and just the proper noun in the second, so groundable named places that
# contain a feature word are kept while standalone "Cape"/"Hill" are not.
# (1) feature word LEADS and is part of the name -> capture the whole toponym.
RE_FEATURE_LED = re.compile(
    r"\b((?:Cape|Mount|Mt|Port|Lake|Gulf|Bay|Isle|Fort|Point|St|Saint|San|Santa|"
    r"Loch|Ben|River|Rio)\.?\s+(?:of\s+)?" + PROPER + r")")
# (2) feature word TRAILS and is part of the name -> capture the whole toponym.
RE_FEATURE_TRAIL = re.compile(
    r"\b(" + PROPER + r"\s+(?:River|Mountains?|Islands?|District|Province|Bay|"
    r"Harbour|Harbor|Lagoon|Valley|Peninsula|Straits?|Channel|Reef|Falls|Creek|"
    r"Hills?|Plains?|Heads?))\b")
# (3) "<feature> of <Name>": the Name is the place -> capture the proper noun.
RE_FEATURE_OF = re.compile(
    r"\b(?i:district|town|city|village|province|island|port|bay|gulf|river|lake|"
    r"colony|settlement|protectorate|kingdom|peninsula|territory)\s+of\s+("
    + PROPER + r")")
GEO_CUES = [(RE_FEATURE_LED, 1), (RE_FEATURE_TRAIL, 1), (RE_FEATURE_OF, 1)]
# Trade-direction cues (the captured token is a trading partner / external).
TRADE_CUE = re.compile(
    rf"\b(?:export(?:ed|s)?|import(?:ed|s)?|shipped|trade|trading|steamers?|"
    rf"mail|cargo|consigned)\b[^.]{{0,40}}?\b(?:to|from|with|via|at)\s+({PROPER})")
RE_PROPER = re.compile(rf"\b({PROPER})\b")


def _slug(s):
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


# Curated external hubs — major non-colony places that recur as references /
# trading partners across the corpus and won't appear in a "X District" cue.
HUB_GAZ = {
    "london", "liverpool", "england", "scotland", "ireland", "wales", "britain",
    "great_britain", "united_kingdom", "manchester", "glasgow", "bristol",
    "southampton", "plymouth", "edinburgh", "dublin", "paris", "france", "marseilles",
    "hamburg", "germany", "bremen", "amsterdam", "rotterdam", "antwerp", "belgium",
    "lisbon", "portugal", "madrid", "spain", "genoa", "italy", "naples", "trieste",
    "new_york", "united_states", "america", "boston", "san_francisco", "chicago",
    "japan", "china", "shanghai", "canton", "yokohama", "egypt", "suez", "port_said",
    "alexandria", "marseille", "europe", "asia", "africa", "india", "bombay",
    "calcutta", "madras", "karachi", "rangoon", "colombo", "penang", "java",
    "batavia", "manila", "panama", "rio", "buenos_aires", "valparaiso",
}


def _is_noise(surface):
    toks = surface.lower().replace("-", " ").split()
    if not toks:
        return True
    # any token a demonym/month/non-place title, or all-institution/function
    if any(t in DEMONYMS or t in MONTHS or t in NON_PLACE for t in toks):
        return True
    if all(t in FUNCTION_WORDS or t in INSTITUTION for t in toks):
        return True
    if toks[0] in FUNCTION_WORDS and len(toks) == 1:
        return True
    if len(toks) == 1 and toks[0] in FEATURE_WORDS:
        return True  # standalone generic feature word, not a name
    if len(surface) < 3:
        return True
    return False


def detect_places(text):
    """Yield (surface, start, end, method) for place candidates in one block.

    Cue-captured toponyms (which may include a feature word, e.g. "Cape Coast")
    take precedence; a bare capitalized token falling INSIDE a cue span (e.g.
    "Coast" within "Cape Coast") is suppressed so the full name wins."""
    spans = []  # (start, end, surface, method)
    for rx, grp in GEO_CUES:
        for m in rx.finditer(text):
            s = m.group(grp).strip()
            if not _is_noise(s):
                spans.append((m.start(grp), m.start(grp) + len(s), s, "geo_cue"))
    for m in TRADE_CUE.finditer(text):
        s = m.group(1)
        if not _is_noise(s):
            spans.append((m.start(1), m.start(1) + len(s), s, "trade_cue"))
    covered = [(a, b) for a, b, _, _ in spans]

    def inside(st, en):
        return any(a <= st and en <= b for a, b in covered)

    for m in RE_PROPER.finditer(text):
        st, en = m.start(1), m.end(1)
        if inside(st, en):
            continue
        surface = m.group(1)
        if _is_noise(surface):
            continue
        prefix = text[max(0, st - 2):st]
        sentence_initial = st == 0 or prefix.endswith(". ") or prefix.endswith(".\n")
        if sentence_initial and " " not in surface and "-" not in surface:
            continue
        if PERSON_TITLE.search(text[max(0, st - 12):st]):
            continue
        spans.append((st, en, surface, "capitalized"))

    # de-dup by start offset, preferring the longest / cue-backed surface
    best = {}
    for st, en, s, method in spans:
        cur = best.get(st)
        if cur is None or len(s) > len(cur[0]) or \
                (method != "capitalized" and cur[2] == "capitalized"):
            best[st] = (s, en, method)
    for st in sorted(best):
        s, en, method = best[st]
        yield s, st, en, method


def kwic(text, s, e):
    left = text[max(0, s - KWIC_WINDOW):s].replace("\n", " ")
    kw = text[s:e]
    right = text[e:e + KWIC_WINDOW].replace("\n", " ")
    return {"left": left, "kw": kw, "right": right}


def report_blocks(doc):
    """Prose blocks that are report content (before the roster), with section."""
    prof = doc["profile"]
    roster = prof.get("roster_start_block")
    hsplit = prof.get("host_split_block")
    cap = len(doc["blocks"])
    if roster is not None:
        cap = min(cap, roster)
    if hsplit is not None:
        cap = min(cap, hsplit)
    section = None
    for b in doc["blocks"]:
        if b["index"] >= cap:
            break
        if b["kind"] == "heading":
            section = b.get("section_slug")
        elif b["kind"] == "prose":
            yield b, section


def assign_role(colony, place_slug, sections, n_colonies, trade_cues,
                family_members, colony_n, total):
    """Per-(place,colony) role from home-share + family + ubiquity + section + cue."""
    key = place_slug.replace("_", "")
    # The colony's own name or a federation sub-unit it contains.
    if key == colony.replace("_", "") or key in family_members:
        return "local"
    # Home colony: this colony holds the bulk of the place's mentions, so the
    # place belongs to it even if it also shows up as a port elsewhere (Colombo in
    # Ceylon, Singapore in the Straits — capitals appear in trade contexts but are
    # local). Decided before the trade-cue rule.
    if total and colony_n / total >= 0.5 and colony_n >= 10:
        return "local"
    dom = sections.most_common(1)[0][0] if sections else None
    if trade_cues > 0 or dom in TRADE_SECTIONS:
        return "trading_partner"
    if dom in LOCAL_SECTIONS and n_colonies <= HUB_UBIQUITY:
        return "local"
    if n_colonies <= LOCAL_UBIQUITY:
        return "local"
    if n_colonies >= HUB_UBIQUITY:
        return "external_reference"
    return "ambiguous"


def main():
    ap = argparse.ArgumentParser(description="Place-name extraction + KWIC + temporal index")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--place", help="inspect a single place slug")
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    files = canon.list_corpus_files(root)
    gaz = canon.build_gazetteer(files)
    docs = []
    skipped = 0
    for f in files:
        for attempt in range(2):  # one retry — the FS occasionally times out a read
            try:
                docs.append(canon.process_file(f, root, gaz))
                break
            except OSError as e:
                if attempt == 0:
                    time.sleep(0.2)
                    continue
                skipped += 1
                print(f"skip (io) {f}: {e}", file=sys.stderr)
    if skipped:
        print(f"(skipped {skipped} files on I/O error)", file=sys.stderr)
    canon.apply_corpus_triage(docs)

    # Colony/territory/hub gazetteer as separator-stripped keys, to validate bare
    # capitalized tokens that name a known colony, federation sub-unit, or hub.
    def _key(s):
        return s.replace("_", "")
    colony_gaz = {_key(d["colony_slug"]) for d in docs}
    for subs in canon.SUB_UNITS.values():
        colony_gaz |= set(subs)                     # already separator-free
    colony_gaz |= {_key(h) for h in HUB_GAZ}

    # place_slug -> {canonical, aliases:set, has_cue:bool,
    #                colonies:{slug:{years:set, sections:Counter, n:int,
    #                                trade_cues:int, kwic:[...]}}}
    places = defaultdict(lambda: {"canonical": None, "aliases": Counter(),
                                  "has_cue": False, "colonies": defaultdict(
        lambda: {"years": set(), "sections": Counter(), "n": 0, "trade_cues": 0,
                 "kwic": [], "_kwic_years": set()})})

    for d in docs:
        if any(f in SKIP_FLAGS for f in d["profile"]["flags"]):
            continue
        colony, year = d["colony_slug"], d["edition_year"]
        for b, section in report_blocks(d):
            text = b["raw_text"]
            for surface, s, e, method in detect_places(text):
                slug = _slug(surface)
                if not slug:
                    continue
                P = places[slug]
                P["aliases"][surface] += 1
                if method in ("geo_cue", "trade_cue"):
                    P["has_cue"] = True
                C = P["colonies"][colony]
                C["years"].add(year)
                C["n"] += 1
                if section:
                    C["sections"][section] += 1
                if method == "trade_cue":
                    C["trade_cues"] += 1
                if len(C["kwic"]) < KWIC_PER_COLONY and year not in C["_kwic_years"]:
                    C["_kwic_years"].add(year)
                    k = kwic(text, s, e)
                    k.update({"year": year, "section": section, "method": method})
                    C["kwic"].append(k)

    # finalize: prune, assign roles
    out = {}
    for slug, P in places.items():
        total = sum(c["n"] for c in P["colonies"].values())
        n_colonies = len(P["colonies"])
        # global dominant section, for the geography-local keep heuristic
        gsec = Counter()
        for c in P["colonies"].values():
            gsec.update(c["sections"])
        dom_section = gsec.most_common(1)[0][0] if gsec else None
        # Keep a place only if corroborated, else it is bare-token noise:
        #  - seen with a geographic/trade CUE anywhere, OR
        #  - a known colony / sub-unit / curated hub, OR
        #  - strongly geography-local (few colonies, geography-section dominant).
        geo_local = (dom_section in LOCAL_SECTIONS and n_colonies <= 4 and total >= 4)
        # A bare proper noun strongly concentrated in ONE colony's GEOGRAPHY /
        # population prose is very likely a local toponym there (a town/port
        # recurring in its own report), even with no cue or gazetteer entry —
        # recovers e.g. Galle. Gated on the geographic sections + a high home
        # share to keep out recurring local surnames / institutions / peoples
        # (which cluster in history/finance/constitution prose).
        home_n = max((c["n"] for c in P["colonies"].values()), default=0)
        home_concentrated = (total >= 10 and home_n / total >= 0.7
                             and dom_section in LOCAL_SECTIONS)
        keep = (P["has_cue"] or slug.replace("_", "") in colony_gaz
                or geo_local or home_concentrated)
        if not keep or total < MIN_TOTAL_MENTIONS:
            continue
        canonical = P["aliases"].most_common(1)[0][0]
        col_records = {}
        roles = Counter()
        all_years = set()
        for colony, C in P["colonies"].items():
            ckey = colony.replace("_", "")
            fam = canon.SUB_UNITS.get(
                max((k for k in canon.SUB_UNITS if k in ckey), key=len, default=""),
                set())
            role = assign_role(colony, slug, C["sections"], n_colonies,
                               C["trade_cues"], fam, C["n"], total)
            roles[role] += 1
            yrs = sorted(C["years"])
            all_years.update(yrs)
            col_records[colony] = {
                "years": yrs, "first_year": yrs[0], "last_year": yrs[-1],
                "n_mentions": C["n"], "sections": dict(C["sections"]),
                "trade_cues": C["trade_cues"], "role": role, "kwic": C["kwic"],
            }
        ay = sorted(all_years)
        out[slug] = {
            "canonical": canonical,
            "aliases": [a for a, _ in P["aliases"].most_common(6)],
            "n_colonies": n_colonies,
            "n_mentions_total": total,
            "first_year": ay[0], "last_year": ay[-1],
            "global_role": roles.most_common(1)[0][0],
            "has_geo_cue": P["has_cue"],
            "asserted_by": "Colonial Office List",
            "colonies": col_records,
        }

    # ---- summary ----
    by_role = Counter(p["global_role"] for p in out.values())
    print(f"\n=== Place extraction ({len(out)} distinct places kept) ===")
    print(f"global role mix: {dict(by_role)}")
    print(f"\ntop external/hub places (most colonies):")
    for slug, p in sorted(out.items(), key=lambda kv: -kv[1]["n_colonies"])[:12]:
        print(f"  {p['canonical']:18s} {p['n_colonies']:3d} colonies  "
              f"{p['first_year']}-{p['last_year']}  [{p['global_role']}]")

    if args.place:
        p = out.get(args.place)
        if p:
            print(f"\n=== {p['canonical']} ({args.place}) ===")
            print(json.dumps({k: v for k, v in p.items() if k != "colonies"}, indent=2))
            for col, c in list(p["colonies"].items())[:5]:
                print(f"  [{col}] {c['role']} years {c['first_year']}-{c['last_year']} "
                      f"({c['n_mentions']}x) sections={c['sections']}")
                for k in c["kwic"][:2]:
                    print(f"      {k['year']} …{k['left'][-40:]}[{k['kw']}]{k['right'][:40]}…")

    if not (args.stats or args.place):
        gen = root / "generated"
        (gen / "places_index.json").write_text(
            json.dumps({"pipeline_version": PIPELINE_VERSION,
                        "date_created": date.today().isoformat(),
                        "note": ("Place-name mentions in Colonial Office List report "
                                 "content. Roles (local/trading_partner/external) are "
                                 "the source's references, not asserted geography; "
                                 "grounding to coordinates is a later phase."),
                        "n_places": len(out), "places": out}, indent=2,
                       ensure_ascii=False), encoding="utf-8")
        with (gen / "places_index.csv").open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["place", "canonical", "n_colonies", "n_mentions",
                        "first_year", "last_year", "global_role", "has_geo_cue"])
            for slug, p in sorted(out.items(), key=lambda kv: -kv[1]["n_mentions_total"]):
                w.writerow([slug, p["canonical"], p["n_colonies"],
                            p["n_mentions_total"], p["first_year"], p["last_year"],
                            p["global_role"], p["has_geo_cue"]])
        print(f"\nwrote generated/places_index.json ({len(out)} places) + places_index.csv")


if __name__ == "__main__":
    main()
