"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "W. Ransley", "canonical_name": "Ransley, W.", "given_names": "W.", "surname": "Ransley", "position": "Preventive Inspector", "department": "Preventive Service - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "F. Q. Martyn", "canonical_name": "Martyn, F. Q.", "given_names": "F. Q.", "surname": "Martyn", "position": "Preventive Officer", "department": "Preventive Service - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "U. J. Lawrence", "canonical_name": "Lawrence, U. J.", "given_names": "U. J.", "surname": "Lawrence", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "T. A. Moses", "canonical_name": "Moses, T. A.", "given_names": "T. A.", "surname": "Moses", "position": "Clerk", "department": "Port and Marine Department - Sierra Leone", "salary_min": 40, "salary_max": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()