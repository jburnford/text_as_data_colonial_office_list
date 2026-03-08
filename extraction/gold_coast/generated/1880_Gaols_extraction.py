"""
Gold Coast Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1880

OFFICIALS = [
    {"name": "Alexander Grant", "canonical_name": "Grant, Alexander", "given_names": "Alexander", "surname": "Grant", "position": "Sheriff (Western Province)", "department": "Gaols - Gold Coast"},
    {"name": "T. W. Jackson", "canonical_name": "Jackson, T. W.", "given_names": "T. W.", "surname": "Jackson", "position": "Deputy Sheriff (Central Province)", "department": "Gaols - Gold Coast"},
    {"name": "P. H. G. Hughes", "canonical_name": "Hughes, P. H. G.", "given_names": "P. H. G.", "surname": "Hughes", "position": "Visiting Committee", "department": "Gaols - Gold Coast"},
    {"name": "G. C. Childs", "canonical_name": "Childs, G. C.", "given_names": "G. C.", "surname": "Childs", "position": "Visiting Committee", "department": "Gaols - Gold Coast"},
    {"name": "Alexander Grant", "canonical_name": "Grant, Alexander", "given_names": "Alexander", "surname": "Grant", "position": "Visiting Committee", "department": "Gaols - Gold Coast"},
    {"name": "Dr. J. D. McCarthy", "canonical_name": "McCarthy, J. D.", "given_names": "J. D.", "surname": "McCarthy", "position": "Visiting Committee", "department": "Gaols - Gold Coast"},
    {"name": "T. Woodcock", "canonical_name": "Woodcock, T.", "given_names": "T.", "surname": "Woodcock", "position": "Visiting Committee", "department": "Gaols - Gold Coast"},
    {"name": "Alexander Grant", "canonical_name": "Grant, Alexander", "given_names": "Alexander", "surname": "Grant", "position": "Officer in charge of Gaols (Western Province)", "department": "Gaols - Gold Coast", "salary_min": 50, "salary_max": 50},
    {"name": None, "canonical_name": None, "position": "Officer in charge of Gaols (Central Province)", "department": "Gaols - Gold Coast", "salary_min": 40, "salary_max": 40},
    {"name": "J. R. Smith", "canonical_name": "Smith, J. R.", "given_names": "J. R.", "surname": "Smith", "position": "Gaoler, Accra", "department": "Gaols - Gold Coast", "salary_min": 50, "salary_max": 50, "location": "Accra"},
    {"name": "J. Symon", "canonical_name": "Symon, J.", "given_names": "J.", "surname": "Symon", "position": "Turnkey", "department": "Gaols - Gold Coast", "salary_min": 40, "salary_max": 40},
    {"name": "Albert D. Amour", "canonical_name": "Amour, Albert D.", "given_names": "Albert D.", "surname": "Amour", "position": "Gaoler, Saltpond", "department": "Gaols - Gold Coast", "salary_min": 36, "salary_max": 36, "location": "Saltpond"},
    {"name": "J. A. Niezer", "canonical_name": "Niezer, J. A.", "given_names": "J. A.", "surname": "Niezer", "position": "” Winnebah", "department": "Gaols - Gold Coast", "salary_min": 36, "salary_max": 36},
    {"name": "J. G. Peters", "canonical_name": "Peters, J. G.", "given_names": "J. G.", "surname": "Peters", "position": "” Elmina", "department": "Gaols - Gold Coast", "salary_min": 100, "salary_max": 100, "location": "Elmina"},
    {"name": "James O. Peters", "canonical_name": "Peters, James O.", "given_names": "James O.", "surname": "Peters", "position": "First Turnkey, Elmina", "department": "Gaols - Gold Coast", "salary_min": 60, "salary_max": 60, "location": "Elmina"},
    {"name": "W. R. Niezer", "canonical_name": "Niezer, W. R.", "given_names": "W. R.", "surname": "Niezer", "position": "Second Gaoler, Secondee ”", "department": "Gaols - Gold Coast", "salary_min": 50, "salary_max": 50},
    {"name": "J. Baffoe", "canonical_name": "Baffoe, J.", "given_names": "J.", "surname": "Baffoe", "position": "” Dixcove", "department": "Gaols - Gold Coast", "salary_min": 40, "salary_max": 40, "location": "Dixcove"},
    {"name": "James Van Dyke", "canonical_name": "Van Dyke, James", "given_names": "James", "surname": "Van Dyke", "position": "” Axim", "department": "Gaols - Gold Coast", "salary_min": 36, "salary_max": 36, "location": "Axim"},
    {"name": "J. J. McCormack", "canonical_name": "McCormack, J. J.", "given_names": "J. J.", "surname": "McCormack", "position": "” Quittah", "department": "Gaols - Gold Coast", "salary_min": 36, "salary_max": 36},
    {"name": "J. Lewis", "canonical_name": "Lewis, J.", "given_names": "J.", "surname": "Lewis", "position": "” Addah", "department": "Gaols - Gold Coast", "salary_min": 36, "salary_max": 36},
    {"name": "J. B. Cole", "canonical_name": "Cole, J. B.", "given_names": "J. B.", "surname": "Cole", "position": "”", "department": "Gaols - Gold Coast", "salary_min": 36, "salary_max": 36},
    {"name": "G. Owoo", "canonical_name": "Owoo, G.", "given_names": "G.", "surname": "Owoo", "position": "”", "department": "Gaols - Gold Coast", "salary_min": 36, "salary_max": 36}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()