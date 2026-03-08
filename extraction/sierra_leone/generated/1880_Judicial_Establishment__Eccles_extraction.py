"""
Sierra Leone Colonial Office List 1880 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1880

OFFICIALS = [
    {"name": "W. W. Streeten", "canonical_name": "Streeten, W. W.", "given_names": "W. W.", "surname": "Streeten", "position": "Chief Justice and Judge of the Vice-Admiralty Court, and Legal Adviser", "department": "Judicial - Sierra Leone", "salary_min": 1600, "salary_max": 1600},
    {"name": "A. B. Martyn", "canonical_name": "Martyn, A. B.", "given_names": "A. B.", "surname": "Martyn", "position": "Clerk to ditto", "department": "Judicial - Sierra Leone", "salary_min": 160},
    {"name": "A. Montagu", "canonical_name": "Montagu, A.", "given_names": "A.", "surname": "Montagu", "position": "Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "J. M. Thomas", "canonical_name": "Thomas, J. M.", "given_names": "J. M.", "surname": "Thomas", "position": "Clerks to ditto", "department": "Judicial - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "J. G. Smith", "canonical_name": "Smith, J. G.", "given_names": "J. G.", "surname": "Smith", "position": "Clerks to ditto", "department": "Judicial - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "John Meheux", "canonical_name": "Meheux, John", "given_names": "John", "surname": "Meheux", "position": "Sheriff and Provost-Marshal", "department": "Judicial - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "A. B. Martyn", "canonical_name": "Martyn, A. B.", "given_names": "A. B.", "surname": "Martyn", "position": "Registrar of Vice-Admiralty Court", "department": "Judicial - Sierra Leone", "acting_status": "Acting"},
    {"name": "John Meheux", "canonical_name": "Meheux, John", "given_names": "John", "surname": "Meheux", "position": "Marshal of ditto", "department": "Judicial - Sierra Leone"},
    {"name": "The Senior Army Medical Officer", "canonical_name": "Senior Army Medical Officer, The", "surname": "Senior Army Medical Officer", "position": "Coroner, Freetown", "department": "Judicial - Sierra Leone", "salary_min": 60, "salary_max": 60, "acting_status": "Acting", "location": "Freetown"},
    {"name": "Right Rev. Henry Cheetham", "canonical_name": "Cheetham, Henry", "given_names": "Henry", "surname": "Cheetham", "position": "Bishop of Sierra Leone", "department": "Ecclesiastical - Sierra Leone", "salary_min": 300, "salary_max": 300, "qualifications": ["D.D."]},
    {"name": "Rev. John Campbell", "canonical_name": "Campbell, John", "given_names": "John", "surname": "Campbell", "position": "Assistant ditto", "department": "Ecclesiastical - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "T. S. Wilson", "canonical_name": "Wilson, T. S.", "given_names": "T. S.", "surname": "Wilson", "position": "Head Master, Model School", "department": "Education Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100, "location": "Freetown"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()