"""
Sierra Leone Colonial Office List 1915 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1915

OFFICIALS = [
    {"name": "R. H. Kennan", "canonical_name": "Kennan, R. H.", "given_names": "R. H.", "surname": "Kennan", "position": "Senior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 900, "salary_max": 1000, "duty_allowance": 180},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Junior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 700, "salary_max": 800, "duty_allowance": 140},
    {"name": "W. Allan", "canonical_name": "Allan, W.", "given_names": "W.", "surname": "Allan", "position": "Medical Officer of Health", "department": "Sanitary Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "J. Black", "canonical_name": "Black, J.", "given_names": "J.", "surname": "Black", "position": "Superintendent Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Superintendent Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "Third Grade Clerk", "department": "Sanitary Department - Sierra Leone", "salary_min": 100, "salary_max": 130}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()