"""
Sierra Leone Colonial Office List 1940 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1940

OFFICIALS = [
    {"name": "F. L. V. Mills", "canonical_name": "Mills, F. L. V.", "given_names": "F. L. V.", "surname": "Mills", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "honors": ["M.C."], "qualifications": ["A.M.I.C.E."], "military_rank": "Major"},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "honors": ["O.B.E."], "qualifications": ["M.Inst.C.E.I.", "F.S.I."], "duty_allowance": 96},
    {"name": "A. R. Smee", "canonical_name": "Smee, A. R.", "given_names": "A. R.", "surname": "Smee", "position": "Provincial Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_scale": "C", "duty_allowance": 92},
    {"name": "A. S. Ellicott", "canonical_name": "Ellicott, A. S.", "given_names": "A. S.", "surname": "Ellicott", "position": "Provincial Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["B.Sc."], "salary_scale": "C", "duty_allowance": 92},
    {"name": "E. L. Smith", "canonical_name": "Smith, E. L.", "given_names": "E. L.", "surname": "Smith", "position": "Executive Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["B.Sc.", "A.M.I.C.E."], "salary_scale": "C"},
    {"name": "K. H. B. Collier", "canonical_name": "Collier, K. H. B.", "given_names": "K. H. B.", "surname": "Collier", "position": "Executive Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_scale": "C"},
    {"name": "J. H. Amos", "canonical_name": "Amos, J. H.", "given_names": "J. H.", "surname": "Amos", "position": "Executive Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["B.Sc.", "A.M.Inst.C.E.", "A.M.C.T."], "salary_min": 475, "salary_max": 840},
    {"name": "J. P. Murphy", "canonical_name": "Murphy, J. P.", "given_names": "J. P.", "surname": "Murphy", "position": "Executive Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["B.E.", "B.Sc."], "salary_min": 475, "salary_max": 840},
    {"name": "J. Stevenson", "canonical_name": "Stevenson, J.", "given_names": "J.", "surname": "Stevenson", "position": "Technical Assistant", "department": "Public Works Department - Sierra Leone", "salary_min": 475, "salary_max": 840},
    {"name": "L. P. John", "canonical_name": "John, L. P.", "given_names": "L. P.", "surname": "John", "position": "Chief Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "duty_allowance": 72},
    {"name": "L. B. White", "canonical_name": "White, L. B.", "given_names": "L. B.", "surname": "White", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 600},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Act. and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 600},
    {"name": "J. F. Giigg", "canonical_name": "Giigg, J. F.", "given_names": "J. F.", "surname": "Giigg", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 560, "salary_max": 600},
    {"name": "T. Maloney", "canonical_name": "Maloney, T.", "given_names": "T.", "surname": "Maloney", "position": "Electrical Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["Assoc.I.E.E."], "salary_min": 630, "salary_max": 840},
    {"name": "A. J. Momoh", "canonical_name": "Momoh, A. J.", "given_names": "A. J.", "surname": "Momoh", "position": "African Ass't Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "A. F. G. Taylor", "canonical_name": "Taylor, A. F. G.", "given_names": "A. F. G.", "surname": "Taylor", "position": "Office Asst.", "department": "Public Works Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()