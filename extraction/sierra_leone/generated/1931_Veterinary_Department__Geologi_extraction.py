"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "T. A. B. Cockedge", "canonical_name": "Cockedge, T. A. B.", "given_names": "T. A. B.", "surname": "Cockedge", "position": "Chief Veterinary Officer", "department": "Veterinary Department - Sierra Leone", "salary_min": 700, "salary_max": 800, "qualifications": ["M.R.C.V.S."], "military_rank": "Major"},
    {"name": "R. A. Farquharson", "canonical_name": "Farquharson, R. A.", "given_names": "R. A.", "surname": "Farquharson", "position": "Director of Agriculture and Geologist", "department": "Geological and Agricultural Department - Sierra Leone", "salary_min": 900, "salary_max": 900, "qualifications": ["M.A.", "M.Sc.", "F.G.S."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()