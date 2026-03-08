"""
Gambia Colonial Office List 1918 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1918

OFFICIALS = [
    {"name": "C. D. Williams", "canonical_name": "Williams, C. D.", "given_names": "C. D.", "surname": "Williams", "position": "Chief Clerk", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. Gabbidon", "canonical_name": "Gabbidon, J.", "given_names": "J.", "surname": "Gabbidon", "position": "First Grade Clerk", "department": "Customs - The Gambia", "salary_min": 130, "salary_max": 160},
    {"name": "E. A. Mackay", "canonical_name": "Mackay, E. A.", "given_names": "E. A.", "surname": "Mackay", "position": "Second Grade Clerk", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "Second Grade Clerk", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "S. W. Davis", "canonical_name": "Davis, S. W.", "given_names": "S. W.", "surname": "Davis", "position": "Second Grade Clerk", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "M. L. Davies", "canonical_name": "Davies, M. L.", "given_names": "M. L.", "surname": "Davies", "position": "Second Grade Clerk", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 125},
    {"name": "A. H. Jones", "canonical_name": "Jones, A. H.", "given_names": "A. H.", "surname": "Jones", "position": "Fourth Grade Clerk", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "J. B. C. Artley", "canonical_name": "Artley, J. B. C.", "given_names": "J. B. C.", "surname": "Artley", "position": "Fourth Grade Clerk", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 70},
    {"name": "C. J. Clarke", "canonical_name": "Clarke, C. J.", "given_names": "C. J.", "surname": "Clarke", "position": "One Sixth Grade Clerk", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "J. A. N'Jai Gomez", "canonical_name": "Gomez, J. A. N'Jai", "given_names": "J. A. N'Jai", "surname": "Gomez", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 190},
    {"name": "J. E. King", "canonical_name": "King, J. E.", "given_names": "J. E.", "surname": "King", "position": "Chief Landing Waiter and Locker", "department": "Customs - The Gambia", "salary_min": 125, "salary_max": 150},
    {"name": "S. Jobe", "canonical_name": "Jobe, S.", "given_names": "S.", "surname": "Jobe", "position": "First Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "E. W. Johnson", "canonical_name": "Johnson, E. W.", "given_names": "E. W.", "surname": "Johnson", "position": "First Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 60},
    {"name": "S. Senghore", "canonical_name": "Senghore, S.", "given_names": "S.", "surname": "Senghore", "position": "Two Second Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "W. W. Leigh", "canonical_name": "Leigh, W. W.", "given_names": "W. W.", "surname": "Leigh", "position": "Two Second Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 40, "salary_max": 50},
    {"name": "G. D. Edwards", "canonical_name": "Edwards, G. D.", "given_names": "G. D.", "surname": "Edwards", "position": "Four Third Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "C. W. Bass", "canonical_name": "Bass, C. W.", "given_names": "C. W.", "surname": "Bass", "position": "Four Third Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "E. L. See", "canonical_name": "See, E. L.", "given_names": "E. L.", "surname": "See", "position": "Four Third Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40},
    {"name": "J. Maxwell", "canonical_name": "Maxwell, J.", "given_names": "J.", "surname": "Maxwell", "position": "Four Third Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 30, "salary_max": 40}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()