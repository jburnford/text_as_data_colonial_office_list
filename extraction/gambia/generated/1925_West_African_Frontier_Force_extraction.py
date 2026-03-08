"""
Gambia Colonial Office List 1925 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1925

OFFICIALS = [
    {"name": "H. E. Allen", "canonical_name": "Allen, H. E.", "given_names": "H. E.", "surname": "Allen", "position": "Officer Commanding", "department": "West African Frontier Force - Gambia", "salary_min": 700, "salary_max": 700, "duty_allowance": 54, "military_rank": "Captain"},
    {"name": "A. J. Chrystal", "canonical_name": "Chrystal, A. J.", "given_names": "A. J.", "surname": "Chrystal", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "B. B. Moxon", "canonical_name": "Moxon, B. B.", "given_names": "B. B.", "surname": "Moxon", "position": "Lieutenant", "department": "West African Frontier Force - Gambia", "salary_min": 600, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "B. W. Wright", "canonical_name": "Wright, B. W.", "given_names": "B. W.", "surname": "Wright", "position": "Company Quartermaster Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 370, "salary_max": 370},
    {"name": "W. Boon", "canonical_name": "Boon, W.", "given_names": "W.", "surname": "Boon", "position": "Company Quartermaster Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 370, "salary_max": 370},
    {"name": "C. R. Bell", "canonical_name": "Bell, C. R.", "given_names": "C. R.", "surname": "Bell", "position": "Platoon Sergeant", "department": "West African Frontier Force - Gambia", "salary_min": 350, "salary_max": 350},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Clerk and Schoolmaster", "department": "West African Frontier Force - Gambia", "salary_min": 100, "salary_max": 136}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()