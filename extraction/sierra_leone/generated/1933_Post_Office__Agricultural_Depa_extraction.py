"""
Sierra Leone Colonial Office List 1933 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1933

OFFICIALS = [
    {"name": "N. S. Davis", "canonical_name": "Davis, N. S.", "given_names": "N. S.", "surname": "Davis", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "C. B. Plenderleith", "canonical_name": "Plenderleith, C. B.", "given_names": "C. B.", "surname": "Plenderleith", "position": "Deputy Postmaster General", "department": "Post Office - Sierra Leone", "salary_scale": "A", "qualifications": ["D.C.M."]},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Assistant Postmaster General and Accountant", "department": "Post Office - Sierra Leone", "salary_min": 360, "salary_max": 600},
    {"name": "A. H. Kirby", "canonical_name": "Kirby, A. H.", "given_names": "A. H.", "surname": "Kirby", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "honors": ["O.B.E."]},
    {"name": "F. J. Martin", "canonical_name": "Martin, F. J.", "given_names": "F. J.", "surname": "Martin", "position": "Assistant Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["Ph.D.", "F.I.C."]},
    {"name": "E. Hargreaves", "canonical_name": "Hargreaves, E.", "given_names": "E.", "surname": "Hargreaves", "position": "Entomologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l. seniority allowance", "qualifications": ["A.R.C.S.", "F.E.S."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Agricultural Chemist", "department": "Agricultural Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "F. C. Deighton", "canonical_name": "Deighton, F. C.", "given_names": "F. C.", "surname": "Deighton", "position": "Mycologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "J. W. D. Fisher", "canonical_name": "Fisher, J. W. D.", "given_names": "J. W. D.", "surname": "Fisher", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C", "military_rank": "Captain"},
    {"name": "R. R. Glanville", "canonical_name": "Glanville, R. R.", "given_names": "R. R.", "surname": "Glanville", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. I. Nisbett", "canonical_name": "Nisbett, E. I.", "given_names": "E. I.", "surname": "Nisbett", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "P. J. Moss", "canonical_name": "Moss, P. J.", "given_names": "P. J.", "surname": "Moss", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "G. M. Roddan", "canonical_name": "Roddan, G. M.", "given_names": "G. M.", "surname": "Roddan", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. S. Garner", "canonical_name": "Garner, E. S.", "given_names": "E. S.", "surname": "Garner", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "F. W. B. Allinson", "canonical_name": "Allinson, F. W. B.", "given_names": "F. W. B.", "surname": "Allinson", "position": "Assistant Inspector of Plants and Produce", "department": "Agricultural Department - Sierra Leone", "salary_min": 400, "salary_max": 690},
    {"name": "E. MacDonald", "canonical_name": "MacDonald, E.", "given_names": "E.", "surname": "MacDonald", "position": "Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "military_rank": "M.C."},
    {"name": "D. G. Thomas", "canonical_name": "Thomas, D. G.", "given_names": "D. G.", "surname": "Thomas", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C", "qualifications": ["B.Sc."]},
    {"name": "A. Burns", "canonical_name": "Burns, A.", "given_names": "A.", "surname": "Burns", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C", "qualifications": ["B.Sc."]},
    {"name": "C. V. Wallace", "canonical_name": "Wallace, C. V.", "given_names": "C. V.", "surname": "Wallace", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()