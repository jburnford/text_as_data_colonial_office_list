"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "P. F. Barton", "canonical_name": "Barton, P. F.", "given_names": "P. F.", "surname": "Barton", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "allowances": "Personal allowance 100l.", "honors": ["V.D."]},
    {"name": "F. A. Mathias", "canonical_name": "Mathias, F. A.", "given_names": "F. A.", "surname": "Mathias", "position": "Deputy Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "C. J. Hodgens", "canonical_name": "Hodgens, C. J.", "given_names": "C. J.", "surname": "Hodgens", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A", "honors": ["M.C."]},
    {"name": "C. S. Rayner", "canonical_name": "Rayner, C. S.", "given_names": "C. S.", "surname": "Rayner", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_scale": "A"},
    {"name": "U. W. Coker", "canonical_name": "Coker, U. W.", "given_names": "U. W.", "surname": "Coker", "position": "African Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 400, "salary_max": 600},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "Staff Superintendent", "department": "Treasury Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "S. D. Palmer", "canonical_name": "Palmer, S. D.", "given_names": "S. D.", "surname": "Palmer", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "C. R. Peacock", "canonical_name": "Peacock, C. R.", "given_names": "C. R.", "surname": "Peacock", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "V. E. Doherty", "canonical_name": "Doherty, V. E.", "given_names": "V. E.", "surname": "Doherty", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "D. E. Stubbs", "canonical_name": "Stubbs, D. E.", "given_names": "D. E.", "surname": "Stubbs", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. M. A. Thomas", "canonical_name": "Thomas, A. M. A.", "given_names": "A. M. A.", "surname": "Thomas", "position": "First Grade Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()