"""
Gambia Colonial Office List 1883 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1883

OFFICIALS = [
    {"name": "M. S. Smith", "canonical_name": "Smith, M. S.", "given_names": "M. S.", "surname": "Smith", "position": "Superintendent", "department": "Police Department - Gambia", "salary_min": 400, "salary_max": 400},
    {"name": "W. H. Timperley", "canonical_name": "Timperley, W. H.", "given_names": "W. H.", "surname": "Timperley", "position": "Inspector", "department": "Police Department - Gambia", "location": "Northern District", "salary_min": 275, "salary_max": 275},
    {"name": "C. Howard", "canonical_name": "Howard, C.", "given_names": "C.", "surname": "Howard", "position": "Inspector", "department": "Police Department - Gambia", "location": "Southern District", "salary_min": 250, "salary_max": 250},
    {"name": "P. Kelly", "canonical_name": "Kelly, P.", "given_names": "P.", "surname": "Kelly", "position": "Chief Clerk", "department": "Police Department - Gambia", "salary_min": 280, "salary_max": 280},
    {"name": "J. Dyer", "canonical_name": "Dyer, J.", "given_names": "J.", "surname": "Dyer", "position": "Clerk", "department": "Police Department - Gambia", "salary_min": 160, "salary_max": 160},
    {"name": "A. R. Waylen", "canonical_name": "Waylen, A. R.", "given_names": "A. R.", "surname": "Waylen", "position": "Visiting Surgeon", "department": "Gaol Department - Gambia", "salary_min": 62, "salary_max": 62},
    {"name": "A. Woodridge", "canonical_name": "Woodridge, A.", "given_names": "A.", "surname": "Woodridge", "position": "Gaoler", "department": "Gaol Department - Gambia", "location": "Perth", "salary_min": 150, "salary_max": 150},
    {"name": "W. Ward", "canonical_name": "Ward, W.", "given_names": "W.", "surname": "Ward", "position": "Gaoler", "department": "Gaol Department - Gambia", "location": "Geraldton", "salary_min": 100, "salary_max": 100},
    {"name": "D. Murray", "canonical_name": "Murray, D.", "given_names": "D.", "surname": "Murray", "position": "Gaoler", "department": "Gaol Department - Gambia", "location": "Fremantle", "salary_min": 50, "salary_max": 50},
    {"name": "J. McGovern", "canonical_name": "McGovern, J.", "given_names": "J.", "surname": "McGovern", "position": "Gaoler", "department": "Gaol Department - Gambia", "location": "Albany", "salary_min": 95, "salary_max": 95},
    {"name": "W. Wicketa", "canonical_name": "Wicketa, W.", "given_names": "W.", "surname": "Wicketa", "position": "Gaoler", "department": "Gaol Department - Gambia", "location": "Roebourne"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Gaoler", "department": "Gaol Department - Gambia", "location": "Perth", "salary_min": 100, "salary_max": 100}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()