"""
Gambia Colonial Office List 1906 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1906

OFFICIALS = [
    {"name": "R. M. Forde", "canonical_name": "Forde, R. M.", "given_names": "R. M.", "surname": "Forde", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 600, "salary_max": 700},
    {"name": "F. J. A. Baldwin", "canonical_name": "Baldwin, F. J. A.", "given_names": "F. J. A.", "surname": "Baldwin", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "J. C. Franklin", "canonical_name": "Franklin, J. C.", "given_names": "J. C.", "surname": "Franklin", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 400, "salary_max": 500, "honors": ["D.S.O."]},
    {"name": "W. S. Smart", "canonical_name": "Smart, W. S.", "given_names": "W. S.", "surname": "Smart", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 75, "salary_max": 85},
    {"name": "F. G. Manly", "canonical_name": "Manly, F. G.", "given_names": "F. G.", "surname": "Manly", "position": "Assistant Dispenser", "department": "Medical - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "Colin Shaw", "canonical_name": "Shaw, Colin", "given_names": "Colin", "surname": "Shaw", "position": "Clerk", "department": "Medical - Gambia", "salary_min": 70, "salary_max": 80},
    {"name": "N. E. Williams", "canonical_name": "Williams, N. E.", "given_names": "N. E.", "surname": "Williams", "position": "Government Printer", "department": "Printing Office - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "1st Class Compositor", "department": "Printing Office - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "E. I. D. John", "canonical_name": "John, E. I. D.", "given_names": "E. I. D.", "surname": "John", "position": "2nd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "O. G. Palmer", "canonical_name": "Palmer, O. G.", "given_names": "O. G.", "surname": "Palmer", "position": "3rd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "S. T. Darboe", "canonical_name": "Darboe, S. T.", "given_names": "S. T.", "surname": "Darboe", "position": "3rd Class Compositor", "department": "Printing Office - Gambia", "salary_min": 24, "salary_max": 30},
    {"name": "E. Vaughan", "canonical_name": "Vaughan, E.", "given_names": "E.", "surname": "Vaughan", "position": "Colonial Engineer", "department": "Colonial Engineer's Department - Gambia", "salary_min": 450, "salary_max": 450, "duty_allowance": 90},
    {"name": "W. Pickering", "canonical_name": "Pickering, W.", "given_names": "W.", "surname": "Pickering", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "F. W. Mead", "canonical_name": "Mead, F. W.", "given_names": "F. W.", "surname": "Mead", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "G. M. N'Jie", "canonical_name": "N'Jie, G. M.", "given_names": "G. M.", "surname": "N'Jie", "position": "Foreman of Works", "department": "Colonial Engineer's Department - Gambia", "salary_min": 120, "salary_max": 150},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Accountant", "department": "Colonial Engineer's Department - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "John C. Fye", "canonical_name": "Fye, John C.", "given_names": "John C.", "surname": "Fye", "position": "Storekeeper", "department": "Colonial Engineer's Department - Gambia", "salary_min": 60, "salary_max": 100},
    {"name": "R. Rendall", "canonical_name": "Rendall, R.", "given_names": "R.", "surname": "Rendall", "position": "Assistant Timekeeper and Clerk", "department": "Colonial Engineer's Department - Gambia", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()