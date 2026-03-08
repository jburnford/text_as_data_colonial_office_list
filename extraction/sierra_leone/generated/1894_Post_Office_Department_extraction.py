"""
Sierra Leone Colonial Office List 1894 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1894

OFFICIALS = [
    {"name": "J. H. Spaine", "canonical_name": "Spaine, J. H.", "given_names": "J. H.", "surname": "Spaine", "position": "Colonial Postmaster", "department": "Post Office Department - Sierra Leone", "salary_min": 220, "salary_max": 220},
    {"name": "C. George", "canonical_name": "George, C.", "given_names": "C.", "surname": "George", "position": "Chief Clerk and Examiner", "department": "Post Office Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "I. S. Johnson", "canonical_name": "Johnson, I. S.", "given_names": "I. S.", "surname": "Johnson", "position": "2nd Clerk and Accountant", "department": "Post Office Department - Sierra Leone", "salary_min": 90, "salary_max": 90},
    {"name": "D. J. P. Cole", "canonical_name": "Cole, D. J. P.", "given_names": "D. J. P.", "surname": "Cole", "position": "3rd and Money Order Clerk", "department": "Post Office Department - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "J. A. W. Smith", "canonical_name": "Smith, J. A. W.", "given_names": "J. A. W.", "surname": "Smith", "position": "First Sorter", "department": "Post Office Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Daniel Carroll", "canonical_name": "Carroll, Daniel", "given_names": "Daniel", "surname": "Carroll", "position": "Stampeller", "department": "Post Office Department - Sierra Leone", "salary_min": 42, "salary_max": 42},
    {"name": "I. J. Baxter", "canonical_name": "Baxter, I. J.", "given_names": "I. J.", "surname": "Baxter", "position": "Parcel Post Clerk", "department": "Post Office Department - Sierra Leone", "salary_min": 43, "salary_max": 43},
    {"name": "H. R. Williams", "canonical_name": "Williams, H. R.", "given_names": "H. R.", "surname": "Williams", "position": "Postmaster", "department": "Post Office Department - Sierra Leone", "location": "Sherbro", "salary_min": 120, "salary_max": 120},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()