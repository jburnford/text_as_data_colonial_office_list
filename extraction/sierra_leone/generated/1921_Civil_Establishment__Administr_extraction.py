"""
Sierra Leone Colonial Office List 1921 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1921

OFFICIALS = [
    {"name": "Sir Geoffrey Francis Archer", "canonical_name": "Archer, Geoffrey Francis", "given_names": "Geoffrey Francis", "surname": "Archer", "position": "Governor and Commander-in-Chief", "department": "Civil Establishment - Sierra Leone", "salary_min": 1500, "salary_max": 1500, "duty_allowance": 300, "honors": ["K.C.M.G."]},
    {"name": "D. J. Jardine", "canonical_name": "Jardine, D. J.", "given_names": "D. J.", "surname": "Jardine", "position": "Secretary to the Administration", "department": "Civil Establishment - Sierra Leone", "salary_min": 700, "salary_max": 800, "honors": ["O.B.E."]},
    {"name": "W. L. Heape", "canonical_name": "Heape, W. L.", "given_names": "W. L.", "surname": "Heape", "position": "Assistant Secretary", "department": "Civil Establishment - Sierra Leone", "salary_min": 300, "salary_max": 600},
    {"name": "G. H. Summers", "canonical_name": "Summers, G. H.", "given_names": "G. H.", "surname": "Summers", "position": "Deputy Commissioner and Officer Commanding Troops", "department": "Civil Establishment - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "honors": ["C.M.G."], "military_rank": "Colonel"},
    {"name": "A. S. Lawrance", "canonical_name": "Lawrance, A. S.", "given_names": "A. S.", "surname": "Lawrance", "position": "District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 600, "salary_max": 700, "honors": ["D.S.O."], "military_rank": "Major"},
    {"name": "J. L. Berne", "canonical_name": "Berne, J. L.", "given_names": "J. L.", "surname": "Berne", "position": "District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 600, "salary_max": 700, "honors": ["O.B.E."], "military_rank": "Capt."},
    {"name": "A. Gibb", "canonical_name": "Gibb, A.", "given_names": "A.", "surname": "Gibb", "position": "District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 600, "salary_max": 700, "honors": ["D.S.O."], "military_rank": "Capt."},
    {"name": "R. R. H. Jebb", "canonical_name": "Jebb, R. R. H.", "given_names": "R. R. H.", "surname": "Jebb", "position": "District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 600, "salary_max": 700, "honors": ["O.B.E."]},
    {"name": "H. Rayne", "canonical_name": "Rayne, H.", "given_names": "H.", "surname": "Rayne", "position": "District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 600, "salary_max": 700, "honors": ["M.B.E.", "M.C."], "military_rank": "Major"},
    {"name": "T. D. Butler", "canonical_name": "Butler, T. D.", "given_names": "T. D.", "surname": "Butler", "position": "District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 600, "salary_max": 700},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 700},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "District Commissioners", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 700},
    {"name": "S. G. Allden", "canonical_name": "Allden, S. G.", "given_names": "S. G.", "surname": "Allden", "position": "Supply and Transport Officer", "department": "Civil Establishment - Sierra Leone", "allowances": "50l.", "military_rank": "Lt.-Major", "honors": ["D.S.O."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()