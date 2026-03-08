"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "G. E. Biddle", "canonical_name": "Biddle, G. E.", "given_names": "G. E.", "surname": "Biddle", "position": "Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_scale": "A"},
    {"name": "A. P. Simmonds", "canonical_name": "Simmonds, A. P.", "given_names": "A. P.", "surname": "Simmonds", "position": "Assistant Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_scale": "F"},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "Storekeeper", "department": "Prisons - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "J. Dare", "canonical_name": "Dare, J.", "given_names": "J.", "surname": "Dare", "position": "Director", "department": "Survey Department - Sierra Leone", "salary_min": 1050, "duty_allowance": 210, "military_rank": "Major", "honors": ["M.C."]},
    {"name": "P. A. Godwin", "canonical_name": "Godwin, P. A.", "given_names": "P. A.", "surname": "Godwin", "position": "Officer i/c Cadastral Branch", "department": "Survey Department - Sierra Leone", "salary_scale": "C", "honors":["M.S.M."]},
    {"name": "R. Temple", "canonical_name": "Temple, R.", "given_names": "R.", "surname": "Temple", "position": "Survey and Lands Officer", "department": "Survey Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. E. W. Nesbitt", "canonical_name": "Nesbitt, A. E. W.", "given_names": "A. E. W.", "surname": "Nesbitt", "position": "Instructor, Survey School", "department": "Survey Department - Sierra Leone", "salary_min": 480, "military_rank": "Capt.", "honors": ["M.C."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()