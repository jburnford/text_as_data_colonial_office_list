"""
Sierra Leone Colonial Office List 1927 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1927

OFFICIALS = [
    {"name": "Director, Assistant Commandant of Police", "canonical_name": "Director, Assistant Commandant of Police", "surname": "Director, Assistant Commandant of Police", "position": "Director, Assistant Commandant of Police", "department": "Prisons - Sierra Leone"},
    {"name": "R. S. Taylor", "canonical_name": "Taylor, R. S.", "given_names": "R. S.", "surname": "Taylor", "position": "Principal Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 900, "salary_max": 1000},
    {"name": "J. A. Young", "canonical_name": "Young, J. A.", "given_names": "J. A.", "surname": "Young", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 900, "honors": ["M.C."]},
    {"name": "A. W. H. Donaldson", "canonical_name": "Donaldson, A. W. H.", "given_names": "A. W. H.", "surname": "Donaldson", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 900, "honors": ["O.B.E."]},
    {"name": "L. V. Tebb", "canonical_name": "Tebb, L. V.", "given_names": "L. V.", "surname": "Tebb", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 900, "acting_status": "temporary"},
    {"name": "C. G. Timms", "canonical_name": "Timms, C. G.", "given_names": "C. G.", "surname": "Timms", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 900, "honors": ["M.C."]},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Medical Officer of Health", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 900},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Senior Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 800, "salary_max": 900},
    {"name": "H. M. O'Byrne", "canonical_name": "O'Byrne, H. M.", "given_names": "H. M.", "surname": "O'Byrne", "position": "Chief of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "C. V. Magill", "canonical_name": "Magill, C. V.", "given_names": "C. V.", "surname": "Magill", "position": "Director of Posts and Telegraphs", "department": "Posts and Telegraphs Department - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "G. G. Kellie", "canonical_name": "Kellie, G. G.", "given_names": "G. G.", "surname": "Kellie", "position": "Postal Assistant Director of Posts and Telegraphs", "department": "Posts and Telegraphs Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "G. Hill", "canonical_name": "Hill, G.", "given_names": "G.", "surname": "Hill", "position": "Assistant Director of Posts and Telegraphs", "department": "Posts and Telegraphs Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "G. B. Jones", "canonical_name": "Jones, G. B.", "given_names": "G. B.", "surname": "Jones", "position": "Electrical Mechanic", "department": "Posts and Telegraphs Department - Sierra Leone", "salary_min": 350, "salary_max": 450}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()