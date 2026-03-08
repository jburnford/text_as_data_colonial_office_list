"""
Sierra Leone Colonial Office List 1913 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1913

OFFICIALS = [
    {"name": "B. E. Hanson", "canonical_name": "Hanson, B. E.", "given_names": "B. E.", "surname": "Hanson", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "R. de C. Baldwin", "canonical_name": "Baldwin, R. de C.", "given_names": "R. de C.", "surname": "Baldwin", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "First Grade Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "G. P. Coker", "canonical_name": "Coker, G. P.", "given_names": "G. P.", "surname": "Coker", "position": "Second Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "Third Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "Third Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()