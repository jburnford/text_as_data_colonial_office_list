"""
Gambia Colonial Office List 1867 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1867

OFFICIALS = [
    {"name": "W. H. Sherwood", "canonical_name": "Sherwood, W. H.", "given_names": "W. H.", "surname": "Sherwood", "position": "High Sheriff", "department": "Judicial Establishment - Gambia"},
    {"name": "Seymour Gay", "canonical_name": "Gay, Seymour", "given_names": "Seymour", "surname": "Gay", "position": "Superintendent of Police", "department": "Judicial Establishment - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "J. Smith", "canonical_name": "Smith, J.", "given_names": "J.", "surname": "Smith", "position": "Resident Manager of Combo", "department": "Judicial Establishment - Gambia", "salary_min": 80, "salary_max": 80, "qualifications": ["J.P."]},
    {"name": "Dr. Sherwood", "canonical_name": "Sherwood, Dr.", "given_names": "Dr.", "surname": "Sherwood", "position": "Police Magistrate", "department": "Judicial Establishment - Gambia", "acting_status": "Acting"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()