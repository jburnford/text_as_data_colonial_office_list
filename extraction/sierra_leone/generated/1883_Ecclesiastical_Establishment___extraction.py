"""
Sierra Leone Colonial Office List 1883 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1883

OFFICIALS = [
    {"name": "The Right. Rev. E. G. Ingham", "canonical_name": "Ingham, E. G.", "given_names": "E. G.", "surname": "Ingham", "position": "Bishop of Sierra Leone", "department": "Ecclesiastical Establishment - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "Rev. John Campbell", "canonical_name": "Campbell, John", "given_names": "John", "surname": "Campbell", "position": "Assistant Chaplain", "department": "Ecclesiastical Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "The Rev. M. Sunter", "canonical_name": "Sunter, M.", "given_names": "M.", "surname": "Sunter", "position": "Inspector of Schools", "department": "Educational Establishment - Sierra Leone", "salary_min": 700, "salary_max": 700, "qualifications": ["M.A."]},
    {"name": "T. S. Wilson", "canonical_name": "Wilson, T. S.", "given_names": "T. S.", "surname": "Wilson", "position": "Head Master, Model School", "department": "Educational Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "W. H. Hart", "canonical_name": "Hart, W. H.", "given_names": "W. H.", "surname": "Hart", "position": "Colonial Surgeon", "department": "Medical Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500, "qualifications": ["M.B."], "location": "Freetown", "allowances": "travelling allowance, 91l. 5s."},
    {"name": "Robt. Smith", "canonical_name": "Smith, Robt.", "given_names": "Robt.", "surname": "Smith", "position": "Assistant Surgeon", "department": "Medical Establishment - Sierra Leone", "salary_min": 300, "salary_max": 300, "qualifications": ["M.R.C.S."], "location": "Freetown", "allowances": "travelling allowance, 91l. 5s."},
    {"name": "D. Cole", "canonical_name": "Cole, D.", "given_names": "D.", "surname": "Cole", "position": "Medical Clerk and Storekeeper", "department": "General Hospital - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "R. Spencer", "canonical_name": "Spencer, R.", "given_names": "R.", "surname": "Spencer", "position": "Compounder", "department": "General Hospital - Sierra Leone", "salary_min": 70, "salary_max": 70}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()