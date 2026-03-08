"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "H. E. S. Cordeaux", "canonical_name": "Cordeaux, H. E. S.", "given_names": "H. E. S.", "surname": "Cordeaux", "position": "Commissioner and Commander-in-Chief", "department": "Civil Establishment - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "honors": ["C.B.", "C.M.G."], "military_rank": "Captain"},
    {"name": "H. A. Byatt", "canonical_name": "Byatt, H. A.", "given_names": "H. A.", "surname": "Byatt", "position": "Secretary to Administration", "department": "Civil Establishment - Sierra Leone", "salary_min": 350, "salary_max": 400, "qualifications": ["B.A."]},
    {"name": "E. Le P. Power", "canonical_name": "Power, E. Le P.", "given_names": "E. Le P.", "surname": "Power", "position": "District Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. H. Thomson", "canonical_name": "Thomson, J. H.", "given_names": "J. H.", "surname": "Thomson", "position": "District Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "H. A. Daniell", "canonical_name": "Daniell, H. A.", "given_names": "H. A.", "surname": "Daniell", "position": "District Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "R. F. B. Wilbraham", "canonical_name": "Wilbraham, R. F. B.", "given_names": "R. F. B.", "surname": "Wilbraham", "position": "Assistant District Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 250, "salary_max": 300, "honors": ["Hon."]},
    {"name": "J. H. Dodds", "canonical_name": "Dodds, J. H.", "given_names": "J. H.", "surname": "Dodds", "position": "Assistant District Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "E. S. Higgins", "canonical_name": "Higgins, E. S.", "given_names": "E. S.", "surname": "Higgins", "position": "Superintendent of Police", "department": "Civil Establishment - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "C. E. Dansey", "canonical_name": "Dansey, C. E.", "given_names": "C. E.", "surname": "Dansey", "position": "Assistant Political Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "100l. allowance", "military_rank": "Captain"},
    {"name": "F. W. Bell", "canonical_name": "Bell, F. W.", "given_names": "F. W.", "surname": "Bell", "position": "Assistant Political Officer", "department": "Civil Establishment - Sierra Leone", "military_rank": "Lieut.", "honors": ["V.C."]},
    {"name": "C. R. E. Jorgensen", "canonical_name": "Jorgensen, C. R. E.", "given_names": "C. R. E.", "surname": "Jorgensen", "position": "Assistant Political Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 350, "salary_max": 400, "allowances": "50l. allowance", "military_rank": "Captain"},
    {"name": "J. C. Walker", "canonical_name": "Walker, J. C.", "given_names": "J. C.", "surname": "Walker", "position": "Assistant Political Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 250, "salary_max": 400, "allowances": "50l. allowance"},
    {"name": "R. C. Corfield", "canonical_name": "Corfield, R. C.", "given_names": "R. C.", "surname": "Corfield", "position": "Assistant Political Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 250, "salary_max": 400, "allowances": "50l. allowance"},
    {"name": "G. G. Gilligan", "canonical_name": "Gilligan, G. G.", "given_names": "G. G.", "surname": "Gilligan", "position": "Assistant Political Officer", "department": "Civil Establishment - Sierra Leone", "salary_min": 250, "salary_max": 400, "allowances": "50l. allowance"},
    {"name": "H. T. Powell", "canonical_name": "Powell, H. T.", "given_names": "H. T.", "surname": "Powell", "position": "Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 350, "salary_max": 500},
    {"name": "J. L. Whitty", "canonical_name": "Whitty, J. L.", "given_names": "J. L.", "surname": "Whitty", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "R. W. Taylor", "canonical_name": "Taylor, R. W.", "given_names": "R. W.", "surname": "Taylor", "position": "Head Accountant", "department": "Treasury Department - Sierra Leone", "salary_min": 250, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()