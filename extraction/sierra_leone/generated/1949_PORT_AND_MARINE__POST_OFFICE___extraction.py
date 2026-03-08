"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "R. E. F. Parsons", "canonical_name": "Parsons, R. E. F.", "given_names": "R. E. F.", "surname": "Parsons", "position": "Harbour-Master", "department": "PORT AND MARINE - Sierra Leone", "salary_min": 900, "salary_max": 900},
    {"name": "C. E. Ross", "canonical_name": "Ross, C. E.", "given_names": "C. E.", "surname": "Ross", "position": "Postmaster-General", "department": "POST OFFICE - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "F. Wood", "canonical_name": "Wood, F.", "given_names": "F.", "surname": "Wood", "position": "Assistant Postmaster-General", "department": "POST OFFICE - Sierra Leone", "salary_scale": "B"},
    {"name": "A. H. Wells", "canonical_name": "Wells, A. H.", "given_names": "A. H.", "surname": "Wells", "position": "Accountant", "department": "POST OFFICE - Sierra Leone", "salary_scale": "B"},
    {"name": "J. C. Oldfield", "canonical_name": "Oldfield, J. C.", "given_names": "J. C.", "surname": "Oldfield", "position": "Postmaster, Freetown", "department": "POST OFFICE - Sierra Leone", "salary_scale": "B", "honors": ["I.S.O."], "location": "Freetown"},
    {"name": "J. N. A. Jones", "canonical_name": "Jones, J. N. A.", "given_names": "J. N. A.", "surname": "Jones", "position": "Assistant Accountant", "department": "POST OFFICE - Sierra Leone", "salary_scale": "B"},
    {"name": "F. G. Taylor", "canonical_name": "Taylor, F. G.", "given_names": "F. G.", "surname": "Taylor", "position": "Senior Engineer", "department": "Wireless and Broadcasting - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()