"""
Sierra Leone Colonial Office List 1924 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1924

OFFICIALS = [
    {"name": "J. I. Lauder", "canonical_name": "Lauder, J. I.", "given_names": "J. I.", "surname": "Lauder", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "R. B. Mackie", "canonical_name": "Mackie, R. B.", "given_names": "R. B.", "surname": "Mackie", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A"},
    {"name": "L. F. Campbell", "canonical_name": "Campbell, L. F.", "given_names": "L. F.", "surname": "Campbell", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Sherbro", "salary_min": 400, "salary_max": 450},
    {"name": "A. C. A. Johnson", "canonical_name": "Johnson, A. C. A.", "given_names": "A. C. A.", "surname": "Johnson", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_min": 400, "salary_max": 450},
    {"name": "P. H. H. George", "canonical_name": "George, P. H. H.", "given_names": "P. H. H.", "surname": "George", "position": "Senior Outdoor Officer", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "T. A. Clemens", "canonical_name": "Clemens, T. A.", "given_names": "T. A.", "surname": "Clemens", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. A. Lewis", "canonical_name": "Lewis, M. A.", "given_names": "M. A.", "surname": "Lewis", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. R. Harris", "canonical_name": "Harris, A. R.", "given_names": "A. R.", "surname": "Harris", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "W. M. Peeler", "canonical_name": "Peeler, W. M.", "given_names": "W. M.", "surname": "Peeler", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "E. H. Morris", "canonical_name": "Morris, E. H.", "given_names": "E. H.", "surname": "Morris", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "R. F. Pinder", "canonical_name": "Pinder, R. F.", "given_names": "R. F.", "surname": "Pinder", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. S. Foster", "canonical_name": "Foster, R. S.", "given_names": "R. S.", "surname": "Foster", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()