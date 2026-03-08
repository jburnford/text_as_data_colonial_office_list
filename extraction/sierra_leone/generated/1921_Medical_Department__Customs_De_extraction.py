"""
Sierra Leone Colonial Office List 1921 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1921

OFFICIALS = [
    {"name": "F. E. Whitehead", "canonical_name": "Whitehead, F. E.", "given_names": "F. E.", "surname": "Whitehead", "position": "Senior Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 700, "salary_max": 800},
    {"name": "E. Cameron", "canonical_name": "Cameron, E.", "given_names": "E.", "surname": "Cameron", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 700, "military_rank": "Surgeon-Commander", "qualifications": ["R.N."]},
    {"name": "J. A. Young", "canonical_name": "Young, J. A.", "given_names": "J. A.", "surname": "Young", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 700, "honors": ["M.C."]},
    {"name": "A. W. H. Donaldson", "canonical_name": "Donaldson, A. W. H.", "given_names": "A. W. H.", "surname": "Donaldson", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 700, "honors": ["O.B.E."]},
    {"name": "H. M. O'Byrne", "canonical_name": "O'Byrne, H. M.", "given_names": "H. M.", "surname": "O'Byrne", "position": "Chief of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 700, "salary_max": 700},
    {"name": "C. R. Keyte", "canonical_name": "Keyte, C. R.", "given_names": "C. R.", "surname": "Keyte", "position": "Director of Posts and Telegraphs", "department": "Posts and Telegraphs Department - Sierra Leone", "salary_min": 600, "salary_max": 600},
    {"name": "C. V. Magill", "canonical_name": "Magill, C. V.", "given_names": "C. V.", "surname": "Magill", "position": "Assistant Director of Posts and Telegraphs", "department": "Posts and Telegraphs Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "H. C. Johnson", "canonical_name": "Johnson, H. C.", "given_names": "H. C.", "surname": "Johnson", "position": "Engineer", "department": "Posts and Telegraphs Department - Sierra Leone", "salary_min": 350, "salary_max": 450}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()