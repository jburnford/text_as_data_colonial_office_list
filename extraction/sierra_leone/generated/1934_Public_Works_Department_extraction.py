"""
Sierra Leone Colonial Office List 1934 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1934

OFFICIALS = [
    {"name": "C. Wilson Brown", "canonical_name": "Brown, C. Wilson", "given_names": "C.", "surname": "Brown", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "military_rank": "Captain", "honors": ["M.C."], "qualifications": ["A.R.T.C.", "F.R.G.S.", "M.Inst.C.E."]},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["A.M.I.C.E.I.", "F.S.I."]},
    {"name": "D. J. Brown", "canonical_name": "Brown, D. J.", "given_names": "D. J.", "surname": "Brown", "position": "Provincial Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l.", "salary_scale": "C", "qualifications": ["A.M.I. Mun. & Cty."]},
    {"name": "W. H. Jackson", "canonical_name": "Jackson, W. H.", "given_names": "W. H.", "surname": "Jackson", "position": "Provincial Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l.", "salary_scale": "C", "qualifications": ["A.M.I.C.E.", "M.I.S.E."]},
    {"name": "A. R. Smee", "canonical_name": "Smee, A. R.", "given_names": "A. R.", "surname": "Smee", "position": "Executive Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "qualifications": ["A.M.I.C.E."]},
    {"name": "A. S. Ellicott", "canonical_name": "Ellicott, A. S.", "given_names": "A. S.", "surname": "Ellicott", "position": "Executive Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Executive Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "W. C. T. Rolls", "canonical_name": "Rolls, W. C. T.", "given_names": "W. C. T.", "surname": "Rolls", "position": "Chief Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "duty_allowance": 72},
    {"name": "T. V. Badger", "canonical_name": "Badger, T. V.", "given_names": "T. V.", "surname": "Badger", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A", "duty_allowance": 60},
    {"name": "L. P. John", "canonical_name": "John, L. P.", "given_names": "L. P.", "surname": "John", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "T. Maloney", "canonical_name": "Maloney, T.", "given_names": "T.", "surname": "Maloney", "position": "Main and Distribution Foreman, Electricity Sub-Dept.", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560, "qualifications": ["Assoc. I.E.E."]},
    {"name": "H. Flint", "canonical_name": "Flint, H.", "given_names": "H.", "surname": "Flint", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 560, "salary_max": 600},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()