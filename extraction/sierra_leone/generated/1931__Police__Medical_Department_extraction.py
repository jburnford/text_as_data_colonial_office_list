"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "J. Beattie", "canonical_name": "Beattie, J.", "given_names": "J.", "surname": "Beattie", "position": "Commandant", "department": "Police - Sierra Leone", "salary_min": 800, "salary_max": 800, "honors": ["M.C."]},
    {"name": "A. P. Oakes", "canonical_name": "Oakes, A. P.", "given_names": "A. P.", "surname": "Oakes", "position": "Assistant Commandant", "department": "Police - Sierra Leone", "salary_min": 450, "salary_max": 700, "honors": ["M.M."]},
    {"name": "H. O. Cain", "canonical_name": "Cain, H. O.", "given_names": "H. O.", "surname": "Cain", "position": "Pay and Quartermaster", "department": "Police - Sierra Leone", "salary_min": 450, "salary_max": 700},
    {"name": "R. S. Taylor", "canonical_name": "Taylor, R. S.", "given_names": "R. S.", "surname": "Taylor", "position": "Principal Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 1000, "salary_max": 1100},
    {"name": "A. W. H. Donaldson", "canonical_name": "Donaldson, A. W. H.", "given_names": "A. W. H.", "surname": "Donaldson", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "honors": ["O.B.E."]},
    {"name": "C. G. Timms", "canonical_name": "Timms, C. G.", "given_names": "C. G.", "surname": "Timms", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "honors": ["M.C."]},
    {"name": "F. C. Small", "canonical_name": "Small, F. C.", "given_names": "F. C.", "surname": "Small", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "J. C. R. Buchanan", "canonical_name": "Buchanan, J. C. R.", "given_names": "J. C. R.", "surname": "Buchanan", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "A. H. Morley", "canonical_name": "Morley, A. H.", "given_names": "A. H.", "surname": "Morley", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "D. P. Turner", "canonical_name": "Turner, D. P.", "given_names": "D. P.", "surname": "Turner", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()