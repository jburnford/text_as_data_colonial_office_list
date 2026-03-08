"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "W. F. Holmes", "canonical_name": "Holmes, W. F.", "given_names": "W. F.", "surname": "Holmes",
     "position": "Senior Inspector of Mines", "department": "Mines Department - Gold Coast", "salary_min": 960, "salary_max": 960,
     "duty_allowance": 96},
    {"name": "Capt. R. P. Wild", "canonical_name": "Wild, R. P.", "given_names": "R. P.", "surname": "Wild",
     "position": "Inspector of Mines", "department": "Mines Department - Gold Coast", "salary_min": 480, "salary_max": 720,
     "military_rank": "Captain"},
    {"name": "P. Bray", "canonical_name": "Bray, P.", "given_names": "P.", "surname": "Bray",
     "position": "Inspector of Machinery", "department": "Mines Department - Gold Coast", "salary_min": 480, "salary_max": 720},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()