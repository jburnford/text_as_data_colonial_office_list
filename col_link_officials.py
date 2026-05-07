"""
COL Stage 4a: Within-Colony Career Chain Linking
=================================================

Creates POSSIBLE_MATCH relationships between broken COL_Official stints
(same name, same colony) with uncertainty scores.

Publication gaps in the COL corpus (1890→1894, 1900→1905, 1912→1921,
1940→1946, etc.) split continuous careers into multiple stints. This
script links them with scored hypotheses, preserving all evidence.

Design principle: Under-link rather than over-link. Uncertainty is
never 0.0 without external verification.

Usage:
    python col_link_officials.py              # full run
    python col_link_officials.py --dry-run    # preview, no writes
    python col_link_officials.py --stats      # report
    python col_link_officials.py --clear      # remove POSSIBLE_MATCH edges
    python col_link_officials.py --colony X   # single colony
    python col_link_officials.py --force      # recompute scores

Requires:
    pip install neo4j
"""

import argparse
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
SCORE_VERSION = "1.1"
BATCH_SIZE = 500


def _load_dotenv():
    """Load .env file from repo root, handling special characters safely."""
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
# EXCLUSION RULES
# =============================================================================

BARE_MEMBER_POSITIONS = {
    "member", "member of parliament", "senator",
}
BARE_MEMBER_PREFIXES = (
    "member of the ",
)


def is_bare_member_position(position: str) -> bool:
    """Return True if a position is a bare legislative title (MP, Senator, etc.).

    These are too noisy for career linking — many common names appear as
    both colonial officials and parliamentarians, causing false positives.
    Parliamentary data is available from dedicated sources.
    """
    p = (position or "").strip().lower()
    return p in BARE_MEMBER_POSITIONS or any(
        p.startswith(pfx) for pfx in BARE_MEMBER_PREFIXES
    )


# =============================================================================
# DOMAIN CLASSIFIER
# =============================================================================

DOMAIN_KEYWORDS = {
    "EXECUTIVE": [
        "governor", "administrator", "colonial secretary", "chief secretary",
        "resident", "commissioner", "secretary of state", "premier",
        "lieutenant-governor", "high commissioner", "acting governor",
    ],
    "LEGAL": [
        "judge", "justice", "magistrate", "attorney", "solicitor",
        "advocate", "barrister", "registrar of deeds", "master of the court",
        "crown counsel", "legal", "law", "court", "judicial",
    ],
    "MEDICAL": [
        "surgeon", "physician", "medical", "health", "sanitary",
        "hospital", "nurse", "quarantine", "pathologist", "bacteriologist",
        "dispensary", "asylum", "lunatic",
    ],
    "FINANCE": [
        "treasurer", "auditor", "comptroller", "collector of customs",
        "customs", "revenue", "excise", "finance", "accountant",
        "paymaster", "receiver-general", "tax", "treasury",
    ],
    "WORKS": [
        "engineer", "public works", "works department", "architect",
        "roads", "bridges", "railways", "harbour", "waterworks",
        "irrigation", "drainage", "building",
    ],
    "SURVEY": [
        "surveyor", "survey", "lands", "land department", "cartographer",
        "geodetic", "trigonometrical", "topograph",
    ],
    "POLICE_PRISONS": [
        "police", "constabulary", "inspector-general of police",
        "prison", "gaol", "jail", "superintendent of prisons",
        "detective", "warden", "penal",
    ],
    "CLERGY": [
        "bishop", "archdeacon", "chaplain", "canon", "dean",
        "ecclesiastical", "church", "clergy", "reverend", "vicar",
    ],
    "EDUCATION": [
        "education", "school", "inspector of schools", "professor",
        "teacher", "university", "college", "training",
    ],
    "MILITARY": [
        "colonel", "major", "captain", "lieutenant",
        "major-general", "brigadier", "lieutenant-general",
        "military", "defence", "army", "regiment", "brigade",
        "commandant", "adjutant", "field marshal",
    ],
    "POSTAL_COMMS": [
        "postmaster", "postal", "post office", "telegraph",
        "telephone", "wireless", "communications",
    ],
    "AGRICULTURE": [
        "agriculture", "botanical", "veterinary", "forest",
        "conservator of forests", "entomologist", "geologist",
        "mines", "mining", "fisheries",
    ],
    "MARITIME": [
        "harbour master", "port", "marine", "shipping", "pilot",
        "lighthouse", "naval", "admiralty", "dock",
    ],
    "CLERICAL": [
        "clerk", "secretary", "assistant secretary", "typist",
        "private secretary", "office", "establishment",
    ],
    "LEGISLATIVE": [
        "legislative", "council", "assembly", "speaker",
        "hansard", "parliament",
    ],
}

# Domains considered compatible for career transitions
# Key insight from research: governors come from many domains (80% of cross-colony
# movers are governors). Survey directors become governors (Guggisberg), military
# officers become governors, legal officers become governors, etc.
PLAUSIBLE_TRANSITIONS = {
    # Executive ↔ most domains (governors come from everywhere)
    ("LEGAL", "EXECUTIVE"),
    ("EXECUTIVE", "LEGAL"),
    ("CLERICAL", "EXECUTIVE"),
    ("EXECUTIVE", "CLERICAL"),
    ("LEGISLATIVE", "EXECUTIVE"),
    ("EXECUTIVE", "LEGISLATIVE"),
    ("SURVEY", "EXECUTIVE"),       # e.g., Guggisberg: Director of Surveys → Governor
    ("EXECUTIVE", "SURVEY"),
    ("MILITARY", "EXECUTIVE"),     # military officers become governors
    ("EXECUTIVE", "MILITARY"),
    ("POLICE_PRISONS", "EXECUTIVE"),  # police/prison heads become governors
    ("EXECUTIVE", "POLICE_PRISONS"),
    ("FINANCE", "EXECUTIVE"),      # treasurers/auditors become governors
    ("EXECUTIVE", "FINANCE"),
    ("EDUCATION", "EXECUTIVE"),    # education directors become governors
    ("EXECUTIVE", "EDUCATION"),
    ("WORKS", "EXECUTIVE"),        # PWD directors become governors
    ("EXECUTIVE", "WORKS"),
    ("AGRICULTURE", "EXECUTIVE"),  # agriculture directors become governors
    ("EXECUTIVE", "AGRICULTURE"),
    # Technical/clerical transitions
    ("CLERICAL", "FINANCE"),
    ("FINANCE", "CLERICAL"),
    ("SURVEY", "WORKS"),
    ("WORKS", "SURVEY"),
    ("POLICE_PRISONS", "MILITARY"),
    ("MILITARY", "POLICE_PRISONS"),
    ("POSTAL_COMMS", "CLERICAL"),
    ("CLERICAL", "POSTAL_COMMS"),
    ("AGRICULTURE", "SURVEY"),
    ("SURVEY", "AGRICULTURE"),
    # Legislative crossovers
    ("LEGISLATIVE", "LEGAL"),
    ("LEGAL", "LEGISLATIVE"),
    ("LEGISLATIVE", "CLERICAL"),
    ("CLERICAL", "LEGISLATIVE"),
}


def classify_domain(position: str | None, department: str | None) -> str | None:
    """Classify a position/department into a career domain. Returns None if unknown."""
    text = ""
    if position:
        text += position.lower() + " "
    if department:
        text += department.lower()
    text = text.strip()
    if not text:
        return None

    scores = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        # Weight multi-word keywords higher (more specific)
        score = sum(len(kw.split()) for kw in keywords if kw in text)
        if score > 0:
            scores[domain] = score

    if not scores:
        return None
    return max(scores, key=scores.get)


def compute_domain_match(
    a_position: str | None, a_department: str | None,
    b_position: str | None, b_department: str | None,
) -> str:
    """Compute domain match category between two stints."""
    a_domain = classify_domain(a_position, a_department)
    b_domain = classify_domain(b_position, b_department)

    if a_domain is None or b_domain is None:
        return "unknown"

    if a_domain == b_domain:
        # Check if positions are textually similar for "exact" vs "overlap"
        a_pos = (a_position or "").lower().strip()
        b_pos = (b_position or "").lower().strip()
        if a_pos and b_pos and (a_pos == b_pos or a_pos in b_pos or b_pos in a_pos):
            return "exact"
        return "overlap"

    if (a_domain, b_domain) in PLAUSIBLE_TRANSITIONS:
        return "plausible"

    return "implausible"


# =============================================================================
# NAME SPECIFICITY
# =============================================================================

# Surnames where 2+ officials sharing the SAME FIRST INITIAL served in
# the same colony in the same year. This is the true collision risk — if
# two "Smith, J." officials overlap, a single-initial match is ambiguous.
# Generated from COL_Official data, last refreshed 2026-03-17. 520 entries.
COMMON_SURNAMES = {
    "adams", "agius", "albury", "alexander", "allen", "alleyne", "allison", "alves",
    "anderson", "andrews", "annan", "anslow", "argent", "armstrong", "austin", "back",
    "bailey", "bain", "baker", "barker", "barnard", "barton", "baynes", "beard",
    "belcher", "belcourt", "bell", "bellot", "bennett", "berridge", "berteau", "best",
    "bethel", "bindley", "black", "blackburn", "blanchard", "bonello", "boon", "borden",
    "borg cardona", "botha", "bourne", "bowe", "bradbury", "branch", "brassington", "brew",
    "briggs", "brink", "brooke", "brown", "bucke", "burnside", "burrowes", "bushe",
    "busuttil", "butler", "bynoe", "byrne", "calder", "caldwell", "cameron", "campbell",
    "carew", "carey", "caron", "carpenter", "carrington", "carroll", "cartwright", "carvosso",
    "cave", "chamberlain", "chambers", "chandler", "chantrell", "chapman", "charles", "clark",
    "clarke", "cloete", "cochrane", "coker", "cole", "colin", "collier", "collins",
    "collymore", "comeau", "comissiong", "conyers", "cooper", "copp", "cornish", "corry",
    "costello", "coster", "cox", "craig", "crawford", "culmer", "cunningham", "cusack",
    "daly", "daniel", "danner", "darrell", "davidson-houston", "davies", "davis", "dawson",
    "day", "de boissiere", "de boucherville", "de freitas", "de gruchy", "de kock", "de kretser", "de nobriga",
    "de saram", "de silva", "de smidt", "deeble", "dickson", "dissanaike", "dodds", "doherty",
    "donovan", "doorly", "dos remedios", "douglas", "dowling", "driberg", "drieberg", "du toit",
    "duke", "duncan", "duncombe", "dundas", "dunlop", "dunn", "durant", "easton",
    "eccles", "edmunds", "edwards", "effendi", "ekanayake", "eldridge", "eliot", "elliott",
    "ellis", "emiage", "espitalier-noel", "evans", "evelyn", "evershed", "eynaud", "facey",
    "farfan", "farquharson", "faure", "fenton", "fernando", "fisher", "fitzgerald", "fletcher",
    "forbes", "foster", "fowlds", "franklin", "fraser", "frazer", "freeman", "frith",
    "fuller", "gabourel", "galea", "galizia", "gall", "gallant", "ganteaume",
    "garraway", "gawler", "gayner", "gentle", "geoffrion", "george", "gibbon", "giblin",
    "gibson", "gill", "godwin", "goodridge", "gordon", "graham", "grant", "greathead",
    "greaves", "green", "gregory", "grenier", "greyling", "griffith", "gurney", "gutierrez",
    "hale", "hales", "hall", "harding", "harrington", "harris", "harrison", "hart",
    "hartley", "harvey", "haynes", "hayward", "hedberg", "heidenstam", "henderson", "henshaw",
    "herbert", "hickson", "hill", "hislop", "hodge", "hodgson", "hoets", "hofmeyr",
    "holland", "holm", "holman", "holmes", "homagee", "honey", "hood", "hopkins",
    "houstoun", "howden", "howell", "howlan", "huggins", "hughes", "humphrey", "humphrys",
    "hungerford", "hunter", "hussein", "husseini", "hussey", "hutchinson", "ibbott", "immelman",
    "jackson", "james", "jayasinghe", "jenkins", "john", "johnson", "johnston", "johnstone",
    "jones", "kannangara", "kaye", "keating", "kennedy", "kenny", "kerr", "khalidi",
    "khan", "killam", "king", "kirk", "kirkbride", "knaggs", "knight", "kretser",
    "krickenbeck", "kuys", "la billois", "la croix", "lane", "laryea", "lassalle", "laurence",
    "lavers", "lavoipierre", "lawrence", "le gendre", "lee", "leembruggen", "legge", "leigh",
    "levy", "lewis", "lightbourn", "livingston", "logan", "longmore", "loos", "lovett",
    "lucie-smith", "lyons", "macauley", "macdiarmid", "macdonald", "macgillivray", "machado", "macintyre",
    "mackay", "mackenzie", "maclean", "maclure", "macwilliam", "magnan", "mair", "march",
    "marchand", "marshall", "martin", "martins", "massiah", "masson", "mccallan", "mcdonald",
    "mcdougall", "mcfarlane", "mckay", "mckinnon", "mclaughlin", "mclean", "mclellan", "mcleod",
    "mcneill", "mensah", "middleton", "miller", "mills", "milne", "mitchell", "molteno",
    "moore", "morgan", "morris", "morrison", "moss", "moutou", "mowbray", "murray",
    "myers", "nash", "neale", "nesbitt", "newbold", "newsam", "noonan", "o'brien",
    "o'shaughnessy", "oakes", "obaldia", "oldham", "orpen", "orrett", "otway", "owen",
    "page", "palmer", "panton", "parker", "parsons", "pasea", "passingham", "paterson",
    "patterson", "paul", "pearce", "pearson", "perera", "perley", "peterswald", "phillips",
    "pieris", "piguenit", "pitman", "pitot", "plagemann", "pollard", "pope", "porter",
    "potter", "pouchet", "power", "pratt", "preston", "price", "pullar", "pullicino",
    "quartey", "quartey-papafio", "quaye", "rae", "ragg", "rainier", "ramson", "randon",
    "ratnatunga", "reece", "reed", "reid", "renton", "rice", "richards", "richardson",
    "risler", "ritchie", "roberts", "robertson", "robinson", "robson", "roche", "rodriguez",
    "rogers", "rooks", "rose", "ross", "rowe", "russell", "ryan", "sabido",
    "sampson", "sands", "saunders", "savage", "sawyer", "schokman", "scott", "searcy",
    "seniloli", "shaw", "short", "simpson", "skeete", "small", "smith", "smuts",
    "smyth", "solomon", "spyker", "squires", "st. julian", "stabb", "stacey", "stevens",
    "stevenson", "stewart", "stokes", "stone", "stops", "stoute", "stow", "swain",
    "sykes", "symonds", "taschereau", "taylor", "teuma", "theron", "thibou", "thomas",
    "thompson", "thomson", "townshend", "tucker", "tunks", "turnbull", "turner", "upington",
    "usher", "vaughan", "venn", "wadham", "walcott", "walker", "wall", "walton",
    "ward", "warner", "warren", "waterhouse", "watermeyer", "watson", "weatherhead", "webb",
    "webster", "weir", "wells", "wheatley", "white", "whittell", "wickremasinghe", "widdup",
    "wight", "wiles", "wilhelm", "williams", "willoughby", "wilson", "winter", "wood",
    "wootton", "wright", "xuereb", "yearwood", "yeo", "yerriah", "young", "ziai-ud-din",
}


def compute_name_specificity(name: str) -> str:
    """Classify how distinctive a name is for matching confidence.

    Returns: 'high' (2+ initials or full given name), 'medium' (1 initial,
    uncommon surname), 'low' (1 initial + common surname, or no given name).
    """
    parts = name.split(", ", 1)
    surname = parts[0].lower().strip()
    given = parts[1].strip() if len(parts) == 2 else ""

    # Count initial-style tokens (single letter with optional period)
    initials = re.findall(r"\b[A-Z]\.?(?:\s|$)", given)
    n_initials = len(initials)

    # Full given name (e.g., "Samuel" not "S.")
    has_full_name = bool(re.search(r"[A-Za-z]{3,}", given))

    if n_initials >= 2 or has_full_name:
        return "high"
    elif n_initials == 1 and surname not in COMMON_SURNAMES:
        return "medium"
    else:
        return "low"


# =============================================================================
# UNCERTAINTY SCORE
# =============================================================================

def compute_uncertainty(editions_missed: int, editions_gap: int,
                        domain_match: str, a_editions: int, b_editions: int,
                        name_specificity: str = "medium",
                        wikidata_verified: bool = False) -> float:
    if wikidata_verified:
        return 0.0

    # 1. Missed editions penalty (strong — concrete evidence of absence)
    missed_penalty = min(0.70, editions_missed * 0.18)

    # 2. Gap editions penalty (weak — pure uncertainty)
    gap_penalty = min(0.20, editions_gap * 0.015)

    # 3. Base uncertainty (never 0 without verification)
    base = 0.03

    # 4. Domain match modifier
    domain_mod = {
        "exact":       -0.08,
        "overlap":     -0.04,
        "plausible":    0.0,
        "unknown":      0.05,
        "implausible":  0.25,
    }.get(domain_match, 0.05)

    # 5. Tenure bonus — longer stints on both sides = more confident
    min_tenure = min(a_editions, b_editions)
    tenure_bonus = min(0.12, min_tenure * 0.02)

    # 6. Name specificity modifier
    #    "E. C. Dear" (high) is far more distinctive than "C. Williams" (low)
    name_mod = {
        "high":   -0.06,   # 2+ initials or full given name — strong identity signal
        "medium":  0.0,    # 1 initial, uncommon surname — baseline
        "low":     0.08,   # 1 initial + common surname, or bare surname — collision risk
    }.get(name_specificity, 0.0)

    score = base + missed_penalty + gap_penalty + domain_mod + name_mod - tenure_bonus
    return round(max(0.02, min(1.0, score)), 3)


# =============================================================================
# COLONY YEAR INDEX
# =============================================================================

def build_colony_year_index(session) -> dict[str, set[int]]:
    """Query COL_TerritoryYear to get per-colony edition coverage."""
    result = session.run(
        "MATCH (ty:COL_TerritoryYear) "
        "RETURN ty.name AS colony, ty.year AS year"
    )
    index = defaultdict(set)
    for record in result:
        index[record["colony"]].add(record["year"])
    return dict(index)


# =============================================================================
# CANDIDATE PAIRS
# =============================================================================

CANDIDATE_QUERY = """
MATCH (a:COL_Official), (b:COL_Official)
WHERE a.name = b.name AND a.colony = b.colony
  AND a.last_year < b.first_year
  AND id(a) < id(b)
MATCH (pra:COL_PersonRecord)-[:RECORD_OF]->(a)
WHERE pra.year = a.last_year
MATCH (prb:COL_PersonRecord)-[:RECORD_OF]->(b)
WHERE prb.year = b.first_year
RETURN
  a.id AS a_id, b.id AS b_id,
  a.colony AS colony, a.name AS name,
  a.last_year AS a_last_year, b.first_year AS b_first_year,
  a.editions AS a_editions, b.editions AS b_editions,
  pra.position_raw AS a_last_position,
  pra.department_raw AS a_last_dept,
  prb.position_raw AS b_first_position,
  prb.department_raw AS b_first_dept
"""

CANDIDATE_QUERY_COLONY = """
MATCH (a:COL_Official), (b:COL_Official)
WHERE a.name = b.name AND a.colony = b.colony
  AND a.colony = $colony
  AND a.last_year < b.first_year
  AND id(a) < id(b)
MATCH (pra:COL_PersonRecord)-[:RECORD_OF]->(a)
WHERE pra.year = a.last_year
MATCH (prb:COL_PersonRecord)-[:RECORD_OF]->(b)
WHERE prb.year = b.first_year
RETURN
  a.id AS a_id, b.id AS b_id,
  a.colony AS colony, a.name AS name,
  a.last_year AS a_last_year, b.first_year AS b_first_year,
  a.editions AS a_editions, b.editions AS b_editions,
  pra.position_raw AS a_last_position,
  pra.department_raw AS a_last_dept,
  prb.position_raw AS b_first_position,
  prb.department_raw AS b_first_dept
"""


def fetch_candidates(session, colony: str | None = None) -> list[dict]:
    """Fetch all candidate pairs for POSSIBLE_MATCH linking."""
    if colony:
        result = session.run(CANDIDATE_QUERY_COLONY, colony=colony)
    else:
        result = session.run(CANDIDATE_QUERY)
    return [dict(r) for r in result]


# =============================================================================
# EVIDENCE COMPUTATION
# =============================================================================

def compute_evidence(pair: dict, colony_year_index: dict[str, set[int]]) -> dict:
    """Compute evidence fields for a candidate pair."""
    colony = pair["colony"]
    a_last = pair["a_last_year"]
    b_first = pair["b_first_year"]

    gap_years = b_first - a_last

    # Which years the colony has data BETWEEN the two stints (exclusive)
    colony_years = colony_year_index.get(colony, set())
    editions_between = {y for y in colony_years if a_last < y < b_first}
    editions_missed = len(editions_between)
    editions_gap = max(0, gap_years - 1 - editions_missed)

    domain_match = compute_domain_match(
        pair["a_last_position"], pair["a_last_dept"],
        pair["b_first_position"], pair["b_first_dept"],
    )

    a_editions = len(pair["a_editions"]) if pair["a_editions"] else 3
    b_editions = len(pair["b_editions"]) if pair["b_editions"] else 3

    name_spec = compute_name_specificity(pair["name"])

    uncertainty = compute_uncertainty(
        editions_missed, editions_gap, domain_match,
        a_editions, b_editions, name_spec,
    )

    return {
        "a_id": pair["a_id"],
        "b_id": pair["b_id"],
        "props": {
            "uncertainty": uncertainty,
            "score_version": SCORE_VERSION,
            "gap_years": gap_years,
            "editions_missed": editions_missed,
            "editions_gap": editions_gap,
            "domain_match": domain_match,
            "name_specificity": name_spec,
            "a_last_position": pair["a_last_position"],
            "b_first_position": pair["b_first_position"],
            "a_last_dept": pair["a_last_dept"],
            "b_first_dept": pair["b_first_dept"],
            "a_editions": a_editions,
            "b_editions": b_editions,
            "method": "automated_linking",
            "date_created": date.today().isoformat(),
        },
    }


# =============================================================================
# WRITE TO NEO4J
# =============================================================================

MERGE_QUERY = """
UNWIND $batch AS rec
MATCH (a:COL_Official {id: rec.a_id})
MATCH (b:COL_Official {id: rec.b_id})
MERGE (a)-[r:POSSIBLE_MATCH]->(b)
SET r += rec.props
"""

MERGE_QUERY_PRESERVE = """
UNWIND $batch AS rec
MATCH (a:COL_Official {id: rec.a_id})
MATCH (b:COL_Official {id: rec.b_id})
MERGE (a)-[r:POSSIBLE_MATCH]->(b)
SET r.uncertainty = rec.props.uncertainty,
    r.score_version = rec.props.score_version,
    r.gap_years = rec.props.gap_years,
    r.editions_missed = rec.props.editions_missed,
    r.editions_gap = rec.props.editions_gap,
    r.domain_match = rec.props.domain_match,
    r.a_last_position = rec.props.a_last_position,
    r.b_first_position = rec.props.b_first_position,
    r.a_last_dept = rec.props.a_last_dept,
    r.b_first_dept = rec.props.b_first_dept,
    r.a_editions = rec.props.a_editions,
    r.b_editions = rec.props.b_editions,
    r.method = rec.props.method,
    r.date_created = rec.props.date_created
"""


def write_links(session, evidence_list: list[dict], force: bool = False):
    """Write POSSIBLE_MATCH edges in batches."""
    query = MERGE_QUERY_PRESERVE if force else MERGE_QUERY
    total = 0
    for i in range(0, len(evidence_list), BATCH_SIZE):
        batch = evidence_list[i:i + BATCH_SIZE]
        session.run(query, batch=batch)
        total += len(batch)
    return total


# =============================================================================
# STATS
# =============================================================================

def print_stats(driver):
    """Report on POSSIBLE_MATCH edges."""
    with driver.session() as session:
        print("\n" + "=" * 60)
        print("POSSIBLE_MATCH LINKING STATISTICS")
        print("=" * 60)

        r = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH]->() RETURN count(r) AS c"
        ).single()
        total = r["c"]
        print(f"\n  Total POSSIBLE_MATCH edges: {total}")

        if total == 0:
            print("  No edges found.")
            return

        # Score distribution
        print("\n  Uncertainty score distribution:")
        result = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH]->() "
            "WITH CASE "
            "  WHEN r.uncertainty < 0.1 THEN '0.00-0.09' "
            "  WHEN r.uncertainty < 0.2 THEN '0.10-0.19' "
            "  WHEN r.uncertainty < 0.3 THEN '0.20-0.29' "
            "  WHEN r.uncertainty < 0.4 THEN '0.30-0.39' "
            "  WHEN r.uncertainty < 0.5 THEN '0.40-0.49' "
            "  WHEN r.uncertainty < 0.6 THEN '0.50-0.59' "
            "  WHEN r.uncertainty < 0.7 THEN '0.60-0.69' "
            "  WHEN r.uncertainty < 0.8 THEN '0.70-0.79' "
            "  WHEN r.uncertainty < 0.9 THEN '0.80-0.89' "
            "  ELSE '0.90-1.00' "
            "END AS bucket, count(*) AS n "
            "RETURN bucket, n ORDER BY bucket"
        )
        for record in result:
            bar = "█" * max(1, record["n"] * 40 // total)
            print(f"    {record['bucket']}  {record['n']:>5}  {bar}")

        # Domain match breakdown
        print("\n  Domain match breakdown:")
        result = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH]->() "
            "RETURN r.domain_match AS dm, count(*) AS n, "
            "       round(avg(r.uncertainty) * 1000) / 1000 AS avg_unc "
            "ORDER BY n DESC"
        )
        for record in result:
            print(f"    {record['dm']:<15} {record['n']:>5}  "
                  f"avg uncertainty: {record['avg_unc']:.3f}")

        # Editions missed breakdown
        print("\n  Editions missed breakdown:")
        result = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH]->() "
            "WHERE r.editions_missed IS NOT NULL "
            "RETURN r.editions_missed AS missed, count(*) AS n, "
            "       round(avg(r.uncertainty) * 1000) / 1000 AS avg_unc "
            "ORDER BY missed"
        )
        for record in result:
            print(f"    missed={record['missed']:<3}  {record['n']:>5} edges  "
                  f"avg uncertainty: {record['avg_unc']:.3f}")

        # Verified edges
        result = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH]->() "
            "WHERE r.verified_by IS NOT NULL "
            "RETURN r.verified_by AS method, count(*) AS n"
        )
        verified = list(result)
        if verified:
            print("\n  Verified edges:")
            for record in verified:
                print(f"    {record['method']}: {record['n']}")

        # Top colonies by edge count
        print("\n  Top 15 colonies by POSSIBLE_MATCH edges:")
        result = session.run(
            "MATCH (a:COL_Official)-[r:POSSIBLE_MATCH]->() "
            "RETURN a.colony AS colony, count(r) AS n "
            "ORDER BY n DESC LIMIT 15"
        )
        for record in result:
            print(f"    {record['colony']:<40} {record['n']:>5}")


# =============================================================================
# DRY RUN
# =============================================================================

def dry_run_report(evidence_list: list[dict]):
    """Preview linking results without writing."""
    print("\n" + "=" * 60)
    print("[DRY RUN] PREVIEW")
    print("=" * 60)

    print(f"\n  Candidate pairs found: {len(evidence_list)}")

    if not evidence_list:
        print("  No pairs to link.")
        return

    # Score distribution
    buckets = defaultdict(int)
    for ev in evidence_list:
        score = ev["props"]["uncertainty"]
        bucket = int(score * 10)
        bucket = min(bucket, 9)
        label = f"{bucket/10:.1f}0-{(bucket+1)/10:.1f}{'0' if bucket < 9 else ''}"
        buckets[label] += 1

    print("\n  Uncertainty score distribution:")
    for label in sorted(buckets):
        n = buckets[label]
        bar = "█" * max(1, n * 40 // len(evidence_list))
        print(f"    {label:<10}  {n:>5}  {bar}")

    # Domain match
    dm_counts = defaultdict(int)
    dm_scores = defaultdict(list)
    for ev in evidence_list:
        dm = ev["props"]["domain_match"]
        dm_counts[dm] += 1
        dm_scores[dm].append(ev["props"]["uncertainty"])

    print("\n  Domain match breakdown:")
    for dm in sorted(dm_counts, key=dm_counts.get, reverse=True):
        avg_s = sum(dm_scores[dm]) / len(dm_scores[dm])
        print(f"    {dm:<15} {dm_counts[dm]:>5}  avg uncertainty: {avg_s:.3f}")

    # Editions missed
    missed_counts = defaultdict(int)
    missed_scores = defaultdict(list)
    for ev in evidence_list:
        m = ev["props"]["editions_missed"]
        missed_counts[m] += 1
        missed_scores[m].append(ev["props"]["uncertainty"])

    print("\n  Editions missed breakdown:")
    for m in sorted(missed_counts):
        avg_s = sum(missed_scores[m]) / len(missed_scores[m])
        print(f"    missed={m:<3}  {missed_counts[m]:>5} pairs  "
              f"avg uncertainty: {avg_s:.3f}")

    # Sample pairs at different score levels
    sorted_ev = sorted(evidence_list, key=lambda e: e["props"]["uncertainty"])
    print("\n  Sample pairs (low uncertainty = likely same):")
    samples = []
    if len(sorted_ev) >= 3:
        samples = [sorted_ev[0], sorted_ev[len(sorted_ev) // 2], sorted_ev[-1]]
    else:
        samples = sorted_ev

    for ev in samples:
        p = ev["props"]
        print(f"    {p['uncertainty']:.3f}  missed={p['editions_missed']} "
              f"gap={p['editions_gap']} domain={p['domain_match']}")
        print(f"           a_id={ev['a_id']}")
        print(f"           b_id={ev['b_id']}")
        print(f"           a_pos: {p['a_last_position']}")
        print(f"           b_pos: {p['b_first_position']}")

    print("\n[DRY RUN] No data written.")


# =============================================================================
# CLEAR
# =============================================================================

def clear_likely_same(driver):
    """Remove all POSSIBLE_MATCH edges."""
    with driver.session() as session:
        r = session.run(
            "MATCH ()-[r:POSSIBLE_MATCH]->() DELETE r RETURN count(r) AS c"
        ).single()
        print(f"Deleted {r['c']} POSSIBLE_MATCH edges.")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Stage 4a: Within-colony career chain linking"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without writing to Neo4j")
    parser.add_argument("--stats", action="store_true",
                        help="Report POSSIBLE_MATCH statistics")
    parser.add_argument("--clear", action="store_true",
                        help="Remove all POSSIBLE_MATCH edges")
    parser.add_argument("--colony", type=str,
                        help="Filter to specific colony")
    parser.add_argument("--force", action="store_true",
                        help="Recompute scores (preserves verified_by/verified_date)")
    parser.add_argument("--ml-score", action="store_true",
                        help="After linking, apply ML scorer to write ml_uncertainty")
    args = parser.parse_args()

    print("=" * 60)
    print("COL STAGE 4a: WITHIN-COLONY CAREER CHAIN LINKING")
    print("=" * 60)

    # Connect to Neo4j
    print(f"\nConnecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        driver.verify_connectivity()
        print("Connected.")

        # --- Stats only ---
        if args.stats:
            print_stats(driver)
            return

        # --- Clear ---
        if args.clear:
            clear_likely_same(driver)
            return

        # --- Build colony year index ---
        print("\nBuilding colony year index...")
        with driver.session() as session:
            colony_year_index = build_colony_year_index(session)
        print(f"  {len(colony_year_index)} colonies with edition data")

        # --- Fetch candidates ---
        print("Fetching candidate pairs...")
        with driver.session() as session:
            candidates = fetch_candidates(session, colony=args.colony)
        print(f"  {len(candidates)} candidate pairs found")

        # Exclude bare legislative members (MPs, Senators)
        before = len(candidates)
        candidates = [
            p for p in candidates
            if not is_bare_member_position(p.get("a_last_position"))
            and not is_bare_member_position(p.get("b_first_position"))
        ]
        excluded = before - len(candidates)
        if excluded:
            print(f"  Excluded {excluded} pairs (bare legislative member)")

        if not candidates:
            print("\nNo candidate pairs found. Nothing to do.")
            return

        # --- Compute evidence ---
        print("Computing evidence and scores...")
        evidence_list = []
        for pair in candidates:
            evidence_list.append(compute_evidence(pair, colony_year_index))

        # --- Dry run or write ---
        if args.dry_run:
            dry_run_report(evidence_list)
            return

        print(f"Writing {len(evidence_list)} POSSIBLE_MATCH edges...")
        with driver.session() as session:
            written = write_links(session, evidence_list, force=args.force)
        print(f"  {written} edges written.")

        # --- Final stats ---
        print_stats(driver)

        # --- Optional ML scoring ---
        if args.ml_score:
            print("\nApplying ML scorer...")
            try:
                from col_ml_score import load_model, score_edges, write_scores_to_neo4j
                from col_ml_features import fetch_all_edges
                model, scaler, feature_cols = load_model("gb")
                with driver.session() as session:
                    edges = fetch_all_edges(session)
                    results = score_edges(edges, model, scaler, feature_cols)
                    written = write_scores_to_neo4j(session, results, "gb")
                    print(f"  ML scores written to {written} edges")
            except Exception as e:
                print(f"  ML scoring failed: {e}")
                print("  Run col_ml_train.py first to train the model")

    finally:
        driver.close()

    print("\nDone.")


if __name__ == "__main__":
    main()
