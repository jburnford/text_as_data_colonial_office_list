"""
Sierra Leone Colonial Office List 1898 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1898

OFFICIALS = [
    {"name": "S. M. Bennett", "canonical_name": "Bennett, S. M.", "given_names": "S. M.", "surname": "Bennett", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "E. O. Johnson", "canonical_name": "Johnson, E. O.", "given_names": "E. O.", "surname": "Johnson", "position": "Assistant Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "G. W. Cole", "canonical_name": "Cole, G. W.", "given_names": "G. W.", "surname": "Cole", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 180},
    {"name": "J. J. Wellington", "canonical_name": "Wellington, J. J.", "given_names": "J. J.", "surname": "Wellington", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "R. A. Smith", "canonical_name": "Smith, R. A.", "given_names": "R. A.", "surname": "Smith", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 55, "salary_max": 70},
    {"name": "J. Edwin", "canonical_name": "Edwin, J.", "given_names": "J.", "surname": "Edwin", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 42, "salary_max": 50},
    {"name": "C. A. Gilpin", "canonical_name": "Gilpin, C. A.", "given_names": "C. A.", "surname": "Gilpin", "position": "6th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 24, "salary_max": 30},
    {"name": "A. Harleston", "canonical_name": "Harleston, A.", "given_names": "A.", "surname": "Harleston", "position": "Clerk and Accountant", "department": "Savings Bank - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "J. Mannah", "canonical_name": "Mannah, J.", "given_names": "J.", "surname": "Mannah", "position": "Assistant Clerk", "department": "Savings Bank - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "The Postmaster", "canonical_name": "Postmaster, The", "surname": "Postmaster", "position": "Clerk at Sherbro", "department": "Savings Bank - Sierra Leone", "salary_min": 20, "salary_max": 20}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()