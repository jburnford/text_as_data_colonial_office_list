"""
Sierra Leone Colonial Office List 1928 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1928

OFFICIALS = [
    {"name": "J. Dare", "canonical_name": "Dare, J.", "given_names": "J.", "surname": "Dare", "position": "Director", "department": "Survey Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210, "military_rank": "Major", "honors": ["M.C."]},
    {"name": "R. Temple", "canonical_name": "Temple, R.", "given_names": "R.", "surname": "Temple", "position": "Survey and Lands Officer", "department": "Survey Department - Sierra Leone", "salary_scale": "C"},
    {"name": "C. A. Smith", "canonical_name": "Smith, C. A.", "given_names": "C. A.", "surname": "Smith", "position": "Instructor, Survey School", "department": "Survey Department - Sierra Leone", "salary_scale": "C"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()