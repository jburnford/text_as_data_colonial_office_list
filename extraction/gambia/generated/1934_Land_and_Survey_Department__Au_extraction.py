"""
Gambia Colonial Office List 1934 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1934

OFFICIALS = [
    {"name": "W. H. McTurk", "canonical_name": "McTurk, W. H.", "given_names": "W. H.", "surname": "McTurk", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 600, "salary_max": 800, "allowances": "72l. seniority allowance"},
    {"name": "W. A. Small", "canonical_name": "Small, W. A.", "given_names": "W. A.", "surname": "Small", "position": "African Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "Chief Clerk, 1st Grade", "department": "Land and Survey Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "A. G. Still", "canonical_name": "Still, A. G.", "given_names": "A. G.", "surname": "Still", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 600, "salary_max": 920, "allowances": "72l. seniority allowance from 720l. and 100l. local allowance"},
    {"name": "E. H. Joiner", "canonical_name": "Joiner, E. H.", "given_names": "E. H.", "surname": "Joiner", "position": "Chief Clerk, 2nd Grade", "department": "Audit Office - Gambia", "salary_min": 160, "salary_max": 230}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()