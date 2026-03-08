"""
Sierra Leone Colonial Office List 1923 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1923

OFFICIALS = [
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "qualifications": ["M. Inst. C.E."], "salary_min": 1000, "duty_allowance": 200},
    {"name": "A. S. Bradshaw", "canonical_name": "Bradshaw, A. S.", "given_names": "A. S.", "surname": "Bradshaw", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 960, "duty_allowance": 96},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Sanitary Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E.", "F.S.I."], "salary_min": 960, "duty_allowance": 96},
    {"name": "G. Stanley", "canonical_name": "Stanley, G.", "given_names": "G.", "surname": "Stanley", "position": "Executive Engineer, Grade 1", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 720, "salary_max": 920, "seniority_allowance": 72},
    {"name": "R. Summerscale", "canonical_name": "Summerscale, R.", "given_names": "R.", "surname": "Summerscale", "position": "Executive Engineers, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.S.A."], "salary_min": 600, "salary_max": 720},
    {"name": "B. W. Fitch-Jones", "canonical_name": "Fitch-Jones, B. W.", "given_names": "B. W.", "surname": "Fitch-Jones", "position": "Executive Engineers, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Executive Engineers, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.A."], "salary_min": 600, "salary_max": 720},
    {"name": "R. Temple", "canonical_name": "Temple, R.", "given_names": "R.", "surname": "Temple", "position": "Surveyors", "department": "Public Works Department - Sierra Leone", "qualifications": ["F.S.I."], "salary_min": 480, "salary_max": 720},
    {"name": "J. L. Fenton", "canonical_name": "Fenton, J. L.", "given_names": "J. L.", "surname": "Fenton", "position": "Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "seniority_allowance": 72},
    {"name": "B. L. Phillips", "canonical_name": "Phillips, B. L.", "given_names": "B. L.", "surname": "Phillips", "position": "Deputy Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 450, "salary_max": 720},
    {"name": "S. C. Benjamin", "canonical_name": "Benjamin, S. C.", "given_names": "S. C.", "surname": "Benjamin", "position": "African Assistant Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "S. B. Gabbidon", "canonical_name": "Gabbidon, S. B.", "given_names": "S. B.", "surname": "Gabbidon", "position": "African Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "J. H. Sheldrake", "canonical_name": "Sheldrake, J. H.", "given_names": "J. H.", "surname": "Sheldrake", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "allowances": "50l."},
    {"name": "E. T. Greenwood", "canonical_name": "Greenwood, E. T.", "given_names": "E. T.", "surname": "Greenwood", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "A. W. Spencer", "canonical_name": "Spencer, A. W.", "given_names": "A. W.", "surname": "Spencer", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "C. Pope", "canonical_name": "Pope, C.", "given_names": "C.", "surname": "Pope", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "E. F. Rhodes", "canonical_name": "Rhodes, E. F.", "given_names": "E. F.", "surname": "Rhodes", "position": "Mechanical Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "G. Weller", "canonical_name": "Weller, G.", "given_names": "G.", "surname": "Weller", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "J. Hardman", "canonical_name": "Hardman, J.", "given_names": "J.", "surname": "Hardman", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "F. H. Bawden", "canonical_name": "Bawden, F. H.", "given_names": "F. H.", "surname": "Bawden", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "E. T. Macfoye", "canonical_name": "Macfoye, E. T.", "given_names": "E. T.", "surname": "Macfoye", "position": "Chief African Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "S. S. Jackson", "canonical_name": "Jackson, S. S.", "given_names": "S. S.", "surname": "Jackson", "position": "First Class African Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "African Clerks, Grade 1", "department": "Public Works Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "F. W. Hooke", "canonical_name": "Hooke, F. W.", "given_names": "F. W.", "surname": "Hooke", "position": "African Clerks, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "African Clerks, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 140, "salary_max": 180},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()