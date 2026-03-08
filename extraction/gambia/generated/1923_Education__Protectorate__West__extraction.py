"""
Gambia Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1923

OFFICIALS = [
    {"name": "W. B. Coker", "canonical_name": "Coker, W. B.", "given_names": "W. B.", "surname": "Coker", "position": "Clerk to Board of Education", "department": "Education - Gambia"},
    {"name": "Dr. K. Hopkinson", "canonical_name": "Hopkinson, K.", "given_names": "K.", "surname": "Hopkinson", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 960, "honors": ["C.M.G.", "D.S.O."]},
    {"name": "Capt. E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 960},
    {"name": "Capt. R. H. H. Whitehead", "canonical_name": "Whitehead, R. H. H.", "given_names": "R. H. H.", "surname": "Whitehead", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 960, "honors": ["M.C."]},
    {"name": "Major R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 960, "honors": ["M.C."]},
    {"name": "Lt.-Col. G. E. Wannell", "canonical_name": "Wannell, G. E.", "given_names": "G. E.", "surname": "Wannell", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 960, "honors": ["D.S.O."], "military_rank": "Lt.-Col."},
    {"name": "Major L. A. W. Brooks", "canonical_name": "Brooks, L. A. W.", "given_names": "L. A. W.", "surname": "Brooks", "position": "Assistant", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 500, "military_rank": "Major"},
    {"name": "Capt. S. H. Streeter", "canonical_name": "Streeter, S. H.", "given_names": "S. H.", "surname": "Streeter", "position": "Assistant", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 500, "military_rank": "Captain"},
    {"name": "Lieut. L. C. Byrne", "canonical_name": "Byrne, L. C.", "given_names": "L. C.", "surname": "Byrne", "position": "Officer Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 700, "salary_max": 700, "honors": ["D.S.O.", "M.C."], "duty_allowance": 54, "military_rank": "Lieut."},
    {"name": "L. C. Evans", "canonical_name": "Evans, L. C.", "given_names": "L. C.", "surname": "Evans", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "F. A. Coward", "canonical_name": "Coward, F. A.", "given_names": "F. A.", "surname": "Coward", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "B. B. Moxon", "canonical_name": "Moxon, B. B.", "given_names": "B. B.", "surname": "Moxon", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "J. A. Moir", "canonical_name": "Moir, J. A.", "given_names": "J. A.", "surname": "Moir", "position": "Company Quartermaster Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 370, "salary_max": 370},
    {"name": "H. J. Jowers", "canonical_name": "Jowers, H. J.", "given_names": "H. J.", "surname": "Jowers", "position": "Platoon Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "Joseph Jobe", "canonical_name": "Jobe, Joseph", "given_names": "Joseph", "surname": "Jobe", "position": "Clerk and Schoolmaster", "department": "West African Frontier Force - Gambia", "salary_min": 90, "salary_max": 170}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()