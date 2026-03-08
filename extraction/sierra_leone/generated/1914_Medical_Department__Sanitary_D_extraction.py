"""
Sierra Leone Colonial Office List 1914 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1914

OFFICIALS = [
    {"name": "T. E. Rice", "canonical_name": "Rice, T. E.", "given_names": "T. E.", "surname": "Rice", "position": "Principal Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 800, "salary_max": 1000, "duty_allowance": 160},
    {"name": "J. W. Collett", "canonical_name": "Collett, J. W.", "given_names": "J. W.", "surname": "Collett", "position": "Senior Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "C. H. Allan", "canonical_name": "Allan, C. H.", "given_names": "C. H.", "surname": "Allan", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "E. Wood-Mason", "canonical_name": "Wood-Mason, E.", "given_names": "E.", "surname": "Wood-Mason", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "H. E. Arbuckle", "canonical_name": "Arbuckle, H. E.", "given_names": "H. E.", "surname": "Arbuckle", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "R. W. Orpen", "canonical_name": "Orpen, R. W.", "given_names": "R. W.", "surname": "Orpen", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. C. Murphy", "canonical_name": "Murphy, J. C.", "given_names": "J. C.", "surname": "Murphy", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. S. Pearson", "canonical_name": "Pearson, J. S.", "given_names": "J. S.", "surname": "Pearson", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. M'Conaghy", "canonical_name": "M'Conaghy, J.", "given_names": "J.", "surname": "M'Conaghy", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "W. A. Nicholson", "canonical_name": "Nicholson, W. A.", "given_names": "W. A.", "surname": "Nicholson", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. Y. Wood", "canonical_name": "Wood, J. Y.", "given_names": "J. Y.", "surname": "Wood", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "G. Rollason", "canonical_name": "Rollason, G.", "given_names": "G.", "surname": "Rollason", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "G. G. Butler", "canonical_name": "Butler, G. G.", "given_names": "G. G.", "surname": "Butler", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "A. Bremner", "canonical_name": "Bremner, A.", "given_names": "A.", "surname": "Bremner", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "E. J. Powell", "canonical_name": "Powell, E. J.", "given_names": "E. J.", "surname": "Powell", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "R. Semple", "canonical_name": "Semple, R.", "given_names": "R.", "surname": "Semple", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "W. C. E. Bower", "canonical_name": "Bower, W. C. E.", "given_names": "W. C. E.", "surname": "Bower", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "E. F. Ward", "canonical_name": "Ward, E. F.", "given_names": "E. F.", "surname": "Ward", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "W. Allan", "canonical_name": "Allan, W.", "given_names": "W.", "surname": "Allan", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "E. H. Mayhew", "canonical_name": "Mayhew, E. H.", "given_names": "E. H.", "surname": "Mayhew", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "F. E. Whitehead", "canonical_name": "Whitehead, F. E.", "given_names": "F. E.", "surname": "Whitehead", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "W. A. Young", "canonical_name": "Young, W. A.", "given_names": "W. A.", "surname": "Young", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "W. F. Campbell", "canonical_name": "Campbell, W. F.", "given_names": "W. F.", "surname": "Campbell", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "W. A. O. Taylor", "canonical_name": "Taylor, W. A. O.", "given_names": "W. A. O.", "surname": "Taylor", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "M. C. F. Easmon", "canonical_name": "Easmon, M. C. F.", "given_names": "M. C. F.", "surname": "Easmon", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "M. N. Lardner", "canonical_name": "Lardner, M. N.", "given_names": "M. N.", "surname": "Lardner", "position": "Resident Dispenser, Colonial Hospital", "department": "Medical Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "E. O. King", "canonical_name": "King, E. O.", "given_names": "E. O.", "surname": "King", "position": "Assistant Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "C. A. Inniss", "canonical_name": "Inniss, C. A.", "given_names": "C. A.", "surname": "Inniss", "position": "Storekeeper", "department": "Medical Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "R. H. Kennan", "canonical_name": "Kennan, R. H.", "given_names": "R. H.", "surname": "Kennan", "position": "Senior Sanitary Officer", "department": "Sanitary Department - Sierra Leone", "salary_min": 800, "salary_max": 900, "duty_allowance": 160},
    {"name": "H. Simms", "canonical_name": "Simms, H.", "given_names": "H.", "surname": "Simms", "position": "Sanitary Engineer", "department": "Sanitary Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "W. H. Jones", "canonical_name": "Jones, W. H.", "given_names": "W. H.", "surname": "Jones", "position": "Superintendent Sanitary Inspector", "department": "Sanitary Department - Sierra Leone", "salary_min": 250, "salary_max": 350}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()