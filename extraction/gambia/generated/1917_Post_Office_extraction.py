"""
Gambia Colonial Office List 1917 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1917

OFFICIALS = [
    {"name": "The Receiver-General", "canonical_name": "Receiver-General, The", "surname": "Receiver-General", "position": "Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "The Assistant Receiver-General", "canonical_name": "Assistant Receiver-General, The", "surname": "Assistant Receiver-General", "position": "Assistant Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "T. B. Williams", "canonical_name": "Williams, T. B.", "given_names": "T. B.", "surname": "Williams", "position": "Postmaster", "department": "Post Office - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. A. Mahoney", "canonical_name": "Mahoney, J. A.", "given_names": "J. A.", "surname": "Mahoney", "position": "2nd Grade Clerk", "department": "Post Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "C. M. Savage", "canonical_name": "Savage, C. M.", "given_names": "C. M.", "surname": "Savage", "position": "3rd Clerk", "department": "Post Office - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "4th Clerk", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "J. B. C. Artley", "canonical_name": "Artley, J. B. C.", "given_names": "J. B. C.", "surname": "Artley", "position": "5th Clerk", "department": "Post Office - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "F. D. Forbes", "canonical_name": "Forbes, F. D.", "given_names": "F. D.", "surname": "Forbes", "position": "6th Grade Clerks", "department": "Post Office - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "E. Huggins", "canonical_name": "Huggins, E.", "given_names": "E.", "surname": "Huggins", "position": "6th Grade Clerks", "department": "Post Office - Gambia", "salary_min": 30, "salary_max": 40},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()