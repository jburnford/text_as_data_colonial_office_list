"""
Gambia Colonial Office List 1927 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1927

OFFICIALS = [
    {"name": "O. E. Kernahan", "canonical_name": "Kernahan, O. E.", "given_names": "O. E.", "surname": "Kernahan", "position": "Supervisor of Customs", "department": "Customs - The Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 230}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()