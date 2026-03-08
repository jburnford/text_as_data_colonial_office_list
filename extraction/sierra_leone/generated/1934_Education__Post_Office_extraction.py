"""
Sierra Leone Colonial Office List 1934 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1934

OFFICIALS = [
    {"name": "H. Blackmore", "canonical_name": "Blackmore, H.", "given_names": "H.", "surname": "Blackmore", "position": "Director of Education", "department": "Education - Sierra Leone", "honors": ["O.B.E.", "V.D."], "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "W. J. Davies", "canonical_name": "Davies, W. J.", "given_names": "W. J.", "surname": "Davies", "position": "Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 540, "salary_max": 920},
    {"name": "H. E. T. Hodgson", "canonical_name": "Hodgson, H. E. T.", "given_names": "H. E. T.", "surname": "Hodgson", "position": "Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "C. P. Ellis", "canonical_name": "Ellis, C. P.", "given_names": "C. P.", "surname": "Ellis", "position": "Vice-Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Muster, Bo School", "department": "Education - Sierra Leone"},
    {"name": "Headmaster", "canonical_name": "Headmaster, ", "surname": "Headmaster", "position": "Headmaster, Koyeima", "department": "Education - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "H. O. Lipscombe", "canonical_name": "Lipscombe, H. O.", "given_names": "H. O.", "surname": "Lipscombe", "position": "Supervisor of Schools", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "Miss K. B. Coope", "canonical_name": "Coope, K. B.", "given_names": "K. B.", "surname": "Coope", "position": "Supervisor of Infant and Female Education", "department": "Education - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "C. A. E. Macaulay", "canonical_name": "Macaulay, C. A. E.", "given_names": "C. A. E.", "surname": "Macaulay", "position": "African Assistant Director of Education", "department": "Education - Sierra Leone", "honors": ["M.B.E."], "salary_min": 360, "salary_max": 600},
    {"name": "N. S. Davis", "canonical_name": "Davis, N. S.", "given_names": "N. S.", "surname": "Davis", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Assistant Postmaster General and Accountant", "department": "Post Office - Sierra Leone", "salary_min": 360, "salary_max": 600}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()