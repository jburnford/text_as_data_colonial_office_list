"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "M. McAffe", "canonical_name": "McAffe, M.", "given_names": "M.", "surname": "McAffe", "position": "Chief Engineer and Master", "department": "Government Vessels - Gambia", "salary_min": 300, "salary_max": 360, "duty_allowance": 50, "allowances": "50l. messing allowance"},
    {"name": "P. F. Munn", "canonical_name": "Munn, P. F.", "given_names": "P. F.", "surname": "Munn", "position": "Second Engineer", "department": "Government Vessels - Gambia", "salary_min": 200, "salary_max": 250, "allowances": "50l. messing allowance"},
    {"name": "The Receiver-General", "canonical_name": "Receiver-General, The", "surname": "Receiver-General", "position": "Postmaster-General", "department": "Post Office - Gambia"},
    {"name": "The Assistant Receiver-General", "canonical_name": "Assistant Receiver-General, The", "surname": "Assistant Receiver-General", "position": "Assistant Postmaster", "department": "Post Office - Gambia"},
    {"name": "T. B. Williams", "canonical_name": "Williams, T. B.", "given_names": "T. B.", "surname": "Williams", "position": "Postmaster", "department": "Post Office - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. A. Mahoney", "canonical_name": "Mahoney, J. A.", "given_names": "J. A.", "surname": "Mahoney", "position": "2nd Grade Clerk", "department": "Post Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "C. M. Savage", "canonical_name": "Savage, C. M.", "given_names": "C. M.", "surname": "Savage", "position": "3rd Clerk", "department": "Post Office - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "4th Clerk", "department": "Post Office - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "J. N. Savage", "canonical_name": "Savage, J. N.", "given_names": "J. N.", "surname": "Savage", "position": "5th Clerk", "department": "Post Office - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "J. B. Artley", "canonical_name": "Artley, J. B.", "given_names": "J. B.", "surname": "Artley", "position": "6th Grade Clerk", "department": "Post Office - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "F. D. Forbes", "canonical_name": "Forbes, F. D.", "given_names": "F. D.", "surname": "Forbes", "position": "6th Grade Clerk", "department": "Post Office - Gambia", "salary_min": 30, "salary_max": 40}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()