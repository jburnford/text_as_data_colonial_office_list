"""
Sierra Leone Colonial Office List 1936 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1936

OFFICIALS = [
    {"name": "G. P. Harding", "canonical_name": "Harding, G. P.", "given_names": "G. P.", "surname": "Harding", "position": "Lieut.-Colonel", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 182, "honors": ["M.C."], "military_rank": "Lieut.-Colonel"},
    {"name": "R. H. D. Grimley", "canonical_name": "Grimley, R. H. D.", "given_names": "R. H. D.", "surname": "Grimley", "position": "Adjutant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 750, "per_diem": "5s. per diem", "military_rank": "Captain"},
    {"name": "F. G. Winward", "canonical_name": "Winward, F. G.", "given_names": "F. G.", "surname": "Winward", "position": "Quartermaster", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 600, "salary_max": 700, "honors": ["M.B.E."], "military_rank": "Captain"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()