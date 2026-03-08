"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Sir Frederick Gordon Guggisberg", "canonical_name": "Guggisberg, Sir Frederick Gordon", "given_names": "Frederick Gordon", "surname": "Guggisberg", "position": "Governor", "department": "Governor - Gold Coast", "salary_min": 4500, "salary_max": 4500, "duty_allowance": 1500, "honors": ["K.C.M.G.", "D.S.O."], "military_rank": "Brigadier-General"},
    {"name": "James Crawford Maxwell", "canonical_name": "Maxwell, James Crawford", "given_names": "James Crawford", "surname": "Maxwell", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 1800, "salary_max": 1800, "duty_allowance": 360, "honors": ["C.M.G."], "qualifications": ["M.B.", "Ch.B."]},
    {"name": "Sir Philip Crampton Smyly", "canonical_name": "Smyly, Sir Philip Crampton", "given_names": "Philip Crampton", "surname": "Smyly", "position": "Chief Justice", "department": "Judicial Department - Gold Coast", "salary_min": 2000, "salary_max": 2000, "duty_allowance": 400, "honors": ["Kt."], "qualifications": ["LL.D."]},
    {"name": "Charles Henry Harper", "canonical_name": "Harper, Charles Henry", "given_names": "Charles Henry", "surname": "Harper", "position": "Chief Commissioner", "department": "Administration - Ashanti", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 320, "honors": ["C.M.G.", "O.B.E."], "region": "Ashanti"},
    {"name": "Captain Cecil Hamilton Armitage", "canonical_name": "Armitage, Cecil Hamilton", "given_names": "Cecil Hamilton", "surname": "Armitage", "position": "Chief Commissioner", "department": "Administration - Northern Territories", "salary_min": 1600, "salary_max": 1600, "duty_allowance": 320, "honors": ["C.M.G.", "D.S.O."], "military_rank": "Captain", "region": "Northern Territories"},
    {"name": "Reginald Warren Hale Wilkinson", "canonical_name": "Wilkinson, Reginald Warren Hale", "given_names": "Reginald Warren Hale", "surname": "Wilkinson", "position": "Attorney-General", "department": "Legal Department - Gold Coast", "salary_min": 1500, "salary_max": 1500, "duty_allowance": 300},
    {"name": "Robert Edward Burns", "canonical_name": "Burns, Robert Edward", "given_names": "Robert Edward", "surname": "Burns", "position": "Treasurer", "department": "Treasury - Gold Coast", "salary_min": 1350, "salary_max": 1350, "duty_allowance": 270},
    {"name": "David Alexander", "canonical_name": "Alexander, David", "given_names": "David", "surname": "Alexander", "position": "Director of Medical Services", "department": "Medical Department - Gold Coast", "salary_min": 1500, "salary_max": 1500, "duty_allowance": 300},
    {"name": "Edward Hugh Dyneley Nicolls", "canonical_name": "Nicolls, Edward Hugh Dyneley", "given_names": "Edward Hugh Dyneley", "surname": "Nicolls", "position": "Director of Public Works", "department": "Public Works Department - Gold Coast", "salary_min": 1500, "salary_max": 1500, "duty_allowance": 300, "honors": ["O.B.E."]},
    {"name": "Edward Walker Cozens-Hardy", "canonical_name": "Cozens-Hardy, Edward Walker", "given_names": "Edward Walker", "surname": "Cozens-Hardy", "position": "General Manager of Railways", "department": "Railway Department - Gold Coast", "salary_min": 1500, "salary_max": 1500, "duty_allowance": 300},
    {"name": "David James Oman", "canonical_name": "Oman, David James", "given_names": "David James", "surname": "Oman", "position": "Director of Education", "department": "Education Department - Gold Coast", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "Harry William Morrey Bamford", "canonical_name": "Bamford, Harry William Morrey", "given_names": "Harry William Morrey", "surname": "Bamford", "position": "Commissioner of Police", "department": "Police Department - Gold Coast", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240, "honors": ["M.C."]},
    {"name": "John McInnes Reid", "canonical_name": "Reid, John McInnes", "given_names": "John McInnes", "surname": "Reid", "position": "Comptroller of Customs", "department": "Customs - Gold Coast", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240, "military_rank": "Captain"},
    {"name": "Colonel Francis Festing", "canonical_name": "Festing, Francis", "given_names": "Francis", "surname": "Festing", "position": "Colonel", "department": "Military - Gold Coast", "honors": ["Sir"], "military_rank": "Colonel"},
    {"name": "Captain John Glover", "canonical_name": "Glover, John", "given_names": "John", "surname": "Glover", "position": "Captain", "department": "Military - Gold Coast", "honors": ["Sir"], "military_rank": "Captain"},
    {"name": "Sir Garnet Wolseley", "canonical_name": "Wolseley, Garnet", "given_names": "Garnet", "surname": "Wolseley", "position": "Commander", "department": "Military - Gold Coast", "honors": ["Viscount"]},
    {"name": "Sir Francis Scott", "canonical_name": "Scott, Francis", "given_names": "Francis", "surname": "Scott", "position": "Commander", "department": "Military - Gold Coast", "honors": ["Sir"]},
    {"name": "Colonel Sir J. Willcocks", "canonical_name": "Willcocks, J.", "given_names": "J.", "surname": "Willcocks", "position": "Commander", "department": "Military - Gold Coast", "honors": ["Sir"], "military_rank": "Colonel"},
    {"name": "Major H. P. Northcott", "canonical_name": "Northcott, H. P.", "given_names": "H. P.", "surname": "Northcott", "position": "Commissioner and Commandant", "department": "Administration - Northern Territories", "military_rank": "Lieutenant-Colonel", "region": "Northern Territories"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()