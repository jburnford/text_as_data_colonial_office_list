"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "F. A. Van der Meulen", "canonical_name": "Van der Meulen, F. A.", "given_names": "F. A.", "surname": "Van der Meulen", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 750, "salary_max": 750},
    {"name": "M. F. J. McDonnell", "canonical_name": "McDonnell, M. F. J.", "given_names": "M. F. J.", "surname": "McDonnell", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "J. J. Oldfield", "canonical_name": "Oldfield, J. J.", "given_names": "J. J.", "surname": "Oldfield", "position": "Assistant Clerk of Courts, 3rd Grade", "department": "Legal Department - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "Geo. D. Williams", "canonical_name": "Williams, Geo. D.", "given_names": "Geo. D.", "surname": "Williams", "position": "Interpreter of Courts", "department": "Legal Department - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Sheriff's Bailiff and Beadle of the Court of Requests", "department": "Legal Department - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk to Legal Adviser, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "N. C. Johnson", "canonical_name": "Johnson, N. C.", "given_names": "N. C.", "surname": "Johnson", "position": "Clerk to Legal Adviser, 3rd Grade", "department": "Legal Department - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "C. J. Clarke", "canonical_name": "Clarke, C. J.", "given_names": "C. J.", "surname": "Clarke", "position": "Clerk to Police Magistrate, 4th Grade", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "C. Greig", "canonical_name": "Greig, C.", "given_names": "C.", "surname": "Greig", "position": "Sheriff", "department": "Legal Department - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()