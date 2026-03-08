"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "M. L. Tew", "canonical_name": "Tew, M. L.", "given_names": "M. L.", "surname": "Tew", "position": "Chief Justice", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 300},
    {"name": "H. A. Young", "canonical_name": "Young, H. A.", "given_names": "H. A.", "surname": "Young", "position": "Puisne and Circuit Judge", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240, "honors": ["K.C."]},
    {"name": "J. Aitken", "canonical_name": "Aitken, J.", "given_names": "J.", "surname": "Aitken", "position": "Attorney-General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Solicitor-General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "B. A. K. McRoberts", "canonical_name": "McRoberts, B. A. K.", "given_names": "B. A. K.", "surname": "McRoberts", "position": "Police Magistrate", "department": "Judicial and Legal - Sierra Leone", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Master and Registrar General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "L. E. C. Evans", "canonical_name": "Evans, L. E. C.", "given_names": "L. E. C.", "surname": "Evans", "position": "Senior Crown Counsel", "department": "Judicial and Legal - Sierra Leone", "salary_min": 600, "salary_max": 840, "allowances": "72l. seniority pay"},
    {"name": "A. A. Cromie", "canonical_name": "Cromie, A. A.", "given_names": "A. A.", "surname": "Cromie", "position": "Junior Crown Counsel", "department": "Judicial and Legal - Sierra Leone", "salary_min": 600, "salary_max": 840, "allowances": "72l. seniority pay"},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Police Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "F. B. E. McEwen", "canonical_name": "McEwen, F. B. E.", "given_names": "F. B. E.", "surname": "McEwen", "position": "Assistant Master, Circuit Court", "department": "Judicial and Legal - Sierra Leone", "salary_min": 210, "salary_max": 250},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()