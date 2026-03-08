"""
Sierra Leone Colonial Office List 1921 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1921

OFFICIALS = [
    {"name": "C. Wilkins", "canonical_name": "Wilkins, C.", "given_names": "C.", "surname": "Wilkins", "position": "Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "V. S. Bryan", "canonical_name": "Bryan, V. S.", "given_names": "V. S.", "surname": "Bryan", "position": "Deputy Treasurer", "department": "Treasury - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "Sydney Turner", "canonical_name": "Turner, Sydney", "given_names": "Sydney", "surname": "Turner", "position": "Assistant Treasurer", "department": "Treasury - Sierra Leone", "honors": ["M.C."], "salary_min": 300, "salary_max": 600},
    {"name": "G. R. Breading", "canonical_name": "Breading, G. R.", "given_names": "G. R.", "surname": "Breading", "position": "Commandant", "department": "Police - Sierra Leone", "honors": ["D.S.O."], "military_rank": "Lt.-Col.", "salary_min": 700, "salary_max": 700},
    {"name": "J. H. Bloomburgh", "canonical_name": "Bloomburgh, J. H.", "given_names": "J. H.", "surname": "Bloomburgh", "position": "Assistant Commandant", "department": "Police - Sierra Leone", "honors": ["O.B.E."], "military_rank": "Capt.", "salary_min": 500, "salary_max": 600},
    {"name": "E. N. Park", "canonical_name": "Park, E. N.", "given_names": "E. N.", "surname": "Park", "position": "District Police Officer", "department": "Police - Sierra Leone", "honors": ["M.C."], "military_rank": "Capt.", "salary_min": 400, "salary_max": 500},
    {"name": "J. Beattie", "canonical_name": "Beattie, J.", "given_names": "J.", "surname": "Beattie", "position": "District Police Officer", "department": "Police - Sierra Leone", "honors": ["M.C."], "military_rank": "Lieut.", "salary_min": 400, "salary_max": 500},
    {"name": "R. H. Smith", "canonical_name": "Smith, R. H.", "given_names": "R. H.", "surname": "Smith", "position": "District Police Officer", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "B. H. Horsley", "canonical_name": "Horsley, B. H.", "given_names": "B. H.", "surname": "Horsley", "position": "District Police Officer", "department": "Police - Sierra Leone", "honors": ["D.S.O.", "M.C."], "military_rank": "Major", "salary_min": 400, "salary_max": 500},
    {"name": "N. S. Mansergh", "canonical_name": "Mansergh, N. S.", "given_names": "N. S.", "surname": "Mansergh", "position": "District Police Officer", "department": "Police - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "Assistant Commandant of Police", "canonical_name": "Assistant Commandant of Police", "surname": "Assistant Commandant of Police", "position": "Director", "department": "Prisons - Sierra Leone"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()