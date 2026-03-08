"""
Sierra Leone Colonial Office List 1940 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1940

OFFICIALS = [
    {"name": "A. Allan", "canonical_name": "Allan, A.", "given_names": "A.", "surname": "Allan", "position": "General Manager and Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 1400, "salary_max": 1400},
    {"name": "W. A. FitzJohn", "canonical_name": "FitzJohn, W. A.", "given_names": "W. A.", "surname": "FitzJohn", "position": "Office Assistant", "department": "Railway Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "G. S. Dick", "canonical_name": "Dick, G. S.", "given_names": "G. S.", "surname": "Dick", "position": "Chief Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "A. Woodburn", "canonical_name": "Woodburn, A.", "given_names": "A.", "surname": "Woodburn", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_scale": "C"},
    {"name": "J. Ronaldson", "canonical_name": "Ronaldson, J.", "given_names": "J.", "surname": "Ronaldson", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Telegraph Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 475, "salary_max": 840},
    {"name": "H. E. Allwood", "canonical_name": "Allwood, H. E.", "given_names": "H. E.", "surname": "Allwood", "position": "Chief Mechanical Engineer", "department": "Railway Department - Sierra Leone", "qualifications": ["M.I.Loc.E."], "salary_min": 1000, "salary_max": 1000},
    {"name": "T. Delmore", "canonical_name": "Delmore, T.", "given_names": "T.", "surname": "Delmore", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. R. Best", "canonical_name": "Best, J. R.", "given_names": "J. R.", "surname": "Best", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 490, "salary_max": 720},
    {"name": "V. Dunglinson", "canonical_name": "Dunglinson, V.", "given_names": "V.", "surname": "Dunglinson", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hamilton", "canonical_name": "Hamilton, J.", "given_names": "J.", "surname": "Hamilton", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "W. H. Salkield", "canonical_name": "Salkield, W. H.", "given_names": "W. H.", "surname": "Salkield", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hunter", "canonical_name": "Hunter, J.", "given_names": "J.", "surname": "Hunter", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "qualifications": ["A.M.Inst.T."], "salary_min": 920, "salary_max": 920, "duty_allowance": 92},
    {"name": "A. Hides", "canonical_name": "Hides, A.", "given_names": "A.", "surname": "Hides", "position": "Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 800, "salary_max": 800},
    {"name": "C. Innes", "canonical_name": "Innes, C.", "given_names": "C.", "surname": "Innes", "position": "Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 720},
    {"name": "J. H. Tracey", "canonical_name": "Tracey, J. H.", "given_names": "J. H.", "surname": "Tracey", "position": "Stock Verifier", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 600},
    {"name": "A. C. Blanchfield", "canonical_name": "Blanchfield, A. C.", "given_names": "A. C.", "surname": "Blanchfield", "position": "Chief Storekeeper", "department": "Railway Department - Sierra Leone", "salary_min": 800, "salary_max": 800, "duty_allowance": 72},
    {"name": "S. G. Thompson", "canonical_name": "Thompson, S. G.", "given_names": "S. G.", "surname": "Thompson", "position": "African Asst. Chief Storekeeper", "department": "Railway Department - Sierra Leone", "salary_min": 310, "salary_max": 450}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()