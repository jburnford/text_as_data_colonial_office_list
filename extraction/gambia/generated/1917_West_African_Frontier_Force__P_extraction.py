"""
Gambia Colonial Office List 1917 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1917

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Captain Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 400, "salary_max": 400, "allowances": "command pay, 96l."},
    {"name": "W. Stanford-Samuel", "canonical_name": "Stanford-Samuel, W.", "given_names": "W.", "surname": "Stanford-Samuel", "position": "Lieutenants", "department": "West African Frontier Force - Gambia", "salary_min": 350, "salary_max": 350, "military_rank": "Capt."},
    {"name": "A. E. Coombs", "canonical_name": "Coombs, A. E.", "given_names": "A. E.", "surname": "Coombs", "position": "Lieutenants", "department": "West African Frontier Force - Gambia", "salary_min": 300, "salary_max": 300, "military_rank": "Lieuts."},
    {"name": "H. E. Allen", "canonical_name": "Allen, H. E.", "given_names": "H. E.", "surname": "Allen", "position": "Lieutenants", "department": "West African Frontier Force - Gambia", "salary_min": 300, "salary_max": 300, "military_rank": "Lieuts."},
    {"name": "J. M. B. Durham", "canonical_name": "Durham, J. M. B.", "given_names": "J. M. B.", "surname": "Durham", "position": "Lieutenants", "department": "West African Frontier Force - Gambia", "salary_min": 300, "salary_max": 300, "military_rank": "Lieuts."},
    {"name": "P. McIntosh", "canonical_name": "McIntosh, P.", "given_names": "P.", "surname": "McIntosh", "position": "Colour-Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120, "duty_allowance": 24},
    {"name": "T. Fitzsimons", "canonical_name": "Fitzsimons, T.", "given_names": "T.", "surname": "Fitzsimons", "position": "Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "G. A. Thomas", "canonical_name": "Thomas, G. A.", "given_names": "G. A.", "surname": "Thomas", "position": "Clerk and Schoolmaster", "department": "West African Frontier Force - Gambia", "salary_min": 75, "salary_max": 100},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "per_diem": "2s.3d. forage allowance"},
    {"name": "C. A. O'Farrell", "canonical_name": "O'Farrell, C. A.", "given_names": "C. A.", "surname": "O'Farrell", "position": "Assistant Superintendent", "department": "Police Force - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "2s. 3d. forage allowance"},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Inspector of Prisons", "department": "Prison - Gambia"},
    {"name": "A. E. Somer", "canonical_name": "Somer, A. E.", "given_names": "A. E.", "surname": "Somer", "position": "Gaoler", "department": "Prison - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "J. J. Bah", "canonical_name": "Bah, J. J.", "given_names": "J. J.", "surname": "Bah", "position": "Chief Warder", "department": "Prison - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "W. de Piver Jones", "canonical_name": "Jones, W. de Piver", "given_names": "W. de Piver", "surname": "Jones", "position": "Chaplain", "department": "Prison - Gambia", "acting_status": "acting"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()