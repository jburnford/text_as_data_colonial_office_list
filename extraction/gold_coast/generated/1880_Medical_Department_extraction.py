"""
Gold Coast Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1880

OFFICIALS = [
    {"name": "Dr. J. H. Jeans", "canonical_name": "Jeans, J. H.", "given_names": "J. H.", "surname": "Jeans",
     "position": "Colonial Surgeon", "department": "Medical Department - Gold Coast", "salary_min": 600},
    {"name": "Dr. C. S. Grant", "canonical_name": "Grant, C. S.", "given_names": "C. S.", "surname": "Grant",
     "position": "Assistant Surgeon", "department": "Medical Department - Gold Coast", "salary_min": 400},
    {"name": "C. F. Castor", "canonical_name": "Castor, C. F.", "given_names": "C. F.", "surname": "Castor",
     "position": "Assistant Dispenser", "department": "Medical Department - Gold Coast", "salary_min": 400, "location": "Cape Coast"},
    {"name": "John Randle", "canonical_name": "Randle, John", "given_names": "John", "surname": "Randle",
     "position": "Smallpox Hospital Keeper", "department": "Medical Department - Gold Coast", "salary_min": 70},
    {"name": "J. B. Hagan", "canonical_name": "Hagan, J. B.", "given_names": "J. B.", "surname": "Hagan",
     "position": "Dresser", "department": "Medical Department - Gold Coast", "salary_min": 50, "location": "Elmina"},
    {"name": "Wallis E. Ansah", "canonical_name": "Ansah, Wallis E.", "given_names": "Wallis E.", "surname": "Ansah",
     "position": "Wardman", "department": "Medical Department - Gold Coast", "salary_min": 36, "location": "Elmina"},
    {"name": "W. Classpeter", "canonical_name": "Classpeter, W.", "given_names": "W.", "surname": "Classpeter",
     "position": "Wardman", "department": "Medical Department - Gold Coast", "salary_min": 20, "location": "Elmina"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()