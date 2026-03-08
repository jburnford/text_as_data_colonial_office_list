"""
Gambia Colonial Office List 1925 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1925

OFFICIALS = [
    {"name": "H. A. Tyler-Smith", "canonical_name": "Tyler-Smith, H. A.", "given_names": "H. A.", "surname": "Tyler-Smith", "position": "Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "A. A. P. D. Stone", "canonical_name": "Stone, A. A. P. D.", "given_names": "A. A. P. D.", "surname": "Stone", "position": "Assistant Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 600, "salary_max": 920},
    {"name": "P. G. Burrage", "canonical_name": "Burrage, P. G.", "given_names": "P. G.", "surname": "Burrage", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. F. Gibbons", "canonical_name": "Gibbons, H. F.", "given_names": "H. F.", "surname": "Gibbons", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "S. Geering", "canonical_name": "Geering, S.", "given_names": "S.", "surname": "Geering", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. W. Duffield", "canonical_name": "Duffield, H. W.", "given_names": "H. W.", "surname": "Duffield", "position": "Mechanical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 500},
    {"name": "H. Heys", "canonical_name": "Heys, H.", "given_names": "H.", "surname": "Heys", "position": "Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 540, "salary_max": 720},
    {"name": "C. H. Philip", "canonical_name": "Philip, C. H.", "given_names": "C. H.", "surname": "Philip", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Stock Verifier", "department": "Public Works Department - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "A. R. Woods", "canonical_name": "Woods, A. R.", "given_names": "A. R.", "surname": "Woods", "position": "Architectural Draughtsman", "department": "Public Works Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk", "department": "Public Works Department - Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "A. R. Mason", "canonical_name": "Mason, A. R.", "given_names": "A. R.", "surname": "Mason", "position": "African Assistant Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "M. S. Maheux", "canonical_name": "Maheux, M. S.", "given_names": "M. S.", "surname": "Maheux", "position": "African Assistant Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "S. O. Tebbs", "canonical_name": "Tebbs, S. O.", "given_names": "S. O.", "surname": "Tebbs", "position": "African Assistant Accountant", "department": "Public Works Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "S. E. Goswell", "canonical_name": "Goswell, S. E.", "given_names": "S. E.", "surname": "Goswell", "position": "African Assistant Storekeepers", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "M. S. See", "canonical_name": "See, M. S.", "given_names": "M. S.", "surname": "See", "position": "African Assistant Storekeepers", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "E. J. Richards", "canonical_name": "Richards, E. J.", "given_names": "E. J.", "surname": "Richards", "position": "African Assistant Storekeepers", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "J. A. Maxwell", "canonical_name": "Maxwell, J. A.", "given_names": "J. A.", "surname": "Maxwell", "position": "3rd Grade Clerk", "department": "Public Works Department - Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. J. Diggs", "canonical_name": "Diggs, J. J.", "given_names": "J. J.", "surname": "Diggs", "position": "4th Grade Clerks", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "H. S. Dixon", "canonical_name": "Dixon, H. S.", "given_names": "H. S.", "surname": "Dixon", "position": "4th Grade Clerks", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "P. A. Williams", "canonical_name": "Williams, P. A.", "given_names": "P. A.", "surname": "Williams", "position": "4th Grade Clerks", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 82}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()