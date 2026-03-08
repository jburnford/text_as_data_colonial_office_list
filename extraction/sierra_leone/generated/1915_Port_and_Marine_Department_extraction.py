"""
Sierra Leone Colonial Office List 1915 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1915

OFFICIALS = [
    {"name": "W. H. Calthrop", "canonical_name": "Calthrop, W. H.", "given_names": "W. H.", "surname": "Calthrop", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "military_rank": "R.N."},
    {"name": "U. J. Lawrence", "canonical_name": "Lawrence, U. J.", "given_names": "U. J.", "surname": "Lawrence", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "T. A. Moses", "canonical_name": "Moses, T. A.", "given_names": "T. A.", "surname": "Moses", "position": "Fourth Grade Clerk", "department": "Port and Marine Department - Sierra Leone", "salary_min": 70, "salary_max": 100},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()