"""
Gambia Colonial Office List 1924 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1924

OFFICIALS = [
    {"name": "the Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Inspector of Schools", "department": "Education - Gambia"},
    {"name": "W. E. Coker", "canonical_name": "Coker, W. E.", "given_names": "W. E.", "surname": "Coker", "position": "Clerk to Board of Education", "department": "Education - Gambia"},
    {"name": "E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["C.M.G.", "D.S.O."], "qualifications": ["M.D."]},
    {"name": "K. B. Leese", "canonical_name": "Leese, K. B.", "given_names": "K. B.", "surname": "Leese", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 450, "salary_max": 960, "military_rank": "Captain"},
    {"name": "R. H. H. Whitehead", "canonical_name": "Whitehead, R. H. H.", "given_names": "R. H. H.", "surname": "Whitehead", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "R. W. Macklin", "canonical_name": "Macklin, R. W.", "given_names": "R. W.", "surname": "Macklin", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["M.C."], "military_rank": "Major"},
    {"name": "G. E. Wannell", "canonical_name": "Wannell, G. E.", "given_names": "G. E.", "surname": "Wannell", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 450, "salary_max": 960, "honors": ["D.S.O."], "military_rank": "Lt.-Col."},
    {"name": "L. A. W. Brooks", "canonical_name": "Brooks, L. A. W.", "given_names": "L. A. W.", "surname": "Brooks", "position": "Assistant", "department": "Protectorate - Gambia", "salary_min": 450, "military_rank": "Major"},
    {"name": "S. H. Streeter", "canonical_name": "Streeter, S. H.", "given_names": "S. H.", "surname": "Streeter", "position": "Assistant", "department": "Protectorate - Gambia", "salary_min": 450, "military_rank": "Captain"},
    {"name": "H. E. Allen", "canonical_name": "Allen, H. E.", "given_names": "H. E.", "surname": "Allen", "position": "Officer Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 700, "salary_max": 700, "duty_allowance": 54, "military_rank": "Captain"},
    {"name": "F. A. Coward", "canonical_name": "Coward, F. A.", "given_names": "F. A.", "surname": "Coward", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "B. B. Moxon", "canonical_name": "Moxon, B. B.", "given_names": "B. B.", "surname": "Moxon", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "T. F. Fischer", "canonical_name": "Fischer, T. F.", "given_names": "T. F.", "surname": "Fischer", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 510, "salary_max": 510},
    {"name": "J. A. Moir", "canonical_name": "Moir, J. A.", "given_names": "J. A.", "surname": "Moir", "position": "Company Quartermaster Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 370, "salary_max": 370},
    {"name": "W. Boon", "canonical_name": "Boon, W.", "given_names": "W.", "surname": "Boon", "position": "Platoon Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Clerk and Schoolmaster", "department": "West African Frontier Force - Gambia", "salary_min": 50, "salary_max": 82}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()