"""
Sierra Leone Colonial Office List 1899 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1899

OFFICIALS = [
    {"name": "an Asst. Inspector", "canonical_name": "Asst. Inspector, An", "surname": "Asst. Inspector", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 500, "acting_status": "Acting", "region": "Panguma District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Panguma District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Civil Establishment - Sierra Leone", "salary_min": 30, "salary_max": 40, "region": "Panguma District"},
    {"name": "O. Horrocks", "canonical_name": "Horrocks, O.", "given_names": "O.", "surname": "Horrocks", "position": "D. Surgeon", "department": "Civil Establishment - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Panguma District"},
    {"name": "J. P. Metzger", "canonical_name": "Metzger, J. P.", "given_names": "J. P.", "surname": "Metzger", "position": "Dispenser", "department": "Civil Establishment - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Panguma District"},
    {"name": "an Asst. Inspector", "canonical_name": "Asst. Inspector, An", "surname": "Asst. Inspector", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 500, "acting_status": "Acting", "region": "Koinadugu District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Koinadugu District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Civil Establishment - Sierra Leone", "salary_min": 30, "salary_max": 40, "region": "Koinadugu District"},
    {"name": "J. F. W. Ward", "canonical_name": "Ward, J. F. W.", "given_names": "J. F. W.", "surname": "Ward", "position": "D. Surgeon", "department": "Civil Establishment - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Koinadugu District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dispenser", "department": "Civil Establishment - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Koinadugu District"},
    {"name": "C. E. Birch", "canonical_name": "Birch, C. E.", "given_names": "C. E.", "surname": "Birch", "position": "A. D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 500}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()