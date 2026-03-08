"""
Sierra Leone Colonial Office List 1899 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1899

OFFICIALS = [
    {"name": "E. O. Johnson", "canonical_name": "Johnson, E. O.", "given_names": "E. O.", "surname": "Johnson", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 500, "salary_max": 550},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "A. G. Lloyd", "canonical_name": "Lloyd, A. G.", "given_names": "A. G.", "surname": "Lloyd", "position": "Chief Clerk and Cashier", "department": "Treasury Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "G. W. Cole", "canonical_name": "Cole, G. W.", "given_names": "G. W.", "surname": "Cole", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 160, "salary_max": 180},
    {"name": "J. Edwin", "canonical_name": "Edwin, J.", "given_names": "J.", "surname": "Edwin", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 90, "salary_max": 110},
    {"name": "C. A. Gilpin", "canonical_name": "Gilpin, C. A.", "given_names": "C. A.", "surname": "Gilpin", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "W. B. Gilpin", "canonical_name": "Gilpin, W. B.", "given_names": "W. B.", "surname": "Gilpin", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "Silas Dove", "canonical_name": "Dove, Silas", "given_names": "Silas", "surname": "Dove", "position": "6th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 24, "salary_max": 30},
    {"name": "A. Harleston", "canonical_name": "Harleston, A.", "given_names": "A.", "surname": "Harleston", "position": "Clerk and Accountant", "department": "Treasury Department - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "G. W. Palmer", "canonical_name": "Palmer, G. W.", "given_names": "G. W.", "surname": "Palmer", "position": "Assistant Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "J. C. E. Parkes", "canonical_name": "Parkes, J. C. E.", "given_names": "J. C. E.", "surname": "Parkes", "position": "Secretary", "department": "Native Affairs Department - Sierra Leone", "salary_min": 350, "salary_max": 350},
    {"name": "Mohammed Sanusi", "canonical_name": "Sanusi, Mohammed", "given_names": "Mohammed", "surname": "Sanusi", "position": "Arabic Writer", "department": "Native Affairs Department - Sierra Leone", "salary_min": 70, "salary_max": 70},
    {"name": "Kathorudeen", "canonical_name": "Kathorudeen, ", "surname": "Kathorudeen", "position": "Clerk", "department": "Native Affairs Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "Jonathan Reffell", "canonical_name": "Reffell, Jonathan", "given_names": "Jonathan", "surname": "Reffell", "position": "Clerk", "department": "Native Affairs Department - Sierra Leone", "salary_min": 30, "salary_max": 40}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()