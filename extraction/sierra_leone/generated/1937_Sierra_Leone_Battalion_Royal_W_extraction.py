"""
Sierra Leone Colonial Office List 1937 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1937

OFFICIALS = [
    {"name": "E. H. D. Grimley", "canonical_name": "Grimley, E. H. D.", "given_names": "E. H. D.", "surname": "Grimley", "position": "Lieut.-Colonel", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 182.5, "military_rank": "Lieut.-Colonel"},
    {"name": "H. L. S. Hillyard", "canonical_name": "Hillyard, H. L. S.", "given_names": "H. L. S.", "surname": "Hillyard", "position": "Adjutant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "per_diem": "5s. per diem", "military_rank": "Lt."},
    {"name": "F. G. Winward", "canonical_name": "Winward, F. G.", "given_names": "F. G.", "surname": "Winward", "position": "Quartermaster", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 600, "salary_max": 700, "honors": ["M.B.E."], "military_rank": "Captain"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()