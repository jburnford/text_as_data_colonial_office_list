"""
Sierra Leone Colonial Office List 1921 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1921

OFFICIALS = [
    {"name": "F. J. A. Beringer", "canonical_name": "Beringer, F. J. A.", "given_names": "F. J. A.", "surname": "Beringer", "position": "Senior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 1300, "salary_max": 1300, "duty_allowance": 200},
    {"name": "W. H. Peacock", "canonical_name": "Peacock, W. H.", "given_names": "W. H.", "surname": "Peacock", "position": "Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 1050, "salary_max": 1200, "duty_allowance": 210},
    {"name": "W. H. Allan", "canonical_name": "Allan, W. H.", "given_names": "W. H.", "surname": "Allan", "position": "Medical Officer of Health", "department": "Sanitary Department - Sierra Leone", "salary_min": 800, "salary_max": 960},
    {"name": "D. Bowen", "canonical_name": "Bowen, D.", "given_names": "D.", "surname": "Bowen", "position": "Superintendent, Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "G. V. Hird", "canonical_name": "Hird, G. V.", "given_names": "G. V.", "surname": "Hird", "position": "Superintendent, Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_min": 440, "salary_max": 500},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()