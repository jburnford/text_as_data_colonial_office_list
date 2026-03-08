"""
Sierra Leone Colonial Office List 1912 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1912

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Colonial Postmaster-General and Manager Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 450, "salary_max": 450, "duty_allowance": 90},
    {"name": "J. S. T. Davies", "canonical_name": "Davies, J. S. T.", "given_names": "J. S. T.", "surname": "Davies", "position": "Assistant Colonial Postmaster-General and Chief Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. N. Crown", "canonical_name": "Crown, J. N.", "given_names": "J. N.", "surname": "Crown", "position": "Chief Clerk and Examiner", "department": "Post Office - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "Assistant Clerk and Examiner", "department": "Post Office - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "D. T. P. Cole", "canonical_name": "Cole, D. T. P.", "given_names": "D. T. P.", "surname": "Cole", "position": "Accountant", "department": "Post Office - Sierra Leone", "salary_min": 150, "salary_max": 200, "allowances": "24l. allowance"},
    {"name": "I. J. Baxter", "canonical_name": "Baxter, I. J.", "given_names": "I. J.", "surname": "Baxter", "position": "Money Order Clerk", "department": "Post Office - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "A. B. Harleston", "canonical_name": "Harleston, A. B.", "given_names": "A. B.", "surname": "Harleston", "position": "1st Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "M. A. John", "canonical_name": "John, M. A.", "given_names": "M. A.", "surname": "John", "position": "Senior Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. T. Nottidge", "canonical_name": "Nottidge, J. T.", "given_names": "J. T.", "surname": "Nottidge", "position": "Registration Clerk", "department": "Post Office - Sierra Leone", "salary_min": 70, "salary_max": 80},
    {"name": "J. O. Nicolls", "canonical_name": "Nicolls, J. O.", "given_names": "J. O.", "surname": "Nicolls", "position": "Assistant Accountant", "department": "Post Office - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "A. P. King", "canonical_name": "King, A. P.", "given_names": "A. P.", "surname": "King", "position": "Stampseller", "department": "Post Office - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "W. E. J. Corkson", "canonical_name": "Corkson, W. E. J.", "given_names": "W. E. J.", "surname": "Corkson", "position": "Mail Clerk", "department": "Post Office - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. Smythe", "canonical_name": "Smythe, J.", "given_names": "J.", "surname": "Smythe", "position": "Postmaster and Savings Bank Clerk", "department": "Post Office - Sierra Leone", "location": "Sherbro", "salary_min": 120, "salary_max": 150},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()