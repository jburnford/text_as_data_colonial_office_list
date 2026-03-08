"""
Gambia Colonial Office List 1897 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1897

OFFICIALS = [
    {"name": "S. D. A. Coker", "canonical_name": "Coker, S. D. A.", "given_names": "S. D. A.", "surname": "Coker", "position": "Chief Clerk and Cashier", "department": "Civil Establishment - Gambia", "salary_min": 175, "salary_max": 175},
    {"name": "S. F. Hig", "canonical_name": "Hig, S. F.", "given_names": "S. F.", "surname": "Hig", "position": "Assistant Clerk", "department": "Civil Establishment - Gambia", "salary_min": 50, "salary_max": 65},
    {"name": "A. A. Thomas", "canonical_name": "Thomas, A. A.", "given_names": "A. A.", "surname": "Thomas", "position": "Junior Clerk", "department": "Civil Establishment - Gambia", "salary_min": 30, "salary_max": 30},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()