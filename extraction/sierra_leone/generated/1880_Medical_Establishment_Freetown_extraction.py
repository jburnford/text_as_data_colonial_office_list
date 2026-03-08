"""
Sierra Leone Colonial Office List 1880 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1880

OFFICIALS = [
    {"name": "W. H. Hart", "canonical_name": "Hart, W. H.", "given_names": "W. H.", "surname": "Hart", "position": "Colonial Surgeon", "department": "Medical Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "travelling allowance, 91l. 5s.", "qualifications": ["M.B."], "location": "Freetown"},
    {"name": "Robt. Smith", "canonical_name": "Smith, Robt.", "given_names": "Robt.", "surname": "Smith", "position": "Assistant Colonial Surgeon", "department": "Medical Establishment - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "travelling allowance, 91l. 5s.", "qualifications": ["M.R.C.S."], "location": "Freetown"},
    {"name": "D. Johnson", "canonical_name": "Johnson, D.", "given_names": "D.", "surname": "Johnson", "position": "Compounder and Storekeeper", "department": "Medical Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150, "location": "Freetown"},
    {"name": "D. Cole", "canonical_name": "Cole, D.", "given_names": "D.", "surname": "Cole", "position": "Medical Clerk", "department": "Medical Establishment - Sierra Leone", "salary_min": 75, "salary_max": 75, "location": "Freetown"},
    {"name": "W. O. During", "canonical_name": "During, W. O.", "given_names": "W. O.", "surname": "During", "position": "Clerk to Inspector of Health", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Edwin Adolphus", "canonical_name": "Adolphus, Edwin", "given_names": "Edwin", "surname": "Adolphus", "position": "Police Magistrate", "department": "Police Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500, "location": "Freetown"},
    {"name": "Daniel Carrol", "canonical_name": "Carrol, Daniel", "given_names": "Daniel", "surname": "Carrol", "position": "Clerk of Police", "department": "Police Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150, "location": "Freetown"},
    {"name": "J. C. Loggie", "canonical_name": "Loggie, J. C.", "given_names": "J. C.", "surname": "Loggie", "position": "Inspector-General of Police", "department": "Police Establishment - Sierra Leone", "salary_min": 400, "salary_max": 400, "allowances": "travelling allowance, 91l. 5s.", "honors": ["C.M.G."], "location": "Freetown"},
    {"name": "Geo. Neville", "canonical_name": "Neville, Geo.", "given_names": "Geo.", "surname": "Neville", "position": "Inspector of Police", "department": "Police Establishment - Sierra Leone", "salary_min": 80, "salary_max": 80, "location": "Freetown"},
    {"name": "W. E. Inniss", "canonical_name": "Inniss, W. E.", "given_names": "W. E.", "surname": "Inniss", "position": "Keeper of Freetown Gaol", "department": "Gaol Establishment - Sierra Leone", "salary_min": 200, "salary_max": 250, "location": "Freetown"},
    {"name": "John Thompson", "canonical_name": "Thompson, John", "given_names": "John", "surname": "Thompson", "position": "Under Gaoler", "department": "Gaol Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100, "location": "Freetown"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()