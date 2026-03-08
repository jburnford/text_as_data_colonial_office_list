"""
Sierra Leone Colonial Office List 1911 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1911

OFFICIALS = [
    {"name": "C. Perinaux", "canonical_name": "Perinaux, C.", "given_names": "C.", "surname": "Perinaux", "position": "France", "department": "Foreign Consuls - Sierra Leone"},
    {"name": "J. Zellweger", "canonical_name": "Zellweger, J.", "given_names": "J.", "surname": "Zellweger", "position": "Germany", "department": "Foreign Consuls - Sierra Leone"},
    {"name": "J. C. Newton", "canonical_name": "Newton, J. C.", "given_names": "J. C.", "surname": "Newton", "position": "Belgium", "department": "Foreign Consuls - Sierra Leone", "acting_status": "acting"},
    {"name": "J. C. Newton", "canonical_name": "Newton, J. C.", "given_names": "J. C.", "surname": "Newton", "position": "The Netherlands", "department": "Foreign Consuls - Sierra Leone"},
    {"name": "J. C. Newton", "canonical_name": "Newton, J. C.", "given_names": "J. C.", "surname": "Newton", "position": "Norway", "department": "Foreign Consuls - Sierra Leone"},
    {"name": "W. H. Hall", "canonical_name": "Hall, W. H.", "given_names": "W. H.", "surname": "Hall", "position": "Spain", "department": "Foreign Consuls - Sierra Leone"},
    {"name": "G. T. Zolia", "canonical_name": "Zolia, G. T.", "given_names": "G. T.", "surname": "Zolia", "position": "Italy", "department": "Foreign Consuls - Sierra Leone"},
    {"name": "D. Horncastle", "canonical_name": "Horncastle, D.", "given_names": "D.", "surname": "Horncastle", "position": "Portugal", "department": "Foreign Consuls - Sierra Leone", "acting_status": "acting"},
    {"name": "J. C. Newton", "canonical_name": "Newton, J. C.", "given_names": "J. C.", "surname": "Newton", "position": "Greece", "department": "Foreign Consuls - Sierra Leone", "acting_status": "acting"},
    {"name": "W. Yerby", "canonical_name": "Yerby, W.", "given_names": "W.", "surname": "Yerby", "position": "United States", "department": "Foreign Consuls - Sierra Leone"},
    {"name": "C. May", "canonical_name": "May, C.", "given_names": "C.", "surname": "May", "position": "Liberia", "department": "Foreign Consuls - Sierra Leone"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()