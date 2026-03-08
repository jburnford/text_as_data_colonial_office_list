"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "R. G. Wickham", "canonical_name": "Wickham, R. G.", "given_names": "R. G.", "surname": "Wickham", "position": "Chief Mechanical Engineer", "department": "Railway - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "J. R. Best", "canonical_name": "Best, J. R.", "given_names": "J. R.", "surname": "Best", "position": "Assistant Locomotive Superintendent", "department": "Railway - Sierra Leone", "salary_scale": "A"},
    {"name": "W. G. Woods", "canonical_name": "Woods, W. G.", "given_names": "W. G.", "surname": "Woods", "position": "Works Manager", "department": "Railway - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Hamilton", "canonical_name": "Hamilton, J.", "given_names": "J.", "surname": "Hamilton", "position": "Traffic Manager", "department": "Railway - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "J. H. Yorston", "canonical_name": "Yorston, J. H.", "given_names": "J. H.", "surname": "Yorston", "position": "Assistant Traffic Superintendent", "department": "Railway - Sierra Leone", "salary_scale": "B", "military_rank": "Captain"},
    {"name": "L. Jones", "canonical_name": "Jones, L.", "given_names": "L.", "surname": "Jones", "position": "Assistant Traffic Superintendent", "department": "Railway - Sierra Leone", "salary_scale": "B"},
    {"name": "F. W. Letchford", "canonical_name": "Letchford, F. W.", "given_names": "F. W.", "surname": "Letchford", "position": "Assistant Locomotive Superintendent", "department": "Railway - Sierra Leone", "salary_scale": "A"},
    {"name": "J. W. Stobart", "canonical_name": "Stobart, J. W.", "given_names": "J. W.", "surname": "Stobart", "position": "Manager", "department": "ROAD TRANSPORT - Sierra Leone", "salary_min": 900, "salary_max": 900},
    {"name": "A. Forbes", "canonical_name": "Forbes, A.", "given_names": "A.", "surname": "Forbes", "position": "Mechanical Superintendent", "department": "ROAD TRANSPORT - Sierra Leone", "salary_scale": "C2.3"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()