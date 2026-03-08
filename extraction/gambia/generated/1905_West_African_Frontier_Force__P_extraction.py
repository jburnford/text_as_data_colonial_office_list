"""
Gambia Colonial Office List 1905 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1905

OFFICIALS = [
    {"name": "C. F. O. Graham", "canonical_name": "Graham, C. F. O.", "given_names": "C. F. O.", "surname": "Graham", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 400, "salary_max": 400, "allowances": "command pay, 96l.", "military_rank": "Captain", "qualifications": ["R.M.L.I."]},
    {"name": "H. Hoskins", "canonical_name": "Hoskins, H.", "given_names": "H.", "surname": "Hoskins", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 325, "salary_max": 325, "military_rank": "Lieutenant"},
    {"name": "C. Morley", "canonical_name": "Morley, C.", "given_names": "C.", "surname": "Morley", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 325, "salary_max": 325, "military_rank": "Lieutenant"},
    {"name": "W. Wheatcroft", "canonical_name": "Wheatcroft, W.", "given_names": "W.", "surname": "Wheatcroft", "position": "Colour-Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "P. L. Webb", "canonical_name": "Webb, P. L.", "given_names": "P. L.", "surname": "Webb", "position": "Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "Joseph Brown", "canonical_name": "Brown, Joseph", "given_names": "Joseph", "surname": "Brown", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 350, "salary_max": 350, "allowances": "50l. personal allowance", "duty_allowance": 50},
    {"name": "T. B. Bracken", "canonical_name": "Bracken, T. B.", "given_names": "T. B.", "surname": "Bracken", "position": "Assistant Superintendent", "department": "Police Force - Gambia", "salary_min": 250, "salary_max": 250, "allowances": "forage allowance of 2s. 3d. per diem each", "per_diem": "2s. 3d."},
    {"name": "Joseph Brown", "canonical_name": "Brown, Joseph", "given_names": "Joseph", "surname": "Brown", "position": "Inspector of Prisons", "department": "Prison - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "C. C. Johnson", "canonical_name": "Johnson, C. C.", "given_names": "C. C.", "surname": "Johnson", "position": "Gaoler", "department": "Prison - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "T. T. Turner", "canonical_name": "Turner, T. T.", "given_names": "T. T.", "surname": "Turner", "position": "Chief Warden", "department": "Prison - Gambia", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()