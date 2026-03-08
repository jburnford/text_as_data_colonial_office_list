"""
Gambia Colonial Office List 1913 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1913

OFFICIALS = [
    {"name": "E. A. Chartres", "canonical_name": "Chartres, E. A.", "given_names": "E. A.", "surname": "Chartres", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "J. C. Franklin", "canonical_name": "Franklin, J. C.", "given_names": "J. C.", "surname": "Franklin", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 500, "salary_max": 600},
    {"name": "J. A. Harley", "canonical_name": "Harley, J. A.", "given_names": "J. A.", "surname": "Harley", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "A. F. Kennedy", "canonical_name": "Kennedy, A. F.", "given_names": "A. F.", "surname": "Kennedy", "position": "Medical Officer of Health", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "F. C. V. Thompson", "canonical_name": "Thompson, F. C. V.", "given_names": "F. C. V.", "surname": "Thompson", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "W. S. Smart", "canonical_name": "Smart, W. S.", "given_names": "W. S.", "surname": "Smart", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 130},
    {"name": "J. F. Johnson", "canonical_name": "Johnson, J. F.", "given_names": "J. F.", "surname": "Johnson", "position": "Assistant Dispenser", "department": "Medical - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "J. S. Kennedy", "canonical_name": "Kennedy, J. S.", "given_names": "J. S.", "surname": "Kennedy", "position": "Assistant Dispenser", "department": "Medical - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "Colin Shaw", "canonical_name": "Shaw, Colin", "given_names": "Colin", "surname": "Shaw", "position": "Clerk", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 120},
    {"name": "E. W. Johns", "canonical_name": "Johns, E. W.", "given_names": "E. W.", "surname": "Johns", "position": "Assistant Clerk", "department": "Medical - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "N. E. Williams", "canonical_name": "Williams, N. E.", "given_names": "N. E.", "surname": "Williams", "position": "Government Printer", "department": "Printing Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "1st Class Compositor", "department": "Printing Office - Gambia", "salary_min": 60, "salary_max": 70},
    {"name": "S. T. Darboe", "canonical_name": "Darboe, S. T.", "given_names": "S. T.", "surname": "Darboe", "position": "2nd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "V. M. King", "canonical_name": "King, V. M.", "given_names": "V. M.", "surname": "King", "position": "2nd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "C. W. Coker", "canonical_name": "Coker, C. W.", "given_names": "C. W.", "surname": "Coker", "position": "3rd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 24, "salary_max": 30}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()