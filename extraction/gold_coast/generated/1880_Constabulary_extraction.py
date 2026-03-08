"""
Gold Coast Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1880

OFFICIALS = [
    {"name": "Alexander Grant", "canonical_name": "Grant, Alexander", "given_names": "Alexander", "surname": "Grant",
     "position": "Inspector-General", "department": "Constabulary - Gold Coast", "salary_min": 600, "salary_max": 600, "allowances": "Free quarters"},
    {"name": "George Coulson Childs", "canonical_name": "Childs, George Coulson", "given_names": "George Coulson", "surname": "Childs",
     "position": "First Class Inspector", "department": "Constabulary - Gold Coast", "salary_min": 450, "salary_max": 450},
    {"name": "Cecil Dudley", "canonical_name": "Dudley, Cecil", "given_names": "Cecil", "surname": "Dudley",
     "position": "First Class Inspector", "department": "Constabulary - Gold Coast", "salary_min": 450, "salary_max": 450},
    {"name": "E. W. Newenham", "canonical_name": "Newenham, E. W.", "given_names": "E. W.", "surname": "Newenham",
     "position": "Adjutant and Musketry Instructor", "department": "Constabulary - Gold Coast", "salary_min": 400, "salary_max": 400},
    {"name": "H. H. Graves", "canonical_name": "Graves, H. H.", "given_names": "H. H.", "surname": "Graves",
     "position": "Artillery Inspector", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "L. A. Brydon", "canonical_name": "Brydon, L. A.", "given_names": "L. A.", "surname": "Brydon",
     "position": "Assistant Inspector", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "Louis Wyatt", "canonical_name": "Wyatt, Louis", "given_names": "Louis", "surname": "Wyatt",
     "position": "Assistant Inspector", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "E. W. G. Gardiner", "canonical_name": "Gardiner, E. W. G.", "given_names": "E. W. G.", "surname": "Gardiner",
     "position": "Assistant Inspector", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "C. de Freville Green", "canonical_name": "Green, C. de Freville", "given_names": "C. de Freville", "surname": "Green",
     "position": "Assistant Inspector", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "P. D. O'Brien", "canonical_name": "O'Brien, P. D.", "given_names": "P. D.", "surname": "O'Brien",
     "position": "Assistant Inspector", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "F. M. F. G. Hackett", "canonical_name": "Hackett, F. M. F. G.", "given_names": "F. M. F. G.", "surname": "Hackett",
     "position": "Assistant Inspector", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "J. R. H. Wilton", "canonical_name": "Wilton, J. R. H.", "given_names": "J. R. H.", "surname": "Wilton",
     "position": "Assistant Inspector", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "W. A. Cuscaden", "canonical_name": "Cuscaden, W. A.", "given_names": "W. A.", "surname": "Cuscaden",
     "position": "Assistant Inspector", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "R. H. B. Campbell", "canonical_name": "Campbell, R. H. B.", "given_names": "R. H. B.", "surname": "Campbell",
     "position": "Assistant Inspector", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "A. W. Forbes", "canonical_name": "Forbes, A. W.", "given_names": "A. W.", "surname": "Forbes",
     "position": "Pay and Quartermaster", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "E. G. Woolhouse", "canonical_name": "Woolhouse, E. G.", "given_names": "E. G.", "surname": "Woolhouse",
     "position": "Assistant to Pay and Quartermaster", "department": "Constabulary - Gold Coast", "salary_min": 350, "salary_max": 350},
    {"name": "Charles Wharton", "canonical_name": "Wharton, Charles", "given_names": "Charles", "surname": "Wharton",
     "position": "Assistant to Pay and Quartermaster", "department": "Constabulary - Gold Coast", "salary_min": 150, "salary_max": 150},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()