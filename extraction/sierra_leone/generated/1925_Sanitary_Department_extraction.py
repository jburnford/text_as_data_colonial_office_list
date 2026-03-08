"""
Sierra Leone Colonial Office List 1925 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1925

OFFICIALS = [
    {"name": "H. H. O'Hara May", "canonical_name": "May, H. H. O'Hara", "given_names": "H. H.", "surname": "May", "position": "Deputy Director, Sanitary Services", "department": "Sanitary Department - Sierra Leone", "salary_min": 1300, "salary_max": 1300, "duty_allowance": 260},
    {"name": "W. H. Peacock", "canonical_name": "Peacock, W. H.", "given_names": "W. H.", "surname": "Peacock", "position": "Senior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 1050, "salary_max": 1200, "duty_allowance": 210},
    {"name": "J. M. Mackay", "canonical_name": "Mackay, J. M.", "given_names": "J. M.", "surname": "Mackay", "position": "Medical Officer of Health", "department": "Sanitary Department - Sierra Leone", "salary_min": 800, "salary_max": 960},
    {"name": "D. Bowen", "canonical_name": "Bowen, D.", "given_names": "D.", "surname": "Bowen", "position": "Superintendent, Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_scale": "F"},
    {"name": "G. V. Herd", "canonical_name": "Herd, G. V.", "given_names": "G. V.", "surname": "Herd", "position": "Superintendent, Sanitary Inspectors", "department": "Sanitary Department - Sierra Leone", "salary_scale": "F"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()