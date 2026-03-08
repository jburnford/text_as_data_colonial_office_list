"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "B. H. T. Frere", "canonical_name": "Frere, B. H. T.", "given_names": "B. H. T.", "surname": "Frere", "position": "Chief Justice", "department": "Judicial Department - Gambia", "salary_min": 1000, "salary_max": 1000},
    {"name": "C. J. Griffin", "canonical_name": "Griffin, C. J.", "given_names": "C. J.", "surname": "Griffin", "position": "Attorney-General", "department": "Judicial Department - Gambia", "salary_min": 800, "salary_max": 800},
    {"name": "C. J. Edwards", "canonical_name": "Edwards, C. J.", "given_names": "C. J.", "surname": "Edwards", "position": "Clerk to the Attorney-General", "department": "Judicial Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. Discombe", "canonical_name": "Discombe, J.", "given_names": "J.", "surname": "Discombe", "position": "Registrar of the Supreme Court, &c.", "department": "Judicial Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "A. S. Prescott", "canonical_name": "Prescott, A. S.", "given_names": "A. S.", "surname": "Prescott", "position": "Assistant Registrar", "department": "Judicial Department - Gambia", "salary_min": 200, "salary_max": 300},
    {"name": "A. Dotto", "canonical_name": "Dotto, A.", "given_names": "A.", "surname": "Dotto", "position": "3rd Class Clerk", "department": "Judicial Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "E. Pizarello", "canonical_name": "Pizarello, E.", "given_names": "E.", "surname": "Pizarello", "position": "3rd Class Clerk", "department": "Judicial Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "W. P. Michelin", "canonical_name": "Michelin, W. P.", "given_names": "W. P.", "surname": "Michelin", "position": "Police Magistrate and Coroner", "department": "Judicial Department - Gambia", "salary_min": 500, "salary_max": 600, "allowances": "42l. for forage allowance"},
    {"name": "A. M. Requena", "canonical_name": "Requena, A. M.", "given_names": "A. M.", "surname": "Requena", "position": "Clerk to the Justices", "department": "Judicial Department - Gambia", "salary_min": 200, "salary_max": 300},
    {"name": "R. F. King", "canonical_name": "King, R. F.", "given_names": "R. F.", "surname": "King", "position": "Clerk in Police Magistrate's Office (2nd Class)", "department": "Judicial Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. Cochrane", "canonical_name": "Cochrane, J.", "given_names": "J.", "surname": "Cochrane", "position": "Chief of Police", "department": "Judicial Department - Gambia", "salary_min": 300, "salary_max": 400, "allowances": "quarters, and 42l. for horse allowance as Supervisor of Markets"},
    {"name": "E. P. Griffin", "canonical_name": "Griffin, E. P.", "given_names": "E. P.", "surname": "Griffin", "position": "Registrar of Births, &c.", "department": "Judicial Department - Gambia", "salary_min": 45, "salary_max": 45},
    {"name": "W. P. Michelin", "canonical_name": "Michelin, W. P.", "given_names": "W. P.", "surname": "Michelin", "position": "Inspector of Schools", "department": "Judicial Department - Gambia", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()