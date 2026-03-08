"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "W. Venner", "canonical_name": "Venner, W.", "given_names": "W.", "surname": "Venner", "position": "General Manager", "department": "Railway Management - Sierra Leone", "salary_min": 1400, "salary_max": 1400},
    {"name": "D. C. A. J. Thomas", "canonical_name": "Thomas, D. C. A. J.", "given_names": "D. C. A. J.", "surname": "Thomas", "position": "Secretary", "department": "Railway Management - Sierra Leone", "salary_scale": "B"},
    {"name": "D. W. Fulton", "canonical_name": "Fulton, D. W.", "given_names": "D. W.", "surname": "Fulton", "position": "Chief Accountant", "department": "Accounts - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "S. G. Whittles", "canonical_name": "Whittles, S. G.", "given_names": "S. G.", "surname": "Whittles", "position": "Assistant Accountant", "department": "Accounts - Sierra Leone", "salary_scale": "B"},
    {"name": "C. A. Hollist", "canonical_name": "Hollist, C. A.", "given_names": "C. A.", "surname": "Hollist", "position": "Assistant Accountant", "department": "Accounts - Sierra Leone", "salary_scale": "B"},
    {"name": "C. F. Donovan", "canonical_name": "Donovan, C. F.", "given_names": "C. F.", "surname": "Donovan", "position": "Stores Superintendent", "department": "Stores - Sierra Leone", "salary_scale": "C.3"},
    {"name": "S. D. M. Robertson", "canonical_name": "Robertson, S. D. M.", "given_names": "S. D. M.", "surname": "Robertson", "position": "Chief Engineer", "department": "Engineering - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
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