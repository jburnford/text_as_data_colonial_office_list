"""
Gambia Colonial Office List 1913 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1913

OFFICIALS = [
    {"name": "the Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Inspector of Schools", "department": "Education - Gambia"},
    {"name": "J. F. Dailey", "canonical_name": "Dailey, J. F.", "given_names": "J. F.", "surname": "Dailey", "position": "Clerk", "department": "Education - Gambia", "salary_min": 10, "salary_max": 10},
    {"name": "T. J. Gibbs", "canonical_name": "Gibbs, T. J.", "given_names": "T. J.", "surname": "Gibbs", "position": "Town Warden", "department": "Education - Gambia", "location": "Bathurst", "salary_min": 250, "salary_max": 300},
    {"name": "H. L. Pryce", "canonical_name": "Pryce, H. L.", "given_names": "H. L.", "surname": "Pryce", "position": "Travelling Commissioner, First Class", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 500, "honors": ["C.M.G."]},
    {"name": "J. K. MacCallum", "canonical_name": "MacCallum, J. K.", "given_names": "J. K.", "surname": "MacCallum", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem travelling allowance"},
    {"name": "H. F. Sproston", "canonical_name": "Sproston, H. F.", "given_names": "H. F.", "surname": "Sproston", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem travelling allowance"},
    {"name": "E. B. Leese", "canonical_name": "Leese, E. B.", "given_names": "E. B.", "surname": "Leese", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem travelling allowance", "military_rank": "Captain"},
    {"name": "E. Hopkinson", "canonical_name": "Hopkinson, E.", "given_names": "E.", "surname": "Hopkinson", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "10s. per diem travelling allowance"},
    {"name": "V. B. Thurston", "canonical_name": "Thurston, V. B.", "given_names": "V. B.", "surname": "Thurston", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 400, "salary_max": 400, "duty_allowance": 96, "military_rank": "Captain"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Lieutenants", "department": "West African Frontier Force - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "H. G. V. M. Freeman", "canonical_name": "Freeman, H. G. V. M.", "given_names": "H. G. V. M.", "surname": "Freeman", "position": "Lieut.", "department": "West African Frontier Force - Gambia", "salary_min": 325, "salary_max": 325},
    {"name": "W. S. Lee", "canonical_name": "Lee, W. S.", "given_names": "W. S.", "surname": "Lee", "position": "Colour-Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120, "duty_allowance": 24},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "C. A. O'Farrell", "canonical_name": "O'Farrell, C. A.", "given_names": "C. A.", "surname": "O'Farrell", "position": "Assistant Superintendent", "department": "Police Force - Gambia", "salary_min": 300, "salary_max": 400, "allowances": "forage allowance of 2s. 3d. per diem each"},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Inspector of Prisons", "department": "Prison - Gambia"},
    {"name": "A. E. Somer", "canonical_name": "Somer, A. E.", "given_names": "A. E.", "surname": "Somer", "position": "Gaoler", "department": "Prison - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "C. E. Stapleton", "canonical_name": "Stapleton, C. E.", "given_names": "C. E.", "surname": "Stapleton", "position": "Chief Warder", "department": "Prison - Gambia", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()