"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "R. White", "canonical_name": "White, R.", "given_names": "R.", "surname": "White", "position": "Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "G. E. Biddle", "canonical_name": "Biddle, G. E.", "given_names": "G. E.", "surname": "Biddle", "position": "Assistant Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "Storekeeper", "department": "Prisons - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Fourth Grade Clerk", "department": "Prisons - Sierra Leone", "salary_min": 70, "salary_max": 100},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()