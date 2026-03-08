"""
Gambia Colonial Office List 1949 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1949

OFFICIALS = [
    {"name": "Sir Andrew Barkworth Wright, K.C.M.G., C.B.E., M.C.", "canonical_name": "Wright, Andrew Barkworth", "given_names": "Andrew Barkworth", "surname": "Wright", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Gambia", "salary_min": 3000, "salary_max": 3000, "honors": ["K.C.M.G.", "C.B.E.", "M.C."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()