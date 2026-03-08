"""
Sierra Leone Colonial Office List 1923 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1923

OFFICIALS = [
    {"name": "E. H. Morris", "canonical_name": "Morris, E. H.", "given_names": "E. H.", "surname": "Morris", "position": "Auditor", "department": "Audit - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "R. F. Pinder", "canonical_name": "Pinder, R. F.", "given_names": "R. F.", "surname": "Pinder", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 450, "salary_max": 920, "allowances": "72l. from 720l."},
    {"name": "R. S. Foster", "canonical_name": "Foster, R. S.", "given_names": "R. S.", "surname": "Foster", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 450, "salary_max": 920, "allowances": "72l. from 720l."},
    {"name": "R. L. Wikner", "canonical_name": "Wikner, R. L.", "given_names": "R. L.", "surname": "Wikner", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "military_rank": "Lieut.", "honors": ["D.S.C."], "qualifications": ["R.N.R."], "salary_min": 480, "salary_max": 920},
    {"name": "T. M. Johnson", "canonical_name": "Johnson, T. M.", "given_names": "T. M.", "surname": "Johnson", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "G. K. T. Purcell", "canonical_name": "Purcell, G. K. T.", "given_names": "G. K. T.", "surname": "Purcell", "position": "Chief Justice", "department": "Judicial and Legal - Sierra Leone", "honors": ["Kt."], "salary_min": 1600, "salary_max": 1600, "duty_allowance": 300},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Puisne and Circuit Judge", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "M. F. J. McDonnell", "canonical_name": "McDonnell, M. F. J.", "given_names": "M. F. J.", "surname": "McDonnell", "position": "Attorney-General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "A. C. V. Prior", "canonical_name": "Prior, A. C. V.", "given_names": "A. C. V.", "surname": "Prior", "position": "Solicitor-General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "W. Butler-Lloyd", "canonical_name": "Butler-Lloyd, W.", "given_names": "W.", "surname": "Butler-Lloyd", "position": "Police Magistrate", "department": "Judicial and Legal - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "J. F. St. A. Fawcett", "canonical_name": "Fawcett, J. F. St. A.", "given_names": "J. F. St. A.", "surname": "Fawcett", "position": "Master and Registrar General", "department": "Judicial and Legal - Sierra Leone", "salary_min": 600, "salary_max": 840},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Crown Prosecutor", "department": "Judicial and Legal - Sierra Leone"},
    {"name": "J. de Hart", "canonical_name": "Hart, J. de", "given_names": "J.", "surname": "Hart", "position": "Legal Assistant", "department": "Judicial and Legal - Sierra Leone", "salary_min": 720, "salary_max": 720},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Chief Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Police Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "F. B. E. A. McEwen", "canonical_name": "McEwen, F. B. E. A.", "given_names": "F. B. E. A.", "surname": "McEwen", "position": "Assistant Master, Circuit Court", "department": "Judicial and Legal - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "J. N. P. Nicol", "canonical_name": "Nicol, J. N. P.", "given_names": "J. N. P.", "surname": "Nicol", "position": "First Grade Clerk", "department": "Judicial and Legal - Sierra Leone", "salary_min": 190, "salary_max": 240}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()