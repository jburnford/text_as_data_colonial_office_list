"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "R. B. Mackie", "canonical_name": "Mackie, R. B.", "given_names": "R. B.", "surname": "Mackie", "position": "Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "W. H. Eccles", "canonical_name": "Eccles, W. H.", "given_names": "W. H.", "surname": "Eccles", "position": "Assistant Comptroller of Customs", "department": "Customs Department - Sierra Leone", "salary_scale": "A"},
    {"name": "W. T. Martin", "canonical_name": "Martin, W. T.", "given_names": "W. T.", "surname": "Martin", "position": "Collectors of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_scale": "A"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Collectors of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_scale": "A"},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Sherbro", "salary_min": 360, "salary_max": 500},
    {"name": "A. C. A. Johnson", "canonical_name": "Johnson, A. C. A.", "given_names": "A. C. A.", "surname": "Johnson", "position": "Supervisor of Customs", "department": "Customs Department - Sierra Leone", "location": "Freetown", "salary_min": 360, "salary_max": 500},
    {"name": "A. R. Harris", "canonical_name": "Harris, A. R.", "given_names": "A. R.", "surname": "Harris", "position": "Senior Outdoor Officer", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. A. Lewis", "canonical_name": "Lewis, M. A.", "given_names": "M. A.", "surname": "Lewis", "position": "Chief Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "W. M. Peeler", "canonical_name": "Peeler, W. M.", "given_names": "W. M.", "surname": "Peeler", "position": "Chief Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. A. Smith", "canonical_name": "Smith, M. A.", "given_names": "M. A.", "surname": "Smith", "position": "Chief Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "C. D. Williams", "canonical_name": "Williams, C. D.", "given_names": "C. D.", "surname": "Williams", "position": "Chief Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "E. A. Turner", "canonical_name": "Turner, E. A.", "given_names": "E. A.", "surname": "Turner", "position": "Chief Clerks", "department": "Customs Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "E. H. Morris", "canonical_name": "Morris, E. H.", "given_names": "E. H.", "surname": "Morris", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "R. S. Foster", "canonical_name": "Foster, R. S.", "given_names": "R. S.", "surname": "Foster", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "R. F. Pinder", "canonical_name": "Pinder, R. F.", "given_names": "R. F.", "surname": "Pinder", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "H. G. Imray", "canonical_name": "Imray, H. G.", "given_names": "H. G.", "surname": "Imray", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "M. P. Cole", "canonical_name": "Cole, M. P.", "given_names": "M. P.", "surname": "Cole", "position": "Chief Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "S. B. Logan", "canonical_name": "Logan, S. B.", "given_names": "S. B.", "surname": "Logan", "position": "First Grade Clerks", "department": "Audit Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. A. Langley", "canonical_name": "Langley, J. A.", "given_names": "J. A.", "surname": "Langley", "position": "First Grade Clerks", "department": "Audit Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "R. L. Wikner", "canonical_name": "Wikner, R. L.", "given_names": "R. L.", "surname": "Wikner", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "military_rank": "Lieut.", "honors": ["D.S.C."], "qualifications": ["R.N.R."], "salary_scale": "C"},
    {"name": "A. F. G. Taylor", "canonical_name": "Taylor, A. F. G.", "given_names": "A. F. G.", "surname": "Taylor", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "H. Bowles", "canonical_name": "Bowles, H.", "given_names": "H.", "surname": "Bowles", "position": "Government Pilot", "department": "Port and Marine Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()