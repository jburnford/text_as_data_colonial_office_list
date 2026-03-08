"""
Gambia Colonial Office List 1899 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1899

OFFICIALS = [
    {"name": "S. H. Gatty", "canonical_name": "Gatty, S. H.", "given_names": "S. H.", "surname": "Gatty", "position": "Chief Justice", "department": "Judicial Department - Gambia", "salary_min": 1083, "salary_max": 1083},
    {"name": "A. W. Fawkes", "canonical_name": "Fawkes, A. W.", "given_names": "A. W.", "surname": "Fawkes", "position": "Attorney-General", "department": "Judicial Department - Gambia", "salary_min": 796, "salary_max": 796, "qualifications": ["Q.C."]},
    {"name": "A. Bosano", "canonical_name": "Bosano, A.", "given_names": "A.", "surname": "Bosano", "position": "Clerk to the Attorney-General", "department": "Judicial Department - Gambia", "salary_min": 208, "salary_max": 208},
    {"name": "E. M. Hutton", "canonical_name": "Hutton, E. M.", "given_names": "E. M.", "surname": "Hutton", "position": "Registrar of the Supreme Court, &c.", "department": "Judicial Department - Gambia", "salary_min": 500, "salary_max": 500},
    {"name": "A. Sanchez", "canonical_name": "Sanchez, A.", "given_names": "A.", "surname": "Sanchez", "position": "Assistant Registrar", "department": "Judicial Department - Gambia", "salary_min": 250, "salary_max": 250},
    {"name": "T. J. Vecchio", "canonical_name": "Vecchio, T. J.", "given_names": "T. J.", "surname": "Vecchio", "position": "Marshal and Interpreter Supreme Court", "department": "Judicial Department - Gambia", "salary_min": 118, "salary_max": 118},
    {"name": "J. Discombe", "canonical_name": "Discombe, J.", "given_names": "J.", "surname": "Discombe", "position": "Clerks in the Supreme Court (2nd class supernumerary)", "department": "Judicial Department - Gambia", "salary_min": 124, "salary_max": 124},
    {"name": "A. S. Prescott", "canonical_name": "Prescott, A. S.", "given_names": "A. S.", "surname": "Prescott", "position": "supplementary clerk", "department": "Judicial Department - Gambia", "salary_min": 80, "salary_max": 80},
    {"name": "A. M. Coll", "canonical_name": "Coll, A. M.", "given_names": "A. M.", "surname": "Coll", "position": "Police Magistrate", "department": "Judicial Department - Gambia", "salary_min": 500, "salary_max": 500, "allowances": "42l. for forage allowance, and 50l. as Inspector of Schools"},
    {"name": "A. M. Requena", "canonical_name": "Requena, A. M.", "given_names": "A. M.", "surname": "Requena", "position": "Clerk to Magistrates", "department": "Judicial Department - Gambia", "salary_min": 150, "salary_max": 150, "allowances": "20l. allowance"},
    {"name": "R. F. King", "canonical_name": "King, R. F.", "given_names": "R. F.", "surname": "King", "position": "Clerk in Police Magistrate's Office (2nd class)", "department": "Judicial Department - Gambia", "salary_min": 132, "salary_max": 132},
    {"name": "J. Bennett", "canonical_name": "Bennett, J.", "given_names": "J.", "surname": "Bennett", "position": "Chief of Police", "department": "Judicial Department - Gambia", "salary_min": 300, "salary_max": 375, "allowances": "42l. for horse allowance as Supervisor of Markets"},
    {"name": "G. F. Cornwell", "canonical_name": "Cornwell, G. F.", "given_names": "G. F.", "surname": "Cornwell", "position": "Coroner", "department": "Judicial Department - Gambia", "salary_min": 50, "salary_max": 50, "qualifications": ["Q.C."]},
    {"name": "J. Porral", "canonical_name": "Porral, J.", "given_names": "J.", "surname": "Porral", "position": "Registrar of Births, &c.", "department": "Judicial Department - Gambia", "salary_min": 42, "salary_max": 42}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()