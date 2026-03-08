"""
Sierra Leone Colonial Office List 1934 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1934

OFFICIALS = [
    {"name": "M. A. Greene", "canonical_name": "Greene, M. A.", "given_names": "M. A.", "surname": "Greene", "position": "Lieut.-Colonel", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 182, "honors": ["M.C."], "military_rank": "Lieut.-Colonel"},
    {"name": "E. H. D. Grimley", "canonical_name": "Grimley, E. H. D.", "given_names": "E. H. D.", "surname": "Grimley", "position": "Adjutant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 750, "per_diem": "6s. per diem", "military_rank": "Captain"},
    {"name": "F. G. Winward", "canonical_name": "Winward, F. G.", "given_names": "F. G.", "surname": "Winward", "position": "Quartermaster", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 600, "salary_max": 720, "military_rank": "Captain"},
    {"name": "W. W. Dyer", "canonical_name": "Dyer, W. W.", "given_names": "W. W.", "surname": "Dyer", "position": "Care and Maintenance", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 750, "salary_max": 750, "military_rank": "Captain"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()