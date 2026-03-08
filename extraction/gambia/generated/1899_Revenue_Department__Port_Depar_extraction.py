"""
Gambia Colonial Office List 1899 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1899

OFFICIALS = [
    {"name": "A.C. Greenwood", "canonical_name": "Greenwood, A.C.", "given_names": "A.C.", "surname": "Greenwood", "position": "Treasurer and Collector", "department": "Revenue Department - Gambia", "salary_min": 400, "salary_max": 500},
    {"name": "A. Padesta", "canonical_name": "Padesta, A.", "given_names": "A.", "surname": "Padesta", "position": "Chief Clerk and Cashier", "department": "Revenue Department - Gambia", "salary_min": 233, "salary_max": 233, "allowances": "30l. for collecting lighthouse dues"},
    {"name": "R. H. Pogue", "canonical_name": "Pogue, R. H.", "given_names": "R. H.", "surname": "Pogue", "position": "1st-Class Clerk", "department": "Revenue Department - Gambia", "salary_min": 208, "salary_max": 208, "allowances": "also Registrar of Marine Court 10l., and clerk to Registrar of Shipping, 21l."},
    {"name": "J. Gareze", "canonical_name": "Gareze, J.", "given_names": "J.", "surname": "Gareze", "position": "2nd-Class Clerk", "department": "Revenue Department - Gambia", "salary_min": 150, "salary_max": 150},
    {"name": "C. Prendergast", "canonical_name": "Prendergast, C.", "given_names": "C.", "surname": "Prendergast", "position": "Sup. Clerk", "department": "Revenue Department - Gambia", "salary_min": 80, "salary_max": 80},
    {"name": "L. Barnes-Lawrence", "canonical_name": "Barnes-Lawrence, L.", "given_names": "L.", "surname": "Barnes-Lawrence", "position": "Captain of the Port and Shipping Master", "department": "Port Department - Gambia", "salary_min": 370, "salary_max": 370, "military_rank": "Commander", "honors": ["R.N."], "allowances": "free quarters, shipping fees, and 60l. as Superintendent of Lighthouse"},
    {"name": "J. B. Planollo", "canonical_name": "Planollo, J. B.", "given_names": "J. B.", "surname": "Planollo", "position": "Chief Clerk and Clerk to Shipping Master", "department": "Port Department - Gambia", "salary_min": 175, "salary_max": 175},
    {"name": "J. B. Triay", "canonical_name": "Triay, J. B.", "given_names": "J. B.", "surname": "Triay", "position": "2nd Class Clerk", "department": "Port Department - Gambia", "salary_min": 146, "salary_max": 146},
    {"name": "W. H. Rathborne", "canonical_name": "Rathborne, W. H.", "given_names": "W. H.", "surname": "Rathborne", "position": "Colonial Engineer", "department": "Public Works - Gambia", "salary_min": 83, "salary_max": 83, "military_rank": "Colonel", "acting_status": "acting", "allowances": "42l. for forage allowance"},
    {"name": "F. Robson", "canonical_name": "Robson, F.", "given_names": "F.", "surname": "Robson", "position": "Clerk of Works", "department": "Public Works - Gambia", "salary_min": 267, "salary_max": 267},
    {"name": "H. Maxted", "canonical_name": "Maxted, H.", "given_names": "H.", "surname": "Maxted", "position": "Third-Class Clerk", "department": "Public Works - Gambia", "salary_min": 108, "salary_max": 108},
    {"name": "W. D. Bathurst", "canonical_name": "Bathurst, W. D.", "given_names": "W. D.", "surname": "Bathurst", "position": "Local Auditor and Sanitary Auditor", "department": "Audit - Gambia", "salary_min": 833, "salary_max": 833}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()