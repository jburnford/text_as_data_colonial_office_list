"""
Sierra Leone Colonial Office List 1933 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1933

OFFICIALS = [
    {"name": "R. Malthus", "canonical_name": "Malthus, R.", "given_names": "R.", "surname": "Malthus", "position": "General Manager and also Chief Mechanical Engineer (Tpy.)", "department": "Railway Department - Sierra Leone", "qualifications": ["A.M.I.M.E."], "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "R. Lane", "canonical_name": "Lane, R.", "given_names": "R.", "surname": "Lane", "position": "Assistant to General Manager", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. J. B. Hewson", "canonical_name": "Hewson, R. J. B.", "given_names": "R. J. B.", "surname": "Hewson", "position": "Chief Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "A. Woodburn", "canonical_name": "Woodburn, A.", "given_names": "A.", "surname": "Woodburn", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. Ronaldson", "canonical_name": "Ronaldson, J.", "given_names": "J.", "surname": "Ronaldson", "position": "Assistant Engineer", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "F. G. Taylor", "canonical_name": "Taylor, F. G.", "given_names": "F. G.", "surname": "Taylor", "position": "Telegraph Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 480, "salary_max": 660},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Mechanical Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "E. H. Wainwright", "canonical_name": "Wainwright, E. H.", "given_names": "E. H.", "surname": "Wainwright", "position": "Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 840, "salary_max": 920},
    {"name": "T. Delmore", "canonical_name": "Delmore, T.", "given_names": "T.", "surname": "Delmore", "position": "Assistant Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "F. E. M. Beatley", "canonical_name": "Beatley, F. E. M.", "given_names": "F. E. M.", "surname": "Beatley", "position": "Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "V. Dunglinson", "canonical_name": "Dunglinson, V.", "given_names": "V.", "surname": "Dunglinson", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hamilton", "canonical_name": "Hamilton, J.", "given_names": "J.", "surname": "Hamilton", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "W. H. Salkfield", "canonical_name": "Salkfield, W. H.", "given_names": "W. H.", "surname": "Salkfield", "position": "Assistant Traffic Superintendent", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hunter", "canonical_name": "Hunter, J.", "given_names": "J.", "surname": "Hunter", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 920, "salary_max": 920, "duty_allowance": 92},
    {"name": "A. Hides", "canonical_name": "Hides, A.", "given_names": "A.", "surname": "Hides", "position": "Assistant Accountant, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. J. Dickinson", "canonical_name": "Dickinson, R. J.", "given_names": "R. J.", "surname": "Dickinson", "position": "Assistant Accountant, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "A. C. Blanchfield", "canonical_name": "Blanchfield, A. C.", "given_names": "A. C.", "surname": "Blanchfield", "position": "Chief Storekeeper", "department": "Railway Department - Sierra Leone", "salary_min": 800, "salary_max": 800, "duty_allowance": 72},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Chief Storekeeper", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "M. A. Greene", "canonical_name": "Greene, M. A.", "given_names": "M. A.", "surname": "Greene", "position": "Lieut.-Colonel", "department": "Sierra Leone Battalion, Royal West African Frontier Force - Sierra Leone", "military_rank": "Lieut.-Colonel", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 182},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Adjutant", "department": "Sierra Leone Battalion, Royal West African Frontier Force - Sierra Leone", "salary_min": 700, "salary_max": 700, "duty_allowance": 91},
    {"name": "F. G. Winward", "canonical_name": "Winward, F. G.", "given_names": "F. G.", "surname": "Winward", "position": "Quartermaster", "department": "Sierra Leone Battalion, Royal West African Frontier Force - Sierra Leone", "military_rank": "Captain", "salary_min": 600, "salary_max": 720},
    {"name": "W. W. Dyer", "canonical_name": "Dyer, W. W.", "given_names": "W. W.", "surname": "Dyer", "position": "Care and Maintenance", "department": "Sierra Leone Battalion, Royal West African Frontier Force - Sierra Leone", "military_rank": "Captain", "salary_min": 750, "salary_max": 750}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()