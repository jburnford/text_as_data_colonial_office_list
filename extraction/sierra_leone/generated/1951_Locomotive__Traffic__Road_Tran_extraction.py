"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "R. G. Wickham", "canonical_name": "Wickham, R. G.", "given_names": "R. G.", "surname": "Wickham", "position": "Chief Mechanical Engineer", "department": "Locomotive - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "J. R. Best", "canonical_name": "Best, J. R.", "given_names": "J. R.", "surname": "Best", "position": "Locomotive Superintendent", "department": "Locomotive - Sierra Leone", "salary_scale": "A"},
    {"name": "W. G. Woods", "canonical_name": "Woods, W. G.", "given_names": "W. G.", "surname": "Woods", "position": "Works Manager", "department": "Locomotive - Sierra Leone", "salary_scale": "A"},
    {"name": "W. Haresign", "canonical_name": "Haresign, W.", "given_names": "W.", "surname": "Haresign", "position": "Assistant Works Manager", "department": "Locomotive - Sierra Leone", "salary_scale": "C.1, 2, 3"},
    {"name": "A. R. G. Saunders", "canonical_name": "Saunders, A. R. G.", "given_names": "A. R. G.", "surname": "Saunders", "position": "Traffic Manager", "department": "Traffic - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "J. H. Yorston", "canonical_name": "Yorston, J. H.", "given_names": "J. H.", "surname": "Yorston", "position": "Traffic Superintendent", "department": "Traffic - Sierra Leone", "salary_scale": "B", "military_rank": "Captain"},
    {"name": "P. S. Terry", "canonical_name": "Terry, P. S.", "given_names": "P. S.", "surname": "Terry", "position": "Assistant Traffic Superintendent", "department": "Traffic - Sierra Leone", "salary_scale": "B"},
    {"name": "F. W. Letchford", "canonical_name": "Letchford, F. W.", "given_names": "F. W.", "surname": "Letchford", "position": "Assistant Locomotive Superintendent", "department": "Traffic - Sierra Leone", "salary_scale": "A"},
    {"name": "J. W. Stobart", "canonical_name": "Stobart, J. W.", "given_names": "J. W.", "surname": "Stobart", "position": "Manager", "department": "Road Transport - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "A. Forbes", "canonical_name": "Forbes, A.", "given_names": "A.", "surname": "Forbes", "position": "Mechanical Superintendent", "department": "Road Transport - Sierra Leone", "salary_scale": "C.2, 3"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()