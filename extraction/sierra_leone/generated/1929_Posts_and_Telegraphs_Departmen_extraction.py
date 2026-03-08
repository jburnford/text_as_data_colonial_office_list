"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "C. V. Magill", "canonical_name": "Magill, C. V.", "given_names": "C. V.", "surname": "Magill", "position": "Director of Posts and Telegraphs", "department": "Posts and Telegraphs Department - Sierra Leone", "salary_min": 800, "salary_max": 800},
    {"name": "G. G. Kellie", "canonical_name": "Kellie, G. G.", "given_names": "G. G.", "surname": "Kellie", "position": "Postal Assistant Director of Posts and Telegraphs", "department": "Posts and Telegraphs Department - Sierra Leone", "salary_min": 450, "salary_max": 700},
    {"name": "G. Hill", "canonical_name": "Hill, G.", "given_names": "G.", "surname": "Hill", "position": "Telegraph Assistant Director", "department": "Posts and Telegraphs Department - Sierra Leone", "salary_min": 460, "salary_max": 700},
    {"name": "L. H. Macnaghten", "canonical_name": "Macnaghten, L. H.", "given_names": "L. H.", "surname": "Macnaghten", "position": "Director", "department": "Public Works Department - Sierra Leone", "salary_min": 900, "salary_max": 900},
    {"name": "A. T. R. Crimson", "canonical_name": "Crimson, A. T. R.", "given_names": "A. T. R.", "surname": "Crimson", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 450, "salary_max": 700},
    {"name": "R. A. Farquharson", "canonical_name": "Farquharson, R. A.", "given_names": "R. A.", "surname": "Farquharson", "position": "Director of Agriculture and Geologist", "department": "Director of Agriculture and Geologist - Sierra Leone", "salary_min": 900, "salary_max": 900, "qualifications": ["M.A.", "M.Sc.", "F.G.S."]},
    {"name": "T. A. B. Cocksedge", "canonical_name": "Cocksedge, T. A. B.", "given_names": "T. A. B.", "surname": "Cocksedge", "position": "Chief Veterinary Officer", "department": "Veterinary Department - Sierra Leone", "salary_min": 700, "salary_max": 800, "military_rank": "Major", "qualifications": ["M.R.C.V.S."]},
    {"name": "R. A. Farquharson", "canonical_name": "Farquharson, R. A.", "given_names": "R. A.", "surname": "Farquharson", "position": "Director of Agriculture and Geologist", "department": "Geological and Agricultural Department - Sierra Leone", "salary_min": 900, "salary_max": 900, "qualifications": ["M.A.", "M.Sc.", "F.G.S."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()