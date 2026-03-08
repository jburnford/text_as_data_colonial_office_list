"""
Gambia Colonial Office List 1924 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1924

OFFICIALS = [
    {"name": "Clinton H. Greig", "canonical_name": "Greig, Clinton H.", "given_names": "Clinton H.", "surname": "Greig", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 720, "salary_max": 920, "duty_allowance": 72, "military_rank": "Captain"},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 720},
    {"name": "A. Minnock", "canonical_name": "Minnock, A.", "given_names": "A.", "surname": "Minnock", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "W. Collins", "canonical_name": "Collins, W.", "given_names": "W.", "surname": "Collins", "position": "Bandmaster", "department": "Police Force - Gambia", "salary_min": 350, "salary_max": 450},
    {"name": "Z. S. A. Williams", "canonical_name": "Williams, Z. S. A.", "given_names": "Z. S. A.", "surname": "Williams", "position": "Pay Clerk and Quartermaster", "department": "Police Force - Gambia", "salary_min": 100, "salary_max": 230},
    {"name": "Clinton H. Greig", "canonical_name": "Greig, Clinton H.", "given_names": "Clinton H.", "surname": "Greig", "position": "Inspector of Prisons", "department": "Prison - Gambia", "military_rank": "Captain"},
    {"name": "T. B. Shingle", "canonical_name": "Shingle, T. B.", "given_names": "T. B.", "surname": "Shingle", "position": "Gaoler", "department": "Prison - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. S. Thomas", "canonical_name": "Thomas, J. S.", "given_names": "J. S.", "surname": "Thomas", "position": "Chief Warder", "department": "Prison - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "E. J. Powell", "canonical_name": "Powell, E. J.", "given_names": "E. J.", "surname": "Powell", "position": "Chaplain", "department": "Prison - Gambia", "qualifications": ["Rev."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()