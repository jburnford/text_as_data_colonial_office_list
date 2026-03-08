"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "W. H. Hart", "canonical_name": "Hart, W. H.", "given_names": "W. H.", "surname": "Hart", "position": "Colonial Surgeon", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "horse allowance, 91l. 5s.", "qualifications": ["M.B."]},
    {"name": "Robt. Smith", "canonical_name": "Smith, Robt.", "given_names": "Robt.", "surname": "Smith", "position": "Assistant Colonial Surgeon", "department": "Medical - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "horse allowance, 91l. 5s."},
    {"name": "D. Johnson", "canonical_name": "Johnson, D.", "given_names": "D.", "surname": "Johnson", "position": "Comptroller and Stor-keeper", "department": "Medical - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "quarters"},
    {"name": "D. Cole", "canonical_name": "Cole, D.", "given_names": "D.", "surname": "Cole", "position": "Medical Clerk", "department": "Medical - Sierra Leone", "salary_min": 75, "salary_max": 75, "allowances": "quarters"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()