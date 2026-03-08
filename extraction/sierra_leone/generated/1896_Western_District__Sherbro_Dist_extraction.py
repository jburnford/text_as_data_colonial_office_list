"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "W. B. Campbell", "canonical_name": "Campbell, W. B.", "given_names": "W. B.", "surname": "Campbell", "position": "D. Commissioner", "department": "Districts - Sierra Leone", "salary_min": 250, "salary_max": 250, "allowances": "rent, 40l.", "region": "Western District."},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "Clerk", "department": "Districts - Sierra Leone", "salary_min": 40, "salary_max": 40, "region": "Western District."},
    {"name": "The D. Commissioner", "canonical_name": "Commissioner, The D.", "surname": "Commissioner", "position": "Coroner", "department": "Districts - Sierra Leone", "salary_min": 20, "salary_max": 20, "region": "Western District."},
    {"name": "T. J. Allridge", "canonical_name": "Allridge, T. J.", "given_names": "T. J.", "surname": "Allridge", "position": "D. Commissioner", "department": "Districts - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "50l lodging allowance", "region": "Sherbro District."},
    {"name": "S. A. Macaulay", "canonical_name": "Macaulay, S. A.", "given_names": "S. A.", "surname": "Macaulay", "position": "Clerks", "department": "Districts - Sierra Leone", "salary_min": 75, "salary_max": 75, "region": "Sherbro District."},
    {"name": "I. A. Fyne", "canonical_name": "Fyne, I. A.", "given_names": "I. A.", "surname": "Fyne", "position": "Clerks", "department": "Districts - Sierra Leone", "salary_min": 50, "salary_max": 50, "region": "Sherbro District."},
    {"name": "A. E. Palmer", "canonical_name": "Palmer, A. E.", "given_names": "A. E.", "surname": "Palmer", "position": "Bailiff", "department": "Districts - Sierra Leone", "salary_min": 36, "salary_max": 36, "region": "Sherbro District."},
    {"name": "The D. Commissioner", "canonical_name": "Commissioner, The D.", "surname": "Commissioner", "position": "Coroner", "department": "Districts - Sierra Leone", "salary_min": 20, "salary_max": 20, "region": "Sherbro District."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()