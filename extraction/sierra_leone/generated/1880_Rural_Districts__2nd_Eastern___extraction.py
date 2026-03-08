"""
Sierra Leone Colonial Office List 1880 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1880

OFFICIALS = [
    {"name": "H. P. Northcott", "canonical_name": "Northcott, H. P.", "given_names": "H. P.", "surname": "Northcott", "position": "Manager", "department": "Rural Districts - Sierra Leone", "acting_status": "Acting", "allowances": "travelling allowance, 45l. 12s. 6d.", "military_rank": "Lieut."},
    {"name": "The Coroner for Freetown", "canonical_name": "Coroner for Freetown, The", "surname": "Coroner", "position": "Coroner", "department": "Rural Districts - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "W. Budge", "canonical_name": "Budge, W.", "given_names": "W.", "surname": "Budge", "position": "Manager", "department": "Rural Districts - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "and travelling allowance, 91l. 5s."},
    {"name": "The Manager", "canonical_name": "Manager, The", "surname": "Manager", "position": "Coroner", "department": "Rural Districts - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "J. B. Elliott", "canonical_name": "Elliott, J. B.", "given_names": "J. B.", "surname": "Elliott", "position": "Manager", "department": "Rural Districts - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "the Manager", "canonical_name": "Manager, The", "surname": "Manager", "position": "Coroner", "department": "Rural Districts - Sierra Leone", "salary_min": 20, "salary_max": 20}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()