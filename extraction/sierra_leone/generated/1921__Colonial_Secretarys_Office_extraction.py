"""
Sierra Leone Colonial Office List 1921 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1921

OFFICIALS = [
    {"name": "J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1350, "salary_max": 1350, "duty_allowance": 270, "honors": ["C.M.G."], "qualifications": ["M.D."]},
    {"name": "R. de C. Baldwin", "canonical_name": "Baldwin, R. de C.", "given_names": "R. de C.", "surname": "Baldwin", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "G. R. Moore", "canonical_name": "Moore, G. R.", "given_names": "G. R.", "surname": "Moore", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "T. N. Goddard", "canonical_name": "Goddard, T. N.", "given_names": "T. N.", "surname": "Goddard", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "D. W. Carrol", "canonical_name": "Carrol, D. W.", "given_names": "D. W.", "surname": "Carrol", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "J. H. Cheetham Smart", "canonical_name": "Smart, J. H. Cheetham", "given_names": "J. H. Cheetham", "surname": "Smart", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 252, "salary_max": 372},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "I. F. T. George", "canonical_name": "George, I. F. T.", "given_names": "I. F. T.", "surname": "George", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "J. L. Mannah", "canonical_name": "Mannah, J. L.", "given_names": "J. L.", "surname": "Mannah", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "A. E. Scott", "canonical_name": "Scott, A. E.", "given_names": "A. E.", "surname": "Scott", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "A. F. G. Taylor", "canonical_name": "Taylor, A. F. G.", "given_names": "A. F. G.", "surname": "Taylor", "position": "Second Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "T. D. Hewer", "canonical_name": "Hewer, T. D.", "given_names": "T. D.", "surname": "Hewer", "position": "Superintendent", "department": "Printing Branch - Sierra Leone", "salary_min": 600, "salary_max": 600},
    {"name": "J. McCulloch", "canonical_name": "McCulloch, J.", "given_names": "J.", "surname": "McCulloch", "position": "Assistant Superintendent", "department": "Printing Branch - Sierra Leone", "salary_min": 440, "salary_max": 500},
    {"name": "J. N. L. Metzger", "canonical_name": "Metzger, J. N. L.", "given_names": "J. N. L.", "surname": "Metzger", "position": "Proof Reader", "department": "Printing Branch - Sierra Leone", "salary_min": 96, "salary_max": 132},
    {"name": "J. A. Macfoy", "canonical_name": "Macfoy, J. A.", "given_names": "J. A.", "surname": "Macfoy", "position": "Senior Compositor", "department": "Printing Branch - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "J. E. Bailey", "canonical_name": "Bailey, J. E.", "given_names": "J. E.", "surname": "Bailey", "position": "Book Binder", "department": "Printing Branch - Sierra Leone", "salary_min": 96, "salary_max": 132},
    {"name": "W. D. Bowden", "canonical_name": "Bowden, W. D.", "given_names": "W. D.", "surname": "Bowden", "position": "Provincial Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "W. B. Stanley", "canonical_name": "Stanley, W. B.", "given_names": "W. B.", "surname": "Stanley", "position": "Provincial Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "military_rank": "Captain", "honors": ["M.B.E."]},
    {"name": "J. Craven", "canonical_name": "Craven, J.", "given_names": "J.", "surname": "Craven", "position": "Provincial Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "military_rank": "Captain"},
    {"name": "H. Ross", "canonical_name": "Ross, H.", "given_names": "H.", "surname": "Ross", "position": "Provincial Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "W. Addison", "canonical_name": "Addison, W.", "given_names": "W.", "surname": "Addison", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "R. S. Hooker", "canonical_name": "Hooker, R. S.", "given_names": "R. S.", "surname": "Hooker", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "N. C. Hollins", "canonical_name": "Hollins, N. C.", "given_names": "N. C.", "surname": "Hollins", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "N. G. Frere", "canonical_name": "Frere, N. G.", "given_names": "N. G.", "surname": "Frere", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "H. C. Hodgson", "canonical_name": "Hodgson, H. C.", "given_names": "H. C.", "surname": "Hodgson", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "L. H. Berry", "canonical_name": "Berry, L. H.", "given_names": "L. H.", "surname": "Berry", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "W. R. Lyon", "canonical_name": "Lyon, W. R.", "given_names": "W. R.", "surname": "Lyon", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840, "military_rank": "Major"},
    {"name": "P. Shuffrey", "canonical_name": "Shuffrey, P.", "given_names": "P.", "surname": "Shuffrey", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "G. W. James", "canonical_name": "James, G. W.", "given_names": "G. W.", "surname": "James", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "J. E. Benham", "canonical_name": "Benham, J. E.", "given_names": "J. E.", "surname": "Benham", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840, "military_rank": "Captain"},
    {"name": "E. R. Langley", "canonical_name": "Langley, E. R.", "given_names": "E. R.", "surname": "Langley", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "A. V. E. Pearse", "canonical_name": "Pearse, A. V. E.", "given_names": "A. V. E.", "surname": "Pearse", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "E. F. Sayers", "canonical_name": "Sayers, E. F.", "given_names": "E. F.", "surname": "Sayers", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "S. M. Despicht", "canonical_name": "Despicht, S. M.", "given_names": "S. M.", "surname": "Despicht", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "J. T. Kemp", "canonical_name": "Kemp, J. T.", "given_names": "J. T.", "surname": "Kemp", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840},
    {"name": "L. W. Wilson", "canonical_name": "Wilson, L. W.", "given_names": "L. W.", "surname": "Wilson", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840, "military_rank": "Captain"},
    {"name": "J. C. Page", "canonical_name": "Page, J. C.", "given_names": "J. C.", "surname": "Page", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840, "military_rank": "Captain"},
    {"name": "J. F. Fitzgerald", "canonical_name": "Fitzgerald, J. F.", "given_names": "J. F.", "surname": "Fitzgerald", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840, "military_rank": "Captain"},
    {"name": "A. T. Allsopp", "canonical_name": "Allsopp, A. T.", "given_names": "A. T.", "surname": "Allsopp", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840, "military_rank": "Captain"},
    {"name": "F. R. Ellis", "canonical_name": "Ellis, F. R.", "given_names": "F. R.", "surname": "Ellis", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 500, "salary_max": 840, "military_rank": "Captain"},
    {"name": "G. R. Morrison", "canonical_name": "Morrison, G. R.", "given_names": "G. R.", "surname": "Morrison", "position": "Office Assistant", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "A. T. A. Beckley", "canonical_name": "Beckley, A. T. A.", "given_names": "A. T. A.", "surname": "Beckley", "position": "Office Assistant", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "T. A. Thompson", "canonical_name": "Thompson, T. A.", "given_names": "T. A.", "surname": "Thompson", "position": "Office Assistant", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "A. N. Morrison", "canonical_name": "Morrison, A. N.", "given_names": "A. N.", "surname": "Morrison", "position": "First Grade Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "T. N. Spencer", "canonical_name": "Spencer, T. N.", "given_names": "T. N.", "surname": "Spencer", "position": "Second Grade Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "A. P. King", "canonical_name": "King, A. P.", "given_names": "A. P.", "surname": "King", "position": "Second Grade Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "F. B. E. A. McEwen", "canonical_name": "McEwen, F. B. E. A.", "given_names": "F. B. E. A.", "surname": "McEwen", "position": "Second Grade Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 140, "salary_max": 180},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Second Grade Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 140, "salary_max": 180}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()