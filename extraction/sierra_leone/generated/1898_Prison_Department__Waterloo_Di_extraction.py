"""
Sierra Leone Colonial Office List 1898 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1898

OFFICIALS = [
    {"name": "G. Page", "canonical_name": "Page, G.", "given_names": "G.", "surname": "Page", "position": "Keeper of Freetown Gaol", "department": "Prison Department - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "R. A. George", "canonical_name": "George, R. A.", "given_names": "R. A.", "surname": "George", "position": "Under Gaoler", "department": "Prison Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "A. Strong", "canonical_name": "Strong, A.", "given_names": "A.", "surname": "Strong", "position": "Clerk", "department": "Prison Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "W. F. John", "canonical_name": "John, W. F.", "given_names": "W. F.", "surname": "John", "position": "Assistant Clerk", "department": "Prison Department - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "Rachel Macauley", "canonical_name": "Macauley, Rachel", "given_names": "Rachel", "surname": "Macauley", "position": "Matron", "department": "Prison Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Mary A. Bull", "canonical_name": "Bull, Mary A.", "given_names": "Mary A.", "surname": "Bull", "position": "Under ditto", "department": "Prison Department - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "S. W. Adams", "canonical_name": "Adams, S. W.", "given_names": "S. W.", "surname": "Adams", "position": "Gaoler at Sherbro", "department": "Prison Department - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "E. Faulkner", "canonical_name": "Faulkner, E.", "given_names": "E.", "surname": "Faulkner", "position": "D. Commissioner", "department": "Waterloo District - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "Lancelot Taylor", "canonical_name": "Taylor, Lancelot", "given_names": "Lancelot", "surname": "Taylor", "position": "Clerk", "department": "Waterloo District - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "The D. Commissioner", "canonical_name": "Commissioner, The D.", "given_names": "The D.", "surname": "Commissioner", "position": "Coroner", "department": "Waterloo District - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "T. J. Allridge", "canonical_name": "Allridge, T. J.", "given_names": "T. J.", "surname": "Allridge", "position": "D. Commissioner", "department": "Sherbro District - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "50l. lodging allowance"},
    {"name": "S. A. Macaulay", "canonical_name": "Macaulay, S. A.", "given_names": "S. A.", "surname": "Macaulay", "position": "Clerks", "department": "Sherbro District - Sierra Leone", "salary_min": 75, "salary_max": 90},
    {"name": "L. A. Fyne", "canonical_name": "Fyne, L. A.", "given_names": "L. A.", "surname": "Fyne", "position": "Clerks", "department": "Sherbro District - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "A. E. Palmer", "canonical_name": "Palmer, A. E.", "given_names": "A. E.", "surname": "Palmer", "position": "Bailiff", "department": "Sherbro District - Sierra Leone", "salary_min": 36, "salary_max": 40},
    {"name": "The D. Commissioner", "canonical_name": "Commissioner, The D.", "given_names": "The D.", "surname": "Commissioner", "position": "Coroner", "department": "Sherbro District - Sierra Leone", "salary_min": 20, "salary_max": 20},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()