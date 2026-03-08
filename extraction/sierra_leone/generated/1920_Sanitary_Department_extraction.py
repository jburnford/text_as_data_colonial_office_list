"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "F. J. A. Beringer", "canonical_name": "Beringer, F. J. A.", "given_names": "F. J. A.", "surname": "Beringer", "position": "Senior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 900, "salary_max": 950, "duty_allowance": 180},
    {"name": "W. H. Peacock", "canonical_name": "Peacock, W. H.", "given_names": "W. H.", "surname": "Peacock", "position": "Junior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 700, "salary_max": 800, "duty_allowance": 140, "military_rank": "Major"},
    {"name": "W. Allan", "canonical_name": "Allan, W.", "given_names": "W.", "surname": "Allan", "position": "Medical Officer of Health", "department": "Sanitary Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "D. S. Bowen", "canonical_name": "Bowen, D. S.", "given_names": "D. S.", "surname": "Bowen", "position": "Superintendent Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Superintendent Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "Third Grade Clerk", "department": "Sanitary Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()