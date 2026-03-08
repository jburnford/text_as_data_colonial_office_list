"""
Gambia Colonial Office List 1912 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1912

OFFICIALS = [
    {"name": "A. K. Lewis", "canonical_name": "Lewis, A. K.", "given_names": "A. K.", "surname": "Lewis", "position": "Assistant Postmaster", "department": "Post Office - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "T. B. Williams", "canonical_name": "Williams, T. B.", "given_names": "T. B.", "surname": "Williams", "position": "Chief Clerk", "department": "Post Office - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "J. J. Fowlis", "canonical_name": "Fowlis, J. J.", "given_names": "J. J.", "surname": "Fowlis", "position": "District Postmaster", "department": "Post Office - Gambia", "location": "MacCarthy Island", "salary_min": 75, "salary_max": 100},
    {"name": "C. M. Savage", "canonical_name": "Savage, C. M.", "given_names": "C. M.", "surname": "Savage", "position": "1st Clerk", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 75},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "2nd Clerk", "department": "Post Office - Gambia", "salary_min": 36, "salary_max": 48},
    {"name": "J. S. Lusack", "canonical_name": "Lusack, J. S.", "given_names": "J. S.", "surname": "Lusack", "position": "3rd Clerks", "department": "Post Office - Gambia", "salary_min": 24, "salary_max": 36},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "3rd Clerks", "department": "Post Office - Gambia", "salary_min": 24, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()