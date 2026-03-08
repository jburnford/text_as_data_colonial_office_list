"""
Sierra Leone Colonial Office List 1899 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1899

OFFICIALS = [
    {"name": "T. J. Alldridge", "canonical_name": "Alldridge, T. J.", "given_names": "T. J.", "surname": "Alldridge", "position": "D. Commissioner", "department": "Customs - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "50l. lodging allowance", "location": "Sherbro"},
    {"name": "S. A. Macaulay", "canonical_name": "Macaulay, S. A.", "given_names": "S. A.", "surname": "Macaulay", "position": "Clerk", "department": "Customs - Sierra Leone", "salary_min": 75, "salary_max": 90, "location": "Sherbro"},
    {"name": "L. A. Fyne", "canonical_name": "Fyne, L. A.", "given_names": "L. A.", "surname": "Fyne", "position": "Clerk", "department": "Customs - Sierra Leone", "salary_min": 60, "salary_max": 60, "location": "Sherbro"},
    {"name": "G. A. Jones", "canonical_name": "Jones, G. A.", "given_names": "G. A.", "surname": "Jones", "position": "Bailiff", "department": "Customs - Sierra Leone", "salary_min": 36, "salary_max": 40, "location": "Sherbro"},
    {"name": "The D. Commissioner", "canonical_name": "Commissioner, The D.", "surname": "Commissioner", "position": "Coroner", "department": "Customs - Sierra Leone", "salary_min": 20, "salary_max": 20, "location": "Sherbro"},
    {"name": "W. S. Sharpe", "canonical_name": "Sharpe, W. S.", "given_names": "W. S.", "surname": "Sharpe", "position": "D. Commissioner", "department": "Customs - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Capt.", "location": "Kurene"},
    {"name": "W. L. King", "canonical_name": "King, W. L.", "given_names": "W. L.", "surname": "King", "position": "Clerk", "department": "Customs - Sierra Leone", "salary_min": 50, "salary_max": 60, "location": "Kurene"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Interpreter", "department": "Customs - Sierra Leone", "salary_min": 30, "salary_max": 40, "location": "Kurene"},
    {"name": "J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell", "position": "D. Surgeon", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 400, "location": "Kurene"},
    {"name": "T. D. Betts", "canonical_name": "Betts, T. D.", "given_names": "T. D.", "surname": "Betts", "position": "Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 70, "location": "Kurene"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()