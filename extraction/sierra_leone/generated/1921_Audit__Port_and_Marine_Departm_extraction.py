"""
Sierra Leone Colonial Office List 1921 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1921

OFFICIALS = [
    {"name": "B. E. Hanson", "canonical_name": "Hanson, B. E.", "given_names": "B. E.", "surname": "Hanson", "position": "Auditor", "department": "Audit - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "N. H. Turton", "canonical_name": "Turton, N. H.", "given_names": "N. H.", "surname": "Turton", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 450, "salary_max": 920},
    {"name": "R. F. Pindar", "canonical_name": "Pindar, R. F.", "given_names": "R. F.", "surname": "Pindar", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 450, "salary_max": 920},
    {"name": "H. V. Cusack", "canonical_name": "Cusack, H. V.", "given_names": "H. V.", "surname": "Cusack", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 450, "salary_max": 920, "military_rank": "Captain"},
    {"name": "T. M. Johnson", "canonical_name": "Johnson, T. M.", "given_names": "T. M.", "surname": "Johnson", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "G. K. T. Purcell", "canonical_name": "Purcell, G. K. T.", "given_names": "G. K. T.", "surname": "Purcell", "position": "Chief Justice", "department": "Legal Department - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 300, "honors": ["Kt."]},
    {"name": "E. V. Parodi", "canonical_name": "Parodi, E. V.", "given_names": "E. V.", "surname": "Parodi", "position": "Puisne and Circuit Judge", "department": "Legal Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "M. F. J. McDonnell", "canonical_name": "McDonnell, M. F. J.", "given_names": "M. F. J.", "surname": "McDonnell", "position": "Attorney-General", "department": "Legal Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "A. C. V. Prior", "canonical_name": "Prior, A. C. V.", "given_names": "A. C. V.", "surname": "Prior", "position": "Solicitor-General", "department": "Legal Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "K. J. Beatty", "canonical_name": "Beatty, K. J.", "given_names": "K. J.", "surname": "Beatty", "position": "Police Magistrate", "department": "Legal Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Chief Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Police Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "M. J. O. Macauley", "canonical_name": "Macauley, M. J. O.", "given_names": "M. J. O.", "surname": "Macauley", "position": "Assistant Master, Circuit Court", "department": "Legal Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "J. N. P. Nicol", "canonical_name": "Nicol, J. N. P.", "given_names": "J. N. P.", "surname": "Nicol", "position": "First Grade Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()