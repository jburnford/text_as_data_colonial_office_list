"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Major J. C. Craig", "canonical_name": "Craig, Major J. C.", "given_names": "J. C.", "surname": "Craig", "position": "Assistant Chief Engineer", "department": "Public Works Department", "salary_min": 2000, "salary_max": 2000, "honors": ["D.S.O."]},
    {"name": "E. B. Widdowson", "canonical_name": "Widdowson, E. B.", "given_names": "E. B.", "surname": "Widdowson", "position": "Accountant and Cashier", "department": "Public Works Department", "salary_min": 600, "salary_max": 600},
    {"name": "Capt. J. Warnock", "canonical_name": "Warnock, Capt. J.", "given_names": "J.", "surname": "Warnock", "position": "Resident Engineer", "department": "Public Works Department", "salary_min": 850, "salary_max": 850, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "Capt. J. M. P. Hamilton", "canonical_name": "Hamilton, Capt. J. M. P.", "given_names": "J. M. P.", "surname": "Hamilton", "position": "Mechanical Engineer", "department": "Public Works Department", "salary_min": 720, "salary_max": 720, "military_rank": "Captain"},
    {"name": "T. F. Quinlan", "canonical_name": "Quinlan, T. F.", "given_names": "T. F.", "surname": "Quinlan", "position": "Assistant Mechanical Engineer", "department": "Public Works Department", "salary_min": 520, "salary_max": 520, "honors": ["M.C."]},
    {"name": "T. M. Forest", "canonical_name": "Forest, T. M.", "given_names": "T. M.", "surname": "Forest", "position": "Concrete Foreman", "department": "Public Works Department", "salary_min": 540, "salary_max": 540},
    {"name": "W. R. Hatherill", "canonical_name": "Hatherill, W. R.", "given_names": "W. R.", "surname": "Hatherill", "position": "Carpenter Foreman", "department": "Public Works Department", "salary_min": 540, "salary_max": 540},
    {"name": "L. MacDonald", "canonical_name": "MacDonald, L.", "given_names": "L.", "surname": "MacDonald", "position": "Assistant Superintendent of Grading", "department": "Public Works Department", "salary_min": 540, "salary_max": 540},
    {"name": "A. Munro", "canonical_name": "Munro, A.", "given_names": "A.", "surname": "Munro", "position": "Time and Storekeeper", "department": "Public Works Department", "salary_min": 480, "salary_max": 480},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()