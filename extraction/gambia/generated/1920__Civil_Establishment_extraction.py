"""
Gambia Colonial Office List 1920 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1920

OFFICIALS = [
    {"name": "Sir Edward J. Cameron", "canonical_name": "Cameron, Edward J.", "given_names": "Edward J.", "surname": "Cameron", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 2500, "salary_max": 2500, "honors": ["K.C.M.G."]},
    {"name": "C. S. Masser", "canonical_name": "Masser, C. S.", "given_names": "C. S.", "surname": "Masser", "position": "Private Secretary", "department": "Civil Establishment - Gambia", "salary_min": 250, "salary_max": 250, "per_diem": "2s. 3d. per diem forage allowance"},
    {"name": "B. D. Wright", "canonical_name": "Wright, B. D.", "given_names": "B. D.", "surname": "Wright", "position": "1st Grade Clerk", "department": "Civil Establishment - Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "M. L. Valantine", "canonical_name": "Valantine, M. L.", "given_names": "M. L.", "surname": "Valantine", "position": "2nd Grade Clerk", "department": "Civil Establishment - Gambia", "salary_min": 50, "salary_max": 70}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()