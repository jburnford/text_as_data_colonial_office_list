"""
Gambia Colonial Office List 1894 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1894

OFFICIALS = [
    {"name": "C. H. H. Mosley", "canonical_name": "Mosley, C. H. H.", "given_names": "C. H. H.", "surname": "Mosley", "position": "Treasurer", "department": "Treasury - Gambia", "salary_min": 500, "salary_max": 500, "allowances": "quarters", "duty_allowance": 60},
    {"name": "S. D. A. Coker", "canonical_name": "Coker, S. D. A.", "given_names": "S. D. A.", "surname": "Coker", "position": "Chief Clerk and Cashier", "department": "Treasury - Gambia", "salary_min": 170, "salary_max": 170},
    {"name": "S. F. Jie", "canonical_name": "Jie, S. F.", "given_names": "S. F.", "surname": "Jie", "position": "Acting Assistant Clerk", "department": "Treasury - Gambia", "salary_min": 50, "salary_max": 50, "acting_status": "Acting"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()