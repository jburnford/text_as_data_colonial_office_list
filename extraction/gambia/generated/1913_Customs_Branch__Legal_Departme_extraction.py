"""
Gambia Colonial Office List 1913 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1913

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Clerk and Cashier", "department": "Customs Branch - Gambia", "salary_min": 175, "salary_max": 200, "allowances": "50l. personal"},
    {"name": "J. A. Nui-Gomez", "canonical_name": "Nui-Gomez, J. A.", "given_names": "J. A.", "surname": "Nui-Gomez", "position": "First Clerk", "department": "Customs Branch - Gambia", "salary_min": 100, "salary_max": 125, "allowances": "12l. as Magazine Keeper"},
    {"name": "J. Gabbidon", "canonical_name": "Gabbidon, J.", "given_names": "J.", "surname": "Gabbidon", "position": "Second Clerk", "department": "Customs Branch - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "S. W. Davies", "canonical_name": "Davies, S. W.", "given_names": "S. W.", "surname": "Davies", "position": "Second Clerk", "department": "Customs Branch - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Second Clerk", "department": "Customs Branch - Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "S. Jobe", "canonical_name": "Jobe, S.", "given_names": "S.", "surname": "Jobe", "position": "Third Clerk", "department": "Customs Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "S. F. Leigh", "canonical_name": "Leigh, S. F.", "given_names": "S. F.", "surname": "Leigh", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs Branch - Gambia", "salary_min": 175, "salary_max": 200},
    {"name": "J. K. King", "canonical_name": "King, J. K.", "given_names": "J. K.", "surname": "King", "position": "Chief Landing Waiter and Locker", "department": "Customs Branch - Gambia", "salary_min": 125, "salary_max": 150},
    {"name": "J. B. Davies", "canonical_name": "Davies, J. B.", "given_names": "J. B.", "surname": "Davies", "position": "First Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "First Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "First Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "Second Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "T. R. King", "canonical_name": "King, T. R.", "given_names": "T. R.", "surname": "King", "position": "Second Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "C. Porquet", "canonical_name": "Porquet, C.", "given_names": "C.", "surname": "Porquet", "position": "Third Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "S. Senghore", "canonical_name": "Senghore, S.", "given_names": "S.", "surname": "Senghore", "position": "Third Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Third Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Third Class Landing Waiter", "department": "Customs Branch - Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "Hon. E. A. Hume", "canonical_name": "Hume, E. A.", "given_names": "E. A.", "surname": "Hume", "position": "Chief Magistrate", "department": "Legal Department - Gambia", "salary_min": 750, "salary_max": 750, "honors": ["Hon."]},
    {"name": "Hon.", "canonical_name": "Hon.,", "surname": "Hon.", "position": "Legal Adviser", "department": "Legal Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Police Magistrate", "department": "Legal Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Clerk of Courts", "department": "Legal Department - Gambia", "salary_min": 150, "salary_max": 200},
    {"name": "J. Finden Dailey", "canonical_name": "Dailey, J. Finden", "given_names": "J. Finden", "surname": "Dailey", "position": "Clerk to Legal Assistant", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk to Legal Assistant", "department": "Legal Department - Gambia", "salary_min": 24, "salary_max": 30},
    {"name": "J. R. E. Lusack", "canonical_name": "Lusack, J. R. E.", "given_names": "J. R. E.", "surname": "Lusack", "position": "Interpreter", "department": "Legal Department - Gambia", "salary_min": 80, "salary_max": 100},
    {"name": "N. J. Allen", "canonical_name": "Allen, N. J.", "given_names": "N. J.", "surname": "Allen", "position": "Beadle and Bailiff", "department": "Legal Department - Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "C. Creig", "canonical_name": "Creig, C.", "given_names": "C.", "surname": "Creig", "position": "Sheriff", "department": "Legal Department - Gambia"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()