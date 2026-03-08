"""
Gambia Colonial Office List 1909 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1909

OFFICIALS = [
    {"name": "M. McAffter", "canonical_name": "McAffter, M.", "given_names": "M.", "surname": "McAffter", "position": "Chief Engineer and Master", "department": "Government Vessels - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "50l. allowance"},
    {"name": "T. W. Hart", "canonical_name": "Hart, T. W.", "given_names": "T. W.", "surname": "Hart", "position": "Second Engineer", "department": "Government Vessels - Gambia", "salary_min": 225, "salary_max": 250, "allowances": "50l. allowance"},
    {"name": "Henry Venn", "canonical_name": "Venn, Henry", "given_names": "Henry", "surname": "Venn", "position": "Purser", "department": "Government Vessels - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "The Treasurer", "canonical_name": "Treasurer, The", "surname": "Treasurer", "position": "Postmaster", "department": "Post Office - Gambia"},
    {"name": "A. K. Lewis", "canonical_name": "Lewis, A. K.", "given_names": "A. K.", "surname": "Lewis", "position": "Assistant Postmaster", "department": "Post Office - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "I. G. McCarthy", "canonical_name": "McCarthy, I. G.", "given_names": "I. G.", "surname": "McCarthy", "position": "Chief Clerk", "department": "Post Office - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "C. M. Savage", "canonical_name": "Savage, C. M.", "given_names": "C. M.", "surname": "Savage", "position": "1st Clerk", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 75},
    {"name": "Thos. Williams", "canonical_name": "Williams, Thomas", "given_names": "Thomas", "surname": "Williams", "position": "2nd Clerk", "department": "Post Office - Gambia", "salary_min": 36, "salary_max": 48},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "3rd Clerk", "department": "Post Office - Gambia", "salary_min": 24, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()