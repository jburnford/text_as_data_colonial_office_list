"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "J. Rowland Crook", "canonical_name": "Crook, J. Rowland", "given_names": "J. Rowland", "surname": "Crook", "position": "Government Engineer", "department": "Public Works - Gambia", "salary_min": 500, "salary_max": 600, "allowances": "42l. for forage allowance", "qualifications": ["M.I.C.E."]},
    {"name": "D. Benatar", "canonical_name": "Benatar, D.", "given_names": "D.", "surname": "Benatar", "position": "Surveyor", "department": "Public Works - Gambia", "salary_min": 200, "salary_max": 250, "qualifications": ["B.Sc.", "B.Eng."]},
    {"name": "H. F. J. Maxted", "canonical_name": "Maxted, H. F. J.", "given_names": "H. F. J.", "surname": "Maxted", "position": "1st Class Clerk", "department": "Public Works - Gambia", "salary_min": 210, "salary_max": 300, "allowances": "45l. as Secretary to Cemetery Committee"},
    {"name": "S. Chiappe", "canonical_name": "Chiappe, S.", "given_names": "S.", "surname": "Chiappe", "position": "Clerk of Works", "department": "Public Works - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "F. L. Francis", "canonical_name": "Francis, F. L.", "given_names": "F. L.", "surname": "Francis", "position": "Auditor", "department": "Audit - Gambia", "salary_min": 350, "salary_max": 400, "allowances": "86l. as Auditor to the Sanitary Commissioners"},
    {"name": "A. Day", "canonical_name": "Day, A.", "given_names": "A.", "surname": "Day", "position": "2nd Class Clerk", "department": "Audit - Gambia", "salary_min": 160, "salary_max": 200},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()