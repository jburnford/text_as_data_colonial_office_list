"""
Sierra Leone Colonial Office List 1907 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1907

OFFICIALS = [
    {"name": "Edgar du Boulay", "canonical_name": "Boulay, Edgar du", "given_names": "Edgar", "surname": "Boulay", "position": "Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "G. R. Moore", "canonical_name": "Moore, G. R.", "given_names": "G. R.", "surname": "Moore", "position": "Assistant Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "1st Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "G. R. Coker", "canonical_name": "Coker, G. R.", "given_names": "G. R.", "surname": "Coker", "position": "2nd Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "3rd Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. L. Mamah", "canonical_name": "Mamah, J. L.", "given_names": "J. L.", "surname": "Mamah", "position": "4th Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "J. F. Smith", "canonical_name": "Smith, J. F.", "given_names": "J. F.", "surname": "Smith", "position": "5th Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()