"""
Sierra Leone Colonial Office List 1925 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1925

OFFICIALS = [
    {"name": "C. R. Webb", "canonical_name": "Webb, C. R.", "given_names": "C. R.", "surname": "Webb", "position": "General Manager and Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280},
    {"name": "J. B. Sidney", "canonical_name": "Sidney, J. B.", "given_names": "J. B.", "surname": "Sidney", "position": "Office Assistant", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "M. W. B. Wright", "canonical_name": "Wright, M. W. B.", "given_names": "M. W. B.", "surname": "Wright", "position": "Principal Clerk, Management Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "T. A. Young", "canonical_name": "Young, T. A.", "given_names": "T. A.", "surname": "Young", "position": "Chief Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "A. R. Homan", "canonical_name": "Homan, A. R.", "given_names": "A. R.", "surname": "Homan", "position": "Assistant Engineers", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. M. M. Whellens", "canonical_name": "Whellens, J. M. M.", "given_names": "J. M. M.", "surname": "Whellens", "position": "Assistant Engineers", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. E. Crocker", "canonical_name": "Crocker, A. E.", "given_names": "A. E.", "surname": "Crocker", "position": "Assistant Engineers", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. Woodburn", "canonical_name": "Woodburn, A.", "given_names": "A.", "surname": "Woodburn", "position": "Assistant Engineers", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "G. Creswell", "canonical_name": "Creswell, G.", "given_names": "G.", "surname": "Creswell", "position": "Assistant Telegraph Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "R. Malthus", "canonical_name": "Malthus, R.", "given_names": "R.", "surname": "Malthus", "position": "Chief Mechanical Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "W. L. King", "canonical_name": "King, W. L.", "given_names": "W. L.", "surname": "King", "position": "Assistant Locomotive Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. A. Wood", "canonical_name": "Wood, J. A.", "given_names": "J. A.", "surname": "Wood", "position": "Assistant Locomotive Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "P. S. Shaw", "canonical_name": "Shaw, P. S.", "given_names": "P. S.", "surname": "Shaw", "position": "Assistant Traffic Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "A. Hides", "canonical_name": "Hides, A.", "given_names": "A.", "surname": "Hides", "position": "Assistant Traffic Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "V. Dunglinson", "canonical_name": "Dunglinson, V.", "given_names": "V.", "surname": "Dunglinson", "position": "Assistant Traffic Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "L. Belmar", "canonical_name": "Belmar, L.", "given_names": "L.", "surname": "Belmar", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "H. C. F. Fisher", "canonical_name": "Fisher, H. C. F.", "given_names": "H. C. F.", "surname": "Fisher", "position": "Assistant Accountants, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_min": 600, "salary_max": 800},
    {"name": "R. J. Dickenson", "canonical_name": "Dickenson, R. J.", "given_names": "R. J.", "surname": "Dickenson", "position": "Assistant Accountants, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "A. C. Blanchfield", "canonical_name": "Blanchfield, A. C.", "given_names": "A. C.", "surname": "Blanchfield", "position": "Chief Storekeeper", "department": "Railway Department - Sierra Leone", "salary_min": 600, "salary_max": 720, "duty_allowance": 72},
    {"name": "C. W. Adamson", "canonical_name": "Adamson, C. W.", "given_names": "C. W.", "surname": "Adamson", "position": "Assistant Storekeeper", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. C. Hamilton", "canonical_name": "Hamilton, J. C.", "given_names": "J. C.", "surname": "Hamilton", "position": "Staff Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "W. I. Johnson", "canonical_name": "Johnson, W. I.", "given_names": "W. I.", "surname": "Johnson", "position": "Principal Clerk, Accounts Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "L. O. W. Taylor", "canonical_name": "Taylor, L. O. W.", "given_names": "L. O. W.", "surname": "Taylor", "position": "Principal Clerk, Stores Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "H. R. Pratt", "canonical_name": "Pratt, H. R.", "given_names": "H. R.", "surname": "Pratt", "position": "Principal Clerk, Traffic Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. J. Aubee", "canonical_name": "Aubee, M. J.", "given_names": "M. J.", "surname": "Aubee", "position": "Principal Clerk, Loco. Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "J. E. Smith", "canonical_name": "Smith, J. E.", "given_names": "J. E.", "surname": "Smith", "position": "Principal Clerk, Engineering Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()