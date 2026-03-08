"""
Gambia Colonial Office List 1931 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1931

OFFICIALS = [
    {"name": "A. G. Still", "canonical_name": "Still, A. G.", "given_names": "A. G.", "surname": "Still", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 600, "salary_max": 920, "allowances": "72l. seniority allowance from 720l., and 100l. local allowance."},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "Chief Clerk, 2nd Grade", "department": "Audit Office - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "A. D. Steele", "canonical_name": "Steele, A. D.", "given_names": "A. D.", "surname": "Steele", "position": "Harbour Master and Marine Superintendent", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720, "duty_allowance": 100, "allowances": "80l. messing allowance."},
    {"name": "J. M. Simpson", "canonical_name": "Simpson, J. M.", "given_names": "J. M.", "surname": "Simpson", "position": "Chief Engineer", "department": "Marine - Gambia", "salary_min": 480, "salary_max": 720},
    {"name": "A. B. Waters", "canonical_name": "Waters, A. B.", "given_names": "A. B.", "surname": "Waters", "position": "Reclamation Officer", "department": "Marine - Gambia", "salary_min": 440, "salary_max": 720},
    {"name": "J. Reid", "canonical_name": "Reid, J.", "given_names": "J.", "surname": "Reid", "position": "Artificer Engineers", "department": "Marine - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "W. J. G. Smith", "canonical_name": "Smith, W. J. G.", "given_names": "W. J. G.", "surname": "Smith", "position": "Artificer Engineers", "department": "Marine - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "R. E. G. Deall", "canonical_name": "Deall, R. E. G.", "given_names": "R. E. G.", "surname": "Deall", "position": "Transport Officer", "department": "Marine - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "Chief Clerk, 1st Grade", "department": "Marine - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "R. A. Brown", "canonical_name": "Brown, R. A.", "given_names": "R. A.", "surname": "Brown", "position": "Officer-in-Charge, Posts and Telegraphs", "department": "Posts and Telegraphs Department - Gambia", "allowances": "150l. allowance."},
    {"name": "A. Wallis", "canonical_name": "Wallis, A.", "given_names": "A.", "surname": "Wallis", "position": "Wireless Electrician", "department": "Posts and Telegraphs Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "Postmaster", "department": "Posts and Telegraphs Department - Gambia", "salary_min": 260, "salary_max": 360},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()