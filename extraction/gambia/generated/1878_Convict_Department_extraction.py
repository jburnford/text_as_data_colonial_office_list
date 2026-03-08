"""
Gambia Colonial Office List 1878 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1878

OFFICIALS = [
    {"name": "W. R. Fauntleroy", "canonical_name": "Fauntleroy, W. R.", "given_names": "W. R.", "surname": "Fauntleroy", "position": "Comptroller of Convicts", "department": "Convict Department - Gambia", "salary_min": 450, "salary_max": 450},
    {"name": "Rev. R. Alderson", "canonical_name": "Alderson, R.", "given_names": "R.", "surname": "Alderson", "position": "Chaplain", "department": "Convict Department - Gambia", "salary_min": 400, "salary_max": 400},
    {"name": "G. C. Attfield", "canonical_name": "Attfield, G. C.", "given_names": "G. C.", "surname": "Attfield", "position": "Surgeon", "department": "Convict Department - Gambia", "salary_min": 450, "salary_max": 450},
    {"name": "D. Francisco", "canonical_name": "Francisco, D.", "given_names": "D.", "surname": "Francisco", "position": "Storekeeper", "department": "Convict Department - Gambia", "salary_min": 200, "salary_max": 200},
    {"name": "E. S. Porter", "canonical_name": "Porter, E. S.", "given_names": "E. S.", "surname": "Porter", "position": "Clerk", "department": "Convict Department - Gambia"},
    {"name": "A. H. Loché", "canonical_name": "Loché, A. H.", "given_names": "A. H.", "surname": "Loché", "position": "Clerk", "department": "Convict Department - Gambia"},
    {"name": "C. Spencer", "canonical_name": "Spencer, C.", "given_names": "C.", "surname": "Spencer", "position": "Clerk", "department": "Convict Department - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()