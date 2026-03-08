"""
Gambia Colonial Office List 1894 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1894

OFFICIALS = [
    {"name": "R. B. Llewelyn", "canonical_name": "Llewelyn, R. B.", "given_names": "R. B.", "surname": "Llewelyn", "position": "Administrator", "department": "Civil Establishment - Gambia", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 300, "allowances": "table allowance, 120l. per annum", "honors": ["C.M.G."]},
    {"name": "R. R. Gace", "canonical_name": "Gace, R. R.", "given_names": "R. R.", "surname": "Gace", "position": "Governor's Confidential Clerk", "department": "Civil Establishment - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "I. H. Johnson", "canonical_name": "Johnson, I. H.", "given_names": "I. H.", "surname": "Johnson", "position": "2nd Clerk", "department": "Civil Establishment - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "N. C. Nathan", "canonical_name": "Nathan, N. C.", "given_names": "N. C.", "surname": "Nathan", "position": "Clerk for Audit Duties", "department": "Civil Establishment - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "J. T. Coker", "canonical_name": "Coker, J. T.", "given_names": "J. T.", "surname": "Coker", "position": "Government Printer", "department": "Civil Establishment - Gambia", "salary_min": 90, "salary_max": 90},
    {"name": "Samuel T. George", "canonical_name": "George, Samuel T.", "given_names": "Samuel T.", "surname": "George", "position": "Assistant ditto", "department": "Civil Establishment - Gambia", "salary_min": 30, "salary_max": 30}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()