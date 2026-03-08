"""
Gambia Colonial Office List 1940 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1940

OFFICIALS = [
    {"name": "J. M. Gray", "canonical_name": "Gray, J. M.", "given_names": "J. M.", "surname": "Gray", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "A. G. B. Manson", "canonical_name": "Manson, A. G. B.", "given_names": "A. G. B.", "surname": "Manson", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "E. F. Qualtrough", "canonical_name": "Qualtrough, E. F.", "given_names": "E. F.", "surname": "Qualtrough", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 750, "salary_max": 840},
    {"name": "G. C. Coker", "canonical_name": "Coker, G. C.", "given_names": "G. C.", "surname": "Coker", "position": "Clerk of Courts, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "R. L. Hill", "canonical_name": "Hill, R. L.", "given_names": "R. L.", "surname": "Hill", "position": "Sheriff", "department": "Legal Department - Gambia", "military_rank": "Capt."},
    {"name": "R. C. Allen", "canonical_name": "Allen, R. C.", "given_names": "R. C.", "surname": "Allen", "position": "Director of Education", "department": "Education - Gambia", "salary_min": 480, "salary_max": 920},
    {"name": "R. G. Biddulph", "canonical_name": "Biddulph, R. G.", "given_names": "R. G.", "surname": "Biddulph", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "A. J. Knott", "canonical_name": "Knott, A. J.", "given_names": "A. J.", "surname": "Knott", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "R. H. Gretton", "canonical_name": "Gretton, R. H.", "given_names": "R. H.", "surname": "Gretton", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "D. Bayley", "canonical_name": "Bayley, D.", "given_names": "D.", "surname": "Bayley", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "N. M. Asheton", "canonical_name": "Asheton, N. M.", "given_names": "N. M.", "surname": "Asheton", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "G. Lorimer", "canonical_name": "Lorimer, G.", "given_names": "G.", "surname": "Lorimer", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "Wilson Plant", "canonical_name": "Plant, Wilson", "given_names": "Wilson", "surname": "Plant", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "J. M. Stow", "canonical_name": "Stow, J. M.", "given_names": "J. M.", "surname": "Stow", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "F. A. Evans", "canonical_name": "Evans, F. A.", "given_names": "F. A.", "surname": "Evans", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "R. L. Hill", "canonical_name": "Hill, R. L.", "given_names": "R. L.", "surname": "Hill", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 750, "salary_max": 920, "military_rank": "Capt."},
    {"name": "W. Collins", "canonical_name": "Collins, W.", "given_names": "W.", "surname": "Collins", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 750},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Inspector", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "R. L. Hill", "canonical_name": "Hill, R. L.", "given_names": "R. L.", "surname": "Hill", "position": "Inspector of Prisons", "department": "Prison - Gambia", "military_rank": "Capt."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()