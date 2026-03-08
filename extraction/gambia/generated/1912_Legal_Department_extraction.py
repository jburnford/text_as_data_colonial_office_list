"""
Gambia Colonial Office List 1912 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1912

OFFICIALS = [
    {"name": "E. A. Hume", "canonical_name": "Hume, E. A.", "given_names": "E. A.", "surname": "Hume", "position": "Chief Magistrate", "department": "Legal Department - Gambia", "salary_min": 750, "salary_max": 750},
    {"name": "D. Kingdon", "canonical_name": "Kingdon, D.", "given_names": "D.", "surname": "Kingdon", "position": "Legal Assistant", "department": "Legal Department - Gambia", "salary_min": 240, "salary_max": 270},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "J. Finden Dailey", "canonical_name": "Dailey, J. Finden", "given_names": "J. Finden", "surname": "Dailey", "position": "Clerks to Legal Assistant", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "C. A. Hughes", "canonical_name": "Hughes, C. A.", "given_names": "C. A.", "surname": "Hughes", "position": "Clerks to Legal Assistant", "department": "Legal Department - Gambia", "salary_min": 24, "salary_max": 30},
    {"name": "J. R. E. Lusack", "canonical_name": "Lusack, J. R. E.", "given_names": "J. R. E.", "surname": "Lusack", "position": "Interpreter", "department": "Legal Department - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Beadle and Bailiff", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "C. Creig", "canonical_name": "Creig, C.", "given_names": "C.", "surname": "Creig", "position": "Sheriff", "department": "Legal Department - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()