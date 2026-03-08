"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "J. H. Thomas", "canonical_name": "Thomas, J. H.", "given_names": "J. H.", "surname": "Thomas", "position": "Director of Public Works, and Commissioner of Railways", "department": "Works and Railways Department - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "R. R. Jewell", "canonical_name": "Jewell, R. R.", "given_names": "R. R.", "surname": "Jewell", "position": "Clerk of Works", "department": "Works and Railways Department - Gambia", "salary_min": 400, "salary_max": 400},
    {"name": "J. Hillman", "canonical_name": "Hillman, J.", "given_names": "J.", "surname": "Hillman", "position": "Chief Clerk", "department": "Works and Railways Department - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "A. F. Thomson", "canonical_name": "Thomson, A. F.", "given_names": "A. F.", "surname": "Thomson", "position": "Accountant Works and Railways", "department": "Works and Railways Department - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "C. E. May", "canonical_name": "May, C. E.", "given_names": "C. E.", "surname": "May", "position": "One Clerk", "department": "Works and Railways Department - Gambia", "salary_min": 120, "salary_max": 120},
    {"name": "F. Birch", "canonical_name": "Birch, F.", "given_names": "F.", "surname": "Birch", "position": "Draftsman", "department": "Works and Railways Department - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "J. Joyce", "canonical_name": "Joyce, J.", "given_names": "J.", "surname": "Joyce", "position": "Caretaker and Messenger", "department": "Works and Railways Department - Gambia", "salary_min": 65, "salary_max": 65},
    {"name": "H. E. Parry", "canonical_name": "Parry, H. E.", "given_names": "H. E.", "surname": "Parry", "position": "Traffic Manager, Locomotive Foreman and Station Master, Geraldton", "department": "Works and Railways Department - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "H. Spalding", "canonical_name": "Spalding, H.", "given_names": "H.", "surname": "Spalding", "position": "Station Master, Northampton", "department": "Works and Railways Department - Gambia", "salary_min": 90, "salary_max": 90},
    {"name": "J. C. Campbell", "canonical_name": "Campbell, J. C.", "given_names": "J. C.", "surname": "Campbell", "position": "Traffic Manager and Stationmaster, Fremantle", "department": "Works and Railways Department - Gambia", "salary_min": 275, "salary_max": 275},
    {"name": "G. F. Wilkinson", "canonical_name": "Wilkinson, G. F.", "given_names": "G. F.", "surname": "Wilkinson", "position": "Station Master, Perth", "department": "Works and Railways Department - Gambia", "salary_min": 200, "salary_max": 200},
    {"name": "R. Wynne", "canonical_name": "Wynne, R.", "given_names": "R.", "surname": "Wynne", "position": "Station Master, Guildford", "department": "Works and Railways Department - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "R. Clough", "canonical_name": "Clough, R.", "given_names": "R.", "surname": "Clough", "position": "Locomotive Foreman", "department": "Works and Railways Department - Gambia", "salary_min": 200, "salary_max": 200}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()