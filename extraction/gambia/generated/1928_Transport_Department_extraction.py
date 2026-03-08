"""
Gambia Colonial Office List 1928 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1928

OFFICIALS = [
    {"name": "J. P. Mullins", "canonical_name": "Mullins, J. P.", "given_names": "J. P.", "surname": "Mullins", "position": "Master, H.M.C.S. \"Pioneer,\"", "department": "Transport Department - Gambia", "salary_min": 504, "salary_max": 504},
    {"name": "O. B. Corbett", "canonical_name": "Corbett, O. B.", "given_names": "O. B.", "surname": "Corbett", "position": "First Engineer Officer", "department": "Transport Department - Gambia", "salary_min": 420, "salary_max": 420},
    {"name": "J. R. Neville", "canonical_name": "Neville, J. R.", "given_names": "J. R.", "surname": "Neville", "position": "Temporary Chief Officer", "department": "Transport Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "L. S. Whysall", "canonical_name": "Whysall, L. S.", "given_names": "L. S.", "surname": "Whysall", "position": "Second Engineer", "department": "Transport Department - Gambia", "salary_min": 360, "salary_max": 360},
    {"name": "D. T. Bentley", "canonical_name": "Bentley, D. T.", "given_names": "D. T.", "surname": "Bentley", "position": "Third Engineer", "department": "Transport Department - Gambia", "salary_min": 275, "salary_max": 275},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()