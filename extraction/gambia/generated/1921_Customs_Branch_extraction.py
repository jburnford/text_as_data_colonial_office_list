"""
Gambia Colonial Office List 1921 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1921

OFFICIALS = [
    {"name": "W. H. Eccles", "canonical_name": "Eccles, W. H.", "given_names": "W. H.", "surname": "Eccles", "position": "Assistant Receiver-General", "department": "Customs - The Gambia", "salary_min": 450, "salary_max": 720},
    {"name": "G. Barraclough", "canonical_name": "Barraclough, G.", "given_names": "G.", "surname": "Barraclough", "position": "Supervisor of Customs", "department": "Customs - The Gambia", "salary_min": 450, "salary_max": 450},
    {"name": "C. D. Williams", "canonical_name": "Williams, C. D.", "given_names": "C. D.", "surname": "Williams", "position": "Chief Clerk, 1st Grade", "department": "Customs - The Gambia", "salary_min": 180, "salary_max": 230},
    {"name": "E. A. Mackay", "canonical_name": "Mackay, E. A.", "given_names": "E. A.", "surname": "Mackay", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. A. Savage", "canonical_name": "Savage, J. A.", "given_names": "J. A.", "surname": "Savage", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "S. W. Davies", "canonical_name": "Davies, S. W.", "given_names": "S. W.", "surname": "Davies", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "M. L. Davis", "canonical_name": "Davis, M. L.", "given_names": "M. L.", "surname": "Davis", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "A. J. Reffell", "canonical_name": "Reffell, A. J.", "given_names": "A. J.", "surname": "Reffell", "position": "2nd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "J. F. Davies", "canonical_name": "Davies, J. F.", "given_names": "J. F.", "surname": "Davies", "position": "3rd Grade Clerk", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. E. King", "canonical_name": "King, J. E.", "given_names": "J. E.", "surname": "King", "position": "Chief Landing Waiter and Locker", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "M. O. Palmer", "canonical_name": "Palmer, M. O.", "given_names": "M. O.", "surname": "Palmer", "position": "Landing Waiter, 1st Class", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "S. Jobe", "canonical_name": "Jobe, S.", "given_names": "S.", "surname": "Jobe", "position": "Landing Waiter, 2nd Class", "department": "Customs - The Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "S. Senghore", "canonical_name": "Senghore, S.", "given_names": "S.", "surname": "Senghore", "position": "Landing Waiter, 3rd Class", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. A. Maxwell", "canonical_name": "Maxwell, J. A.", "given_names": "J. A.", "surname": "Maxwell", "position": "Landing Waiter, 3rd Class", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. C. Lusack", "canonical_name": "Lusack, J. C.", "given_names": "J. C.", "surname": "Lusack", "position": "Landing Waiter, 4th Class", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "J. T. Macauley", "canonical_name": "Macauley, J. T.", "given_names": "J. T.", "surname": "Macauley", "position": "Landing Waiter, 4th Class", "department": "Customs - The Gambia", "salary_min": 50, "salary_max": 80},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()