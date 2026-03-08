"""
Sierra Leone Colonial Office List 1898 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1898

OFFICIALS = [
    {"name": "G. Stallard", "canonical_name": "Stallard, G.", "given_names": "G.", "surname": "Stallard", "position": "Chief Justice", "department": "Legal Departments - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "P. Crampton Smyly", "canonical_name": "Smyly, P. Crampton", "given_names": "P. Crampton", "surname": "Smyly", "position": "Attorney-General", "department": "Legal Departments - Sierra Leone", "salary_min": 700, "salary_max": 700, "allowances": "rent alike. 60l., or free quarters."},
    {"name": "A. Hudson", "canonical_name": "Hudson, A.", "given_names": "A.", "surname": "Hudson", "position": "Solicitor-General", "department": "Legal Departments - Sierra Leone", "salary_min": 400, "salary_max": 500, "allowances": "rent 50l."},
    {"name": "W. A. Valantin", "canonical_name": "Valantin, W. A.", "given_names": "W. A.", "surname": "Valantin", "position": "First Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Second Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Third Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "D. F. Wilbraham", "canonical_name": "Wilbraham, D. F.", "given_names": "D. F.", "surname": "Wilbraham", "position": "Master and Registrar of the Supreme Court and Registrar-General", "department": "Legal Departments - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "W. S. Saunders", "canonical_name": "Saunders, W. S.", "given_names": "W. S.", "surname": "Saunders", "position": "Chief Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "F. E. B. Bucknor", "canonical_name": "Bucknor, F. E. B.", "given_names": "F. E. B.", "surname": "Bucknor", "position": "Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "A. Kennedy Lewis", "canonical_name": "Lewis, A. Kennedy", "given_names": "A. Kennedy", "surname": "Lewis", "position": "Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "S. A. Metzger", "canonical_name": "Metzger, S. A.", "given_names": "S. A.", "surname": "Metzger", "position": "Clerk, Master's Office", "department": "Legal Departments - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Sheriff and Provost-Marshal", "department": "Legal Departments - Sierra Leone", "salary_min": 50, "salary_max": 50, "allowances": "ex officio."},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Under Sheriff", "department": "Legal Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "R. J. de Groot", "canonical_name": "de Groot, R. J.", "given_names": "R. J.", "surname": "de Groot", "position": "Police Magistrate and Judge of Court of Requests and Coroner", "department": "Legal Departments - Sierra Leone", "salary_min": 450, "salary_max": 450},
    {"name": "A. E. T. Metzger", "canonical_name": "Metzger, A. E. T.", "given_names": "A. E. T.", "surname": "Metzger", "position": "Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "H. Williams", "canonical_name": "Williams, H.", "given_names": "H.", "surname": "Williams", "position": "2nd Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 48, "salary_max": 48}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()