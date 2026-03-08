"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "J. O'Connor", "canonical_name": "O'Connor, J.", "given_names": "J.", "surname": "O'Connor", "position": "Keeper of Freetown Gaol", "department": "Prison Department - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "R. A. George", "canonical_name": "George, R. A.", "given_names": "R. A.", "surname": "George", "position": "Under Gaoler", "department": "Prison Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "A. Strong", "canonical_name": "Strong, A.", "given_names": "A.", "surname": "Strong", "position": "Clerk", "department": "Prison Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "Rachel Macaulay", "canonical_name": "Macaulay, Rachel", "given_names": "Rachel", "surname": "Macaulay", "position": "Matron", "department": "Prison Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Mary A. Bull", "canonical_name": "Bull, Mary A.", "given_names": "Mary A.", "surname": "Bull", "position": "Under Matron", "department": "Prison Department - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "S. W. Adams", "canonical_name": "Adams, S. W.", "given_names": "S. W.", "surname": "Adams", "position": "Gaoler at Sherbro", "department": "Prison Department - Sierra Leone", "salary_min": 75, "salary_max": 75, "location": "Sherbro"},
    {"name": "W. M. Huggins", "canonical_name": "Huggins, W. M.", "given_names": "W. M.", "surname": "Huggins", "position": "D. Commissioner", "department": "Districts - Sierra Leone", "salary_min": 300, "salary_max": 350, "region": "Eastern District"},
    {"name": "Lancelot Taylor", "canonical_name": "Taylor, Lancelot", "given_names": "Lancelot", "surname": "Taylor", "position": "Clerk", "department": "Districts - Sierra Leone", "salary_min": 40, "salary_max": 40, "region": "Eastern District"},
    {"name": "The D. Commissioner", "canonical_name": "Commissioner, The D.", "surname": "Commissioner", "position": "Coroner", "department": "Districts - Sierra Leone", "salary_min": 20, "salary_max": 20, "region": "Eastern District"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()