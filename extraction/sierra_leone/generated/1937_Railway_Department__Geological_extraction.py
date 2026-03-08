"""
Sierra Leone Colonial Office List 1937 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1937

OFFICIALS = [
    {"name": "F. E. M. Beatley", "canonical_name": "Beatley, F. E. M.", "given_names": "F. E. M.", "surname": "Beatley", "position": "General Manager and Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240, "honors": ["O.B.E."]},
    {"name": "W. A. FitzJohn", "canonical_name": "FitzJohn, W. A.", "given_names": "W. A.", "surname": "FitzJohn", "position": "Office Assistant", "department": "Railway Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "H. Weightman", "canonical_name": "Weightman, H.", "given_names": "H.", "surname": "Weightman", "position": "Chief Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "A. Woodburn", "canonical_name": "Woodburn, A.", "given_names": "A.", "surname": "Woodburn", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "salary_scale": "C", "qualifications": ["A.M.I.C.E."]},
    {"name": "J. Ronaldson", "canonical_name": "Ronaldson, J.", "given_names": "J.", "surname": "Ronaldson", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "F. G. Taylor", "canonical_name": "Taylor, F. G.", "given_names": "F. G.", "surname": "Taylor", "position": "Telegraph Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 480, "salary_max": 720, "qualifications": ["F.R.S.A.", "M.I.R.S.E.", "Assoc.I.E.E.", "F.R.G.S."]},
    {"name": "H. E. Allwood", "canonical_name": "Allwood, H. E.", "given_names": "H. E.", "surname": "Allwood", "position": "Chief Mechanical Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 920, "salary_max": 920, "duty_allowance": 92, "qualifications": ["M.I.Loco.E."]},
    {"name": "T. Delmore", "canonical_name": "Delmore, T.", "given_names": "T.", "surname": "Delmore", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. R. Best", "canonical_name": "Best, J. R.", "given_names": "J. R.", "surname": "Best", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "V. Dunglinson", "canonical_name": "Dunglinson, V.", "given_names": "V.", "surname": "Dunglinson", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hamilton", "canonical_name": "Hamilton, J.", "given_names": "J.", "surname": "Hamilton", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "W. H. Salkield", "canonical_name": "Salkield, W. H.", "given_names": "W. H.", "surname": "Salkield", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hunter", "canonical_name": "Hunter, J.", "given_names": "J.", "surname": "Hunter", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 920, "salary_max": 920, "duty_allowance": 92, "qualifications": ["A.M.Inst.T."]},
    {"name": "A. Hides", "canonical_name": "Hides, A.", "given_names": "A.", "surname": "Hides", "position": "Assistant Accountant, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "A. C. Blanchfield", "canonical_name": "Blanchfield, A. C.", "given_names": "A. C.", "surname": "Blanchfield", "position": "Chief Storekeeper", "department": "Railway Department - Sierra Leone", "salary_min": 800, "salary_max": 800, "duty_allowance": 72},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Director, Geological Survey", "department": "Geological and Mines - Sierra Leone"},
    {"name": "J. D. Pollett", "canonical_name": "Pollett, J. D.", "given_names": "J. D.", "surname": "Pollett", "position": "Assistant Geologist", "department": "Geological and Mines - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "K. E. Heesom", "canonical_name": "Heesom, K. E.", "given_names": "K. E.", "surname": "Heesom", "position": "Inspector of Mines", "department": "Geological and Mines - Sierra Leone", "salary_scale": "C"},
    {"name": "F. A. Cassidy", "canonical_name": "Cassidy, F. A.", "given_names": "F. A.", "surname": "Cassidy", "position": "Assist. Inspector of Mines", "department": "Geological and Mines - Sierra Leone", "salary_scale": "C"},
    {"name": "A. Akiwumi", "canonical_name": "Akiwumi, A.", "given_names": "A.", "surname": "Akiwumi", "position": "African Assistant Inspector of Mines", "department": "Geological and Mines - Sierra Leone", "salary_min": 300, "salary_max": 450}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()