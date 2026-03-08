"""
Sierra Leone Colonial Office List 1924 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1924

OFFICIALS = [
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "qualifications": ["M. Inst. C.E."]},
    {"name": "A. S. Bradshaw", "canonical_name": "Bradshaw, A. S.", "given_names": "A. S.", "surname": "Bradshaw", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["A.M.I.C.E."]},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Sanitary Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["A.M.I.C.E.", "F.S.I."]},
    {"name": "G. Stanley", "canonical_name": "Stanley, G.", "given_names": "G.", "surname": "Stanley", "position": "Executive Engineer, Grade 1", "department": "Public Works Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "seniority allowance 72l.", "qualifications": ["A.M.I.C.E."]},
    {"name": "B. W. Fitch-Jones", "canonical_name": "Fitch-Jones, B. W.", "given_names": "B. W.", "surname": "Fitch-Jones", "position": "Executive Engineers, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_scale": "C", "qualifications": ["M.S.A."]},
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Executive Engineers, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_scale": "C", "qualifications": ["M.A."]},
    {"name": "J. R. C. Tyler", "canonical_name": "Tyler, J. R. C.", "given_names": "J. R. C.", "surname": "Tyler", "position": "Executive Engineers, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_scale": "C", "qualifications": ["M.Inst.C.E.", "B.Sc."]},
    {"name": "R. Temple", "canonical_name": "Temple, R.", "given_names": "R.", "surname": "Temple", "position": "Surveyor", "department": "Public Works Department - Sierra Leone", "salary_scale": "C", "qualifications": ["F.S.I."]},
    {"name": "W. C. T. Rolls", "canonical_name": "Rolls, W. C. T.", "given_names": "W. C. T.", "surname": "Rolls", "position": "Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "allowances": "seniority allowance 72l."},
    {"name": "B. L. Philips", "canonical_name": "Philips, B. L.", "given_names": "B. L.", "surname": "Philips", "position": "Deputy Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "H. Lister", "canonical_name": "Lister, H.", "given_names": "H.", "surname": "Lister", "position": "Checker of Stores", "department": "Public Works Department - Sierra Leone", "salary_min": 450, "salary_max": 720},
    {"name": "S. C. Benjamin", "canonical_name": "Benjamin, S. C.", "given_names": "S. C.", "surname": "Benjamin", "position": "African Assistant Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "M. B. Reader", "canonical_name": "Reader, M. B.", "given_names": "M. B.", "surname": "Reader", "position": "African Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "E. T. Greenwood", "canonical_name": "Greenwood, E. T.", "given_names": "E. T.", "surname": "Greenwood", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 560, "salary_max": 600},
    {"name": "A. W. Spencer", "canonical_name": "Spencer, A. W.", "given_names": "A. W.", "surname": "Spencer", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "C. Pope", "canonical_name": "Pope, C.", "given_names": "C.", "surname": "Pope", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "E. F. Rhodes", "canonical_name": "Rhodes, E. F.", "given_names": "E. F.", "surname": "Rhodes", "position": "Mechanical Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "J. Hardman", "canonical_name": "Hardman, J.", "given_names": "J.", "surname": "Hardman", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "F. H. Bawden", "canonical_name": "Bawden, F. H.", "given_names": "F. H.", "surname": "Bawden", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "E. T. Macfoye", "canonical_name": "Macfoye, E. T.", "given_names": "E. T.", "surname": "Macfoye", "position": "Chief African Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "S. S. Jackson", "canonical_name": "Jackson, S. S.", "given_names": "S. S.", "surname": "Jackson", "position": "First Class African Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "African Clerk, Grade 1", "department": "Public Works Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. A. Thompson", "canonical_name": "Thompson, A. A.", "given_names": "A. A.", "surname": "Thompson", "position": "African Clerk, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()