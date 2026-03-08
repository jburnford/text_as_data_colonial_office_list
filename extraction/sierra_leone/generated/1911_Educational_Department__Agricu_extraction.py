"""
Sierra Leone Colonial Office List 1911 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1911

OFFICIALS = [
    {"name": "R. F. Honter", "canonical_name": "Honter, R. F.", "given_names": "R. F.", "surname": "Honter", "position": "Director of Education", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "50l. personal"},
    {"name": "J. Proudfoot", "canonical_name": "Proudfoot, J.", "given_names": "J.", "surname": "Proudfoot", "position": "Principal, Bo-School", "department": "Educational Department - Sierra Leone", "salary_min": 450, "salary_max": 500},
    {"name": "J. Pool", "canonical_name": "Pool, J.", "given_names": "J.", "surname": "Pool", "position": "Assistant Masters, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 360, "salary_max": 400},
    {"name": "W. J. Holloway", "canonical_name": "Holloway, W. J.", "given_names": "W. J.", "surname": "Holloway", "position": "Assistant Masters, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 360, "salary_max": 400},
    {"name": "A. Aitkin", "canonical_name": "Aitkin, A.", "given_names": "A.", "surname": "Aitkin", "position": "Assistant Masters, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "Hadir-u-deen", "canonical_name": "Hadir-u-deen", "surname": "Hadir-u-deen", "position": "Secretary to Board of Mohammedan Education", "department": "Educational Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "H. L. Weber", "canonical_name": "Weber, H. L.", "given_names": "H. L.", "surname": "Weber", "position": "Clerk to Director of Education", "department": "Educational Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. Hartley", "canonical_name": "Hartley, J.", "given_names": "J.", "surname": "Hartley", "position": "Overseer", "department": "Agricultural Development Branch. - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "12l. personal"},
    {"name": "C. E. Lane-Pool", "canonical_name": "Lane-Pool, C. E.", "given_names": "C. E.", "surname": "Lane-Pool", "position": "Forestry Officer", "department": "Agricultural Development Branch. - Sierra Leone", "salary_min": 500, "salary_max": 500},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()