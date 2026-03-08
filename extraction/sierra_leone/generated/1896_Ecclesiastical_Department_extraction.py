"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "Right Rev. E. G. Ingham", "canonical_name": "Ingham, E. G.", "given_names": "E. G.", "surname": "Ingham", "position": "Bishop of Sierra Leone", "department": "Ecclesiastical Department - Sierra Leone", "qualifications": ["D.D."]},
    {"name": "Rev. S. Spain", "canonical_name": "Spain, S.", "given_names": "S.", "surname": "Spain", "position": "Colonial Chaplain", "department": "Ecclesiastical Department - Sierra Leone", "salary_min": 204, "salary_max": 204, "qualifications": ["B.A."]},
    {"name": "J. Midley", "canonical_name": "Midley, J.", "given_names": "J.", "surname": "Midley", "position": "Organist", "department": "Ecclesiastical Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "Clerk", "department": "Ecclesiastical Department - Sierra Leone", "salary_min": 25, "salary_max": 25}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()