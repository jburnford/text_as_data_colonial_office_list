"""
Sierra Leone Colonial Office List 1933 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1933

OFFICIALS = [
    {"name": "C. Wilson Brown", "canonical_name": "Brown, C. Wilson", "given_names": "C. Wilson", "surname": "Brown", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "honors": ["M.C."], "qualifications": ["A.R.T.C.", "F.R.G.S.", "A.M.I.C.E."], "military_rank": "Captain"},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["A.M.I.C.E.", "F.S.I."]},
    {"name": "J. R. C. Tyler", "canonical_name": "Tyler, J. R. C.", "given_names": "J. R. C.", "surname": "Tyler", "position": "Provincial Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l.", "qualifications": ["A.M.I.C.E."]},
    {"name": "D. J. Brown", "canonical_name": "Brown, D. J.", "given_names": "D. J.", "surname": "Brown", "position": "Provincial Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l.", "qualifications": ["A.M.I. Mun. & Oty. E."]},
    {"name": "T. W. McLeod", "canonical_name": "McLeod, T. W.", "given_names": "T. W.", "surname": "McLeod", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "A. R. Smee", "canonical_name": "Smee, A. R.", "given_names": "A. R.", "surname": "Smee", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "W. H. Jackson", "canonical_name": "Jackson, W. H.", "given_names": "W. H.", "surname": "Jackson", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "A. S. Ellicott", "canonical_name": "Ellicott, A. S.", "given_names": "A. S.", "surname": "Ellicott", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "W. C. T. Rolls", "canonical_name": "Rolls, W. C. T.", "given_names": "W. C. T.", "surname": "Rolls", "position": "Chief Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "duty_allowance": 72},
    {"name": "T. V. Badger", "canonical_name": "Badger, T. V.", "given_names": "T. V.", "surname": "Badger", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A", "duty_allowance": 60},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "H. Watkin", "canonical_name": "Watkin, H.", "given_names": "H.", "surname": "Watkin", "position": "Chief Electrical Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "qualifications": ["A.M.I.E.E."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Electrical Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "L. P. John", "canonical_name": "John, L. P.", "given_names": "L. P.", "surname": "John", "position": "Assistant Accountant, Electricity Sub-Department", "department": "Public Works Department - Sierra Leone", "salary_min": 450, "salary_max": 720},
    {"name": "H. Flint", "canonical_name": "Flint, H.", "given_names": "H.", "surname": "Flint", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 560, "salary_max": 600},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()