"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "V. S. Gouldsbury", "canonical_name": "Gouldsbury, V. S.", "given_names": "V. S.", "surname": "Gouldsbury", "position": "Administrator", "department": "Civil Establishment - Gambia", "salary_min": 1300, "salary_max": 1300, "honors": ["C.M.G."], "military_rank": "Surgeon-Major"},
    {"name": "W. P. Roche", "canonical_name": "Roche, W. P.", "given_names": "W. P.", "surname": "Roche", "position": "1st Writer", "department": "Civil Establishment - Gambia", "salary_min": 200, "salary_max": 200, "military_rank": "Capt."},
    {"name": "Robt. H. Syrett", "canonical_name": "Syrett, Robt. H.", "given_names": "Robt. H.", "surname": "Syrett", "position": "Governor's Clerk", "department": "Civil Establishment - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "J. J. Coker", "canonical_name": "Coker, J. J.", "given_names": "J. J.", "surname": "Coker", "position": "Compositor", "department": "Government Printing Establishment - Gambia", "salary_min": 65, "salary_max": 65},
    {"name": "J. N. C. Wilhelm", "canonical_name": "Wilhelm, J. N. C.", "given_names": "J. N. C.", "surname": "Wilhelm", "position": "Assistant Compositor", "department": "Government Printing Establishment - Gambia", "salary_min": 40, "salary_max": 40},
    {"name": "G. T. Carter", "canonical_name": "Carter, G. T.", "given_names": "G. T.", "surname": "Carter", "position": "Collector and Treasurer, and Postmaster", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 700, "salary_max": 700},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Chief Clerk and Cashier", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "S. D. A. Coker", "canonical_name": "Coker, S. D. A.", "given_names": "S. D. A.", "surname": "Coker", "position": "Assistant Clerk", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 72, "salary_max": 72},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "First Clerk of Customs, Tide Surveyor, and Quarantine Officer", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 300, "salary_max": 300},
    {"name": "W. J. Davis", "canonical_name": "Davis, W. J.", "given_names": "W. J.", "surname": "Davis", "position": "Landing Waiter", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 90, "salary_max": 90},
    {"name": "A. J. Nicol", "canonical_name": "Nicol, A. J.", "given_names": "A. J.", "surname": "Nicol", "position": "Tide Waiter", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "C. B. Jones", "canonical_name": "Jones, C. B.", "given_names": "C. B.", "surname": "Jones", "position": "Collector of Palm Wine Duty", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Pilot", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 72, "salary_max": 72},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Pilot", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 72, "salary_max": 72},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Pilot", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 72, "salary_max": 72},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Master of Pilot Boat", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 42, "salary_max": 42},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Seaman", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 24, "salary_max": 24},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Seaman", "department": "Collector and Treasurer's Office - Gambia", "salary_min": 24, "salary_max": 24}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()