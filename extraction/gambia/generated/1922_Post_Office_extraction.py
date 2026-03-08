"""
Gambia Colonial Office List 1922 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1922

OFFICIALS = [
    {"name": "A. D. Frith", "canonical_name": "Frith, A. D.", "given_names": "A. D.", "surname": "Frith", "position": "Director of Posts and Telegraphs", "department": "Post Office - Gambia", "salary_min": 600, "salary_max": 720},
    {"name": "J. O. Nicolls", "canonical_name": "Nicolls, J. O.", "given_names": "J. O.", "surname": "Nicolls", "position": "Postmaster", "department": "Post Office - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "S. E. Johnson", "canonical_name": "Johnson, S. E.", "given_names": "S. E.", "surname": "Johnson", "position": "2nd Grade Clerks", "department": "Post Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "S. M. H. Sawyerr", "canonical_name": "Sawyerr, S. M. H.", "given_names": "S. M. H.", "surname": "Sawyerr", "position": "2nd Grade Clerks", "department": "Post Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "E. A. Jones", "canonical_name": "Jones, E. A.", "given_names": "E. A.", "surname": "Jones", "position": "2nd Grade Clerks", "department": "Post Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "G. B. D. Campbell", "canonical_name": "Campbell, G. B. D.", "given_names": "G. B. D.", "surname": "Campbell", "position": "2nd Grade Clerks", "department": "Post Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. B. George", "canonical_name": "George, J. B.", "given_names": "J. B.", "surname": "George", "position": "3rd Grade Clerks", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. E. Davies", "canonical_name": "Davies, J. E.", "given_names": "J. E.", "surname": "Davies", "position": "3rd Grade Clerks", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 80},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()