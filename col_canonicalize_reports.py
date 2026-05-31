#!/usr/bin/env python3
"""
COL Colony-Reports Phase 0: Source Canonicalizer
=================================================

Maps every parsed colony `.txt` file into ONE internal representation,
regardless of whether the upstream parse emitted Markdown (`###`, `**bold**`)
or plain text (bare `Title.` headings, inline `Subheading.—` headings).

This is the highest-leverage step of the colony-reports extraction plan
(COLONY_REPORTS_EXTRACTION_PLAN.md, "Phase 0"): it normalizes the heading
heterogeneity ONCE, centrally, so every downstream consumer sees consistent
input. It is deliberately *deterministic* — it needs no LLM and is fully
testable against the corpus offline:

  * Tables: ~90% of files carry well-formed `|---|` Markdown tables, parsed
    directly into cells (handling ragged rows and lost leading pipes). The
    remainder fall back to structural detection.
  * Headings: detects heading *candidates* and their structural style
    (md / bold / bare-period / inline-dash / ALL-CAPS). Mapping a heading's
    TEXT to a canonical `section_slug` is meaning-based and is the one part
    that genuinely needs the model (Finding 2.5); that step is deferred to the
    Phase-A/D normalizer. A conservative keyword fallback assigns a slug only
    on a high-confidence match, otherwise leaves it null with needs_model=true.
  * Dot-leader lines (`label .... value`) are captured as a distinct kind.
  * Degenerate-file triage (Finding 2.9): empty / very-short / garbled-or-
    lowercase filename / no-table / possible-truncation (size << the colony's
    own neighbouring editions) / anomalous-giant (misparse, e.g. 1888 Ascension).
  * Per-file expectation profile (Finding 2.7-2.8): word/table/heading counts,
    used downstream to judge yield *relative to* a file's own size, not a flat
    threshold.

Every block keeps a back-pointer (line_start/line_end, char_start/char_end)
to the original file so any later extraction is auditable to the page.

Usage:
    python col_canonicalize_reports.py                 # full corpus
    python col_canonicalize_reports.py --stats         # corpus summary only
    python col_canonicalize_reports.py --file 1900_manual_parsed/MAURITIUS.txt
    python col_canonicalize_reports.py --limit 50      # first 50 files
    python col_canonicalize_reports.py --out-dir generated/reports_canonical

Output:
    generated/reports_canonical/<edition_year>/<colony_slug>.json
"""

import argparse
import json
import re
import statistics
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

PIPELINE_VERSION = "col_canonicalize_reports/0.1"

# ---------------------------------------------------------------------------
# Triage thresholds (Findings 2.7-2.9)
# ---------------------------------------------------------------------------
VERY_SHORT_WORDS = 150     # below this: probably not a real report
SHORT_WORDS = 400          # below this: thin; review
TRUNCATION_RATIO = 0.30    # < this fraction of the colony's median => likely truncated
GIANT_RATIO = 5.0          # > this multiple of the colony's median => likely misparse
MIN_EDITIONS_FOR_NEIGHBOUR = 3  # need a few editions before median is meaningful
NEIGHBOUR_MEDIAN_FLOOR = 300    # colony median must exceed this for ratio flags to be trusted
ABS_GIANT_FLOOR = 5000     # a "giant" must also be large in absolute terms (guards tiny-median colonies)

# ---------------------------------------------------------------------------
# Boundary-integrity thresholds (Finding 2.11 — the highest-stakes triage).
# A single size flag cannot separate three situations that need OPPOSITE
# handling: a whole-volume dump, a wrong-colony concatenation, and a legitimate
# federation mega-entry. These detect them by CONTENT, not size.
# ---------------------------------------------------------------------------
VOLUME_DUMP_WORDS = 150000  # above any plausible single entry (Australia tops ~85k); a dump
MISPARSE_MIN_UNRELATED = 2  # >= this many UNRELATED colony headers => wrong-colony concatenation
FEDERATION_MIN_SUBUNITS = 2  # >= this many of the entry's OWN sub-units present => legit nesting
APPENDIX_MARKER_MIN = 8     # honours/cross-colony markers above this => appendix bled in

# Federation / parent -> set of its legitimate sub-unit names (normalized).
# Sourced from guides/federated_territories_guide.md and settler_colonies_guide.md.
# Used to tell "Australia contains its own states" (process it — a recovery
# target) from "British Honduras contains Canadian provinces" (misparse).
def _norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


_SUBUNIT_SOURCE = {
    "leeward islands": ["Antigua", "Dominica", "Montserrat", "St Christopher and Nevis",
                        "St Christopher", "Nevis", "St Kitts", "Virgin Islands", "Anguilla"],
    "windward islands": ["Grenada", "St Lucia", "St Vincent", "Tobago", "Dominica"],
    "federated malay states": ["Perak", "Selangor", "Negri Sembilan", "Pahang"],
    "federation of malaya": ["Perak", "Selangor", "Negri Sembilan", "Pahang", "Johore",
                             "Kedah", "Kelantan", "Trengganu", "Perlis", "Malacca", "Penang"],
    "straits settlements": ["Singapore", "Penang", "Malacca", "Labuan", "Federated Malay States",
                            "Perak", "Selangor", "Negri Sembilan", "Pahang",
                            "Johore", "Kedah", "Kelantan", "Trengganu", "Perlis"],
    "high commission territories": ["Basutoland", "Bechuanaland Protectorate", "Bechuanaland",
                                    "Swaziland"],
    "federation of rhodesia and nyasaland": ["Southern Rhodesia", "Northern Rhodesia", "Nyasaland"],
    "west african settlements": ["Sierra Leone", "Gold Coast", "Gambia", "Lagos"],
    "west africa settlements": ["Sierra Leone", "Gold Coast", "Gambia", "Lagos"],
    "dominion of canada": ["Ontario", "Quebec", "Nova Scotia", "New Brunswick",
                           "British Columbia", "Prince Edward Island", "Manitoba", "Alberta",
                           "Saskatchewan", "Northwest Territories", "Vancouver Island",
                           "Newfoundland"],
    "canada": ["Ontario", "Quebec", "Nova Scotia", "New Brunswick", "British Columbia",
               "Prince Edward Island", "Manitoba", "Alberta", "Saskatchewan",
               "Northwest Territories", "Vancouver Island"],
    "australia": ["New South Wales", "Victoria", "Queensland", "South Australia",
                  "Western Australia", "Tasmania", "Papua", "Norfolk Island",
                  "Lord Howe Island", "Northern Territory", "Commonwealth Control",
                  "Commonwealth"],
    "commonwealth of australia": ["New South Wales", "Victoria", "Queensland", "South Australia",
                                  "Western Australia", "Tasmania", "Papua", "Norfolk Island",
                                  "Lord Howe Island", "Northern Territory"],
    "union of south africa": ["Cape of Good Hope", "Natal", "Transvaal", "Orange River Colony",
                              "Orange Free State"],
    # The SA Governor-General / High Commissioner also administered the High
    # Commission Territories (Basutoland, Bechuanaland, Swaziland) and, in some
    # editions, the Rhodesias appear in the same entry — legitimate nesting here.
    "south africa": ["Cape of Good Hope", "Natal", "Transvaal", "Orange River Colony",
                     "Orange Free State", "Basutoland", "Bechuanaland Protectorate",
                     "Bechuanaland", "Swaziland", "Southern Rhodesia", "Northern Rhodesia",
                     "Southern Rhodesia Administration"],
    # "The Commonwealth" = the Australian federal entry; nests the states.
    "commonwealth": ["New South Wales", "Victoria", "Queensland", "South Australia",
                     "Western Australia", "Tasmania", "Papua", "Norfolk Island",
                     "Lord Howe Island", "Northern Territory"],
    # Unfederated Malay States — its own members.
    "unfederated malay states": ["Johore", "Kedah", "Kelantan", "Trengganu", "Perlis"],
    # Malaya (post-1936 reorganized entries: MALAYA_STRAITS_SETTLEMENTS, etc.).
    "malaya": ["Straits Settlements", "Singapore", "Penang", "Malacca", "Labuan",
               "Federated Malay States", "Perak", "Selangor", "Negri Sembilan", "Pahang",
               "Johore", "Kedah", "Kelantan", "Trengganu", "Perlis", "Christmas Island"],
    # Western Pacific High Commission — nests its island territories.
    "western pacific": ["Fiji", "Tonga", "Pitcairn Island", "New Hebrides",
                        "Gilbert and Ellice Islands", "British Solomon Islands",
                        "Western Pacific High Commission"],
    # single-unit dependencies, listed so a legitimate dependency header is not
    # mistaken for foreign-colony contamination:
    "mauritius": ["Rodrigues", "Seychelles"],
    "ceylon": [],
}


def _load_curated_families():
    """Build the federation allow-list from the historically-curated
    taxonomy/colony_families.json (the authoritative source), keyed by every
    parent alias so the boundary detector's substring resolution finds a file's
    family by its common name. The allow-list unions a family's strict `members`
    with its `associated_territories` (administered-with but separate, e.g. the
    Rhodesias under the South African High Commissioner) so era-overlap nestings
    are not misread as misparses. Falls back to the inline seed if the file is
    missing."""
    path = Path(__file__).resolve().parent / "taxonomy" / "colony_families.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {_norm(k): {_norm(v) for v in vs} for k, vs in _SUBUNIT_SOURCE.items()}
    sub = {}
    for fam in data.get("families", {}).values():
        aliases = fam.get("parent_aliases", []) or [fam.get("canonical_name", "")]
        allow = {_norm(m) for m in fam.get("members", [])}
        allow |= {_norm(t) for t in fam.get("associated_territories", [])}
        allow |= {_norm(a) for a in aliases}
        allow.discard("")
        for alias in aliases:
            key = _norm(alias)
            if key:
                sub[key] = sub.get(key, set()) | allow
    return sub


# Strict membership (no associated territories / aliases) for sub-unit stamping.
def _load_strict_members():
    path = Path(__file__).resolve().parent / "taxonomy" / "colony_families.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return {fam.get("canonical_name", k): sorted(fam.get("members", []))
            for k, fam in data.get("families", {}).items()}


SUB_UNITS = _load_curated_families()
FAMILY_MEMBERS = _load_strict_members()

# Appendix / cross-section contamination markers (reused from the personnel
# pipeline's honours-list detector, EXTRACTION_AUDIT.md). These catch section
# bleed (e.g. Aden 1922) that a size heuristic misses.
RE_APPENDIX_MARKER = re.compile(
    r"knights?\s+grand\s+cross|knights?\s+commander|"
    r"st\.?\s+michael\s+and\s+st\.?\s+george|order\s+of\s+st\.?\s+michael|"
    r"king\s+of\s+arms|general\s+colonial\s+service\s+list", re.I)

# An ALL-CAPS heading-like line that may name a colony (for boundary detection).
RE_CAPS_NAME = re.compile(r"^[A-Z][A-Z][A-Z .,&'/-]{2,30}$")

# ---------------------------------------------------------------------------
# Conservative heading-text -> section_slug fallback.
# Intentionally small and high-precision. Anything not matched is left null
# with needs_model=true, to be resolved by the meaning-based normalizer.
# ---------------------------------------------------------------------------
SECTION_KEYWORDS = {
    "situation": "geography",
    "area": "geography",
    "extent": "geography",
    "boundaries": "geography",
    "history": "history",
    "constitution": "constitution",
    "government": "government",
    "finance": "finance",
    "finances": "finance",
    "revenue": "finance",
    "expenditure": "finance",
    "debt": "finance",
    "trade": "trade",
    "commerce": "trade",
    "imports": "trade",
    "exports": "trade",
    "shipping": "shipping",
    "navigation": "shipping",
    "population": "population",
    "census": "population",
    "religion": "religion",
    "education": "education",
    "railways": "infrastructure",
    "communications": "infrastructure",
    "posts": "infrastructure",
    "telegraphs": "infrastructure",
    "climate": "geography",
    "production": "production",
    "industry": "production",
    "agriculture": "production",
}

# Headings that mark the start of the personnel ROSTER (not report content).
ROSTER_MARKERS = re.compile(
    r"^(civil\s+establishment|military\s+officers|foreign\s+consuls|"
    r"officers\s+of\s+|staff\b|list\s+of\s+officers|judicial\s+department|"
    r"government\s+house\b)",
    re.I,
)

# ---------------------------------------------------------------------------
# Line classification
# ---------------------------------------------------------------------------
RE_MD_HEADING = re.compile(r"^\s*#{1,6}\s+\S")
RE_BOLD_HEADING = re.compile(r"^\s*\*{1,2}([^*]{2,60})\*{1,2}\s*$")
RE_SEPARATOR = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
RE_DOT_LEADER = re.compile(r"^(?P<label>.+?)\s*\.{4,}\s*(?P<value>\S.*)$")
# inline em-dash / double-hyphen subheading at start of a paragraph
RE_INLINE_HEADING = re.compile(r"^(?P<label>[A-Z][A-Za-z][A-Za-z ,&'()]{1,38})\.\s*(—|--|–)\s*(?P<rest>\S)")
# bare "Title." heading line: short, starts uppercase, ends with a single '.',
# and is not itself a full sentence (no internal '. ' boundary).
RE_BARE_HEADING = re.compile(r"^\s*([A-Z][A-Za-z][A-Za-z ,&'.()/-]{1,48})\.\s*$")
RE_ALLCAPS_HEADING = re.compile(r"^\s*([A-Z][A-Z .,&'()/-]{2,48})\.?\s*$")


def is_pipe_line(line):
    return line.count("|") >= 2 or (line.count("|") >= 1 and line.lstrip().startswith("|"))


def looks_like_sentence(text):
    """A bare-heading candidate is rejected if it reads like a sentence."""
    inner = text.rstrip(".").strip()
    if ". " in inner:
        return True
    # too many words for a heading
    if len(inner.split()) > 8:
        return True
    return False


def heading_slug_guess(heading_text):
    """Conservative, high-precision text->slug. Returns (slug|None, needs_model)."""
    words = re.findall(r"[a-z]+", heading_text.lower())
    for w in words:
        if w in SECTION_KEYWORDS:
            return SECTION_KEYWORDS[w], False
    return None, True


# ---------------------------------------------------------------------------
# Table parsing
# ---------------------------------------------------------------------------
def split_pipe_cells(line):
    parts = line.split("|")
    # drop a single leading/trailing empty produced by surrounding pipes
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [p.strip() for p in parts]


def parse_table(lines):
    """lines: list of (raw, is_sep). Return a structured table dict."""
    rows = []
    separator_index = None
    for i, (raw, is_sep) in enumerate(lines):
        if is_sep:
            if separator_index is None:
                separator_index = len(rows)
            continue
        rows.append(split_pipe_cells(raw))
    header = None
    if separator_index is not None and separator_index >= 1:
        header = rows[separator_index - 1]
    elif rows:
        header = rows[0]
    widths = {len(r) for r in rows}
    return {
        "header": header,
        "separator_index": separator_index,
        "rows": rows,
        "ragged": len(widths) > 1,
        "n_rows": len(rows),
        "n_cols_max": max((len(r) for r in rows), default=0),
    }


# ---------------------------------------------------------------------------
# Core segmentation
# ---------------------------------------------------------------------------
def canonicalize_text(text):
    """Return (blocks, format_markers, dot_leader_count)."""
    blocks = []
    fmt = defaultdict(int)
    dot_leader_total = 0

    # precompute char offset at start of each line
    lines = text.split("\n")
    offsets = []
    pos = 0
    for ln in lines:
        offsets.append(pos)
        pos += len(ln) + 1  # +1 for the '\n'

    def char_span(i_start, i_end):
        cs = offsets[i_start]
        ce = offsets[i_end] + len(lines[i_end])
        return cs, ce

    def emit(kind, i_start, i_end, extra=None):
        raw = "\n".join(lines[i_start:i_end + 1]).strip("\n")
        cs, ce = char_span(i_start, i_end)
        block = {
            "index": len(blocks),
            "kind": kind,
            "raw_text": raw,
            "line_start": i_start + 1,
            "line_end": i_end + 1,
            "char_start": cs,
            "char_end": ce,
        }
        if extra:
            block.update(extra)
        blocks.append(block)

    n = len(lines)
    i = 0
    first_nonblank_seen = False
    while i < n:
        raw = lines[i]
        stripped = raw.strip()

        if stripped == "":
            i += 1
            continue

        # --- colony header: the very first non-blank line ---
        if not first_nonblank_seen:
            first_nonblank_seen = True
            # treat as colony header only if it looks like a title (no long prose)
            if len(stripped.split()) <= 10 and not is_pipe_line(raw):
                emit("colony_header", i, i)
                i += 1
                continue

        # --- table block ---
        if is_pipe_line(raw) or RE_SEPARATOR.match(raw):
            j = i
            tlines = []
            while j < n:
                lj = lines[j]
                if lj.strip() == "":
                    # allow a single blank inside a table only if next line is pipe
                    if j + 1 < n and is_pipe_line(lines[j + 1]):
                        j += 1
                        continue
                    break
                if is_pipe_line(lj) or RE_SEPARATOR.match(lj):
                    tlines.append((lj, bool(RE_SEPARATOR.match(lj))))
                    j += 1
                else:
                    break
            if tlines:
                table = parse_table(tlines)
                if table["separator_index"] is not None:
                    fmt["pipe_table_with_sep"] += 1
                else:
                    fmt["pipe_table_no_sep"] += 1
                emit("table", i, j - 1, {"table": table, "pipe_rows": len(tlines)})
                i = j
                continue

        # --- markdown heading ---
        if RE_MD_HEADING.match(raw):
            fmt["hash"] += 1
            txt = re.sub(r"^\s*#{1,6}\s+", "", stripped).rstrip("#").strip()
            slug, needs = heading_slug_guess(txt)
            emit("heading", i, i, {
                "heading_style": "md",
                "heading_text": txt,
                "section_slug": slug,
                "needs_model": needs,
                "is_roster_marker": bool(ROSTER_MARKERS.match(txt)),
            })
            i += 1
            continue

        # --- bold heading ---
        mb = RE_BOLD_HEADING.match(raw)
        if mb and not is_pipe_line(raw):
            fmt["bold"] += 1
            txt = mb.group(1).strip().rstrip(".")
            slug, needs = heading_slug_guess(txt)
            emit("heading", i, i, {
                "heading_style": "bold",
                "heading_text": txt,
                "section_slug": slug,
                "needs_model": needs,
                "is_roster_marker": bool(ROSTER_MARKERS.match(txt)),
            })
            i += 1
            continue

        # --- dot-leader run ---
        if RE_DOT_LEADER.match(raw):
            j = i
            entries = []
            while j < n and RE_DOT_LEADER.match(lines[j]):
                m = RE_DOT_LEADER.match(lines[j])
                entries.append({"label": m.group("label").strip(),
                                "value_raw": m.group("value").strip()})
                j += 1
            dot_leader_total += len(entries)
            emit("dot_leader", i, j - 1, {"entries": entries})
            i = j
            continue

        # --- bare-period / ALL-CAPS heading (single short line) ---
        is_isolated = (i + 1 >= n or lines[i + 1].strip() == "") and \
                      (i == 0 or lines[i - 1].strip() == "")
        mbare = RE_BARE_HEADING.match(raw)
        mcaps = RE_ALLCAPS_HEADING.match(raw)
        if is_isolated and (mbare or mcaps) and not looks_like_sentence(stripped):
            allcaps = bool(mcaps) and stripped.upper() == stripped
            style = "allcaps" if allcaps else "bare_period"
            fmt[style] += 1
            txt = stripped.rstrip(".").strip()
            slug, needs = heading_slug_guess(txt)
            emit("heading", i, i, {
                "heading_style": style,
                "heading_text": txt,
                "section_slug": slug,
                "needs_model": needs,
                "is_roster_marker": bool(ROSTER_MARKERS.match(txt)),
            })
            i += 1
            continue

        # --- prose paragraph (until heading/table/dot-leader/blank-gap break) ---
        j = i
        while j < n:
            lj = lines[j]
            if lj.strip() == "":
                # paragraph break: stop the prose block at the blank line
                break
            if is_pipe_line(lj) or RE_SEPARATOR.match(lj) or RE_MD_HEADING.match(lj) \
                    or RE_DOT_LEADER.match(lj):
                break
            j += 1
        end = max(i, j - 1)
        extra = {}
        # inline em-dash subheading at paragraph start (Finding 2.5)
        mih = RE_INLINE_HEADING.match(lines[i])
        if mih:
            fmt["inline_dash"] += 1
            label = mih.group("label").strip()
            slug, needs = heading_slug_guess(label)
            extra = {"inline_heading": label, "section_slug": slug, "needs_model": needs,
                     "is_roster_marker": bool(ROSTER_MARKERS.match(label))}
        emit("prose", i, end, extra)
        i = end + 1

    return blocks, dict(fmt), dot_leader_total


# ---------------------------------------------------------------------------
# File-level processing
# ---------------------------------------------------------------------------
def parse_path(relpath):
    """'1900_manual_parsed/MAURITIUS.txt' -> (1900, 'mauritius', 'MAURITIUS')."""
    p = Path(relpath)
    m = re.match(r"(\d{4})_manual_parsed", p.parts[0])
    year = int(m.group(1)) if m else None
    stem = p.stem
    slug = re.sub(r"[^a-z0-9]+", "_", stem.lower()).strip("_")
    return year, slug, stem


def filename_flags(stem):
    flags = []
    if stem != stem.upper() and stem != stem.title().replace(" ", "_"):
        # mixed/lowercase relative to the usual ALL-CAPS convention
        if stem == stem.lower():
            flags.append("lowercase_filename")
    if re.search(r"_REF\b|_\d|__|\b\d{2,}\b", stem):
        flags.append("garbled_filename")
    return flags


def build_gazetteer(files):
    """Set of normalized colony names from filenames + all known sub-units."""
    gaz = set()
    for f in files:
        gaz.add(_norm(Path(f).stem))
    for subs in SUB_UNITS.values():
        gaz |= subs
    gaz.discard("")
    return gaz


def detect_boundary_issues(text, colony_slug, gazetteer):
    """Content-based boundary integrity check (Finding 2.11).

    Distinguishes a legitimate federation mega-entry (its own sub-units nested
    inside) from a wrong-colony concatenation (unrelated colonies misfiled into
    one file) and from appendix bleed — three cases a size heuristic cannot tell
    apart. Returns a dict of evidence + flags.
    """
    # Drop a leading article so "THE_LEEWARD_ISLANDS" matches the federation key.
    self_norm = _norm(re.sub(r"^the[\s_]+", "", colony_slug, flags=re.I))
    # Resolve the federation key by substring, so compound/reorganized names like
    # "MALAYA_STRAITS_SETTLEMENTS" find "straits settlements" and inherit its
    # sub-units. Pick the longest matching key to avoid spurious short matches.
    fed_key = max((k for k in SUB_UNITS if k in self_norm),
                  key=len, default=self_norm if self_norm in SUB_UNITS else None)
    allowed = set(SUB_UNITS.get(fed_key, set()))
    allowed.add(self_norm)
    is_federation = fed_key is not None and fed_key in SUB_UNITS

    foreign = []
    for ln in text.splitlines():
        s = ln.strip().rstrip(".").strip()
        if RE_CAPS_NAME.match(s):
            # "THE NORTHERN TERRITORY" / "THE COMMONWEALTH" -> drop the article
            s = re.sub(r"^THE\s+", "", s, flags=re.I)
            nm = _norm(s)
            if nm and nm != self_norm and nm in gazetteer:
                foreign.append(nm)
    foreign_set = set(foreign)
    subunits_present = sorted(foreign_set & allowed)
    unrelated = sorted(foreign_set - allowed)

    appendix_markers = len(RE_APPENDIX_MARKER.findall(text))

    flags = []
    # Legitimate federation nesting (a RECOVERY target, not an error). This is a
    # robust per-file judgement: the entry's OWN sub-units appear inside it.
    if is_federation and len(subunits_present) >= FEDERATION_MIN_SUBUNITS:
        flags.append("federation_nested")
    # Appendix / cross-section bleed (caught by markers, not size).
    if appendix_markers >= APPENDIX_MARKER_MIN:
        flags.append("appendix_contamination")
    # NOTE: multi_colony_misparse is decided later (apply_corpus_triage), because
    # a couple of incidental colony mentions in prose/tables are NOT a misparse;
    # a true wrong-colony concatenation needs corroboration (many unrelated names
    # or a size outlier). See apply_corpus_triage.

    return {
        "flags": flags,
        "foreign_colony_headers": sorted(foreign_set),
        "unrelated_colony_headers": unrelated,
        "subunit_headers": subunits_present,
        "appendix_marker_count": appendix_markers,
        "is_known_federation": is_federation,
    }


def process_file(relpath, root, gazetteer=None):
    full = root / relpath
    text = full.read_text(encoding="utf-8", errors="replace")
    year, slug, stem = parse_path(relpath)
    blocks, fmt, dot_leaders = canonicalize_text(text)
    word_count = len(text.split())
    table_blocks = [b for b in blocks if b["kind"] == "table"]
    pipe_rows = sum(b.get("pipe_rows", 0) for b in table_blocks)
    headings = [b for b in blocks if b["kind"] == "heading"]
    roster_idx = next((b["index"] for b in blocks
                       if b.get("is_roster_marker")), None)

    profile = {
        "word_count": word_count,
        "char_count": len(text),
        "block_count": len(blocks),
        "table_block_count": len(table_blocks),
        "pipe_row_count": pipe_rows,
        "heading_candidate_count": len(headings),
        "headings_mapped": sum(1 for h in headings if h.get("section_slug")),
        "dot_leader_count": dot_leaders,
        "format_markers": fmt,
        "roster_start_block": roster_idx,
        "flags": [],  # filled by triage (single + corpus pass)
    }
    profile["flags"].extend(filename_flags(stem))
    if word_count == 0:
        profile["flags"].append("empty")
    elif word_count < VERY_SHORT_WORDS:
        profile["flags"].append("very_short")
    elif word_count < SHORT_WORDS:
        profile["flags"].append("short")
    if len(table_blocks) == 0 and word_count >= VERY_SHORT_WORDS:
        profile["flags"].append("no_tables")

    # Boundary integrity (Finding 2.11): content-based, not size-based.
    if gazetteer is not None:
        boundary = detect_boundary_issues(text, slug, gazetteer)
        profile["boundary"] = boundary
        profile["flags"].extend(boundary["flags"])
    # Volume dump is the absolute-size backstop, because header detection
    # undercounts dumps whose colony headers are OCR-mangled (1888 Ascension).
    if word_count >= VOLUME_DUMP_WORDS:
        profile["flags"].append("volume_dump")

    return {
        "source_file": relpath,
        "colony_slug": slug,
        "edition_year": year,
        "pipeline_version": PIPELINE_VERSION,
        "date_created": date.today().isoformat(),
        "profile": profile,
        "blocks": blocks,
    }


def apply_corpus_triage(docs):
    """Second pass: flag truncation/giant relative to each colony's own editions."""
    by_colony = defaultdict(list)
    for d in docs:
        by_colony[d["colony_slug"]].append(d)
    for colony, group in by_colony.items():
        counts = [d["profile"]["word_count"] for d in group
                  if d["profile"]["word_count"] > 0]
        if len(counts) < MIN_EDITIONS_FOR_NEIGHBOUR:
            continue
        med = statistics.median(counts)
        if med <= 0:
            continue
        for d in group:
            wc = d["profile"]["word_count"]
            # A high size-outlier is now only a *review* signal, not a verdict:
            # content-based detection (multi_colony_misparse / federation_nested)
            # decides whether a large file is a misparse or a legitimate
            # mega-entry. We keep the size signal because it can surface a dump
            # whose embedded colony headers were too OCR-mangled to detect.
            if wc > GIANT_RATIO * med and wc >= ABS_GIANT_FLOOR:
                d["profile"]["flags"].append("size_outlier_high")
                d["profile"]["colony_median_words"] = med
            # Truncation is only meaningful when the median is itself trustworthy;
            # a tiny median means most editions are degenerate stubs, not a baseline.
            elif med >= NEIGHBOUR_MEDIAN_FLOOR and 0 < wc < TRUNCATION_RATIO * med:
                d["profile"]["flags"].append("possible_truncation")
                d["profile"]["colony_median_words"] = med

    # Wrong-colony concatenation (Finding 2.11). A few incidental colony mentions
    # are not a misparse; a true one is corroborated by either many unrelated
    # headers or an unexplained size spike. Decided here so size_outlier is known.
    for d in docs:
        b = d["profile"].get("boundary")
        if not b:
            continue
        n_unrelated = len(b["unrelated_colony_headers"])
        size_flag = ("size_outlier_high" in d["profile"]["flags"]
                     or "volume_dump" in d["profile"]["flags"])
        if n_unrelated >= 4 or (n_unrelated >= MISPARSE_MIN_UNRELATED and size_flag):
            d["profile"]["flags"].append("multi_colony_misparse")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def list_corpus_files(root):
    out = subprocess.check_output(["git", "ls-files"], cwd=root).decode().splitlines()
    return [f for f in out if re.search(r"_manual_parsed/.*\.txt$", f)]


def print_corpus_stats(docs):
    n = len(docs)
    wc = sorted(d["profile"]["word_count"] for d in docs)
    with_tables = sum(1 for d in docs if d["profile"]["table_block_count"] > 0)
    with_headings = sum(1 for d in docs if d["profile"]["heading_candidate_count"] > 0)
    mapped = sum(1 for d in docs if d["profile"]["headings_mapped"] > 0)
    flag_counts = defaultdict(int)
    for d in docs:
        for f in d["profile"]["flags"]:
            flag_counts[f] += 1
    style_totals = defaultdict(int)
    for d in docs:
        for k, v in d["profile"]["format_markers"].items():
            style_totals[k] += v

    def pct(x):
        return f"{100 * x / n:.0f}%"

    print(f"\n=== Phase-0 canonicalization summary ({n} files) ===")
    print(f"word count  min/median/max : {wc[0]} / {statistics.median(wc):.0f} / {wc[-1]}")
    print(f"files with >=1 table block : {with_tables} ({pct(with_tables)})")
    print(f"files with heading candidate: {with_headings} ({pct(with_headings)})")
    print(f"files with >=1 mapped slug  : {mapped} ({pct(mapped)})")
    print("heading-style block totals  :", dict(style_totals))
    print("triage flags:")
    for k in sorted(flag_counts, key=lambda x: -flag_counts[x]):
        print(f"   {k:24s} {flag_counts[k]}")


def main():
    ap = argparse.ArgumentParser(description="Phase 0: canonicalize colony report files")
    ap.add_argument("--file", help="process a single relative file path")
    ap.add_argument("--limit", type=int, help="process only the first N files")
    ap.add_argument("--out-dir", default="generated/reports_canonical")
    ap.add_argument("--stats", action="store_true", help="print corpus stats, do not write")
    ap.add_argument("--no-write", action="store_true", help="compute but do not write JSON")
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    # The gazetteer needs the full corpus file list (every colony name), even
    # when only one file is processed, so boundary detection works in --file mode.
    gazetteer = build_gazetteer(list_corpus_files(root))

    if args.file:
        doc = process_file(args.file, root, gazetteer)
        print(json.dumps(doc, indent=2, ensure_ascii=False))
        return

    files = list_corpus_files(root)
    if args.limit:
        files = files[:args.limit]

    docs = []
    for relpath in files:
        try:
            docs.append(process_file(relpath, root, gazetteer))
        except Exception as e:  # noqa: BLE001
            print(f"ERROR {relpath}: {e}", file=sys.stderr)

    apply_corpus_triage(docs)

    if not (args.stats or args.no_write):
        out_dir = root / args.out_dir
        for d in docs:
            sub = out_dir / str(d["edition_year"])
            sub.mkdir(parents=True, exist_ok=True)
            (sub / f"{d['colony_slug']}.json").write_text(
                json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {len(docs)} canonical JSON files under {args.out_dir}/")

    print_corpus_stats(docs)


if __name__ == "__main__":
    main()
