"""
Sierra Leone Colonial Office List 1934 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1934

OFFICIALS = [
    {"name": "F. J. Martin", "canonical_name": "Martin, F. J.", "given_names": "F. J.", "surname": "Martin", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210, "qualifications": ["Ph.D.", "F.I.C."]},
    {"name": "E. Hargreaves", "canonical_name": "Hargreaves, E.", "given_names": "E.", "surname": "Hargreaves", "position": "Entomologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l. seniority allowance", "qualifications": ["A.R.C.S.", "F.E.S."]},
    {"name": "F. C. Deighton", "canonical_name": "Deighton, F. C.", "given_names": "F. C.", "surname": "Deighton", "position": "Mycologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "J. W. D. Fisher", "canonical_name": "Fisher, J. W. D.", "given_names": "J. W. D.", "surname": "Fisher", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C", "military_rank": "Captain"},
    {"name": "R. Glanville", "canonical_name": "Glanville, R.", "given_names": "R.", "surname": "Glanville", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. I. Nisbett", "canonical_name": "Nisbett, E. I.", "given_names": "E. I.", "surname": "Nisbett", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "G. M. Roddan", "canonical_name": "Roddan, G. M.", "given_names": "G. M.", "surname": "Roddan", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. S. Garner", "canonical_name": "Garner, E. S.", "given_names": "E. S.", "surname": "Garner", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "F. W. B. Allinson", "canonical_name": "Allinson, F. W. B.", "given_names": "F. W. B.", "surname": "Allinson", "position": "Assistant Inspector of Plants and Produce", "department": "Agricultural Department - Sierra Leone", "salary_min": 400, "salary_max": 690},
    {"name": "E. MacDonald", "canonical_name": "MacDonald, E.", "given_names": "E.", "surname": "MacDonald", "position": "Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "honors": ["M.C."]},
    {"name": "D. G. Thomas", "canonical_name": "Thomas, D. G.", "given_names": "D. G.", "surname": "Thomas", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C", "qualifications": ["B.Sc."]},
    {"name": "C. V. Wallace", "canonical_name": "Wallace, C. V.", "given_names": "C. V.", "surname": "Wallace", "position": "Assistant Conservator of Forests", "department": "Forests Department - Sierra Leone", "salary_scale": "C"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()