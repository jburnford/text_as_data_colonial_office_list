"""
Gambia Colonial Office List 1934 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1934

OFFICIALS = [
    {"name": "J. A. Brawn", "canonical_name": "Brawn, J. A.", "given_names": "J. A.", "surname": "Brawn", "position": "Officer Commanding", "department": "Royal West African Frontier Force - Gambia", "salary_min": 700, "salary_max": 700, "duty_allowance": 54, "military_rank": "Captain"},
    {"name": "F. B. B. Dowling", "canonical_name": "Dowling, F. B. B.", "given_names": "F. B. B.", "surname": "Dowling", "position": "Lieutenant", "department": "Royal West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "honors": ["M.C."], "military_rank": "Lieutenant"},
    {"name": "S. B. Cope", "canonical_name": "Cope, S. B.", "given_names": "S. B.", "surname": "Cope", "position": "Lieutenant", "department": "Royal West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()