"""
Gambia Colonial Office List 1889 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1889

OFFICIALS = [
    {"name": "C. B. Mitford", "canonical_name": "Mitford, C. B.", "given_names": "C. B.", "surname": "Mitford", "position": "Treasurer", "department": "Treasury - Gambia", "salary_min": 400, "salary_max": 400, "duty_allowance": 60},
    {"name": "S. D. A. Coker", "canonical_name": "Coker, S. D. A.", "given_names": "S. D. A.", "surname": "Coker", "position": "First Clerk", "department": "Treasury - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "A. J. Nicol", "canonical_name": "Nicol, A. J.", "given_names": "A. J.", "surname": "Nicol", "position": "Assistant Clerk", "department": "Treasury - Gambia", "salary_min": 85, "salary_max": 85},
    {"name": "S. C. King", "canonical_name": "King, S. C.", "given_names": "S. C.", "surname": "King", "position": "Sorter and Copyist", "department": "Treasury - Gambia", "salary_min": 36, "salary_max": 36},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()