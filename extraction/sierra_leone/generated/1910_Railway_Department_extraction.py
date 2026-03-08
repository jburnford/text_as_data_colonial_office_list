"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "J. R. W. Comber", "canonical_name": "Comber, J. R. W.", "given_names": "J. R. W.", "surname": "Comber", "position": "General Manager and Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 625, "salary_max": 700},
    {"name": "R. W. Espeut", "canonical_name": "Espeut, R. W.", "given_names": "R. W.", "surname": "Espeut", "position": "Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "F. A. Neck", "canonical_name": "Neck, F. A.", "given_names": "F. A.", "surname": "Neck", "position": "Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "E. D. Willoughby", "canonical_name": "Willoughby, E. D.", "given_names": "E. D.", "surname": "Willoughby", "position": "Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. H. Salt", "canonical_name": "Salt, A. H.", "given_names": "A. H.", "surname": "Salt", "position": "Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "R. M. Johnstone", "canonical_name": "Johnstone, R. M.", "given_names": "R. M.", "surname": "Johnstone", "position": "Junior Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "S. Renshaw", "canonical_name": "Renshaw, S.", "given_names": "S.", "surname": "Renshaw", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 450, "salary_max": 450, "duty_allowance": 90},
    {"name": "E. G. Barker", "canonical_name": "Barker, E. G.", "given_names": "E. G.", "surname": "Barker", "position": "Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 550, "salary_max": 650},
    {"name": "E. D. Jenkins", "canonical_name": "Jenkins, E. D.", "given_names": "E. D.", "surname": "Jenkins", "position": "Permanent Way Inspector", "department": "Railway Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "R. L. Hunt", "canonical_name": "Hunt, R. L.", "given_names": "R. L.", "surname": "Hunt", "position": "Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "R. J. Morison", "canonical_name": "Morison, R. J.", "given_names": "R. J.", "surname": "Morison", "position": "Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "M. N. Forster", "canonical_name": "Forster, M. N.", "given_names": "M. N.", "surname": "Forster", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "J. D. Martin", "canonical_name": "Martin, J. D.", "given_names": "J. D.", "surname": "Martin", "position": "Senior Assistant Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 450, "salary_max": 450, "duty_allowance": 90},
    {"name": "A. J. Cullen", "canonical_name": "Cullen, A. J.", "given_names": "A. J.", "surname": "Cullen", "position": "Traffic Officer, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_min": 275, "salary_max": 325},
    {"name": "J. T. Tillotson", "canonical_name": "Tillotson, J. T.", "given_names": "J. T.", "surname": "Tillotson", "position": "Traffic Officer, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_min": 275, "salary_max": 325},
    {"name": "B. Stewart", "canonical_name": "Stewart, B.", "given_names": "B.", "surname": "Stewart", "position": "Traffic Officer, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_min": 275, "salary_max": 325},
    {"name": "E. H. Barker", "canonical_name": "Barker, E. H.", "given_names": "E. H.", "surname": "Barker", "position": "Traffic Officer, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_min": 225, "salary_max": 245},
    {"name": "J. B. Sidney", "canonical_name": "Sidney, J. B.", "given_names": "J. B.", "surname": "Sidney", "position": "Clerk to General Manager", "department": "Railway Department - Sierra Leone", "salary_min": 200, "salary_max": 275},
    {"name": "S. A. Macauley", "canonical_name": "Macauley, S. A.", "given_names": "S. A.", "surname": "Macauley", "position": "Chief Clerk to Clerk", "department": "Railway Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "P. Nicolls", "canonical_name": "Nicolls, P.", "given_names": "P.", "surname": "Nicolls", "position": "Traffic Supervisor and Travelling Inspector of Accounts", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "S. L. Farmer", "canonical_name": "Farmer, S. L.", "given_names": "S. L.", "surname": "Farmer", "position": "Superintendent of Telegraphs", "department": "Railway Department - Sierra Leone", "salary_min": 200, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()