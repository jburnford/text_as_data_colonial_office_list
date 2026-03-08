"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "C. E. Ross", "canonical_name": "Ross, C. E.", "given_names": "C. E.", "surname": "Ross", "position": "Postmaster-General", "department": "Post Office - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "F. E. B. Clarke", "canonical_name": "Clarke, F. E. B.", "given_names": "F. E. B.", "surname": "Clarke", "position": "Assistant Postmaster-General", "department": "Post Office - Sierra Leone", "salary_scale": "B", "salary_min": 660, "salary_max": 900},
    {"name": "J. C. I. Oldfield", "canonical_name": "Oldfield, J. C. I.", "given_names": "J. C. I.", "surname": "Oldfield", "position": "Accountant", "department": "Post Office - Sierra Leone", "salary_scale": "B", "honors": ["I.S.O."]},
    {"name": "J. N. A. Jones", "canonical_name": "Jones, J. N. A.", "given_names": "J. N. A.", "surname": "Jones", "position": "Assistant Accountant", "department": "Post Office - Sierra Leone", "salary_scale": "B"},
    {"name": "J. J. Mecheux", "canonical_name": "Mecheux, J. J.", "given_names": "J. J.", "surname": "Mecheux", "position": "Assistant Surveyor", "department": "Post Office - Sierra Leone", "salary_scale": "B"},
    {"name": "J. E. Mackay", "canonical_name": "Mackay, J. E.", "given_names": "J. E.", "surname": "Mackay", "position": "Postmaster, Freetown", "department": "Post Office - Sierra Leone", "salary_scale": "B", "location": "Freetown"},
    {"name": "H. A. Turner", "canonical_name": "Turner, H. A.", "given_names": "H. A.", "surname": "Turner", "position": "Engineer-in-Chief", "department": "Engineering - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "J. B. Garrett", "canonical_name": "Garrett, J. B.", "given_names": "J. B.", "surname": "Garrett", "position": "Engineers", "department": "Engineering - Sierra Leone", "salary_scale": "A"},
    {"name": "C. S. Davies", "canonical_name": "Davies, C. S.", "given_names": "C. S.", "surname": "Davies", "position": "Engineers", "department": "Engineering - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()