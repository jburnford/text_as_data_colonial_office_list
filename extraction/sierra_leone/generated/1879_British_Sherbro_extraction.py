"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "T. A. Wall", "canonical_name": "Wall, T. A.", "given_names": "T. A.", "surname": "Wall", "position": "Commandant and Coroner", "department": "Civil Establishment - Sierra Leone", "salary_min": 520, "salary_max": 520},
    {"name": "Dr. Jarrett", "canonical_name": "Jarrett, Dr.", "given_names": "Dr.", "surname": "Jarrett", "position": "Acting Assistant Colonial Surgeon", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 350, "acting_status": "Acting", "allowances": "travelling allowance, 45l. 12s. 6d."},
    {"name": "T. A. Wall", "canonical_name": "Wall, T. A.", "given_names": "T. A.", "surname": "Wall", "position": "Deputy Collector of Customs", "department": "Customs - Sierra Leone", "acting_status": "Acting"},
    {"name": "W. M. Laborde", "canonical_name": "Laborde, W. M.", "given_names": "W. M.", "surname": "Laborde", "position": "Acting Clerk of Customs", "department": "Customs - Sierra Leone", "salary_min": 100, "salary_max": 100, "acting_status": "Acting"},
    {"name": "Frederick J. Davis", "canonical_name": "Davis, Frederick J.", "given_names": "Frederick J.", "surname": "Davis", "position": "1st Tide Waiter", "department": "Customs - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "F. A. Jones", "canonical_name": "Jones, F. A.", "given_names": "F. A.", "surname": "Jones", "position": "2nd Tide Waiter", "department": "Customs - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "M. E. Betts", "canonical_name": "Betts, M. E.", "given_names": "M. E.", "surname": "Betts", "position": "Sub-Inspector of Police", "department": "Police - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "S. B. Caulker", "canonical_name": "Caulker, S. B.", "given_names": "S. B.", "surname": "Caulker", "position": "Sub-Collector of Customs", "department": "Customs - Sierra Leone", "salary_min": 200, "salary_max": 200, "allowances": "rent 50l.", "location": "Isle de Los"},
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Harbour Master and Superintendent of Lighthouse, Deputy", "department": "Civil Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "Mohammed Sannasi", "canonical_name": "Sannasi, Mohammed", "given_names": "Mohammed", "surname": "Sannasi", "position": "Arabic Writer", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Thos. G. Lawson", "canonical_name": "Lawson, Thos. G.", "given_names": "Thos. G.", "surname": "Lawson", "position": "Government Messenger and Interpreter", "department": "Civil Establishment - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "S. H. John", "canonical_name": "John, S. H.", "given_names": "S. H.", "surname": "John", "position": "Acting Government Printer", "department": "Printing - Sierra Leone", "salary_min": 60, "salary_max": 60, "acting_status": "Acting"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()