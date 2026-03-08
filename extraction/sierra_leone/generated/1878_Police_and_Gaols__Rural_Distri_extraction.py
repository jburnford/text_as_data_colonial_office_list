"""
Sierra Leone Colonial Office List 1878 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1878

OFFICIALS = [
    {"name": "M. Doorly", "canonical_name": "Doorly, M.", "given_names": "M.", "surname": "Doorly", "position": "Police Magistrate", "department": "Police and Gaols - Sierra Leone", "salary_min": 500, "salary_max": 500, "military_rank": "Major"},
    {"name": "J. M. Davis", "canonical_name": "Davis, J. M.", "given_names": "J. M.", "surname": "Davis", "position": "Clerk of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 200, "salary_max": 200, "acting_status": "acting"},
    {"name": "J. C. Loggie", "canonical_name": "Loggie, J. C.", "given_names": "J. C.", "surname": "Loggie", "position": "Inspector-General of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 400, "salary_max": 400, "allowances": "91l. 5s.", "honors": ["C.M.G."]},
    {"name": "Geo. Neville", "canonical_name": "Neville, Geo.", "given_names": "Geo.", "surname": "Neville", "position": "Inspector of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "W. E. Inniss", "canonical_name": "Inniss, W. E.", "given_names": "W. E.", "surname": "Inniss", "position": "Keeper of Freetown Gaol", "department": "Police and Gaols - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "John Thompson", "canonical_name": "Thompson, John", "given_names": "John", "surname": "Thompson", "position": "Assistant ditto", "department": "Police and Gaols - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "The Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Manager, 1st Eastern District", "department": "Rural Districts - Sierra Leone", "salary_min": 45, "salary_max": 45, "allowances": "12s. 6d."},
    {"name": "The Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Manager, Mountain District", "department": "Rural Districts - Sierra Leone"},
    {"name": "Wm. Budge", "canonical_name": "Budge, Wm.", "given_names": "Wm.", "surname": "Budge", "position": "Manager and Coroner, 2nd Eastern District", "department": "Rural Districts - Sierra Leone", "salary_min": 320, "salary_max": 320, "allowances": "91l. 5s. 0d."},
    {"name": "J. B. Elliott", "canonical_name": "Elliott, J. B.", "given_names": "J. B.", "surname": "Elliott", "position": "Manager and Coroner, Western District", "department": "Rural Districts - Sierra Leone", "salary_min": 270, "salary_max": 270, "allowances": "40l. rent"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()