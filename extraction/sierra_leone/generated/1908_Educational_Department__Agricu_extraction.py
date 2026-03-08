"""
Sierra Leone Colonial Office List 1908 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1908

OFFICIALS = [
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "50l. personal"},
    {"name": "J. Proudfoot", "canonical_name": "Proudfoot, J.", "given_names": "J.", "surname": "Proudfoot", "position": "Principal, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 450, "salary_max": 500},
    {"name": "J. H. Duff", "canonical_name": "Duff, J. H.", "given_names": "J. H.", "surname": "Duff", "position": "Education Expert, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. Pool", "canonical_name": "Pool, J.", "given_names": "J.", "surname": "Pool", "position": "Education Expert, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "W. J. Holloway", "canonical_name": "Holloway, W. J.", "given_names": "W. J.", "surname": "Holloway", "position": "Education Expert, Bo School", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "T. Taylor", "canonical_name": "Taylor, T.", "given_names": "T.", "surname": "Taylor", "position": "Clerk to Board of Education", "department": "Educational Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "Hadir-u-deen", "canonical_name": "Hadir-u-deen", "surname": "Hadir-u-deen", "position": "Secretary to Board of Mohammedan Education", "department": "Educational Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "M. J. O. Macauley", "canonical_name": "Macauley, M. J. O.", "given_names": "M. J. O.", "surname": "Macauley", "position": "Clerk to Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "C. W. Smythe", "canonical_name": "Smythe, C. W.", "given_names": "C. W.", "surname": "Smythe", "position": "Superintendent of Agriculture", "department": "Agricultural Development Branch. - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "J. Hartley", "canonical_name": "Hartley, J.", "given_names": "J.", "surname": "Hartley", "position": "Overseer", "department": "Agricultural Development Branch. - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "12l. personal"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()