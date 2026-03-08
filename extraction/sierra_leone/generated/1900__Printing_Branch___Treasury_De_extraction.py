"""
Sierra Leone Colonial Office List 1900 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1900

OFFICIALS = [
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Government Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. C. Gilpin", "canonical_name": "Gilpin, J. C.", "given_names": "J. C.", "surname": "Gilpin", "position": "Second Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "T. B. Macauley", "canonical_name": "Macauley, T. B.", "given_names": "T. B.", "surname": "Macauley", "position": "First Class Composer", "department": "Printing Branch - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. C. Johnston", "canonical_name": "Johnston, E. C.", "given_names": "E. C.", "surname": "Johnston", "position": "First Class Composer", "department": "Printing Branch - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. O. Johnson", "canonical_name": "Johnson, E. O.", "given_names": "E. O.", "surname": "Johnson", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 500, "salary_max": 550},
    {"name": "A. P. Viret", "canonical_name": "Viret, A. P.", "given_names": "A. P.", "surname": "Viret", "position": "Assistant Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "F. H. Hamilton", "canonical_name": "Hamilton, F. H.", "given_names": "F. H.", "surname": "Hamilton", "position": "Chief Clerk and Cashier", "department": "Treasury Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "G. W. Cole", "canonical_name": "Cole, G. W.", "given_names": "G. W.", "surname": "Cole", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 180},
    {"name": "J. Edwin", "canonical_name": "Edwin, J.", "given_names": "J.", "surname": "Edwin", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 90, "salary_max": 110},
    {"name": "W. E. Campbell", "canonical_name": "Campbell, W. E.", "given_names": "W. E.", "surname": "Campbell", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 65, "salary_max": 80},
    {"name": "C. A. Gilpin", "canonical_name": "Gilpin, C. A.", "given_names": "C. A.", "surname": "Gilpin", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "Silas Dove", "canonical_name": "Dove, Silas", "given_names": "Silas", "surname": "Dove", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "F. Martyn", "canonical_name": "Martyn, F.", "given_names": "F.", "surname": "Martyn", "position": "6th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 24, "salary_max": 30},
    {"name": "A. Harleston", "canonical_name": "Harleston, A.", "given_names": "A.", "surname": "Harleston", "position": "Clerk and Accountant", "department": "Savings Bank - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "G. P. Coker", "canonical_name": "Coker, G. P.", "given_names": "G. P.", "surname": "Coker", "position": "Assistant Clerk", "department": "Savings Bank - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "The Postmaster", "canonical_name": "Postmaster, The", "surname": "Postmaster", "position": "Clerk at Sherbro", "department": "Savings Bank - Sierra Leone", "salary_min": 20, "salary_max": 20, "location": "Sherbro"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()