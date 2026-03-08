"""
Gambia Colonial Office List 1908 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1908

OFFICIALS = [
    {"name": "Thomas Hood", "canonical_name": "Hood, Thomas", "given_names": "Thomas", "surname": "Hood", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 600, "salary_max": 700},
    {"name": "F. J. A. Baldwin", "canonical_name": "Baldwin, F. J. A.", "given_names": "F. J. A.", "surname": "Baldwin", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "J. C. Franklin", "canonical_name": "Franklin, J. C.", "given_names": "J. C.", "surname": "Franklin", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500, "honors": ["D.S.O."]},
    {"name": "W. S. Smart", "canonical_name": "Smart, W. S.", "given_names": "W. S.", "surname": "Smart", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 100, "salary_max": 130},
    {"name": "L. G. Boyle", "canonical_name": "Boyle, L. G.", "given_names": "L. G.", "surname": "Boyle", "position": "Assistant Dispenser", "department": "Medical - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "Colin Shaw", "canonical_name": "Shaw, Colin", "given_names": "Colin", "surname": "Shaw", "position": "Clerk", "department": "Medical - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "N. E. Williams", "canonical_name": "Williams, N. E.", "given_names": "N. E.", "surname": "Williams", "position": "Government Printer", "department": "Printing Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "1st Class Compositor", "department": "Printing Office - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "J. F. Marong", "canonical_name": "Marong, J. F.", "given_names": "J. F.", "surname": "Marong", "position": "2nd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "O. G. Palmer", "canonical_name": "Palmer, O. G.", "given_names": "O. G.", "surname": "Palmer", "position": "3rd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "S. T. Darboe", "canonical_name": "Darboe, S. T.", "given_names": "S. T.", "surname": "Darboe", "position": "3rd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 24, "salary_max": 30}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()