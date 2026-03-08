"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "The Senior Control Officer", "canonical_name": "Senior Control Officer, The", "surname": "Senior Control Officer", "position": "Auditor-Gen. of W. African Settlements", "department": "Audit Office - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "G. W. Cole", "canonical_name": "Cole, G. W.", "given_names": "G. W.", "surname": "Cole", "position": "Clerk to ditto", "department": "Audit Office - Sierra Leone", "salary_min": 100, "salary_max": 100},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()