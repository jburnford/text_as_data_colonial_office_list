"""
Sierra Leone Colonial Office List 1913 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1913

OFFICIALS = [
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Commissioner", "department": "Civil Police - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "allowances": "personal allowance 100l."},
    {"name": "I. Heslip", "canonical_name": "Heslip, I.", "given_names": "I.", "surname": "Heslip", "position": "Assistant Commissioner", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 400, "military_rank": "Capt."},
    {"name": "R. White", "canonical_name": "White, R.", "given_names": "R.", "surname": "White", "position": "Superintendent of Prisons", "department": "Prisons Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "N. H. Sawyerr", "canonical_name": "Sawyerr, N. H.", "given_names": "N. H.", "surname": "Sawyerr", "position": "Storekeeper", "department": "Prisons Department - Sierra Leone", "salary_min": 175, "salary_max": 200},
    {"name": "A. P. Viret", "canonical_name": "Viret, A. P.", "given_names": "A. P.", "surname": "Viret", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 600, "salary_max": 700, "duty_allowance": 120, "allowances": "100l. allowance in lieu of fees."},
    {"name": "A. S. Fraser", "canonical_name": "Fraser, A. S.", "given_names": "A. S.", "surname": "Fraser", "position": "Assistant ditto", "department": "Customs Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "allowances": "50l. allowance in lieu of fees."},
    {"name": "R. B. Mackie", "canonical_name": "Mackie, R. B.", "given_names": "R. B.", "surname": "Mackie", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_min": 300, "salary_max": 400},
    {"name": "L. F. Campbell", "canonical_name": "Campbell, L. F.", "given_names": "L. F.", "surname": "Campbell", "position": "Ditto", "department": "Customs Department - Sierra Leone", "location": "Sherbro", "salary_min": 300, "salary_max": 350},
    {"name": "A. C. A. Johnson", "canonical_name": "Johnson, A. C. A.", "given_names": "A. C. A.", "surname": "Johnson", "position": "Chief Clerk and Warehousekeeper", "department": "Customs Department - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "P. H. H. George", "canonical_name": "George, P. H. H.", "given_names": "P. H. H.", "surname": "George", "position": "Senior Outdoor Officer", "department": "Customs Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "V. E. Spaine", "canonical_name": "Spaine, V. E.", "given_names": "V. E.", "surname": "Spaine", "position": "First Grade Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "T. A. Clemens", "canonical_name": "Clemens, T. A.", "given_names": "T. A.", "surname": "Clemens", "position": "First Grade Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "T. M. Johnson", "canonical_name": "Johnson, T. M.", "given_names": "T. M.", "surname": "Johnson", "position": "Second ditto ditto", "department": "Customs Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "M. A. Lewis", "canonical_name": "Lewis, M. A.", "given_names": "M. A.", "surname": "Lewis", "position": "Second ditto ditto", "department": "Customs Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "T. A. Davies", "canonical_name": "Davies, T. A.", "given_names": "T. A.", "surname": "Davies", "position": "Second ditto ditto", "department": "Customs Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "Second ditto ditto", "department": "Customs Department - Sierra Leone", "salary_min": 130, "salary_max": 160}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()