"""
Rule-Based Pre-Clustering for Stage 3 Normalization
=====================================================

Deterministic regex rules for clustering department names and position titles.
Handles ~60% of departments and ~40% of positions with HIGH confidence.
Remaining items pass through to LLM-assisted clustering or manual review.

Usage:
    from normalize_rules import cluster_departments, cluster_positions

    dept_clusters, dept_unclustered = cluster_departments(raw_dept_counts)
    pos_clusters, pos_unclustered = cluster_positions(raw_pos_counts)
"""

import re
from collections import defaultdict


# =============================================================================
# DEPARTMENT CLUSTERING RULES
# =============================================================================

# Each entry: cluster_id -> {canonical_name, career_track, patterns[]}
# Patterns are compiled regexes matched against lowercased department names.

DEPARTMENT_RULES = {
    "civil_establishment": {
        "canonical_name": "Civil Establishment",
        "career_track": None,  # catch-all, no single track
        "patterns": [
            r"^civil\s+establishment$",
            r"^civil\s+service$",
            r"^general\s+establishment$",
        ],
    },
    "executive_council": {
        "canonical_name": "Executive Council",
        "career_track": "Administrative",
        "patterns": [
            r"^executive\s+council$",
            r"^ex(?:ec)?\.?\s+council$",
        ],
    },
    "legislative_council": {
        "canonical_name": "Legislative Council",
        "career_track": "Administrative",
        "patterns": [
            r"^legislative\s+council$",
            r"^leg(?:is)?\.?\s+council$",
            r"^legislative\s+assembly$",
        ],
    },
    "colonial_secretary": {
        "canonical_name": "Colonial Secretary's Office",
        "career_track": "Administrative",
        "patterns": [
            r"^colonial\s+secretary.s?\s+(office|department)$",
            r"^colonial\s+secretary$",
            r"^col(?:onial)?\.?\s+sec(?:retary)?\.?(?:'s)?\s*(office|dept\.?|department)?$",
            r"^secretariat$",
            r"^chief\s+secretary.s?\s+(office|department)$",
        ],
    },
    "governor": {
        "canonical_name": "Governor's Office",
        "career_track": "Administrative",
        "patterns": [
            r"^governor.?s?\s*(office|staff|establishment)?$",
            r"^government\s+house$",
            r"^lieutenant[- ]governor.?s?\s*(office)?$",
            r"^administrator.?s?\s*(office)?$",
            r"^high\s+commissioner.?s?\s*(office)?$",
        ],
    },
    "treasury": {
        "canonical_name": "Treasury",
        "career_track": "Financial",
        "patterns": [
            r"^(the\s+)?treasury(\s+department)?$",
            r"^treasurer.?s?\s+(office|department)$",
            r"^colonial\s+treasury$",
            r"^public\s+treasury$",
        ],
    },
    "audit": {
        "canonical_name": "Audit Department",
        "career_track": "Financial",
        "patterns": [
            r"^audit(\s+department|\s+office)?$",
            r"^auditor[- ]general.?s?\s*(office|department)?$",
            r"^audit\s+and\s+accounts$",
        ],
    },
    "customs": {
        "canonical_name": "Customs Department",
        "career_track": "Financial",
        "patterns": [
            r"^customs(\s+department)?$",
            r"^customs\s+and\s+excise$",
            r"^collector\s+of\s+customs$",
            r"^customs\s+and\s+inland\s+revenue$",
        ],
    },
    "medical": {
        "canonical_name": "Medical Department",
        "career_track": "Medical",
        "patterns": [
            r"^medical(\s+department|\s+establishment)?$",
            r"^medical\s+and\s+sanitary(\s+department)?$",
            r"^medical\s+and\s+health(\s+department|\s+services?)?$",
            r"^medical\s+service$",
            r"^health\s+department$",
            r"^department\s+of\s+medical\s+services?$",
        ],
    },
    "judicial": {
        "canonical_name": "Judicial Department",
        "career_track": "Legal",
        "patterns": [
            r"^judicial(\s+department|\s+establishment)?$",
            r"^judiciary$",
            r"^judicial\s+and\s+legal$",
        ],
    },
    "attorney_general": {
        "canonical_name": "Attorney-General's Office",
        "career_track": "Legal",
        "patterns": [
            r"^attorney[- ]general.?s?\s*(office|department|chambers?)?$",
            r"^law\s+officers?$",
            r"^legal\s+department$",
            r"^legal\s+adviser.?s?\s*(office|department)?$",
        ],
    },
    "police": {
        "canonical_name": "Police Department",
        "career_track": "Police",
        "patterns": [
            r"^police(\s+department|\s+force|\s+establishment)?$",
            r"^police\s+and\s+gaols?$",
            r"^police\s+and\s+prisons?$",
            r"^constabulary$",
        ],
    },
    "prisons": {
        "canonical_name": "Prisons Department",
        "career_track": "Police",
        "patterns": [
            r"^prisons?(\s+department|\s+establishment)?$",
            r"^gaols?(\s+department|\s+establishment)?$",
            r"^gaol$",
        ],
    },
    "public_works": {
        "canonical_name": "Public Works Department",
        "career_track": "Engineering",
        "patterns": [
            r"^public\s+works(\s+department)?$",
            r"^p\.?\s*w\.?\s*d\.?$",
            r"^works\s+department$",
            r"^department\s+of\s+public\s+works$",
        ],
    },
    "survey": {
        "canonical_name": "Survey Department",
        "career_track": "Survey",
        "patterns": [
            r"^survey(\s+department)?$",
            r"^surveyor[- ]general.?s?\s*(office|department)?$",
            r"^lands?\s+and\s+survey(s)?(\s+department)?$",
            r"^survey\s+and\s+lands?$",
        ],
    },
    "education": {
        "canonical_name": "Education Department",
        "career_track": "Education",
        "patterns": [
            r"^education(al)?(\s+department)?$",
            r"^department\s+of\s+education$",
            r"^public\s+instruction$",
            r"^director\s+of\s+education$",
        ],
    },
    "ecclesiastical": {
        "canonical_name": "Ecclesiastical Establishment",
        "career_track": "Ecclesiastical",
        "patterns": [
            r"^ecclesiastic(al)?(\s+department|\s+establishment)?(\s*\(.*\))?$",
            r"^ecclesiastic(al)?\s+establishments?\s+\(.*\)$",
            r"^church\s+establishment$",
            r"^clergy\b.*",
            r"^roman\s+catholic\s+church$",
            r"^pastoral\s+districts?$",
        ],
    },
    "postal": {
        "canonical_name": "Post Office",
        "career_track": "Postal",
        "patterns": [
            r"^post\s*[-.]?\s*office(\s+department)?$",
            r"^postal(\s+department|\s+service)?$",
            r"^general\s+post\s+office$",
            r"^post\s+and\s+telegraph(s)?(\s+department)?$",
            r"^posts?\s+and\s+telecommunications?$",
        ],
    },
    "telegraph": {
        "canonical_name": "Telegraph Department",
        "career_track": "Postal",
        "patterns": [
            r"^telegraph(\s+department)?$",
            r"^telegraphs$",
            r"^electric\s+telegraph$",
        ],
    },
    "railways": {
        "canonical_name": "Railway Department",
        "career_track": "Engineering",
        "patterns": [
            r"^railway(s)?(\s+department)?$",
            r"^government\s+railway(s)?$",
        ],
    },
    "harbour": {
        "canonical_name": "Harbour Department",
        "career_track": "Engineering",
        "patterns": [
            r"^harbour(\s+department|\s+office)?$",
            r"^harbor(\s+department)?$",
            r"^harbour\s+master.?s?\s*(office|department)?$",
            r"^marine(\s+department)?$",
            r"^port\s+(department|office|authority)$",
        ],
    },
    "printing": {
        "canonical_name": "Government Printing Office",
        "career_track": "Administrative",
        "patterns": [
            r"^(government\s+)?printing(\s+office|\s+department)?$",
            r"^government\s+printer$",
        ],
    },
    "registrar": {
        "canonical_name": "Registrar's Office",
        "career_track": "Legal",
        "patterns": [
            r"^registrar.?s?\s*(office|department)?$",
            r"^registrar[- ]general.?s?\s*(office|department)?$",
            r"^registration(\s+department)?$",
        ],
    },
    "crown_lands": {
        "canonical_name": "Crown Lands Department",
        "career_track": "Survey",
        "patterns": [
            r"^crown\s+lands?(\s+department|\s+office)?$",
            r"^lands?\s+department$",
            r"^commissioner\s+of\s+(crown\s+)?lands?$",
        ],
    },
    "immigration": {
        "canonical_name": "Immigration Department",
        "career_track": "Administrative",
        "patterns": [
            r"^immigration(\s+department|\s+office)?$",
            r"^emigration(\s+department)?$",
            r"^protector\s+of\s+immigrants?$",
        ],
    },
    "botanic_gardens": {
        "canonical_name": "Botanic Gardens",
        "career_track": "Agricultural",
        "patterns": [
            r"^botanic(al)?\s+gardens?(\s+department)?$",
            r"^botanical\s+department$",
        ],
    },
    "agriculture": {
        "canonical_name": "Agriculture Department",
        "career_track": "Agricultural",
        "patterns": [
            r"^agriculture(\s+department)?$",
            r"^agricultural(\s+department)?$",
            r"^department\s+of\s+agriculture$",
            r"^director\s+of\s+agriculture$",
        ],
    },
    "military": {
        "canonical_name": "Military Establishment",
        "career_track": "Military",
        "patterns": [
            r"^military(\s+department|\s+establishment)?$",
            r"^defence(\s+department|\s+force)?$",
            r"^defense(\s+department|\s+force)?$",
            r"^garrison$",
            r"^royal\s+engineers?$",
            r"^west\s+african?\s+frontier\s+force",
            r"^w\.?\s*a\.?\s*f\.?\s*f\.?$",
            r"^king.?s?\s+african?\s+rifles?",
            r"^k\.?\s*a\.?\s*r\.?$",
        ],
    },
    "consular": {
        "canonical_name": "Foreign Consuls",
        "career_track": None,  # not a colonial career track
        "patterns": [
            r"^foreign\s+consuls?$",
            r"^consular\s+(corps|body|agents?)$",
            r"^consuls?$",
        ],
    },
    "sanitary": {
        "canonical_name": "Sanitary Department",
        "career_track": "Medical",
        "patterns": [
            r"^sanitary(\s+department|\s+board|\s+authority)?$",
            r"^board\s+of\s+health$",
        ],
    },
    "forest": {
        "canonical_name": "Forest Department",
        "career_track": "Agricultural",
        "patterns": [
            r"^forest(s)?(\s+department)?$",
            r"^forestry(\s+department)?$",
            r"^conservator\s+of\s+forests?$",
        ],
    },
    "mines": {
        "canonical_name": "Mines Department",
        "career_track": "Engineering",
        "patterns": [
            r"^mines?(\s+department)?$",
            r"^mining(\s+department)?$",
            r"^geological\s+survey$",
            r"^inspector\s+of\s+mines?$",
        ],
    },
    "veterinary": {
        "canonical_name": "Veterinary Department",
        "career_track": "Agricultural",
        "patterns": [
            r"^veterinary(\s+department|\s+service)?$",
        ],
    },
    "supreme_court": {
        "canonical_name": "Supreme Court",
        "career_track": "Legal",
        "patterns": [
            r"^supreme\s+court$",
            r"^court\s+of\s+appeal$",
        ],
    },
    "district_courts": {
        "canonical_name": "District and Minor Courts",
        "career_track": "Legal",
        "patterns": [
            r"^district\s+and\s+minor\s+courts?$",
            r"^district\s+courts?$",
            r"^minor\s+courts?$",
            r"^magistrate.?s?\s+courts?$",
            r"^magistrates?\s+and\s+local\s+courts?$",
            r"^local\s+courts?$",
        ],
    },
    "district_administration": {
        "canonical_name": "District Administration",
        "career_track": "Administrative",
        "patterns": [
            r"^provincial\s+administration$",
            r"^district\s+administration$",
            r"^district\s+commissioners?$",
            r"^district\s+magistracy$",
            r"^provincial\s+and\s+district\s+administration$",
            r"^resident\s+commissioners?$",
            r"^provincial\s+commissioners?$",
        ],
    },
    "revenue": {
        "canonical_name": "Revenue Department",
        "career_track": "Financial",
        "patterns": [
            r"^revenue(\s+department)?$",
            r"^inland\s+revenue$",
            r"^internal\s+revenue$",
        ],
    },
    "convict": {
        "canonical_name": "Convict Department",
        "career_track": "Police",
        "patterns": [
            r"^convict(\s+department|\s+establishment)?$",
            r"^convict\s+service$",
        ],
    },
    "house_assembly": {
        "canonical_name": "House of Assembly",
        "career_track": "Administrative",
        "patterns": [
            r"^house\s+of\s+assembly$",
            r"^house\s+of\s+representatives$",
        ],
    },
    "justice": {
        "canonical_name": "Department of Justice",
        "career_track": "Legal",
        "patterns": [
            r"^department\s+of\s+justice$",
            r"^judicial\s+and\s+legal(\s+departments?)?$",
        ],
    },
    "government_agencies": {
        "canonical_name": "Government Agencies",
        "career_track": "Administrative",
        "patterns": [
            r"^government\s+agenc(y|ies)$",
            r"^government\s+agents?$",
        ],
    },
    "medical_officers": {
        "canonical_name": "Government Medical Officers",
        "career_track": "Medical",
        "patterns": [
            r"^government\s+medical\s+officers?$",
            r"^civil\s+medical(\s+department|\s+officers?)?$",
        ],
    },
    "public_health": {
        "canonical_name": "Public Health Department",
        "career_track": "Medical",
        "patterns": [
            r"^public\s+health(\s+department)?$",
        ],
    },
    "fire_brigade": {
        "canonical_name": "Fire Brigade",
        "career_track": "Police",
        "patterns": [
            r"^fire\s+(brigade|department|service)$",
        ],
    },
    "works_department": {
        "canonical_name": "Works Department",
        "career_track": "Engineering",
        "patterns": [
            r"^works(\s+department)?$",
            r"^department\s+of\s+works$",
        ],
    },
    "water_supply": {
        "canonical_name": "Water Supply Department",
        "career_track": "Engineering",
        "patterns": [
            r"^water\s+(supply|works?)(\s+department)?$",
        ],
    },
    "labour": {
        "canonical_name": "Labour Department",
        "career_track": "Administrative",
        "patterns": [
            r"^labou?r(\s+department|\s+office)?$",
        ],
    },
    "cooperative": {
        "canonical_name": "Co-operative Department",
        "career_track": "Agricultural",
        "patterns": [
            r"^co-?operative(\s+department|\s+societies)?$",
        ],
    },
}

# Compile all patterns once
_COMPILED_DEPT_RULES = {}
for cluster_id, rule in DEPARTMENT_RULES.items():
    _COMPILED_DEPT_RULES[cluster_id] = {
        **rule,
        "compiled": [re.compile(p, re.IGNORECASE) for p in rule["patterns"]],
    }


def cluster_departments(raw_counts: dict[str, int]) -> tuple[list[dict], list[dict]]:
    """Cluster department names using regex rules.

    Args:
        raw_counts: {raw_department_name: instance_count}

    Returns:
        (clusters, unclustered) where:
        - clusters: list of {id, canonical_name, career_track, members: [{raw, count, confidence}]}
        - unclustered: list of {raw, count}
    """
    # Track which names have been claimed
    claimed = {}  # raw_name -> cluster_id

    for raw_name, count in raw_counts.items():
        name_lower = raw_name.strip().lower()
        for cluster_id, rule in _COMPILED_DEPT_RULES.items():
            for pattern in rule["compiled"]:
                if pattern.match(name_lower):
                    claimed[raw_name] = cluster_id
                    break
            if raw_name in claimed:
                break

    # Build cluster output
    cluster_members = defaultdict(list)
    for raw_name, cluster_id in claimed.items():
        cluster_members[cluster_id].append({
            "raw": raw_name,
            "count": raw_counts[raw_name],
            "confidence": "HIGH",
            "method": "rule",
        })

    clusters = []
    for cluster_id, rule in DEPARTMENT_RULES.items():
        members = cluster_members.get(cluster_id, [])
        if not members:
            continue
        members.sort(key=lambda m: m["count"], reverse=True)
        clusters.append({
            "id": f"dept_{cluster_id}",
            "canonical_name": rule["canonical_name"],
            "career_track": rule["career_track"],
            "members": members,
        })

    clusters.sort(key=lambda c: sum(m["count"] for m in c["members"]), reverse=True)

    # Unclustered
    unclustered = []
    for raw_name, count in raw_counts.items():
        if raw_name not in claimed:
            unclustered.append({"raw": raw_name, "count": count})
    unclustered.sort(key=lambda x: x["count"], reverse=True)

    return clusters, unclustered


# =============================================================================
# POSITION PRE-NORMALIZATION
# =============================================================================

# Abbreviation expansions applied before clustering
ABBREVIATIONS = {
    # NOTE: Use \b on both sides of the abbreviation to prevent matching
    # prefixes of full words (e.g. "Gen" in "General", "Surg" in "Surgeon").
    r"\bcol\.\s*": "Colonial ",
    r"\basst\b\.?\s*": "Assistant ",
    r"\bass[tn]\b\.?\s+": "Assistant ",
    r"\bsupt\b\.?\s*": "Superintendent ",
    r"\bgovt\b\.?\s*": "Government ",
    r"\bdept\b\.?\s*": "Department ",
    r"\bsecy\b\.?\s*": "Secretary ",
    r"\bsec\b\.?\s+": "Secretary ",
    r"\bcommr\b\.?\s*": "Commissioner ",
    r"\bcomm?dt\b\.?\s*": "Commandant ",
    r"\binspr?\b\.?\s*": "Inspector ",
    r"\bmagist\b\.?\s*": "Magistrate ",
    r"\bsurg\b\.?\s*": "Surgeon ",
    r"\bphys\b\.?\s*": "Physician ",
    r"\bengr\b\.?\s*": "Engineer ",
    r"\bacct\b\.?\s*": "Accountant ",
    r"\bactg\b\.?\s*": "Acting ",
    r"\bdepty\b\.?\s*": "Deputy ",
    r"\bdep\b\.?\s+": "Deputy ",
    r"\bprinc\b\.?\s*": "Principal ",
    r"\bsenr?\b\.?\s+": "Senior ",
    r"\bjunr?\b\.?\s+": "Junior ",
    r"\bgen\b\.?\s*": "General ",
    r"\bsurvr?\b\.?\s*": "Surveyor ",
    r"\bregr\b\.?\s*": "Registrar ",
}

_COMPILED_ABBREVS = [
    (re.compile(pattern, re.IGNORECASE), replacement)
    for pattern, replacement in ABBREVIATIONS.items()
]

# Ordinal words to numbers
ORDINALS = {
    "first": "1st", "second": "2nd", "third": "3rd", "fourth": "4th",
    "fifth": "5th", "sixth": "6th", "seventh": "7th", "eighth": "8th",
    "ninth": "9th", "tenth": "10th",
}

# Grade extraction patterns
GRADE_PATTERNS = [
    # "2nd Clerk", "1st Class Clerk"
    re.compile(r"^(\d+)(?:st|nd|rd|th)\s+(?:class\s+)?(.+)$", re.IGNORECASE),
    # "Clerk, 1st Class"
    re.compile(r"^(.+?),?\s+(\d+)(?:st|nd|rd|th)\s+class$", re.IGNORECASE),
    # "Clerk Class I", "Clerk Class II"
    re.compile(r"^(.+?),?\s+class\s+(I{1,3}|IV|V|VI)$", re.IGNORECASE),
]

ROMAN_TO_INT = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6}

# Common plural -> singular
PLURALS = {
    r"clerks$": "Clerk",
    r"inspectors$": "Inspector",
    r"magistrates$": "Magistrate",
    r"surgeons$": "Surgeon",
    r"engineers$": "Engineer",
    r"officers$": "Officer",
    r"commissioners$": "Commissioner",
    r"constables$": "Constable",
    r"warders$": "Warder",
    r"overseers$": "Overseer",
    r"messengers$": "Messenger",
    r"interpreters$": "Interpreter",
}


def normalize_position_text(raw: str) -> str:
    """Normalize a position title string (lowercase, expand abbreviations, etc.)."""
    text = raw.strip()

    # Normalize dashes and quotes
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')

    # Strip trailing period
    text = text.rstrip(".")

    # Expand abbreviations
    for pattern, replacement in _COMPILED_ABBREVS:
        text = pattern.sub(replacement, text)

    # Normalize ordinal words
    for word, num in ORDINALS.items():
        text = re.sub(rf"\b{word}\b", num, text, flags=re.IGNORECASE)

    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Title case (but preserve numbers like "2nd")
    words = []
    for w in text.split():
        if w[0].isdigit() or w.isupper() and len(w) <= 4:
            words.append(w)
        else:
            words.append(w.capitalize())
    text = " ".join(words)

    return text


def extract_grade(normalized: str) -> tuple[str, int | None]:
    """Extract grade/class from a normalized position title.

    Returns (base_title, grade_level) where grade_level is an int or None.
    """
    for pattern in GRADE_PATTERNS:
        m = pattern.match(normalized)
        if m:
            groups = m.groups()
            if groups[0].isdigit():
                # "2nd Clerk" pattern
                grade = int(groups[0])
                base = groups[1].strip()
            elif groups[1] in ROMAN_TO_INT:
                # "Clerk Class II" pattern
                grade = ROMAN_TO_INT[groups[1]]
                base = groups[0].strip()
            else:
                try:
                    grade = int(groups[1])
                except ValueError:
                    continue
                base = groups[0].strip()
            return base, grade

    return normalized, None


def singularize(text: str) -> str:
    """Convert common plural position titles to singular."""
    for pattern, replacement in PLURALS.items():
        new = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        if new != text:
            return new
    return text


# =============================================================================
# POSITION CLUSTERING RULES
# =============================================================================

# Position family rules: {family_id: {canonical_name, career_track, patterns[]}}
POSITION_FAMILIES = {
    "governor": {
        "canonical_name": "Governor",
        "career_track": "Administrative",
        "patterns": [
            r"^governor$",
            r"^governor[- ]general$",
            r"^governor\s+and\s+commander[- ]in[- ]chief$",
        ],
    },
    "lieutenant_governor": {
        "canonical_name": "Lieutenant-Governor",
        "career_track": "Administrative",
        "patterns": [
            r"^lieutenant[- ]governor$",
            r"^lieut\.\s*governor$",
        ],
    },
    "administrator": {
        "canonical_name": "Administrator",
        "career_track": "Administrative",
        "patterns": [r"^administrator$"],
    },
    "colonial_secretary": {
        "canonical_name": "Colonial Secretary",
        "career_track": "Administrative",
        "patterns": [
            r"^colonial\s+secretary$",
            r"^chief\s+secretary$",
        ],
    },
    "assistant_colonial_secretary": {
        "canonical_name": "Assistant Colonial Secretary",
        "career_track": "Administrative",
        "patterns": [
            r"^assistant\s+colonial\s+secretary$",
            r"^assistant\s+chief\s+secretary$",
        ],
    },
    "treasurer": {
        "canonical_name": "Treasurer",
        "career_track": "Financial",
        "patterns": [
            r"^(colonial\s+)?treasurer$",
            r"^assistant\s+treasurer$",
        ],
    },
    "auditor": {
        "canonical_name": "Auditor",
        "career_track": "Financial",
        "patterns": [
            r"^auditor[- ]general$",
            r"^auditor$",
            r"^assistant\s+auditor$",
        ],
    },
    "collector_customs": {
        "canonical_name": "Collector of Customs",
        "career_track": "Financial",
        "patterns": [
            r"^collector\s+of\s+customs$",
            r"^comptroller\s+of\s+customs$",
        ],
    },
    "chief_justice": {
        "canonical_name": "Chief Justice",
        "career_track": "Legal",
        "patterns": [r"^chief\s+justice$"],
    },
    "puisne_judge": {
        "canonical_name": "Puisne Judge",
        "career_track": "Legal",
        "patterns": [
            r"^puisne\s+judge$",
            r"^puisne\s+justice$",
        ],
    },
    "attorney_general": {
        "canonical_name": "Attorney-General",
        "career_track": "Legal",
        "patterns": [
            r"^attorney[- ]general$",
        ],
    },
    "solicitor_general": {
        "canonical_name": "Solicitor-General",
        "career_track": "Legal",
        "patterns": [r"^solicitor[- ]general$"],
    },
    "magistrate": {
        "canonical_name": "Magistrate",
        "career_track": "Legal",
        "patterns": [
            r"^(police\s+|stipendiary\s+|district\s+|resident\s+)?magistrate$",
            r"^(police\s+|stipendiary\s+|district\s+|resident\s+)?magistrates$",
        ],
    },
    "colonial_surgeon": {
        "canonical_name": "Colonial Surgeon",
        "career_track": "Medical",
        "patterns": [
            r"^colonial\s+surgeon$",
        ],
    },
    "medical_officer": {
        "canonical_name": "Medical Officer",
        "career_track": "Medical",
        "patterns": [
            r"^(senior\s+|district\s+|assistant\s+)?medical\s+officer$",
            r"^principal\s+medical\s+officer$",
            r"^chief\s+medical\s+officer$",
        ],
    },
    "director_medical": {
        "canonical_name": "Director of Medical Services",
        "career_track": "Medical",
        "patterns": [
            r"^director\s+of\s+medical\s+services?$",
            r"^director\s+of\s+medical\s+and\s+sanitary\s+services?$",
        ],
    },
    "clerk": {
        "canonical_name": "Clerk",
        "career_track": None,  # depends on department context
        "patterns": [
            r"^clerk$",
            r"^clerks?$",
        ],
    },
    "chief_clerk": {
        "canonical_name": "Chief Clerk",
        "career_track": None,
        "patterns": [r"^chief\s+clerk$"],
    },
    "senior_clerk": {
        "canonical_name": "Senior Clerk",
        "career_track": None,
        "patterns": [r"^senior\s+clerk$"],
    },
    "inspector_general_police": {
        "canonical_name": "Inspector-General of Police",
        "career_track": "Police",
        "patterns": [
            r"^inspector[- ]general\s+of\s+police$",
            r"^commissioner\s+of\s+police$",
        ],
    },
    "inspector_police": {
        "canonical_name": "Inspector of Police",
        "career_track": "Police",
        "patterns": [
            r"^(assistant\s+|sub[- ]?)?inspector\s+of\s+police$",
            r"^(district\s+)?superintendent\s+of\s+police$",
        ],
    },
    "director_public_works": {
        "canonical_name": "Director of Public Works",
        "career_track": "Engineering",
        "patterns": [
            r"^director\s+of\s+public\s+works$",
            r"^colonial\s+engineer$",
        ],
    },
    "surveyor_general": {
        "canonical_name": "Surveyor-General",
        "career_track": "Survey",
        "patterns": [r"^surveyor[- ]general$"],
    },
    "director_education": {
        "canonical_name": "Director of Education",
        "career_track": "Education",
        "patterns": [
            r"^director\s+of\s+education$",
            r"^director\s+of\s+public\s+instruction$",
            r"^inspector\s+of\s+schools$",
        ],
    },
    "postmaster_general": {
        "canonical_name": "Postmaster-General",
        "career_track": "Postal",
        "patterns": [
            r"^postmaster[- ]general$",
            r"^postmaster$",
        ],
    },
    "bishop": {
        "canonical_name": "Bishop",
        "career_track": "Ecclesiastical",
        "patterns": [r"^bishop$", r"^lord\s+bishop$"],
    },
    "archdeacon": {
        "canonical_name": "Archdeacon",
        "career_track": "Ecclesiastical",
        "patterns": [r"^archdeacon$"],
    },
    "colonial_chaplain": {
        "canonical_name": "Colonial Chaplain",
        "career_track": "Ecclesiastical",
        "patterns": [
            r"^colonial\s+chaplain$",
            r"^chaplain$",
            r"^government\s+chaplain$",
        ],
    },
    "member": {
        "canonical_name": "Member",
        "career_track": None,  # depends on council context
        "patterns": [
            r"^member$",
            r"^unofficial\s+member$",
            r"^official\s+member$",
            r"^nominated\s+member$",
            r"^elected\s+member$",
            r"^ex[- ]officio\s+member$",
        ],
    },
    "director_agriculture": {
        "canonical_name": "Director of Agriculture",
        "career_track": "Agricultural",
        "patterns": [
            r"^director\s+of\s+agriculture$",
        ],
    },
    "registrar_general": {
        "canonical_name": "Registrar-General",
        "career_track": "Legal",
        "patterns": [
            r"^registrar[- ]general$",
            r"^registrar$",
        ],
    },
    "harbour_master": {
        "canonical_name": "Harbour Master",
        "career_track": "Engineering",
        "patterns": [
            r"^harbo[u]?r\s+master$",
        ],
    },
    "government_printer": {
        "canonical_name": "Government Printer",
        "career_track": "Administrative",
        "patterns": [r"^government\s+printer$"],
    },
    "superintendent_prisons": {
        "canonical_name": "Superintendent of Prisons",
        "career_track": "Police",
        "patterns": [
            r"^superintendent\s+of\s+(prisons?|gaols?)$",
            r"^inspector\s+of\s+prisons?$",
        ],
    },
    "collector_revenue": {
        "canonical_name": "Collector of Revenue",
        "career_track": "Financial",
        "patterns": [
            r"^collector\s+of\s+revenue$",
            r"^receiver[- ]general$",
        ],
    },
    "queen_king_advocate": {
        "canonical_name": "Queen's/King's Advocate",
        "career_track": "Legal",
        "patterns": [
            r"^(queen|king).?s\s+advocate$",
        ],
    },
    "protector_immigrants": {
        "canonical_name": "Protector of Immigrants",
        "career_track": "Administrative",
        "patterns": [
            r"^protector\s+of\s+immigrants?$",
            r"^agent[- ]general\s+of\s+immigration$",
        ],
    },
    "commissioner_lands": {
        "canonical_name": "Commissioner of Lands",
        "career_track": "Survey",
        "patterns": [
            r"^commissioner\s+of\s+(crown\s+)?lands?$",
        ],
    },
    "conservator_forests": {
        "canonical_name": "Conservator of Forests",
        "career_track": "Agricultural",
        "patterns": [r"^conservator\s+of\s+forests?$"],
    },
    "general_manager_railways": {
        "canonical_name": "General Manager of Railways",
        "career_track": "Engineering",
        "patterns": [
            r"^general\s+manager[,]?\s+(of\s+)?railway(s)?$",
        ],
    },
    "consul": {
        "canonical_name": "Consul",
        "career_track": None,
        "patterns": [
            r"^consul$",
            r"^(vice[- ])?consul$",
            r"^consul[- ]general$",
            r"^consular\s+agent$",
        ],
    },
    "inspector_general": {
        "canonical_name": "Inspector",
        "career_track": None,
        "patterns": [
            r"^inspector$",
            r"^sub[- ]?inspector$",
            r"^assistant\s+inspector$",
            r"^inspector[- ]general$",
        ],
    },
    "superintendent": {
        "canonical_name": "Superintendent",
        "career_track": None,
        "patterns": [
            r"^superintendent$",
            r"^superintending\s+officer$",
            r"^assistant\s+superintendent$",
        ],
    },
    "accountant": {
        "canonical_name": "Accountant",
        "career_track": "Financial",
        "patterns": [
            r"^(chief\s+|assistant\s+)?accountant$",
            r"^accountant[- ]general$",
        ],
    },
    "government_medical_officer": {
        "canonical_name": "Government Medical Officer",
        "career_track": "Medical",
        "patterns": [
            r"^government\s+medical\s+officer$",
        ],
    },
    "assistant_colonial_surgeon": {
        "canonical_name": "Assistant Colonial Surgeon",
        "career_track": "Medical",
        "patterns": [
            r"^assistant\s+colonial\s+surgeon$",
        ],
    },
    "sub_collector": {
        "canonical_name": "Sub-Collector",
        "career_track": "Financial",
        "patterns": [
            r"^sub[- ]collector$",
        ],
    },
    "commissioner": {
        "canonical_name": "Commissioner",
        "career_track": None,
        "patterns": [
            r"^commissioner$",
            r"^(district\s+|provincial\s+|resident\s+)?commissioner$",
            r"^deputy\s+commissioner$",
            r"^assistant\s+commissioner$",
        ],
    },
    "secretary": {
        "canonical_name": "Secretary",
        "career_track": "Administrative",
        "patterns": [
            r"^secretary$",
            r"^private\s+secretary$",
            r"^under[- ]secretary$",
        ],
    },
    "government_agent": {
        "canonical_name": "Government Agent",
        "career_track": "Administrative",
        "patterns": [
            r"^(assistant\s+)?government\s+agent$",
        ],
    },
    "district_officer": {
        "canonical_name": "District Officer",
        "career_track": "Administrative",
        "patterns": [
            r"^(assistant\s+)?district\s+officer$",
            r"^(assistant\s+)?political\s+officer$",
        ],
    },
    "surveyor": {
        "canonical_name": "Surveyor",
        "career_track": "Survey",
        "patterns": [
            r"^(district\s+|assistant\s+)?surveyor$",
        ],
    },
    "engineer": {
        "canonical_name": "Engineer",
        "career_track": "Engineering",
        "patterns": [
            r"^(assistant\s+|executive\s+|district\s+)?engineer$",
        ],
    },
    "collector": {
        "canonical_name": "Collector",
        "career_track": "Financial",
        "patterns": [
            r"^collector$",
            r"^assistant\s+collector$",
        ],
    },
    "dispenser": {
        "canonical_name": "Dispenser",
        "career_track": "Medical",
        "patterns": [
            r"^dispenser$",
            r"^assistant\s+dispenser$",
        ],
    },
    "cadet": {
        "canonical_name": "Cadet",
        "career_track": "Administrative",
        "patterns": [r"^cadet$"],
    },
    "crown_agent": {
        "canonical_name": "Crown Agent",
        "career_track": "Administrative",
        "patterns": [
            r"^crown\s+agents?(\s+for\s+the\s+colonies)?$",
        ],
    },
    "commissioner_police": {
        "canonical_name": "Commissioner of Police",
        "career_track": "Police",
        "patterns": [
            r"^(deputy\s+|assistant\s+)?commissioner\s+of\s+police$",
        ],
    },
    "warden": {
        "canonical_name": "Warden",
        "career_track": "Administrative",
        "patterns": [
            r"^(chief\s+|district\s+)?warden$",
        ],
    },
    "dresser": {
        "canonical_name": "Dresser",
        "career_track": "Medical",
        "patterns": [r"^dresser$"],
    },
    "constable": {
        "canonical_name": "Constable",
        "career_track": "Police",
        "patterns": [
            r"^(head\s+|chief\s+)?constable$",
        ],
    },
    "schoolmaster": {
        "canonical_name": "Schoolmaster",
        "career_track": "Education",
        "patterns": [
            r"^(head\s+)?schoolmaster$",
            r"^(head\s+)?school\s*master$",
            r"^(head\s+)?teacher$",
        ],
    },
}

# Compile position family patterns
_COMPILED_POS_RULES = {}
for family_id, rule in POSITION_FAMILIES.items():
    _COMPILED_POS_RULES[family_id] = {
        **rule,
        "compiled": [re.compile(p, re.IGNORECASE) for p in rule["patterns"]],
    }


def cluster_positions(raw_counts: dict[str, int]) -> tuple[list[dict], list[dict]]:
    """Cluster position titles using normalization + regex rules.

    Args:
        raw_counts: {raw_position_title: instance_count}

    Returns:
        (clusters, unclustered)
    """
    # Step 1: Normalize all titles
    # Map normalized -> list of (raw, count)
    norm_groups = defaultdict(list)
    for raw, count in raw_counts.items():
        normalized = normalize_position_text(raw)
        singular = singularize(normalized)
        norm_groups[singular].append({"raw": raw, "count": count})

    # Step 2: Extract grades from normalized forms
    # Map (base, grade) -> list of raw entries
    graded = {}  # normalized_key -> {base, grade, entries}
    for normalized, entries in norm_groups.items():
        base, grade = extract_grade(normalized)
        key = f"{base}||{grade}" if grade is not None else base
        if key not in graded:
            graded[key] = {"base": base, "grade": grade, "entries": []}
        graded[key]["entries"].extend(entries)

    # Step 3: Match against position family rules
    claimed = {}  # normalized_key -> family_id
    for key, info in graded.items():
        match_text = info["base"]
        for family_id, rule in _COMPILED_POS_RULES.items():
            for pattern in rule["compiled"]:
                if pattern.match(match_text):
                    claimed[key] = family_id
                    break
            if key in claimed:
                break

    # Step 4: Build cluster output
    cluster_members = defaultdict(list)
    for key, family_id in claimed.items():
        info = graded[key]
        for entry in info["entries"]:
            cluster_members[family_id].append({
                "raw": entry["raw"],
                "count": entry["count"],
                "confidence": "HIGH",
                "method": "rule",
            })

    clusters = []
    for family_id, rule in POSITION_FAMILIES.items():
        members = cluster_members.get(family_id, [])
        if not members:
            continue
        members.sort(key=lambda m: m["count"], reverse=True)

        # Determine grade from members (take the first non-None)
        grade = None
        for key, fid in claimed.items():
            if fid == family_id:
                g = graded[key]["grade"]
                if g is not None:
                    grade = g
                    break

        clusters.append({
            "id": f"pos_{family_id}",
            "canonical_name": rule["canonical_name"],
            "career_track": rule["career_track"],
            "grade_level": grade,
            "members": members,
        })

    clusters.sort(key=lambda c: sum(m["count"] for m in c["members"]), reverse=True)

    # Unclustered: anything whose normalized key was not claimed
    unclustered_entries = []
    for key, info in graded.items():
        if key not in claimed:
            total_count = sum(e["count"] for e in info["entries"])
            # Use the highest-count raw form as representative
            info["entries"].sort(key=lambda e: e["count"], reverse=True)
            unclustered_entries.append({
                "raw": info["entries"][0]["raw"],
                "count": total_count,
                "normalized": info["base"],
                "grade": info["grade"],
                "all_variants": [e["raw"] for e in info["entries"]] if len(info["entries"]) > 1 else None,
            })

    unclustered_entries.sort(key=lambda x: x["count"], reverse=True)

    return clusters, unclustered_entries


# =============================================================================
# CLI — quick test
# =============================================================================

if __name__ == "__main__":
    import json
    from pathlib import Path

    GENERATED_DIR = Path(__file__).parent / "generated"
    dept_counts = defaultdict(int)
    pos_counts = defaultdict(int)

    for f in sorted(GENERATED_DIR.glob("*_data_*.json")):
        try:
            data = json.load(open(f))
            for o in data.get("officials", []):
                d = o.get("department")
                p = o.get("position")
                if d and d.strip():
                    dept_counts[d.strip()] += 1
                if p and p.strip():
                    pos_counts[p.strip()] += 1
        except Exception:
            pass

    total_dept_instances = sum(dept_counts.values())
    total_pos_instances = sum(pos_counts.values())
    print(f"Raw departments: {len(dept_counts)} distinct, {total_dept_instances} instances")
    print(f"Raw positions: {len(pos_counts)} distinct, {total_pos_instances} instances")

    # Cluster departments
    dept_clusters, dept_unclustered = cluster_departments(dict(dept_counts))
    print(f"\nDepartment clusters: {len(dept_clusters)}")
    claimed_dept = sum(len(c["members"]) for c in dept_clusters)
    claimed_dept_inst = sum(m["count"] for c in dept_clusters for m in c["members"])
    print(f"Claimed: {claimed_dept} / {len(dept_counts)} distinct "
          f"({100*claimed_dept/len(dept_counts):.1f}%)")
    print(f"Claimed: {claimed_dept_inst} / {total_dept_instances} instances "
          f"({100*claimed_dept_inst/total_dept_instances:.1f}%)")
    print(f"Unclustered: {len(dept_unclustered)}")

    for c in dept_clusters[:10]:
        total = sum(m["count"] for m in c["members"])
        print(f"  {c['canonical_name']:<40} {len(c['members']):>3} variants, "
              f"{total:>5} instances")

    # Cluster positions
    pos_clusters, pos_unclustered = cluster_positions(dict(pos_counts))
    print(f"\nPosition clusters: {len(pos_clusters)}")
    claimed_pos = sum(len(c["members"]) for c in pos_clusters)
    claimed_pos_inst = sum(m["count"] for c in pos_clusters for m in c["members"])
    print(f"Claimed: {claimed_pos} / {len(pos_counts)} distinct "
          f"({100*claimed_pos/len(pos_counts):.1f}%)")
    print(f"Claimed: {claimed_pos_inst} / {total_pos_instances} instances "
          f"({100*claimed_pos_inst/total_pos_instances:.1f}%)")
    print(f"Unclustered: {len(pos_unclustered)}")

    for c in pos_clusters[:10]:
        total = sum(m["count"] for m in c["members"])
        print(f"  {c['canonical_name']:<40} {len(c['members']):>3} variants, "
              f"{total:>5} instances")

    print(f"\nTop 20 unclustered departments:")
    for u in dept_unclustered[:20]:
        print(f"  {u['count']:>5}  {u['raw']}")

    print(f"\nTop 20 unclustered positions:")
    for u in pos_unclustered[:20]:
        print(f"  {u['count']:>5}  {u['raw']}")
