"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "H. W. Lewis", "canonical_name": "Lewis, H. W.", "given_names": "H. W.", "surname": "Lewis", "position": "Keeper, Lunatic Asylum, Kissy", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "W. Z. Young", "canonical_name": "Young, W. Z.", "given_names": "W. Z.", "surname": "Young", "position": "Dispensers", "department": "Medical - Sierra Leone", "location": "Waterloo", "salary_min": 50, "salary_max": 50},
    {"name": "M. Aubec", "canonical_name": "Aubec, M.", "given_names": "M.", "surname": "Aubec", "position": "Dispensers", "department": "Medical - Sierra Leone", "location": "Hastings", "salary_min": 36, "salary_max": 36},
    {"name": "C. A. Innis", "canonical_name": "Innis, C. A.", "given_names": "C. A.", "surname": "Innis", "position": "Dispensers", "department": "Medical - Sierra Leone", "location": "York", "salary_min": 40, "salary_max": 40},
    {"name": "A. W. Elliott", "canonical_name": "Elliott, A. W.", "given_names": "A. W.", "surname": "Elliott", "position": "Dispensers", "department": "Medical - Sierra Leone", "location": "Sherbro", "salary_min": 50, "salary_max": 50},
    {"name": "S. A. Bell", "canonical_name": "Bell, S. A.", "given_names": "S. A.", "surname": "Bell", "position": "Dispensers", "department": "Medical - Sierra Leone", "location": "Sulymah", "salary_min": 60, "salary_max": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()