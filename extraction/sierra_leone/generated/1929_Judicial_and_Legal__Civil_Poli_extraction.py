"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "Sir G. K. T. Purcell", "canonical_name": "Purcell, G. K. T.", "given_names": "G. K. T.", "surname": "Purcell", "position": "Chief Justice", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 300, "honors": ["Kt."]},
    {"name": "W. B. Lloyd", "canonical_name": "Lloyd, W. B.", "given_names": "W. B.", "surname": "Lloyd", "position": "Puisne and Circuit Judge", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "A. C. V. Prior", "canonical_name": "Prior, A. C. V.", "given_names": "A. C. V.", "surname": "Prior", "position": "Attorney-General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "L. J. T. Turbett", "canonical_name": "Turbett, L. J. T.", "given_names": "L. J. T.", "surname": "Turbett", "position": "Solicitor-General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "Mr. B. A. K. McRoberts", "canonical_name": "McRoberts, B. A. K.", "given_names": "B. A. K.", "surname": "McRoberts", "position": "Police Magistrate", "department": "Judicial and Legal - Sierra Leone", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Master and Registrar General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "L. E. C. Evans", "canonical_name": "Evans, L. E. C.", "given_names": "L. E. C.", "surname": "Evans", "position": "Senior Crown Counsel", "department": "Judicial and Legal - Sierra Leone", "salary_min": 600, "salary_max": 840, "allowances": "72l. seniority pay"},
    {"name": "A. A. Cromie", "canonical_name": "Cromie, A. A.", "given_names": "A. A.", "surname": "Cromie", "position": "Junior Crown Counsel", "department": "Judicial and Legal - Sierra Leone", "salary_min": 600, "salary_max": 840, "allowances": "72l. seniority pay"},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Police Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "F. B. E. McEwen", "canonical_name": "McEwen, F. B. E.", "given_names": "F. B. E.", "surname": "McEwen", "position": "Assistant Master, Circuit Court", "department": "Judicial and Legal - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. N. P. Nicol", "canonical_name": "Nicol, J. N. P.", "given_names": "J. N. P.", "surname": "Nicol", "position": "First Grade Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "C. H. King", "canonical_name": "King, C. H.", "given_names": "C. H.", "surname": "King", "position": "Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "military_rank": "Major"},
    {"name": "P. T. Brodie", "canonical_name": "Brodie, P. T.", "given_names": "P. T.", "surname": "Brodie", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "honors": ["D.S.O.", "M.C."], "salary_scale": "A", "military_rank": "Capt."},
    {"name": "J. Rabbitt", "canonical_name": "Rabbitt, J.", "given_names": "J.", "surname": "Rabbitt", "position": "Chief Inspector", "department": "Civil Police - Sierra Leone", "salary_min": 450, "salary_max": 720},
    {"name": "R. J. Craig", "canonical_name": "Craig, R. J.", "given_names": "R. J.", "surname": "Craig", "position": "Senior Inspector", "department": "Civil Police - Sierra Leone", "salary_min": 600, "salary_max": 720, "honors": ["M.C."], "military_rank": "Capt."},
    {"name": "B. Lovett", "canonical_name": "Lovett, B.", "given_names": "B.", "surname": "Lovett", "position": "Inspectors", "department": "Civil Police - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "V. Warren", "canonical_name": "Warren, V.", "given_names": "V.", "surname": "Warren", "position": "Inspectors", "department": "Civil Police - Sierra Leone", "salary_min": 400, "salary_max": 500}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()