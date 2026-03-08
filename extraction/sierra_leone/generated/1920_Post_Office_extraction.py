"""
Sierra Leone Colonial Office List 1920 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1920

OFFICIALS = [
    {"name": "H. T. March", "canonical_name": "March, H. T.", "given_names": "H. T.", "surname": "March", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "N. S. Davis", "canonical_name": "Davis, N. S.", "given_names": "N. S.", "surname": "Davis", "position": "Accountant", "department": "Post Office - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Chief Clerk", "department": "Post Office - Sierra Leone", "salary_min": 200, "salary_max": 300},
    {"name": "J. Smythe", "canonical_name": "Smythe, J.", "given_names": "J.", "surname": "Smythe", "position": "First Grade Clerks", "department": "Post Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "M. A. John", "canonical_name": "John, M. A.", "given_names": "M. A.", "surname": "John", "position": "First Grade Clerks", "department": "Post Office - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "I. J. Baxter", "canonical_name": "Baxter, I. J.", "given_names": "I. J.", "surname": "Baxter", "position": "Second Grade Clerks", "department": "Post Office - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "D. A. Davies", "canonical_name": "Davies, D. A.", "given_names": "D. A.", "surname": "Davies", "position": "Second Grade Clerks", "department": "Post Office - Sierra Leone", "salary_min": 130, "salary_max": 160},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()