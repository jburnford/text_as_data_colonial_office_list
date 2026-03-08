"""
Sierra Leone Colonial Office List 1878 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1878

OFFICIALS = [
    {"name": "Isaac Fitzjohn", "canonical_name": "Fitzjohn, Isaac", "given_names": "Isaac", "surname": "Fitzjohn", "position": "Postmaster and Mail Packet Agent", "department": "Post Office - Sierra Leone", "salary_min": 200, "salary_max": 200, "allowances": "commission"},
    {"name": "S. Buckle", "canonical_name": "Buckle, S.", "given_names": "S.", "surname": "Buckle", "position": "Clerk", "department": "Post Office - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "J. D. Renner", "canonical_name": "Renner, J. D.", "given_names": "J. D.", "surname": "Renner", "position": "Clerk", "department": "Post Office - Sierra Leone", "salary_min": 35, "salary_max": 35},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sorter", "department": "Post Office - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sorter", "department": "Post Office - Sierra Leone", "salary_min": 25, "salary_max": 25},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Mail Carrier", "department": "Post Office - Sierra Leone", "salary_min": 25, "salary_max": 25},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Mail Carrier", "department": "Post Office - Sierra Leone", "salary_min": 18, "salary_max": 18},
    {"name": "F. H. Lovell", "canonical_name": "Lovell, F. H.", "given_names": "F. H.", "surname": "Lovell", "position": "Colonial Surgeon", "department": "Medical Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "horse allowance, 91l. 5s."},
    {"name": "Robt. Smith", "canonical_name": "Smith, Robt.", "given_names": "Robt.", "surname": "Smith", "position": "Assistant Surgeon", "department": "Medical Establishment - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "horse allowance, 91l. 5s."},
    {"name": "D. Johnson", "canonical_name": "Johnson, D.", "given_names": "D.", "surname": "Johnson", "position": "Compounder and Storekeeper", "department": "Medical Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "quarters"},
    {"name": "D. Cole", "canonical_name": "Cole, D.", "given_names": "D.", "surname": "Cole", "position": "Medical Clerk", "department": "Medical Establishment - Sierra Leone", "salary_min": 75, "salary_max": 75, "allowances": "quarters"},
    {"name": "J. H. F. Roberts", "canonical_name": "Roberts, J. H. F.", "given_names": "J. H. F.", "surname": "Roberts", "position": "Inspector of Health", "department": "Sanitary Department - Sierra Leone", "salary_min": 350, "salary_max": 350},
    {"name": "W. C. During", "canonical_name": "During, W. C.", "given_names": "W. C.", "surname": "During", "position": "Clerk to Inspector", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()