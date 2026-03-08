"""
Sierra Leone Colonial Office List 1907 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1907

OFFICIALS = [
    {"name": "J. C. Smith", "canonical_name": "Smith, J. C.", "given_names": "J. C.", "surname": "Smith", "position": "Colonial Postmaster-General", "department": "Post Office - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "J. S. T. Davies", "canonical_name": "Davies, J. S. T.", "given_names": "J. S. T.", "surname": "Davies", "position": "Assistant Colonial Postmaster-General and Chief Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. N. Crown", "canonical_name": "Crown, J. N.", "given_names": "J. N.", "surname": "Crown", "position": "Chief Clerk and Examiner", "department": "Post Office - Sierra Leone", "salary_min": 180, "salary_max": 220},
    {"name": "M. S. Macaulay", "canonical_name": "Macaulay, M. S.", "given_names": "M. S.", "surname": "Macaulay", "position": "Assistant Chief Clerk and Examiner", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "D. T. P. Cole", "canonical_name": "Cole, D. T. P.", "given_names": "D. T. P.", "surname": "Cole", "position": "Accountant", "department": "Post Office - Sierra Leone", "salary_min": 130, "salary_max": 180},
    {"name": "I. J. Baxter", "canonical_name": "Baxter, I. J.", "given_names": "I. J.", "surname": "Baxter", "position": "Money Order Clerk", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "E. C. Davies", "canonical_name": "Davies, E. C.", "given_names": "E. C.", "surname": "Davies", "position": "Correspondence Clerk", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 90},
    {"name": "J. T. Nottidge", "canonical_name": "Nottidge, J. T.", "given_names": "J. T.", "surname": "Nottidge", "position": "Assistant Correspondence Clerk", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "J. Smythe", "canonical_name": "Smythe, J.", "given_names": "J.", "surname": "Smythe", "position": "Assistant Accountant", "department": "Post Office - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "A. B. Charleston", "canonical_name": "Charleston, A. B.", "given_names": "A. B.", "surname": "Charleston", "position": "Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "M. A. John", "canonical_name": "John, M. A.", "given_names": "M. A.", "surname": "John", "position": "1st Assistant Clerk", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "M. B. Reider", "canonical_name": "Reider, M. B.", "given_names": "M. B.", "surname": "Reider", "position": "2nd Assistant Clerk", "department": "Post Office - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. B. C. Pratt", "canonical_name": "Pratt, J. B. C.", "given_names": "J. B. C.", "surname": "Pratt", "position": "Registration Clerk", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Stampseller", "department": "Post Office - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "U. W. Coker", "canonical_name": "Coker, U. W.", "given_names": "U. W.", "surname": "Coker", "position": "Parcel Post Clerk", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "J. G. Johnson", "canonical_name": "Johnson, J. G.", "given_names": "J. G.", "surname": "Johnson", "position": "Assistant Clerk", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "D. A. Davies", "canonical_name": "Davies, D. A.", "given_names": "D. A.", "surname": "Davies", "position": "Chief Sorter", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 90},
    {"name": "V. E. George", "canonical_name": "George, V. E.", "given_names": "V. E.", "surname": "George", "position": "2nd Sorter", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "E. B. Campbell", "canonical_name": "Campbell, E. B.", "given_names": "E. B.", "surname": "Campbell", "position": "3rd Sorter", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "J. N. Taylor", "canonical_name": "Taylor, J. N.", "given_names": "J. N.", "surname": "Taylor", "position": "4th Sorter", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "H. L. Webber", "canonical_name": "Webber, H. L.", "given_names": "H. L.", "surname": "Webber", "position": "Mail Clerk", "department": "Post Office - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. Smythe", "canonical_name": "Smythe, J.", "given_names": "J.", "surname": "Smythe", "position": "Postmaster, Sherbro", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 120, "acting_status": "Acting", "location": "Sherbro"},
    {"name": "J. S. Coker", "canonical_name": "Coker, J. S.", "given_names": "J. S.", "surname": "Coker", "position": "Clerk to Postmaster", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 40, "location": "Sherbro"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()