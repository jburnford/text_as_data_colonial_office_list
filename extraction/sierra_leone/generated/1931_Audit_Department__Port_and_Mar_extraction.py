"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "J. D. M. Bourne", "canonical_name": "Bourne, J. D. M.", "given_names": "J. D. M.", "surname": "Bourne", "position": "Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "R. S. Foster", "canonical_name": "Foster, R. S.", "given_names": "R. S.", "surname": "Foster", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "A. G. Bowring", "canonical_name": "Bowring, A. G.", "given_names": "A. G.", "surname": "Bowring", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "H. G. Inray", "canonical_name": "Inray, H. G.", "given_names": "H. G.", "surname": "Inray", "position": "Assistant Auditors", "department": "Audit Department - Sierra Leone", "salary_scale": "A"},
    {"name": "E. S. George", "canonical_name": "George, E. S.", "given_names": "E. S.", "surname": "George", "position": "Chief Clerk", "department": "Audit Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "J. A. Langley", "canonical_name": "Langley, J. A.", "given_names": "J. A.", "surname": "Langley", "position": "First Grade Clerks", "department": "Audit Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "S. A. Short", "canonical_name": "Short, S. A.", "given_names": "S. A.", "surname": "Short", "position": "First Grade Clerks", "department": "Audit Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "R. L. Wikner", "canonical_name": "Wikner, R. L.", "given_names": "R. L.", "surname": "Wikner", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_scale": "C", "military_rank": "Lieut.", "honors": ["D.S.C."], "qualifications": ["R.N.R."]},
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