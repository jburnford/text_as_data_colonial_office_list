"""
Gambia Colonial Office List 1879 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1879

OFFICIALS = [
    {"name": "V. S. Gouldsbury", "canonical_name": "Gouldsbury, V. S.", "given_names": "V. S.", "surname": "Gouldsbury", "position": "Administrator", "department": "Civil Establishment - Gambia", "salary_min": 1300, "salary_max": 1300, "honors": ["C.M.G."], "military_rank": "Surgeon-Major"},
    {"name": "Robt. H. Syrett", "canonical_name": "Syrett, Robt. H.", "given_names": "Robt. H.", "surname": "Syrett", "position": "Governor's Clerk", "department": "Civil Establishment - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "Edward Metzger", "canonical_name": "Metzger, Edward", "given_names": "Edward", "surname": "Metzger", "position": "Compositor", "department": "Government Printing Establishment - Gambia", "salary_min": 65, "salary_max": 65},
    {"name": "J. T. Coker", "canonical_name": "Coker, J. T.", "given_names": "J. T.", "surname": "Coker", "position": "Assistant Compositor", "department": "Government Printing Establishment - Gambia", "salary_min": 40, "salary_max": 40},
    {"name": "W. H. Berkeley", "canonical_name": "Berkeley, W. H.", "given_names": "W. H.", "surname": "Berkeley", "position": "Collector and Treasurer, and Superintendent of Pilots", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 600, "salary_max": 600},
    {"name": "Thomas Johnson", "canonical_name": "Johnson, Thomas", "given_names": "Thomas", "surname": "Johnson", "position": "Chief Clerk and Cashier", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "A. Walter Lewis", "canonical_name": "Lewis, A. Walter", "given_names": "A. Walter", "surname": "Lewis", "position": "First Clerk of Customs, Tide Surveyor, and Quarantine Officer", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "W. J. Davis", "canonical_name": "Davis, W. J.", "given_names": "W. J.", "surname": "Davis", "position": "Landing Waiter", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 75, "salary_max": 75},
    {"name": "S. D. A. Coker", "canonical_name": "Coker, S. D. A.", "given_names": "S. D. A.", "surname": "Coker", "position": "Tide Waiter", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "C. B. Jones", "canonical_name": "Jones, C. B.", "given_names": "C. B.", "surname": "Jones", "position": "Collector of Palm Wine Duty", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "1st Writer and Superintendent of Police", "department": "Civil Establishment - Gambia", "salary_min": 400, "salary_max": 400}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()