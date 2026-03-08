"""
Sierra Leone Colonial Office List 1909 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1909

OFFICIALS = [
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Commissioner", "department": "Civil Police - Sierra Leone", "salary_min": 300, "salary_max": 350, "allowances": "50l. personal"},
    {"name": "D. R. A. Bettington", "canonical_name": "Bettington, D. R. A.", "given_names": "D. R. A.", "surname": "Bettington", "position": "Inspector", "department": "Civil Police - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "R. White", "canonical_name": "White, R.", "given_names": "R.", "surname": "White", "position": "Superintendent of Prisons", "department": "Prisons Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "N. H. Sawyerr", "canonical_name": "Sawyerr, N. H.", "given_names": "N. H.", "surname": "Sawyerr", "position": "Storekeeper", "department": "Prisons Department - Sierra Leone", "salary_min": 175, "salary_max": 200},
    {"name": "G. N. Ganson", "canonical_name": "Ganson, G. N.", "given_names": "G. N.", "surname": "Ganson", "position": "Chief Warden", "department": "Prisons Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "C. A. Dixon", "canonical_name": "Dixon, C. A.", "given_names": "C. A.", "surname": "Dixon", "position": "Principal Warden Clerk", "department": "Prisons Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "R. C. Maister", "canonical_name": "Maister, R. C.", "given_names": "R. C.", "surname": "Maister", "position": "Matron", "department": "Prisons Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()