"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "A. P. Viret", "canonical_name": "Viret, A. P.", "given_names": "A. P.", "surname": "Viret", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 600, "salary_max": 700, "duty_allowance": 120, "allowances": "in lieu of Overtime Fees 100l."},
    {"name": "A. S. Fraser", "canonical_name": "Fraser, A. S.", "given_names": "A. S.", "surname": "Fraser", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "R. B. Mackie", "canonical_name": "Mackie, R. B.", "given_names": "R. B.", "surname": "Mackie", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_min": 300, "salary_max": 400},
    {"name": "L. F. Campbell", "canonical_name": "Campbell, L. F.", "given_names": "L. F.", "surname": "Campbell", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Sherbro", "salary_min": 300, "salary_max": 350},
    {"name": "A. C. A. Johnson", "canonical_name": "Johnson, A. C. A.", "given_names": "A. C. A.", "surname": "Johnson", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "P. H. H. George", "canonical_name": "George, P. H. H.", "given_names": "P. H. H.", "surname": "George", "position": "Senior Outdoor Officer", "department": "Customs Department - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "T. A. Clemens", "canonical_name": "Clemens, T. A.", "given_names": "T. A.", "surname": "Clemens", "position": "First Class Officer", "department": "Customs Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "T. M. Johnson", "canonical_name": "Johnson, T. M.", "given_names": "T. M.", "surname": "Johnson", "position": "First Class Officer", "department": "Customs Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "B. E. Hanson", "canonical_name": "Hanson, B. E.", "given_names": "B. E.", "surname": "Hanson", "position": "Auditor", "department": "Audit - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "S. P. Warbrook", "canonical_name": "Warbrook, S. P.", "given_names": "S. P.", "surname": "Warbrook", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 300, "salary_max": 400, "duty_allowance": 60},
    {"name": "N. H. Turton", "canonical_name": "Turton, N. H.", "given_names": "N. H.", "surname": "Turton", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. E. C. Merrick", "canonical_name": "Merrick, H. E. C.", "given_names": "H. E. C.", "surname": "Merrick", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "M. B. Reader", "canonical_name": "Reader, M. B.", "given_names": "M. B.", "surname": "Reader", "position": "Second Grade Clerk", "department": "Audit - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "Third Grade Clerk", "department": "Audit - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "E. F. W. Smart", "canonical_name": "Smart, E. F. W.", "given_names": "E. F. W.", "surname": "Smart", "position": "Third Grade Clerk", "department": "Audit - Sierra Leone", "salary_min": 100, "salary_max": 130},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()