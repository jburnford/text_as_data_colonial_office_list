"""
Sierra Leone Colonial Office List 1911 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1911

OFFICIALS = [
    {"name": "B. E. Hanson", "canonical_name": "Hanson, B. E.", "given_names": "B. E.", "surname": "Hanson", "position": "Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "R. De C. Baldwin", "canonical_name": "Baldwin, R. De C.", "given_names": "R. De C.", "surname": "Baldwin", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. Twells", "canonical_name": "Twells, J.", "given_names": "J.", "surname": "Twells", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "1st Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 180},
    {"name": "G. P. Coker", "canonical_name": "Coker, G. P.", "given_names": "G. P.", "surname": "Coker", "position": "2nd Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 160},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "3rd Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "4th Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "M. B. Reader", "canonical_name": "Reader, M. B.", "given_names": "M. B.", "surname": "Reader", "position": "5th Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "A. E. Lavers", "canonical_name": "Lavers, A. E.", "given_names": "A. E.", "surname": "Lavers", "position": "6th Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 60, "salary_max": 80},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()