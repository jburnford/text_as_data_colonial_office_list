"""
Sierra Leone Colonial Office List 1883 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1883

OFFICIALS = [
    {"name": "T. A. Wall", "canonical_name": "Wall, T. A.", "given_names": "T. A.", "surname": "Wall", "position": "Civil Commandant", "department": "Civil Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "W. H. Hughes", "canonical_name": "Hughes, W. H.", "given_names": "W. H.", "surname": "Hughes", "position": "Clerk to Commandant", "department": "Civil Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "J. E. Parkes", "canonical_name": "Parkes, J. E.", "given_names": "J. E.", "surname": "Parkes", "position": "Clerk to Commandant", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "C. H. Mosley", "canonical_name": "Mosley, C. H.", "given_names": "C. H.", "surname": "Mosley", "position": "Sub-Treasurer and Collector of Customs", "department": "Customs - Sierra Leone", "salary_min": 350, "salary_max": 350},
    {"name": "J. Dougan", "canonical_name": "Dougan, J.", "given_names": "J.", "surname": "Dougan", "position": "Clerk and Warehouse Keeper", "department": "Civil Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "H. R. Williams", "canonical_name": "Williams, H. R.", "given_names": "H. R.", "surname": "Williams", "position": "Postmaster", "department": "Post Office - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "Cline Ogoo", "canonical_name": "Ogoo, Cline", "given_names": "Cline", "surname": "Ogoo", "position": "Bailiff", "department": "Judicial - Sierra Leone", "salary_min": 36, "salary_max": 36},
    {"name": "M. L. Jarrett", "canonical_name": "Jarrett, M. L.", "given_names": "M. L.", "surname": "Jarrett", "position": "Assistant Colonial Surgeon", "department": "Medical - Sierra Leone", "salary_min": 250, "salary_max": 250, "qualifications": ["M.R.C.S."]},
    {"name": "J. M. Metzger", "canonical_name": "Metzger, J. M.", "given_names": "J. M.", "surname": "Metzger", "position": "Sub-Collector of Customs, Officer in charge", "department": "Customs - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "F. J. Davies", "canonical_name": "Davies, F. J.", "given_names": "F. J.", "surname": "Davies", "position": "Sub-Collector", "department": "Customs - Sierra Leone", "acting_status": "Acting", "allowances": "54l. 15s."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()