"""
Gambia Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1923

OFFICIALS = [
    {"name": "G. H. Barraclough", "canonical_name": "Barraclough, G. H.", "given_names": "G. H.", "surname": "Barraclough", "position": "Supervisor of Customs", "department": "Customs - The Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "C. D. Williams", "canonical_name": "Williams, C. D.", "given_names": "C. D.", "surname": "Williams", "position": "Chief Clerk, 1st Grade", "department": "Customs - The Gambia", "salary_min": 180, "salary_max": 230},
    {"name": "E. A. Mackay", "canonical_name": "Mackay, E. A.", "given_names": "E. A.", "surname": "Mackay", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "S. W. Davies", "canonical_name": "Davies, S. W.", "given_names": "S. W.", "surname": "Davies", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "A. J. Reffell", "canonical_name": "Reffell, A. J.", "given_names": "A. J.", "surname": "Reffell", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. W. G. Carr", "canonical_name": "Carr, J. W. G.", "given_names": "J. W. G.", "surname": "Carr", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "A. C. Nicols", "canonical_name": "Nicols, A. C.", "given_names": "A. C.", "surname": "Nicols", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. F. Davies", "canonical_name": "Davies, J. F.", "given_names": "J. F.", "surname": "Davies", "position": "3rd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "L. A. Allen", "canonical_name": "Allen, L. A.", "given_names": "L. A.", "surname": "Allen", "position": "3rd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. E. King", "canonical_name": "King, J. E.", "given_names": "J. E.", "surname": "King", "position": "1st Class Landing Waiter (1st Grade)", "department": "Customs - The Gambia", "salary_min": 180, "salary_max": 230},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "1st Class Landing Waiter (2nd Grade)", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "I. B. M. Y. Jobe", "canonical_name": "Jobe, I. B. M. Y.", "given_names": "I. B. M. Y.", "surname": "Jobe", "position": "1st Class Landing Waiter (2nd Grade)", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. G. Lango", "canonical_name": "Lango, J. G.", "given_names": "J. G.", "surname": "Lango", "position": "1st Class Landing Waiter (2nd Grade)", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "S. Senghore", "canonical_name": "Senghore, S.", "given_names": "S.", "surname": "Senghore", "position": "2nd Class Landing Waiter (3rd Grade)", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. C. Lusaak", "canonical_name": "Lusaak, J. C.", "given_names": "J. C.", "surname": "Lusaak", "position": "2nd Class Landing Waiter (3rd Grade)", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. T. Macauley", "canonical_name": "Macauley, J. T.", "given_names": "J. T.", "surname": "Macauley", "position": "2nd Class Landing Waiter (3rd Grade)", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "N. E. C. Macfoy", "canonical_name": "Macfoy, N. E. C.", "given_names": "N. E. C.", "surname": "Macfoy", "position": "2nd Class Landing Waiter (3rd Grade)", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "E. A. Smart", "canonical_name": "Smart, E. A.", "given_names": "E. A.", "surname": "Smart", "position": "2nd Class Landing Waiter (3rd Grade)", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()