"""
Gambia Colonial Office List 1936 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1936

OFFICIALS = [
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Commissioner", "department": "Police Force - Gambia", "salary_min": 720, "salary_max": 920, "duty_allowance": 72},
    {"name": "R. L. Hill", "canonical_name": "Hill, R. L.", "given_names": "R. L.", "surname": "Hill", "position": "Assistant", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 720, "military_rank": "Capt."},
    {"name": "W. Collins", "canonical_name": "Collins, W.", "given_names": "W.", "surname": "Collins", "position": "Superintendent", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "T. A. Medhurst", "canonical_name": "Medhurst, T. A.", "given_names": "T. A.", "surname": "Medhurst", "position": "Bandmaster", "department": "Police Force - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "H. L. Webley", "canonical_name": "Webley, H. L.", "given_names": "H. L.", "surname": "Webley", "position": "Inspector of Prisons", "department": "Prison - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()