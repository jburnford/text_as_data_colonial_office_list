"""
Gambia Colonial Office List 1894 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1894

OFFICIALS = [
    {"name": "Capt. R. J Hughes", "canonical_name": "Hughes, R. J", "given_names": "R. J", "surname": "Hughes", "position": "Superintendent of Police and Sheriff", "department": "Police - Gambia", "salary_min": 400, "salary_max": 400, "per_diem": "2s. 3d."},
    {"name": "J. Brown", "canonical_name": "Brown, J.", "given_names": "J.", "surname": "Brown", "position": "Sub-Inspector of Police", "department": "Police - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "J. C. Bailey", "canonical_name": "Bailey, J. C.", "given_names": "J. C.", "surname": "Bailey", "position": "Sergeant Major of Police", "department": "Police - Gambia", "acting_status": "acting"},
    {"name": "R. H. Syrett", "canonical_name": "Syrett, R. H.", "given_names": "R. H.", "surname": "Syrett", "position": "McCarthy's Island", "department": "Police - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "G. J. Thomas", "canonical_name": "Thomas, G. J.", "given_names": "G. J.", "surname": "Thomas", "position": "British Combo", "department": "Police - Gambia", "salary_min": 100, "salary_max": 100},
    {"name": "J. H. Ozanne", "canonical_name": "Ozanne, J. H.", "given_names": "J. H.", "surname": "Ozanne", "position": "Travelling Commissioners", "department": "Police - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "C Sitwell", "canonical_name": "Sitwell, C", "given_names": "C", "surname": "Sitwell", "position": "Travelling Commissioners", "department": "Police - Gambia", "salary_min": 300, "salary_max": 300}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()