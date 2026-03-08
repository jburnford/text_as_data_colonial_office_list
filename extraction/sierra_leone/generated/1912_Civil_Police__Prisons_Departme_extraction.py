"""
Sierra Leone Colonial Office List 1912 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1912

OFFICIALS = [
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Commissioner", "department": "Civil Police - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "I. Heslip", "canonical_name": "Heslip, I.", "given_names": "I.", "surname": "Heslip", "position": "Assistant Commissioner", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 350, "military_rank": "Capt."},
    {"name": "R. White", "canonical_name": "White, R.", "given_names": "R.", "surname": "White", "position": "Superintendent of Prisons", "department": "Prisons Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "N. H. Sawyers", "canonical_name": "Sawyers, N. H.", "given_names": "N. H.", "surname": "Sawyers", "position": "Storekeeper", "department": "Prisons Department - Sierra Leone", "salary_min": 175, "salary_max": 200}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()