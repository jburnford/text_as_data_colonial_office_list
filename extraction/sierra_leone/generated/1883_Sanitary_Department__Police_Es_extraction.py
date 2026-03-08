"""
Sierra Leone Colonial Office List 1883 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1883

OFFICIALS = [
    {"name": "A. Revington", "canonical_name": "Revington, A.", "given_names": "A.", "surname": "Revington", "position": "Inspector of Health", "department": "Sanitary Department - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "H. H. Palmer", "canonical_name": "Palmer, H. H.", "given_names": "H. H.", "surname": "Palmer", "position": "Clerk to ditto", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Edwin Adolphus", "canonical_name": "Adolphus, Edwin", "given_names": "Edwin", "surname": "Adolphus", "position": "Police Magistrate", "department": "Police Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "A. B. Martyn", "canonical_name": "Martyn, A. B.", "given_names": "A. B.", "surname": "Martyn", "position": "Clerk of Police", "department": "Police Establishment - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "H. M. Jackson", "canonical_name": "Jackson, H. M.", "given_names": "H. M.", "surname": "Jackson", "position": "Inspector-General of Police", "department": "Police Establishment - Sierra Leone", "salary_min": 400, "salary_max": 400, "military_rank": "Captain", "per_diem": "91l. 5s."},
    {"name": "A. Revington", "canonical_name": "Revington, A.", "given_names": "A.", "surname": "Revington", "position": "Inspector", "department": "Police Establishment - Sierra Leone"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Keeper of Freetown Gaol", "department": "Gaol Establishment - Sierra Leone", "salary_min": 250, "salary_max": 250, "location": "Freetown"},
    {"name": "S. J. Thomas", "canonical_name": "Thomas, S. J.", "given_names": "S. J.", "surname": "Thomas", "position": "Under Gaoler", "department": "Gaol Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100, "location": "Freetown"},
    {"name": "E. Adolphus", "canonical_name": "Adolphus, E.", "given_names": "E.", "surname": "Adolphus", "position": "Manager", "department": "Rural Districts - Sierra Leone", "acting_status": "acting", "per_diem": "45l. 12s. 6d."},
    {"name": "The Coroner for Freetown", "canonical_name": "Coroner for Freetown, The", "surname": "Coroner", "position": "Coroner", "department": "Rural Districts - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dresser", "department": "Rural Districts - Sierra Leone", "salary_min": 36, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()