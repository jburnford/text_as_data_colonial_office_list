"""
Gambia Colonial Office List 1925 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1925

OFFICIALS = [
    {"name": "W. J. H. Vaughan", "canonical_name": "Vaughan, W. J. H.", "given_names": "W. J. H.", "surname": "Vaughan", "position": "Supervisor of Customs", "department": "Customs - The Gambia", "salary_min": 400, "salary_max": 720, "military_rank": "Paymr.-Lt.-Com."},
    {"name": "C. D. Williams", "canonical_name": "Williams, C. D.", "given_names": "C. D.", "surname": "Williams", "position": "Chief Clerk, 1st Grade", "department": "Customs - The Gambia", "salary_min": 260, "salary_max": 360},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "One 2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "S. W. Davies", "canonical_name": "Davies, S. W.", "given_names": "S. W.", "surname": "Davies", "position": "Six 3rd Grade Clerks", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. G. Lango", "canonical_name": "Lango, J. G.", "given_names": "J. G.", "surname": "Lango", "position": "Six 3rd Grade Clerks", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "N. E. C. Macfoy", "canonical_name": "Macfoy, N. E. C.", "given_names": "N. E. C.", "surname": "Macfoy", "position": "Six 3rd Grade Clerks", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "J. W. G. Carr", "canonical_name": "Carr, J. W. G.", "given_names": "J. W. G.", "surname": "Carr", "position": "Six 3rd Grade Clerks", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "A. C. Nicols", "canonical_name": "Nicols, A. C.", "given_names": "A. C.", "surname": "Nicols", "position": "Six 3rd Grade Clerks", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "E. A. Mackay", "canonical_name": "Mackay, E. A.", "given_names": "E. A.", "surname": "Mackay", "position": "Six 3rd Grade Clerks", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "S. H. Jones", "canonical_name": "Jones, S. H.", "given_names": "S. H.", "surname": "Jones", "position": "One 4th Grade Clerk", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "J. R. King", "canonical_name": "King, J. R.", "given_names": "J. R.", "surname": "King", "position": "1st Class Landing Waiter", "department": "Customs - The Gambia", "salary_min": 160, "salary_max": 230},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "1st Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "1st Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "I. B. M. Y. Jobe", "canonical_name": "Jobe, I. B. M. Y.", "given_names": "I. B. M. Y.", "surname": "Jobe", "position": "1st Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 100, "salary_max": 136},
    {"name": "S. Senghore", "canonical_name": "Senghore, S.", "given_names": "S.", "surname": "Senghore", "position": "2nd Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "J. C. Lusack", "canonical_name": "Lusack, J. C.", "given_names": "J. C.", "surname": "Lusack", "position": "2nd Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "H. B. Nicol", "canonical_name": "Nicol, H. B.", "given_names": "H. B.", "surname": "Nicol", "position": "2nd Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 82},
    {"name": "E. B. Gibson", "canonical_name": "Gibson, E. B.", "given_names": "E. B.", "surname": "Gibson", "position": "2nd Class Landing Waiters", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 82},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()