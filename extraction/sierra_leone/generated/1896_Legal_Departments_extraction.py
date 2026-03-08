"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "E. B. Hindle", "canonical_name": "Hindle, E. B.", "given_names": "E. B.", "surname": "Hindle", "position": "Chief Justice", "department": "Legal Departments - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "W. A. Valantin", "canonical_name": "Valantin, W. A.", "given_names": "W. A.", "surname": "Valantin", "position": "Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "P. Crampton Smyly", "canonical_name": "Smyly, P. Crampton", "given_names": "P. Crampton", "surname": "Smyly", "position": "Queen's Advocate", "department": "Legal Departments - Sierra Leone", "salary_min": 700, "salary_max": 700, "allowances": "rent allace. 60l., or free quarters."},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 85, "salary_max": 100},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Assistant Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "R. J. de Groot", "canonical_name": "Groot, R. J. de", "given_names": "R. J.", "surname": "Groot", "position": "Master and Registrar of the Supreme Court and Registrar-General", "department": "Legal Departments - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "W. S. Saunders", "canonical_name": "Saunders, W. S.", "given_names": "W. S.", "surname": "Saunders", "position": "Chief Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "S. A. Metzger", "canonical_name": "Metzger, S. A.", "given_names": "S. A.", "surname": "Metzger", "position": "Clerks", "department": "Legal Departments - Sierra Leone", "salary_min": 56, "salary_max": 56},
    {"name": "F. E. B. Bucknor", "canonical_name": "Bucknor, F. E. B.", "given_names": "F. E. B.", "surname": "Bucknor", "position": "Clerks", "department": "Legal Departments - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "A. Kennedy Lewis", "canonical_name": "Lewis, A. Kennedy", "given_names": "A. Kennedy", "surname": "Lewis", "position": "Clerks", "department": "Legal Departments - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "U. F. Lapham", "canonical_name": "Lapham, U. F.", "given_names": "U. F.", "surname": "Lapham", "position": "Sheriff and Provost-Marshal", "department": "Legal Departments - Sierra Leone", "salary_min": 50, "salary_max": 50, "military_rank": "Capt."},
    {"name": "W. A. Valantin", "canonical_name": "Valantin, W. A.", "given_names": "W. A.", "surname": "Valantin", "position": "Deputy Sheriff", "department": "Legal Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "W. Clark", "canonical_name": "Clark, W.", "given_names": "W.", "surname": "Clark", "position": "Police Magistrate and Judge of Court of Requests and Coroner", "department": "Legal Departments - Sierra Leone", "salary_min": 450, "salary_max": 450, "qualifications": ["B.L."]},
    {"name": "A. E. T. Metzger", "canonical_name": "Metzger, A. E. T.", "given_names": "A. E. T.", "surname": "Metzger", "position": "Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 160, "salary_max": 180},
    {"name": "A. W. Nylander", "canonical_name": "Nylander, A. W.", "given_names": "A. W.", "surname": "Nylander", "position": "2nd Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 48, "salary_max": 48}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()