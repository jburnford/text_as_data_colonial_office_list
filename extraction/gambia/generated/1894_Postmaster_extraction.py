"""
Gambia Colonial Office List 1894 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1894

OFFICIALS = [
    {"name": "A. J. Nicol", "canonical_name": "Nicol, A. J.", "given_names": "A. J.", "surname": "Nicol", "position": "Postmaster", "department": "Post Office - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "D. Abraham", "canonical_name": "Abraham, D.", "given_names": "D.", "surname": "Abraham", "position": "Clerk", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "J. McCarthy", "canonical_name": "McCarthy, J.", "given_names": "J.", "surname": "McCarthy", "position": "Sorter", "department": "Post Office - Gambia", "salary_min": 36, "salary_max": 36},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()