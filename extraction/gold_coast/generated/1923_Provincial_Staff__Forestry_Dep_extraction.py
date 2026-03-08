"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "N. C. McLeod", "position": "Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 1200, "duty_allowance": 240},
    {"name": "Capt. R. W. Brent", "canonical_name": "Brent, Capt. R. W.", "given_names": "R. W.", "surname": "Brent", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920, "military_rank": "Captain", "honors": ["M.C."]},
    {"name": "N. T. Garnett", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920},
    {"name": "P. G. Arnold", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920},
    {"name": "Capt. G. S. Greene", "canonical_name": "Greene, Capt. G. S.", "given_names": "G. S.", "surname": "Greene", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920, "military_rank": "Captain"},
    {"name": "L. C. Rowney", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920},
    {"name": "J. A. Wills", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920},
    {"name": "F. Burnett", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920},
    {"name": "C. Vigne", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920},
    {"name": "D. Hendry", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920},
    {"name": "J. D. MacAinsh", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920},
    {"name": "H. W. Moore", "position": "Assistant Conservator of Forests", "department": "Forestry Department - Gold Coast", "salary_min": 480, "salary_max": 920},
    {"name": "L. V. Wilcox", "position": "European Forester", "department": "Forestry Department - Gold Coast", "salary_min": 440, "salary_max": 500},
    {"name": "B. Bennett", "position": "European Forester", "department": "Forestry Department - Gold Coast", "salary_min": 440, "salary_max": 500},
    {"name": "F. C. Coleman", "position": "Saw Doctor", "department": "Forestry Department - Gold Coast", "salary_min": 440, "salary_max": 500},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()