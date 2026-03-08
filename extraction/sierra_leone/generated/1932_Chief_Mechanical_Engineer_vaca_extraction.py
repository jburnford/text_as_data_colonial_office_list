"""
Sierra Leone Colonial Office List 1932 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1932

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Mechanical Engineer", "department": "Railway - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "E. H. Wainwright", "canonical_name": "Wainwright, E. H.", "given_names": "E. H.", "surname": "Wainwright", "position": "Locomotive Superintendent", "department": "Railway - Sierra Leone", "salary_min": 840, "salary_max": 920},
    {"name": "T. Delmore", "canonical_name": "Delmore, T.", "given_names": "T.", "surname": "Delmore", "position": "Assistant Locomotive Superintendent", "department": "Railway - Sierra Leone", "salary_scale": "C"},
    {"name": "F. E. M. Beatley", "canonical_name": "Beatley, F. E. M.", "given_names": "F. E. M.", "surname": "Beatley", "position": "Traffic Manager", "department": "Railway - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "A. Hides", "canonical_name": "Hides, A.", "given_names": "A.", "surname": "Hides", "position": "Assistant Traffic Superintendents", "department": "Railway - Sierra Leone", "salary_scale": "A"},
    {"name": "V. Dunglinson", "canonical_name": "Dunglinson, V.", "given_names": "V.", "surname": "Dunglinson", "position": "Assistant Traffic Superintendents", "department": "Railway - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hamilton", "canonical_name": "Hamilton, J.", "given_names": "J.", "surname": "Hamilton", "position": "Assistant Traffic Superintendents", "department": "Railway - Sierra Leone", "salary_scale": "A"},
    {"name": "W. H. Salkield", "canonical_name": "Salkield, W. H.", "given_names": "W. H.", "surname": "Salkield", "position": "Assistant Traffic Superintendents", "department": "Railway - Sierra Leone", "salary_scale": "A"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Accountant", "department": "Railway - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "J. Hunter", "canonical_name": "Hunter, J.", "given_names": "J.", "surname": "Hunter", "position": "Assistant Accountants, 1st Grade", "department": "Railway - Sierra Leone", "salary_min": 600, "salary_max": 800},
    {"name": "R. J. Dickinson", "canonical_name": "Dickinson, R. J.", "given_names": "R. J.", "surname": "Dickinson", "position": "Assistant Accountants, 2nd Grade", "department": "Railway - Sierra Leone", "salary_scale": "A"},
    {"name": "A. C. Blanchfield", "canonical_name": "Blanchfield, A. C.", "given_names": "A. C.", "surname": "Blanchfield", "position": "Chief Storekeeper", "department": "Railway - Sierra Leone", "salary_min": 800, "salary_max": 800, "duty_allowance": 72},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Chief Storekeeper", "department": "Railway - Sierra Leone", "salary_scale": "A"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()