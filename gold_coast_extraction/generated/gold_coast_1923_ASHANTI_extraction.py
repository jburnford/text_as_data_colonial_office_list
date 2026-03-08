"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "C. H. Harper", "canonical_name": "Harper, C. H.", "given_names": "C. H.", "surname": "Harper", "position": "Chief Commissioner", "department": "Administrative and Political Department - Ashanti", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 320, "honors": ["C.M.G.", "O.B.E."], "region": "Ashanti"},
    {"name": "Lt.-Col. C. E. D. O. Rew", "canonical_name": "Rew, C. E. D. O.", "given_names": "C. E. D. O.", "surname": "Rew", "position": "Deputy Chief Commissioner", "department": "Administrative and Political Department - Ashanti", "salary_min": 1360, "salary_max": 1360, "duty_allowance": 270, "honors": ["O.B.E."], "military_rank": "Lt.-Col.", "region": "Ashanti"},
    {"name": "E. Gardiner Smith", "canonical_name": "Smith, E. Gardiner", "given_names": "E. Gardiner", "surname": "Smith", "position": "Circuit Judge", "department": "Ashanti and Northern Territories Judiciary - Ashanti", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240, "region": "Ashanti"},
    {"name": "F. J. J. F. McDowell", "canonical_name": "McDowell, F. J. J. F.", "given_names": "F. J. J. F.", "surname": "McDowell", "position": "Police Magistrate", "department": "Ashanti and Northern Territories Judiciary - Ashanti", "salary_min": 720, "salary_max": 960, "location": "Coomassie", "region": "Ashanti"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()