"""
Sierra Leone Colonial Office List 1939 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1939

OFFICIALS = [
    {"name": "H. U. Richards", "canonical_name": "Richards, H. U.", "given_names": "H. U.", "surname": "Richards", "position": "Lieut.-Colonel", "department": "Sierra Leone Battalion, Royal West African Frontier Force", "salary_min": 1000, "salary_max": 1000, "per_diem": "10s. a day duty allowance", "military_rank": "Lt.-Col."},
    {"name": "L. H. Bean", "canonical_name": "Bean, L. H.", "given_names": "L. H.", "surname": "Bean", "position": "Second-in-Command", "department": "Sierra Leone Battalion, Royal West African Frontier Force", "salary_min": 850, "salary_max": 850, "military_rank": "Major"},
    {"name": "E. J. O'B. Croker", "canonical_name": "Croker, E. J. O'B.", "given_names": "E. J. O'B.", "surname": "Croker", "position": "Adjutant", "department": "Sierra Leone Battalion, Royal West African Frontier Force", "salary_min": 510, "salary_max": 600, "per_diem": "5s. per diem", "military_rank": "Capt."},
    {"name": "W. W. King", "canonical_name": "King, W. W.", "given_names": "W. W.", "surname": "King", "position": "Quartermaster", "department": "Sierra Leone Battalion, Royal West African Frontier Force", "salary_min": 600, "salary_max": 700, "military_rank": "Captain"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()