"""
Sierra Leone Colonial Office List 1908 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1908

OFFICIALS = [
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "T. A. Moses", "canonical_name": "Moses, T. A.", "given_names": "T. A.", "surname": "Moses", "position": "Clerk", "department": "Port and Marine Department - Sierra Leone", "salary_min": 40, "salary_max": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()