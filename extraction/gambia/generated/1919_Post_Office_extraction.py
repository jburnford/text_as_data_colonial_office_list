"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "The Receiver-General", "canonical_name": "Receiver-General, The", "surname": "Receiver-General", "position": "Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "The Assistant Receiver-General", "canonical_name": "Assistant Receiver-General, The", "surname": "Assistant Receiver-General", "position": "Assistant Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "T. B. Williams", "canonical_name": "Williams, T. B.", "given_names": "T. B.", "surname": "Williams", "position": "Postmaster", "department": "Post Office - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "S. E. Johnson", "canonical_name": "Johnson, S. E.", "given_names": "S. E.", "surname": "Johnson", "position": "2nd Grade Clerk", "department": "Post Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "M. E. Grant", "canonical_name": "Grant, M. E.", "given_names": "M. E.", "surname": "Grant", "position": "3rd Clerk", "department": "Post Office - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "J. N. Savage", "canonical_name": "Savage, J. N.", "given_names": "J. N.", "surname": "Savage", "position": "3rd Clerk", "department": "Post Office - Gambia", "salary_min": 75, "salary_max": 100},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()