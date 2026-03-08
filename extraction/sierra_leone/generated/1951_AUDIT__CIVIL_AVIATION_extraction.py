"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "F. P. L. Derriman", "canonical_name": "Derriman, F. P. L.", "given_names": "F. P. L.", "surname": "Derriman", "position": "Director of Audit", "department": "Audit - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "W. A. Knight", "canonical_name": "Knight, W. A.", "given_names": "W. A.", "surname": "Knight", "position": "Senior Auditor", "department": "Audit - Sierra Leone", "salary_scale": "B", "salary_min": 810, "salary_max": 900},
    {"name": "A. C. Wilson", "canonical_name": "Wilson, A. C.", "given_names": "A. C.", "surname": "Wilson", "position": "Auditor", "department": "Audit - Sierra Leone", "salary_scale": "B", "salary_min": 510, "salary_max": 780},
    {"name": "G. A. Fuller-Quin", "canonical_name": "Fuller-Quin, G. A.", "given_names": "G. A.", "surname": "Fuller-Quin", "position": "Airport Manager", "department": "Civil Aviation - Sierra Leone", "salary_scale": "B", "salary_min": 660, "salary_max": 900},
    {"name": "H. Dipper", "canonical_name": "Dipper, H.", "given_names": "H.", "surname": "Dipper", "position": "Assistant Airport Manager", "department": "Civil Aviation - Sierra Leone", "salary_scale": "B"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()