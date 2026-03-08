"""
Sierra Leone Colonial Office List 1914 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1914

OFFICIALS = [
    {"name": "W. H. C. Calthrop", "canonical_name": "Calthrop, W. H. C.", "given_names": "W. H. C.", "surname": "Calthrop", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "military_rank": "Commander"},
    {"name": "U. J. Lawrence", "canonical_name": "Lawrence, U. J.", "given_names": "U. J.", "surname": "Lawrence", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "T. A. Moses", "canonical_name": "Moses, T. A.", "given_names": "T. A.", "surname": "Moses", "position": "Fifth Grade Clerk", "department": "Port and Marine Department - Sierra Leone", "salary_min": 50, "salary_max": 70},
    {"name": "H. T. March", "canonical_name": "March, H. T.", "given_names": "H. T.", "surname": "March", "position": "Colonial Postmaster-General and Manager Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "J. S. T. Davies", "canonical_name": "Davies, J. S. T.", "given_names": "J. S. T.", "surname": "Davies", "position": "Assistant Colonial Postmaster-General and Chief Clerk, Savings Bank", "department": "Post Office - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "N. S. Davis", "canonical_name": "Davis, N. S.", "given_names": "N. S.", "surname": "Davis", "position": "Accountant, Savings Bank, Post Office Department", "department": "Post Office - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. N. Crown", "canonical_name": "Crown, J. N.", "given_names": "J. N.", "surname": "Crown", "position": "Chief Clerk and Examiner", "department": "Post Office - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "D. T. P. Cole", "canonical_name": "Cole, D. T. P.", "given_names": "D. T. P.", "surname": "Cole", "position": "First Grade Clerk", "department": "Post Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "I. J. Baxter", "canonical_name": "Baxter, I. J.", "given_names": "I. J.", "surname": "Baxter", "position": "Second Clerk", "department": "Post Office - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "J. Smythe", "canonical_name": "Smythe, J.", "given_names": "J.", "surname": "Smythe", "position": "Second Clerk", "department": "Post Office - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "M. John", "canonical_name": "John, M.", "given_names": "M.", "surname": "John", "position": "Third Clerk", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "D. A. Davies", "canonical_name": "Davies, D. A.", "given_names": "D. A.", "surname": "Davies", "position": "Third Clerk", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 130},
    {"name": "V. E. George", "canonical_name": "George, V. E.", "given_names": "V. E.", "surname": "George", "position": "Third Clerk", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 130}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()