"""
Gambia Colonial Office List 1934 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1934

OFFICIALS = [
    {"name": "W. K. Horne", "canonical_name": "Horne, W. K.", "given_names": "W. K.", "surname": "Horne", "position": "Judge of the Supreme Court", "department": "Legal Department - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "A. G. B. Manson", "canonical_name": "Manson, A. G. B.", "given_names": "A. G. B.", "surname": "Manson", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "M. D. Lyon", "canonical_name": "Lyon, M. D.", "given_names": "M. D.", "surname": "Lyon", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 600, "salary_max": 800},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "Clerk of Courts, 1st Grade", "department": "Legal Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Sheriff", "department": "Legal Department - Gambia"},
    {"name": "Capt. E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["O.B.E."], "military_rank": "Captain"},
    {"name": "Major R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "Captain H. R. Oke", "canonical_name": "Oke, H. R.", "given_names": "H. R.", "surname": "Oke", "position": "Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"},
    {"name": "Captain P. Jeffs", "canonical_name": "Jeffs, P.", "given_names": "P.", "surname": "Jeffs", "position": "Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "A. R. Clark", "canonical_name": "Clark, A. R.", "given_names": "A. R.", "surname": "Clark", "position": "Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "W. T. Hamlyn", "canonical_name": "Hamlyn, W. T.", "given_names": "W. T.", "surname": "Hamlyn", "position": "Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "G. N. N. Nunn", "canonical_name": "Nunn, G. N. N.", "given_names": "G. N. N.", "surname": "Nunn", "position": "Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "N. M. Asheton", "canonical_name": "Asheton, N. M.", "given_names": "N. M.", "surname": "Asheton", "position": "Commissioners", "department": "Provincial Administration - Gambia", "salary_min": 450, "salary_max": 960},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()