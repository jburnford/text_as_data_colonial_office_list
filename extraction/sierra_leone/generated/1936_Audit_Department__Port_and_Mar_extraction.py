"""
Sierra Leone Colonial Office List 1936 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1936

OFFICIALS = [
    {"name": "J. D. M. Bourne", "canonical_name": "Bourne, J. D. M.", "given_names": "J. D. M.", "surname": "Bourne", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "A. G. Bowring", "canonical_name": "Bowring, A. G.", "given_names": "A. G.", "surname": "Bowring", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A", "military_rank": "Captain"},
    {"name": "C. W. Hodges", "canonical_name": "Hodges, C. W.", "given_names": "C. W.", "surname": "Hodges", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. L. Wikner", "canonical_name": "Wikner, R. L.", "given_names": "R. L.", "surname": "Wikner", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_scale": "C", "honors": ["D.S.C."]},
    {"name": "H. Bowles", "canonical_name": "Bowles, H.", "given_names": "H.", "surname": "Bowles", "position": "Government Pilot", "department": "Port and Marine Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "E. S. George", "canonical_name": "George, E. S.", "given_names": "E. S.", "surname": "George", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 204, "salary_max": 372},
    {"name": "A. F. C. Webber", "canonical_name": "Webber, A. F. C.", "given_names": "A. F. C.", "surname": "Webber", "position": "Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 320},
    {"name": "E. J. Macquarrie", "canonical_name": "Macquarrie, E. J.", "given_names": "E. J.", "surname": "Macquarrie", "position": "Puisne Judge", "department": "Judicial - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "B. A. K. McRoberts", "canonical_name": "McRoberts, B. A. K.", "given_names": "B. A. K.", "surname": "McRoberts", "position": "Police Magistrate, Coroner and Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "A. Alhadi", "canonical_name": "Alhadi, A.", "given_names": "A.", "surname": "Alhadi", "position": "Master and Registrar, Supreme Court", "department": "Judicial - Sierra Leone", "salary_min": 360, "salary_max": 500}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()