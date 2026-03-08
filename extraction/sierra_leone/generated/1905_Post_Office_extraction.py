"""
Sierra Leone Colonial Office List 1905 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1905

OFFICIALS = [
    {"name": "J. C. Smith", "canonical_name": "Smith, J. C.", "given_names": "J. C.", "surname": "Smith", "position": "Colonial Postmaster-General", "department": "Post Office - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "J. S. T. Davies", "canonical_name": "Davies, J. S. T.", "given_names": "J. S. T.", "surname": "Davies", "position": "Assistant Colonial Postmaster-General and Chief Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. N. Crown", "canonical_name": "Crown, J. N.", "given_names": "J. N.", "surname": "Crown", "position": "Chief Clerk and Examiner", "department": "Post Office - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "D. T. P. Cole", "canonical_name": "Cole, D. T. P.", "given_names": "D. T. P.", "surname": "Cole", "position": "Accountant", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "I. J. Baxter", "canonical_name": "Baxter, I. J.", "given_names": "I. J.", "surname": "Baxter", "position": "Money Order Clerk", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "E. C. Davies", "canonical_name": "Davies, E. C.", "given_names": "E. C.", "surname": "Davies", "position": "Correspondence Clerk", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 90},
    {"name": "T. B. Jones", "canonical_name": "Jones, T. B.", "given_names": "T. B.", "surname": "Jones", "position": "Assistant Correspondence Clerk", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "A. B. Harleston", "canonical_name": "Harleston, A. B.", "given_names": "A. B.", "surname": "Harleston", "position": "Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 95},
    {"name": "M. A. John", "canonical_name": "John, M. A.", "given_names": "M. A.", "surname": "John", "position": "1st Assistant Clerk", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "D. E. Grant", "canonical_name": "Grant, D. E.", "given_names": "D. E.", "surname": "Grant", "position": "2nd Assistant Clerk", "department": "Post Office - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. B. C. Pratt", "canonical_name": "Pratt, J. B. C.", "given_names": "J. B. C.", "surname": "Pratt", "position": "Registration Clerk", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "V. E. George", "canonical_name": "George, V. E.", "given_names": "V. E.", "surname": "George", "position": "Stampseller", "department": "Post Office - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "U. W. Coker", "canonical_name": "Coker, U. W.", "given_names": "U. W.", "surname": "Coker", "position": "Parcel Post Clerk", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "Chief Sorter", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 90},
    {"name": "D. A. Davies", "canonical_name": "Davies, D. A.", "given_names": "D. A.", "surname": "Davies", "position": "2nd Sorter", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "H. L. Webber", "canonical_name": "Webber, H. L.", "given_names": "H. L.", "surname": "Webber", "position": "3rd Sorter", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "M. B. Reider", "canonical_name": "Reider, M. B.", "given_names": "M. B.", "surname": "Reider", "position": "4th Sorter", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "M. A. John", "canonical_name": "John, M. A.", "given_names": "M. A.", "surname": "John", "position": "Mail Clerk", "department": "Post Office - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. A. Songo Davies", "canonical_name": "Davies, J. A. Songo", "given_names": "J. A. Songo", "surname": "Davies", "position": "Postmaster", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 120, "location": "Sherbro", "allowances": "plus 20l. as Savings Bank Clerk"},
    {"name": "A. E. Mammah", "canonical_name": "Mammah, A. E.", "given_names": "A. E.", "surname": "Mammah", "position": "Clerk to ditto", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40, "location": "Sherbro"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()