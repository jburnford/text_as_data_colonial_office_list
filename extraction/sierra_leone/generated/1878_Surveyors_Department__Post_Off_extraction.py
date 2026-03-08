"""
Sierra Leone Colonial Office List 1878 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1878

OFFICIALS = [
    {"name": "J. C. Bauer", "canonical_name": "Bauer, J. C.", "given_names": "J. C.", "surname": "Bauer", "position": "Colonial Engineer and Sanitary Inspector", "department": "Surveyor's Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "allowance for forage and rent"},
    {"name": "Thomas Johnson", "canonical_name": "Johnson, Thomas", "given_names": "Thomas", "surname": "Johnson", "position": "Postmaster", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "S. A. Davis", "canonical_name": "Davis, S. A.", "given_names": "S. A.", "surname": "Davis", "position": "Sorter", "department": "Post Office - Sierra Leone", "salary_min": 24, "salary_max": 24},
    {"name": "Thomas H. Spilsbury", "canonical_name": "Spilsbury, Thomas H.", "given_names": "Thomas H.", "surname": "Spilsbury", "position": "Colonial Surgeon", "department": "Medical Establishment - Sierra Leone", "salary_min": 400, "salary_max": 400, "allowances": "forage allowances"},
    {"name": "T. H. Heney", "canonical_name": "Heney, T. H.", "given_names": "T. H.", "surname": "Heney", "position": "Assistant ditto", "department": "Medical Establishment - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "forage allowances"},
    {"name": "R. H. Syrett", "canonical_name": "Syrett, R. H.", "given_names": "R. H.", "surname": "Syrett", "position": "Dispenser", "department": "Medical Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100, "acting_status": "acting", "allowances": "residence, and allowance"},
    {"name": "E. Adolphus", "canonical_name": "Adolphus, E.", "given_names": "E.", "surname": "Adolphus", "position": "Chief Magistrate", "department": "Judicial Establishment - Sierra Leone", "salary_min": 600, "salary_max": 600, "allowances": "fees"},
    {"name": "Thomas Johnson", "canonical_name": "Johnson, Thomas", "given_names": "Thomas", "surname": "Johnson", "position": "Registrar of Deeds", "department": "Judicial Establishment - Sierra Leone", "allowances": "fees only"},
    {"name": "Zach. T Gibson", "canonical_name": "Gibson, Zach. T", "given_names": "Zach. T", "surname": "Gibson", "position": "Clerk of Courts and Registrar", "department": "Judicial Establishment - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "W. H. Berkeley", "canonical_name": "Berkeley, W. H.", "given_names": "W. H.", "surname": "Berkeley", "position": "Coroner", "department": "Judicial Establishment - Sierra Leone", "allowances": "fees only"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()