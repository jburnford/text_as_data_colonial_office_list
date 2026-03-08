"""
Sierra Leone Colonial Office List 1921 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1921

OFFICIALS = [
    {"name": "S. Renshaw", "canonical_name": "Renshaw, S.", "given_names": None, "surname": "Renshaw", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "L. Belmar", "canonical_name": "Belmar, L.", "given_names": None, "surname": "Belmar", "position": "Senior Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 450, "salary_max": 920},
    {"name": "P. W. Clemens", "canonical_name": "Clemens, P. W.", "given_names": None, "surname": "Clemens", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 450, "salary_max": 920},
    {"name": "H. D. Smith", "canonical_name": "Smith, H. D.", "given_names": None, "surname": "Smith", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 450, "salary_max": 920},
    {"name": "E. Godman Taylor", "canonical_name": "Taylor, E. Godman", "given_names": "E. Godman", "surname": "Taylor", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "M. B. Reader", "canonical_name": "Reader, M. B.", "given_names": None, "surname": "Reader", "position": "Principal Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "M. P. Cole", "canonical_name": "Cole, M. P.", "given_names": None, "surname": "Cole", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": None, "surname": "Jones", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "U. W. Coker", "canonical_name": "Coker, U. W.", "given_names": None, "surname": "Coker", "position": "Second Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "S. D. Palmer", "canonical_name": "Palmer, S. D.", "given_names": None, "surname": "Palmer", "position": "Second Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "A. P. Viret", "canonical_name": "Viret, A. P.", "given_names": None, "surname": "Viret", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "A. S. Fraser", "canonical_name": "Fraser, A. S.", "given_names": None, "surname": "Fraser", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 450, "salary_max": 920},
    {"name": "R. B. Mackie", "canonical_name": "Mackie, R. B.", "given_names": None, "surname": "Mackie", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 450, "salary_max": 920, "location": "Freetown"},
    {"name": "L. F. Campbell", "canonical_name": "Campbell, L. F.", "given_names": None, "surname": "Campbell", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "location": "Sherbro"},
    {"name": "A. C. A. Johnson", "canonical_name": "Johnson, A. C. A.", "given_names": None, "surname": "Johnson", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "P. H. H. George", "canonical_name": "George, P. H. H.", "given_names": None, "surname": "George", "position": "Senior Outdoor Officer", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "T. A. Clemens", "canonical_name": "Clemens, T. A.", "given_names": None, "surname": "Clemens", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "M. A. Lewis", "canonical_name": "Lewis, M. A.", "given_names": None, "surname": "Lewis", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": None, "surname": "Jones", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "A. R. Harris", "canonical_name": "Harris, A. R.", "given_names": None, "surname": "Harris", "position": "Principal Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 252, "salary_max": 372},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()