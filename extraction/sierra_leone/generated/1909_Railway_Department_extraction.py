"""
Sierra Leone Colonial Office List 1909 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1909

OFFICIALS = [
    {"name": "J. R. W. Comber", "canonical_name": "Comber, J. R. W.", "given_names": "J. R. W.", "surname": "Comber", "position": "General Manager and Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 625, "salary_max": 700},
    {"name": "R. W. Espeut", "canonical_name": "Espeut, R. W.", "given_names": "R. W.", "surname": "Espeut", "position": "Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "F. A. Neck", "canonical_name": "Neck, F. A.", "given_names": "F. A.", "surname": "Neck", "position": "Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "E. D. Willoughby", "canonical_name": "Willoughby, E. D.", "given_names": "E. D.", "surname": "Willoughby", "position": "Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. H. Salt", "canonical_name": "Salt, A. H.", "given_names": "A. H.", "surname": "Salt", "position": "Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "R. M. Johnstone", "canonical_name": "Johnstone, R. M.", "given_names": "R. M.", "surname": "Johnstone", "position": "Junior Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. W. Owen", "canonical_name": "Owen, J. W.", "given_names": "J. W.", "surname": "Owen", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "E. G. Barker", "canonical_name": "Barker, E. G.", "given_names": "E. G.", "surname": "Barker", "position": "Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 550, "salary_max": 650},
    {"name": "E. D. Jenkins", "canonical_name": "Jenkins, E. D.", "given_names": "E. D.", "surname": "Jenkins", "position": "Permanent Way Inspector", "department": "Railway Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "R. L. Hunt", "canonical_name": "Hunt, R. L.", "given_names": "R. L.", "surname": "Hunt", "position": "Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "R. J. Morison", "canonical_name": "Morison, R. J.", "given_names": "R. J.", "surname": "Morison", "position": "Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. D. Robin son", "canonical_name": "Robin son, J. D.", "given_names": "J. D.", "surname": "Robin son", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "J. D. Martin", "canonical_name": "Martin, J. D.", "given_names": "J. D.", "surname": "Martin", "position": "Senior Assistant Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "T. E. Kewley", "canonical_name": "Kewley, T. E.", "given_names": "T. E.", "surname": "Kewley", "position": "Traffic Officer, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_min": 275, "salary_max": 325},
    {"name": "A. J. Cullen", "canonical_name": "Cullen, A. J.", "given_names": "A. J.", "surname": "Cullen", "position": "Traffic Officer, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_min": 275, "salary_max": 325},
    {"name": "E. H. Barker", "canonical_name": "Barker, E. H.", "given_names": "E. H.", "surname": "Barker", "position": "Traffic Officer, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_min": 250, "salary_max": 275},
    {"name": "B. Stewart", "canonical_name": "Stewart, B.", "given_names": "B.", "surname": "Stewart", "position": "Chief Traffic Inspector and Convenor", "department": "Railway Department - Sierra Leone", "salary_min": 275, "salary_max": 275},
    {"name": "J. B. Sidney", "canonical_name": "Sidney, J. B.", "given_names": "J. B.", "surname": "Sidney", "position": "Clerk to General Manager", "department": "Railway Department - Sierra Leone", "salary_min": 200, "salary_max": 275},
    {"name": "S. A. Macauley", "canonical_name": "Macauley, S. A.", "given_names": "S. A.", "surname": "Macauley", "position": "Chief Clerk to ditto", "department": "Railway Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "P. Nicolls", "canonical_name": "Nicolls, P.", "given_names": "P.", "surname": "Nicolls", "position": "Traffic Supervisor and Travelling Inspector of Accounts", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()