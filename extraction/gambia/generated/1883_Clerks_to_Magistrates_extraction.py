"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "F. Taunton", "canonical_name": "Taunton, F.", "given_names": "F.", "surname": "Taunton", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "North District", "salary_min": 100, "salary_max": 100},
    {"name": "W. D. Cowan", "canonical_name": "Cowan, W. D.", "given_names": "W. D.", "surname": "Cowan", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "Victoria District", "salary_min": 160, "salary_max": 160},
    {"name": "J. W. E. Archdeacon", "canonical_name": "Archdeacon, J. W. E.", "given_names": "J. W. E.", "surname": "Archdeacon", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "Greenough District", "salary_min": 110, "salary_max": 110},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "York District", "salary_min": 125, "salary_max": 125},
    {"name": "W. R. Piess", "canonical_name": "Piess, W. R.", "given_names": "W. R.", "surname": "Piess", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "Toodyay District", "salary_min": 125, "salary_max": 125},
    {"name": "N. E. Knight", "canonical_name": "Knight, N. E.", "given_names": "N. E.", "surname": "Knight", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "Swan District", "salary_min": 112, "salary_max": 112},
    {"name": "John Adam", "canonical_name": "Adam, John", "given_names": "John", "surname": "Adam", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "Perth District", "salary_min": 175, "salary_max": 175},
    {"name": "G. S. Compton", "canonical_name": "Compton, G. S.", "given_names": "G. S.", "surname": "Compton", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "Fremantle District", "salary_min": 150, "salary_max": 150},
    {"name": "G. R. Teede", "canonical_name": "Teede, G. R.", "given_names": "G. R.", "surname": "Teede", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "Wellington District", "salary_min": 110, "salary_max": 110},
    {"name": "F. A. Hare", "canonical_name": "Hare, F. A.", "given_names": "F. A.", "surname": "Hare", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "Sussex District", "salary_min": 110, "salary_max": 110},
    {"name": "H. M. Thomas", "canonical_name": "Thomas, H. M.", "given_names": "H. M.", "surname": "Thomas", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "Plantagenet District", "salary_min": 160, "salary_max": 160},
    {"name": "F. H. Piess", "canonical_name": "Piess, F. H.", "given_names": "F. H.", "surname": "Piess", "position": "Clerk to Magistrate", "department": "Judicial - Gambia", "location": "Williams District", "salary_min": 55, "salary_max": 55}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()