"""
Sierra Leone Colonial Office List 1906 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1906

OFFICIALS = [
    {"name": "G. W. Page", "canonical_name": "Page, G. W.", "given_names": "G. W.", "surname": "Page", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "location": "Sherbro", "salary_min": 500, "salary_max": 500},
    {"name": "L. A. Fyne", "canonical_name": "Fyne, L. A.", "given_names": "L. A.", "surname": "Fyne", "position": "1st Clerk", "department": "Provincial Administration - Sierra Leone", "location": "Sherbro", "salary_min": 90, "salary_max": 120},
    {"name": "E. Faulkner", "canonical_name": "Faulkner, E.", "given_names": "E.", "surname": "Faulkner", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "location": "Waterloo", "salary_min": 300, "salary_max": 350},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "location": "Waterloo", "salary_min": 60, "salary_max": 70},
    {"name": "A. Hudson", "canonical_name": "Hudson, A.", "given_names": "A.", "surname": "Hudson", "position": "Circuit Judge", "department": "Provincial Administration - Sierra Leone", "salary_min": 800, "salary_max": 800, "duty_allowance": 100},
    {"name": "J. R. Wright", "canonical_name": "Wright, J. R.", "given_names": "J. R.", "surname": "Wright", "position": "Assistant Master", "department": "Provincial Administration - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "E. C. D. Fairtlough", "canonical_name": "Fairtlough, E. C. D.", "given_names": "E. C. D.", "surname": "Fairtlough", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Major", "honors": ["C.M.G.", "D.S.O."]},
    {"name": "J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 400, "salary_max": 500, "qualifications": ["M.D."]},
    {"name": "G. D. Anderson", "canonical_name": "Anderson, G. D.", "given_names": "G. D.", "surname": "Anderson", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Major"},
    {"name": "H. G. Warren", "canonical_name": "Warren, H. G.", "given_names": "H. G.", "surname": "Warren", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 400, "salary_max": 500, "military_rank": "Major"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. T. Cramer", "canonical_name": "Cramer, J. T.", "given_names": "J. T.", "surname": "Cramer", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. J. Berney", "canonical_name": "Berney, A. J.", "given_names": "A. J.", "surname": "Berney", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "W. St. J. Osweil", "canonical_name": "Osweil, W. St. J.", "given_names": "W. St. J.", "surname": "Osweil", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. G. F. Paling", "canonical_name": "Paling, A. G. F.", "given_names": "A. G. F.", "surname": "Paling", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "W. D. D. Bowden", "canonical_name": "Bowden, W. D. D.", "given_names": "W. D. D.", "surname": "Bowden", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. W. Boddy", "canonical_name": "Boddy, A. W.", "given_names": "A. W.", "surname": "Boddy", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "N. H. Boston", "canonical_name": "Boston, N. H.", "given_names": "N. H.", "surname": "Boston", "position": "Native Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "C. A. Morrison", "canonical_name": "Morrison, C. A.", "given_names": "C. A.", "surname": "Morrison", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "A. N. Morrison", "canonical_name": "Morrison, A. N.", "given_names": "A. N.", "surname": "Morrison", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "T. N. Joah", "canonical_name": "Joah, T. N.", "given_names": "T. N.", "surname": "Joah", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. G. Pearce", "canonical_name": "Pearce, J. G.", "given_names": "J. G.", "surname": "Pearce", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. B. Jarrett", "canonical_name": "Jarrett, J. B.", "given_names": "J. B.", "surname": "Jarrett", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "M. J. Cole", "canonical_name": "Cole, M. J.", "given_names": "M. J.", "surname": "Cole", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. A. Turner", "canonical_name": "Turner, E. A.", "given_names": "E. A.", "surname": "Turner", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "T. N. Spencer", "canonical_name": "Spencer, T. N.", "given_names": "T. N.", "surname": "Spencer", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "O. C. H. Thompson", "canonical_name": "Thompson, O. C. H.", "given_names": "O. C. H.", "surname": "Thompson", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()