"""
Gambia Colonial Office List 1925 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1925

OFFICIALS = [
    {"name": "H. D. Smith", "canonical_name": "Smith, H. D.", "given_names": "H. D.", "surname": "Smith", "position": "Director of Posts and Telegraphs", "department": "Posts and Telegraphs - Gambia"},
    {"name": "A. Wallis", "canonical_name": "Wallis, A.", "given_names": "A.", "surname": "Wallis", "position": "Electrical Foreman", "department": "Posts and Telegraphs - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "G. Hill", "canonical_name": "Hill, G.", "given_names": "G.", "surname": "Hill", "position": "Wireless Engineer Operator", "department": "Posts and Telegraphs - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "J. O. Nicolls", "canonical_name": "Nicolls, J. O.", "given_names": "J. O.", "surname": "Nicolls", "position": "Postmaster", "department": "Posts and Telegraphs - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "2nd Grade Clerk", "department": "Posts and Telegraphs - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "S. E. Johnson", "canonical_name": "Johnson, S. E.", "given_names": "S. E.", "surname": "Johnson", "position": "3rd Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "S. M. H. Sawyer", "canonical_name": "Sawyer, S. M. H.", "given_names": "S. M. H.", "surname": "Sawyer", "position": "3rd Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. B. George", "canonical_name": "George, J. B.", "given_names": "J. B.", "surname": "George", "position": "3rd Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "W. T. King", "canonical_name": "King, W. T.", "given_names": "W. T.", "surname": "King", "position": "3rd Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "F. A. Smart", "canonical_name": "Smart, F. A.", "given_names": "F. A.", "surname": "Smart", "position": "3rd Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "C. J. Thomas", "canonical_name": "Thomas, C. J.", "given_names": "C. J.", "surname": "Thomas", "position": "3rd Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. E. Davies", "canonical_name": "Davies, J. E.", "given_names": "J. E.", "surname": "Davies", "position": "4th Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "W. F. Mahoney", "canonical_name": "Mahoney, W. F.", "given_names": "W. F.", "surname": "Mahoney", "position": "4th Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "S. A. Bidwell", "canonical_name": "Bidwell, S. A.", "given_names": "S. A.", "surname": "Bidwell", "position": "4th Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "S. E. Grant", "canonical_name": "Grant, S. E.", "given_names": "S. E.", "surname": "Grant", "position": "4th Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "J. E. Boston", "canonical_name": "Boston, J. E.", "given_names": "J. E.", "surname": "Boston", "position": "4th Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "M. L. Jones", "canonical_name": "Jones, M. L.", "given_names": "M. L.", "surname": "Jones", "position": "4th Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "A. John", "canonical_name": "John, A.", "given_names": "A.", "surname": "John", "position": "4th Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "R. J. Andrews", "canonical_name": "Andrews, R. J.", "given_names": "R. J.", "surname": "Andrews", "position": "4th Grade Clerks", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "R. S. S. Decker", "canonical_name": "Decker, R. S. S.", "given_names": "R. S. S.", "surname": "Decker", "position": "Telephone Operator", "department": "Posts and Telegraphs - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "A. J. Brooks", "canonical_name": "Brooks, A. J.", "given_names": "A. J.", "surname": "Brooks", "position": "Director of Agriculture", "department": "Agricultural Department - Gambia", "salary_min": 600, "salary_max": 920, "qualifications": ["F.L.S.", "F.C.S.", "F.R.H.S."]},
    {"name": "C. W. J. Line", "canonical_name": "Line, C. W. J.", "given_names": "C. W. J.", "surname": "Line", "position": "Assistant Director", "department": "Agricultural Department - Gambia", "salary_min": 510, "salary_max": 720, "qualifications": ["B.A."]},
    {"name": "J. Pirie", "canonical_name": "Pirie, J.", "given_names": "J.", "surname": "Pirie", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 450, "salary_max": 600}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()