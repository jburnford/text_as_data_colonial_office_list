"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "S. B. Haffner", "canonical_name": "Haffner, S. B.", "given_names": "S. B.", "surname": "Haffner", "position": "Chief Printer", "department": "Printing Branch - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "Chief Compositor", "department": "Printing Branch - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "M. C. Johnson", "canonical_name": "Johnson, M. C.", "given_names": "M. C.", "surname": "Johnson", "position": "1st Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 60, "salary_max": 75},
    {"name": "O. D. Cummings", "canonical_name": "Cummings, O. D.", "given_names": "O. D.", "surname": "Cummings", "position": "1st Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 60, "salary_max": 75},
    {"name": "V. A. John", "canonical_name": "John, V. A.", "given_names": "V. A.", "surname": "John", "position": "2nd Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "R. J. Williams", "canonical_name": "Williams, R. J.", "given_names": "R. J.", "surname": "Williams", "position": "2nd Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "E. See", "canonical_name": "See, E.", "given_names": "E.", "surname": "See", "position": "3rd Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "J. Brown", "canonical_name": "Brown, J.", "given_names": "J.", "surname": "Brown", "position": "3rd Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "V. Davies", "canonical_name": "Davies, V.", "given_names": "V.", "surname": "Davies", "position": "3rd Class Compositor", "department": "Printing Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "C. Gwyn", "canonical_name": "Gwyn, C.", "given_names": "C.", "surname": "Gwyn", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 500, "salary_max": 600, "duty_allowance": 100, "allowances": "30l. as Chairman of Navigation and Pilotage Board."},
    {"name": "J. Iles Lauder", "canonical_name": "Lauder, J. Iles", "given_names": "J. Iles", "surname": "Lauder", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "B. P. E. Bulstrode", "canonical_name": "Bulstrode, B. P. E.", "given_names": "B. P. E.", "surname": "Bulstrode", "position": "Assistant Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "A. H. Jones", "canonical_name": "Jones, A. H.", "given_names": "A. H.", "surname": "Jones", "position": "4th Grade Clerk", "department": "Receiver-General's Department - Gambia", "salary_min": 50, "salary_max": 70},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()