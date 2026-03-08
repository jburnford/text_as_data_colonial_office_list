"""
Gambia Colonial Office List 1922 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1922

OFFICIALS = [
    {"name": "C. H. Armitage", "canonical_name": "Armitage, C. H.", "given_names": "C. H.", "surname": "Armitage", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 750, "honors": ["C.M.G.", "D.S.O."], "military_rank": "Captain"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 500, "salary_max": 500},
    {"name": "M. L. Valantine", "canonical_name": "Valantine, M. L.", "given_names": "M. L.", "surname": "Valantine", "position": "2nd Grade Clerks", "department": "Civil Establishment - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Civil Establishment - Gambia", "salary_min": 90, "salary_max": 170},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()