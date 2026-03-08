"""
Gambia Colonial Office List 1914 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1914

OFFICIALS = [
    {"name": "Sir F. Evans", "canonical_name": "Evans, F.", "given_names": "F.", "surname": "Evans", "position": "Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 1000, "salary_max": 1000, "honors": ["K.C.M.G.", "K.C.V.O."]},
    {"name": "J. Porral", "canonical_name": "Porral, J.", "given_names": "J.", "surname": "Porral", "position": "Assistant Colonial Secretary", "department": "Civil Establishment - Gambia", "salary_min": 350, "salary_max": 350, "allowances": "50l. as Secretary to Board of Health, and quarters."},
    {"name": "E. P. Griffin", "canonical_name": "Griffin, E. P.", "given_names": "E. P.", "surname": "Griffin", "position": "Chief Clerk", "department": "Civil Establishment - Gambia", "salary_min": 210, "salary_max": 300, "allowances": "55l. for translating and interpreting."},
    {"name": "J. Bruzon", "canonical_name": "Bruzon, J.", "given_names": "J.", "surname": "Bruzon", "position": "2nd Class Clerk", "department": "Civil Establishment - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "R. Giraldi", "canonical_name": "Giraldi, R.", "given_names": "R.", "surname": "Giraldi", "position": "1st Class Clerk", "department": "Crown Property Department - Gambia", "salary_min": 210, "salary_max": 300},
    {"name": "A. C. Greenwood", "canonical_name": "Greenwood, A. C.", "given_names": "A. C.", "surname": "Greenwood", "position": "Treasurer and Collector", "department": "Revenue Department - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "A. Podesta", "canonical_name": "Podesta, A.", "given_names": "A.", "surname": "Podesta", "position": "Chief Clerk and Cashier", "department": "Revenue Department - Gambia", "salary_min": 250, "salary_max": 350, "allowances": "86l. as Treasurer to the Sanitary Commissioners."},
    {"name": "R. H. Pogue", "canonical_name": "Pogue, R. H.", "given_names": "R. H.", "surname": "Pogue", "position": "1st Class Clerk", "department": "Revenue Department - Gambia", "salary_min": 210, "salary_max": 300, "allowances": "(and Clerk to Registrar of Shipping, 25l.)."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()