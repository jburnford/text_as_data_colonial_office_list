"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "A. J. M. Paget", "canonical_name": "Paget, A. J. M.", "given_names": "A. J. M.", "surname": "Paget", "position": "Senior Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "R. E. Drake-Brockman", "canonical_name": "Drake-Brockman, R. E.", "given_names": "R. E.", "surname": "Drake-Brockman", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "H. M. O'Byrne", "canonical_name": "O'Byrne, H. M.", "given_names": "H. M.", "surname": "O'Byrne", "position": "Chief of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "O. R. L. Green", "canonical_name": "Green, O. R. L.", "given_names": "O. R. L.", "surname": "Green", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 350},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()