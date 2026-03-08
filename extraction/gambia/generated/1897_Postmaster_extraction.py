"""
Gambia Colonial Office List 1897 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1897

OFFICIALS = [
    {"name": "Postmaster", "canonical_name": "Postmaster, ", "surname": "Postmaster", "position": "Postmaster", "department": "Post Office - Gambia", "salary_min": 110, "salary_max": 110},
    {"name": "I. G. McCarthy", "canonical_name": "McCarthy, I. G.", "given_names": "I. G.", "surname": "McCarthy", "position": "Clerk", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "T. E. Peirce", "canonical_name": "Peirce, T. E.", "given_names": "T. E.", "surname": "Peirce", "position": "Collector of Customs", "department": "Customs - Gambia", "salary_min": 400, "salary_max": 400, "duty_allowance": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()