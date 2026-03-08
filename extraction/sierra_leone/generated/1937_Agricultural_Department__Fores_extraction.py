"""
Sierra Leone Colonial Office List 1937 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1937

OFFICIALS = [
    {"name": "F. J. Martin", "canonical_name": "Martin, F. J.", "given_names": "F. J.", "surname": "Martin", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210, "qualifications": ["Ph.D.", "F.I.C."]},
    {"name": "E. Hargreaves", "canonical_name": "Hargreaves, E.", "given_names": "E.", "surname": "Hargreaves", "position": "Entomologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l. seniority allowance", "qualifications": ["A.R.C.S.", "F.E.S."]},
    {"name": "F. C. Deighton", "canonical_name": "Deighton, F. C.", "given_names": "F. C.", "surname": "Deighton", "position": "Plant Pathologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "J. W. D. Fisher", "canonical_name": "Fisher, J. W. D.", "given_names": "J. W. D.", "surname": "Fisher", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "R. R. Glanville", "canonical_name": "Glanville, R. R.", "given_names": "R. R.", "surname": "Glanville", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C", "honors": ["M. B. E."]},
    {"name": "E. I. Nisbett", "canonical_name": "Nisbett, E. I.", "given_names": "E. I.", "surname": "Nisbett", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "G. M. Roddan", "canonical_name": "Roddan, G. M.", "given_names": "G. M.", "surname": "Roddan", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. S. Garner", "canonical_name": "Garner, E. S.", "given_names": "E. S.", "surname": "Garner", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. F. MacKenzie", "canonical_name": "MacKenzie, A. F.", "given_names": "A. F.", "surname": "MacKenzie", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "H. Machuskie", "canonical_name": "Machuskie, H.", "given_names": "H.", "surname": "Machuskie", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "F. W. B. Allinson", "canonical_name": "Allinson, F. W. B.", "given_names": "F. W. B.", "surname": "Allinson", "position": "Inspector of Plants and Produce", "department": "Agricultural Department - Sierra Leone", "salary_min": 400, "salary_max": 690},
    {"name": "W. M. Robertson", "canonical_name": "Robertson, W. M.", "given_names": "W. M.", "surname": "Robertson", "position": "Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050},
    {"name": "D. G. Thomas", "canonical_name": "Thomas, D. G.", "given_names": "D. G.", "surname": "Thomas", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C", "qualifications": ["B.Sc."]},
    {"name": "C. V. Wallace", "canonical_name": "Wallace, C. V.", "given_names": "C. V.", "surname": "Wallace", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C"},
    {"name": "T. E. Edwardson", "canonical_name": "Edwardson, T. E.", "given_names": "T. E.", "surname": "Edwardson", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C"},
    {"name": "C. Wilson Brown", "canonical_name": "Brown, C. Wilson", "given_names": "C. Wilson", "surname": "Brown", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "honors": ["O.B.E.", "M.C."], "military_rank": "Captain", "qualifications": ["A.R.T.C.", "F.R.G.S.", "M.Inst.C.E."]},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["M.Inst.C.E.I.", "F.S.I."]},
    {"name": "A. R. Smee", "canonical_name": "Smee, A. R.", "given_names": "A. R.", "surname": "Smee", "position": "Provincial Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l.", "salary_scale": "C", "qualifications": ["A.M.I.C.E."]},
    {"name": "A. S. Ellicott", "canonical_name": "Ellicott, A. S.", "given_names": "A. S.", "surname": "Ellicott", "position": "Provincial Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l.", "salary_scale": "C", "qualifications": ["B.Sc."]},
    {"name": "E. L. Smith", "canonical_name": "Smith, E. L.", "given_names": "E. L.", "surname": "Smith", "position": "Executive Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 480, "salary_max": 920, "qualifications": ["B.Sc.", "A.M.I.C.E."]},
    {"name": "K. H. B. Collier", "canonical_name": "Collier, K. H. B.", "given_names": "K. H. B.", "surname": "Collier", "position": "Executive Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 480, "salary_max": 920, "qualifications": ["A.M.I.C.E."]},
    {"name": "L. P. John", "canonical_name": "John, L. P.", "given_names": "L. P.", "surname": "John", "position": "Chief Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "duty_allowance": 72},
    {"name": "L. B. White", "canonical_name": "White, L. B.", "given_names": "L. B.", "surname": "White", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A", "salary_max": 720},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 560, "salary_max": 600},
    {"name": "T. Maloney", "canonical_name": "Maloney, T.", "given_names": "T.", "surname": "Maloney", "position": "Electrical Superintendent", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 72, "qualifications": ["Assoc.I.E.E."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()