"""
Gambia Colonial Office List 1920 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1920

OFFICIALS = [
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 80, "per_diem": "2s. 3d. per diem forage allowance", "military_rank": "Captain"},
    {"name": "G. L. Morehead", "canonical_name": "Morehead, G. L.", "given_names": "G. L.", "surname": "Morehead", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 300, "salary_max": 400, "per_diem": "2s. 3d. per diem forage allowance"},
    {"name": "Clinton Greig", "canonical_name": "Greig, Clinton", "given_names": "Clinton", "surname": "Greig", "position": "Inspector of Prisons", "department": "Prison - Gambia", "military_rank": "Captain"},
    {"name": "A. E. Somer", "canonical_name": "Somer, A. E.", "given_names": "A. E.", "surname": "Somer", "position": "Gaoler", "department": "Prison - Gambia", "salary_min": 120, "salary_max": 120, "allowances": "and personal allowance 36l. per annum"},
    {"name": "H. G. Meyer", "canonical_name": "Meyer, H. G.", "given_names": "H. G.", "surname": "Meyer", "position": "Chief Warder", "department": "Prison - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "W. de River Jones", "canonical_name": "Jones, W. de River", "given_names": "W. de River", "surname": "Jones", "position": "Chaplain", "department": "Prison - Gambia", "acting_status": "acting"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()