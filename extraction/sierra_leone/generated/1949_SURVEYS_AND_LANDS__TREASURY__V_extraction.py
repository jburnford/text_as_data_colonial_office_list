"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "R. C. Burgess", "canonical_name": "Burgess, R. C.", "given_names": "R. C.", "surname": "Burgess", "position": "Director of Surveys and Lands", "department": "SURVEYS AND LANDS - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "J. Stevenson", "canonical_name": "Stevenson, J.", "given_names": "J.", "surname": "Stevenson", "position": "Lands Officer and Senior Surveyor", "department": "SURVEYS AND LANDS - Sierra Leone", "salary_scale": "A"},
    {"name": "D. G. Glassford", "canonical_name": "Glassford, D. G.", "given_names": "D. G.", "surname": "Glassford", "position": "Surveyors", "department": "SURVEYS AND LANDS - Sierra Leone", "salary_scale": "A"},
    {"name": "D. T. Lloyd", "canonical_name": "Lloyd, D. T.", "given_names": "D. T.", "surname": "Lloyd", "position": "Surveyors", "department": "SURVEYS AND LANDS - Sierra Leone", "salary_scale": "A"},
    {"name": "T. W. Skuse", "canonical_name": "Skuse, T. W.", "given_names": "T. W.", "surname": "Skuse", "position": "Superintendent of Training", "department": "SURVEYS AND LANDS - Sierra Leone", "salary_scale": "A"},
    {"name": "C. J. Hodgens", "canonical_name": "Hodgens, C. J.", "given_names": "C. J.", "surname": "Hodgens", "position": "Colonial Treasurer", "department": "TREASURY - Sierra Leone", "salary_min": 1350, "salary_max": 1350, "honors": ["C.B.E.", "M.C."]},
    {"name": "W. D. A. Jones", "canonical_name": "Jones, W. D. A.", "given_names": "W. D. A.", "surname": "Jones", "position": "Deputy Treasurer", "department": "TREASURY - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "D. O. T. Fountain", "canonical_name": "Fountain, D. O. T.", "given_names": "D. O. T.", "surname": "Fountain", "position": "Assistant Treasurers", "department": "TREASURY - Sierra Leone", "salary_scale": "B"},
    {"name": "S. E. Joah", "canonical_name": "Joah, S. E.", "given_names": "S. E.", "surname": "Joah", "position": "Assistant Treasurers", "department": "TREASURY - Sierra Leone", "salary_scale": "B", "honors": ["I.S.O."]},
    {"name": "J. M. Williams", "canonical_name": "Williams, J. M.", "given_names": "J. M.", "surname": "Williams", "position": "Assistant Treasurers", "department": "TREASURY - Sierra Leone", "salary_scale": "B"},
    {"name": "A. Fulton", "canonical_name": "Fulton, A.", "given_names": "A.", "surname": "Fulton", "position": "Director of Veterinary Services", "department": "VETERINARY - Sierra Leone", "salary_min": 1150, "salary_max": 1150}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()