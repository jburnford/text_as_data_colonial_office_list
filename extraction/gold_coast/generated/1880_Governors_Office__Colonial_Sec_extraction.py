"""
Gold Coast Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1880

OFFICIALS = [
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "First Clerk", "department": "Governor's Office - Gold Coast", "salary_min": 120, "salary_max": 120},
    {"name": "A. J. Quansah", "canonical_name": "Quansah, A. J.", "given_names": "A. J.", "surname": "Quansah", "position": "Second Clerk", "department": "Governor's Office - Gold Coast", "salary_min": 100, "salary_max": 100},
    {"name": "C. W. Badger", "canonical_name": "Badger, C. W.", "given_names": "C. W.", "surname": "Badger", "position": "Third Clerk and Interpreter", "department": "Governor's Office - Gold Coast", "salary_min": 50, "salary_max": 50},
    {"name": "Quamina Agill", "canonical_name": "Agill, Quamina", "given_names": "Quamina", "surname": "Agill", "position": "Office Messenger", "department": "Governor's Office - Gold Coast", "salary_min": 24, "salary_max": 24},
    {"name": "Capt. O. A. Moloney", "canonical_name": "Moloney, O. A.", "given_names": "O. A.", "surname": "Moloney", "position": "Colonial Secretary", "department": "Colonial Secretariat - Gold Coast", "salary_min": 1000, "salary_max": 1000, "military_rank": "Captain", "allowances": "Free quarters."},
    {"name": "J. S. Hay", "canonical_name": "Hay, J. S.", "given_names": "J. S.", "surname": "Hay", "position": "Assistant Colonial Secretary", "department": "Colonial Secretariat - Gold Coast", "salary_min": 700, "salary_max": 700, "allowances": "\" "},
    {"name": "Jacob Simons", "canonical_name": "Simons, Jacob", "given_names": "Jacob", "surname": "Simons", "position": "Chief Clerk", "department": "Colonial Secretariat - Gold Coast", "salary_min": 200, "salary_max": 200, "allowances": "\" "},
    {"name": "J. T. Ribiero", "canonical_name": "Ribiero, J. T.", "given_names": "J. T.", "surname": "Ribiero", "position": "Second Clerk", "department": "Colonial Secretariat - Gold Coast", "salary_min": 100, "salary_max": 100, "allowances": "\" "},
    {"name": "J. P. Huydecoper", "canonical_name": "Huydecoper, J. P.", "given_names": "J. P.", "surname": "Huydecoper", "position": "Third Clerk", "department": "Colonial Secretariat - Gold Coast", "salary_min": 60, "salary_max": 60, "allowances": "\" "},
    {"name": "T. King", "canonical_name": "King, T.", "given_names": "T.", "surname": "King", "position": "Messenger", "department": "Colonial Secretariat - Gold Coast", "salary_min": 12, "salary_max": 12, "allowances": "\" "}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()