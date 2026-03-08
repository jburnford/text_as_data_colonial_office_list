"""
Gambia Colonial Office List 1931 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1931

OFFICIALS = [
    {"name": "A. J. Brooks", "canonical_name": "Brooks, A. J.", "given_names": "A. J.", "surname": "Brooks", "position": "Director of Agriculture", "department": "Agricultural Department - Gambia", "qualifications": ["F.I.S.", "F.C.S.", "F.R.H.S."], "salary_min": 600, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "F. W. Hall", "canonical_name": "Hall, F. W.", "given_names": "F. W.", "surname": "Hall", "position": "Assistant Director", "department": "Agricultural Department - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "J. Pirie", "canonical_name": "Pirie, J.", "given_names": "J.", "surname": "Pirie", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. W. Sparrow", "canonical_name": "Sparrow, J. W.", "given_names": "J. W.", "surname": "Sparrow", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "T. R. Hayes", "canonical_name": "Hayes, T. R.", "given_names": "T. R.", "surname": "Hayes", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. A. Brawn", "canonical_name": "Brawn, J. A.", "given_names": "J. A.", "surname": "Brawn", "position": "Officer Commanding", "department": "Royal West African Frontier Force - Gambia", "military_rank": "Captain", "salary_min": 700, "salary_max": 700, "duty_allowance": 54},
    {"name": "F. B. B. Dowling", "canonical_name": "Dowling, F. B. B.", "given_names": "F. B. B.", "surname": "Dowling", "position": "Lieutenants", "department": "Royal West African Frontier Force - Gambia", "military_rank": "Lieutenant", "honors": ["M.C."], "salary_min": 600, "salary_max": 600},
    {"name": "S. B. Cope", "canonical_name": "Cope, S. B.", "given_names": "S. B.", "surname": "Cope", "position": "Lieutenants", "department": "Royal West African Frontier Force - Gambia", "military_rank": "Lieutenant", "salary_min": 600, "salary_max": 600},
    {"name": "R. G. L. Ford", "canonical_name": "Ford, R. G. L.", "given_names": "R. G. L.", "surname": "Ford", "position": "Lieutenants", "department": "Royal West African Frontier Force - Gambia", "military_rank": "Lieutenant", "salary_min": 600, "salary_max": 600},
    {"name": "A. Rives", "canonical_name": "Rives, A.", "given_names": "A.", "surname": "Rives", "position": "Vice-Consul", "department": "Foreign Consuls - Gambia", "location": "Belgium"},
    {"name": "F. Orcel", "canonical_name": "Orcel, F.", "given_names": "F.", "surname": "Orcel", "position": "Consular Agent", "department": "Foreign Consuls - Gambia", "location": "France"},
    {"name": "F. Orcel", "canonical_name": "Orcel, F.", "given_names": "F.", "surname": "Orcel", "position": "Consul", "department": "Foreign Consuls - Gambia", "location": "Portugal"},
    {"name": "J. Howie", "canonical_name": "Howie, J.", "given_names": "J.", "surname": "Howie", "position": "Vice-Consul", "department": "Foreign Consuls - Gambia", "location": "Spain"},
    {"name": "V. Q. Petersen", "canonical_name": "Petersen, V. Q.", "given_names": "V. Q.", "surname": "Petersen", "position": "Consul", "department": "Foreign Consuls - Gambia", "location": "Norway"},
    {"name": "V. Q. Petersen", "canonical_name": "Petersen, V. Q.", "given_names": "V. Q.", "surname": "Petersen", "position": "Vice-Consul", "department": "Foreign Consuls - Gambia", "location": "Finland"},
    {"name": "V. Q. Petersen", "canonical_name": "Petersen, V. Q.", "given_names": "V. Q.", "surname": "Petersen", "position": "Consul", "department": "Foreign Consuls - Gambia", "location": "Denmark"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()