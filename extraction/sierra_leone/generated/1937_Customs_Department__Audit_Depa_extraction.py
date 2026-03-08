"""
Sierra Leone Colonial Office List 1937 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1937

OFFICIALS = [
    {"name": "W. H. Eccles", "canonical_name": "Eccles, W. H.", "given_names": "W. H.", "surname": "Eccles", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1650, "salary_max": 1650, "duty_allowance": 210},
    {"name": "W. T. Martin", "canonical_name": "Martin, W. T.", "given_names": "W. T.", "surname": "Martin", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A", "salary_min": 600},
    {"name": "F. A. von Weiller", "canonical_name": "Weiller, F. A. von", "given_names": "F. A.", "surname": "Weiller", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A"},
    {"name": "F. C. Campbell", "canonical_name": "Campbell, F. C.", "given_names": "F. C.", "surname": "Campbell", "position": "Supervisors", "department": "Customs Department - Sierra Leone", "salary_min": 300, "salary_max": 600},
    {"name": "S. E. Cole", "canonical_name": "Cole, S. E.", "given_names": "S. E.", "surname": "Cole", "position": "Supervisors", "department": "Customs Department - Sierra Leone", "salary_min": 300, "salary_max": 600},
    {"name": "W. A. P. Buck", "canonical_name": "Buck, W. A. P.", "given_names": "W. A. P.", "surname": "Buck", "position": "Staff Superintendent", "department": "Customs Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "J. D. M. Bourne", "canonical_name": "Bourne, J. D. M.", "given_names": "J. D. M.", "surname": "Bourne", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "A. G. Bowring", "canonical_name": "Bowring, A. G.", "given_names": "A. G.", "surname": "Bowring", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_scale": "A", "military_rank": "Captain"},
    {"name": "C. W. Hodges", "canonical_name": "Hodges, C. W.", "given_names": "C. W.", "surname": "Hodges", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. T. Spencer", "canonical_name": "Spencer, R. T.", "given_names": "R. T.", "surname": "Spencer", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. L. Wikner", "canonical_name": "Wikner, R. L.", "given_names": "R. L.", "surname": "Wikner", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_scale": "C", "honors": ["D.S.C."]},
    {"name": "H. Bowles", "canonical_name": "Bowles, H.", "given_names": "H.", "surname": "Bowles", "position": "Government Pilot", "department": "Port and Marine Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "S. G. Randall", "canonical_name": "Randall, S. G.", "given_names": "S. G.", "surname": "Randall", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. F. C. Webber", "canonical_name": "Webber, A. F. C.", "given_names": "A. F. C.", "surname": "Webber", "position": "Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 1800, "salary_max": 1800, "duty_allowance": 320, "honors": ["Kt."]},
    {"name": "E. J. Macquarrie", "canonical_name": "Macquarrie, E. J.", "given_names": "E. J.", "surname": "Macquarrie", "position": "Puisne Judge", "department": "Judicial - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "B. A. K. McRoberts", "canonical_name": "McRoberts, B. A. K.", "given_names": "B. A. K.", "surname": "McRoberts", "position": "Police Magistrate, Coroner and Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "A. Alhadi", "canonical_name": "Alhadi, A.", "given_names": "A.", "surname": "Alhadi", "position": "Master and Registrar, Supreme Court", "department": "Judicial - Sierra Leone", "salary_min": 360, "salary_max": 600, "honors": ["M.B.E."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()