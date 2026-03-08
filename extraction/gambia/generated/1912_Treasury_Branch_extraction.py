"""
Gambia Colonial Office List 1912 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1912

OFFICIALS = [
    {"name": "C. C. Johnson", "canonical_name": "Johnson, C. C.", "given_names": "C. C.", "surname": "Johnson", "position": "Chief Clerk and Cashier", "department": "Treasury - Gambia", "salary_min": 175, "salary_max": 200},
    {"name": "P. Sowe", "canonical_name": "Sowe, P.", "given_names": "P.", "surname": "Sowe", "position": "First Clerk", "department": "Treasury - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "S. P. Gibbs", "canonical_name": "Gibbs, S. P.", "given_names": "S. P.", "surname": "Gibbs", "position": "Second Clerk", "department": "Treasury - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "Third Clerk", "department": "Treasury - Gambia", "salary_min": 36, "salary_max": 36},
    {"name": "Apprentice", "canonical_name": "Apprentice, ", "surname": "Apprentice", "position": "Apprentice", "department": "Treasury - Gambia", "salary_min": 12, "salary_max": 12},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()