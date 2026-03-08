"""
Gambia Colonial Office List 1929 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1929

OFFICIALS = [
    {"name": "J. Aitken", "canonical_name": "Aitken, J.", "given_names": "J.", "surname": "Aitken", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 600, "salary_max": 920},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 800},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Clerk of Courts, 1st Grade", "department": "Legal Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "F. A. R. Gibson", "canonical_name": "Gibson, F. A. R.", "given_names": "F. A. R.", "surname": "Gibson", "position": "Interpreter of Courts, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Sheriff's Bailiff and Beadle of the Court of Requests, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "W. M. Bright", "canonical_name": "Bright, W. M.", "given_names": "W. M.", "surname": "Bright", "position": "2nd Grade Clerk", "department": "Legal Adviser's Office - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "Capt. C. Greig", "canonical_name": "Greig, C.", "given_names": "C.", "surname": "Greig", "position": "Sheriff", "department": "Legal Department - Gambia", "military_rank": "Captain"},
    {"name": "E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["C.M.G.", "D.S.O."], "military_rank": "Captain"},
    {"name": "Capt. E. B. Leece", "canonical_name": "Leece, E. B.", "given_names": "E. B.", "surname": "Leece", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"},
    {"name": "Major R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "Major L. A. W. Brooks", "canonical_name": "Brooks, L. A. W.", "given_names": "L. A. W.", "surname": "Brooks", "position": "Travelling Commissioner", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Major"},
    {"name": "Captain P. Jeffs", "canonical_name": "Jeffs, P.", "given_names": "P.", "surname": "Jeffs", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "Captain T. W. Doke", "canonical_name": "Doke, T. W.", "given_names": "T. W.", "surname": "Doke", "position": "Assistant", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()