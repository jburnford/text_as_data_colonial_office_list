"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "C. B. Mitford", "canonical_name": "Mitford, C. B.", "given_names": "C. B.", "surname": "Mitford", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 500, "salary_max": 550},
    {"name": "S. M. Bennett", "canonical_name": "Bennett, S. M.", "given_names": "S. M.", "surname": "Bennett", "position": "Assistant Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "M. A. Potts", "canonical_name": "Potts, M. A.", "given_names": "M. A.", "surname": "Potts", "position": "Chief Clerk and Cashier", "department": "Treasury Department - Sierra Leone", "salary_min": 200},
    {"name": "G. W. Cole", "canonical_name": "Cole, G. W.", "given_names": "G. W.", "surname": "Cole", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 160},
    {"name": "J. J. Wellington", "canonical_name": "Wellington, J. J.", "given_names": "J. J.", "surname": "Wellington", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "R. A. Smith", "canonical_name": "Smith, R. A.", "given_names": "R. A.", "surname": "Smith", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 55, "salary_max": 55},
    {"name": "J. Edwin", "canonical_name": "Edwin, J.", "given_names": "J.", "surname": "Edwin", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 42, "salary_max": 42},
    {"name": "J. S. Wright", "canonical_name": "Wright, J. S.", "given_names": "J. S.", "surname": "Wright", "position": "6th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "J. A. Cline", "canonical_name": "Cline, J. A.", "given_names": "J. A.", "surname": "Cline", "position": "Sub-Accountant at Sulymah", "department": "Treasury Department - Sierra Leone", "salary_min": 10, "salary_max": 10},
    {"name": "W. Metzger", "canonical_name": "Metzger, W.", "given_names": "W.", "surname": "Metzger", "position": "Assistant Clerk", "department": "Savings Bank - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "The Postmaster", "canonical_name": "Postmaster, The", "surname": "Postmaster", "position": "Clerk at Sherbro", "department": "Savings Bank - Sierra Leone", "salary_min": 20, "salary_max": 20, "location": "Sherbro"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()