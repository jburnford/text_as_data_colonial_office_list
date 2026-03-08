"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "The Earl of Selborne", "canonical_name": "Selborne, The Earl of", "surname": "Selborne", "position": "High Commissioner", "department": "High Commissioner and Staff - Sierra Leone", "salary_min": 3000, "salary_max": 3000, "honors": ["K.G.", "G.C.M.G."]},
    {"name": "C. H. Rodwell", "canonical_name": "Rodwell, C. H.", "given_names": "C. H.", "surname": "Rodwell", "position": "Imperial Secretary and Accountant", "department": "High Commissioner and Staff - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "allowances": "500l. allowance", "honors": ["C.M.G."]},
    {"name": "W. G. Bentinck", "canonical_name": "Bentinck, W. G.", "given_names": "W. G.", "surname": "Bentinck", "position": "Assistant Secretary", "department": "High Commissioner and Staff - Sierra Leone", "salary_min": 800, "salary_max": 800, "military_rank": "Major", "honors": ["D.S.O."]},
    {"name": "H. J. Roberts", "canonical_name": "Roberts, H. J.", "given_names": "H. J.", "surname": "Roberts", "position": "Assistant Accountant", "department": "High Commissioner and Staff - Sierra Leone"},
    {"name": "C. L. O'Brien Dutton", "canonical_name": "Dutton, C. L. O'Brien", "given_names": "C. L. O'Brien", "surname": "Dutton", "position": "Chief Clerk", "department": "High Commissioner and Staff - Sierra Leone"},
    {"name": "E. Cohen", "canonical_name": "Cohen, E.", "given_names": "E.", "surname": "Cohen", "position": "Clerical Staff", "department": "High Commissioner and Staff - Sierra Leone"},
    {"name": "J. Moore", "canonical_name": "Moore, J.", "given_names": "J.", "surname": "Moore", "position": "Clerical Staff", "department": "High Commissioner and Staff - Sierra Leone"},
    {"name": "E. G. Dutton", "canonical_name": "Dutton, E. G.", "given_names": "E. G.", "surname": "Dutton", "position": "Clerical Staff", "department": "High Commissioner and Staff - Sierra Leone"},
    {"name": "Shirley Eales", "canonical_name": "Eales, Shirley", "given_names": "Shirley", "surname": "Eales", "position": "Clerical Staff", "department": "High Commissioner and Staff - Sierra Leone"},
    {"name": "Miss Hanbury", "canonical_name": "Hanbury, Miss", "surname": "Hanbury", "position": "Clerical Staff", "department": "High Commissioner and Staff - Sierra Leone"},
    {"name": "Miss Dickson", "canonical_name": "Dickson, Miss", "surname": "Dickson", "position": "Clerical Staff", "department": "High Commissioner and Staff - Sierra Leone"},
    {"name": "Miss Honey", "canonical_name": "Honey, Miss", "surname": "Honey", "position": "Clerical Staff", "department": "High Commissioner and Staff - Sierra Leone"},
    {"name": "Miss Roberts", "canonical_name": "Roberts, Miss", "surname": "Roberts", "position": "Clerical Staff", "department": "High Commissioner and Staff - Sierra Leone"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()