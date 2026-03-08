"""
Gold Coast Colonial Office List 1896 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1896

OFFICIALS = [
    {"name": "F. H. D. Negus", "canonical_name": "Negus, F. H. D.", "given_names": "F. H. D.", "surname": "Negus",
     "position": "Local Auditor", "department": "Audit Office - Gold Coast", "salary_min": 400, "salary_max": 500},
    {"name": "R. E. Quartey", "canonical_name": "Quartey, R. E.", "given_names": "R. E.", "surname": "Quartey",
     "position": "Clerk", "department": "Audit Office - Gold Coast", "salary_min": 120, "salary_max": 150},
    {"name": "Alexander Konuah", "canonical_name": "Konuah, Alexander", "given_names": "Alexander", "surname": "Konuah",
     "position": "Clerk", "department": "Audit Office - Gold Coast", "salary_min": 70, "salary_max": 100},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()