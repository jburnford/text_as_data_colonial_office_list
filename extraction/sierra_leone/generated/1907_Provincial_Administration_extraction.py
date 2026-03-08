"""
Sierra Leone Colonial Office List 1907 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1907

OFFICIALS = [
    {"name": "G. W. Page", "canonical_name": "Page, G. W.", "given_names": "G. W.", "surname": "Page", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 500, "location": "Sherbro"},
    {"name": "C. T. Reaney", "canonical_name": "Reaney, C. T.", "given_names": "C. T.", "surname": "Reaney", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "location": "Sherbro"},
    {"name": "L. A. Fyne", "canonical_name": "Fyne, L. A.", "given_names": "L. A.", "surname": "Fyne", "position": "1st Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 90, "salary_max": 120, "location": "Sherbro"},
    {"name": "E. Faulkner", "canonical_name": "Faulkner, E.", "given_names": "E.", "surname": "Faulkner", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 350, "location": "Waterloo"},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 70, "location": "Waterloo"},
    {"name": "A. Hudson", "canonical_name": "Hudson, A.", "given_names": "A.", "surname": "Hudson", "position": "Circuit Judge", "department": "Provincial Administration - Sierra Leone", "salary_min": 800, "salary_max": 800, "duty_allowance": 100},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Assistant Master", "department": "Provincial Administration - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "E. C. D. Fairtough", "canonical_name": "Fairtough, E. C. D.", "given_names": "E. C. D.", "surname": "Fairtough", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 400, "salary_max": 500, "honors": ["C.M.G.", "D.S.O."], "military_rank": "Major"},
    {"name": "J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 400, "salary_max": 500, "qualifications": ["Dr."], "military_rank": "Major"},
    {"name": "G. D. Anderson", "canonical_name": "Anderson, G. D.", "given_names": "G. D.", "surname": "Anderson", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Major"},
    {"name": "H. G. Warren", "canonical_name": "Warren, H. G.", "given_names": "H. G.", "surname": "Warren", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Major"},
    {"name": "W. St. John Oswell", "canonical_name": "Oswell, W. St. John", "given_names": "W. St. John", "surname": "Oswell", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "A. G. F. Paling", "canonical_name": "Paling, A. G. F.", "given_names": "A. G. F.", "surname": "Paling", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "W. D. D. Bowden", "canonical_name": "Bowden, W. D. D.", "given_names": "W. D. D.", "surname": "Bowden", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. W. Boddy", "canonical_name": "Boddy, A. W.", "given_names": "A. W.", "surname": "Boddy", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "H. E. Bailey", "canonical_name": "Bailey, H. E.", "given_names": "H. E.", "surname": "Bailey", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "J. J. K. Greenway", "canonical_name": "Greenway, J. J. K.", "given_names": "J. J. K.", "surname": "Greenway", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "J. Craven", "canonical_name": "Craven, J.", "given_names": "J.", "surname": "Craven", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400, "military_rank": "Capt."},
    {"name": "W. Addison", "canonical_name": "Addison, W.", "given_names": "W.", "surname": "Addison", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400, "military_rank": "Lieut."},
    {"name": "J. S. Burra", "canonical_name": "Burra, J. S.", "given_names": "J. S.", "surname": "Burra", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400, "military_rank": "Lieut."},
    {"name": "J. A. S. Davies", "canonical_name": "Davies, J. A. S.", "given_names": "J. A. S.", "surname": "Davies", "position": "Native Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "C. A. Morrison", "canonical_name": "Morrison, C. A.", "given_names": "C. A.", "surname": "Morrison", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "A. N. Morrison", "canonical_name": "Morrison, A. N.", "given_names": "A. N.", "surname": "Morrison", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "T. N. Joah", "canonical_name": "Joah, T. N.", "given_names": "T. N.", "surname": "Joah", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. G. Pearce", "canonical_name": "Pearce, J. G.", "given_names": "J. G.", "surname": "Pearce", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. B. Jarrett", "canonical_name": "Jarrett, J. B.", "given_names": "J. B.", "surname": "Jarrett", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "M. J. Cole", "canonical_name": "Cole, M. J.", "given_names": "M. J.", "surname": "Cole", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. A. Turner", "canonical_name": "Turner, E. A.", "given_names": "E. A.", "surname": "Turner", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "T. N. Spencer", "canonical_name": "Spencer, T. N.", "given_names": "T. N.", "surname": "Spencer", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "O. C. H. Thompson", "canonical_name": "Thompson, O. C. H.", "given_names": "O. C. H.", "surname": "Thompson", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()