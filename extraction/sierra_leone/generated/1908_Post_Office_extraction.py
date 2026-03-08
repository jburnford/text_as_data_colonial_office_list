"""
Sierra Leone Colonial Office List 1908 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1908

OFFICIALS = [
    {"name": "J. C. Smith", "canonical_name": "Smith, J. C.", "given_names": "J. C.", "surname": "Smith", "position": "Colonial Postmaster-General, and Manager, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 450, "salary_max": 450, "duty_allowance": 90},
    {"name": "J. S. T. Davies", "canonical_name": "Davies, J. S. T.", "given_names": "J. S. T.", "surname": "Davies", "position": "Assistant Colonial Postmaster-General and Chief Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. N. Crown", "canonical_name": "Crown, J. N.", "given_names": "J. N.", "surname": "Crown", "position": "Chief Clerk and Examiner", "department": "Post Office - Sierra Leone", "salary_min": 180, "salary_max": 220},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "Assistant Clerk and Examiner", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "D. T. P. Cole", "canonical_name": "Cole, D. T. P.", "given_names": "D. T. P.", "surname": "Cole", "position": "Accountant", "department": "Post Office - Sierra Leone", "salary_min": 130, "salary_max": 180, "allowances": "24l. allowance"},
    {"name": "I. J. Baxter", "canonical_name": "Baxter, I. J.", "given_names": "I. J.", "surname": "Baxter", "position": "Money Order Clerk", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "E. C. Davies", "canonical_name": "Davies, E. C.", "given_names": "E. C.", "surname": "Davies", "position": "Correspondence Clerk", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 90},
    {"name": "J. T. Nottidge", "canonical_name": "Nottidge, J. T.", "given_names": "J. T.", "surname": "Nottidge", "position": "Assistant Correspondence Clerk", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "A. B. Harleston", "canonical_name": "Harleston, A. B.", "given_names": "A. B.", "surname": "Harleston", "position": "1st Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "M. A. John", "canonical_name": "John, M. A.", "given_names": "M. A.", "surname": "John", "position": "2nd Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "G. P. Bull", "canonical_name": "Bull, G. P.", "given_names": "G. P.", "surname": "Bull", "position": "3rd Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. B. C. Pratt", "canonical_name": "Pratt, J. B. C.", "given_names": "J. B. C.", "surname": "Pratt", "position": "Registration Clerk", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Accountant", "department": "Post Office - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Stampseller", "department": "Post Office - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "U. W. Coker", "canonical_name": "Coker, U. W.", "given_names": "U. W.", "surname": "Coker", "position": "Parcel Post Clerk", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "J. G. Johnson", "canonical_name": "Johnson, J. G.", "given_names": "J. G.", "surname": "Johnson", "position": "Assistant Parcel Post Clerk", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "D. A. Davies", "canonical_name": "Davies, D. A.", "given_names": "D. A.", "surname": "Davies", "position": "Chief Sorter", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 90},
    {"name": "V. E. George", "canonical_name": "George, V. E.", "given_names": "V. E.", "surname": "George", "position": "2nd Sorter and Storekeeper", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "U. R. Crown", "canonical_name": "Crown, U. R.", "given_names": "U. R.", "surname": "Crown", "position": "3rd Sorter and Storekeeper", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "Z. H. Smith", "canonical_name": "Smith, Z. H.", "given_names": "Z. H.", "surname": "Smith", "position": "4th Sorter and Storekeeper", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "H. L. Weber", "canonical_name": "Weber, H. L.", "given_names": "H. L.", "surname": "Weber", "position": "Mail Clerk", "department": "Post Office - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. Smythe", "canonical_name": "Smythe, J.", "given_names": "J.", "surname": "Smythe", "position": "Postmaster, Sherbro", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 120, "allowances": "20l. as Savings Bank Clerk", "location": "Sherbro"},
    {"name": "J. S. Coker", "canonical_name": "Coker, J. S.", "given_names": "J. S.", "surname": "Coker", "position": "Clerk to Postmaster", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40, "location": "Sherbro"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()