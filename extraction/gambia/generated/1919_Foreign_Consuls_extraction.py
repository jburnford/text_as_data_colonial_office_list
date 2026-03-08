"""
Gambia Colonial Office List 1919 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1919

OFFICIALS = [
    {"name": "P. Bourquin", "canonical_name": "Bourquin, P.", "given_names": "P.", "surname": "Bourquin", "position": "Vice-Consul", "department": "Foreign Consuls - Gambia", "location": "Belgium"},
    {"name": "F. Orcel", "canonical_name": "Orcel, F.", "given_names": "F.", "surname": "Orcel", "position": "Consular Agent", "department": "Foreign Consuls - Gambia", "location": "France"},
    {"name": "Hon. J. Howie", "canonical_name": "Howie, J.", "given_names": "J.", "surname": "Howie", "position": "Consul", "department": "Foreign Consuls - Gambia", "honors": ["Hon."], "location": "Portugal"},
    {"name": "Hon. J. Howie", "canonical_name": "Howie, J.", "given_names": "J.", "surname": "Howie", "position": "Vice-Consul", "department": "Foreign Consuls - Gambia", "honors": ["Hon."], "location": "Spain"},
    {"name": "P. Bourquin", "canonical_name": "Bourquin, P.", "given_names": "P.", "surname": "Bourquin", "position": "Consul", "department": "Foreign Consuls - Gambia", "location": "Norway"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()