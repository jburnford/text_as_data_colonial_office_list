"""
Gambia Colonial Office List 1921 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1921

OFFICIALS = [
    {"name": "The Receiver-General", "canonical_name": "Receiver-General, The", "surname": "Receiver-General", "position": "Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "The Assistant Receiver-General", "canonical_name": "Assistant Receiver-General, The", "surname": "Assistant Receiver-General", "position": "Assistant Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "J. O. Nicolls", "canonical_name": "Nicolls, J. O.", "given_names": "J. O.", "surname": "Nicolls", "position": "Postmaster", "department": "Post Office - Gambia", "salary_min": 180, "salary_max": 230},
    {"name": "S. E. Johnson", "canonical_name": "Johnson, S. E.", "given_names": "S. E.", "surname": "Johnson", "position": "2nd Grade Clerk", "department": "Post Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "A. J. Momoh", "canonical_name": "Momoh, A. J.", "given_names": "A. J.", "surname": "Momoh", "position": "2nd Grade Clerk", "department": "Post Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. N. Jones", "canonical_name": "Jones, J. N.", "given_names": "J. N.", "surname": "Jones", "position": "2nd Grade Clerk", "department": "Post Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "E. A. Jones", "canonical_name": "Jones, E. A.", "given_names": "E. A.", "surname": "Jones", "position": "2nd Grade Clerk", "department": "Post Office - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. B. George", "canonical_name": "George, J. B.", "given_names": "J. B.", "surname": "George", "position": "3rd Grade Clerk", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 80}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()