"""
Gambia Colonial Office List 1932 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1932

OFFICIALS = [
    {"name": "M. M. Auchinleck", "canonical_name": "Auchinleck, M. M.", "given_names": "M. M.", "surname": "Auchinleck", "position": "Officer-in-Charge, Posts and Telegraphs", "department": "Posts and Telegraphs Department - Gambia", "allowances": "150l. allowance"},
    {"name": "A. Wallis", "canonical_name": "Wallis, A.", "given_names": "A.", "surname": "Wallis", "position": "Wireless Electrician", "department": "Posts and Telegraphs Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "F. E. Danner", "canonical_name": "Danner, F. E.", "given_names": "F. E.", "surname": "Danner", "position": "Postmaster", "department": "Posts and Telegraphs Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "A. J. Brooks", "canonical_name": "Brooks, A. J.", "given_names": "A. J.", "surname": "Brooks", "position": "Director of Agriculture", "department": "Agricultural Department - Gambia", "salary_min": 600, "salary_max": 920, "qualifications": ["F.L.S.", "F.C.S.", "F.R.H.S."]},
    {"name": "F. W. Hall", "canonical_name": "Hall, F. W.", "given_names": "F. W.", "surname": "Hall", "position": "Assistant Director", "department": "Agricultural Department - Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "J. Pirie", "canonical_name": "Pirie, J.", "given_names": "J.", "surname": "Pirie", "position": "Agricultural Superintendents", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. W. Sparrow", "canonical_name": "Sparrow, J. W.", "given_names": "J. W.", "surname": "Sparrow", "position": "Agricultural Superintendents", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "T. R. Hayes", "canonical_name": "Hayes, T. R.", "given_names": "T. R.", "surname": "Hayes", "position": "Agricultural Superintendents", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. A. Brawn", "canonical_name": "Brawn, J. A.", "given_names": "J. A.", "surname": "Brawn", "position": "Officer Commanding", "department": "Royal West African Frontier Force - Gambia", "salary_min": 700, "duty_allowance": 54, "military_rank": "Capt."},
    {"name": "F. B. B. Dowling", "canonical_name": "Dowling, F. B. B.", "given_names": "F. B. B.", "surname": "Dowling", "position": "Lieutenants", "department": "Royal West African Frontier Force - Gambia", "salary_min": 600, "military_rank": "Lieutenants", "honors": ["M.C."]},
    {"name": "S. B. Cope", "canonical_name": "Cope, S. B.", "given_names": "S. B.", "surname": "Cope", "position": "Lieutenants", "department": "Royal West African Frontier Force - Gambia", "salary_min": 600, "military_rank": "Lieutenants"},
    {"name": "R. G. L. Ford", "canonical_name": "Ford, R. G. L.", "given_names": "R. G. L.", "surname": "Ford", "position": "Lieutenants", "department": "Royal West African Frontier Force - Gambia", "salary_min": 600, "military_rank": "Lieutenants"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()