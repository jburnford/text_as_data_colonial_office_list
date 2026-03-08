"""
Gambia Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1923

OFFICIALS = [
    {"name": "S. Gaye", "canonical_name": "Gaye, S.", "given_names": "S.", "surname": "Gaye", "position": "Caretaker", "department": "MacCarthy Square Board - Gambia", "salary_min": 48, "salary_max": 48},
    {"name": "H. A. Tyler-Smith", "canonical_name": "Tyler-Smith, H. A.", "given_names": "H. A.", "surname": "Tyler-Smith", "position": "Director of Public Works", "department": "Public Works Department - Gambia", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "A. A. P. D. Stone", "canonical_name": "Stone, A. A. P. D.", "given_names": "A. A. P. D.", "surname": "Stone", "position": "District Engineer", "department": "Public Works Department - Gambia", "salary_min": 600, "salary_max": 920, "location": "Georgetown"},
    {"name": "R. H. Phillips", "canonical_name": "Phillips, R. H.", "given_names": "R. H.", "surname": "Phillips", "position": "Assistant Engineer", "department": "Public Works Department - Gambia", "salary_min": 480, "salary_max": 720},
    {"name": "P. G. Burrage", "canonical_name": "Burrage, P. G.", "given_names": "P. G.", "surname": "Burrage", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. F. Gibbons", "canonical_name": "Gibbons, H. F.", "given_names": "H. F.", "surname": "Gibbons", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "S. Geering", "canonical_name": "Geering, S.", "given_names": "S.", "surname": "Geering", "position": "Clerk of Works", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "A. V. E. Batchelor", "canonical_name": "Batchelor, A. V. E.", "given_names": "A. V. E.", "surname": "Batchelor", "position": "Mechanical Foreman", "department": "Public Works Department - Gambia", "salary_min": 500, "salary_max": 560},
    {"name": "H. Heys", "canonical_name": "Heys, H.", "given_names": "H.", "surname": "Heys", "position": "Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 540, "salary_max": 720},
    {"name": "W. N. Chicken", "canonical_name": "Chicken, W. N.", "given_names": "W. N.", "surname": "Chicken", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 450, "salary_max": 600},
    {"name": "A. R. Woods", "canonical_name": "Woods, A. R.", "given_names": "A. R.", "surname": "Woods", "position": "Architectural Draughtsman", "department": "Public Works Department - Gambia", "salary_min": 480, "salary_max": 600},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Chief Clerk", "department": "Public Works Department - Gambia", "salary_min": 180, "salary_max": 230},
    {"name": "A. R. Mason", "canonical_name": "Mason, A. R.", "given_names": "A. R.", "surname": "Mason", "position": "African Assistant Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "M. S. Meheux", "canonical_name": "Meheux, M. S.", "given_names": "M. S.", "surname": "Meheux", "position": "African Assistant Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "S. O. Tebbs", "canonical_name": "Tebbs, S. O.", "given_names": "S. O.", "surname": "Tebbs", "position": "African Assistant Accountant", "department": "Public Works Department - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "H. G. Meyer", "canonical_name": "Meyer, H. G.", "given_names": "H. G.", "surname": "Meyer", "position": "African Assistant Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "S. E. Goswell", "canonical_name": "Goswell, S. E.", "given_names": "S. E.", "surname": "Goswell", "position": "African Assistant Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "M. S. See", "canonical_name": "See, M. S.", "given_names": "M. S.", "surname": "See", "position": "African Assistant Storekeeper", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. A. Maxwell", "canonical_name": "Maxwell, J. A.", "given_names": "J. A.", "surname": "Maxwell", "position": "2nd Grade Clerk", "department": "Public Works Department - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "R. E. Clarke", "canonical_name": "Clarke, R. E.", "given_names": "R. E.", "surname": "Clarke", "position": "3rd Grade Clerk", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. J. Diggs", "canonical_name": "Diggs, J. J.", "given_names": "J. J.", "surname": "Diggs", "position": "3rd Grade Clerk", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "P. A. Williams", "canonical_name": "Williams, P. A.", "given_names": "P. A.", "surname": "Williams", "position": "3rd Grade Clerk", "department": "Public Works Department - Gambia", "salary_min": 50, "salary_max": 80}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()