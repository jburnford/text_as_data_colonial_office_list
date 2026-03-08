"""
Sierra Leone Colonial Office List 1950 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1950

OFFICIALS = [
    {"name": "W. Venner", "canonical_name": "Venner, W.", "given_names": "W.", "surname": "Venner", "position": "General Manager", "department": "RAILWAY - Sierra Leone", "salary_min": 1400, "salary_max": 1400},
    {"name": "D. W. Fulton", "canonical_name": "Fulton, D. W.", "given_names": "D. W.", "surname": "Fulton", "position": "Chief Accountant", "department": "RAILWAY - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "S. G. Whittles", "canonical_name": "Whittles, S. G.", "given_names": "S. G.", "surname": "Whittles", "position": "Assistant Accountant", "department": "RAILWAY - Sierra Leone", "salary_scale": "B"},
    {"name": "C. F. Donovan", "canonical_name": "Donovan, C. F.", "given_names": "C. F.", "surname": "Donovan", "position": "Stores Superintendent", "department": "RAILWAY - Sierra Leone", "salary_scale": "C.3"},
    {"name": "R. E. Broomfield", "canonical_name": "Broomfield, R. E.", "given_names": "R. E.", "surname": "Broomfield", "position": "Chief Engineer", "department": "RAILWAY - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "E. F. Draper", "canonical_name": "Draper, E. F.", "given_names": "E. F.", "surname": "Draper", "position": "Assistant Engineer", "department": "RAILWAY - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Astley", "canonical_name": "Astley, J.", "given_names": "J.", "surname": "Astley", "position": "Assistant Engineer", "department": "RAILWAY - Sierra Leone", "salary_scale": "A"},
    {"name": "A. D. Eaton", "canonical_name": "Eaton, A. D.", "given_names": "A. D.", "surname": "Eaton", "position": "Assistant Engineer", "department": "RAILWAY - Sierra Leone", "salary_scale": "A"},
    {"name": "R. G. Wickham", "canonical_name": "Wickham, R. G.", "given_names": "R. G.", "surname": "Wickham", "position": "Chief Mechanical Engineer", "department": "RAILWAY - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "J. R. Best", "canonical_name": "Best, J. R.", "given_names": "J. R.", "surname": "Best", "position": "Assistant Locomotive Superintendent", "department": "RAILWAY - Sierra Leone", "salary_scale": "A"},
    {"name": "W. G. Woods", "canonical_name": "Woods, W. G.", "given_names": "W. G.", "surname": "Woods", "position": "Works Manager", "department": "RAILWAY - Sierra Leone", "salary_scale": "A"},
    {"name": "W. Haresign", "canonical_name": "Haresign, W.", "given_names": "W.", "surname": "Haresign", "position": "Assistant Works Manager", "department": "RAILWAY - Sierra Leone", "salary_scale": "C.1, 2, 3"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()