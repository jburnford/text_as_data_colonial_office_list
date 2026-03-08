"""
Sierra Leone Colonial Office List 1927 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1927

OFFICIALS = [
    {"name": "Sir G. K. T. Purcell", "canonical_name": "Purcell, G. K. T.", "given_names": "G. K. T.", "surname": "Purcell", "position": "Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 300, "honors": ["Kt."]},
    {"name": "W. B. Lloyd", "canonical_name": "Lloyd, W. B.", "given_names": "W. B.", "surname": "Lloyd", "position": "Puisne and Circuit Judge", "department": "Judicial - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Attorney-General", "department": "Judicial - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "I. J. T. Turbett", "canonical_name": "Turbett, I. J. T.", "given_names": "I. J. T.", "surname": "Turbett", "position": "Solicitor-General", "department": "Judicial - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "Mr. B. A. K. McRoberts", "canonical_name": "McRoberts, B. A. K.", "given_names": "B. A. K.", "surname": "McRoberts", "position": "Police Magistrate", "department": "Judicial - Sierra Leone", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Master and Registrar General", "department": "Judicial - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "J. de Hart", "canonical_name": "Hart, J. de", "given_names": "J.", "surname": "Hart", "position": "Senior Crown Counsel", "department": "Judicial - Sierra Leone", "salary_min": 600, "salary_max": 960, "allowances": "72l. seniority pay"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Junior Crown Counsel", "department": "Judicial - Sierra Leone", "salary_scale": "B"},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Police Clerk", "department": "Judicial - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "F. B. E. McEwen", "canonical_name": "McEwen, F. B. E.", "given_names": "F. B. E.", "surname": "McEwen", "position": "Assistant Master, Circuit Court", "department": "Judicial - Sierra Leone", "salary_min": 210, "salary_max": 260},
    {"name": "J. N. P. Nicol", "canonical_name": "Nicol, J. N. P.", "given_names": "J. N. P.", "surname": "Nicol", "position": "First Grade Clerk", "department": "Judicial - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "Major C. H. King", "canonical_name": "King, C. H.", "given_names": "C. H.", "surname": "King", "position": "Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "military_rank": "Major"},
    {"name": "Capt. P. T. Brodie", "canonical_name": "Brodie, P. T.", "given_names": "P. T.", "surname": "Brodie", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A", "honors": ["D.S.O.", "M.C."], "military_rank": "Captain"},
    {"name": "J. Rabbitt", "canonical_name": "Rabbitt, J.", "given_names": "J.", "surname": "Rabbitt", "position": "Chief Inspector", "department": "Civil Police - Sierra Leone", "salary_min": 450, "salary_max": 510}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()