"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "R. F. Allan", "canonical_name": "Allan, R. F.", "given_names": "R. F.", "surname": "Allan", "position": "Chief Accountant", "department": "Accounts - Sierra Leone", "salary_min": 900, "salary_max": 900},
    {"name": "D. W. Fulton", "canonical_name": "Fulton, D. W.", "given_names": "D. W.", "surname": "Fulton", "position": "Assistant Accountant", "department": "Accounts - Sierra Leone", "salary_scale": "B"},
    {"name": "S. G. Whittles", "canonical_name": "Whittles, S. G.", "given_names": "S. G.", "surname": "Whittles", "position": "Assistant Accountant", "department": "Accounts - Sierra Leone", "salary_scale": "B"},
    {"name": "C. F. Donovan", "canonical_name": "Donovan, C. F.", "given_names": "C. F.", "surname": "Donovan", "position": "Stores Superintendent", "department": "Stores - Sierra Leone", "salary_scale": "C3"},
    {"name": "R. E. Broomfield", "canonical_name": "Broomfield, R. E.", "given_names": "R. E.", "surname": "Broomfield", "position": "Chief Engineer", "department": "Engineering - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "E. F. Draper", "canonical_name": "Draper, E. F.", "given_names": "E. F.", "surname": "Draper", "position": "Assistant Engineer", "department": "Engineering - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Astley", "canonical_name": "Astley, J.", "given_names": "J.", "surname": "Astley", "position": "Assistant Engineer", "department": "Engineering - Sierra Leone", "salary_scale": "A"},
    {"name": "A. D. Eaton", "canonical_name": "Eaton, A. D.", "given_names": "A. D.", "surname": "Eaton", "position": "Assistant Engineer", "department": "Engineering - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()