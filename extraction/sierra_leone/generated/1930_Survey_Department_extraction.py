"""
Sierra Leone Colonial Office List 1930 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1930

OFFICIALS = [
    {"name": "J. Dare", "canonical_name": "Dare, J.", "given_names": "J.", "surname": "Dare", "position": "Director of Surveys", "department": "Survey Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210, "military_rank": "Major"},
    {"name": "V. E. H. Sanoeau", "canonical_name": "Sanoeau, V. E. H.", "given_names": "V. E. H.", "surname": "Sanoeau", "position": "Officer in charge, Topographical Branch", "department": "Survey Department - Sierra Leone", "military_rank": "Capt."},
    {"name": "P. F. White", "canonical_name": "White, P. F.", "given_names": "P. F.", "surname": "White", "position": "Camp Officer", "department": "Survey Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "military_rank": "Capt."},
    {"name": "I. V. R. Smith", "canonical_name": "Smith, I. V. R.", "given_names": "I. V. R.", "surname": "Smith", "position": "Camp Officer", "department": "Survey Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "military_rank": "Capt."},
    {"name": "W. H. Treasy", "canonical_name": "Treasy, W. H.", "given_names": "W. H.", "surname": "Treasy", "position": "Camp Officer", "department": "Survey Department - Sierra Leone", "salary_min": 720, "salary_max": 920, "military_rank": "Lieut."},
    {"name": "P. A. Godwin", "canonical_name": "Godwin, P. A.", "given_names": "P. A.", "surname": "Godwin", "position": "Officer i/c Cadastral Branch", "department": "Survey Department - Sierra Leone", "salary_scale": "C", "qualifications": ["M.S.M."]},
    {"name": "R. Temple", "canonical_name": "Temple, R.", "given_names": "R.", "surname": "Temple", "position": "Survey and Lands Officer", "department": "Survey Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. E. W. Nesbitt", "canonical_name": "Nesbitt, A. E. W.", "given_names": "A. E. W.", "surname": "Nesbitt", "position": "Instructor, Survey School", "department": "Survey Department - Sierra Leone", "salary_min": 480, "salary_max": 480, "military_rank": "Capt.", "honors":["M.C."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()