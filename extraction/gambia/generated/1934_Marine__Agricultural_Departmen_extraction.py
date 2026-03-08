"""
Gambia Colonial Office List 1934 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1934

OFFICIALS = [
    {"name": "A. D. Steele", "canonical_name": "Steele, A. D.", "given_names": "A. D.", "surname": "Steele", "position": "Harbour Master and Marine Superintendent", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720, "duty_allowance": 100, "allowances": "80l. messing allowance"},
    {"name": "J. M. Simpson", "canonical_name": "Simpson, J. M.", "given_names": "J. M.", "surname": "Simpson", "position": "Chief Engineer", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720},
    {"name": "J. Reid", "canonical_name": "Reid, J.", "given_names": "J.", "surname": "Reid", "position": "Artificer Engineer", "department": "Marine - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "R. E. G. Deall", "canonical_name": "Deall, R. E. G.", "given_names": "R. E. G.", "surname": "Deall", "position": "Transport Officer", "department": "Marine - Gambia", "salary_min": 400, "salary_max": 500, "military_rank": "Captain"},
    {"name": "A. J. Brooks", "canonical_name": "Brooks, A. J.", "given_names": "A. J.", "surname": "Brooks", "position": "Director of Agriculture", "department": "Agricultural Department - Gambia", "salary_min": 600, "salary_max": 920, "qualifications": ["F.L.S.", "F.C.S.", "F.R.H.S."]},
    {"name": "F. W. Hall", "canonical_name": "Hall, F. W.", "given_names": "F. W.", "surname": "Hall", "position": "Assistant Director", "department": "Agricultural Department - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "J. Pirie", "canonical_name": "Pirie, J.", "given_names": "J.", "surname": "Pirie", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. W. Sparrow", "canonical_name": "Sparrow, J. W.", "given_names": "J. W.", "surname": "Sparrow", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()