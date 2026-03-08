"""
Gambia Colonial Office List 1894 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1894

OFFICIALS = [
    {"name": "James Collie", "canonical_name": "Collie, James", "given_names": "James", "surname": "Collie", "position": "Colonial Engineer and Sanitary Inspector", "department": "Civil Establishment - Gambia", "salary_min": 500, "salary_max": 500, "allowances": "and quarters, or 60l. for rent"},
    {"name": "G. M. Jie", "canonical_name": "Jie, G. M.", "given_names": "G. M.", "surname": "Jie", "position": "Foreman of Works", "department": "Civil Establishment - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "T. J. Carew", "canonical_name": "Carew, T. J.", "given_names": "T. J.", "surname": "Carew", "position": "Clerk", "department": "Civil Establishment - Gambia", "salary_min": 60, "salary_max": 60, "allowances": "(of which 10l. is personal)"},
    {"name": "John C. Fye", "canonical_name": "Fye, John C.", "given_names": "John C.", "surname": "Fye", "position": "Storekeeper, Timekeeper, and Office Assistant", "department": "Civil Establishment - Gambia", "salary_min": 50, "salary_max": 50, "per_diem": "per annum"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()