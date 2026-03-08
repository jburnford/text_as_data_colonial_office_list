"""
Sierra Leone Colonial Office List 1950 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1950

OFFICIALS = [
    {"name": "H. C. C. Smith", "canonical_name": "Smith, H. C. C.", "given_names": "H. C. C.", "surname": "Smith", "position": "Consul for Portugal, Belgium, Norway", "department": "Foreign Consular Officers - Sierra Leone", "location": "Freetown"},
    {"name": "J. P. Holman", "canonical_name": "Holman, J. P.", "given_names": "J. P.", "surname": "Holman", "position": "Consul for Denmark", "department": "Foreign Consular Officers - Sierra Leone", "location": "Freetown"},
    {"name": "P. W. Lubbers", "canonical_name": "Lubbers, P. W.", "given_names": "P. W.", "surname": "Lubbers", "position": "Consul for the Netherlands", "department": "Foreign Consular Officers - Sierra Leone", "acting_status": "Acting", "location": "Freetown"},
    {"name": "W. Sigg", "canonical_name": "Sigg, W.", "given_names": "W.", "surname": "Sigg", "position": "Consul for Switzerland", "department": "Foreign Consular Officers - Sierra Leone", "location": "Freetown"},
    {"name": "M. Z. Pappas", "canonical_name": "Pappas, M. Z.", "given_names": "M. Z.", "surname": "Pappas", "position": "Consul for Greece", "department": "Foreign Consular Officers - Sierra Leone", "location": "Freetown"},
    {"name": "J. A. Thomas", "canonical_name": "Thomas, J. A.", "given_names": "J. A.", "surname": "Thomas", "position": "Consul for Liberia", "department": "Foreign Consular Officers - Sierra Leone", "acting_status": "Acting", "location": "Freetown"},
    {"name": "M. Jourdan", "canonical_name": "Jourdan, M.", "given_names": "M.", "surname": "Jourdan", "position": "Consul for France", "department": "Foreign Consular Officers - Sierra Leone", "location": "Freetown"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()