"""
Sierra Leone Colonial Office List 1878 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1878

OFFICIALS = [
    {"name": "J. W. Jenkins", "canonical_name": "Jenkins, J. W.", "given_names": "J. W.", "surname": "Jenkins", "position": "Colonial Surveyor, Commissioner of Roads, and Superintendent of Public Works", "department": "Surveyor's Department - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "travelling allowances, 1864, 17s. 6d."},
    {"name": "W. B. Campbell", "canonical_name": "Campbell, W. B.", "given_names": "W. B.", "surname": "Campbell", "position": "Clerk to Surveyor", "department": "Surveyor's Department - Sierra Leone", "salary_min": 115, "salary_max": 115},
    {"name": "A. Harleston", "canonical_name": "Harleston, A.", "given_names": "A.", "surname": "Harleston", "position": "Extra Clerk", "department": "Surveyor's Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "W. H. Palmer", "canonical_name": "Palmer, W. H.", "given_names": "W. H.", "surname": "Palmer", "position": "Supervisor of Roads", "department": "Surveyor's Department - Sierra Leone", "salary_min": 65, "salary_max": 65},
    {"name": "S. W. Macrae", "canonical_name": "Macrae, S. W.", "given_names": "S. W.", "surname": "Macrae", "position": "Overseer of ditto", "department": "Surveyor's Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "John Ashwood", "canonical_name": "Ashwood, John", "given_names": "John", "surname": "Ashwood", "position": "Collector of Customs", "department": "Customs Departments - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "J. F. Brown", "canonical_name": "Brown, J. F.", "given_names": "J. F.", "surname": "Brown", "position": "1st Clerk and Warehouse-keeper", "department": "Customs Departments - Sierra Leone", "salary_min": 350, "salary_max": 350},
    {"name": "J. W. Cole", "canonical_name": "Cole, J. W.", "given_names": "J. W.", "surname": "Cole", "position": "2nd ditto and Locker", "department": "Customs Departments - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "J. F. Front", "canonical_name": "Front, J. F.", "given_names": "J. F.", "surname": "Front", "position": "Assistant Clerk", "department": "Customs Departments - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "A. B. Hanson", "canonical_name": "Hanson, A. B.", "given_names": "A. B.", "surname": "Hanson", "position": "Landing Surveyor", "department": "Customs Departments - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "C. W. Edwin", "canonical_name": "Edwin, C. W.", "given_names": "C. W.", "surname": "Edwin", "position": "Senior Landing Writer", "department": "Customs Departments - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "F. J. Davis", "canonical_name": "Davis, F. J.", "given_names": "F. J.", "surname": "Davis", "position": "2nd ditto", "department": "Customs Departments - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant ditto", "department": "Customs Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Tide-waiter", "department": "Customs Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Locker", "department": "Customs Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Locker", "department": "Customs Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Warehousemen", "department": "Customs Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Warehousemen", "department": "Customs Departments - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Isaac Fitzjohn", "canonical_name": "Fitzjohn, Isaac", "given_names": "Isaac", "surname": "Fitzjohn", "position": "Postmaster and Mail Packet Agent", "department": "Post Office - Sierra Leone", "salary_min": 200, "salary_max": 200, "allowances": "commission"},
    {"name": "S. Buckle", "canonical_name": "Buckle, S.", "given_names": "S.", "surname": "Buckle", "position": "Clerks", "department": "Post Office - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "J. D. Renner", "canonical_name": "Renner, J. D.", "given_names": "J. D.", "surname": "Renner", "position": "Clerks", "department": "Post Office - Sierra Leone", "salary_min": 35, "salary_max": 35},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sorters", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sorters", "department": "Post Office - Sierra Leone", "salary_min": 25, "salary_max": 25},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Mail Carriers", "department": "Post Office - Sierra Leone", "salary_min": 25, "salary_max": 25},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Mail Carriers", "department": "Post Office - Sierra Leone", "salary_min": 18, "salary_max": 18},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()