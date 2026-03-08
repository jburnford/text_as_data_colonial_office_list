"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 700, "salary_max": 800, "duty_allowance": 140},
    {"name": "A. S. Bradshaw", "canonical_name": "Bradshaw, A. S.", "given_names": "A. S.", "surname": "Bradshaw", "position": "Assistant ditto and Protectorate Roads Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Sanitary Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "A. A. P. D. Stone", "canonical_name": "Stone, A. A. P. D.", "given_names": "A. A. P. D.", "surname": "Stone", "position": "Assistant Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "B. W. Fitch-Jones", "canonical_name": "Fitch-Jones, B. W.", "given_names": "B. W.", "surname": "Fitch-Jones", "position": "Assistant Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "A. Turnbull", "canonical_name": "Turnbull, A.", "given_names": "A.", "surname": "Turnbull", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "W. J. Halls", "canonical_name": "Halls, W. J.", "given_names": "W. J.", "surname": "Halls", "position": "Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. G. Fenton", "canonical_name": "Fenton, J. G.", "given_names": "J. G.", "surname": "Fenton", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "J. D. Morgan", "canonical_name": "Morgan, J. D.", "given_names": "J. D.", "surname": "Morgan", "position": "Assistant Storekeeper and Deputy Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. H. Sheldrake", "canonical_name": "Sheldrake, J. H.", "given_names": "J. H.", "surname": "Sheldrake", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "E. T. Macfoye", "canonical_name": "Macfoye, E. T.", "given_names": "E. T.", "surname": "Macfoye", "position": "Chief Native Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "E. C. Davies", "canonical_name": "Davies, E. C.", "given_names": "E. C.", "surname": "Davies", "position": "Third Grade Clerks", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "G. A. Harding", "canonical_name": "Harding, G. A.", "given_names": "G. A.", "surname": "Harding", "position": "Third Grade Clerks", "department": "Public Works Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "G. Stanley", "canonical_name": "Stanley, G.", "given_names": "G.", "surname": "Stanley", "position": "Engineer", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "G. Wilson", "canonical_name": "Wilson, G.", "given_names": "G.", "surname": "Wilson", "position": "Assistant Engineer", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "D. E. Frazer", "canonical_name": "Frazer, D. E.", "given_names": "D. E.", "surname": "Frazer", "position": "Native Surveyor", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "S. E. Cole", "canonical_name": "Cole, S. E.", "given_names": "S. E.", "surname": "Cole", "position": "Native Draughtsman", "department": "Protectorate Roads Department - Sierra Leone", "salary_min": 60, "salary_max": 80}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()