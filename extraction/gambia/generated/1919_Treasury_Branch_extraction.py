"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "C. C. Johnson", "canonical_name": "Johnson, C. C.", "given_names": "C. C.", "surname": "Johnson", "position": "Chief Clerk and Cashier", "department": "Treasury - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "P. Sowe", "canonical_name": "Sowe, P.", "given_names": "P.", "surname": "Sowe", "position": "1st Grade Clerk", "department": "Treasury - Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "B. J. George", "canonical_name": "George, B. J.", "given_names": "B. J.", "surname": "George", "position": "2nd Clerk", "department": "Treasury - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "S. P. Gibbs", "canonical_name": "Gibbs, S. P.", "given_names": "S. P.", "surname": "Gibbs", "position": "2nd Clerk", "department": "Treasury - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "3rd Clerk", "department": "Treasury - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "3rd Clerk", "department": "Treasury - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "4th Clerk", "department": "Treasury - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "T. S. King", "canonical_name": "King, T. S.", "given_names": "T. S.", "surname": "King", "position": "5th Clerk", "department": "Treasury - Gambia", "salary_min": 40, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()