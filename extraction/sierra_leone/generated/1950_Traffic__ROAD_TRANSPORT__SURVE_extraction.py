"""
Sierra Leone Colonial Office List 1950 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1950

OFFICIALS = [
    {"name": "A. R. G. Saunders", "canonical_name": "Saunders, A. R. G.", "given_names": "A. R. G.", "surname": "Saunders", "position": "Traffic Manager", "department": "Railway - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "J. H. Yorston", "canonical_name": "Yorston, J. H.", "given_names": "J. H.", "surname": "Yorston", "position": "Assistant Traffic Superintendent", "department": "Railway - Sierra Leone", "salary_scale": "B", "military_rank": "Captain"},
    {"name": "L. Jones", "canonical_name": "Jones, L.", "given_names": "L.", "surname": "Jones", "position": "Assistant Traffic Superintendent", "department": "Railway - Sierra Leone", "salary_scale": "B"},
    {"name": "F. W. Letchford", "canonical_name": "Letchford, F. W.", "given_names": "F. W.", "surname": "Letchford", "position": "Assistant Locomotive Superintendent", "department": "Railway - Sierra Leone", "salary_scale": "A"},
    {"name": "J. W. Stobart", "canonical_name": "Stobart, J. W.", "given_names": "J. W.", "surname": "Stobart", "position": "Manager", "department": "ROAD TRANSPORT - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "A. Forbes", "canonical_name": "Forbes, A.", "given_names": "A.", "surname": "Forbes", "position": "Mechanical Superintendent", "department": "ROAD TRANSPORT - Sierra Leone", "salary_scale": "C.2, 3"},
    {"name": "R. C. Burgess", "canonical_name": "Burgess, R. C.", "given_names": "R. C.", "surname": "Burgess", "position": "Director of Surveys and Lands", "department": "SURVEYS AND LANDS - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "J. Stevenson", "canonical_name": "Stevenson, J.", "given_names": "J.", "surname": "Stevenson", "position": "Lands Officer and Senior Surveyor", "department": "SURVEYS AND LANDS - Sierra Leone", "salary_scale": "A"},
    {"name": "D. G. Glassford", "canonical_name": "Glassford, D. G.", "given_names": "D. G.", "surname": "Glassford", "position": "Surveyor", "department": "SURVEYS AND LANDS - Sierra Leone", "salary_scale": "A"},
    {"name": "D. T. Lloyd", "canonical_name": "Lloyd, D. T.", "given_names": "D. T.", "surname": "Lloyd", "position": "Surveyor", "department": "SURVEYS AND LANDS - Sierra Leone", "salary_scale": "A"},
    {"name": "T. W. Skuse", "canonical_name": "Skuse, T. W.", "given_names": "T. W.", "surname": "Skuse", "position": "Superintendent of Training", "department": "SURVEYS AND LANDS - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()