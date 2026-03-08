"""
Sierra Leone Colonial Office List 1880 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1880

OFFICIALS = [
    {"name": "C. J. Mannah", "canonical_name": "Mannah, C. J.", "given_names": "C. J.", "surname": "Mannah", "position": "Sub-Collector of Customs", "department": "Customs - Sierra Leone", "salary_min": 200, "salary_max": 200, "acting_status": "Acting", "location": "Isles de Los"},
    {"name": "W. M. Laborde", "canonical_name": "Laborde, W. M.", "given_names": "W. M.", "surname": "Laborde", "position": "Civil Commandant and Sub-Collector", "department": "Civil Establishment - Sierra Leone", "acting_status": "Acting", "location": "Kikonkeh"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()