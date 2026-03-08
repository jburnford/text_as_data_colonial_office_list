"""
Gambia Colonial Office List 1920 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1920

OFFICIALS = [
    {"name": "the Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Inspector of Schools", "department": "Education - Gambia"},
    {"name": "C. J. Clarke", "canonical_name": "Clarke, C. J.", "given_names": "C. J.", "surname": "Clarke", "position": "Clerk to Board of Education", "department": "Education - Gambia"},
    {"name": "H. L. Pryce", "canonical_name": "Pryce, H. L.", "given_names": "H. L.", "surname": "Pryce", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 350, "salary_max": 550, "allowances": "10s. per diem travelling allowance", "per_diem": "10s. per diem travelling allowance", "honors": ["C.M.G."]},
    {"name": "E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 350, "salary_max": 550, "allowances": "10s. per diem travelling allowance", "per_diem": "10s. per diem travelling allowance", "honors": ["D.S.O."]},
    {"name": "H. F. Sproston", "canonical_name": "Sproston, H. F.", "given_names": "H. F.", "surname": "Sproston", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 350, "salary_max": 550, "allowances": "10s. per diem travelling allowance", "per_diem": "10s. per diem travelling allowance", "military_rank": "Captain"},
    {"name": "E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Travelling Commissioner", "department": "Protectorate - Gambia", "salary_min": 350, "salary_max": 550, "allowances": "10s. per diem travelling allowance", "per_diem": "10s. per diem travelling allowance", "military_rank": "Captain"},
    {"name": "H. C. T. Strange", "canonical_name": "Strange, H. C. T.", "given_names": "H. C. T.", "surname": "Strange", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 400, "salary_max": 400, "allowances": "command pay, 90l.", "honors": ["D.S.O.", "M.C."], "military_rank": "Captain"},
    {"name": "E. P. Edyvean", "canonical_name": "Edyvean, E. P.", "given_names": "E. P.", "surname": "Edyvean", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 300, "salary_max": 300, "military_rank": "Lieutenant"},
    {"name": "G. W. Woodard", "canonical_name": "Woodard, G. W.", "given_names": "G. W.", "surname": "Woodard", "position": "Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120, "per_diem": "2s. 6d. per diem messing allowance", "allowances": "2s. 6d. per diem messing allowance"},
    {"name": "Joseph Jobe", "canonical_name": "Jobe, Joseph", "given_names": "Joseph", "surname": "Jobe", "position": "Clerk and Schoolmaster", "department": "West African Frontier Force - Gambia", "salary_min": 75, "salary_max": 100}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()