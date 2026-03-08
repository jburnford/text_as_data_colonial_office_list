"""
Sierra Leone Colonial Office List 1894 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1894

OFFICIALS = [
    {"name": "W. B. Campbell", "canonical_name": "Campbell, W. B.", "given_names": "W. B.", "surname": "Campbell", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 250, "salary_max": 250, "allowances": "rent 40l."},
    {"name": "A. Kennedy Lewis", "canonical_name": "Lewis, A. Kennedy", "given_names": "A. Kennedy", "surname": "Lewis", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "the D. Commissioner", "canonical_name": "Commissioner, the D.", "surname": "Commissioner", "position": "Coroner", "department": "Civil Establishment - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "T. J. Alldridge", "canonical_name": "Alldridge, T. J.", "given_names": "T. J.", "surname": "Alldridge", "position": "D. Commissioner", "department": "Civil Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "50l. lodging allowance"},
    {"name": "S. A. Macauley", "canonical_name": "Macauley, S. A.", "given_names": "S. A.", "surname": "Macauley", "position": "Clerks", "department": "Civil Establishment - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "E. C. Davies", "canonical_name": "Davies, E. C.", "given_names": "E. C.", "surname": "Davies", "position": "Clerks", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "G. Jarrett", "canonical_name": "Jarrett, G.", "given_names": "G.", "surname": "Jarrett", "position": "Bailiff", "department": "Civil Establishment - Sierra Leone", "salary_min": 36, "salary_max": 36},
    {"name": "the D. Commissioner", "canonical_name": "Commissioner, the D.", "surname": "Commissioner", "position": "Coroner", "department": "Civil Establishment - Sierra Leone", "salary_min": 20, "salary_max": 20},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()