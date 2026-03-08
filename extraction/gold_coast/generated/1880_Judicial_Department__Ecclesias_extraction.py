"""
Gold Coast Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1880

OFFICIALS = [
    {"name": "James Marshall", "canonical_name": "Marshall, James", "given_names": "James", "surname": "Marshall",
     "position": "Chief Justice", "department": "Judicial Department - Gold Coast", "salary_min": 1500, "salary_max": 1500,
     "allowances": "Free quarters."},
    {"name": "T. W. Jackson", "canonical_name": "Jackson, T. W.", "given_names": "T. W.", "surname": "Jackson",
     "position": "Puisne Judge (Western Province)", "department": "Judicial Department - Gold Coast", "salary_min": 900, "salary_max": 900,
     "allowances": "\" "},
    {"name": "W. Thompson", "canonical_name": "Thompson, W.", "given_names": "W.", "surname": "Thompson",
     "position": "Registrar (Western Province)", "department": "Judicial Department - Gold Coast", "salary_min": 250, "salary_max": 250,
     "allowances": "\" "},
    {"name": "Thomas Hughes", "canonical_name": "Hughes, Thomas", "given_names": "Thomas", "surname": "Hughes",
     "position": "Deputy Registrar", "department": "Judicial Department - Gold Coast", "salary_min": 120, "salary_max": 120},
    {"name": "A. W. Thompson", "canonical_name": "Thompson, A. W.", "given_names": "A. W.", "surname": "Thompson",
     "position": "Deputy Registrar", "department": "Judicial Department - Gold Coast", "salary_min": 120, "salary_max": 120},
    {"name": "J. F. Thompson", "canonical_name": "Thompson, J. F.", "given_names": "J. F.", "surname": "Thompson",
     "position": "Deputy Registrar", "department": "Judicial Department - Gold Coast", "salary_min": 60, "salary_max": 60,
     "location": "Quitta"},
    {"name": "W. M. Addo", "canonical_name": "Addo, W. M.", "given_names": "W. M.", "surname": "Addo",
     "position": "Deputy Registrar", "department": "Judicial Department - Gold Coast", "salary_min": 60, "salary_max": 60,
     "location": "Accra"},
    {"name": "Jonathan Palmer", "canonical_name": "Palmer, Jonathan", "given_names": "Jonathan", "surname": "Palmer",
     "position": "Interpreter and Taxing Master", "department": "Judicial Department - Gold Coast", "salary_min": 75, "salary_max": 75},
    {"name": "John Williams", "canonical_name": "Williams, John", "given_names": "John", "surname": "Williams",
     "position": "Messenger and Caretaker", "department": "Judicial Department - Gold Coast", "salary_min": 20, "salary_max": 20},
    {"name": "Thomas Woodcock", "canonical_name": "Woodcock, Thomas", "given_names": "Thomas", "surname": "Woodcock",
     "position": "Queen’s Advocate", "department": "Judicial Department - Gold Coast", "salary_min": 1000, "salary_max": 1000,
     "allowances": "Free quarters & private practice"},
    {"name": "W. Z. Coker", "canonical_name": "Coker, W. Z.", "given_names": "W. Z.", "surname": "Coker",
     "position": "Clerk", "department": "Judicial Department - Gold Coast", "salary_min": 60, "salary_max": 60},
    {"name": "Rev. T. Maxwell", "canonical_name": "Maxwell, T.", "given_names": "T.", "surname": "Maxwell",
     "position": "Colonial Chaplain", "department": "Ecclesiastical Department - Gold Coast", "salary_min": 440, "salary_max": 440},
    {"name": "James Classpeter", "canonical_name": "Classpeter, James", "given_names": "James", "surname": "Classpeter",
     "position": "Sexton", "department": "Ecclesiastical Department - Gold Coast", "salary_min": 18, "salary_max": 18},
    {"name": "T. E. Duncan", "canonical_name": "Duncan, T. E.", "given_names": "T. E.", "surname": "Duncan",
     "position": "Organist", "department": "Ecclesiastical Department - Gold Coast", "salary_min": 20, "salary_max": 20,
     "acting_status": "acting"},
    {"name": "T. O. Newman", "canonical_name": "Newman, T. O.", "given_names": "T. O.", "surname": "Newman",
     "position": "Schoolmaster", "department": "Educational - Gold Coast", "salary_min": 100, "salary_max": 100},
    {"name": "J. A. Wulff", "canonical_name": "Wulff, J. A.", "given_names": "J. A.", "surname": "Wulff",
     "position": "Schoolmaster", "department": "Educational - Gold Coast", "salary_min": 100, "salary_max": 100,
     "location": "Accra"},
    {"name": "Thomas Duncan", "canonical_name": "Duncan, Thomas", "given_names": "Thomas", "surname": "Duncan",
     "position": "Schoolmistress", "department": "Educational - Gold Coast", "salary_min": 12, "salary_max": 12},
    {"name": "Mrs. S. A. Johnson", "canonical_name": "Johnson, S. A.", "given_names": "S. A.", "surname": "Johnson",
     "position": "Schoolmistress", "department": "Educational - Gold Coast", "salary_min": 72, "salary_max": 72,
     "location": "Accra"},
    {"name": "Elizabeth Brew", "canonical_name": "Brew, Elizabeth", "given_names": "Elizabeth", "surname": "Brew",
     "position": "Assistant Schoolmistress", "department": "Educational - Gold Coast", "salary_min": 72, "salary_max": 72},
    {"name": "Rose Miller", "canonical_name": "Miller, Rose", "given_names": "Rose", "surname": "Miller",
     "position": "Assistant Schoolmistress", "department": "Educational - Gold Coast", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()