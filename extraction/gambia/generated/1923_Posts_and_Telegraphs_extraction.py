"""
Gambia Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1923

OFFICIALS = [
    {"name": "G. R. H. Frith", "canonical_name": "Frith, G. R. H.", "given_names": "G. R. H.", "surname": "Frith", "position": "Director of Posts and Telegraphs", "department": "Posts and Telegraphs - Gambia", "salary_min": 600, "salary_max": 720},
    {"name": "A. Wallis", "canonical_name": "Wallis, A.", "given_names": "A.", "surname": "Wallis", "position": "Electrical Foreman", "department": "Posts and Telegraphs - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "J. O. Nicolls", "canonical_name": "Nicolls, J. O.", "given_names": "J. O.", "surname": "Nicolls", "position": "Postmaster", "department": "Posts and Telegraphs - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "S. E. Johnson", "canonical_name": "Johnson, S. E.", "given_names": "S. E.", "surname": "Johnson", "position": "2nd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "S. M. H. Sawyerr", "canonical_name": "Sawyerr, S. M. H.", "given_names": "S. M. H.", "surname": "Sawyerr", "position": "2nd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "E. A. Jones", "canonical_name": "Jones, E. A.", "given_names": "E. A.", "surname": "Jones", "position": "2nd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "G. B. D. Campbell", "canonical_name": "Campbell, G. B. D.", "given_names": "G. B. D.", "surname": "Campbell", "position": "2nd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. B. George", "canonical_name": "George, J. B.", "given_names": "J. B.", "surname": "George", "position": "2nd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "W. T. King", "canonical_name": "King, W. T.", "given_names": "W. T.", "surname": "King", "position": "3rd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "W. F. Mahoney", "canonical_name": "Mahoney, W. F.", "given_names": "W. F.", "surname": "Mahoney", "position": "3rd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "S. A. Bidwell", "canonical_name": "Bidwell, S. A.", "given_names": "S. A.", "surname": "Bidwell", "position": "3rd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. E. Davies", "canonical_name": "Davies, J. E.", "given_names": "J. E.", "surname": "Davies", "position": "3rd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 80}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()