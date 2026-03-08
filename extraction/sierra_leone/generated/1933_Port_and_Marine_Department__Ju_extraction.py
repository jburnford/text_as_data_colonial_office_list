"""
Sierra Leone Colonial Office List 1933 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1933

OFFICIALS = [
    {"name": "R. L. Wikner", "canonical_name": "Wikner, R. L.", "given_names": "R. L.", "surname": "Wikner", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_scale": "C", "military_rank": "Lieut.", "honors": ["D.S.C."], "qualifications": ["R.N.R."]},
    {"name": "H. Bowles", "canonical_name": "Bowles, H.", "given_names": "H.", "surname": "Bowles", "position": "Government Pilot", "department": "Port and Marine Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "A. F. G. Taylor", "canonical_name": "Taylor, A. F. G.", "given_names": "A. F. G.", "surname": "Taylor", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. F. C. Webber", "canonical_name": "Webber, A. F. C.", "given_names": "A. F. C.", "surname": "Webber", "position": "Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 300},
    {"name": "E. J. Macquarrie", "canonical_name": "Macquarrie, E. J.", "given_names": "E. J.", "surname": "Macquarrie", "position": "Puisne Judge", "department": "Judicial - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "B. A. K. McRoberts", "canonical_name": "McRoberts, B. A. K.", "given_names": "B. A. K.", "surname": "McRoberts", "position": "Police Magistrate, Coroner and Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Master and Registrar, Supreme Court", "department": "Judicial - Sierra Leone", "salary_min": 360, "salary_max": 600, "honors": ["I.S.O."]},
    {"name": "J. Aitken", "canonical_name": "Aitken, J.", "given_names": "J.", "surname": "Aitken", "position": "Attorney-General", "department": "Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "L. J. T. Turbett", "canonical_name": "Turbett, L. J. T.", "given_names": "L. J. T.", "surname": "Turbett", "position": "Solicitor-General", "department": "Legal - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "L. E. C. Evans", "canonical_name": "Evans, L. E. C.", "given_names": "L. E. C.", "surname": "Evans", "position": "Senior Crown Counsel", "department": "Legal - Sierra Leone", "salary_min": 600, "salary_max": 840, "allowances": "72l. seniority allowance"},
    {"name": "A. A. Cromie", "canonical_name": "Cromie, A. A.", "given_names": "A. A.", "surname": "Cromie", "position": "Junior Crown Counsel", "department": "Legal - Sierra Leone", "salary_min": 600, "salary_max": 840, "allowances": "72l. seniority allowance"},
    {"name": "P. T. Brodie", "canonical_name": "Brodie, P. T.", "given_names": "P. T.", "surname": "Brodie", "position": "Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 920, "salary_max": 920, "duty_allowance": 92, "military_rank": "Capt.", "honors": ["D.S.O.", "M.C."]},
    {"name": "J. Rabbitt", "canonical_name": "Rabbitt, J.", "given_names": "J.", "surname": "Rabbitt", "position": "Assistant Commissioners of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A"},
    {"name": "R. J. Craig", "canonical_name": "Craig, R. J.", "given_names": "R. J.", "surname": "Craig", "position": "Assistant Commissioners of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A", "military_rank": "Capt.", "honors": ["M.C."]},
    {"name": "G. Tuach", "canonical_name": "Tuach, G.", "given_names": "G.", "surname": "Tuach", "position": "Assistant Commissioners of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()