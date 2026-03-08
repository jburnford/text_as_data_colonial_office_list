"""
Sierra Leone Colonial Office List 1928 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1928

OFFICIALS = [
    {"name": "J. H. Bloomburgh", "canonical_name": "Bloomburgh, J. H.", "given_names": "J. H.", "surname": "Bloomburgh", "position": "Commandant", "department": "Police - Sierra Leone", "salary_min": 800, "salary_max": 800, "honors": ["O.B.E."], "military_rank": "Capt."},
    {"name": "A. P. Oakes", "canonical_name": "Oakes, A. P.", "given_names": "A. P.", "surname": "Oakes", "position": "Assistant Commandant", "department": "Police - Sierra Leone", "salary_min": 450, "salary_max": 700, "qualifications": ["M.M."]},
    {"name": "R. S. Taylor", "canonical_name": "Taylor, R. S.", "given_names": "R. S.", "surname": "Taylor", "position": "Principal Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 1000, "salary_max": 1100},
    {"name": "A. W. H. Donaldson", "canonical_name": "Donaldson, A. W. H.", "given_names": "A. W. H.", "surname": "Donaldson", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "honors": ["O.B.E."]},
    {"name": "L. V. Tebbs", "canonical_name": "Tebbs, L. V.", "given_names": "L. V.", "surname": "Tebbs", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 700, "salary_max": 700, "acting_status": "temporary"},
    {"name": "C. G. Timms", "canonical_name": "Timms, C. G.", "given_names": "C. G.", "surname": "Timms", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "qualifications": ["M.C."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()