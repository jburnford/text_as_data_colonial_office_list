"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "W. Bowerley", "canonical_name": "Bowerley, W.", "given_names": "W.", "surname": "Bowerley",
     "position": "Auditor", "department": "Audit Department - Gold Coast", "salary_min": 1100, "salary_max": 1100,
     "duty_allowance": 220},
    {"name": "L. G. Corney", "canonical_name": "Corney, L. G.", "given_names": "L. G.", "surname": "Corney",
     "position": "Deputy Auditor", "department": "Audit Department - Gold Coast", "salary_min": 960, "salary_max": 960,
     "duty_allowance": 96},
    {"name": "W. L. Mackinnon", "canonical_name": "Mackinnon, W. L.", "given_names": "W. L.", "surname": "Mackinnon",
     "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920,
     "allowances": "plus 72l. seniority allowance from 720l."},
    {"name": "Capt. C. Griffith", "canonical_name": "Griffith, C.", "given_names": "C.", "surname": "Griffith",
     "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920,
     "allowances": "plus 72l. seniority allowance from 720l.", "military_rank": "Captain"},
    {"name": "Capt. W. H. Lemriere", "canonical_name": "Lemriere, W. H.", "given_names": "W. H.", "surname": "Lemriere",
     "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920,
     "allowances": "plus 72l. seniority allowance from 720l.", "military_rank": "Captain"},
    {"name": "N. C. Fonnerau", "canonical_name": "Fonnerau, N. C.", "given_names": "N. C.", "surname": "Fonnerau",
     "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920,
     "allowances": "plus 72l. seniority allowance from 720l."},
    {"name": "A. C. Hands", "canonical_name": "Hands, A. C.", "given_names": "A. C.", "surname": "Hands",
     "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920,
     "allowances": "plus 72l. seniority allowance from 720l."},
    {"name": "E. H. C. Lillicrup", "canonical_name": "Lillicrup, E. H. C.", "given_names": "E. H. C.", "surname": "Lillicrup",
     "position": "Assistant Auditor", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920,
     "allowances": "plus 72l. seniority allowance from 720l."},
    {"name": "V. C. Randolph", "canonical_name": "Randolph, V. C.", "given_names": "V. C.", "surname": "Randolph",
     "position": "Chief Audit Clerk", "department": "Audit Department - Gold Coast", "salary_min": 300, "salary_max": 396},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()