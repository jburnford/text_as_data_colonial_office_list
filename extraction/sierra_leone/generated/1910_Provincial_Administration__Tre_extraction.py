"""
Sierra Leone Colonial Office List 1910 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1910

OFFICIALS = [
    {"name": "E. C. D'H. Fairtlough", "canonical_name": "Fairtlough, E. C. D'H.", "given_names": "E. C. D'H.", "surname": "Fairtlough", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "honors": ["C.M.G.", "D.S.O."], "military_rank": "Major"},
    {"name": "J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "qualifications": ["Dr."], "military_rank": "Major"},
    {"name": "G. D. A. Anderson", "canonical_name": "Anderson, G. D. A.", "given_names": "G. D. A.", "surname": "Anderson", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "military_rank": "Major"},
    {"name": "H. G. Warren", "canonical_name": "Warren, H. G.", "given_names": "H. G.", "surname": "Warren", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "military_rank": "Major"},
    {"name": "G. W. Page", "canonical_name": "Page, G. W.", "given_names": "G. W.", "surname": "Page", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650},
    {"name": "W. St. John Oswell", "canonical_name": "Oswell, W. St. John", "given_names": "W. St. John", "surname": "Oswell", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650},
    {"name": "W. D. D. Bowden", "canonical_name": "Bowden, W. D. D.", "given_names": "W. D. D.", "surname": "Bowden", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. E. Bailey", "canonical_name": "Bailey, H. E.", "given_names": "H. E.", "surname": "Bailey", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "C. T. Reaney", "canonical_name": "Reaney, C. T.", "given_names": "C. T.", "surname": "Reaney", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. Craven", "canonical_name": "Craven, J.", "given_names": "J.", "surname": "Craven", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "W. Addison", "canonical_name": "Addison, W.", "given_names": "W.", "surname": "Addison", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. S. Burra", "canonical_name": "Burra, J. S.", "given_names": "J. S.", "surname": "Burra", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "R. H. K. Willans", "canonical_name": "Willans, R. H. K.", "given_names": "R. H. K.", "surname": "Willans", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400, "military_rank": "Major"},
    {"name": "E. D. Vergette", "canonical_name": "Vergette, E. D.", "given_names": "E. D.", "surname": "Vergette", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. A. H. Tinling", "canonical_name": "Tinling, J. A. H.", "given_names": "J. A. H.", "surname": "Tinling", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "W. A. N. Davies", "canonical_name": "Davies, W. A. N.", "given_names": "W. A. N.", "surname": "Davies", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "C. H. S. Vaudrey", "canonical_name": "Vaudrey, C. H. S.", "given_names": "C. H. S.", "surname": "Vaudrey", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. J. Powell", "canonical_name": "Powell, H. J.", "given_names": "H. J.", "surname": "Powell", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "N. G. Frere", "canonical_name": "Frere, N. G.", "given_names": "N. G.", "surname": "Frere", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "R. W. H. Wilkinson", "canonical_name": "Wilkinson, R. W. H.", "given_names": "R. W. H.", "surname": "Wilkinson", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. A. S. Davies", "canonical_name": "Davies, J. A. S.", "given_names": "J. A. S.", "surname": "Davies", "position": "Native Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "A. E. Tuboku-Metzger", "canonical_name": "Tuboku-Metzger, A. E.", "given_names": "A. E.", "surname": "Tuboku-Metzger", "position": "Native Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "W. A. Valantin", "canonical_name": "Valantin, W. A.", "given_names": "W. A.", "surname": "Valantin", "position": "Native Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "A. N. Morrison", "canonical_name": "Morrison, A. N.", "given_names": "A. N.", "surname": "Morrison", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "C. R. Morrison", "canonical_name": "Morrison, C. R.", "given_names": "C. R.", "surname": "Morrison", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "A. D. Yasey", "canonical_name": "Yasey, A. D.", "given_names": "A. D.", "surname": "Yasey", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 90, "salary_max": 120},
    {"name": "J. W. Carew", "canonical_name": "Carew, J. W.", "given_names": "J. W.", "surname": "Carew", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "M. J. O. Macauley", "canonical_name": "Macauley, M. J. O.", "given_names": "M. J. O.", "surname": "Macauley", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "G. A. Harding", "canonical_name": "Harding, G. A.", "given_names": "G. A.", "surname": "Harding", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "N. R. E. Fyne", "canonical_name": "Fyne, N. R. E.", "given_names": "N. R. E.", "surname": "Fyne", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "R. Vandermost", "canonical_name": "Vandermost, R.", "given_names": "R.", "surname": "Vandermost", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "W. A. John", "canonical_name": "John, W. A.", "given_names": "W. A.", "surname": "John", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "C. R. Smith", "canonical_name": "Smith, C. R.", "given_names": "C. R.", "surname": "Smith", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. B. Thomas", "canonical_name": "Thomas, J. B.", "given_names": "J. B.", "surname": "Thomas", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "M. O. Thorpe", "canonical_name": "Thorpe, M. O.", "given_names": "M. O.", "surname": "Thorpe", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "A. F. Taylor", "canonical_name": "Taylor, A. F.", "given_names": "A. F.", "surname": "Taylor", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "M. E. Coomber", "canonical_name": "Coomber, M. E.", "given_names": "M. E.", "surname": "Coomber", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. O. Johnson", "canonical_name": "Johnson, E. O.", "given_names": "E. O.", "surname": "Johnson", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "F. H. Hamilton", "canonical_name": "Hamilton, F. H.", "given_names": "F. H.", "surname": "Hamilton", "position": "Senior Assistant ditto", "department": "Treasury Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "G. R. Moore", "canonical_name": "Moore, G. R.", "given_names": "G. R.", "surname": "Moore", "position": "Assistant ditto", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. N. Edwin", "canonical_name": "Edwin, J. N.", "given_names": "J. N.", "surname": "Edwin", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 180, "salary_max": 220},
    {"name": "A. G. Johnson", "canonical_name": "Johnson, A. G.", "given_names": "A. G.", "surname": "Johnson", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 120, "salary_max": 150, "duty_allowance": 25},
    {"name": "W. B. Gilpin", "canonical_name": "Gilpin, W. B.", "given_names": "W. B.", "surname": "Gilpin", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "M. P. Cole", "canonical_name": "Cole, M. P.", "given_names": "M. P.", "surname": "Cole", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. B. Jarrett", "canonical_name": "Jarrett, J. B.", "given_names": "J. B.", "surname": "Jarrett", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 65, "salary_max": 80},
    {"name": "J. F. Knox", "canonical_name": "Knox, J. F.", "given_names": "J. F.", "surname": "Knox", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "C. G. Black", "canonical_name": "Black, C. G.", "given_names": "C. G.", "surname": "Black", "position": "6th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 35, "salary_max": 45},
    {"name": "E. G. Taylor", "canonical_name": "Taylor, E. G.", "given_names": "E. G.", "surname": "Taylor", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "S. Benjamin", "canonical_name": "Benjamin, S.", "given_names": "S.", "surname": "Benjamin", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. H. Kelso", "canonical_name": "Kelso, J. H.", "given_names": "J. H.", "surname": "Kelso", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 70, "salary_max": 90},
    {"name": "C. Elba", "canonical_name": "Elba, C.", "given_names": "C.", "surname": "Elba", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "S. A. Adams", "canonical_name": "Adams, S. A.", "given_names": "S. A.", "surname": "Adams", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 35, "salary_max": 45},
    {"name": "H. R. W. Gerber", "canonical_name": "Gerber, H. R. W.", "given_names": "H. R. W.", "surname": "Gerber", "position": "6th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "T. N. Spencer", "canonical_name": "Spencer, T. N.", "given_names": "T. N.", "surname": "Spencer", "position": "Treasury Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 50, "salary_max": 60, "location": "Bonthe"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()