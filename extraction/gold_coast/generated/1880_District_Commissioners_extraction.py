"""
Gold Coast Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1880

OFFICIALS = [
    {"name": "Isaac Addo", "canonical_name": "Addo, Isaac", "given_names": "Isaac", "surname": "Addo",
     "position": "District Commissioner", "department": "District Commissioners - Gold Coast", "location": "Accra", "salary_min": 50, "allowances": "Free quarters."},
    {"name": "A. D. Gauthier", "canonical_name": "Gauthier, A. D.", "given_names": "A. D.", "surname": "Gauthier",
     "position": "Deputy Registrar", "department": "District Commissioners - Gold Coast", "location": "Accra", "salary_min": 20},
    {"name": "A. Fitzjohn", "canonical_name": "Fitzjohn, A.", "given_names": "A.", "surname": "Fitzjohn",
     "position": "District Commissioner", "department": "District Commissioners - Gold Coast", "location": "Quittah", "salary_min": 60, "allowances": "Free quarters."},
    {"name": "John Blavo", "canonical_name": "Blavo, John", "given_names": "John", "surname": "Blavo",
     "position": "Deputy Registrar", "department": "District Commissioners - Gold Coast", "location": "Quittah", "salary_min": 50, "allowances": "Free quarters."},
    {"name": "J. S. Parker", "canonical_name": "Parker, J. S.", "given_names": "J. S.", "surname": "Parker",
     "position": "Interpreter", "department": "District Commissioners - Gold Coast", "location": "Quittah", "salary_min": 250, "acting_status": "acting", "allowances": "Free quarters."},
    {"name": "Andrew C. Holm", "canonical_name": "Holm, Andrew C.", "given_names": "Andrew C.", "surname": "Holm",
     "position": "District Commissioner", "department": "District Commissioners - Gold Coast", "location": "Addah", "salary_min": 50},
    {"name": "Samuel C. Brew", "canonical_name": "Brew, Samuel C.", "given_names": "Samuel C.", "surname": "Brew",
     "position": "District Commissioner", "department": "District Commissioners - Gold Coast", "location": "Winnebah", "salary_min": 200, "allowances": "Free quarters."},
    {"name": "C. C. Mills", "canonical_name": "Mills, C. C.", "given_names": "C. C.", "surname": "Mills",
     "position": "Deputy Registrar and Interpreter", "department": "District Commissioners - Gold Coast", "location": "Winnebah", "salary_min": 50, "allowances": "Free quarters."},
    {"name": "J. S. Mills", "canonical_name": "Mills, J. S.", "given_names": "J. S.", "surname": "Mills",
     "position": "Deputy Registrar and Interpreter", "department": "District Commissioners - Gold Coast", "location": "Saltpond", "salary_min": 60, "allowances": "Free quarters."},
    {"name": "Edmund Watt", "canonical_name": "Watt, Edmund", "given_names": "Edmund", "surname": "Watt",
     "position": "Civil Commissioner", "department": "District Commissioners - Gold Coast", "location": "Cape Coast", "salary_min": 700},
    {"name": "P. H. G. Hughes", "canonical_name": "Hughes, P. H. G.", "given_names": "P. H. G.", "surname": "Hughes",
     "position": "District Commissioner", "department": "District Commissioners - Gold Coast", "location": "Cape Coast", "salary_min": 400, "allowances": "Free quarters"},
    {"name": "Thomas Blankson", "canonical_name": "Blankson, Thomas", "given_names": "Thomas", "surname": "Blankson",
     "position": "District Registrar and Interpreter", "department": "District Commissioners - Gold Coast", "location": "Cape Coast", "salary_min": 50},
    {"name": "James Davis", "canonical_name": "Davis, James", "given_names": "James", "surname": "Davis",
     "position": "Messenger to Native Chiefs", "department": "District Commissioners - Gold Coast", "location": "Cape Coast", "salary_min": 60},
    {"name": "Cudjoe Sago", "canonical_name": "Sago, Cudjoe", "given_names": "Cudjoe", "surname": "Sago",
     "position": "Messenger to Interior", "department": "District Commissioners - Gold Coast", "location": "Cape Coast", "salary_min": 36},
    {"name": "Alexander Grant", "canonical_name": "Grant, Alexander", "given_names": "Alexander", "surname": "Grant",
     "position": "District Commissioner", "department": "District Commissioners - Gold Coast", "location": "Elmina", "allowances": "Free quarters"},
    {"name": "C. J. Mensah", "canonical_name": "Mensah, C. J.", "given_names": "C. J.", "surname": "Mensah",
     "position": "Deputy Registrar and Interpreter", "department": "District Commissioners - Gold Coast", "location": "Elmina", "salary_min": 40},
    {"name": "Isaac G. Jones", "canonical_name": "Jones, Isaac G.", "given_names": "Isaac G.", "surname": "Jones",
     "position": "District Commissioner", "department": "District Commissioners - Gold Coast", "location": "Secondee", "salary_min": 250, "allowances": "Free quarters"},
    {"name": "George Smith", "canonical_name": "Smith, George", "given_names": "George", "surname": "Smith",
     "position": "District Commissioner", "department": "District Commissioners - Gold Coast", "location": "Dixcove", "salary_min": 200, "allowances": "Free quarters"},
    {"name": "Mauritz Mends", "canonical_name": "Mends, Mauritz", "given_names": "Mauritz", "surname": "Mends",
     "position": "Deputy Registrar and Interpreter", "department": "District Commissioners - Gold Coast", "location": "Dixcove", "salary_min": 50},
    {"name": "Louis Wyatt", "canonical_name": "Wyatt, Louis", "given_names": "Louis", "surname": "Wyatt",
     "position": "District Commissioner", "department": "District Commissioners - Gold Coast", "location": "Axim", "allowances": "Free quarters"},
    {"name": "Joseph Lazarus Minnow", "canonical_name": "Minnow, Joseph Lazarus", "given_names": "Joseph Lazarus", "surname": "Minnow",
     "position": "Deputy Registrar and Interpreter", "department": "District Commissioners - Gold Coast", "location": "Axim", "salary_min": 60},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()