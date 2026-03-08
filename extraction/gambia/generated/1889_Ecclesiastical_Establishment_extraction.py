"""
Gambia Colonial Office List 1889 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1889

OFFICIALS = [
    {"name": "C. B. D. Nicol", "canonical_name": "Nicol, C. B. D.", "given_names": "C. B. D.", "surname": "Nicol", "position": "Clerk and Organist", "department": "Ecclesiastical Establishment - Gambia", "salary_min": 20, "salary_max": 20},
    {"name": "M. B. Mason", "canonical_name": "Mason, M. B.", "given_names": "M. B.", "surname": "Mason", "position": "Keeper of Cemetery", "department": "Ecclesiastical Establishment - Gambia", "salary_min": 25, "salary_max": 25},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()