"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "A. E. Kitson", "canonical_name": "Kitson, A. E.", "given_names": "A. E.", "surname": "Kitson",
     "position": "Director of Geological Survey", "department": "Geological Survey - Gold Coast", "salary_min": 1200, "salary_max": 1200,
     "honors": ["C.M.G.", "C.B.E."], "qualifications": ["F.G.S."], "duty_allowance": 240},
    {"name": "E. O. Teale", "canonical_name": "Teale, E. O.", "given_names": "E. O.", "surname": "Teale",
     "position": "Assistant-Director of Geological Survey", "department": "Geological Survey - Gold Coast", "salary_min": 960, "salary_max": 960,
     "qualifications": ["D.Sc.", "F.G.S."], "duty_allowance": 96},
    {"name": "W. G. G. Cooper", "canonical_name": "Cooper, W. G. G.", "given_names": "W. G. G.", "surname": "Cooper",
     "position": "Assistant Geologist", "department": "Geological Survey - Gold Coast", "salary_min": 540, "salary_max": 920,
     "qualifications": ["B.Sc. (Eng.)"]},
    {"name": "Major N. R. Junner", "canonical_name": "Junner, Major N. R.", "given_names": "N. R.", "surname": "Junner",
     "position": "Assistant Geologist", "department": "Geological Survey - Gold Coast", "salary_min": 540, "salary_max": 920,
     "military_rank": "Major", "honors": ["M.C."], "qualifications": ["D.Sc."]},
    {"name": "O. A. L. Whitelaw", "canonical_name": "Whitelaw, O. A. L.", "given_names": "O. A. L.", "surname": "Whitelaw",
     "position": "Assistant Geologist", "department": "Geological Survey - Gold Coast", "salary_min": 540, "salary_max": 920},
    {"name": "W. T. James", "canonical_name": "James, W. T.", "given_names": "W. T.", "surname": "James",
     "position": "Superintendent of Records (London Office)", "department": "Geological Survey - Gold Coast"},
    {"name": "F. Oates", "canonical_name": "Oates, F.", "given_names": "F.", "surname": "Oates",
     "position": "Assistant to Director", "department": "Geological Survey - Gold Coast", "salary_min": 480, "salary_max": 920,
     "honors": ["M.B.E."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()