"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "R. F. Havart", "canonical_name": "Havart, R. F.", "given_names": "R. F.", "surname": "Havart", "position": "Chief Electrical Engineer", "department": "Electricity - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "J. A. Wild", "canonical_name": "Wild, J. A.", "given_names": "J. A.", "surname": "Wild", "position": "Electrical Engineer", "department": "Electricity - Sierra Leone", "salary_scale": "A"},
    {"name": "G. W. Hutchison", "canonical_name": "Hutchison, G. W.", "given_names": "G. W.", "surname": "Hutchison", "position": "Senior Station Superintendent", "department": "Electricity - Sierra Leone", "salary_scale": "C.2"},
    {"name": "R. I. A. Aubee", "canonical_name": "Aubee, R. I. A.", "given_names": "R. I. A.", "surname": "Aubee", "position": "Accountant", "department": "Electricity - Sierra Leone", "salary_scale": "B", "honors": ["M.B.E."]},
    {"name": "D. W. Abbott", "canonical_name": "Abbott, D. W.", "given_names": "D. W.", "surname": "Abbott", "position": "Senior Assistant Land Drainage Engineer", "department": "Land Drainage - Sierra Leone", "salary_scale": "A"},
    {"name": "W. G. Ash", "canonical_name": "Ash, W. G.", "given_names": "W. G.", "surname": "Ash", "position": "Public Relations Officer", "department": "Public Relations - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()