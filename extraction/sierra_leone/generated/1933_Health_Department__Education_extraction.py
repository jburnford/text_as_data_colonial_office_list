"""
Sierra Leone Colonial Office List 1933 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1933

OFFICIALS = [
    {"name": "J. A. A. Duncan", "canonical_name": "Duncan, J. A. A.", "given_names": "J. A. A.", "surname": "Duncan", "position": "Assistant Director, Health Service", "department": "Health Department - Sierra Leone", "salary_min": 1300, "salary_max": 1300, "duty_allowance": 260, "qualifications": ["M.C."]},
    {"name": "A. B. Monks", "canonical_name": "Monks, A. B.", "given_names": "A. B.", "surname": "Monks", "position": "Senior Health Officer", "department": "Health Department - Sierra Leone", "salary_min": 1050, "salary_max": 1200, "duty_allowance": 210},
    {"name": "G. V. Herd", "canonical_name": "Herd, G. V.", "given_names": "G. V.", "surname": "Herd", "position": "Sanitary Superintendent and Training Officer", "department": "Health Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "H. Blackmore", "canonical_name": "Blackmore, H.", "given_names": "H.", "surname": "Blackmore", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "honors": ["O.B.E.", "V.D."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Deputy Director of Education and Chief Inspector of Schools", "department": "Education - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "W. J. Davies", "canonical_name": "Davies, W. J.", "given_names": "W. J.", "surname": "Davies", "position": "Principal, Prince of Wales' School", "department": "Education - Sierra Leone"},
    {"name": "H. E. T. Hodgson", "canonical_name": "Hodgson, H. E. T.", "given_names": "H. E. T.", "surname": "Hodgson", "position": "Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 800, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "O. P. Ellis", "canonical_name": "Ellis, O. P.", "given_names": "O. P.", "surname": "Ellis", "position": "Vice-Principal", "department": "Education - Sierra Leone", "salary_scale": "C"},
    {"name": "F. A. Lacey", "canonical_name": "Lacey, F. A.", "given_names": "F. A.", "surname": "Lacey", "position": "Principal, Protectorate Central College", "department": "Education - Sierra Leone"},
    {"name": "H. O. Lipcoombe", "canonical_name": "Lipcoombe, H. O.", "given_names": "H. O.", "surname": "Lipcoombe", "position": "Supervisor of Schools", "department": "Education - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "Miss K. B. Coope", "canonical_name": "Coope, K. B.", "given_names": "K. B.", "surname": "Coope", "position": "Supervisor of Infant and Female Education", "department": "Education - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "C. A. E. Macaulay", "canonical_name": "Macaulay, C. A. E.", "given_names": "C. A. E.", "surname": "Macaulay", "position": "African Assistant Director of Education", "department": "Education - Sierra Leone", "salary_min": 360, "salary_max": 500, "honors": ["M.B.E."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()