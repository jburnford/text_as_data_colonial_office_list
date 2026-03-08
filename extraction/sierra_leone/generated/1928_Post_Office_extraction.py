"""
Sierra Leone Colonial Office List 1928 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1928

OFFICIALS = [
    {"name": "N. S. Davis", "canonical_name": "Davis, N. S.", "given_names": "N. S.", "surname": "Davis", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Assistant Postmaster General and Accountant", "department": "Post Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "J. H. Smyth", "canonical_name": "Smyth, J. H.", "given_names": "J. H.", "surname": "Smyth", "position": "Staff Superintendent", "department": "Post Office - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "M. A. John", "canonical_name": "John, M. A.", "given_names": "M. A.", "surname": "John", "position": "Chief Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "D. A. Davies", "canonical_name": "Davies, D. A.", "given_names": "D. A.", "surname": "Davies", "position": "Chief Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "V. E. George", "canonical_name": "George, V. E.", "given_names": "V. E.", "surname": "George", "position": "Chief Clerk", "department": "Post Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "J. G. Johnson", "canonical_name": "Johnson, J. G.", "given_names": "J. G.", "surname": "Johnson", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. T. Nottridge", "canonical_name": "Nottridge, J. T.", "given_names": "J. T.", "surname": "Nottridge", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. T. W. Richards", "canonical_name": "Richards, A. T. W.", "given_names": "A. T. W.", "surname": "Richards", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "W. J. Cole", "canonical_name": "Cole, W. J.", "given_names": "W. J.", "surname": "Cole", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "E. S. B. Francis", "canonical_name": "Francis, E. S. B.", "given_names": "E. S. B.", "surname": "Francis", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "Z. H. Smith", "canonical_name": "Smith, Z. H.", "given_names": "Z. H.", "surname": "Smith", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "G. H. H. Branche", "canonical_name": "Branche, G. H. H.", "given_names": "G. H. H.", "surname": "Branche", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "P. S. Godwin", "canonical_name": "Godwin, P. S.", "given_names": "P. S.", "surname": "Godwin", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. E. Mamman", "canonical_name": "Mamman, A. E.", "given_names": "A. E.", "surname": "Mamman", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "M. Y. Sanusi", "canonical_name": "Sanusi, M. Y.", "given_names": "M. Y.", "surname": "Sanusi", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()