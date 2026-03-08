"""
Gold Coast Colonial Office List 1920 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1920

OFFICIALS = [
    {"name": "F. M. Hodgson", "canonical_name": "Hodgson, F. M.", "given_names": "F. M.", "surname": "Hodgson", "position": "Governor", "department": "Civil Establishment - Gold Coast", "salary_min": 3000, "salary_max": 3000, "allowances": "500l. table allowance", "honors": ["C.M.G."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()