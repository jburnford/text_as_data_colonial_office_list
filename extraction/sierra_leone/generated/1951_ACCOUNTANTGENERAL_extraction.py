"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "W. D. A. Jones", "canonical_name": "Jones, W. D. A.", "given_names": "W. D. A.", "surname": "Jones", "position": "Accountant-General", "department": "Accountant-General - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "D. O. T. Fountain", "canonical_name": "Fountain, D. O. T.", "given_names": "D. O. T.", "surname": "Fountain", "position": "Assistant Treasurers and Accountants", "department": "Accountant-General - Sierra Leone", "salary_scale": "B"},
    {"name": "J. M. Williams", "canonical_name": "Williams, J. M.", "given_names": "J. M.", "surname": "Williams", "position": "Assistant Treasurers and Accountants", "department": "Accountant-General - Sierra Leone", "salary_scale": "B"},
    {"name": "L. G. A. Beckley", "canonical_name": "Beckley, L. G. A.", "given_names": "L. G. A.", "surname": "Beckley", "position": "Assistant Treasurers and Accountants", "department": "Accountant-General - Sierra Leone", "salary_scale": "B"},
    {"name": "H. M. Johnson", "canonical_name": "Johnson, H. M.", "given_names": "H. M.", "surname": "Johnson", "position": "Assistant Treasurers and Accountants", "department": "Accountant-General - Sierra Leone", "salary_scale": "B"},
    {"name": "A. A. Dupigny", "canonical_name": "Dupigny, A. A.", "given_names": "A. A.", "surname": "Dupigny", "position": "Assistant Treasurers and Accountants", "department": "Accountant-General - Sierra Leone", "salary_scale": "B"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()