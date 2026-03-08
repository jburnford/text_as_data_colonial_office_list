"""
Gambia Colonial Office List 1899 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1899

OFFICIALS = [
    {"name": "H. M. Jackson", "canonical_name": "Jackson, H. M.", "given_names": "H. M.", "surname": "Jackson", "position": "Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 833, "salary_max": 833, "honors": ["C.M.G."], "allowances": "free house"},
    {"name": "J. C. King", "canonical_name": "King, J. C.", "given_names": "J. C.", "surname": "King", "position": "Assistant Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 303, "salary_max": 303, "allowances": "42l. as Secretary to Board of Health"},
    {"name": "J. Porral", "canonical_name": "Porral, J.", "given_names": "J.", "surname": "Porral", "position": "Chief Clerk", "department": "Civil Establishment - Gambia", "salary_min": 208, "salary_max": 208, "allowances": "50l. for translating and interpreting"},
    {"name": "E. P. Griffin", "canonical_name": "Griffin, E. P.", "given_names": "E. P.", "surname": "Griffin", "position": "1st-Class Clerk", "department": "Civil Establishment - Gambia", "salary_min": 208, "salary_max": 208},
    {"name": "J. Bruzon", "canonical_name": "Bruzon, J.", "given_names": "J.", "surname": "Bruzon", "position": "3rd-Class Clerk", "department": "Civil Establishment - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "the Colonial Secretary", "canonical_name": "Colonial Secretary, the", "surname": "Colonial Secretary", "position": "Chief Commissioner", "department": "Crown Property Department - Gambia"},
    {"name": "A. Porral", "canonical_name": "Porral, A.", "given_names": "A.", "surname": "Porral", "position": "Commissioner", "department": "Crown Property Department - Gambia", "salary_min": 233, "salary_max": 233},
    {"name": "R. Giraldi", "canonical_name": "Giraldi, R.", "given_names": "R.", "surname": "Giraldi", "position": "Clerk", "department": "Crown Property Department - Gambia", "salary_min": 154, "salary_max": 154}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()