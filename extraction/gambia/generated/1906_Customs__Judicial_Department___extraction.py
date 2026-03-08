"""
Gambia Colonial Office List 1906 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1906

OFFICIALS = [
    {"name": "T. E. Peirce", "canonical_name": "Peirce, T. E.", "given_names": "T. E.", "surname": "Peirce", "position": "Collector of Customs", "department": "Customs - Gambia", "salary_min": 400, "salary_max": 500, "duty_allowance": 60},
    {"name": "S. J. Auber", "canonical_name": "Auber, S. J.", "given_names": "S. J.", "surname": "Auber", "position": "Chief Clerk and Cashier", "department": "Customs - Gambia", "salary_min": 175, "salary_max": 200, "allowances": "20l. personal"},
    {"name": "J. A. Gomez", "canonical_name": "Gomez, J. A.", "given_names": "J. A.", "surname": "Gomez", "position": "Second Clerk", "department": "Customs - Gambia", "salary_min": 50, "salary_max": 65, "allowances": "12l. as Magazine Keeper"},
    {"name": "L. M. Joof", "canonical_name": "Joof, L. M.", "given_names": "L. M.", "surname": "Joof", "position": "Third Clerk", "department": "Customs - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "S. F. Leigh", "canonical_name": "Leigh, S. F.", "given_names": "S. F.", "surname": "Leigh", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs - Gambia", "salary_min": 175, "salary_max": 200},
    {"name": "J. C. Chapman", "canonical_name": "Chapman, J. C.", "given_names": "J. C.", "surname": "Chapman", "position": "Chief Landing Waiter and Locker", "department": "Customs - Gambia", "salary_min": 125, "salary_max": 150},
    {"name": "J. E. King", "canonical_name": "King, J. E.", "given_names": "J. E.", "surname": "King", "position": "First Class Landing Waiter", "department": "Customs - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "J. T. Monday", "canonical_name": "Monday, J. T.", "given_names": "J. T.", "surname": "Monday", "position": "First Class Landing Waiter", "department": "Customs - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "T. B. Wright", "canonical_name": "Wright, T. B.", "given_names": "T. B.", "surname": "Wright", "position": "Second Class Landing Waiter", "department": "Customs - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "S. C. Richards", "canonical_name": "Richards, S. C.", "given_names": "S. C.", "surname": "Richards", "position": "Second Class Landing Waiter", "department": "Customs - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "W. Topp", "canonical_name": "Topp, W.", "given_names": "W.", "surname": "Topp", "position": "Third Class Landing Waiter", "department": "Customs - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "D. D. Peters", "canonical_name": "Peters, D. D.", "given_names": "D. D.", "surname": "Peters", "position": "Third Class Landing Waiter", "department": "Customs - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "A. D. Russell", "canonical_name": "Russell, A. D.", "given_names": "A. D.", "surname": "Russell", "position": "Chief Magistrate", "department": "Judicial Department - Gambia", "salary_min": 750, "salary_max": 750, "qualifications": ["M.A.", "LL.B."]},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Judicial Department - Gambia", "salary_min": 100, "salary_max": 150},
    {"name": "F. M. Fye", "canonical_name": "Fye, F. M.", "given_names": "F. M.", "surname": "Fye", "position": "Interpreter", "department": "Judicial Department - Gambia", "salary_min": 60, "salary_max": 60},
    {"name": "Joseph Brown", "canonical_name": "Brown, Joseph", "given_names": "Joseph", "surname": "Brown", "position": "Sheriff", "department": "Judicial Department - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Beadle and Bailiff", "department": "Judicial Department - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "H. L. Prvce", "canonical_name": "Prvce, H. L.", "given_names": "H. L.", "surname": "Prvce", "position": "Travelling Commissioner, First Class", "department": "Protectorate - Gambia", "salary_min": 500, "salary_max": 500},
    {"name": "G. H. Sangster", "canonical_name": "Sangster, G. H.", "given_names": "G. H.", "surname": "Sangster", "position": "Travelling Commissioner, Second Class", "department": "Protectorate - Gambia", "salary_min": 400, "salary_max": 400},
    {"name": "W. B. Stanley", "canonical_name": "Stanley, W. B.", "given_names": "W. B.", "surname": "Stanley", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"},
    {"name": "J. K. McCallum", "canonical_name": "McCallum, J. K.", "given_names": "J. K.", "surname": "McCallum", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"},
    {"name": "H. F. Sproston", "canonical_name": "Sproston, H. F.", "given_names": "H. F.", "surname": "Sproston", "position": "Travelling Commissioner, Third Class", "department": "Protectorate - Gambia", "salary_min": 300, "salary_max": 300, "per_diem": "10s. per diem"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()