"""
Sierra Leone Colonial Office List 1879 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1879

OFFICIALS = [
    {"name": "M. V. D. Stuart", "canonical_name": "Stuart, M. V. D.", "given_names": "M. V. D.", "surname": "Stuart", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "J. F. Brown", "canonical_name": "Brown, J. F.", "given_names": "J. F.", "surname": "Brown", "position": "1st Clerk and Warehouse-keeper", "department": "Customs Department - Sierra Leone", "salary_min": 350, "salary_max": 350},
    {"name": "J. W. Cole", "canonical_name": "Cole, J. W.", "given_names": "J. W.", "surname": "Cole", "position": "2nd Clerk and Locker", "department": "Customs Department - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "J. F. Front", "canonical_name": "Front, J. F.", "given_names": "J. F.", "surname": "Front", "position": "Assistant Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Landing Surveyor", "department": "Customs Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "C. W. Edwin", "canonical_name": "Edwin, C. W.", "given_names": "C. W.", "surname": "Edwin", "position": "1st Landing Waiter and Searcher", "department": "Customs Department - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "Charles T. Mannah", "canonical_name": "Mannah, Charles T.", "given_names": "Charles T.", "surname": "Mannah", "position": "2nd Landing Waiter and Searcher", "department": "Customs Department - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "John D. Macaulay", "canonical_name": "Macaulay, John D.", "given_names": "John D.", "surname": "Macaulay", "position": "Assistant Landing Waiter and Searcher", "department": "Customs Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Tide-waiter", "department": "Customs Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Locker", "department": "Customs Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Locker", "department": "Customs Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Warehouseman", "department": "Customs Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Warehouseman", "department": "Customs Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()