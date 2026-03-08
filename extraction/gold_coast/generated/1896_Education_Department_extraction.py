"""
Gold Coast Colonial Office List 1896 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1896

OFFICIALS = [
    {"name": "G. MacDonald", "canonical_name": "MacDonald, G.", "given_names": "G.", "surname": "MacDonald",
     "position": "Director of Education", "department": "Education Department - Gold Coast", "salary_min": 500, "salary_max": 500},
    {"name": "F. Wright", "canonical_name": "Wright, F.", "given_names": "F.", "surname": "Wright",
     "position": "Master in Government Schools", "department": "Education Department - Gold Coast", "salary_min": 300, "salary_max": 350},
    {"name": "J. Dobie", "canonical_name": "Dobie, J.", "given_names": "J.", "surname": "Dobie",
     "position": "Schoolmaster", "department": "Education Department - Gold Coast", "location": "Accra", "salary_min": 270, "salary_max": 270},
    {"name": "P. E. Sampson", "canonical_name": "Sampson, P. E.", "given_names": "P. E.", "surname": "Sampson",
     "position": "Assistant ditto", "department": "Education Department - Gold Coast", "location": "Accra", "salary_min": 60, "salary_max": 60},
    {"name": "Iris Parkes", "canonical_name": "Parkes, Iris", "given_names": "Iris", "surname": "Parkes",
     "position": "Schoolmistress", "department": "Education Department - Gold Coast", "location": "Accra", "salary_min": 84, "salary_max": 84},
    {"name": "H. Vanderpuye", "canonical_name": "Vanderpuye, H.", "given_names": "H.", "surname": "Vanderpuye",
     "position": "Assistant ditto", "department": "Education Department - Gold Coast", "location": "Accra", "salary_min": 54, "salary_max": 54},
    {"name": "J. A. Britton", "canonical_name": "Britton, J. A.", "given_names": "J. A.", "surname": "Britton",
     "position": "Schoolmaster", "department": "Education Department - Gold Coast", "location": "Cape Coast", "salary_min": 120, "salary_max": 120},
    {"name": "E. N. Sarbah", "canonical_name": "Sarbah, E. N.", "given_names": "E. N.", "surname": "Sarbah",
     "position": "Schoolmistress", "department": "Education Department - Gold Coast", "location": "Cape Coast", "salary_min": 72, "salary_max": 72},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()