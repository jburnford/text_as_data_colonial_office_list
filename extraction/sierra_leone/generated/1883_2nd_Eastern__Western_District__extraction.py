"""
Sierra Leone Colonial Office List 1883 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1883

OFFICIALS = [
    {"name": "W. Budge", "canonical_name": "Budge, W.", "given_names": "W.", "surname": "Budge", "position": "Manager", "department": "Civil Establishment - Sierra Leone", "salary_min": 350, "salary_max": 350, "allowances": "travelling allowance 91l. 5s. and quarters"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "The Manager", "canonical_name": "Manager, The", "surname": "Manager", "position": "Coroner", "department": "Civil Establishment - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dresser", "department": "Medical - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. B. Elliott", "canonical_name": "Elliott, J. B.", "given_names": "J. B.", "surname": "Elliott", "position": "Manager", "department": "Civil Establishment - Sierra Leone", "salary_min": 250, "salary_max": 250, "allowances": "rent 40l."},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "the Manager", "canonical_name": "Manager, The", "surname": "Manager", "position": "Coroner", "department": "Civil Establishment - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Gaoler", "department": "Gaol - Sierra Leone"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Overseer", "department": "Gaol - Sierra Leone"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dresser", "department": "Medical - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dresser", "department": "Medical - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "E. Adolphus", "canonical_name": "Adolphus, E.", "given_names": "E.", "surname": "Adolphus", "position": "Manager", "department": "Civil Establishment - Sierra Leone", "acting_status": "Acting", "allowances": "travelling allowance, 45l. 12s. 6d."},
    {"name": "the Coroner for Freetown", "canonical_name": "Coroner for Freetown, The", "surname": "Coroner", "position": "Coroner", "department": "Civil Establishment - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dresser", "department": "Medical - Sierra Leone", "salary_min": 36, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()