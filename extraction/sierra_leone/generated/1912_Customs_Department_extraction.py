"""
Sierra Leone Colonial Office List 1912 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1912

OFFICIALS = [
    {"name": "A. P. Viret", "canonical_name": "Viret, A. P.", "given_names": "A. P.", "surname": "Viret", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "allowances": "100l. allowance in lieu of fees"},
    {"name": "A. S. Fraser", "canonical_name": "Fraser, A. S.", "given_names": "A. S.", "surname": "Fraser", "position": "Assistant Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 350, "salary_max": 400, "allowances": "50l. allowance in lieu of fees"},
    {"name": "T. M. Johnson", "canonical_name": "Johnson, T. M.", "given_names": "T. M.", "surname": "Johnson", "position": "First Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "V. E. Spaine", "canonical_name": "Spaine, V. E.", "given_names": "V. E.", "surname": "Spaine", "position": "Examining Officer, First Class", "department": "Customs Department - Sierra Leone", "salary_min": 150, "salary_max": 170},
    {"name": "T. A. Clemens", "canonical_name": "Clemens, T. A.", "given_names": "T. A.", "surname": "Clemens", "position": "Examining Officer, Ditto ditto Second Class", "department": "Customs Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "M. A. Smith", "canonical_name": "Smith, M. A.", "given_names": "M. A.", "surname": "Smith", "position": "Examining Officer, Ditto ditto Third Class", "department": "Customs Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "M. A. Lewis", "canonical_name": "Lewis, M. A.", "given_names": "M. A.", "surname": "Lewis", "position": "Clerk, Upper Section", "department": "Customs Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "Ditto ditto", "department": "Customs Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "A. R. Harris", "canonical_name": "Harris, A. R.", "given_names": "A. R.", "surname": "Harris", "position": "Ditto ditto", "department": "Customs Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "L. F. Campbell", "canonical_name": "Campbell, L. F.", "given_names": "L. F.", "surname": "Campbell", "position": "Supervisor", "department": "Customs Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "location": "Sherbro"},
    {"name": "P. H. George", "canonical_name": "George, P. H.", "given_names": "P. H.", "surname": "George", "position": "Chief Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 150, "salary_max": 170, "location": "Sherbro"},
    {"name": "T. D. Brown", "canonical_name": "Brown, T. D.", "given_names": "T. D.", "surname": "Brown", "position": "Examining Officer, Lower Section", "department": "Customs Department - Sierra Leone", "salary_min": 100, "salary_max": 120, "location": "Sherbro"},
    {"name": "A. C. A. Johnson", "canonical_name": "Johnson, A. C. A.", "given_names": "A. C. A.", "surname": "Johnson", "position": "Senior Outdoor Officer", "department": "Customs Department - Sierra Leone", "salary_min": 170, "salary_max": 200},
    {"name": "T. A. Davies", "canonical_name": "Davies, T. A.", "given_names": "T. A.", "surname": "Davies", "position": "Senior 1st Class Officer", "department": "Customs Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "F. Q. Martyn", "canonical_name": "Martyn, F. Q.", "given_names": "F. Q.", "surname": "Martyn", "position": "Preventive Officer", "department": "Customs Department - Sierra Leone", "salary_min": 100, "salary_max": 100}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()