"""
Sierra Leone Colonial Office List 1915 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1915

OFFICIALS = [
    {"name": "I. Heslip", "canonical_name": "Heslip, I.", "given_names": "I.", "surname": "Heslip", "position": "Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "military_rank": "Captain"},
    {"name": "A. S. Mavrogordato", "canonical_name": "Mavrogordato, A. S.", "given_names": "A. S.", "surname": "Mavrogordato", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "F. T. McKeon", "canonical_name": "McKeon, F. T.", "given_names": "F. T.", "surname": "McKeon", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "R. White", "canonical_name": "White, R.", "given_names": "R.", "surname": "White", "position": "Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "G. E. Biddle", "canonical_name": "Biddle, G. E.", "given_names": "G. E.", "surname": "Biddle", "position": "Assistant Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "Storekeeper", "department": "Prisons - Sierra Leone", "salary_min": 160, "salary_max": 200},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()