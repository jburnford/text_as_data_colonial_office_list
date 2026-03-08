"""
Gambia Colonial Office List 1928 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1928

OFFICIALS = [
    {"name": "S. Bach", "canonical_name": "Bach, S.", "surname": "Bach", "position": "Government Printer", "department": "Printing Office - Gambia", "salary_min": 500, "salary_max": 600},
    {"name": "J. J. McHugh", "canonical_name": "McHugh, J. J.", "surname": "McHugh", "position": "Foreman Compositor", "department": "Printing Office - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "V. F. Lobendahn", "canonical_name": "Lobendahn, V. F.", "surname": "Lobendahn", "position": "Compositor", "department": "Printing Office - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "J. W. Dewhirst", "canonical_name": "Dewhirst, J. W.", "surname": "Dewhirst", "position": "Compositor", "department": "Printing Office - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "L. L. Ryland", "canonical_name": "Ryland, L. L.", "surname": "Ryland", "position": "Compositor", "department": "Printing Office - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "G. W. Cockburn", "canonical_name": "Cockburn, G. W.", "surname": "Cockburn", "position": "Compositor", "department": "Printing Office - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "D. T. Sale", "canonical_name": "Sale, D. T.", "surname": "Sale", "position": "Compositor", "department": "Printing Office - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "Dwarka Singh", "canonical_name": "Singh, Dwarka", "surname": "Singh", "position": "Compositor", "department": "Printing Office - Gambia", "salary_min": 200, "salary_max": 250},
    {"name": "R. Campbell", "canonical_name": "Campbell, R.", "surname": "Campbell", "position": "Bookbinder", "department": "Printing Office - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "L. Cox", "canonical_name": "Cox, L.", "surname": "Cox", "position": "Machinist", "department": "Printing Office - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "L. L. Hulek", "canonical_name": "Hulek, L. L.", "surname": "Hulek", "position": "Third Class Clerk", "department": "Printing Office - Gambia", "salary_min": 150, "salary_max": 270},
    {"name": "E. I. March", "canonical_name": "March, E. I.", "surname": "March", "position": "Government Storekeeper", "department": "Stores Department - Gambia"},
    {"name": "F. W. J. Plucknett", "canonical_name": "Plucknett, F. W. J.", "surname": "Plucknett", "position": "First Class Clerk", "department": "Stores Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "H. J. Hulek", "canonical_name": "Hulek, H. J.", "surname": "Hulek", "position": "Second Class Clerk", "department": "Stores Department - Gambia", "salary_min": 270, "salary_max": 400},
    {"name": "L. B. Benjamin", "canonical_name": "Benjamin, L. B.", "surname": "Benjamin", "position": "Third Class Clerk", "department": "Stores Department - Gambia", "salary_min": 150, "salary_max": 270},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()