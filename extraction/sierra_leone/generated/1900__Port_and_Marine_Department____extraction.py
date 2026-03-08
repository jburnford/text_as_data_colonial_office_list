"""
Sierra Leone Colonial Office List 1900 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1900

OFFICIALS = [
    {"name": "J. E. Dawson", "canonical_name": "Dawson, J. E.", "given_names": "J. E.", "surname": "Dawson", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "R. Moses", "canonical_name": "Moses, R.", "given_names": "R.", "surname": "Moses", "position": "Clerk to ditto", "department": "Port and Marine Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "A. Forrester", "canonical_name": "Forrester, A.", "given_names": "A.", "surname": "Forrester", "position": "Chief Engineer", "department": "Colonial Steamer - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "A. Eaton", "canonical_name": "Eaton, A.", "given_names": "A.", "surname": "Eaton", "position": "2nd Engineer", "department": "Colonial Steamer - Sierra Leone", "salary_min": 227, "salary_max": 227},
    {"name": "J. E. Cole", "canonical_name": "Cole, J. E.", "given_names": "J. E.", "surname": "Cole", "position": "Clerk", "department": "Colonial Steamer - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "G. A. Copland", "canonical_name": "Copland, G. A.", "given_names": "G. A.", "surname": "Copland", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 550},
    {"name": "F. H. Stone", "canonical_name": "Stone, F. H.", "given_names": "F. H.", "surname": "Stone", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "John Walker", "canonical_name": "Walker, John", "given_names": "John", "surname": "Walker", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 275, "allowances": "with hammock allowance and lodging allowance"},
    {"name": "B. L. Wilson", "canonical_name": "Wilson, B. L.", "given_names": "B. L.", "surname": "Wilson", "position": "Superintendent", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 150, "qualifications": ["C.E."]},
    {"name": "T. A. Wilhelm", "canonical_name": "Wilhelm, T. A.", "given_names": "T. A.", "surname": "Wilhelm", "position": "Chief Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "J. W. Paris", "canonical_name": "Paris, J. W.", "given_names": "J. W.", "surname": "Paris", "position": "Chief Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "G. P. Jarrett", "canonical_name": "Jarrett, G. P.", "given_names": "G. P.", "surname": "Jarrett", "position": "2nd Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. H. Kelso", "canonical_name": "Kelso, J. H.", "given_names": "J. H.", "surname": "Kelso", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 30, "salary_max": 40}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()