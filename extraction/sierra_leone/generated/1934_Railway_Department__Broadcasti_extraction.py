"""
Sierra Leone Colonial Office List 1934 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1934

OFFICIALS = [
    {"name": "F. E. M. Beasley", "canonical_name": "Beasley, F. E. M.", "given_names": "F. E. M.", "surname": "Beasley", "position": "General Manager and Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "R. Lane", "canonical_name": "Lane, R.", "given_names": "R.", "surname": "Lane", "position": "Assistant to General Manager", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. R. C. Tyler", "canonical_name": "Tyler, J. R. C.", "given_names": "J. R. C.", "surname": "Tyler", "position": "Senior Assistant Engineer", "department": "Railway Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_scale": "C", "duty_allowance": 92},
    {"name": "A. Woodburn", "canonical_name": "Woodburn, A.", "given_names": "A.", "surname": "Woodburn", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_scale": "C"},
    {"name": "J. Ronaldson", "canonical_name": "Ronaldson, J.", "given_names": "J.", "surname": "Ronaldson", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "F. G. Taylor", "canonical_name": "Taylor, F. G.", "given_names": "F. G.", "surname": "Taylor", "position": "Telegraph Engineer", "department": "Railway Department - Sierra Leone", "qualifications": ["F.R.S.A.", "M.I.R.S.E.", "Assoc.I.E.E.", "F.R.G.S."], "salary_min": 480, "salary_max": 720},
    {"name": "H. E. Allwood", "canonical_name": "Allwood, H. E.", "given_names": "H. E.", "surname": "Allwood", "position": "Chief Mechanical Engineer", "department": "Railway Department - Sierra Leone", "qualifications": ["M.I.Loco.E."], "salary_min": 920, "salary_max": 920, "duty_allowance": 92},
    {"name": "T. Delmore", "canonical_name": "Delmore, T.", "given_names": "T.", "surname": "Delmore", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. R. Best", "canonical_name": "Best, J. R.", "given_names": "J. R.", "surname": "Best", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "V. Dunglinson", "canonical_name": "Dunglinson, V.", "given_names": "V.", "surname": "Dunglinson", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hamilton", "canonical_name": "Hamilton, J.", "given_names": "J.", "surname": "Hamilton", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "W. H. Salkield", "canonical_name": "Salkield, W. H.", "given_names": "W. H.", "surname": "Salkield", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hunter", "canonical_name": "Hunter, J.", "given_names": "J.", "surname": "Hunter", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "qualifications": ["A.M.Inst.T."], "salary_min": 920, "salary_max": 920, "duty_allowance": 92},
    {"name": "A. Hides", "canonical_name": "Hides, A.", "given_names": "A.", "surname": "Hides", "position": "Assistant Accountant, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. J. Dickinson", "canonical_name": "Dickinson, R. J.", "given_names": "R. J.", "surname": "Dickinson", "position": "Assistant Accountant, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "A. C. Blanchfield", "canonical_name": "Blanchfield, A. C.", "given_names": "A. C.", "surname": "Blanchfield", "position": "Chief Storekeeper", "department": "Railway Department - Sierra Leone", "salary_min": 800, "salary_max": 800, "duty_allowance": 72},
    {"name": "F. A. W. Byron", "canonical_name": "Byron, F. A. W.", "given_names": "F. A. W.", "surname": "Byron", "position": "Broadcast Officer", "department": "Broadcasting - Sierra Leone", "salary_min": 540, "salary_max": 720}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()