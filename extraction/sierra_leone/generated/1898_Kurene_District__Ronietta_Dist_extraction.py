"""
Sierra Leone Colonial Office List 1898 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1898

OFFICIALS = [
    {"name": "W. S. Sharpe", "canonical_name": "Sharpe, W. S.", "given_names": "W. S.", "surname": "Sharpe", "position": "D. Commissioner", "department": "Districts - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Capt.", "region": "Kurene District"},
    {"name": "W. L. King", "canonical_name": "King, W. L.", "given_names": "W. L.", "surname": "King", "position": "Clerk", "department": "Districts - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Kurene District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Districts - Sierra Leone", "salary_min": 30, "salary_max": 40, "region": "Kurene District"},
    {"name": "J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell", "position": "D. Surgeon", "department": "Districts - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Kurene District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dispenser", "department": "Districts - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Kurene District"},
    {"name": "E. D. Fairtough", "canonical_name": "Fairtough, E. D.", "given_names": "E. D.", "surname": "Fairtough", "position": "D. Commissioner", "department": "Districts - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Capt.", "region": "Ronietta District"},
    {"name": "A. C. Forde", "canonical_name": "Forde, A. C.", "given_names": "A. C.", "surname": "Forde", "position": "Clerk", "department": "Districts - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Ronietta District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Districts - Sierra Leone", "salary_min": 30, "salary_max": 40, "region": "Ronietta District"},
    {"name": "Hood", "canonical_name": "Hood, ", "surname": "Hood", "position": "D. Surgeon", "department": "Districts - Sierra Leone", "salary_min": 350, "salary_max": 400, "region": "Ronietta District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dispenser", "department": "Districts - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Ronietta District"},
    {"name": "C. E. Carr", "canonical_name": "Carr, C. E.", "given_names": "C. E.", "surname": "Carr", "position": "D. Commissioner", "department": "Districts - Sierra Leone", "salary_min": 400, "salary_max": 500, "region": "Bandajuma District"},
    {"name": "D. A. Branche", "canonical_name": "Branche, D. A.", "given_names": "D. A.", "surname": "Branche", "position": "Clerk", "department": "Districts - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Bandajuma District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Districts - Sierra Leone", "salary_min": 30, "salary_max": 40, "region": "Bandajuma District"},
    {"name": "G. J. Arnold", "canonical_name": "Arnold, G. J.", "given_names": "G. J.", "surname": "Arnold", "position": "D. Surgeon", "department": "Districts - Sierra Leone", "salary_min": 300, "salary_max": 350, "qualifications": ["F.R.C.S."], "region": "Bandajuma District"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dispenser", "department": "Districts - Sierra Leone", "salary_min": 60, "salary_max": 70, "region": "Bandajuma District"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()