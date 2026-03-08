"""
Gambia Colonial Office List 1910 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1910

OFFICIALS = [
    {"name": "The Treasurer", "canonical_name": "Treasurer, The", "surname": "Treasurer", "position": "Postmaster", "department": "Post Office - Gambia"},
    {"name": "A. K. Lewis", "canonical_name": "Lewis, A. K.", "given_names": "A. K.", "surname": "Lewis", "position": "Assistant Postmaster", "department": "Post Office - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "I. G. McCarthy", "canonical_name": "McCarthy, I. G.", "given_names": "I. G.", "surname": "McCarthy", "position": "Chief Clerk", "department": "Post Office - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "C. M. Savage", "canonical_name": "Savage, C. M.", "given_names": "C. M.", "surname": "Savage", "position": "1st Clerk", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 75},
    {"name": "Thos. Williams", "canonical_name": "Williams, Thos.", "given_names": "Thos.", "surname": "Williams", "position": "2nd Clerk", "department": "Post Office - Gambia", "salary_min": 38, "salary_max": 48},
    {"name": "T. King", "canonical_name": "King, T.", "given_names": "T.", "surname": "King", "position": "3rd Clerk", "department": "Post Office - Gambia", "salary_min": 24, "salary_max": 36},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()