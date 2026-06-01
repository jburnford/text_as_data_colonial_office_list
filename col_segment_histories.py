#!/usr/bin/env python3
"""
COL History Track (Phase 0): Section bounding + cross-edition version dedup
===========================================================================

Builds the deduplicated backbone for the History-narrative track
(HISTORY_NARRATIVE_EXTRACTION_PLAN.md). Two jobs, both deterministic (no LLM):

  1. **Robust section bounding.** From the Phase-0 canonical blocks
     (col_canonicalize_reports.py), isolate each colony-year's *History*
     section: the prose following the `history` heading, ending at the NEXT
     heading and hard-capped at the personnel-roster boundary
     (`roster_start_block`) and, for misparses, the recoverable-host split
     (`host_split_block`). This avoids the ~6% of cross-edition "rewrites" that
     are really section-boundary over-runs (see June1.md history analysis).

  2. **Cross-edition version clustering.** History sections are ~81% republished
     verbatim across editions; each colony has only ~4-13 *distinct* versions
     across 30-68 editions. We collapse near-duplicate consecutive editions
     (difflib.SequenceMatcher, the same measure that found the 81% figure) into
     one `COL_HistoryVersion` carrying `edition_years[]`. Entities/framing are
     then extracted ONCE per version (col_frame_histories.py), not 60x.

CRITICAL stance (HISTORY_NARRATIVE_EXTRACTION_PLAN.md): these histories are
*claims asserted by the Colonial Office*, not objective fact. This stage only
bounds and dedups; it preserves verbatim text and source spans and never asserts
truth. Downstream records carry `asserted_by` / `asserted_as_claim`.

Output: generated/histories_segmented/<colony>.json

Usage:
    python col_segment_histories.py                 # full corpus
    python col_segment_histories.py --stats         # version-count summary only
    python col_segment_histories.py --colony sierra_leone
"""

import argparse
import json
import re
from collections import defaultdict
from datetime import date
from difflib import SequenceMatcher
from hashlib import sha1
from pathlib import Path

import col_canonicalize_reports as canon

PIPELINE_VERSION = "col_segment_histories/0.1"
SECTION_SLUG = "history"
MIN_WORDS = 20                 # below this: not a usable history section
SAME_VERSION_THRESHOLD = 0.90  # consecutive editions >= this similarity = same version
# Source triage flags that make a bounded section untrustworthy for attribution.
HARD_QUARANTINE_FLAGS = {"volume_dump"}
# Flags worth surfacing (a misparse host-prefix history is salvageable but flagged).
SOURCE_REVIEW_FLAGS = {"multi_colony_misparse", "appendix_contamination",
                       "size_outlier_high", "possible_truncation"}


def _words(text):
    return re.sub(r"\s+", " ", text).strip().lower().split()


def _version_hash(text):
    norm = re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()
    return sha1(norm.encode("utf-8")).hexdigest()[:12]


def extract_history(doc, slug=SECTION_SLUG):
    """Bound the History section from a canonical doc.

    Returns a dict with text + span + how the section ended, or a dict with
    status != 'ok' when the section is absent, empty, or falls in a
    misattributed (foreign) region. Hard-capped at the roster boundary and the
    recoverable-host split so it never over-runs into personnel or misfiled text.
    """
    blocks = doc["blocks"]
    prof = doc["profile"]
    roster = prof.get("roster_start_block")
    hsplit = prof.get("host_split_block")
    caps = [len(blocks)]
    if roster is not None:
        caps.append(roster)
    if hsplit is not None:
        caps.append(hsplit)
    hard_end = min(caps)

    start_h = None
    for b in blocks:
        if b["kind"] == "heading":
            ht = (b.get("heading_text") or "").strip().lower()
            if b.get("section_slug") == slug or ht == slug:
                start_h = b["index"]
                break
    if start_h is None:
        return {"status": "no_history"}
    if start_h >= hard_end:
        # the History heading sits inside the roster / foreign-misparse region
        return {"status": "after_boundary"}

    parts, cs, ce = [], None, None
    end_reason = "eof"
    i = start_h + 1
    while i < hard_end:
        b = blocks[i]
        if b["kind"] == "heading":
            end_reason = "next_heading"
            break
        if b["kind"] == "prose":
            parts.append(b["raw_text"])
            if cs is None:
                cs = b["char_start"]
            ce = b["char_end"]
        i += 1
    else:
        end_reason = ("roster_backstop" if hard_end == roster
                      else "host_split" if hard_end == hsplit else "eof")

    text = re.sub(r"\s+", " ", " ".join(parts)).strip()
    if len(text.split()) < MIN_WORDS:
        return {"status": "too_short", "word_count": len(text.split())}
    return {"status": "ok", "text": text, "char_start": cs, "char_end": ce,
            "heading_block": start_h, "end_reason": end_reason}


def cluster_versions(entries):
    """Chain consecutive editions (by year) into versions: a drop below
    SAME_VERSION_THRESHOLD vs the previous edition starts a new version. This is
    the same consecutive-similarity measure that established the ~4-13 distinct
    versions / colony finding. The representative text is the longest member (the
    most complete reading); intra-cluster min similarity is recorded so drift
    inside a version stays visible."""
    entries = sorted(entries, key=lambda e: e["edition_year"])
    versions = []
    for e in entries:
        ew = _words(e["text"])
        if versions:
            prev = versions[-1]["members"][-1]
            ratio = SequenceMatcher(None, prev["_w"], ew).ratio()
            if ratio >= SAME_VERSION_THRESHOLD:
                versions[-1]["members"].append(e)
                versions[-1]["sims"].append(ratio)
                e["_w"] = ew
                continue
        versions.append({"members": [e], "sims": []})
        e["_w"] = ew
    return versions


def build_version_records(colony, versions):
    out = []
    for v in versions:
        members = v["members"]
        rep = max(members, key=lambda m: len(m["text"]))
        vhash = _version_hash(rep["text"])
        years = sorted(m["edition_year"] for m in members)
        flags = sorted({f for m in members for f in m["source_flags"]})
        quarantined = any(m["quarantined"] for m in members)
        out.append({
            "uri": f"col:hversion/{colony}/history/{vhash}",
            "colony": colony,
            "section_slug": SECTION_SLUG,
            "version_hash": vhash,
            "asserted_by": "Colonial Office List",
            "text": rep["text"],
            "edition_years": years,
            "first_edition_year": years[0],
            "last_edition_year": years[-1],
            "n_editions": len(members),
            "representative_source_file": rep["source_file"],
            "char_start": rep["char_start"],
            "char_end": rep["char_end"],
            "end_reason": rep["end_reason"],
            "intra_cluster_min_sim": round(min(v["sims"]), 3) if v["sims"] else 1.0,
            "source_flags": flags,
            "quarantined": quarantined,
            "pipeline_version": PIPELINE_VERSION,
            "date_created": date.today().isoformat(),
        })
    return out


def segment_corpus(root, only_colony=None):
    files = canon.list_corpus_files(root)
    gaz = canon.build_gazetteer(files)
    docs = [canon.process_file(f, root, gaz) for f in files]
    canon.apply_corpus_triage(docs)

    by_colony = defaultdict(list)
    skipped = defaultdict(int)
    for d in docs:
        colony = d["colony_slug"]
        if only_colony and colony != only_colony:
            continue
        res = extract_history(d)
        if res["status"] != "ok":
            skipped[res["status"]] += 1
            continue
        prof = d["profile"]
        sflags = [f for f in prof["flags"] if f in SOURCE_REVIEW_FLAGS
                  or f in HARD_QUARANTINE_FLAGS]
        by_colony[colony].append({
            "edition_year": d["edition_year"],
            "source_file": d["source_file"],
            "text": res["text"],
            "char_start": res["char_start"],
            "char_end": res["char_end"],
            "end_reason": res["end_reason"],
            "source_flags": sflags,
            "quarantined": any(f in HARD_QUARANTINE_FLAGS for f in sflags),
        })

    colonies = {}
    for colony, entries in by_colony.items():
        versions = cluster_versions(entries)
        colonies[colony] = {
            "colony": colony,
            "n_editions_with_history": len(entries),
            "n_versions": len(versions),
            "versions": build_version_records(colony, versions),
        }
    return colonies, skipped


def main():
    ap = argparse.ArgumentParser(description="Phase 0 of the History track: bound + dedup")
    ap.add_argument("--colony", help="process only this colony slug")
    ap.add_argument("--stats", action="store_true", help="summary only, do not write")
    ap.add_argument("--out-dir", default="generated/histories_segmented")
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    colonies, skipped = segment_corpus(root, args.colony)

    n_col = len(colonies)
    n_ed = sum(c["n_editions_with_history"] for c in colonies.values())
    n_ver = sum(c["n_versions"] for c in colonies.values())
    vcounts = sorted(c["n_versions"] for c in colonies.values())
    import statistics
    print(f"\n=== History segmentation ({n_col} colonies with a History section) ===")
    print(f"editions with a bounded History : {n_ed}")
    print(f"distinct versions               : {n_ver}  "
          f"(dedup ratio {n_ed / n_ver:.1f}x)" if n_ver else "")
    if vcounts:
        print(f"versions/colony  min/median/max : {vcounts[0]} / "
              f"{statistics.median(vcounts):.0f} / {vcounts[-1]}")
    print(f"skipped sections                : {dict(skipped)}")

    if not args.stats:
        out_dir = root / args.out_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        for colony, data in colonies.items():
            (out_dir / f"{colony}.json").write_text(
                json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {n_col} colony files under {args.out_dir}/")


if __name__ == "__main__":
    main()
