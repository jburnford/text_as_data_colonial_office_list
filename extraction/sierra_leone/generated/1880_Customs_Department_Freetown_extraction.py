"""
Sierra Leone Colonial Office List 1880 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1880

OFFICIALS = [
    {"name": "M. V. D. Stuart", "canonical_name": "Stuart, M. V. D.", "given_names": "M. V. D.", "surname": "Stuart", "position": "Collector of Customs", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 500, "salary_max": 500},
    {"name": "J. F. Brown", "canonical_name": "Brown, J. F.", "given_names": "J. F.", "surname": "Brown", "position": "Chief Clerk", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 350, "salary_max": 350},
    {"name": "J. W. Cole", "canonical_name": "Cole, J. W.", "given_names": "J. W.", "surname": "Cole", "position": "Clerk", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 200, "salary_max": 200},
    {"name": "J. S. Front", "canonical_name": "Front, J. S.", "given_names": "J. S.", "surname": "Front", "position": "Clerk", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 100, "salary_max": 100},
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Landing Surveyor", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 300, "salary_max": 300},
    {"name": "C. W. Edwin", "canonical_name": "Edwin, C. W.", "given_names": "C. W.", "surname": "Edwin", "position": "Landing Waiter", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 150, "salary_max": 150},
    {"name": "C. T. Mannah", "canonical_name": "Mannah, C. T.", "given_names": "C. T.", "surname": "Mannah", "position": "Landing Waiter", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 75, "salary_max": 75},
    {"name": "J. D. McCauley", "canonical_name": "McCauley, J. D.", "given_names": "J. D.", "surname": "McCauley", "position": "Landing Waiter", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 50, "salary_max": 50},
    {"name": "Tide-watcher 1", "canonical_name": "Tide-watcher 1, .", "surname": "Tide-watcher 1", "position": "Tide-watcher", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 50, "salary_max": 50},
    {"name": "Tide-watcher 2", "canonical_name": "Tide-watcher 2, .", "surname": "Tide-watcher 2", "position": "Tide-watcher", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 50, "salary_max": 50},
    {"name": "Warehouseman 1", "canonical_name": "Warehouseman 1, .", "surname": "Warehouseman 1", "position": "Warehouseman", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 50, "salary_max": 50},
    {"name": "Warehouseman 2", "canonical_name": "Warehouseman 2, .", "surname": "Warehouseman 2", "position": "Warehouseman", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 50, "salary_max": 50},
    {"name": "Warehouseman 3", "canonical_name": "Warehouseman 3, .", "surname": "Warehouseman 3", "position": "Warehouseman", "department": "Customs - Sierra Leone", "location": "Freetown", "salary_min": 50, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()