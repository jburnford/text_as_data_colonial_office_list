"""
Gambia Colonial Office List 1914 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1914

OFFICIALS = [
    {"name": "V. B. Thurston", "canonical_name": "Thurston, V. B.", "given_names": "V. B.", "surname": "Thurston", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 400, "salary_max": 400, "per_diem": "96l.", "military_rank": "Captain"},
    {"name": "O. C. R. Hill", "canonical_name": "Hill, O. C. R.", "given_names": "O. C. R.", "surname": "Hill", "position": "Lieutenants", "department": "West African Frontier Force - Gambia", "salary_min": 350, "salary_max": 350, "military_rank": "Lieut."},
    {"name": "H. G. V. M. Freeman", "canonical_name": "Freeman, H. G. V. M.", "given_names": "H. G. V. M.", "surname": "Freeman", "position": "Lieutenants", "department": "West African Frontier Force - Gambia", "salary_min": 325, "salary_max": 325, "military_rank": "Lieut."},
    {"name": "T. Fitzsimons", "canonical_name": "Fitzsimons, T.", "given_names": "T.", "surname": "Fitzsimons", "position": "Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120, "military_rank": "Sergeant"},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "per_diem": "2s.3d. forage allowance per diem"},
    {"name": "C. A. O'Farrell", "canonical_name": "O'Farrell, C. A.", "given_names": "C. A.", "surname": "O'Farrell", "position": "Assistant Superintendent", "department": "Police Force - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "2s.3d. forage allowance per diem"},
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