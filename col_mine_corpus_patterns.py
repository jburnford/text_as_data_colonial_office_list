#!/usr/bin/env python3
"""
COL Colony-Reports: Corpus Pattern Miner (data-driven structure discovery)
==========================================================================

Philosophy (deliberate, see COLONY_REPORTS_SESSION_HANDOFF.md):
    The corpus is too irregular to drive design from a small hand-labelled gold
    standard, and hand-authored maps (the federation->sub-unit list that the
    boundary detector first used) are brittle and need constant maintenance.
    Instead, mine the regularities from the FULL corpus and let scale +
    self-consistency reveal the structure. A gold standard is a ruler (for
    measuring the result), not a teacher (for deriving it).

What this derives, with no hand map:
  1. Federation FAMILIES (parent <- consistently-nested sub-units), with the
     parent's own NAME DRIFT absorbed automatically: parents that share
     sub-units are merged into one canonical family (so FMS/UMS/Straits/"Malaya"
     collapse together, canada/dominion_of_canada collapse, etc. — the Finding
     2.10 entity-drift problem, solved from data rather than by hand).
  2. FLOATING / appendix sections — colony-name headers that nest under many
     DIFFERENT families with no stable parent (the "Miscellaneous Islands /
     Ascension / Tristan da Cunha" appendix that bleeds into whatever entry
     precedes it). These are the source of multi_colony attribution errors.
  3. Heading + table-column-header FREQUENCY tables — the empirical section and
     indicator vocabularies, frequency-ranked, to seed the taxonomies at scale
     (Phase A) rather than from a 40-file sample.

Method (interpretable, auditable — this is also a teaching project):
  * A header token nests under a host = it appears as an ALL-CAPS heading line
    inside a file owned by a different colony.
  * Build parent->child candidate edges from nestings; merge parents that share
    >= MERGE_MIN_SHARED children into canonical families (transitive closure).
  * A token is a FAMILY SUB-UNIT if >= FAMILY_SHARE of its nestings fall within
    one family; FLOATING if it has no such family and spans >= FLOAT_MIN_FAMILIES
    distinct families.

Output: generated/corpus_patterns.json  (consumed by col_canonicalize_reports.py
        when present, so the boundary detector self-calibrates from the corpus).

Usage:
    python col_mine_corpus_patterns.py            # mine + write JSON + summary
    python col_mine_corpus_patterns.py --stats    # summary only, no write
    python col_mine_corpus_patterns.py --top 40   # show top-N headings/columns
"""

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import col_canonicalize_reports as canon

PIPELINE_VERSION = "col_mine_corpus_patterns/0.1"

# Tunable discovery thresholds (NOT domain knowledge — purely statistical).
MIN_NESTINGS = 2          # ignore tokens nested fewer times (too sparse to judge)
MERGE_MIN_SHARED = 2      # parents sharing >= this many children merge into one family
FAMILY_SHARE = 0.60       # >= this share of nestings within one family => sub-unit
FLOAT_MIN_FAMILIES = 3    # nests under >= this many distinct families => floating/appendix
# A child appearing under more than this many distinct parents is a promiscuous
# "hub" (a floating appendix section, or a region cross-referenced everywhere).
# Such children are excluded as MERGE EVIDENCE, because otherwise the appendix
# bridges unrelated families and union-find collapses them into one blob.
HUB_PARENT_LIMIT = 4
# In the iterative loop, a non-excluded file with at least this many foreign
# colony headers OUTSIDE its own derived family is judged a misparse and excluded
# before the next mining round (family-aware, so no size corroboration needed).
MISPARSE_UNRELATED = 4
MAX_ROUNDS = 6

RE_CAPS_NAME = re.compile(r"^[A-Z][A-Z][A-Z .,&'/-]{2,30}$")


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def scan_nestings(files, root, gazetteer, exclude=frozenset()):
    """Scan once. Returns:
      nest_hosts: token -> Counter(host_colony -> n_files_nested_in)
      real:       set of colony slugs that own at least one file
      file_foreign: relpath -> set(foreign colony-name tokens it contains)
    Files in `exclude` (detected misparses/dumps) are skipped as nesting hosts,
    so their misfiled foreign content cannot pollute the derived families.
    """
    nest_hosts = defaultdict(Counter)
    real = set()
    file_foreign = {}
    for f in files:
        self_slug = _norm(Path(f).stem.split(".")[0])
        real.add(self_slug)
        text = (root / f).read_text(encoding="utf-8", errors="replace")
        seen = set()
        for ln in text.splitlines():
            s = ln.strip().rstrip(".").strip()
            if RE_CAPS_NAME.match(s):
                s = re.sub(r"^THE\s+", "", s, flags=re.I)
                nm = _norm(s)
                if nm in gazetteer and nm != self_slug and nm not in seen:
                    seen.add(nm)
                    if f not in exclude:
                        nest_hosts[nm][self_slug] += 1
        file_foreign[f] = seen
    return nest_hosts, real, file_foreign


def merge_parents_into_families(nest_hosts):
    """Union-find over parents that share >= MERGE_MIN_SHARED children.

    This is where the entity-name drift dissolves: FMS, UMS, Straits and the
    'Malaya...' variants all parent the same Malay states, so they merge.
    Returns (parent_of: child->canonical_family, family_members: family->set).
    """
    # children grouped by parent (only dominant-ish hosts count as parents)
    children_of = defaultdict(set)
    child_parent_count = Counter()
    for child, hosts in nest_hosts.items():
        if sum(hosts.values()) < MIN_NESTINGS:
            continue
        child_parent_count[child] = len(hosts)
        for host in hosts:
            children_of[host].add(child)

    # Only DISCRIMINATIVE children (low promiscuity) are trusted as evidence that
    # two parents are the same family. Hub children (appendix sections, regions
    # cross-referenced everywhere) would otherwise merge unrelated families.
    discriminative_of = {
        p: {c for c in cs if child_parent_count[c] <= HUB_PARENT_LIMIT}
        for p, cs in children_of.items()
    }

    parents = list(children_of)
    uf = {p: p for p in parents}

    def find(x):
        while uf[x] != x:
            uf[x] = uf[uf[x]]
            x = uf[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            uf[ra] = rb

    for i, p1 in enumerate(parents):
        for p2 in parents[i + 1:]:
            if len(discriminative_of[p1] & discriminative_of[p2]) >= MERGE_MIN_SHARED:
                union(p1, p2)

    # canonical family name = the parent in the group with the most children
    groups = defaultdict(list)
    for p in parents:
        groups[find(p)].append(p)
    family_members = {}
    parent_to_family = {}
    for root_p, members in groups.items():
        canonical = max(members, key=lambda m: len(children_of[m]))
        family_members[canonical] = set(members)
        for m in members:
            parent_to_family[m] = canonical
    return parent_to_family, family_members, children_of


def classify(nest_hosts, parent_to_family):
    """Assign each token to a family sub-unit or floating/appendix or regional."""
    families = defaultdict(set)   # canonical_family -> {sub-units}
    floating = {}                 # token -> n distinct families it spans
    regional = {}                 # token -> n hosts (has a family but also spreads)

    for token, hosts in nest_hosts.items():
        total = sum(hosts.values())
        if total < MIN_NESTINGS:
            continue
        # tally nestings by family
        by_family = Counter()
        for host, n in hosts.items():
            fam = parent_to_family.get(host, host)
            by_family[fam] += n
        top_family, top_n = by_family.most_common(1)[0]
        share = top_n / total
        n_families = len(by_family)

        if share >= FAMILY_SHARE:
            families[top_family].add(token)
            if n_families >= FLOAT_MIN_FAMILIES:
                regional[token] = n_families  # belongs to a family but also cross-refs
        elif n_families >= FLOAT_MIN_FAMILIES:
            floating[token] = n_families
    return families, floating, regional


def mine_families(nest_hosts):
    """merge parents across name-drift, classify tokens, keep real families."""
    parent_to_family, family_members, _ = merge_parents_into_families(nest_hosts)
    families, floating, regional = classify(nest_hosts, parent_to_family)
    families = {p: sorted(s) for p, s in families.items() if len(s) >= 2}
    return families, family_members, floating, regional


def build_allowed(families, family_members):
    """slug -> the set of names that legitimately co-occur with it (its family's
    sub-units + the family's parent name-variants + itself)."""
    slug_allowed = {}
    for canonical, subs in families.items():
        members = set(subs) | set(family_members.get(canonical, {canonical})) | {canonical}
        for m in members:
            slug_allowed[m] = members
    return slug_allowed


def hand_allowed(self_slug):
    """Curated-knowledge fallback (the hand-seed federation map in the
    canonicalizer), resolved by longest-substring key like the boundary detector.
    Reconciled WITH the derived families because where the corpus is sparse (rare
    federations like the Unfederated Malay States, few editions) derivation is
    fragile and the curated knowledge is more reliable: a header is allowed if
    EITHER source permits it."""
    fed_key = max((k for k in canon.SUB_UNITS if k in self_slug), key=len,
                  default=self_slug if self_slug in canon.SUB_UNITS else None)
    allowed = set(canon.SUB_UNITS.get(fed_key, set()))
    allowed.add(self_slug)
    return allowed


def seed_misparse_exclude(files, root, gazetteer):
    """Round-0 seed: the already-validated hand-map boundary detector. This is
    scaffolding the derived structure then surpasses — using it only to bootstrap
    the exclusion set so misfiled content can't pollute the first mining round."""
    docs = [canon.process_file(f, root, gazetteer) for f in files]
    canon.apply_corpus_triage(docs)
    return {d["source_file"] for d in docs
            if "multi_colony_misparse" in d["profile"]["flags"]
            or "volume_dump" in d["profile"]["flags"]}


def iterative_decontaminate(files, root, gazetteer, seed_exclude):
    """Detect -> exclude -> re-mine until the exclude set stabilizes. After the
    seed round, misparse detection uses the DERIVED families (not the hand map),
    so it catches concatenations the hand map missed while the seeded exclusions
    keep the families clean (breaking the contamination chicken-and-egg)."""
    exclude = set(seed_exclude)
    history = [("seed", len(exclude))]
    families = family_members = floating = regional = None
    for rnd in range(1, MAX_ROUNDS + 1):
        nest_hosts, _, file_foreign = scan_nestings(files, root, gazetteer, exclude)
        families, family_members, floating, regional = mine_families(nest_hosts)
        slug_allowed = build_allowed(families, family_members)
        new_exclude = set(exclude)
        for f in files:
            if f in new_exclude:
                continue
            self_slug = _norm(Path(f).stem.split(".")[0])
            # Reconcile derived families with the curated hand-seed (union): trust
            # whichever source recognizes the nesting, so sparse-evidence
            # federations aren't mistaken for misparses.
            allowed = slug_allowed.get(self_slug, {self_slug}) | hand_allowed(self_slug)
            unrelated = file_foreign[f] - allowed
            if len(unrelated) >= MISPARSE_UNRELATED:
                new_exclude.add(f)
        history.append((f"round {rnd}", len(new_exclude)))
        if new_exclude == exclude:
            break
        exclude = new_exclude
    return exclude, families, family_members, floating, regional, history


def mine_headings(root, gazetteer):
    """Frequency-rank heading candidates and table column headers across the
    corpus (Phase-A taxonomy seed, at scale)."""
    files = canon.list_corpus_files(root)
    heading_freq = Counter()
    column_freq = Counter()
    for f in files:
        doc = canon.process_file(f, root, gazetteer)
        for b in doc["blocks"]:
            if b["kind"] == "heading":
                txt = b.get("heading_text", "").strip().lower()
                if 2 <= len(txt) <= 40:
                    heading_freq[txt] += 1
            elif b["kind"] == "table":
                hdr = b.get("table", {}).get("header") or []
                for cell in hdr:
                    cl = cell.strip().lower()
                    if 1 <= len(cl) <= 30 and not cl.isdigit():
                        column_freq[cl] += 1
    return heading_freq, column_freq


def main():
    ap = argparse.ArgumentParser(description="Mine corpus-scale patterns (no hand map)")
    ap.add_argument("--stats", action="store_true", help="summary only, do not write")
    ap.add_argument("--top", type=int, default=30, help="show top-N headings/columns")
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default="generated/corpus_patterns.json")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    files = canon.list_corpus_files(root)
    gazetteer = canon.build_gazetteer(files)

    # Before: mine with NO decontamination (shows the misparse contamination).
    nest0, _, _ = scan_nestings(files, root, gazetteer)
    fam0, fammem0, _, _ = mine_families(nest0)

    # Iterative detect -> exclude -> re-mine.
    seed = seed_misparse_exclude(files, root, gazetteer)
    exclude, families, family_members, floating, regional, history = \
        iterative_decontaminate(files, root, gazetteer, seed)

    print("=== iterative decontamination (detect -> exclude -> re-mine) ===")
    for label, n in history:
        print(f"   {label:10s} excluded files: {n}")
    print(f"   converged: {len(exclude)} misparse/dump files excluded from mining")
    newly_caught = sorted(exclude - seed)
    if newly_caught:
        print(f"   caught by DERIVED families but missed by the hand-map seed ({len(newly_caught)}):")
        for f in newly_caught:
            print(f"      {f}")
    # Show the contamination that was removed.
    contaminated = {p: sorted(set(fam0.get(p, [])) - set(families.get(p, [])))
                    for p in fam0}
    contaminated = {p: v for p, v in contaminated.items() if v}
    if contaminated:
        print("   misparse-induced family members REMOVED by decontamination:")
        for p, v in contaminated.items():
            print(f"      {p}: {v}")
    print()

    print("=== DERIVED federation families (parents merged across name drift) ===")
    for parent in sorted(families, key=lambda p: -len(families[p])):
        variants = sorted(family_members.get(parent, {parent}))
        vtxt = f"  [merged parents: {variants}]" if len(variants) > 1 else ""
        print(f"  {parent:22s} ({len(families[parent])} sub-units){vtxt}")
        print(f"      {families[parent]}")
    print(f"\n=== FLOATING / appendix sections (no stable parent, span >= {FLOAT_MIN_FAMILIES} families) ===")
    for tok, n in sorted(floating.items(), key=lambda x: -x[1]):
        print(f"  {tok:30s} spans {n} families")

    heading_freq, column_freq = mine_headings(root, gazetteer)
    print(f"\n=== Top {args.top} heading texts (empirical section vocabulary) ===")
    for txt, n in heading_freq.most_common(args.top):
        print(f"  {n:6d}  {txt}")
    print(f"\n=== Top {args.top} table column headers (empirical indicator vocabulary) ===")
    for txt, n in column_freq.most_common(args.top):
        print(f"  {n:6d}  {txt}")

    # Reconciled (authoritative) map = derived UNION curated hand-seed. Derived
    # supplies well-evidenced extensions; curated supplies sparse-but-true facts
    # (Saskatchewan, UMS) the corpus is too thin to confirm on its own.
    reconciled = {ck: set(subs) for ck, subs in families.items()}
    for hk, hsubs in canon.SUB_UNITS.items():
        if len(hsubs) < 2:
            continue
        # Merge into a derived family only on a substring key match or >= 2 shared
        # members; a single shared island (e.g. Tobago) must NOT fuse Windward
        # into Trinidad & Tobago.
        match = next((ck for ck in reconciled
                      if ck in hk or hk in ck or len(reconciled[ck] & hsubs) >= 2), None)
        if match:
            reconciled[match] |= hsubs
        else:
            reconciled[hk] = set(hsubs)
    reconciled = {k: sorted(v) for k, v in reconciled.items()}

    if not args.stats:
        out = {
            "pipeline_version": PIPELINE_VERSION,
            "date_created": date.today().isoformat(),
            "thresholds": {"MIN_NESTINGS": MIN_NESTINGS, "MERGE_MIN_SHARED": MERGE_MIN_SHARED,
                           "FAMILY_SHARE": FAMILY_SHARE, "FLOAT_MIN_FAMILIES": FLOAT_MIN_FAMILIES,
                           "HUB_PARENT_LIMIT": HUB_PARENT_LIMIT,
                           "MISPARSE_UNRELATED": MISPARSE_UNRELATED},
            "decontamination": {
                "history": [{"stage": s, "excluded": n} for s, n in history],
                "excluded_misparse_files": sorted(exclude),
                "family_members_removed_as_contamination": contaminated,
            },
            "reconciled_families": reconciled,
            "families": families,
            "family_parent_variants": {p: sorted(v) for p, v in family_members.items()
                                       if p in families},
            "floating_sections": sorted(floating),
            "regional_cross_reference": sorted(regional),
            "heading_frequency": dict(heading_freq.most_common(300)),
            "column_header_frequency": dict(column_freq.most_common(300)),
        }
        out_path = root / args.out
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
