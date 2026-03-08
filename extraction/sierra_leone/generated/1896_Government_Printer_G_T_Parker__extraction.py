"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Government Printer", "department": "Printing - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "T. E. Laing", "canonical_name": "Laing, T. E.", "given_names": "T. E.", "surname": "Laing", "position": "Colonial Surveyor", "department": "Surveyor's Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "W. Cuddeford", "canonical_name": "Cuddeford, W.", "given_names": "W.", "surname": "Cuddeford", "position": "Local Auditor", "department": "Audit Department - Sierra Leone", "salary_min": 450, "salary_max": 450, "allowances": "quarters"},
    {"name": "W. J. P. Elliott", "canonical_name": "Elliott, W. J. P.", "given_names": "W. J. P.", "surname": "Elliott", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 750, "salary_max": 750}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()