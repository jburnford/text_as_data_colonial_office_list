"""
Gambia Colonial Office List 1915 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1915

OFFICIALS = [
    {"name": "A. C. Greenwood", "canonical_name": "Greenwood, A. C.", "given_names": "A. C.", "surname": "Greenwood", "position": "Treasurer and Collector", "department": "Revenue Department - Gambia", "salary_min": 400, "salary_max": 600},
    {"name": "A. Podesta", "canonical_name": "Podesta, A.", "given_names": "A.", "surname": "Podesta", "position": "Chief Clerk and Cashier", "department": "Revenue Department - Gambia", "salary_min": 250, "salary_max": 350, "allowances": "50l. personal, 86l. as Treasurer to the Sanitary Commissioners."},
    {"name": "H. Bacarisa", "canonical_name": "Bacarisa, H.", "given_names": "H.", "surname": "Bacarisa", "position": "2nd Class Clerk", "department": "Revenue Department - Gambia", "salary_min": 160, "salary_max": 200, "allowances": "25l. as Accountant."},
    {"name": "B. R. Miles", "canonical_name": "Miles, B. R.", "given_names": "B. R.", "surname": "Miles", "position": "2nd Class Clerk", "department": "Revenue Department - Gambia", "salary_min": 160, "salary_max": 200},
    {"name": "J. Dotto", "canonical_name": "Dotto, J.", "given_names": "J.", "surname": "Dotto", "position": "3rd Class Clerk", "department": "Revenue Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "H. Cavilla", "canonical_name": "Cavilla, H.", "given_names": "H.", "surname": "Cavilla", "position": "3rd Class Clerk", "department": "Revenue Department - Gambia", "salary_min": 75, "salary_max": 150},
    {"name": "W. H. Niles", "canonical_name": "Niles, W. H.", "given_names": "W. H.", "surname": "Niles", "position": "Captain of the Port and Shipping Master", "department": "Port Department - Gambia", "salary_min": 500, "salary_max": 500, "allowances": "100l. as Emigration Officer, 60l. as Superintendent of Lighthouse.", "military_rank": "Commander", "qualifications": ["R.D.", "R.N.R."]},
    {"name": "F. B. Planello", "canonical_name": "Planello, F. B.", "given_names": "F. B.", "surname": "Planello", "position": "1st Class Clerk and Clerk to Shipping Master", "department": "Port Department - Gambia", "salary_min": 210, "salary_max": 300, "allowances": "moiety of shipping fees."},
    {"name": "J. B. Triay", "canonical_name": "Triay, J. B.", "given_names": "J. B.", "surname": "Triay", "position": "1st Class Clerk", "department": "Port Department - Gambia", "salary_min": 210, "salary_max": 300}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()