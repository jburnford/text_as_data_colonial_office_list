"""
Sierra Leone Colonial Office List 1889 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1889

OFFICIALS = [
    {"name": "W. M. Huggins", "canonical_name": "Huggins, W. M.", "given_names": "W. M.", "surname": "Huggins", "position": "Manager", "department": "Districts - Sierra Leone", "salary_min": 300, "salary_max": 300, "acting_status": "Acting", "allowances": "9l. 5s., and quarters", "region": "2nd Eastern"},
    {"name": "M. J. W. Rocks", "canonical_name": "Rocks, M. J. W.", "given_names": "M. J. W.", "surname": "Rocks", "position": "Clerk", "department": "Districts - Sierra Leone", "salary_min": 30, "salary_max": 30, "region": "2nd Eastern"},
    {"name": "The Manager", "canonical_name": "Manager, The", "surname": "Manager", "position": "Coroner", "department": "Districts - Sierra Leone", "salary_min": 20, "salary_max": 20, "region": "2nd Eastern"},
    {"name": "W. Z. Young", "canonical_name": "Young, W. Z.", "given_names": "W. Z.", "surname": "Young", "position": "Medical Dresser", "department": "Districts - Sierra Leone", "salary_min": 50, "salary_max": 50, "location": "Waterloo", "region": "2nd Eastern"},
    {"name": "N. Dundas", "canonical_name": "Dundas, N.", "given_names": "N.", "surname": "Dundas", "position": "Ditto", "department": "Districts - Sierra Leone", "salary_min": 36, "salary_max": 36, "location": "Hastings", "region": "2nd Eastern"},
    {"name": "M. J. W. Rocks", "canonical_name": "Rocks, M. J. W.", "given_names": "M. J. W.", "surname": "Rocks", "position": "Registrar", "department": "Districts - Sierra Leone", "region": "2nd Eastern"},
    {"name": "J. M. Metzger", "canonical_name": "Metzger, J. M.", "given_names": "J. M.", "surname": "Metzger", "position": "Manager", "department": "Districts - Sierra Leone", "salary_min": 250, "salary_max": 250, "allowances": "rent 40l.", "region": "Western District"},
    {"name": "J. B. McCormack", "canonical_name": "McCormack, J. B.", "given_names": "J. B.", "surname": "McCormack", "position": "Clerk", "department": "Districts - Sierra Leone", "salary_min": 30, "salary_max": 30, "region": "Western District"},
    {"name": "The Manager", "canonical_name": "Manager, The", "surname": "Manager", "position": "Coroner", "department": "Districts - Sierra Leone", "salary_min": 20, "salary_max": 20, "region": "Western District"},
    {"name": "W. Dawson", "canonical_name": "Dawson, W.", "given_names": "W.", "surname": "Dawson", "position": "Medical Dresser", "department": "Districts - Sierra Leone", "salary_min": 40, "salary_max": 40, "location": "Kent", "region": "Western District"},
    {"name": "D. M. P. Thorpe", "canonical_name": "Thorpe, D. M. P.", "given_names": "D. M. P.", "surname": "Thorpe", "position": "Ditto", "department": "Districts - Sierra Leone", "salary_min": 36, "salary_max": 36, "location": "York", "region": "Western District"},
    {"name": "E. Adolphus", "canonical_name": "Adolphus, E.", "given_names": "E.", "surname": "Adolphus", "position": "Manager", "department": "Districts - Sierra Leone", "allowances": "travelling allowance, 45l. 12s. 6d.", "region": "Mountain District"},
    {"name": "The Coroner for Freetown", "canonical_name": "Coroner for Freetown, The", "surname": "Coroner", "position": "Coroner", "department": "Districts - Sierra Leone", "salary_min": 20, "salary_max": 20, "region": "Mountain District"},
    {"name": "W. Harding", "canonical_name": "Harding, W.", "given_names": "W.", "surname": "Harding", "position": "Medical Dresser", "department": "Districts - Sierra Leone", "salary_min": 36, "salary_max": 36, "location": "Regent", "region": "Mountain District"},
    {"name": "Rev. N. J. Cole", "canonical_name": "Cole, N. J.", "given_names": "N. J.", "surname": "Cole", "position": "Registrar", "department": "Districts - Sierra Leone", "region": "Mountain District"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()