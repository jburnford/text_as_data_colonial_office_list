"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "J. Dare", "canonical_name": "Dare, J.", "given_names": "J.", "surname": "Dare", "position": "Director of Surveys", "department": "Survey Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "P. A. Godwin", "canonical_name": "Godwin, P. A.", "given_names": "P. A.", "surname": "Godwin", "position": "Officer i/c Cadastral Branch", "department": "Survey Department - Sierra Leone", "salary_scale": "C", "honors": ["M.S.M."]},
    {"name": "R. Temple", "canonical_name": "Temple, R.", "given_names": "R.", "surname": "Temple", "position": "Survey and Lands Officer", "department": "Survey Department - Sierra Leone", "salary_scale": "C"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()