"""
Sierra Leone Colonial Office List 1922 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1922

OFFICIALS = [
    {"name": "A. P. Viret", "canonical_name": "Viret, A. P.", "given_names": "A. P.", "surname": "Viret", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "A. S. Fraser", "canonical_name": "Fraser, A. S.", "given_names": "A. S.", "surname": "Fraser", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 450, "salary_max": 920},
    {"name": "R. B. Mackie", "canonical_name": "Mackie, R. B.", "given_names": "R. B.", "surname": "Mackie", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_min": 450, "salary_max": 920},
    {"name": "L. F. Campbell", "canonical_name": "Campbell, L. F.", "given_names": "L. F.", "surname": "Campbell", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Sherbro", "salary_min": 400, "salary_max": 450},
    {"name": "A. C. A. Johnson", "canonical_name": "Johnson, A. C. A.", "given_names": "A. C. A.", "surname": "Johnson", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "P. H. H. George", "canonical_name": "George, P. H. H.", "given_names": "P. H. H.", "surname": "George", "position": "Senior Outdoor Officer", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "T. A. Clemens", "canonical_name": "Clemens, T. A.", "given_names": "T. A.", "surname": "Clemens", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "M. A. Lewis", "canonical_name": "Lewis, M. A.", "given_names": "M. A.", "surname": "Lewis", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "A. R. Harris", "canonical_name": "Harris, A. R.", "given_names": "A. R.", "surname": "Harris", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Auditor", "department": "Audit - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "N. H. Turton", "canonical_name": "Turton, N. H.", "given_names": "N. H.", "surname": "Turton", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 450, "salary_max": 920},
    {"name": "R. F. Pindar", "canonical_name": "Pindar, R. F.", "given_names": "R. F.", "surname": "Pindar", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 450, "salary_max": 920},
    {"name": "H. V. Cusack", "canonical_name": "Cusack, H. V.", "given_names": "H. V.", "surname": "Cusack", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 450, "salary_max": 920, "military_rank": "Captain"},
    {"name": "R. L. Wikner", "canonical_name": "Wikner, R. L.", "given_names": "R. L.", "surname": "Wikner", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 480, "salary_max": 920, "military_rank": "Lieutenant", "honors": ["D.S.C."]},
    {"name": "T. M. Johnson", "canonical_name": "Johnson, T. M.", "given_names": "T. M.", "surname": "Johnson", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 252, "salary_max": 372}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()