"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "J. Lochhead", "canonical_name": "Lochhead, J.", "given_names": "J.", "surname": "Lochhead", "position": "Surgeon, Colonial Hospital", "department": "Medical Department - Gambia", "salary_min": 400, "salary_max": 400, "qualifications": ["M.D."]},
    {"name": "T. R. Robertson", "canonical_name": "Robertson, T. R.", "given_names": "T. R.", "surname": "Robertson", "position": "Assistant Surgeon, Colonial Hospital", "department": "Medical Department - Gambia", "salary_min": 350, "salary_max": 350, "qualifications": ["M.B."]},
    {"name": "R. F. Priestley", "canonical_name": "Priestley, R. F.", "given_names": "R. F.", "surname": "Priestley", "position": "2nd Assistant Surgeon", "department": "Medical Department - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "L. H. Gill", "canonical_name": "Gill, L. H.", "given_names": "L. H.", "surname": "Gill", "position": "Deputy Surgeon", "department": "Medical Department - Gambia", "salary_min": 125, "salary_max": 125},
    {"name": "A. J. Triay", "canonical_name": "Triay, A. J.", "given_names": "A. J.", "surname": "Triay", "position": "Surgeon Smallpox Hospital", "department": "Medical Department - Gambia", "salary_min": 60, "salary_max": 60, "qualifications": ["M.B."]},
    {"name": "H. G. Warr", "canonical_name": "Warr, H. G.", "given_names": "H. G.", "surname": "Warr", "position": "Secretary, Colonial Hospital", "department": "Medical Department - Gambia", "salary_min": 220, "salary_max": 250},
    {"name": "H. Recalo", "canonical_name": "Recalo, H.", "given_names": "H.", "surname": "Recalo", "position": "Clerk, ditto", "department": "Medical Department - Gambia", "salary_min": 200, "salary_max": 200},
    {"name": "N. Oman", "canonical_name": "Oman, N.", "given_names": "N.", "surname": "Oman", "position": "Port Surgeon", "department": "Medical Department - Gambia", "salary_min": 60, "salary_max": 60, "qualifications": ["M.D."]},
    {"name": "J. V. Albrino", "canonical_name": "Albrino, J. V.", "given_names": "J. V.", "surname": "Albrino", "position": "Deputy Port Surgeon", "department": "Medical Department - Gambia", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()