"""
Sierra Leone Colonial Office List 1923 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1923

OFFICIALS = [
    {"name": "E. G. Barker", "canonical_name": "Barker, E. G.", "given_names": "E. G.", "surname": "Barker", "position": "General Manager, Chief Mechanical Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "J. B. Sidney", "canonical_name": "Sidney, J. B.", "given_names": "J. B.", "surname": "Sidney", "position": "Office Assistant", "department": "Railway Department - Sierra Leone", "salary_min": 450, "salary_max": 600},
    {"name": "F. St. J. Gebbie", "canonical_name": "Gebbie, F. St. J.", "given_names": "F. St. J.", "surname": "Gebbie", "position": "Chief Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "R. M. Johnstone", "canonical_name": "Johnstone, R. M.", "given_names": "R. M.", "surname": "Johnstone", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 920},
    {"name": "A. R. Homan", "canonical_name": "Homan, A. R.", "given_names": "A. R.", "surname": "Homan", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 920},
    {"name": "J. M. M. Wellens", "canonical_name": "Wellens, J. M. M.", "given_names": "J. M. M.", "surname": "Wellens", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 920},
    {"name": "A. E. Crocker", "canonical_name": "Crocker, A. E.", "given_names": "A. E.", "surname": "Crocker", "position": "Inspector of Works", "department": "Railway Department - Sierra Leone", "salary_min": 600, "salary_max": 600},
    {"name": "W. L. King", "canonical_name": "King, W. L.", "given_names": "W. L.", "surname": "King", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "J. A. Wood", "canonical_name": "Wood, J. A.", "given_names": "J. A.", "surname": "Wood", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "P. S. Shaw", "canonical_name": "Shaw, P. S.", "given_names": "P. S.", "surname": "Shaw", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "A. Hides", "canonical_name": "Hides, A.", "given_names": "A.", "surname": "Hides", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "V. Dunglinson", "canonical_name": "Dunglinson, V.", "given_names": "V.", "surname": "Dunglinson", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 450, "salary_max": 800},
    {"name": "L. Belmar", "canonical_name": "Belmar, L.", "given_names": "L.", "surname": "Belmar", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "A. E. Munn", "canonical_name": "Munn, A. E.", "given_names": "A. E.", "surname": "Munn", "position": "Assistant Accountant, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_min": 600, "salary_max": 800},
    {"name": "H. C. F. Fisher", "canonical_name": "Fisher, H. C. F.", "given_names": "H. C. F.", "surname": "Fisher", "position": "Assistant Accountant, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_min": 450, "salary_max": 720},
    {"name": "A. C. Blanchfield", "canonical_name": "Blanchfield, A. C.", "given_names": "A. C.", "surname": "Blanchfield", "position": "Assistant Accountant, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_min": 450, "salary_max": 720},
    {"name": "C. E. Hoyte", "canonical_name": "Hoyte, C. E.", "given_names": "C. E.", "surname": "Hoyte", "position": "Principal Clerk, Accounts Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "L. O. W. Taylor", "canonical_name": "Taylor, L. O. W.", "given_names": "L. O. W.", "surname": "Taylor", "position": "Principal Clerk, Stores Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "H. R. Pratt", "canonical_name": "Pratt, H. R.", "given_names": "H. R.", "surname": "Pratt", "position": "Principal Clerk, Traffic Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. J. Aubee", "canonical_name": "Aubee, M. J.", "given_names": "M. J.", "surname": "Aubee", "position": "Principal Clerk, Loco. Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()