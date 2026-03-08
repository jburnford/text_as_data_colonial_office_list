"""
Gambia Colonial Office List 1936 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1936

OFFICIALS = [
    {"name": "J. M. Gray", "canonical_name": "Gray, J. M.", "given_names": "J. M.", "surname": "Gray", "position": "Judge of the Supreme Court", "department": "Judicial - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "A. G. B. Manson", "canonical_name": "Manson, A. G. B.", "given_names": "A. G. B.", "surname": "Manson", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "I. C. C. Rigby", "canonical_name": "Rigby, I. C. C.", "given_names": "I. C. C.", "surname": "Rigby", "position": "Police Magistrate", "department": "Judicial - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "G. C. Coker", "canonical_name": "Coker, G. C.", "given_names": "G. C.", "surname": "Coker", "position": "Clerk of Courts, 2nd Grade", "department": "Judicial - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Sheriff", "department": "Police - Gambia"},
    {"name": "Major R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "Captain P. Jeffs", "canonical_name": "Jeffs, P.", "given_names": "P.", "surname": "Jeffs", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "A. J. Knott", "canonical_name": "Knott, A. J.", "given_names": "A. J.", "surname": "Knott", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "R. H. Gretton", "canonical_name": "Gretton, R. H.", "given_names": "R. H.", "surname": "Gretton", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "R. G. Syme", "canonical_name": "Syme, R. G.", "given_names": "R. G.", "surname": "Syme", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "T. F. G. Hopkins", "canonical_name": "Hopkins, T. F. G.", "given_names": "T. F. G.", "surname": "Hopkins", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "K. C. Tours", "canonical_name": "Tours, K. C.", "given_names": "K. C.", "surname": "Tours", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "N. M. Assheton", "canonical_name": "Assheton, N. M.", "given_names": "N. M.", "surname": "Assheton", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "Wilson Plant", "canonical_name": "Plant, Wilson", "given_names": "Wilson", "surname": "Plant", "position": "Commissioners and Assistant Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()