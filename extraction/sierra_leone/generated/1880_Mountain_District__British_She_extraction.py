"""
Sierra Leone Colonial Office List 1880 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1880

OFFICIALS = [
    {"name": "H. P. Northcott", "canonical_name": "Northcott, H. P.", "given_names": "H. P.", "surname": "Northcott", "position": "Manager", "department": "Mountain District - Sierra Leone", "acting_status": "Acting", "allowances": "travelling allowance, 45l. 12s. 6d.", "military_rank": "Lieut."},
    {"name": "the Coroner for Freetown", "canonical_name": "Coroner for Freetown, The", "surname": "Coroner", "position": "Coroner", "department": "Mountain District - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "T. A. Wall", "canonical_name": "Wall, T. A.", "given_names": "T. A.", "surname": "Wall", "position": "Civil Commandant", "department": "British Sherbro - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Clerk and Sub-Accountant to ditto", "department": "British Sherbro - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "the Commandant", "canonical_name": "Commandant, The", "surname": "Commandant", "position": "Deputy Collector of Customs", "department": "British Sherbro - Sierra Leone", "acting_status": "Acting", "salary_min": 100, "salary_max": 100},
    {"name": "W. M. Laborde", "canonical_name": "Laborde, W. M.", "given_names": "W. M.", "surname": "Laborde", "position": "Clerk", "department": "British Sherbro - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Landing Waiters", "department": "British Sherbro - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Landing Waiters", "department": "British Sherbro - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Tide Waiter", "department": "British Sherbro - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT, VACANT", "surname": "VACANT", "position": "Warehouse Keeper", "department": "British Sherbro - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "H. R. Williams", "canonical_name": "Williams, H. R.", "given_names": "H. R.", "surname": "Williams", "position": "Postmaster", "department": "British Sherbro - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "W. H. Hughes", "canonical_name": "Hughes, W. H.", "given_names": "W. H.", "surname": "Hughes", "position": "Bailiff", "department": "British Sherbro - Sierra Leone", "salary_min": 86, "salary_max": 86},
    {"name": "the Commandant", "canonical_name": "Commandant, The", "surname": "Commandant", "position": "Coroner", "department": "British Sherbro - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "M. L. Jarrett", "canonical_name": "Jarrett, M. L.", "given_names": "M. L.", "surname": "Jarrett", "position": "Assistant Colonial Surgeon", "department": "Medical - British Sherbro", "qualifications": ["M.R.C.S."], "acting_status": "Acting", "salary_min": 250, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()