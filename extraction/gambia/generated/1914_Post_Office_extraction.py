"""
Gambia Colonial Office List 1914 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1914

OFFICIALS = [
    {"name": "The Receiver-General", "canonical_name": "Receiver-General, The", "surname": "Receiver-General", "position": "Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "The Assistant Receiver-General", "canonical_name": "Receiver-General, The Assistant", "surname": "Receiver-General", "position": "Assistant Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "T. B. Williams", "canonical_name": "Williams, T. B.", "given_names": "T. B.", "surname": "Williams", "position": "Postmaster", "department": "Post Office - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "J. A. Mahoney", "canonical_name": "Mahoney, J. A.", "given_names": "J. A.", "surname": "Mahoney", "position": "2nd Grade Clerk", "department": "Post Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "C. M. Savage", "canonical_name": "Savage, C. M.", "given_names": "C. M.", "surname": "Savage", "position": "3rd Clerk", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 75},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "6th Grade Clerk", "department": "Post Office - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "C. A. Hughes", "canonical_name": "Hughes, C. A.", "given_names": "C. A.", "surname": "Hughes", "position": "6th Grade Clerks", "department": "Post Office - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "T. W. Davies", "canonical_name": "Davies, T. W.", "given_names": "T. W.", "surname": "Davies", "position": "6th Grade Clerks", "department": "Post Office - Gambia", "salary_min": 30, "salary_max": 40},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()