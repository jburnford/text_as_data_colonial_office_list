"""
Sierra Leone Colonial Office List 1913 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1913

OFFICIALS = [
    {"name": "A. C. Hollis", "canonical_name": "Hollis, A. C.", "given_names": "A. C.", "surname": "Hollis", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "honors": ["C.M.G."]},
    {"name": "E. E. Evelyn", "canonical_name": "Evelyn, E. E.", "given_names": "E. E.", "surname": "Evelyn", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100, "honors": ["I.S.O."]},
    {"name": "A. Farrar", "canonical_name": "Farrar, A.", "given_names": "A.", "surname": "Farrar", "position": "Asst. Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 500, "duty_allowance": 80},
    {"name": "R. W. H. Wilkinson", "canonical_name": "Wilkinson, R. W. H.", "given_names": "R. W. H.", "surname": "Wilkinson", "position": "Asst. Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 300, "salary_max": 400},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()