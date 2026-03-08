#!/usr/bin/env python3
"""
Colonial Office List — Shared Extraction Schema
=================================================

Defines the canonical schema for personnel records extracted from
Colonial Office List source files. Every generated extraction script
should produce OFFICIALS lists conforming to this schema.

Usage in generated extraction scripts:
    # At the top of each extraction .py file
    # (schema is embedded, not imported, so scripts are self-contained)

Usage for validation:
    from guides.schema import validate_official, REQUIRED_FIELDS, SCHEMA_FIELDS
"""

from typing import Optional


# =============================================================================
# FIELD DEFINITIONS
# =============================================================================

SCHEMA_FIELDS = {
    # --- Identity (REQUIRED) ---
    "name": {
        "type": str,
        "required": True,
        "description": "Name as it appears in the source text",
        "example": "F. M. Hodgson",
    },
    "canonical_name": {
        "type": str,
        "required": True,
        "description": "Standardized 'Surname, Given Names' format",
        "example": "Hodgson, F. M.",
    },
    "given_names": {
        "type": (str, type(None)),
        "required": False,
        "description": "Given names / initials (may be None if unknown)",
        "example": "F. M.",
    },
    "surname": {
        "type": str,
        "required": True,
        "description": "Family name",
        "example": "Hodgson",
    },

    # --- Position (REQUIRED) ---
    "position": {
        "type": str,
        "required": True,
        "description": "Official title / role",
        "example": "Governor",
    },
    "department": {
        "type": str,
        "required": True,
        "description": "Department or administrative unit, with colony suffix",
        "example": "Civil Establishment - Gold Coast",
    },

    # --- Salary ---
    "salary_min": {
        "type": (int, float, type(None)),
        "required": False,
        "description": "Minimum annual salary (numeric, in local currency)",
        "example": 3000,
    },
    "salary_max": {
        "type": (int, float, type(None)),
        "required": False,
        "description": "Maximum annual salary (numeric, in local currency)",
        "example": 3500,
    },
    "salary_currency": {
        "type": (str, type(None)),
        "required": False,
        "description": "Currency code: GBP, Rs, USD, ECD, SSd, HKD, etc.",
        "example": "GBP",
        "default": None,
    },
    "salary_scale": {
        "type": (str, type(None)),
        "required": False,
        "description": "Salary scale designation (1940s-1950s): A, B, C.1, C.2, M2",
        "example": "C.1",
    },
    "allowances": {
        "type": (str, type(None)),
        "required": False,
        "description": "Raw text description of allowances",
        "example": "500l. table allowance",
    },
    "duty_allowance": {
        "type": (int, float, type(None)),
        "required": False,
        "description": "Numeric duty allowance amount",
        "example": 360,
    },
    "expatriation_pay": {
        "type": (int, float, type(None)),
        "required": False,
        "description": "Expatriation pay amount (1940s-1950s)",
        "example": 300,
    },
    "per_diem": {
        "type": (str, type(None)),
        "required": False,
        "description": "Daily rate if position is paid per diem",
        "example": "5s. 6d.",
    },

    # --- Status ---
    "acting_status": {
        "type": (str, type(None)),
        "required": False,
        "description": "Acting/Temporary/Officiating/Relief status",
        "example": "Acting",
        "valid_values": ["Acting", "Temporary", "Officiating", "Relief"],
    },

    # --- Classification ---
    "honors": {
        "type": list,
        "required": False,
        "description": "Post-nominal honors (C.M.G., K.C.M.G., O.B.E., etc.)",
        "example": ["C.M.G.", "O.B.E."],
        "default": [],
    },
    "qualifications": {
        "type": list,
        "required": False,
        "description": "Academic/professional qualifications (M.D., B.A., etc.)",
        "example": ["M.D.", "M.R.C.S."],
        "default": [],
    },
    "military_rank": {
        "type": (str, type(None)),
        "required": False,
        "description": "Military rank if applicable",
        "example": "Colonel",
    },

    # --- Location ---
    "location": {
        "type": (str, type(None)),
        "required": False,
        "description": "Specific station or posting location",
        "example": "Accra",
    },
    "region": {
        "type": (str, type(None)),
        "required": False,
        "description": "Administrative region within colony",
        "example": "Ashanti",
    },
}

REQUIRED_FIELDS = [k for k, v in SCHEMA_FIELDS.items() if v.get("required")]
OPTIONAL_FIELDS = [k for k, v in SCHEMA_FIELDS.items() if not v.get("required")]
ALL_FIELDS = list(SCHEMA_FIELDS.keys())


# =============================================================================
# KNOWN VALUES
# =============================================================================

KNOWN_HONORS = {
    "K.C.M.G.", "G.C.M.G.", "C.M.G.", "K.C.B.", "G.C.B.", "C.B.",
    "K.B.E.", "O.B.E.", "M.B.E.", "C.B.E.", "G.B.E.",
    "K.C.S.I.", "C.I.E.", "K.C.I.E.", "G.C.I.E.",
    "D.S.O.", "M.C.", "V.D.", "E.D.", "T.D.",
    "Kt.", "Knt.", "K.C.V.O.", "C.V.O.", "M.V.O.",
    "K.P.M.", "C.P.M.",
    "K.St.J.", "O.St.J.",
}

KNOWN_QUALIFICATIONS = {
    # Medical
    "M.D.", "M.B.", "M.R.C.S.", "F.R.C.S.", "L.R.C.S.", "L.R.C.P.",
    "F.R.C.P.", "Ch.B.", "B.Ch.", "D.P.H.", "D.T.M.", "D.T.M.&H.",
    "M.R.C.P.", "L.M.S.S.A.",
    # Academic
    "B.A.", "M.A.", "B.Sc.", "M.Sc.", "LL.D.", "D.D.", "Ph.D.",
    "B.L.", "LL.B.", "LL.M.", "B.Litt.", "D.Litt.", "D.Phil.",
    "B.Com.", "B.Ed.",
    # Engineering
    "R.E.", "C.E.", "M.I.C.E.", "A.I.C.E.", "A.M.I.C.E.",
    "M.I.E.E.", "A.M.I.E.E.", "M.I.Mech.E.",
    # Other
    "F.R.S.", "F.R.G.S.", "A.R.I.B.A.", "F.R.I.B.A.",
    "F.L.S.", "F.Z.S.", "F.G.S.", "F.S.A.",
    "F.R.A.S.", "F.R.Hist.S.",
}

KNOWN_MILITARY_RANKS = {
    "Colonel", "Col.", "Lt.-Col.", "Lieut.-Col.", "Lieutenant-Colonel",
    "Major-General", "Major", "Captain", "Capt.", "Brigadier",
    "Brigadier-General", "General", "Lieutenant", "Lieut.",
    "Commander", "Rear-Admiral", "Vice-Admiral", "Admiral",
    "Wing Commander", "Group Captain", "Air Commodore",
}

KNOWN_ACTING_STATUSES = {"Acting", "Temporary", "Officiating", "Relief"}


# =============================================================================
# VALIDATION
# =============================================================================

def validate_official(official: dict, strict: bool = False) -> list:
    """Validate a single official record against the schema.

    Args:
        official: Dict representing one extracted official.
        strict: If True, flag unknown fields. If False, allow extras.

    Returns:
        List of error strings. Empty list means valid.
    """
    errors = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in official:
            errors.append(f"Missing required field: {field}")
        elif official[field] is None:
            errors.append(f"Required field is None: {field}")
        elif isinstance(official[field], str) and official[field].strip() == "":
            errors.append(f"Required field is empty string: {field}")

    # Check field types
    for field, value in official.items():
        if field not in SCHEMA_FIELDS:
            if strict:
                errors.append(f"Unknown field: {field}")
            continue

        expected_type = SCHEMA_FIELDS[field]["type"]
        if value is not None and not isinstance(value, expected_type):
            errors.append(
                f"Wrong type for {field}: expected {expected_type}, got {type(value).__name__}"
            )

    # Plausibility checks
    salary_min = official.get("salary_min")
    salary_max = official.get("salary_max")

    if salary_min is not None and salary_max is not None:
        if salary_min < 0:
            errors.append(f"Negative salary_min: {salary_min}")
        if salary_max < 0:
            errors.append(f"Negative salary_max: {salary_max}")
        if salary_min > salary_max:
            errors.append(
                f"salary_min ({salary_min}) > salary_max ({salary_max})"
            )

    # Check honors are strings
    honors = official.get("honors", [])
    if isinstance(honors, list):
        for h in honors:
            if not isinstance(h, str):
                errors.append(f"Non-string honor: {h}")

    # Check qualifications are strings
    quals = official.get("qualifications", [])
    if isinstance(quals, list):
        for q in quals:
            if not isinstance(q, str):
                errors.append(f"Non-string qualification: {q}")

    return errors


def validate_officials_list(officials: list) -> dict:
    """Validate a full OFFICIALS list.

    Returns:
        Dict with 'valid' (bool), 'total' (int), 'error_count' (int),
        'errors' (list of (index, errors) tuples).
    """
    all_errors = []
    for i, official in enumerate(officials):
        errors = validate_official(official)
        if errors:
            all_errors.append((i, errors))

    return {
        "valid": len(all_errors) == 0,
        "total": len(officials),
        "error_count": len(all_errors),
        "errors": all_errors,
    }


# =============================================================================
# SCHEMA TEMPLATE (for embedding in generated extraction scripts)
# =============================================================================

SCHEMA_TEMPLATE_COMMENT = """# Schema fields (only include fields with actual values):
# REQUIRED: name, canonical_name, surname, position, department
# OPTIONAL: given_names, salary_min, salary_max, salary_currency,
#           salary_scale, allowances, duty_allowance, expatriation_pay,
#           per_diem, acting_status, honors (list), qualifications (list),
#           military_rank, location, region
"""


if __name__ == "__main__":
    # Self-test
    test_official = {
        "name": "F. M. Hodgson",
        "canonical_name": "Hodgson, F. M.",
        "given_names": "F. M.",
        "surname": "Hodgson",
        "position": "Governor",
        "department": "Civil Establishment - Gold Coast",
        "salary_min": 3000,
        "salary_max": 3000,
        "honors": ["C.M.G."],
        "military_rank": "Colonel",
    }

    errors = validate_official(test_official)
    if errors:
        print(f"FAIL: {errors}")
    else:
        print("PASS: Test official validates correctly")

    # Test missing required field
    bad_official = {"name": "Test"}
    errors = validate_official(bad_official)
    assert len(errors) > 0, "Should have errors for missing fields"
    print(f"PASS: Missing fields detected ({len(errors)} errors)")

    # Test salary range
    bad_salary = {
        "name": "T", "canonical_name": "T, T", "surname": "T",
        "position": "Clerk", "department": "Test",
        "salary_min": 500, "salary_max": 200,
    }
    errors = validate_official(bad_salary)
    assert any("salary_min" in e for e in errors), "Should flag bad salary range"
    print("PASS: Bad salary range detected")

    print(f"\nSchema has {len(ALL_FIELDS)} fields ({len(REQUIRED_FIELDS)} required, {len(OPTIONAL_FIELDS)} optional)")
