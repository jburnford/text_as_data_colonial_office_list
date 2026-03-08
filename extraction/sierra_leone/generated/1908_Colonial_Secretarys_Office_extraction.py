"""
Sierra Leone Colonial Office List 1908 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1908

OFFICIALS = [
    {"name": "G. B. Haddon Smith", "canonical_name": "Smith, G. B. Haddon", "given_names": "G. B.", "surname": "Smith", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 800, "salary_max": 1000, "honors": ["C.M.G."], "duty_allowance": 160},
    {"name": "E. E. Evelyn", "canonical_name": "Evelyn, E. E.", "given_names": "E. E.", "surname": "Evelyn", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "A. Farrar", "canonical_name": "Farrar, A.", "given_names": "A.", "surname": "Farrar", "position": "Asst. Col. Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. W. M. Nylander", "canonical_name": "Nylander, A. W. M.", "given_names": "A. W. M.", "surname": "Nylander", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "D. W. Carrol", "canonical_name": "Carrol, D. W.", "given_names": "D. W.", "surname": "Carrol", "position": "1st Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 160},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "2nd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 120, "salary_max": 140},
    {"name": "A. D. Yaskey", "canonical_name": "Yaskey, A. D.", "given_names": "A. D.", "surname": "Yaskey", "position": "3rd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. H. C. Smart", "canonical_name": "Smart, J. H. C.", "given_names": "J. H. C.", "surname": "Smart", "position": "4th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "C. J. Gilpin", "canonical_name": "Gilpin, C. J.", "given_names": "C. J.", "surname": "Gilpin", "position": "Assistant Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 60, "salary_max": 100, "allowances": "15l. as Bookbinder"},
    {"name": "J. Macfoy", "canonical_name": "Macfoy, J.", "given_names": "J.", "surname": "Macfoy", "position": "1st Class Composer", "department": "Printing Branch - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "C. E. Turner", "canonical_name": "Turner, C. E.", "given_names": "C. E.", "surname": "Turner", "position": "1st Class Composer", "department": "Printing Branch - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "N. S. Thomas", "canonical_name": "Thomas, N. S.", "given_names": "N. S.", "surname": "Thomas", "position": "1st Class Composer", "department": "Printing Branch - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "A. T. George", "canonical_name": "George, A. T.", "given_names": "A. T.", "surname": "George", "position": "2nd Class Composer", "department": "Printing Branch - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. H. Danner", "canonical_name": "Danner, J. H.", "given_names": "J. H.", "surname": "Danner", "position": "2nd Class Composer", "department": "Printing Branch - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. C. D'H. Fairtough", "canonical_name": "Fairtough, E. C. D'H.", "given_names": "E. C. D'H.", "surname": "Fairtough", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "honors": ["C.M.G.", "D.S.O."], "military_rank": "Major"},
    {"name": "J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "qualifications": ["Dr."]},
    {"name": "G. D. A. Anderson", "canonical_name": "Anderson, G. D. A.", "given_names": "G. D. A.", "surname": "Anderson", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "military_rank": "Major"},
    {"name": "H. G. Warren", "canonical_name": "Warren, H. G.", "given_names": "H. G.", "surname": "Warren", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "military_rank": "Major"},
    {"name": "G. W. Page", "canonical_name": "Page, G. W.", "given_names": "G. W.", "surname": "Page", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650},
    {"name": "W. St. John Oswell", "canonical_name": "Oswell, W. St. John", "given_names": "W. St. John", "surname": "Oswell", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650},
    {"name": "A. G. F. Paling", "canonical_name": "Paling, A. G. F.", "given_names": "A. G. F.", "surname": "Paling", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "A. W. Boddy", "canonical_name": "Boddy, A. W.", "given_names": "A. W.", "surname": "Boddy", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "W. D. D. Bowden", "canonical_name": "Bowden, W. D. D.", "given_names": "W. D. D.", "surname": "Bowden", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "H. E. Bailey", "canonical_name": "Bailey, H. E.", "given_names": "H. E.", "surname": "Bailey", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "C. T. Reaney", "canonical_name": "Reaney, C. T.", "given_names": "C. T.", "surname": "Reaney", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "J. Craven", "canonical_name": "Craven, J.", "given_names": "J.", "surname": "Craven", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "W. Addison", "canonical_name": "Addison, W.", "given_names": "W.", "surname": "Addison", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "J. S. Burra", "canonical_name": "Burra, J. S.", "given_names": "J. S.", "surname": "Burra", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "R. H. K. Williams", "canonical_name": "Williams, R. H. K.", "given_names": "R. H. K.", "surname": "Williams", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450, "military_rank": "Major"},
    {"name": "F. A. Vander Meulen", "canonical_name": "Meulen, F. A. Vander", "given_names": "F. A.", "surname": "Meulen", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450, "qualifications": ["B.L."]},
    {"name": "E. D. Vergette", "canonical_name": "Vergette, E. D.", "given_names": "E. D.", "surname": "Vergette", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "E. Faulkner", "canonical_name": "Faulkner, E.", "given_names": "E.", "surname": "Faulkner", "position": "Native District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. A. S. Davies", "canonical_name": "Davies, J. A. S.", "given_names": "J. A. S.", "surname": "Davies", "position": "Native Assistant ditto", "department": "Provincial Administration - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "L. A. Fyne", "canonical_name": "Fyne, L. A.", "given_names": "L. A.", "surname": "Fyne", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 90, "salary_max": 120},
    {"name": "A. N. Morrison", "canonical_name": "Morrison, A. N.", "given_names": "A. N.", "surname": "Morrison", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "C. R. Morrison", "canonical_name": "Morrison, C. R.", "given_names": "C. R.", "surname": "Morrison", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "T. N. Noah", "canonical_name": "Noah, T. N.", "given_names": "T. N.", "surname": "Noah", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "J. B. Jarrett", "canonical_name": "Jarrett, J. B.", "given_names": "J. B.", "surname": "Jarrett", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "J. W. Carew", "canonical_name": "Carew, J. W.", "given_names": "J. W.", "surname": "Carew", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "T. N. Spencer", "canonical_name": "Spencer, T. N.", "given_names": "T. N.", "surname": "Spencer", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "A. P. King", "canonical_name": "King, A. P.", "given_names": "A. P.", "surname": "King", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. W. Davies", "canonical_name": "Davies, J. W.", "given_names": "J. W.", "surname": "Davies", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "W. R. Macauley", "canonical_name": "Macauley, W. R.", "given_names": "W. R.", "surname": "Macauley", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. B. Campbell", "canonical_name": "Campbell, E. B.", "given_names": "E. B.", "surname": "Campbell", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. A. Williams", "canonical_name": "Williams, J. A.", "given_names": "J. A.", "surname": "Williams", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "R. Vandermost", "canonical_name": "Vandermost, R.", "given_names": "R.", "surname": "Vandermost", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()