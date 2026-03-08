"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "V. B. Thurston", "canonical_name": "Thurston, V. B.", "given_names": "V. B.", "surname": "Thurston", "position": "Captain Commanding", "department": "West African Frontier Force", "salary_min": 400, "salary_max": 400, "military_rank": "Captain", "allowances": "command pay, 96l."},
    {"name": "A. M. Inglis", "canonical_name": "Inglis, A. M.", "given_names": "A. M.", "surname": "Inglis", "position": "Lieutenants", "department": "West African Frontier Force", "salary_min": 350, "salary_max": 350, "military_rank": "Lieut."},
    {"name": "H. G. V. M. Freeman", "canonical_name": "Freeman, H. G. V. M.", "given_names": "H. G. V. M.", "surname": "Freeman", "position": "Lieutenants", "department": "West African Frontier Force", "salary_min": 325, "salary_max": 325, "military_rank": "Lieut."},
    {"name": "K. Markham-Rose", "canonical_name": "Markham-Rose, K.", "given_names": "K.", "surname": "Markham-Rose", "position": "Lieutenants", "department": "West African Frontier Force", "salary_min": 325, "salary_max": 325, "military_rank": "Lieut."},
    {"name": "P. McIntosh", "canonical_name": "McIntosh, P.", "given_names": "P.", "surname": "McIntosh", "position": "Colour-Sergeant", "department": "West African Frontier Force", "salary_min": 120, "salary_max": 120, "duty_allowance": 24},
    {"name": "T. Fitzsimons", "canonical_name": "Fitzsimons, T.", "given_names": "T.", "surname": "Fitzsimons", "position": "Sergeant", "department": "West African Frontier Force", "salary_min": 120, "salary_max": 120},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "per_diem": "2s.3d. forage allowance per diem"},
    {"name": "C. A. O'Farrell", "canonical_name": "O'Farrell, C. A.", "given_names": "C. A.", "surname": "O'Farrell", "position": "Assistant Superintendent", "department": "Police Force - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "2s.3d. forage allowance per diem"},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Inspector of Prisons", "department": "Prison - Gambia"},
    {"name": "A. E. Somer", "canonical_name": "Somer, A. E.", "given_names": "A. E.", "surname": "Somer", "position": "Gaoler", "department": "Prison - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Warder", "department": "Prison - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "Rev. T. F. Nicholas", "canonical_name": "Nicholas, T. F.", "given_names": "T. F.", "surname": "Nicholas", "position": "Chaplain", "department": "Prison - Gambia", "qualifications": ["M.A."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()