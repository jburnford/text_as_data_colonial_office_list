"""
Sierra Leone Colonial Office List 1908 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1908

OFFICIALS = [
    {"name": "E. du Boulay", "canonical_name": "Boulay, E. du", "given_names": "E.", "surname": "Boulay", "position": "Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "R. H. Jebb", "canonical_name": "Jebb, R. H.", "given_names": "R. H.", "surname": "Jebb", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "1st Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 160},
    {"name": "G. P. Coker", "canonical_name": "Coker, G. P.", "given_names": "G. P.", "surname": "Coker", "position": "2nd Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 140},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "3rd Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "4th Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "J. F. Smith", "canonical_name": "Smith, J. F.", "given_names": "J. F.", "surname": "Smith", "position": "5th Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()