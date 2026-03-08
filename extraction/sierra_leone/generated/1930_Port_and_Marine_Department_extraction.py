"""
Sierra Leone Colonial Office List 1930 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1930

OFFICIALS = [
    {"name": "R. L. Wikner", "canonical_name": "Wikner, R. L.", "given_names": "R. L.", "surname": "Wikner", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_scale": "C", "military_rank": "Lieut.", "honors": ["D.S.C."], "qualifications": ["R.N.R."]},
    {"name": "A. F. G. Taylor", "canonical_name": "Taylor, A. F. G.", "given_names": "A. F. G.", "surname": "Taylor", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "H. Bowles", "canonical_name": "Bowles, H.", "given_names": "H.", "surname": "Bowles", "position": "Government Pilot", "department": "Port and Marine Department - Sierra Leone", "salary_min": 500, "salary_max": 500}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()