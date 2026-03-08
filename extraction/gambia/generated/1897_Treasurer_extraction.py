"""
Gambia Colonial Office List 1897 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1897

OFFICIALS = [
    {"name": "J. T. Coker", "canonical_name": "Coker, J. T.", "given_names": "J. T.", "surname": "Coker", "position": "Government Printer", "department": "Civil Establishment - Gambia", "salary_min": 90, "salary_max": 90},
    {"name": "F. T. Wilton", "canonical_name": "Wilton, F. T.", "given_names": "F. T.", "surname": "Wilton", "position": "Assistant Government Printer", "department": "Civil Establishment - Gambia", "salary_min": 30, "salary_max": 30},
    {"name": "H. M. R. Griffith", "canonical_name": "Griffith, H. M. R.", "given_names": "H. M. R.", "surname": "Griffith", "position": "Treasurer", "department": "Civil Establishment - Gambia", "salary_min": 500, "salary_max": 600, "allowances": "quarters", "duty_allowance": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()