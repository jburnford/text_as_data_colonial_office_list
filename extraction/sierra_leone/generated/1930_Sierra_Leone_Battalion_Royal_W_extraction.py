"""
Sierra Leone Colonial Office List 1930 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1930

OFFICIALS = [
    {"name": "W. A. Taaffe", "canonical_name": "Taaffe, W. A.", "given_names": "W. A.", "surname": "Taaffe", "position": "Major", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 850, "salary_max": 850, "duty_allowance": 182, "military_rank": "Major"},
    {"name": "F. J. Williams", "canonical_name": "Williams, F. J.", "given_names": "F. J.", "surname": "Williams", "position": "Adjutant", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "duty_allowance": 91, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "F. G. Winward", "canonical_name": "Winward, F. G.", "given_names": "F. G.", "surname": "Winward", "position": "Quartermaster", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 600, "salary_max": 720, "military_rank": "Captain"},
    {"position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600},
    {"name": "E. R. Harrison", "canonical_name": "Harrison, E. R.", "given_names": "E. R.", "surname": "Harrison", "position": "Signal Officer", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "allowances": "46l. signalling allowance", "military_rank": "Lieut."},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()