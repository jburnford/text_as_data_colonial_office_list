"""
Gambia Colonial Office List 1939 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1939

OFFICIALS = [
    {"name": "Sir (Wilfrid) Thomas Southorn", "canonical_name": "Southorn, (Wilfrid) Thomas", "given_names": "Wilfrid Thomas", "surname": "Southorn", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 550, "honors": ["K.C.M.G.", "K.B.E."]},
    {"name": "Captain T. N. Hawtin", "canonical_name": "Hawtin, T. N.", "given_names": "T. N.", "surname": "Hawtin", "position": "Aide-de-Camp and Private Secretary", "department": "Civil Establishment - Gambia", "military_rank": "Captain"},
    {"name": "H. R. Oke", "canonical_name": "Oke, H. R.", "given_names": "H. R.", "surname": "Oke", "position": "Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "honors": ["C.M.G.", "M.C."]},
    {"name": "G. Amos", "canonical_name": "Amos, G.", "given_names": "G.", "surname": "Amos", "position": "Office Assistant", "department": "Civil Establishment - Gambia", "salary_min": 400, "salary_max": 600, "honors": ["M.B.E."]},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "African Assistant Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 300, "salary_max": 450},
    {"name": "F. D. D. Roach", "canonical_name": "Roach, F. D. D.", "given_names": "F. D. D.", "surname": "Roach", "position": "Chief Clerk, 1st Grade", "department": "Civil Establishment - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "A. J. Samuel", "canonical_name": "Samuel, A. J.", "given_names": "A. J.", "surname": "Samuel", "position": "Government Printer", "department": "Civil Establishment - Gambia", "salary_min": 260, "salary_max": 360}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()