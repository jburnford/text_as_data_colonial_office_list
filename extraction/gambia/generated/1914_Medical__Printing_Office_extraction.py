"""
Gambia Colonial Office List 1914 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1914

OFFICIALS = [
    {"name": "E. A. Chartres", "canonical_name": "Chartres, E. A.", "given_names": "E. A.", "surname": "Chartres", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "J. A. Harley", "canonical_name": "Harley, J. A.", "given_names": "J. A.", "surname": "Harley", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500, "per_diem": "2s. 3d."},
    {"name": "A. F. Kennedy", "canonical_name": "Kennedy, A. F.", "given_names": "A. F.", "surname": "Kennedy", "position": "Medical Officer of Health", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500, "per_diem": "2s. 3d."},
    {"name": "F. C. V. Thompson", "canonical_name": "Thompson, F. C. V.", "given_names": "F. C. V.", "surname": "Thompson", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500, "per_diem": "2s. 3d."},
    {"name": "S. L. Brohier", "canonical_name": "Brohier, S. L.", "given_names": "S. L.", "surname": "Brohier", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500, "per_diem": "2s. 3d."},
    {"name": "J. F. Johnson", "canonical_name": "Johnson, J. F.", "given_names": "J. F.", "surname": "Johnson", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 130},
    {"name": "Colin Shaw", "canonical_name": "Shaw, Colin", "given_names": "Colin", "surname": "Shaw", "position": "Clerk", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 120},
    {"name": "N. E. Williams", "canonical_name": "Williams, N. E.", "given_names": "N. E.", "surname": "Williams", "position": "Government Printer", "department": "Printing Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "1st Class Compositor", "department": "Printing Office - Gambia", "salary_min": 60, "salary_max": 70},
    {"name": "S. T. Darboe", "canonical_name": "Darboe, S. T.", "given_names": "S. T.", "surname": "Darboe", "position": "1st Class Compositor", "department": "Printing Office - Gambia", "salary_min": 60, "salary_max": 70},
    {"name": "V. M. King", "canonical_name": "King, V. M.", "given_names": "V. M.", "surname": "King", "position": "2nd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "C. W. Coker", "canonical_name": "Coker, C. W.", "given_names": "C. W.", "surname": "Coker", "position": "3rd Class Composer", "department": "Printing Office - Gambia", "salary_min": 24, "salary_max": 30},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()