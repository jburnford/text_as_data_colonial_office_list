"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Lieut.-Col. H. W. M. Bamford", "canonical_name": "Bamford, H. W. M.", "given_names": "H. W. M.", "surname": "Bamford",
     "position": "Commandant", "department": "Northern Territories Constabulary - Gold Coast", "salary_min": 960, "duty_allowance": 96, "military_rank": "Lieut.-Colonel", "honors": ["O.B.E.", "M.C."]},
    {"name": "Captain J. S. Massie", "canonical_name": "Massie, J. S.", "given_names": "J. S.", "surname": "Massie",
     "position": "Adjutant, and 2nd in Command", "department": "Northern Territories Constabulary - Gold Coast", "salary_min": 720, "salary_max": 920, "seniority_allowance": 72, "military_rank": "Captain"},
    {"name": "Lieut. F. R. Westbrook", "canonical_name": "Westbrook, F. R.", "given_names": "F. R.", "surname": "Westbrook",
     "position": "Senior Assistant Commandant", "department": "Northern Territories Constabulary - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72, "military_rank": "Lieut."},
    {"name": "Captain G. M. Downer", "canonical_name": "Downer, G. M.", "given_names": "G. M.", "surname": "Downer",
     "position": "Assistant Commandant", "department": "Northern Territories Constabulary - Gold Coast", "salary_min": 450, "salary_max": 920, "seniority_allowance": 72, "military_rank": "Captain"},
    {"name": "Lieut. A. P. Taylor", "canonical_name": "Taylor, A. P.", "given_names": "A. P.", "surname": "Taylor",
     "position": "Assistant Commandant", "department": "Northern Territories Constabulary - Gold Coast", "salary_min": 450, "salary_max": 920, "seniority_allowance": 72, "military_rank": "Lieut.", "honors": ["M.C."]},
    {"name": "S. L. Lomotey", "canonical_name": "Lomotey, S. L.", "given_names": "S. L.", "surname": "Lomotey",
     "position": "1st Class Orderly Room Clerk", "department": "Northern Territories Constabulary - Gold Coast", "salary_min": 222, "salary_max": 282},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()