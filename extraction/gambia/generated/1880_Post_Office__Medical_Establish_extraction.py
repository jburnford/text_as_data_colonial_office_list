"""
Gambia Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1880

OFFICIALS = [
    {"name": "Thomas Johnson", "canonical_name": "Johnson, Thomas", "given_names": "Thomas", "surname": "Johnson", "position": "Postmaster", "department": "Post Office - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "J. T. Shooter", "canonical_name": "Shooter, J. T.", "given_names": "J. T.", "surname": "Shooter", "position": "Sorter", "department": "Post Office - Gambia", "salary_min": 24, "salary_max": 24},
    {"name": "Thomas H. Spilsbury", "canonical_name": "Spilsbury, Thomas H.", "given_names": "Thomas H.", "surname": "Spilsbury", "position": "Colonial Surgeon", "department": "Medical Establishment - Gambia", "salary_min": 400, "salary_max": 400, "allowances": "forage allowances"},
    {"name": "T. H. Heney", "canonical_name": "Heney, T. H.", "given_names": "T. H.", "surname": "Heney", "position": "Assistant ditto", "department": "Medical Establishment - Gambia", "salary_min": 300, "salary_max": 300, "allowances": "forage allowances"},
    {"name": "S. W. Dawson", "canonical_name": "Dawson, S. W.", "given_names": "S. W.", "surname": "Dawson", "position": "Dispenser", "department": "Medical Establishment - Gambia", "salary_min": 50, "salary_max": 50, "allowances": "residence, and allowance", "acting_status": "Acting"},
    {"name": "Francis Smith", "canonical_name": "Smith, Francis", "given_names": "Francis", "surname": "Smith", "position": "Chief Magistrate", "department": "Judicial Establishment - Gambia", "salary_min": 600, "salary_max": 600, "allowances": "fees"},
    {"name": "Thomas Johnson", "canonical_name": "Johnson, Thomas", "given_names": "Thomas", "surname": "Johnson", "position": "Registrar of Deeds", "department": "Judicial Establishment - Gambia", "allowances": "fees only"},
    {"name": "Zach. T Gibson", "canonical_name": "Gibson, Zach. T", "given_names": "Zach. T", "surname": "Gibson", "position": "Clerk of Courts and Registrar", "department": "Judicial Establishment - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "W. H. Berkeley", "canonical_name": "Berkeley, W. H.", "given_names": "W. H.", "surname": "Berkeley", "position": "Coroner", "department": "Judicial Establishment - Gambia", "allowances": "fees only"},
    {"name": "W. P. Roche", "canonical_name": "Roche, W. P.", "given_names": "W. P.", "surname": "Roche", "position": "Superintendent of Police", "department": "Police and Gaols - Gambia", "salary_min": 200, "salary_max": 200, "allowances": "forage allowances", "military_rank": "Capt."},
    {"name": "J. M. S. Johns", "canonical_name": "Johns, J. M. S.", "given_names": "J. M. S.", "surname": "Johns", "position": "Gaoler", "department": "Police and Gaols - Gambia", "salary_min": 75, "salary_max": 75},
    {"name": "E. A. M. Smith", "canonical_name": "Smith, E. A. M.", "given_names": "E. A. M.", "surname": "Smith", "position": "Manager of Districts", "department": "Managers of Districts - Gambia", "salary_min": 250, "salary_max": 250, "location": "McCarthy's Island", "allowances": "residence, and forage allowance"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()