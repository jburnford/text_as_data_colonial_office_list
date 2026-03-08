"""
Sierra Leone Colonial Office List 1922 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1922

OFFICIALS = [
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "qualifications": ["M. Inst. C.E."]},
    {"name": "A. S. Bradshaw", "canonical_name": "Bradshaw, A. S.", "given_names": "A. S.", "surname": "Bradshaw", "position": "Assistant ditto", "department": "Public Works Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["A.M.I.C.E."]},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Sanitary Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["A.M.I.C.E.", "F.S.I."]},
    {"name": "G. Stanley", "canonical_name": "Stanley, G.", "given_names": "G.", "surname": "Stanley", "position": "Executive Engineer, Grade I", "department": "Public Works Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "seniority allowance 72l.", "qualifications": ["A.M.I.C.E."]},
    {"name": "G. Wilson", "canonical_name": "Wilson, G.", "given_names": "G.", "surname": "Wilson", "position": "Executive Engineers, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "R. Summerscale", "canonical_name": "Summerscale, R.", "given_names": "R.", "surname": "Summerscale", "position": "Executive Engineers, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "B. W. Fitch-Jones", "canonical_name": "Fitch-Jones, B. W.", "given_names": "B. W.", "surname": "Fitch-Jones", "position": "Executive Engineers, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 720, "qualifications": ["M.S.A."]},
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Executive Engineers, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 720, "qualifications": ["M.A."]},
    {"name": "R. Temple", "canonical_name": "Temple, R.", "given_names": "R.", "surname": "Temple", "position": "Surveyors", "department": "Public Works Department - Sierra Leone", "salary_min": 480, "salary_max": 720, "qualifications": ["F.S.I."]},
    {"name": "G. L. Strachan", "canonical_name": "Strachan, G. L.", "given_names": "G. L.", "surname": "Strachan", "position": "Surveyors", "department": "Public Works Department - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "J. L. Fenton", "canonical_name": "Fenton, J. L.", "given_names": "J. L.", "surname": "Fenton", "position": "Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "allowances": "seniority allowance 72l. after 720l."},
    {"name": "B. L. Phillips", "canonical_name": "Phillips, B. L.", "given_names": "B. L.", "surname": "Phillips", "position": "Deputy Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 450, "salary_max": 720},
    {"name": "S. C. Benjamin", "canonical_name": "Benjamin, S. C.", "given_names": "S. C.", "surname": "Benjamin", "position": "African Assistant Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "S. B. Gabbidon", "canonical_name": "Gabbidon, S. B.", "given_names": "S. B.", "surname": "Gabbidon", "position": "African Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "J. H. Sheldrake", "canonical_name": "Sheldrake, J. H.", "given_names": "J. H.", "surname": "Sheldrake", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 600, "allowances": "and personal allowance 50l."},
    {"name": "E. T. Greenwood", "canonical_name": "Greenwood, E. T.", "given_names": "E. T.", "surname": "Greenwood", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "A. W. Spencer", "canonical_name": "Spencer, A. W.", "given_names": "A. W.", "surname": "Spencer", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "C. Pope", "canonical_name": "Pope, C.", "given_names": "C.", "surname": "Pope", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "W. Clay", "canonical_name": "Clay, W.", "given_names": "W.", "surname": "Clay", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "L. Durham", "canonical_name": "Durham, L.", "given_names": "L.", "surname": "Durham", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "H. W. Daley", "canonical_name": "Daley, H. W.", "given_names": "H. W.", "surname": "Daley", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "E. F. Rhodes", "canonical_name": "Rhodes, E. F.", "given_names": "E. F.", "surname": "Rhodes", "position": "Foreman Fitter", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "G. Wellar", "canonical_name": "Wellar, G.", "given_names": "G.", "surname": "Wellar", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "J. Hardman", "canonical_name": "Hardman, J.", "given_names": "J.", "surname": "Hardman", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "F. H. Bawden", "canonical_name": "Bawden, F. H.", "given_names": "F. H.", "surname": "Bawden", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "W. S. Pierce", "canonical_name": "Pierce, W. S.", "given_names": "W. S.", "surname": "Pierce", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "E. T. Macfoye", "canonical_name": "Macfoye, E. T.", "given_names": "E. T.", "surname": "Macfoye", "position": "Chief African Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "S. S. Jackson", "canonical_name": "Jackson, S. S.", "given_names": "S. S.", "surname": "Jackson", "position": "First Class African Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "African Clerks, Grade I", "department": "Public Works Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "G. A. Harding", "canonical_name": "Harding, G. A.", "given_names": "G. A.", "surname": "Harding", "position": "African Clerks, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 140, "salary_max": 180}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()