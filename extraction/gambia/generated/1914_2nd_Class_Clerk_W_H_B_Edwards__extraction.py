"""
Gambia Colonial Office List 1914 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1914

OFFICIALS = [
    {"name": "W. H. B. Edwards", "canonical_name": "Edwards, W. H. B.", "given_names": "W. H. B.", "surname": "Edwards", "position": "2nd Class Clerk", "department": "Civil Establishment - Gambia", "salary_min": 160, "salary_max": 200, "allowances": "25l. as Accountant"},
    {"name": "H. Bacarises", "canonical_name": "Bacarises, H.", "given_names": "H.", "surname": "Bacarises", "position": "3rd Class Clerk", "department": "Civil Establishment - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "J. Dotto", "canonical_name": "Dotto, J.", "given_names": "J.", "surname": "Dotto", "position": "3rd Class Clerk", "department": "Civil Establishment - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "W. H. Niles", "canonical_name": "Niles, W. H.", "given_names": "W. H.", "surname": "Niles", "position": "Captain of the Port and Shipping Master", "department": "Port Department - Gambia", "salary_min": 500, "salary_max": 500, "allowances": "60l. as Superintendent of Lighthouse", "military_rank": "Commander"},
    {"name": "F. B. Planello", "canonical_name": "Planello, F. B.", "given_names": "F. B.", "surname": "Planello", "position": "1st Class Clerk and Clerk to Shipping Master", "department": "Port Department - Gambia", "salary_min": 210, "salary_max": 300, "allowances": "moiety of shipping fees"},
    {"name": "J. B. Triay", "canonical_name": "Triay, J. B.", "given_names": "J. B.", "surname": "Triay", "position": "1st Class Clerk", "department": "Port Department - Gambia", "salary_min": 210, "salary_max": 300},
    {"name": "J. Rowland Crook", "canonical_name": "Crook, J. Rowland", "given_names": "J. Rowland", "surname": "Crook", "position": "Government Engineer", "department": "Public Works - Gambia", "salary_min": 500, "salary_max": 600, "qualifications": ["M.I.C.E."], "allowances": "42l. for forage allowance"},
    {"name": "D. Benatar", "canonical_name": "Benatar, D.", "given_names": "D.", "surname": "Benatar", "position": "Surveyor", "department": "Public Works - Gambia", "salary_min": 200, "salary_max": 250, "qualifications": ["B.So.", "B.Eng."]},
    {"name": "H. F. J. Maxted", "canonical_name": "Maxted, H. F. J.", "given_names": "H. F. J.", "surname": "Maxted", "position": "1st Class Clerk", "department": "Public Works - Gambia", "salary_min": 210, "salary_max": 300, "allowances": "45l. as Secretary to Cemetery Committee"},
    {"name": "S. Chiappe", "canonical_name": "Chiappe, S.", "given_names": "S.", "surname": "Chiappe", "position": "Clerk of Works", "department": "Public Works - Gambia", "salary_min": 100, "salary_max": 150}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()