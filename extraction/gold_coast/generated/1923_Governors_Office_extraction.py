"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Brigadier-General Sir F. Gordon Guggisberg", "canonical_name": "Guggisberg, Sir F. Gordon", "given_names": "F. Gordon", "surname": "Guggisberg", "position": "Governor", "department": "Governor's Office - Gold Coast", "salary_min": 4500, "salary_max": 4500, "honors": ["K.C.M.G.", "D.S.O."], "military_rank": "Brigadier-General", "allowances": "plus 1,500£. duty allowance"},
    {"name": "Vincent Basevi", "canonical_name": "Basevi, Vincent", "given_names": "Vincent", "surname": "Basevi", "position": "Private Secretary", "department": "Governor's Office - Gold Coast", "salary_min": 500, "salary_max": 500},
    {"name": "Captain R. C. M. Buckby", "canonical_name": "Buckby, R. C. M.", "given_names": "R. C. M.", "surname": "Buckby", "position": "Aide-de-Camp", "department": "Governor's Office - Gold Coast", "salary_min": 500, "salary_max": 500, "military_rank": "Captain"},
    {"name": "M. C. Hanson", "canonical_name": "Hanson, M. C.", "given_names": "M. C.", "surname": "Hanson", "position": "Chief Clerk", "department": "Governor's Office - Gold Coast", "salary_min": 396, "salary_max": 396},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()