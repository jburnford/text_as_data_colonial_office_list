"""
Gold Coast Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1880

OFFICIALS = [
    {"name": "John Pagan", "canonical_name": "Pagan, John", "given_names": "John", "surname": "Pagan",
     "position": "Surveyor General", "department": "Public Works Department - Gold Coast", "salary_min": 800},
    {"name": "Matthew Jones", "canonical_name": "Jones, Matthew", "given_names": "Matthew", "surname": "Jones",
     "position": "Assistant Colonial Surveyor", "department": "Public Works Department - Gold Coast", "salary_min": 350},
    {"name": "John Snowley", "canonical_name": "Snowley, John", "given_names": "John", "surname": "Snowley",
     "position": "Foremen of Works", "department": "Public Works Department - Gold Coast", "salary_min": 250},
    {"name": "W. M. Constable", "canonical_name": "Constable, W. M.", "given_names": "W. M.", "surname": "Constable",
     "position": "Foremen of Works", "department": "Public Works Department - Gold Coast", "salary_min": 250},
    {"name": "Thomas Djapia", "canonical_name": "Djapia, Thomas", "given_names": "Thomas", "surname": "Djapia",
     "position": "Foremen of Works", "department": "Public Works Department - Gold Coast", "salary_min": 60},
    {"name": "J. M. Brown", "canonical_name": "Brown, J. M.", "given_names": "J. M.", "surname": "Brown",
     "position": "Clerk", "department": "Public Works Department - Gold Coast", "salary_min": 55},
    {"name": "R. J. Ghartey", "canonical_name": "Ghartey, R. J.", "given_names": "R. J.", "surname": "Ghartey",
     "position": "Storekeeper and Issuer", "department": "Public Works Department - Gold Coast", "salary_min": 40},
    {"name": "Charles Affull", "canonical_name": "Affull, Charles", "given_names": "Charles", "surname": "Affull",
     "position": "Messenger and Yardkeeper", "department": "Public Works Department - Gold Coast", "salary_min": 20},
    {"name": "G. Meyer", "canonical_name": "Meyer, G.", "given_names": "G.", "surname": "Meyer",
     "position": "Storekeeper and Issuer", "department": "Public Works Department - Gold Coast", "per_diem": "1s."},
    {"name": "M. D. Thorpe", "canonical_name": "Thorpe, M. D.", "given_names": "M. D.", "surname": "Thorpe",
     "position": "Clerk and Accountant", "department": "Public Works Department - Gold Coast", "salary_min": 60},
    {"name": "J. A. Mills", "canonical_name": "Mills, J. A.", "given_names": "J. A.", "surname": "Mills",
     "position": "Inspector of Nuisances", "department": "Sanitary Department - Gold Coast", "salary_min": 30, "location": "Accra"},
    {"name": "Adolph Limberg", "canonical_name": "Limberg, Adolph", "given_names": "Adolph", "surname": "Limberg",
     "position": "Inspector of Nuisances", "department": "Sanitary Department - Gold Coast", "salary_min": 30, "location": "Christianborg"},
    {"name": "P. L. Bartels", "canonical_name": "Bartels, P. L.", "given_names": "P. L.", "surname": "Bartels",
     "position": "Inspector of Nuisances", "department": "Sanitary Department - Gold Coast", "salary_min": 30, "location": "Cape Coast"},
    {"name": "J. S. Anderson", "canonical_name": "Anderson, J. S.", "given_names": "J. S.", "surname": "Anderson",
     "position": "Inspector of Nuisances", "department": "Sanitary Department - Gold Coast", "salary_min": 45, "location": "Elmina"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()