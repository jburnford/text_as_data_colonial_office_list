"""
Sierra Leone Colonial Office List 1898 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1898

OFFICIALS = [
    {"name": "J. Cleugh", "canonical_name": "Cleugh, J.", "given_names": "J.", "surname": "Cleugh", "position": "Postmaster-General", "department": "Post Office Department - Sierra Leone", "salary_min": 350, "salary_max": 400, "allowances": "rent alike. 40l. per ann."},
    {"name": "J. C. Smith", "canonical_name": "Smith, J. C.", "given_names": "J. C.", "surname": "Smith", "position": "Assistant Postmaster-General", "department": "Post Office Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. S. T. Davies", "canonical_name": "Davies, J. S. T.", "given_names": "J. S. T.", "surname": "Davies", "position": "Chief Clerk and Examiner", "department": "Post Office Department - Sierra Leone", "salary_min": 110, "salary_max": 150},
    {"name": "J. N. Crown", "canonical_name": "Crown, J. N.", "given_names": "J. N.", "surname": "Crown", "position": "2nd Clerk and Accountant", "department": "Post Office Department - Sierra Leone", "salary_min": 90, "salary_max": 120},
    {"name": "D. T. P. Cole", "canonical_name": "Cole, D. T. P.", "given_names": "D. T. P.", "surname": "Cole", "position": "3rd Clerk and Money Order Clerk", "department": "Post Office Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "First Sorter", "department": "Post Office Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "Daniel Carroll", "canonical_name": "Carroll, Daniel", "given_names": "Daniel", "surname": "Carroll", "position": "Stampseller", "department": "Post Office Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "I. J. Baxter", "canonical_name": "Baxter, I. J.", "given_names": "I. J.", "surname": "Baxter", "position": "Parcel Post Clerk", "department": "Post Office Department - Sierra Leone", "salary_min": 43, "salary_max": 50},
    {"name": "H. R. Williams", "canonical_name": "Williams, H. R.", "given_names": "H. R.", "surname": "Williams", "position": "Postmaster", "department": "Post Office Department - Sierra Leone", "location": "Sherbro", "salary_min": 120, "salary_max": 120}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()