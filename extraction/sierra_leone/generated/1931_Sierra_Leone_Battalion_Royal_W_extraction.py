"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "W. A. Taaffe", "canonical_name": "Taaffe, W. A.", "given_names": "W. A.", "surname": "Taaffe", "position": "Lieut.-Colonel", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 182, "military_rank": "Lieut.-Colonel"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Adjutant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "duty_allowance": 91},
    {"name": "F. G. Winward", "canonical_name": "Winward, F. G.", "given_names": "F. G.", "surname": "Winward", "position": "Quartermaster", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 600, "salary_max": 720, "military_rank": "Captain"},
    {"name": "C. A. R. M. Bolton", "canonical_name": "Bolton, C. A. R. M.", "given_names": "C. A. R. M.", "surname": "Bolton", "position": "Signal Officer", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieut."},
    {"name": "W. W. Dyer", "canonical_name": "Dyer, W. W.", "given_names": "W. W.", "surname": "Dyer", "position": "Care and Maintenance", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 750, "salary_max": 750, "military_rank": "Capt."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()