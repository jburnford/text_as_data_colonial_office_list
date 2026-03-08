"""
Gambia Colonial Office List 1889 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1889

OFFICIALS = [
    {"name": "J. T. Coker", "canonical_name": "Coker, J. T.", "given_names": "J. T.", "surname": "Coker", "position": "Government Printer", "department": "Government Printing Office - Gambia", "salary_min": 75, "salary_max": 75},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Assistant Printer", "department": "Government Printing Office - Gambia", "salary_min": 24, "salary_max": 24}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()