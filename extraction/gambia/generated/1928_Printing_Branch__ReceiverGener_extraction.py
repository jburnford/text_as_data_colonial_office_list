"""
Gambia Colonial Office List 1928 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1928

OFFICIALS = [
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "Chief Printer", "department": "Printing Branch - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "H. Densham Smith", "canonical_name": "Smith, H. Densham", "given_names": "H. Densham", "surname": "Smith", "position": "Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "Captain W. H. Eccles", "canonical_name": "Eccles, W. H.", "given_names": "W. H.", "surname": "Eccles", "position": "Assistants Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 720, "military_rank": "Captain"},
    {"name": "F. A. Mathias", "canonical_name": "Mathias, F. A.", "given_names": "F. A.", "surname": "Mathias", "position": "Assistants Receiver-General", "department": "Receiver-General's Department - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "F. D. MacPhail", "canonical_name": "MacPhail, F. D.", "given_names": "F. D.", "surname": "MacPhail", "position": "Accountant", "department": "Treasury Branch - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "Chief Clerk", "department": "Treasury Branch - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "E. G. C. Gabbidon", "canonical_name": "Gabbidon, E. G. C.", "given_names": "E. G. C.", "surname": "Gabbidon", "position": "Cashier", "department": "Treasury Branch - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "D. T. Taylor", "canonical_name": "Taylor, D. T.", "given_names": "D. T.", "surname": "Taylor", "position": "2nd Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "E. W. Carrol", "canonical_name": "Carrol, E. W.", "given_names": "E. W.", "surname": "Carrol", "position": "2nd Grade Clerks", "department": "Treasury Branch - Gambia", "salary_min": 160, "salary_max": 230},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()