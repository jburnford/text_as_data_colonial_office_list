"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Surveyor-General and Commissioner of Crown Lands", "department": "Survey Department - Gambia", "salary_min": 600, "salary_max": 600, "allowances": "150l."},
    {"name": "J. Forrest", "canonical_name": "Forrest, J.", "given_names": "J.", "surname": "Forrest", "position": "Deputy Surveyor-General", "department": "Survey Department - Gambia", "salary_min": 350, "salary_max": 350, "allowances": "150l."},
    {"name": "J. S. Brooking", "canonical_name": "Brooking, J. S.", "given_names": "J. S.", "surname": "Brooking", "position": "Surveyor", "department": "Survey Department - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "150l."},
    {"name": "C. D. Price", "canonical_name": "Price, C. D.", "given_names": "C. D.", "surname": "Price", "position": "Do.", "department": "Survey Department - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "150l."},
    {"name": "G. Vincent", "canonical_name": "Vincent, G.", "given_names": "G.", "surname": "Vincent", "position": "Chief Draftsman and Custodian of Plans", "department": "Survey Department - Gambia", "salary_min": 320, "salary_max": 320},
    {"name": "E. C. Dean", "canonical_name": "Dean, E. C.", "given_names": "E. C.", "surname": "Dean", "position": "Draftsman", "department": "Survey Department - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "M. A. C. Fraser", "canonical_name": "Fraser, M. A. C.", "given_names": "M. A. C.", "surname": "Fraser", "position": "Meteorologist", "department": "Survey Department - Gambia"},
    {"name": "R. C. Clifton", "canonical_name": "Clifton, R. C.", "given_names": "R. C.", "surname": "Clifton", "position": "Chief Clerk and Record Keeper", "department": "Survey Department - Gambia", "salary_min": 270, "salary_max": 270},
    {"name": "A. H. Williams", "canonical_name": "Williams, A. H.", "given_names": "A. H.", "surname": "Williams", "position": "Clerk", "department": "Survey Department - Gambia", "salary_min": 180, "salary_max": 180}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()