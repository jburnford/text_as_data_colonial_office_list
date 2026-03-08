"""
Sierra Leone Colonial Office List 1936 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1936

OFFICIALS = [
    {"name": "J. A. A. Duncan", "canonical_name": "Duncan, J. A. A.", "given_names": "J. A. A.", "surname": "Duncan", "position": "Assistant Director, Medical Services", "department": "Health Department - Sierra Leone", "salary_min": 1300, "salary_max": 1300, "duty_allowance": 280, "honors": ["M.C."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Senior Health Officer", "department": "Health Department - Sierra Leone", "salary_min": 1050, "salary_max": 1200, "duty_allowance": 210},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Medical Officer (Health)", "department": "Health Department - Sierra Leone", "salary_min": 800, "salary_max": 960},
    {"name": "G. V. Herd", "canonical_name": "Herd, G. V.", "given_names": "G. V.", "surname": "Herd", "position": "Chief Sanitary Superintendent", "department": "Health Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "W. E. Nicholson", "canonical_name": "Nicholson, W. E.", "given_names": "W. E.", "surname": "Nicholson", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "W. J. Davies", "canonical_name": "Davies, W. J.", "given_names": "W. J.", "surname": "Davies", "position": "Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 540, "salary_max": 920},
    {"name": "H. E. T. Hodgson", "canonical_name": "Hodgson, H. E. T.", "given_names": "H. E. T.", "surname": "Hodgson", "position": "Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 720, "salary_max": 920},
    {"name": "C. P. Ellis", "canonical_name": "Ellis, C. P.", "given_names": "C. P.", "surname": "Ellis", "position": "Vice-Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_scale": "C", "salary_min": 480, "salary_max": 920},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Master, Bo School", "department": "Education - Sierra Leone"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Headmaster, Koycima", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Supervisor of Schools", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "Miss K. B. Coope", "canonical_name": "Coope, K. B.", "given_names": "K. B.", "surname": "Coope", "position": "Supervisor of Infant and Female Education", "department": "Education - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "C. A. E. Macaulay", "canonical_name": "Macaulay, C. A. E.", "given_names": "C. A. E.", "surname": "Macaulay", "position": "African Assistant Director of Education", "department": "Education - Sierra Leone", "salary_min": 360, "salary_max": 600, "honors": ["M.B.E."]},
    {"name": "C. B. Plenderleith", "canonical_name": "Plenderleith, C. B.", "given_names": "C. B.", "surname": "Plenderleith", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 920, "salary_max": 920, "duty_allowance": 92, "honors": ["D.C.M."]},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Assistant Postmaster General and Accountant", "department": "Post Office - Sierra Leone", "salary_min": 360, "salary_max": 600}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()