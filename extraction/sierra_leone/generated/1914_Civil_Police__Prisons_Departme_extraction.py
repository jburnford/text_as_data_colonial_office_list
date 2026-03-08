"""
Sierra Leone Colonial Office List 1914 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1914

OFFICIALS = [
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Commissioner", "department": "Civil Police - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "allowances": "100l. personal allowance"},
    {"name": "I. Heelip", "canonical_name": "Heelip, I.", "given_names": "I.", "surname": "Heelip", "position": "Assistant Commissioner", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 400, "military_rank": "Captain"},
    {"name": "A. S. Mavrogordato", "canonical_name": "Mavrogordato, A. S.", "given_names": "A. S.", "surname": "Mavrogordato", "position": "Assistant Commissioner", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "R. White", "canonical_name": "White, R.", "given_names": "R.", "surname": "White", "position": "Superintendent of Prisons", "department": "Prisons Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "N. H. Sawyerr", "canonical_name": "Sawyerr, N. H.", "given_names": "N. H.", "surname": "Sawyerr", "position": "Storekeeper", "department": "Prisons Department - Sierra Leone", "salary_min": 175, "salary_max": 200}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()