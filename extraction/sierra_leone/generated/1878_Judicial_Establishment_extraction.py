"""
Sierra Leone Colonial Office List 1878 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1878

OFFICIALS = [
    {"name": "H. J. Huggins", "canonical_name": "Huggins, H. J.", "given_names": "H. J.", "surname": "Huggins", "position": "Chief Justice and Judge of the Vice-Admiralty Court", "department": "Judicial - Sierra Leone", "salary_min": 1500, "salary_max": 1500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk to ditto", "department": "Judicial - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "W. W. Streeten", "canonical_name": "Streeten, W. W.", "given_names": "W. W.", "surname": "Streeten", "position": "Queen's Advocate", "department": "Judicial - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk to Queen's Advocate", "department": "Judicial - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Clerk to ditto", "department": "Judicial - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "T. Marston", "canonical_name": "Marston, T.", "given_names": "T.", "surname": "Marston", "position": "Master and Registrar of the Supreme Court", "department": "Judicial - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "A. B. Martyn", "canonical_name": "Martyn, A. B.", "given_names": "A. B.", "surname": "Martyn", "position": "Clerk to ditto", "department": "Judicial - Sierra Leone", "salary_min": 160, "salary_max": 160},
    {"name": "John Meheux", "canonical_name": "Meheux, John", "given_names": "John", "surname": "Meheux", "position": "Sheriff and Provost-Marshal", "department": "Judicial - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "A. Montagu", "canonical_name": "Montagu, A.", "given_names": "A.", "surname": "Montagu", "position": "Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "J. M. Thomas", "canonical_name": "Thomas, J. M.", "given_names": "J. M.", "surname": "Thomas", "position": "Clerks to ditto", "department": "Judicial - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "J. H. Lacton", "canonical_name": "Lacton, J. H.", "given_names": "J. H.", "surname": "Lacton", "position": "Clerks to ditto", "department": "Judicial - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "D. Carroll", "canonical_name": "Carroll, D.", "given_names": "D.", "surname": "Carroll", "position": "Registrar of Court of Summary Jurisdiction", "department": "Judicial - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. Cole", "canonical_name": "Cole, J.", "given_names": "J.", "surname": "Cole", "position": "Clerk to ditto", "department": "Judicial - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "J. Ashwood", "canonical_name": "Ashwood, J.", "given_names": "J.", "surname": "Ashwood", "position": "Coroner for Freetown", "department": "Judicial - Sierra Leone", "salary_min": 100, "salary_max": 100, "location": "Freetown"},
    {"name": "T. Marston", "canonical_name": "Marston, T.", "given_names": "T.", "surname": "Marston", "position": "Registrar of Vice-Admiralty Court", "department": "Judicial - Sierra Leone"},
    {"name": "John Meheux", "canonical_name": "Meheux, John", "given_names": "John", "surname": "Meheux", "position": "Marshal of ditto", "department": "Judicial - Sierra Leone"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()