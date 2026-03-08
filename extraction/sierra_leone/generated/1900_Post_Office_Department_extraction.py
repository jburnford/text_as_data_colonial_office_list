"""
Sierra Leone Colonial Office List 1900 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1900

OFFICIALS = [
    {"name": "J. Cleugh", "canonical_name": "Cleugh, J.", "given_names": "J.", "surname": "Cleugh", "position": "Postmaster-General", "department": "Post Office Department - Sierra Leone", "salary_min": 350, "salary_max": 400, "allowances": "rent alluce, 40l. per ann."},
    {"name": "J. C. Smith", "canonical_name": "Smith, J. C.", "given_names": "J. C.", "surname": "Smith", "position": "Assistant Postmaster-General", "department": "Post Office Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. S. T. Davies", "canonical_name": "Davies, J. S. T.", "given_names": "J. S. T.", "surname": "Davies", "position": "Chief Clerk and Examiner", "department": "Post Office Department - Sierra Leone", "salary_min": 110, "salary_max": 150},
    {"name": "J. N. Crown", "canonical_name": "Crown, J. N.", "given_names": "J. N.", "surname": "Crown", "position": "2nd Clerk and Accountant", "department": "Post Office Department - Sierra Leone", "salary_min": 90, "salary_max": 120},
    {"name": "D. T. P. Cole", "canonical_name": "Cole, D. T. P.", "given_names": "D. T. P.", "surname": "Cole", "position": "3rd Clerk and Money Order Clerk", "department": "Post Office Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "K. D. Williams", "canonical_name": "Williams, K. D.", "given_names": "K. D.", "surname": "Williams", "position": "Assistant Money Order Clerk", "department": "Post Office Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "M. S. Macquarie", "canonical_name": "Macquarie, M. S.", "given_names": "M. S.", "surname": "Macquarie", "position": "First Sorter", "department": "Post Office Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "D. A. Davies", "canonical_name": "Davies, D. A.", "given_names": "D. A.", "surname": "Davies", "position": "Stampseller", "department": "Post Office Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. J. Baxter", "canonical_name": "Baxter, J. J.", "given_names": "J. J.", "surname": "Baxter", "position": "Parcel Post Clerk", "department": "Post Office Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Daniel Carroll", "canonical_name": "Carroll, Daniel", "given_names": "Daniel", "surname": "Carroll", "position": "Postmaster", "department": "Post Office Department - Sierra Leone", "salary_min": 100, "salary_max": 120, "location": "Sherbro"},
    {"name": "T. S. Wilson", "canonical_name": "Wilson, T. S.", "given_names": "T. S.", "surname": "Wilson", "position": "Registration Clerk", "department": "Post Office Department - Sierra Leone", "salary_min": 44, "salary_max": 44},
    {"name": "C. Leigh", "canonical_name": "Leigh, C.", "given_names": "C.", "surname": "Leigh", "position": "Corresponding Clerk", "department": "Post Office Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. B. Augustine", "canonical_name": "Augustine, J. B.", "given_names": "J. B.", "surname": "Augustine", "position": "2nd Sorter", "department": "Post Office Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. N. Whitfield", "canonical_name": "Whitfield, J. N.", "given_names": "J. N.", "surname": "Whitfield", "position": "3rd Sorter", "department": "Post Office Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "S. H. E. Baker", "canonical_name": "Baker, S. H. E.", "given_names": "S. H. E.", "surname": "Baker", "position": "4th Sorter", "department": "Post Office Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "D. John", "canonical_name": "John, D.", "given_names": "D.", "surname": "John", "position": "5th Sorter", "department": "Post Office Department - Sierra Leone", "salary_min": 24, "salary_max": 30}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()