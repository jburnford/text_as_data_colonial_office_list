"""
Gambia Colonial Office List 1905 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1905

OFFICIALS = [
    {"name": "A. D. Russell", "canonical_name": "Russell, A. D.", "given_names": "A. D.", "surname": "Russell", "position": "Chief Magistrate", "department": "Judicial - Gambia", "salary_min": 750, "salary_max": 750, "qualifications": ["M.A.", "LL.B."]},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Judicial - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "F. M. Fye", "canonical_name": "Fye, F. M.", "given_names": "F. M.", "surname": "Fye", "position": "Interpreter", "department": "Judicial - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "Joseph Brown", "canonical_name": "Brown, Joseph", "given_names": "Joseph", "surname": "Brown", "position": "Sheriff", "department": "Judicial - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "M. C. Peacock", "canonical_name": "Peacock, M. C.", "given_names": "M. C.", "surname": "Peacock", "position": "Beadle and Bailiff", "department": "Judicial - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "H. L. Pryce", "canonical_name": "Pryce, H. L.", "given_names": "H. L.", "surname": "Pryce", "position": "Travelling Commissioner, First Class", "department": "Judicial - Gambia", "salary_min": 500, "salary_max": 500},
    {"name": "G. H. Sangster", "canonical_name": "Sangster, G. H.", "given_names": "G. H.", "surname": "Sangster", "position": "Travelling Commissioner, Second Class", "department": "Judicial - Gambia", "salary_min": 400, "salary_max": 400},
    {"name": "W. B. Stanley", "canonical_name": "Stanley, W. B.", "given_names": "W. B.", "surname": "Stanley", "position": "Travelling Commissioner, Third Class", "department": "Judicial - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"},
    {"name": "J. K. McCallum", "canonical_name": "McCallum, J. K.", "given_names": "J. K.", "surname": "McCallum", "position": "Travelling Commissioner, Third Class", "department": "Judicial - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"},
    {"name": "A. K. Withers", "canonical_name": "Withers, A. K.", "given_names": "A. K.", "surname": "Withers", "position": "Travelling Commissioner, Third Class", "department": "Judicial - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()