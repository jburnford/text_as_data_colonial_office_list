"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "J. C. H. James", "canonical_name": "James, J. C. H.", "given_names": "J. C. H.", "surname": "James", "position": "Commissioner", "department": "Land Titles Department - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "F. A. Moseley", "canonical_name": "Moseley, F. A.", "given_names": "F. A.", "surname": "Moseley", "position": "Registrar of Titles and Deeds", "department": "Land Titles Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "A. Glyde", "canonical_name": "Glyde, A.", "given_names": "A.", "surname": "Glyde", "position": "Clerk", "department": "Land Titles Department - Gambia", "salary_min": 60, "salary_max": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()