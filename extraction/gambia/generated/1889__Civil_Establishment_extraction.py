"""
Gambia Colonial Office List 1889 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1889

OFFICIALS = [
    {"name": "Gilbert T. Carter", "canonical_name": "Carter, Gilbert T.", "given_names": "Gilbert T.", "surname": "Carter", "position": "Administrator", "department": "Civil Establishment - Gambia", "salary_min": 800, "salary_max": 800, "duty_allowance": 300},
    {"name": "Robt. H. Syrett", "canonical_name": "Syrett, Robt. H.", "given_names": "Robt. H.", "surname": "Syrett", "position": "Governor's Clerk", "department": "Civil Establishment - Gambia", "salary_min": 160, "salary_max": 160},
    {"name": "M. A. Savage", "canonical_name": "Savage, M. A.", "given_names": "M. A.", "surname": "Savage", "position": "Arabic Writer and General Interpreter", "department": "Civil Establishment - Gambia", "salary_min": 50, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()