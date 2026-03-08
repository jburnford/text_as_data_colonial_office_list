"""
Sierra Leone Colonial Office List 1905 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1905

OFFICIALS = [
    {"name": "J. R. W. Comber", "canonical_name": "Comber, J. R. W.", "given_names": "J. R. W.", "surname": "Comber", "position": "General Manager and Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 625, "salary_max": 700},
    {"name": "R. W. Espeut", "canonical_name": "Espeut, R. W.", "given_names": "R. W.", "surname": "Espeut", "position": "Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "F. A. Neck", "canonical_name": "Neck, F. A.", "given_names": "F. A.", "surname": "Neck", "position": "Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "J. W. Owen", "canonical_name": "Owen, J. W.", "given_names": "J. W.", "surname": "Owen", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 600, "salary_max": 650},
    {"name": "E. D. Jenkins", "canonical_name": "Jenkins, E. D.", "given_names": "E. D.", "surname": "Jenkins", "position": "Permanent Way Inspector", "department": "Railway Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "G. P. Eaton", "canonical_name": "Eaton, G. P.", "given_names": "G. P.", "surname": "Eaton", "position": "Inspector of Works and Buildings", "department": "Railway Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "H. E. Goodship", "canonical_name": "Goodship, H. E.", "given_names": "H. E.", "surname": "Goodship", "position": "Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "2nd Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "D. Robinson", "canonical_name": "Robinson, D.", "given_names": "D.", "surname": "Robinson", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. D. Martin", "canonical_name": "Martin, J. D.", "given_names": "J. D.", "surname": "Martin", "position": "Senior Assistant Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "T. E. Kewley", "canonical_name": "Kewley, T. E.", "given_names": "T. E.", "surname": "Kewley", "position": "Assistant Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 275, "salary_max": 300},
    {"name": "J. Lilley", "canonical_name": "Lilley, J.", "given_names": "J.", "surname": "Lilley", "position": "District Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 275, "salary_max": 300},
    {"name": "B. Stewart", "canonical_name": "Stewart, B.", "given_names": "B.", "surname": "Stewart", "position": "Chief Traffic Inspector", "department": "Railway Department - Sierra Leone", "salary_min": 250, "salary_max": 275},
    {"name": "C. Morris", "canonical_name": "Morris, C.", "given_names": "C.", "surname": "Morris", "position": "Traffic Inspector", "department": "Railway Department - Sierra Leone", "salary_min": 225, "salary_max": 250},
    {"name": "R. L. Hunt", "canonical_name": "Hunt, R. L.", "given_names": "R. L.", "surname": "Hunt", "position": "Clerk to General Manager", "department": "Railway Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "S. A. Macaulay", "canonical_name": "Macaulay, S. A.", "given_names": "S. A.", "surname": "Macaulay", "position": "Chief Clerk to General Manager", "department": "Railway Department - Sierra Leone", "salary_min": 110, "salary_max": 110},
    {"name": "Peter Nicolls", "canonical_name": "Nicolls, Peter", "given_names": "Peter", "surname": "Nicolls", "position": "Supervisor of Traffic and Travelling Inspector of Accounts", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()