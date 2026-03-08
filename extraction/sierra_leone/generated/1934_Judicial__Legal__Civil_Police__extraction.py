"""
Sierra Leone Colonial Office List 1934 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1934

OFFICIALS = [
    {"name": "A. F. C. Webber", "canonical_name": "Webber, A. F. C.", "given_names": "A. F. C.", "surname": "Webber", "position": "Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 300},
    {"name": "E. J. Macquarrie", "canonical_name": "Macquarrie, E. J.", "given_names": "E. J.", "surname": "Macquarrie", "position": "Puisne Judge", "department": "Judicial - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "B. A. K. McRoberts", "canonical_name": "McRoberts, B. A. K.", "given_names": "B. A. K.", "surname": "McRoberts", "position": "Police Magistrate, Coroner and Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Master and Registrar, Supreme Court", "department": "Judicial - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Attorney-General", "department": "Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Solicitor-General", "department": "Legal - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "L. E. C. Evans", "canonical_name": "Evans, L. E. C.", "given_names": "L. E. C.", "surname": "Evans", "position": "Senior Crown Counsel", "department": "Legal - Sierra Leone", "salary_min": 600, "salary_max": 840, "allowances": "72l. seniority allowance"},
    {"name": "A. A. Crombie", "canonical_name": "Crombie, A. A.", "given_names": "A. A.", "surname": "Crombie", "position": "Junior Crown Counsel", "department": "Legal - Sierra Leone", "salary_min": 600, "salary_max": 840, "allowances": "72l. seniority allowance"},
    {"name": "P. T. Brodie", "canonical_name": "Brodie, P. T.", "given_names": "P. T.", "surname": "Brodie", "position": "Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 920, "salary_max": 920, "duty_allowance": 92, "honors": ["D.S.O.", "M.C."], "military_rank": "Capt."},
    {"name": "J. Rabbitt", "canonical_name": "Rabbitt, J.", "given_names": "J.", "surname": "Rabbitt", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A", "salary_max": 720},
    {"name": "R. J. Craig", "canonical_name": "Craig, R. J.", "given_names": "R. J.", "surname": "Craig", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A", "salary_max": 720, "honors": ["M.C."], "military_rank": "Capt."},
    {"name": "G. Tunach", "canonical_name": "Tunach, G.", "given_names": "G.", "surname": "Tunach", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A", "salary_max": 720},
    {"name": "G. E. Biddle", "canonical_name": "Biddle, G. E.", "given_names": "G. E.", "surname": "Biddle", "position": "Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_scale": "A", "salary_max": 720, "honors": ["M.B.E."], "allowances": "72l. seniority allowance"},
    {"name": "A. Simmonds", "canonical_name": "Simmonds, A.", "given_names": "A.", "surname": "Simmonds", "position": "Asst. Superintendent of Prisons", "department": "Prisons - Sierra Leone"},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "African Asst. Keeper of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 310, "salary_max": 450}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()