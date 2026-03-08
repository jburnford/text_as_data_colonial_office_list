"""
Gambia Colonial Office List 1951 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1951

OFFICIALS = [
    {"name": "G. Peters", "canonical_name": "Peters, G.", "given_names": "G.", "surname": "Peters", "position": "Information Officer", "department": "PUBLIC RELATIONS - Gambia", "salary_scale": "B"},
    {"name": "K. Wilson", "canonical_name": "Wilson, K.", "given_names": "K.", "surname": "Wilson", "position": "Director", "department": "PUBLIC UTILITIES - Gambia", "salary_min": 1100, "salary_max": 1100},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Deputy Director", "department": "PUBLIC UTILITIES - Gambia", "salary_min": 1000, "salary_max": 1000},
    {"name": "J. Reid", "canonical_name": "Reid, J.", "given_names": "J.", "surname": "Reid", "position": "Harbourmaster and Chief Engineer", "department": "PUBLIC UTILITIES - Gambia", "salary_scale": "A"},
    {"name": "A. N. Robinson", "canonical_name": "Robinson, A. N.", "given_names": "A. N.", "surname": "Robinson", "position": "Executive Engineer", "department": "PUBLIC UTILITIES - Gambia", "salary_scale": "A"},
    {"name": "P. J. S. Bradshaw", "canonical_name": "Bradshaw, P. J. S.", "given_names": "P. J. S.", "surname": "Bradshaw", "position": "Executive Engineer", "department": "PUBLIC UTILITIES - Gambia", "salary_scale": "A"},
    {"name": "F. Cliffe", "canonical_name": "Cliffe, F.", "given_names": "F.", "surname": "Cliffe", "position": "Accountant", "department": "PUBLIC UTILITIES - Gambia", "salary_scale": "B"},
    {"name": "W. A. Dyke-Poynter", "canonical_name": "Dyke-Poynter, W. A.", "given_names": "W. A.", "surname": "Dyke-Poynter", "position": "Storekeeper", "department": "PUBLIC UTILITIES - Gambia", "salary_scale": "C"},
    {"name": "W. A. Small", "canonical_name": "Small, W. A.", "given_names": "W. A.", "surname": "Small", "position": "Superintendent of Surveys", "department": "SURVEY - Gambia", "salary_scale": "B"},
    {"name": "A. Fulton", "canonical_name": "Fulton, A.", "given_names": "A.", "surname": "Fulton", "position": "Director", "department": "VETERINARY - Gambia", "salary_min": 1200, "salary_max": 1200},
    {"name": "D. F. Hamilton", "canonical_name": "Hamilton, D. F.", "given_names": "D. F.", "surname": "Hamilton", "position": "Veterinary Officer", "department": "VETERINARY - Gambia", "salary_scale": "A"},
    {"name": "G. J. Knight", "canonical_name": "Knight, G. J.", "given_names": "G. J.", "surname": "Knight", "position": "Laboratory Superintendent", "department": "VETERINARY - Gambia", "salary_scale": "C"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()