"""
Gambia Colonial Office List 1950 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1950

OFFICIALS = [
    {"name": "L. G. Culshaw", "canonical_name": "Culshaw, L. G.", "given_names": "L. G.", "surname": "Culshaw", "position": "Director", "department": "Public Utilities - Gambia", "salary_min": 1100, "salary_max": 1100, "expatriation_pay": 350},
    {"name": "K. Wilson", "canonical_name": "Wilson, K.", "given_names": "K.", "surname": "Wilson", "position": "Deputy Director", "department": "Public Utilities - Gambia", "salary_min": 1000, "salary_max": 1000, "expatriation_pay": 300},
    {"name": "J. Reid", "canonical_name": "Reid, J.", "given_names": "J.", "surname": "Reid", "position": "Harbourmaster and Chief Engineer", "department": "Public Utilities - Gambia", "salary_scale": "A"},
    {"name": "A. N. Robinson", "canonical_name": "Robinson, A. N.", "given_names": "A. N.", "surname": "Robinson", "position": "Executive Engineer", "department": "Public Utilities - Gambia", "salary_scale": "A"},
    {"name": "D. Evans", "canonical_name": "Evans, D.", "given_names": "D.", "surname": "Evans", "position": "Drainage Engineer", "department": "Public Utilities - Gambia", "salary_scale": "A"},
    {"name": "H. Brough", "canonical_name": "Brough, H.", "given_names": "H.", "surname": "Brough", "position": "Electrical Engineer", "department": "Public Utilities - Gambia", "salary_scale": "A"},
    {"name": "F. Cliffe", "canonical_name": "Cliffe, F.", "given_names": "F.", "surname": "Cliffe", "position": "Accountant", "department": "Public Utilities - Gambia", "salary_scale": "B"},
    {"name": "W. A. Dyke-Poynter", "canonical_name": "Dyke-Poynter, W. A.", "given_names": "W. A.", "surname": "Dyke-Poynter", "position": "Storekeeper", "department": "Public Utilities - Gambia", "salary_scale": "C"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()