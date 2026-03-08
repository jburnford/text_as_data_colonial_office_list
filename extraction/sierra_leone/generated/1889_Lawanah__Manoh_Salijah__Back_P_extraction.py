"""
Sierra Leone Colonial Office List 1889 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1889

OFFICIALS = [
    {"name": "L. J. E. Roques", "canonical_name": "Roques, L. J. E.", "given_names": "L. J. E.", "surname": "Roques", "position": "Assistant Examining Officer", "department": "Customs - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "J. A. Songo Davies", "canonical_name": "Davies, J. A. Songo", "given_names": "J. A. Songo", "surname": "Davies", "position": "Assistant Examining Officer", "department": "Customs - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "U. J. Lawrence", "canonical_name": "Lawrence, U. J.", "given_names": "U. J.", "surname": "Lawrence", "position": "Officer in Charge", "department": "Customs - Sierra Leone", "salary_min": 75, "salary_max": 75},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()