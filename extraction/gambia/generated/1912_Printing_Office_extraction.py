"""
Gambia Colonial Office List 1912 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1912

OFFICIALS = [
    {"name": "N. E. Williams", "canonical_name": "Williams, N. E.", "given_names": "N. E.", "surname": "Williams", "position": "Government Printer", "department": "Printing Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "1st Class Compositor", "department": "Printing Office - Gambia", "salary_min": 60, "salary_max": 70},
    {"name": "O. G. Palmer", "canonical_name": "Palmer, O. G.", "given_names": "O. G.", "surname": "Palmer", "position": "2nd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "S. T. Darboe", "canonical_name": "Darboe, S. T.", "given_names": "S. T.", "surname": "Darboe", "position": "2nd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "C. W. Coker", "canonical_name": "Coker, C. W.", "given_names": "C. W.", "surname": "Coker", "position": "3rd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 24, "salary_max": 30},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()