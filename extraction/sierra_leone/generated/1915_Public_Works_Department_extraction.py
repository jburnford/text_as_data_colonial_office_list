"""
Sierra Leone Colonial Office List 1915 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1915

OFFICIALS = [
    {"name": "C. A. Copland", "canonical_name": "Copland, C. A.", "given_names": "C. A.", "surname": "Copland", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 800, "salary_max": 1000, "duty_allowance": 160},
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "H. Simms", "canonical_name": "Simms, H.", "given_names": "H.", "surname": "Simms", "position": "Sanitary Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "G. Stanley", "canonical_name": "Stanley, G.", "given_names": "G.", "surname": "Stanley", "position": "Assistant Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. A. P. D. Stone", "canonical_name": "Stone, A. A. P. D.", "given_names": "A. A. P. D.", "surname": "Stone", "position": "Assistant Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "R. Summerscale", "canonical_name": "Summerscale, R.", "given_names": "R.", "surname": "Summerscale", "position": "Assistant Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "T. Knight", "canonical_name": "Knight, T.", "given_names": "T.", "surname": "Knight", "position": "Assistant Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "B. W. Fitch-Jones", "canonical_name": "Fitch-Jones, B. W.", "given_names": "B. W.", "surname": "Fitch-Jones", "position": "Drawshtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "L. B. Shaw", "canonical_name": "Shaw, L. B.", "given_names": "L. B.", "surname": "Shaw", "position": "Drawshtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Drawshtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "S. B. Jones", "canonical_name": "Jones, S. B.", "given_names": "S. B.", "surname": "Jones", "position": "Drawshtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "H. Denham Smith", "canonical_name": "Smith, H. Denham", "given_names": "H. Denham", "surname": "Smith", "position": "Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. G. Harrison", "canonical_name": "Harrison, J. G.", "given_names": "J. G.", "surname": "Harrison", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "N. Nye", "canonical_name": "Nye, N.", "given_names": "N.", "surname": "Nye", "position": "Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. H. Sheikdrake", "canonical_name": "Sheikdrake, J. H.", "given_names": "J. H.", "surname": "Sheikdrake", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "B. L. Wilson", "canonical_name": "Wilson, B. L.", "given_names": "B. L.", "surname": "Wilson", "position": "Chief Native Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "T. L. Wilhelm", "canonical_name": "Wilhelm, T. L.", "given_names": "T. L.", "surname": "Wilhelm", "position": "Chief Native Drawtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "G. P. Jarrett", "canonical_name": "Jarrett, G. P.", "given_names": "G. P.", "surname": "Jarrett", "position": "First Grade Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "E. C. Davies", "canonical_name": "Davies, E. C.", "given_names": "E. C.", "surname": "Davies", "position": "Third Grade Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "G. A. Harding", "canonical_name": "Harding, G. A.", "given_names": "G. A.", "surname": "Harding", "position": "Third Grade Clerk", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 130}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()