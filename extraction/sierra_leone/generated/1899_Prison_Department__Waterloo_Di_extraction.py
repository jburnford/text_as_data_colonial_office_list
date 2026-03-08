"""
Sierra Leone Colonial Office List 1899 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1899

OFFICIALS = [
    {"name": "G. Page", "canonical_name": "Page, G.", "given_names": "G.", "surname": "Page", "position": "Keeper of Freetown Gaol", "department": "Prison Department - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "R. A. George", "canonical_name": "George, R. A.", "given_names": "R. A.", "surname": "George", "position": "Under Gaoler", "department": "Prison Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "A. Strong", "canonical_name": "Strong, A.", "given_names": "A.", "surname": "Strong", "position": "Clerk", "department": "Prison Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "W. F. John", "canonical_name": "John, W. F.", "given_names": "W. F.", "surname": "John", "position": "Assistant Clerk", "department": "Prison Department - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "Rachol Macauley", "canonical_name": "Macauley, Rachol", "given_names": "Rachol", "surname": "Macauley", "position": "Matron", "department": "Prison Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "S. W. Adams", "canonical_name": "Adams, S. W.", "given_names": "S. W.", "surname": "Adams", "position": "Gaoler at Sherboro", "department": "Prison Department - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "E. Faulkner", "canonical_name": "Faulkner, E.", "given_names": "E.", "surname": "Faulkner", "position": "D. Commissioner", "department": "Prison Department - Sierra Leone", "salary_min": 350, "salary_max": 800, "allowances": "travelling allowance, 91l. 5s.", "location": "Waterloo"},
    {"name": "Lancelot Taylor", "canonical_name": "Taylor, Lancelot", "given_names": "Lancelot", "surname": "Taylor", "position": "Clerk", "department": "Prison Department - Sierra Leone", "salary_min": 40, "salary_max": 40, "location": "Waterloo"},
    {"name": "The D. Commissioner", "canonical_name": "Commissioner, The D.", "given_names": "The D.", "surname": "Commissioner", "position": "Coroner", "department": "Prison Department - Sierra Leone", "salary_min": 20, "salary_max": 20, "location": "Waterloo"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()