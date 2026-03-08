"""
Gambia Colonial Office List 1932 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1932

OFFICIALS = [
    {"name": "A. F. V. Vaughan", "canonical_name": "Vaughan, A. F. V.", "given_names": "A. F. V.", "surname": "Vaughan", "position": "Sanitary Inspector", "department": "Health Department - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "G. P. Lawrence", "canonical_name": "Lawrence, G. P.", "given_names": "G. P.", "surname": "Lawrence", "position": "Assistant Sanitary Inspector", "department": "Health Department - Gambia", "salary_min": 350, "salary_max": 480},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()