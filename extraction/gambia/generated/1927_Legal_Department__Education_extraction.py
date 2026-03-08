"""
Gambia Colonial Office List 1927 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1927

OFFICIALS = [
    {"name": "J. Aitken", "canonical_name": "Aitken, J.", "given_names": "J.", "surname": "Aitken", "position": "Judge of the Supreme Court", "department": "Judicial - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "C. M. Barton", "canonical_name": "Barton, C. M.", "given_names": "C. M.", "surname": "Barton", "position": "Legal Adviser", "department": "Legal - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "J. M. de Freitas", "canonical_name": "de Freitas, J. M.", "given_names": "J. M.", "surname": "de Freitas", "position": "Police Magistrate", "department": "Judicial - Gambia", "salary_min": 630, "salary_max": 800, "honors": ["O.B.E."], "military_rank": "Captain"},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Clerk of Courts, 1st Grade", "department": "Judicial - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Sheriff's Bailiff and Beadle of the Court of Requests, 2nd Grade", "department": "Judicial - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "W. M. Bright", "canonical_name": "Bright, W. M.", "given_names": "W. M.", "surname": "Bright", "position": "2nd Grade Clerk", "department": "Legal Adviser's Office - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "C. Greig", "canonical_name": "Greig, C.", "given_names": "C.", "surname": "Greig", "position": "Sheriff", "department": "Judicial - Gambia", "military_rank": "Captain"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()