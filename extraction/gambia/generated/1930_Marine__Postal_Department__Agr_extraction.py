"""
Gambia Colonial Office List 1930 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1930

OFFICIALS = [
    {"name": "A. D. Steele", "canonical_name": "Steele, A. D.", "given_names": "A. D.", "surname": "Steele", "position": "Harbour Master and Marine Superintendent", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720, "duty_allowance": 100, "allowances": "80l. messing allowance"},
    {"name": "J. M. Simpson", "canonical_name": "Simpson, J. M.", "given_names": "J. M.", "surname": "Simpson", "position": "Chief Engineer", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720},
    {"name": "A. B. Waters", "canonical_name": "Waters, A. B.", "given_names": "A. B.", "surname": "Waters", "position": "Reclamation Officer", "department": "Marine - Gambia", "salary_min": 440, "salary_max": 720},
    {"name": "E. E. Dixson", "canonical_name": "Dixson, E. E.", "given_names": "E. E.", "surname": "Dixson", "position": "Artiller Engineers", "department": "Marine - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "J. Reid", "canonical_name": "Reid, J.", "given_names": "J.", "surname": "Reid", "position": "Artiller Engineers", "department": "Marine - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Transport Officer", "department": "Marine - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "F. A. Mathias", "canonical_name": "Mathias, F. A.", "given_names": "F. A.", "surname": "Mathias", "position": "Director of Posts", "department": "Postal Department - Gambia"},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "Postmaster", "department": "Postal Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "C. J. Thomas", "canonical_name": "Thomas, C. J.", "given_names": "C. J.", "surname": "Thomas", "position": "2nd Grade Clerk", "department": "Postal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "A. J. Brooks", "canonical_name": "Brooks, A. J.", "given_names": "A. J.", "surname": "Brooks", "position": "Director of Agriculture", "department": "Agricultural Department - Gambia", "salary_min": 600, "salary_max": 920, "qualifications": ["F.I.S.", "F.C.S.", "F.R.H.S."], "allowances": "72l. seniority allowance from 720l."},
    {"name": "F. W. Hall", "canonical_name": "Hall, F. W.", "given_names": "F. W.", "surname": "Hall", "position": "Assistant Director", "department": "Agricultural Department - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "J. Pirie", "canonical_name": "Pirie, J.", "given_names": "J.", "surname": "Pirie", "position": "Agricultural Superintendents", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. W. Sparrow", "canonical_name": "Sparrow, J. W.", "given_names": "J. W.", "surname": "Sparrow", "position": "Agricultural Superintendents", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "T. R. Hayes", "canonical_name": "Hayes, T. R.", "given_names": "T. R.", "surname": "Hayes", "position": "Agricultural Superintendents", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. A. Brawn", "canonical_name": "Brawn, J. A.", "given_names": "J. A.", "surname": "Brawn", "position": "Officer Commanding", "department": "Royal West African Frontier Force - Gambia", "salary_min": 700, "salary_max": 700, "duty_allowance": 54, "military_rank": "Capt."},
    {"name": "F. B. B. Dowling", "canonical_name": "Dowling, F. B. B.", "given_names": "F. B. B.", "surname": "Dowling", "position": "Lieutenants", "department": "Royal West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "honors": ["M.C."], "military_rank": "Lieutenants"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Lieutenants", "department": "Royal West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenants"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Lieutenants", "department": "Royal West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenants"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()