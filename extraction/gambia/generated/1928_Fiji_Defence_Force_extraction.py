"""
Gambia Colonial Office List 1928 - Extracted Data
"""
COLONY = "Fiji"
YEAR = 1928

OFFICIALS = [
    {"name": "G. J. L. Golding", "canonical_name": "Golding, G. J. L.", "given_names": "G. J. L.", "surname": "Golding", "position": "Commandant", "department": "Fiji Defence Force", "military_rank": "Colonel"},
    {"name": "A. H. Stafford", "canonical_name": "Stafford, A. H.", "given_names": "A. H.", "surname": "Stafford", "position": "Adjutant", "department": "Fiji Defence Force", "salary_min": 300, "salary_max": 300, "allowances": "50l. house allowance", "military_rank": "Capt."},
    {"name": "A. W. Caten", "canonical_name": "Caten, A. W.", "given_names": "A. W.", "surname": "Caten", "position": "Bandmaster", "department": "Fiji Defence Force", "salary_min": 300, "salary_max": 300, "military_rank": "Lieut."},
    {"name": "F. Stanley", "canonical_name": "Stanley, F.", "given_names": "F.", "surname": "Stanley", "position": "Drill and Musketry Instructor", "department": "Fiji Defence Force", "salary_min": 250, "salary_max": 350, "military_rank": "Sergt.-Major"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()