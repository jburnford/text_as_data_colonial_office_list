"""
Sierra Leone Colonial Office List 1900 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1900

OFFICIALS = [
    {"name": "G. Page", "canonical_name": "Page, G.", "given_names": "G.", "surname": "Page", "position": "Keeper of Freedom Gaol", "department": "Prison Department - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "R. A. George", "canonical_name": "George, R. A.", "given_names": "R. A.", "surname": "George", "position": "Under Gaoler", "department": "Prison Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "Rachel Macauley", "canonical_name": "Macauley, Rachel", "given_names": "Rachel", "surname": "Macauley", "position": "Matron", "department": "Prison Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "S. W. Adams", "canonical_name": "Adams, S. W.", "given_names": "S. W.", "surname": "Adams", "position": "Gaoler at Sherbrovo", "department": "Prison Department - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "E. Faulkner", "canonical_name": "Faulkner, E.", "given_names": "E.", "surname": "Faulkner", "position": "D. Commissioner", "department": "Waterloo District - Sierra Leone", "salary_min": 300, "salary_max": 350, "location": "Waterloo", "allowances": "travelling allowance, 91l. 5s."},
    {"name": "Lancelot Taylor", "canonical_name": "Taylor, Lancelot", "given_names": "Lancelot", "surname": "Taylor", "position": "Clerk", "department": "Waterloo District - Sierra Leone", "salary_min": 40, "salary_max": 40, "location": "Waterloo"},
    {"name": "The D. Commissioner", "canonical_name": "Commissioner, The D.", "surname": "Commissioner", "position": "Coroner", "department": "Waterloo District - Sierra Leone", "salary_min": 20, "salary_max": 20, "location": "Waterloo"},
    {"name": "T. J. Alldridge", "canonical_name": "Alldridge, T. J.", "given_names": "T. J.", "surname": "Alldridge", "position": "D. Commissioner", "department": "Sherbro District - Sierra Leone", "salary_min": 500, "salary_max": 500, "region": "Sherbro", "allowances": "50l. lodging allowance"},
    {"name": "S. A. Macauley", "canonical_name": "Macauley, S. A.", "given_names": "S. A.", "surname": "Macauley", "position": "Clerks", "department": "Sherbro District - Sierra Leone", "salary_min": 75, "salary_max": 90, "region": "Sherbro"},
    {"name": "L. A. Fyne", "canonical_name": "Fyne, L. A.", "given_names": "L. A.", "surname": "Fyne", "position": "Clerks", "department": "Sherbro District - Sierra Leone", "salary_min": 50, "salary_max": 50, "region": "Sherbro"},
    {"name": "W. B. Gilpin", "canonical_name": "Gilpin, W. B.", "given_names": "W. B.", "surname": "Gilpin", "position": "Treasury Clerk", "department": "Sherbro District - Sierra Leone", "salary_min": 50, "salary_max": 60, "region": "Sherbro"},
    {"name": "G. A. Jones", "canonical_name": "Jones, G. A.", "given_names": "G. A.", "surname": "Jones", "position": "Bailiff", "department": "Sherbro District - Sierra Leone", "salary_min": 36, "salary_max": 40, "region": "Sherbro"},
    {"name": "The D. Commissioner", "canonical_name": "Commissioner, The D.", "surname": "Commissioner", "position": "Coroner", "department": "Sherbro District - Sierra Leone", "salary_min": 20, "salary_max": 20, "region": "Sherbro"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()