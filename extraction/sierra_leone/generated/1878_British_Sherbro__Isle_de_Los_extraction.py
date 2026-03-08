"""
Sierra Leone Colonial Office List 1878 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1878

OFFICIALS = [
    {"name": "T. A. Wall", "canonical_name": "Wall, T. A.", "given_names": "T. A.", "surname": "Wall", "position": "Commandant", "department": "Civil Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "Clerk to ditto", "canonical_name": "Clerk to ditto, .", "surname": "Clerk to ditto", "position": "Clerk to ditto", "department": "Civil Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "Dr. Jarrett", "canonical_name": "Jarrett, Dr.", "given_names": "Dr.", "surname": "Jarrett", "position": "Assistant Colonial Surgeon", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 350, "allowances": "travelling allowance, 45l. 12s. 6d."},
    {"name": "F. G. Thomas", "canonical_name": "Thomas, F. G.", "given_names": "F. G.", "surname": "Thomas", "position": "Compounder and Dresser in Hospital", "department": "Medical - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "T. A. Wall", "canonical_name": "Wall, T. A.", "given_names": "T. A.", "surname": "Wall", "position": "Deputy Collector of Customs and Coroner", "department": "Customs - Sierra Leone", "salary_min": 370, "salary_max": 370, "allowances": "50l. rent", "acting_status": "Acting"},
    {"name": "B. G. Porter", "canonical_name": "Porter, B. G.", "given_names": "B. G.", "surname": "Porter", "position": "Clerk of Customs", "department": "Customs - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "J. G. Sawyer", "canonical_name": "Sawyer, J. G.", "given_names": "J. G.", "surname": "Sawyer", "position": "1st Tide Waiter", "department": "Customs - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "F. A. Jones", "canonical_name": "Jones, F. A.", "given_names": "F. A.", "surname": "Jones", "position": "2nd Tide Waiter", "department": "Customs - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "M. E. Betts", "canonical_name": "Betts, M. E.", "given_names": "M. E.", "surname": "Betts", "position": "Sub-Inspector of Police", "department": "Police - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "S. B. Caulker", "canonical_name": "Caulker, S. B.", "given_names": "S. B.", "surname": "Caulker", "position": "Sub-Collector of Customs", "department": "Customs - Sierra Leone", "salary_min": 200, "salary_max": 200, "allowances": "Rent 50l."},
    {"name": "J. G. Smith", "canonical_name": "Smith, J. G.", "given_names": "J. G.", "surname": "Smith", "position": "Clerk to ditto", "department": "Civil Establishment - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "Mohammed Sannasi", "canonical_name": "Sannasi, Mohammed", "given_names": "Mohammed", "surname": "Sannasi", "position": "Arabic Writer", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Thos. G. Lawson", "canonical_name": "Lawson, Thos. G.", "given_names": "Thos. G.", "surname": "Lawson", "position": "Government Messenger and Interpreter", "department": "Civil Establishment - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "G. M. Macaulay", "canonical_name": "Macaulay, G. M.", "given_names": "G. M.", "surname": "Macaulay", "position": "Assistant Interpreter and Protector of Strangers", "department": "Civil Establishment - Sierra Leone", "salary_min": 80, "salary_max": 80}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()