"""
Sierra Leone Colonial Office List 1930 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1930

OFFICIALS = [
    {"name": "C. R. Webb", "canonical_name": "Webb, C. R.", "given_names": "C. R.", "surname": "Webb", "position": "General Manager and Traffic Manager", "department": "Railway Department - Sierra Leone", "honors": ["O.B.E.", "M.C."], "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280},
    {"name": "R. Lane", "canonical_name": "Lane, R.", "given_names": "R.", "surname": "Lane", "position": "Assistant to General Manager", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "M. W. B. Wright", "canonical_name": "Wright, M. W. B.", "given_names": "M. W. B.", "surname": "Wright", "position": "Principal Clerk, Management Branch", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "W. A. FitzJohn", "canonical_name": "FitzJohn, W. A.", "given_names": "W. A.", "surname": "FitzJohn", "position": "First Grade Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. C. Metzger", "canonical_name": "Metzger, J. C.", "given_names": "J. C.", "surname": "Metzger", "position": "First Grade Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 960, "duty_allowance": 96},
    {"name": "A. R. Homan", "canonical_name": "Homan, A. R.", "given_names": "A. R.", "surname": "Homan", "position": "Assistant Engineers", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. M. M. Whellens", "canonical_name": "Whellens, J. M. M.", "given_names": "J. M. M.", "surname": "Whellens", "position": "Assistant Engineers", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. Woodburn", "canonical_name": "Woodburn, A.", "given_names": "A.", "surname": "Woodburn", "position": "Assistant Engineers", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "J. Ronaldson", "canonical_name": "Ronaldson, J.", "given_names": "J.", "surname": "Ronaldson", "position": "Assistant Engineers", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "G. Cresswell", "canonical_name": "Cresswell, G.", "given_names": "G.", "surname": "Cresswell", "position": "Telegraph Engineer", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "R. Malthus", "canonical_name": "Malthus, R.", "given_names": "R.", "surname": "Malthus", "position": "Chief Mechanical Engineer", "department": "Railway Department - Sierra Leone", "qualifications": ["A.M.I.M.E."], "salary_min": 960, "allowances": "50l. p.a.", "duty_allowance": 96},
    {"name": "E. H. Wainwright", "canonical_name": "Wainwright, E. H.", "given_names": "E. H.", "surname": "Wainwright", "position": "Assistant Locomotive Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "T. Delmore", "canonical_name": "Delmore, T.", "given_names": "T.", "surname": "Delmore", "position": "Assistant Locomotive Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "C"},
    {"name": "F. E. M. Bentley", "canonical_name": "Bentley, F. E. M.", "given_names": "F. E. M.", "surname": "Bentley", "position": "Deputy Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 900, "allowances": "50l. p.a."},
    {"name": "A. Hides", "canonical_name": "Hides, A.", "given_names": "A.", "surname": "Hides", "position": "Assistant Traffic Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "V. Dunglinson", "canonical_name": "Dunglinson, V.", "given_names": "V.", "surname": "Dunglinson", "position": "Assistant Traffic Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hamilton", "canonical_name": "Hamilton, J.", "given_names": "J.", "surname": "Hamilton", "position": "Assistant Traffic Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "W. H. Salkield", "canonical_name": "Salkield, W. H.", "given_names": "W. H.", "surname": "Salkield", "position": "Assistant Traffic Superintendents", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "H. C. F. Fisher", "canonical_name": "Fisher, H. C. F.", "given_names": "H. C. F.", "surname": "Fisher", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 960, "duty_allowance": 96},
    {"name": "J. Hunter", "canonical_name": "Hunter, J.", "given_names": "J.", "surname": "Hunter", "position": "Assistant Accountants, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_min": 600, "salary_max": 800},
    {"name": "R. J. Dickinson", "canonical_name": "Dickinson, R. J.", "given_names": "R. J.", "surname": "Dickinson", "position": "Assistant Accountants, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "A. C. Blanchfield", "canonical_name": "Blanchfield, A. C.", "given_names": "A. C.", "surname": "Blanchfield", "position": "Chief Storekeeper", "department": "Railway Department - Sierra Leone", "salary_min": 800, "duty_allowance": 72},
    {"name": "C. W. Adamson", "canonical_name": "Adamson, C. W.", "given_names": "C. W.", "surname": "Adamson", "position": "Assistant Chief Storekeeper", "department": "Railway Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. C. Hamilton", "canonical_name": "Hamilton, J. C.", "given_names": "J. C.", "surname": "Hamilton", "position": "Staff Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "S. G. Thompson", "canonical_name": "Thompson, S. G.", "given_names": "S. G.", "surname": "Thompson", "position": "Chief Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "E. Thomas", "canonical_name": "Thomas, E.", "given_names": "E.", "surname": "Thomas", "position": "Chief Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. J. Aubee", "canonical_name": "Aubee, M. J.", "given_names": "M. J.", "surname": "Aubee", "position": "Chief Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "H. R. Pratt", "canonical_name": "Pratt, H. R.", "given_names": "H. R.", "surname": "Pratt", "position": "Chief Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "E. E. Wilson", "canonical_name": "Wilson, E. E.", "given_names": "E. E.", "surname": "Wilson", "position": "Chief Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "T. E. Stanley", "canonical_name": "Stanley, T. E.", "given_names": "T. E.", "surname": "Stanley", "position": "First Grade Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "T. N. Pratt", "canonical_name": "Pratt, T. N.", "given_names": "T. N.", "surname": "Pratt", "position": "First Grade Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "G. C. Williams", "canonical_name": "Williams, G. C.", "given_names": "G. C.", "surname": "Williams", "position": "First Grade Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "S. J. C. Johnson", "canonical_name": "Johnson, S. J. C.", "given_names": "S. J. C.", "surname": "Johnson", "position": "First Grade Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "C. B. Johnson", "canonical_name": "Johnson, C. B.", "given_names": "C. B.", "surname": "Johnson", "position": "First Grade Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. A. Thomas", "canonical_name": "Thomas, J. A.", "given_names": "J. A.", "surname": "Thomas", "position": "First Grade Clerks", "department": "Railway Department - Sierra Leone", "salary_min": 210, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()