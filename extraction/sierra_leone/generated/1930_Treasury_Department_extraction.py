"""
Sierra Leone Colonial Office List 1930 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1930

OFFICIALS = [
    {"name": "P. F. Barton", "canonical_name": "Barton, P. F.", "given_names": "P. F.", "surname": "Barton", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "allowances": "Personal allowance 100l.", "honors": ["V.D."]},
    {"name": "Edwin Taylor", "canonical_name": "Taylor, Edwin", "given_names": "Edwin", "surname": "Taylor", "position": "Senior Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 840, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "C. J. Hodgens", "canonical_name": "Hodgens, C. J.", "given_names": "C. J.", "surname": "Hodgens", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A", "honors": ["M.C."]},
    {"name": "C. S. Rayner", "canonical_name": "Rayner, C. S.", "given_names": "C. S.", "surname": "Rayner", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A"},
    {"name": "E. Godman Taylor", "canonical_name": "Taylor, E. Godman", "given_names": "E. Godman", "surname": "Taylor", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 400, "salary_max": 600},
    {"name": "U. W. Coker", "canonical_name": "Coker, U. W.", "given_names": "U. W.", "surname": "Coker", "position": "Staff Superintendent", "department": "Treasury Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. E. Laverse", "canonical_name": "Laverse, A. E.", "given_names": "A. E.", "surname": "Laverse", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "S. D. Palmer", "canonical_name": "Palmer, S. D.", "given_names": "S. D.", "surname": "Palmer", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "C. E. Peacock", "canonical_name": "Peacock, C. E.", "given_names": "C. E.", "surname": "Peacock", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "V. E. Doherty", "canonical_name": "Doherty, V. E.", "given_names": "V. E.", "surname": "Doherty", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()