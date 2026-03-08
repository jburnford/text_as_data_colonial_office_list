"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "Sir P. C. Smyly", "canonical_name": "Smyly, P. C.", "given_names": "P. C.", "surname": "Smyly", "position": "Chief Justice", "department": "Legal Department - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240, "honors": ["Kt."], "qualifications": ["LL.D."]},
    {"name": "J. C. Johnson", "canonical_name": "Johnson, J. C.", "given_names": "J. C.", "surname": "Johnson", "position": "Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "D. F. Wilbraham", "canonical_name": "Wilbraham, D. F.", "given_names": "D. F.", "surname": "Wilbraham", "position": "Attorney-General", "department": "Legal Department - Sierra Leone", "salary_min": 700, "salary_max": 700, "duty_allowance": 140},
    {"name": "W. R. Townsend", "canonical_name": "Townsend, W. R.", "given_names": "W. R.", "surname": "Townsend", "position": "Puisne Judge (paid as Circuit Judge)", "department": "Legal Department - Sierra Leone", "salary_min": 800, "salary_max": 800, "duty_allowance": 100},
    {"name": "F. A. Van der Meulen", "canonical_name": "Van der Meulen, F. A.", "given_names": "F. A.", "surname": "Van der Meulen", "position": "Solicitor-General", "department": "Legal Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Chief Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "J. N. P. Nicol", "canonical_name": "Nicol, J. N. P.", "given_names": "J. N. P.", "surname": "Nicol", "position": "2nd Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "S. G. Randall", "canonical_name": "Randall, S. G.", "given_names": "S. G.", "surname": "Randall", "position": "3rd Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. O. Johnson", "canonical_name": "Johnson, J. O.", "given_names": "J. O.", "surname": "Johnson", "position": "4th Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "A. T. A. Beckley", "canonical_name": "Beckley, A. T. A.", "given_names": "A. T. A.", "surname": "Beckley", "position": "Assistant Master, Circuit Court", "department": "Legal Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "K. J. Beatty", "canonical_name": "Beatty, K. J.", "given_names": "K. J.", "surname": "Beatty", "position": "Master of Supreme Court, Registrar-General, and Police Magistrate", "department": "Legal Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "F. Bucknor", "canonical_name": "Bucknor, F.", "given_names": "F.", "surname": "Bucknor", "position": "Chief Clerk Registrar-General's Office", "department": "Legal Department - Sierra Leone", "salary_min": 80, "salary_max": 100},
    {"name": "A. N. Strong", "canonical_name": "Strong, A. N.", "given_names": "A. N.", "surname": "Strong", "position": "2nd Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. N. Taylor", "canonical_name": "Taylor, J. N.", "given_names": "J. N.", "surname": "Taylor", "position": "3rd Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. S. C. Hanson", "canonical_name": "Hanson, E. S. C.", "given_names": "E. S. C.", "surname": "Hanson", "position": "4th Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "S. A. Metzger", "canonical_name": "Metzger, S. A.", "given_names": "S. A.", "surname": "Metzger", "position": "Deputy Master of Supreme Court", "department": "Legal Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "E. O. Farmer", "canonical_name": "Farmer, E. O.", "given_names": "E. O.", "surname": "Farmer", "position": "2nd Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "K. J. Beatty", "canonical_name": "Beatty, K. J.", "given_names": "K. J.", "surname": "Beatty", "position": "Police Magistrate and Coroner", "department": "Legal Department - Sierra Leone"},
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Sheriff and Provost-Marshal", "department": "Legal Department - Sierra Leone"},
    {"name": "S. A. Metzger", "canonical_name": "Metzger, S. A.", "given_names": "S. A.", "surname": "Metzger", "position": "Under Sheriff", "department": "Legal Department - Sierra Leone", "salary_min": 65, "salary_max": 65},
    {"name": "W. S. Grant", "canonical_name": "Grant, W. S.", "given_names": "W. S.", "surname": "Grant", "position": "Clerk to Sheriff and Senior Bailiff", "department": "Legal Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Clerk, Police Court", "department": "Legal Department - Sierra Leone", "salary_min": 120, "salary_max": 180},
    {"name": "J. W. Davies", "canonical_name": "Davies, J. W.", "given_names": "J. W.", "surname": "Davies", "position": "2nd Clerk", "department": "Legal Department - Sierra Leone", "salary_min": 50, "salary_max": 70},
    {"name": "W. A. Cole", "canonical_name": "Cole, W. A.", "given_names": "W. A.", "surname": "Cole", "position": "Bailiff", "department": "Legal Department - Sierra Leone", "salary_min": 50, "salary_max": 60, "allowances": "15l. personal"},
    {"name": "S. A. Metzger", "canonical_name": "Metzger, S. A.", "given_names": "S. A.", "surname": "Metzger", "position": "Curator of Intestate Estates", "department": "Legal Department - Sierra Leone", "acting_status": "Acting"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()