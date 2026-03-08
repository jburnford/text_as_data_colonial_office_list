"""
Sierra Leone Colonial Office List 1883 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1883

OFFICIALS = [
    {"name": "The Deputy Harbour Master", "canonical_name": "Deputy Harbour Master, The", "surname": "Deputy Harbour Master", "position": "Superintendent", "department": "Lighthouse - Sierra Leone", "acting_status": "Acting"},
    {"name": "Lighthouse Keeper", "canonical_name": "Lighthouse Keeper, ", "surname": "Lighthouse Keeper", "position": "Lighthouse Keeper", "department": "Lighthouse - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "Assistant ditto", "canonical_name": "Assistant ditto, ", "surname": "Assistant ditto", "position": "Assistant Lighthouse Keeper", "department": "Lighthouse - Sierra Leone", "salary_min": 31.5, "salary_max": 31.5},
    {"name": "J. C. Gore", "canonical_name": "Gore, J. C.", "given_names": "J. C.", "surname": "Gore", "position": "Auditor-General of W. Africa Settlements", "department": "Audit Office - Sierra Leone", "salary_min": 600, "salary_max": 600},
    {"name": "G. W. Cole", "canonical_name": "Cole, G. W.", "given_names": "G. W.", "surname": "Cole", "position": "Clerk to ditto", "department": "Audit Office - Sierra Leone", "salary_min": 125, "salary_max": 125},
    {"name": "F. F. Pinkett", "canonical_name": "Pinkett, F. F.", "given_names": "F. F.", "surname": "Pinkett", "position": "Chief Justice and Judge of the Vice-Admiralty Court, and Legal Adviser", "department": "Judicial Establishment - Sierra Leone", "salary_min": 1500, "salary_max": 1500},
    {"name": "I. H. Campbell", "canonical_name": "Campbell, I. H.", "given_names": "I. H.", "surname": "Campbell", "position": "Clerk to ditto", "department": "Judicial Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "A. M. Tarleton", "canonical_name": "Tarleton, A. M.", "given_names": "A. M.", "surname": "Tarleton", "position": "Queen's Advocate and Registrar-General", "department": "Judicial Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "62l. 10s. from Gambia"},
    {"name": "Daniel Carrol", "canonical_name": "Carrol, Daniel", "given_names": "Daniel", "surname": "Carrol", "position": "Master and Registrar of the Supreme Court", "department": "Judicial Establishment - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "F. A. Jones", "canonical_name": "Jones, F. A.", "given_names": "F. A.", "surname": "Jones", "position": "Clerk to ditto", "department": "Judicial Establishment - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "R. M. Sheppard", "canonical_name": "Sheppard, R. M.", "given_names": "R. M.", "surname": "Sheppard", "position": "Clerk to ditto", "department": "Judicial Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "John Meheux", "canonical_name": "Meheux, John", "given_names": "John", "surname": "Meheux", "position": "Sheriff and Provost-Marshal", "department": "Judicial Establishment - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Registrar of Vice-Admiralty Court", "department": "Judicial Establishment - Sierra Leone"},
    {"name": "John Meheux", "canonical_name": "Meheux, John", "given_names": "John", "surname": "Meheux", "position": "Marshal of ditto", "department": "Judicial Establishment - Sierra Leone"},
    {"name": "E. Adolphus", "canonical_name": "Adolphus, E.", "given_names": "E.", "surname": "Adolphus", "position": "Coroner", "department": "Judicial Establishment - Sierra Leone", "salary_min": 60, "salary_max": 60, "location": "Freetown"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()