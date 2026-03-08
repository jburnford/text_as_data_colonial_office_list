"""
Gambia Colonial Office List 1939 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1939

OFFICIALS = [
    {"name": "J. M. Gray", "canonical_name": "Gray, J. M.", "given_names": "J. M.", "surname": "Gray", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 1000, "salary_max": 1150, "duty_allowance": 200},
    {"name": "A. G. B. Manson", "canonical_name": "Manson, A. G. B.", "given_names": "A. G. B.", "surname": "Manson", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 600, "salary_max": 1000, "allowances": "72l. seniority allowance"},
    {"name": "E. F. Qualtrough", "canonical_name": "Qualtrough, E. F.", "given_names": "E. F.", "surname": "Qualtrough", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 630, "salary_max": 840},
    {"name": "G. C. Coker", "canonical_name": "Coker, G. C.", "given_names": "G. C.", "surname": "Coker", "position": "Clerk of Courts, 2nd Grade", "department": "Legal Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Sheriff", "department": "Legal Department - Gambia"},
    {"name": "R. C. Allen", "canonical_name": "Allen, R. C.", "given_names": "R. C.", "surname": "Allen", "position": "Director of Education", "department": "Education - Gambia", "salary_min": 400, "salary_max": 840, "allowances": "72l. seniority allowance"},
    {"name": "R. G. Biddulph", "canonical_name": "Biddulph, R. G.", "given_names": "R. G.", "surname": "Biddulph", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 400, "salary_max": 1000, "allowances": "72l. seniority allowance"},
    {"name": "A. J. Knott", "canonical_name": "Knott, A. J.", "given_names": "A. J.", "surname": "Knott", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 400, "salary_max": 1000, "allowances": "72l. seniority allowance"},
    {"name": "R. H. Gretton", "canonical_name": "Gretton, R. H.", "given_names": "R. H.", "surname": "Gretton", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 400, "salary_max": 1000, "allowances": "72l. seniority allowance"},
    {"name": "R. G. Syme", "canonical_name": "Syme, R. G.", "given_names": "R. G.", "surname": "Syme", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 400, "salary_max": 1000, "allowances": "72l. seniority allowance"},
    {"name": "T. F. G. Hopkins", "canonical_name": "Hopkins, T. F. G.", "given_names": "T. F. G.", "surname": "Hopkins", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 400, "salary_max": 1000, "allowances": "72l. seniority allowance"},
    {"name": "D. Bayley", "canonical_name": "Bayley, D.", "given_names": "D.", "surname": "Bayley", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 400, "salary_max": 1000, "allowances": "72l. seniority allowance"},
    {"name": "N. M. Asheton", "canonical_name": "Asheton, N. M.", "given_names": "N. M.", "surname": "Asheton", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 400, "salary_max": 1000, "allowances": "72l. seniority allowance"},
    {"name": "Wilson Plant", "canonical_name": "Plant, Wilson", "given_names": "Wilson", "surname": "Plant", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 400, "salary_max": 1000, "allowances": "72l. seniority allowance"},
    {"name": "J. M. Stow", "canonical_name": "Stow, J. M.", "given_names": "J. M.", "surname": "Stow", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 400, "salary_max": 1000, "allowances": "72l. seniority allowance"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()