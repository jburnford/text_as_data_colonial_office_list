"""
Gambia Colonial Office List 1940 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1940

OFFICIALS = [
    {"name": "F. J. C. Palmour", "canonical_name": "Palmour, F. J. C.", "given_names": "F. J. C.", "surname": "Palmour", "position": "Land Officer and Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 690, "salary_max": 840},
    {"name": "W. A. Small", "canonical_name": "Small, W. A.", "given_names": "W. A.", "surname": "Small", "position": "African Surveyor", "department": "Land and Survey Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "E. L. Auber", "canonical_name": "Auber, E. L.", "given_names": "E. L.", "surname": "Auber", "position": "Chief Clerk, 1st Grade", "department": "Land and Survey Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "A. G. Still", "canonical_name": "Still, A. G.", "given_names": "A. G.", "surname": "Still", "position": "Auditor", "department": "Audit Office - Gambia", "salary_min": 600, "salary_max": 920, "allowances": "72l. seniority allowance from 720l. and 100l. local allowance, personal."},
    {"name": "A. Skinner", "canonical_name": "Skinner, A.", "given_names": "A.", "surname": "Skinner", "position": "Harbour Master and Marine Superintendent", "department": "Marine - Gambia", "salary_min": 630, "salary_max": 840},
    {"name": "J. M. Simpson", "canonical_name": "Simpson, J. M.", "given_names": "J. M.", "surname": "Simpson", "position": "Chief Engineer", "department": "Marine - Gambia", "salary_min": 510, "salary_max": 720, "honors": ["O.B.E."]},
    {"name": "J. Reid", "canonical_name": "Reid, J.", "given_names": "J.", "surname": "Reid", "position": "Artificer Engineer", "department": "Marine - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "R. E. G. Deall", "canonical_name": "Deall, R. E. G.", "given_names": "R. E. G.", "surname": "Deall", "position": "Transport Officer", "department": "Marine - Gambia", "salary_min": 400, "salary_max": 500, "military_rank": "Captain"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Senior Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 690, "salary_max": 840},
    {"name": "J. D. Tallantire", "canonical_name": "Tallantire, J. D.", "given_names": "J. D.", "surname": "Tallantire", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 490, "salary_max": 600},
    {"name": "L. H. Saunders", "canonical_name": "Saunders, L. H.", "given_names": "L. H.", "surname": "Saunders", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 480, "salary_max": 840},
    {"name": "H. J. Taylor", "canonical_name": "Taylor, H. J.", "given_names": "H. J.", "surname": "Taylor", "position": "Agricultural Superintendent", "department": "Agricultural Department - Gambia", "salary_min": 450, "salary_max": 630},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Officer Commanding", "department": "Royal West African Frontier Force - Gambia", "salary_min": 700, "salary_max": 700, "duty_allowance": 55}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()