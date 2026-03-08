"""
Sierra Leone Colonial Office List 1928 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1928

OFFICIALS = [
    {"name": "R. L. Wikner", "canonical_name": "Wikner, R. L.", "given_names": "R. L.", "surname": "Wikner", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_scale": "C", "military_rank": "Lieut.", "honors": ["D.S.C."]},
    {"name": "T. M. Johnson", "canonical_name": "Johnson, T. M.", "given_names": "T. M.", "surname": "Johnson", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. E. Adams", "canonical_name": "Adams, A. E.", "given_names": "A. E.", "surname": "Adams", "position": "Government Pilot", "department": "Port and Marine Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "G. K. T. Purcell", "canonical_name": "Purcell, G. K. T.", "given_names": "G. K. T.", "surname": "Purcell", "position": "Chief Justice", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 300, "honors": ["Kt."]},
    {"name": "W. B. Lloyd", "canonical_name": "Lloyd, W. B.", "given_names": "W. B.", "surname": "Lloyd", "position": "Puisne and Circuit Judge", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "A. C.V. Prior", "canonical_name": "Prior, A. C.V.", "given_names": "A. C.V.", "surname": "Prior", "position": "Attorney-General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Solicitor-General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "B. A. K. McRoberts", "canonical_name": "McRoberts, B. A. K.", "given_names": "B. A. K.", "surname": "McRoberts", "position": "Police Magistrate", "department": "Judicial and Legal - Sierra Leone", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Master and Registrar General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "L. E. C. Evans", "canonical_name": "Evans, L. E. C.", "given_names": "L. E. C.", "surname": "Evans", "position": "Senior Crown Counsel", "department": "Judicial and Legal - Sierra Leone", "salary_min": 600, "salary_max": 960, "allowances": "72l. seniority pay"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Junior Crown Counsel", "department": "Judicial and Legal - Sierra Leone", "salary_scale": "B"},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Police Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "F. B. E. McEwen", "canonical_name": "McEwen, F. B. E.", "given_names": "F. B. E.", "surname": "McEwen", "position": "Assistant Master, Circuit Court", "department": "Judicial and Legal - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. N. P. Nicol", "canonical_name": "Nicol, J. N. P.", "given_names": "J. N. P.", "surname": "Nicol", "position": "First Grade Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 210, "salary_max": 250},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()