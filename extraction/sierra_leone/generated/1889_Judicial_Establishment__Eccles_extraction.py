"""
Sierra Leone Colonial Office List 1889 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1889

OFFICIALS = [
    {"name": "W. H. Quayle Jones", "canonical_name": "Jones, W. H. Quayle", "given_names": "W. H.", "surname": "Jones", "position": "Chief Justice and Judge of the Vice-Admiralty Court", "department": "Judicial - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "S. T. Nicol", "canonical_name": "Nicol, S. T.", "given_names": "S. T.", "surname": "Nicol", "position": "Clerk to ditto", "department": "Judicial - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "J. K. Donaldson", "canonical_name": "Donaldson, J. K.", "given_names": "J. K.", "surname": "Donaldson", "position": "Queen's Advocate and Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 750, "salary_max": 750},
    {"name": "W. A. Valantin", "canonical_name": "Valantin, W. A.", "given_names": "W. A.", "surname": "Valantin", "position": "Clerk to ditto", "department": "Judicial - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "Daniel Carrol", "canonical_name": "Carrol, Daniel", "given_names": "Daniel", "surname": "Carrol", "position": "Master and Registrar of the Supreme Court", "department": "Judicial - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "F. A. Jones", "canonical_name": "Jones, F. A.", "given_names": "F. A.", "surname": "Jones", "position": "Clerks to ditto", "department": "Judicial - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "T. A. Wilhelm", "canonical_name": "Wilhelm, T. A.", "given_names": "T. A.", "surname": "Wilhelm", "position": "Clerks to ditto", "department": "Judicial - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "W. S. Saunders", "canonical_name": "Saunders, W. S.", "given_names": "W. S.", "surname": "Saunders", "position": "Clerks to ditto", "department": "Judicial - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Daniel Carrol", "canonical_name": "Carrol, Daniel", "given_names": "Daniel", "surname": "Carrol", "position": "Sheriff and Provost-Marshal", "department": "Judicial - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "S. Metzger", "canonical_name": "Metzger, S.", "given_names": "S.", "surname": "Metzger", "position": "Sheriff's Clerk", "department": "Judicial - Sierra Leone", "salary_min": 43, "salary_max": 43},
    {"name": "E. Adolphus", "canonical_name": "Adolphus, E.", "given_names": "E.", "surname": "Adolphus", "position": "Coroner, Freedom", "department": "Judicial - Sierra Leone", "location": "Freedom", "salary_min": 60, "salary_max": 60},
    {"name": "Edwin Adolphus", "canonical_name": "Adolphus, Edwin", "given_names": "Edwin", "surname": "Adolphus", "position": "Police Magistrate", "department": "Judicial - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "M. Quin", "canonical_name": "Quin, M.", "given_names": "M.", "surname": "Quin", "position": "Clerk of Police", "department": "Judicial - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "O. J. Robinson", "canonical_name": "Robinson, O. J.", "given_names": "O. J.", "surname": "Robinson", "position": "Assistant Clerk", "department": "Judicial - Sierra Leone", "salary_min": 36, "salary_max": 36},
    {"name": "W. G. Isaacs", "canonical_name": "Isaacs, W. G.", "given_names": "W. G.", "surname": "Isaacs", "position": "Bailiff", "department": "Judicial - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "T. N. Cole", "canonical_name": "Cole, T. N.", "given_names": "T. N.", "surname": "Cole", "position": "Assistant ditto", "department": "Judicial - Sierra Leone", "salary_min": 36, "salary_max": 36},
    {"name": "Right Rev. E. G. Ingham", "canonical_name": "Ingham, E. G.", "given_names": "E. G.", "surname": "Ingham", "position": "Bishop of Sierra Leone", "department": "Ecclesiastical - Sierra Leone", "qualifications": ["D.D."]},
    {"name": "Rev. J. E Taylor", "canonical_name": "Taylor, J. E", "given_names": "J. E", "surname": "Taylor", "position": "Assistant Chaplain", "department": "Ecclesiastical - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "fees"},
    {"name": "V. King", "canonical_name": "King, V.", "given_names": "V.", "surname": "King", "position": "Organist", "department": "Ecclesiastical - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "Clerk", "department": "Ecclesiastical - Sierra Leone", "salary_min": 25, "salary_max": 25}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()