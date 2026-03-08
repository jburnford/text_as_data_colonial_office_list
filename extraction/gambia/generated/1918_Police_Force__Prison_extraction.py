"""
Gambia Colonial Office List 1918 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1918

OFFICIALS = [
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 50, "per_diem": "2s.3d. forage allowance per diem"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Superintendent", "department": "Police Force - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "2s. 3d. forage allowance per diem"},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Inspector of Prisons", "department": "Prison - Gambia"},
    {"name": "A. E. Somer", "canonical_name": "Somer, A. E.", "given_names": "A. E.", "surname": "Somer", "position": "Guards", "department": "Prison - Gambia", "salary_min": 120, "salary_max": 120, "allowances": "personal allowance 36l. per annum"},
    {"name": "J. J. Bah", "canonical_name": "Bah, J. J.", "given_names": "J. J.", "surname": "Bah", "position": "Chief Warder", "department": "Prison - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "Rev. W. de Piver Jones", "canonical_name": "Jones, Rev. W. de Piver", "given_names": "W. de Piver", "surname": "Jones", "position": "Chaplain", "department": "Prison - Gambia", "acting_status": "Acting"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()