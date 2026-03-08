"""
Sierra Leone Colonial Office List 1917 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1917

OFFICIALS = [
    {"name": "O. Mitchell", "canonical_name": "Mitchell, O.", "given_names": "O.", "surname": "Mitchell", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "A. S. Fraser", "canonical_name": "Fraser, A. S.", "given_names": "A. S.", "surname": "Fraser", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "R. B. Mackie", "canonical_name": "Mackie, R. B.", "given_names": "R. B.", "surname": "Mackie", "position": "Supervisor of Customs, Freetown", "department": "Customs Department - Sierra Leone", "salary_min": 300, "salary_max": 400, "location": "Freetown"},
    {"name": "L. F. Campbell", "canonical_name": "Campbell, L. F.", "given_names": "L. F.", "surname": "Campbell", "position": "Supervisor of Customs, Sherbro", "department": "Customs Department - Sierra Leone", "salary_min": 300, "salary_max": 350, "location": "Sherbro"},
    {"name": "A. C. A. Johnson", "canonical_name": "Johnson, A. C. A.", "given_names": "A. C. A.", "surname": "Johnson", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "P. H. H. George", "canonical_name": "George, P. H. H.", "given_names": "P. H. H.", "surname": "George", "position": "Senior Outdoor Officer", "department": "Customs Department - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "V. E. Spaine", "canonical_name": "Spaine, V. E.", "given_names": "V. E.", "surname": "Spaine", "position": "First Class Officers", "department": "Customs Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "T. A. Clemens", "canonical_name": "Clemens, T. A.", "given_names": "T. A.", "surname": "Clemens", "position": "First Class Officers", "department": "Customs Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()