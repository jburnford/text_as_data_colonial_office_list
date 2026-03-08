"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "Right Rev. Henry Cheetham", "canonical_name": "Cheetham, Henry", "given_names": "Henry", "surname": "Cheetham", "position": "Bishop of Sierra Leone", "department": "Ecclesiastical - Sierra Leone", "salary_min": 500, "salary_max": 500, "qualifications": ["D.D."]},
    {"name": "Rev. L. Nicholson", "canonical_name": "Nicholson, L.", "given_names": "L.", "surname": "Nicholson", "position": "Colonial Chaplain", "department": "Ecclesiastical - Sierra Leone", "acting_status": "Acting"},
    {"name": "Rev. John Campbell", "canonical_name": "Campbell, John", "given_names": "John", "surname": "Campbell", "position": "Assistant Chaplain", "department": "Ecclesiastical - Sierra Leone", "salary_min": 150, "salary_max": 150}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()