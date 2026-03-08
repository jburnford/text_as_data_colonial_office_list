"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "H. J. Huggins", "canonical_name": "Huggins, H. J.", "given_names": "H. J.", "surname": "Huggins", "position": "Chief Justice and Judge of the Vice-Admiralty Court", "department": "Judicial - Sierra Leone", "salary_min": 1500, "salary_max": 1500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk to Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "W. W. Streeten", "canonical_name": "Streeten, W. W.", "given_names": "W. W.", "surname": "Streeten", "position": "Queen's Advocate", "department": "Judicial - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "allowances": "62l. 10s. from Gambia"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk to Queen's Advocate", "department": "Judicial - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Clerk to Queen's Advocate", "department": "Judicial - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "A. B. Marston", "canonical_name": "Marston, A. B.", "given_names": "A. B.", "surname": "Marston", "position": "Master and Registrar of the Supreme Court", "department": "Judicial - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "A. B. Martyn", "canonical_name": "Martyn, A. B.", "given_names": "A. B.", "surname": "Martyn", "position": "Clerk to Master and Registrar", "department": "Judicial - Sierra Leone", "salary_min": 160, "salary_max": 160},
    {"name": "John Meheux", "canonical_name": "Meheux, John", "given_names": "John", "surname": "Meheux", "position": "Sheriff and Provost-Marshal", "department": "Judicial - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "A. Montagu", "canonical_name": "Montagu, A.", "given_names": "A.", "surname": "Montagu", "position": "Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "J. M. Thomas", "canonical_name": "Thomas, J. M.", "given_names": "J. M.", "surname": "Thomas", "position": "Clerk to Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "J. G. Smith", "canonical_name": "Smith, J. G.", "given_names": "J. G.", "surname": "Smith", "position": "Clerk to Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Coroner for Freetown", "department": "Judicial - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "A. B. Martyn", "canonical_name": "Martyn, A. B.", "given_names": "A. B.", "surname": "Martyn", "position": "Registrar of Vice-Admiralty Court", "department": "Judicial - Sierra Leone", "acting_status": "Acting"},
    {"name": "John Meheux", "canonical_name": "Meheux, John", "given_names": "John", "surname": "Meheux", "position": "Marshal of Vice-Admiralty Court", "department": "Judicial - Sierra Leone"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()