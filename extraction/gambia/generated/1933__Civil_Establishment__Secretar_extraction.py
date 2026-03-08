"""
Gambia Colonial Office List 1933 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1933

OFFICIALS = [
    {"name": "Sir Herbert R. Palmer", "canonical_name": "Palmer, Herbert R.", "given_names": "Herbert R.", "surname": "Palmer", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "duty_allowance": 750, "honors": ["K.C.M.G.", "C.B.E."]},
    {"name": "H. Lloyd-Carson", "canonical_name": "Lloyd-Carson, H.", "given_names": "H.", "surname": "Lloyd-Carson", "position": "Aide-de-Camp and Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 450, "salary_max": 450, "military_rank": "Capt."},
    {"name": "G. C. B. Parish", "canonical_name": "Parish, G. C. B.", "given_names": "G. C. B.", "surname": "Parish", "position": "Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "L. A. W. Brooks", "canonical_name": "Brooks, L. A. W.", "given_names": "L. A. W.", "surname": "Brooks", "position": "Senior Assistant Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Major"},
    {"name": "R. H. Gretton", "canonical_name": "Gretton, R. H.", "given_names": "R. H.", "surname": "Gretton", "position": "Assistant Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 450, "salary_max": 960},
    {"name": "G. Amos", "canonical_name": "Amos, G.", "given_names": "G.", "surname": "Amos", "position": "Office Assistant", "department": "Civil Establishment - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "African Assistant Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 300, "salary_max": 400},
    {"name": "J. M. Lawani", "canonical_name": "Lawani, J. M.", "given_names": "J. M.", "surname": "Lawani", "position": "Government Printer", "department": "Civil Establishment - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "H. Densham Smith", "canonical_name": "Smith, H. Densham", "given_names": "H. Densham", "surname": "Smith", "position": "Receiver-General", "department": "Civil Establishment - Gambia", "salary_min": 960, "salary_max": 960, "duty_allowance": 96}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()