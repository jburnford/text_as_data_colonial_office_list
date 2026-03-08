"""
Gambia Colonial Office List 1928 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1928

OFFICIALS = [
    {"name": "J. Aitken", "canonical_name": "Aitken, J.", "given_names": "J.", "surname": "Aitken", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "C. M. Barton", "canonical_name": "Barton, C. M.", "given_names": "C. M.", "surname": "Barton", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 600, "salary_max": 920},
    {"name": "J. M. De Freitas", "canonical_name": "De Freitas, J. M.", "given_names": "J. M.", "surname": "De Freitas", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 800, "honors": ["O.B.E."], "military_rank": "Captain"},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Clerk of Courts, 1st Grade", "department": "Legal Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "F. A. R. Gibson", "canonical_name": "Gibson, F. A. R.", "given_names": "F. A. R.", "surname": "Gibson", "position": "Interpreter of Courts, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Sheriff's Bailiff and Beadle of the Court of Requests, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "W. M. Bright", "canonical_name": "Bright, W. M.", "given_names": "W. M.", "surname": "Bright", "position": "2nd Grade Clerk", "department": "Legal Adviser's Office - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "C. Greig", "canonical_name": "Greig, C.", "given_names": "C.", "surname": "Greig", "position": "Sheriff", "department": "Legal Department - Gambia", "military_rank": "Captain"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()