"""
Gold Coast Colonial Office List 1896 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1896

OFFICIALS = [
    {"name": "J. R. Phillips", "canonical_name": "Phillips, J. R.", "given_names": "J. R.", "surname": "Phillips",
     "position": "Sheriff", "department": "Prisons Department - Gold Coast", "salary_min": 400, "salary_max": 500, "qualifications": ["B.A."]},
    {"name": "J. H. Anquandah", "canonical_name": "Anquandah, J. H.", "given_names": "J. H.", "surname": "Anquandah",
     "position": "Keeper of Prison", "department": "Prisons Department - Gold Coast", "location": "Accra", "salary_min": 100, "salary_max": 120},
    {"name": "Sanli Owoh", "canonical_name": "Owoh, Sanli", "given_names": "Sanli", "surname": "Owoh",
     "position": "Chief Warder", "department": "Prisons Department - Gold Coast", "location": "Accra", "salary_min": 60, "salary_max": 80},
    {"name": "J. Bafoe", "canonical_name": "Bafoe, J.", "given_names": "J.", "surname": "Bafoe",
     "position": "Keeper of Prison", "department": "Prisons Department - Gold Coast", "location": "Elmina", "salary_min": 100, "salary_max": 120},
    {"name": "A. G. Des Bordes", "canonical_name": "Des Bordes, A. G.", "given_names": "A. G.", "surname": "Des Bordes",
     "position": "Chief Warder", "department": "Prisons Department - Gold Coast", "location": "Elmina", "salary_min": 60, "salary_max": 80},
    {"name": "G. M. Graves", "canonical_name": "Graves, G. M.", "given_names": "G. M.", "surname": "Graves",
     "position": "Keeper of Prison", "department": "Prisons Department - Gold Coast", "location": "Cape Coast", "salary_min": 60, "salary_max": 80},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()