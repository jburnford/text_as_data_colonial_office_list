"""
Gambia Colonial Office List 1913 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1913

OFFICIALS = [
    {"name": "The Receiver-General", "canonical_name": "Receiver-General, The", "surname": "Receiver-General", "position": "Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "The Assistant Receiver-General", "canonical_name": "Assistant Receiver-General, The", "surname": "Assistant Receiver-General", "position": "Assistant Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "T. B. Williams", "canonical_name": "Williams, T. B.", "given_names": "T. B.", "surname": "Williams", "position": "Postmaster", "department": "Post Office - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "J. A. Mahoney", "canonical_name": "Mahoney, J. A.", "given_names": "J. A.", "surname": "Mahoney", "position": "Chief Clerk", "department": "Post Office - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "C. M. Savage", "canonical_name": "Savage, C. M.", "given_names": "C. M.", "surname": "Savage", "position": "1st Clerk", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 75},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "2nd Clerk", "department": "Post Office - Gambia", "salary_min": 36, "salary_max": 48},
    {"name": "J. S. Lussack", "canonical_name": "Lussack, J. S.", "given_names": "J. S.", "surname": "Lussack", "position": "3rd Clerk", "department": "Post Office - Gambia", "salary_min": 24, "salary_max": 36},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "3rd Clerk", "department": "Post Office - Gambia", "salary_min": 24, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()