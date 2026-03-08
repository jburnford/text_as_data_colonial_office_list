"""
Sierra Leone Colonial Office List 1894 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1894

OFFICIALS = [
    {"name": "Sir W. H. Quayle Jones", "canonical_name": "Jones, W. H. Quayle", "given_names": "W. H. Quayle", "surname": "Jones", "position": "Chief Justice", "department": "Legal Departments - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "honors": ["Kt."]},
    {"name": "W. A. Valantin", "canonical_name": "Valantin, W. A.", "given_names": "W. A.", "surname": "Valantin", "position": "Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "J. A. McCarthy", "canonical_name": "McCarthy, J. A.", "given_names": "J. A.", "surname": "McCarthy", "position": "Queen's Advocate", "department": "Legal Departments - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "F. A. Miller", "canonical_name": "Miller, F. A.", "given_names": "F. A.", "surname": "Miller", "position": "Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "S. D. Aymar", "canonical_name": "Aymar, S. D.", "given_names": "S. D.", "surname": "Aymar", "position": "Assistant Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "A. Sharood", "canonical_name": "Sharood, A.", "given_names": "A.", "surname": "Sharood", "position": "Master and Registrar of the Supreme Court and Registrar-General", "department": "Legal Departments - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "A. E. T. Metzger", "canonical_name": "Metzger, A. E. T.", "given_names": "A. E. T.", "surname": "Metzger", "position": "Chief Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "W. S. Saunders", "canonical_name": "Saunders, W. S.", "given_names": "W. S.", "surname": "Saunders", "position": "Clerks", "department": "Legal Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "S. A. Metzger", "canonical_name": "Metzger, S. A.", "given_names": "S. A.", "surname": "Metzger", "position": "Clerks", "department": "Legal Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "F. E. B. Bucknor", "canonical_name": "Bucknor, F. E. B.", "given_names": "F. E. B.", "surname": "Bucknor", "position": "Clerks", "department": "Legal Departments - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "W. A. Valantin", "canonical_name": "Valantin, W. A.", "given_names": "W. A.", "surname": "Valantin", "position": "Deputy Sheriff", "department": "Legal Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. Bayldon Walker", "canonical_name": "Walker, J. Bayldon", "given_names": "J. Bayldon", "surname": "Walker", "position": "Police Magistrate and Judge of Court of Requests and Coroner", "department": "Legal Departments - Sierra Leone", "salary_min": 450, "salary_max": 450, "qualifications": ["B.L."]},
    {"name": "William Hughes", "canonical_name": "Hughes, William", "given_names": "William", "surname": "Hughes", "position": "Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "A. W. Nylander", "canonical_name": "Nylander, A. W.", "given_names": "A. W.", "surname": "Nylander", "position": "2nd Clerk", "department": "Legal Departments - Sierra Leone", "salary_min": 43, "salary_max": 43},
    {"name": "A. E. T. Metzger", "canonical_name": "Metzger, A. E. T.", "given_names": "A. E. T.", "surname": "Metzger", "position": "Registrar of Births, Deaths, and Marriages", "department": "Legal Departments - Sierra Leone"},
    {"name": "Rev. G. J. Macaulay", "canonical_name": "Macaulay, G. J.", "given_names": "G. J.", "surname": "Macaulay", "position": "Registrar of Births, Deaths, and Marriages", "department": "Legal Departments - Sierra Leone"},
    {"name": "Rev. N. J. Cole", "canonical_name": "Cole, N. J.", "given_names": "N. J.", "surname": "Cole", "position": "Registrar of Births, Deaths, and Marriages", "department": "Legal Departments - Sierra Leone"},
    {"name": "J. B. M'Cormack", "canonical_name": "M'Cormack, J. B.", "given_names": "J. B.", "surname": "M'Cormack", "position": "Registrar of Births, Deaths, and Marriages", "department": "Legal Departments - Sierra Leone"},
    {"name": "A. K. Lewis", "canonical_name": "Lewis, A. K.", "given_names": "A. K.", "surname": "Lewis", "position": "Registrar of Births, Deaths, and Marriages", "department": "Legal Departments - Sierra Leone"},
    {"name": "M. L. Jarrett", "canonical_name": "Jarrett, M. L.", "given_names": "M. L.", "surname": "Jarrett", "position": "Registrar of Births, Deaths, and Marriages", "department": "Legal Departments - Sierra Leone"},
    {"name": "J. J. Warburton", "canonical_name": "Warburton, J. J.", "given_names": "J. J.", "surname": "Warburton", "position": "Registrar of Births, Deaths, and Marriages", "department": "Legal Departments - Sierra Leone"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()