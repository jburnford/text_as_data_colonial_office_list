"""
Gambia Colonial Office List 1924 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1924

OFFICIALS = [
    {"name": "G. R. H. Frith", "canonical_name": "Frith, G. R. H.", "given_names": "G. R. H.", "surname": "Frith", "position": "Director of Posts and Telegraphs", "department": "Posts and Telegraphs - Gambia", "salary_min": 600, "salary_max": 720},
    {"name": "A. Wallis", "canonical_name": "Wallis, A.", "given_names": "A.", "surname": "Wallis", "position": "Electrical Foreman", "department": "Posts and Telegraphs - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "G. Hill", "canonical_name": "Hill, G.", "given_names": "G.", "surname": "Hill", "position": "Wireless Engineer Operator", "department": "Posts and Telegraphs - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "J. O. Nicola", "canonical_name": "Nicola, J. O.", "given_names": "J. O.", "surname": "Nicola", "position": "Postmaster", "department": "Posts and Telegraphs - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "S. E. Johnson", "canonical_name": "Johnson, S. E.", "given_names": "S. E.", "surname": "Johnson", "position": "3rd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "S.M.H. Sawyer", "canonical_name": "Sawyer, S.M.H.", "given_names": "S.M.H.", "surname": "Sawyer", "position": "3rd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "R. A. Jones", "canonical_name": "Jones, R. A.", "given_names": "R. A.", "surname": "Jones", "position": "3rd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. B. George", "canonical_name": "George, J. B.", "given_names": "J. B.", "surname": "George", "position": "3rd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. R. T'vies", "canonical_name": "T'vies, J. R.", "given_names": "J. R.", "surname": "T'vies", "position": "3rd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "W. T. King", "canonical_name": "King, W. T.", "given_names": "W. T.", "surname": "King", "position": "3rd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "W. F. Mahoney", "canonical_name": "Mahoney, W. F.", "given_names": "W. F.", "surname": "Mahoney", "position": "4th Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "S. A. Bidwell", "canonical_name": "Bidwell, S. A.", "given_names": "S. A.", "surname": "Bidwell", "position": "4th Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "K. A. Smart", "canonical_name": "Smart, K. A.", "given_names": "K. A.", "surname": "Smart", "position": "4th Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "S. E. Grant", "canonical_name": "Grant, S. E.", "given_names": "S. E.", "surname": "Grant", "position": "4th Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "C. E. Bell", "canonical_name": "Bell, C. E.", "given_names": "C. E.", "surname": "Bell", "position": "4th Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "J. E. Houston", "canonical_name": "Houston, J. E.", "given_names": "J. E.", "surname": "Houston", "position": "4th Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "M. L. Jones", "canonical_name": "Jones, M. L.", "given_names": "M. L.", "surname": "Jones", "position": "4th Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "R. S. S. Decker", "canonical_name": "Decker, R. S. S.", "given_names": "R. S. S.", "surname": "Decker", "position": "Telephone Operator", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()