"""
Sierra Leone Colonial Office List 1917 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1917

OFFICIALS = [
    {"name": "R. Laurie", "canonical_name": "Laurie, R.", "given_names": "R.", "surname": "Laurie", "position": "Senior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 900, "salary_max": 950, "duty_allowance": 180},
    {"name": "G. T. Pirie", "canonical_name": "Pirie, G. T.", "given_names": "G. T.", "surname": "Pirie", "position": "Junior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 700, "salary_max": 800, "duty_allowance": 140},
    {"name": "W. Allan", "canonical_name": "Allan, W.", "given_names": "W.", "surname": "Allan", "position": "Medical Officer of Health", "department": "Sanitary Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100, "allowances": "100l. staff pay"},
    {"name": "D. S. Bowen", "canonical_name": "Bowen, D. S.", "given_names": "D. S.", "surname": "Bowen", "position": "Superintendent Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Superintendent Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "Third Grade Clerk", "department": "Sanitary Department - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Fourth Grade Clerk", "department": "Sanitary Department - Sierra Leone", "salary_min": 70, "salary_max": 100},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Fifth Grade Clerks", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 70},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Fifth Grade Clerks", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 70},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()