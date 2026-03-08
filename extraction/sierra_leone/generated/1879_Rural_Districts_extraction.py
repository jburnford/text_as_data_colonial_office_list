"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "The Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Manager, 1st East ra District", "department": "Rural Districts - Sierra Leone", "salary_min": 45, "salary_max": 45, "allowances": "travelling allowance", "duty_allowance": 20},
    {"name": "The Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Manager, Mountain District", "department": "Rural Districts - Sierra Leone", "duty_allowance": 20},
    {"name": "Wm. Budge", "canonical_name": "Budge, William", "given_names": "Wm.", "surname": "Budge", "position": "Manager and Coroner, 2nd Eastern District", "department": "Rural Districts - Sierra Leone", "salary_min": 320, "salary_max": 320, "allowances": "travelling allowance, 91l. 5s. 0d., and a house."},
    {"name": "J. B. Elliott", "canonical_name": "Elliott, J. B.", "given_names": "J. B.", "surname": "Elliott", "position": "Manager and Coroner, Western District", "department": "Rural Districts - Sierra Leone", "salary_min": 270, "salary_max": 270, "allowances": "40l. rent."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()