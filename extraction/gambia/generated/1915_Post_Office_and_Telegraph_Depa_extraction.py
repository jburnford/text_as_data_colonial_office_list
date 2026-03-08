"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "C. W. Hill", "canonical_name": "Hill, C. W.", "given_names": "C. W.", "surname": "Hill", "position": "Postmaster", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "A. Chipulina", "canonical_name": "Chipulina, A.", "given_names": "A.", "surname": "Chipulina", "position": "Chief Clerk and Cashier", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 210, "salary_max": 300},
    {"name": "J. Chipulina", "canonical_name": "Chipulina, J.", "given_names": "J.", "surname": "Chipulina", "position": "Senior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 160, "salary_max": 240},
    {"name": "J. J. Desoza", "canonical_name": "Desoza, J. J.", "given_names": "J. J.", "surname": "Desoza", "position": "Senior Clerk", "department": "Post Office and Telegraph Department - Gambia"},
    {"name": "T. Chipulina", "canonical_name": "Chipulina, T.", "given_names": "T.", "surname": "Chipulina", "position": "Senior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "A. de la Paz", "canonical_name": "de la Paz, A.", "given_names": "A.", "surname": "de la Paz", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "E. Jones", "canonical_name": "Jones, E.", "given_names": "E.", "surname": "Jones", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "E. Coll", "canonical_name": "Coll, E.", "given_names": "E.", "surname": "Coll", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "A. Pons", "canonical_name": "Pons, A.", "given_names": "A.", "surname": "Pons", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "A. Canepa", "canonical_name": "Canepa, A.", "given_names": "A.", "surname": "Canepa", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "A. Gilbert", "canonical_name": "Gilbert, A.", "given_names": "A.", "surname": "Gilbert", "position": "Junior Clerk", "department": "Post Office and Telegraph Department - Gambia", "salary_min": 75, "salary_max": 150},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()