"""
Sierra Leone Colonial Office List 1909 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1909

OFFICIALS = [
    {"name": "Major E. C. D'H. Fairtough", "canonical_name": "Fairtough, E. C. D'H.", "given_names": "E. C. D'H.", "surname": "Fairtough", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "honors": ["C.M.G.", "D.S.O."], "military_rank": "Major"},
    {"name": "Dr. J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "qualifications": ["Dr."]},
    {"name": "Major G. D. A. Anderson", "canonical_name": "Anderson, G. D. A.", "given_names": "G. D. A.", "surname": "Anderson", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "military_rank": "Major"},
    {"name": "Major H. G. Warren", "canonical_name": "Warren, H. G.", "given_names": "H. G.", "surname": "Warren", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650, "military_rank": "Major"},
    {"name": "G. W. Page", "canonical_name": "Page, G. W.", "given_names": "G. W.", "surname": "Page", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650},
    {"name": "W. St. John Oswell", "canonical_name": "Oswell, W. St. John", "given_names": "W. St. John", "surname": "Oswell", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 450, "salary_max": 650},
    {"name": "A. G. F. Paling", "canonical_name": "Paling, A. G. F.", "given_names": "A. G. F.", "surname": "Paling", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "A. W. Boddy", "canonical_name": "Boddy, A. W.", "given_names": "A. W.", "surname": "Boddy", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "W. D. D. Bowden", "canonical_name": "Bowden, W. D. D.", "given_names": "W. D. D.", "surname": "Bowden", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "H. E. Bailey", "canonical_name": "Bailey, H. E.", "given_names": "H. E.", "surname": "Bailey", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "C. T. Reaney", "canonical_name": "Reaney, C. T.", "given_names": "C. T.", "surname": "Reaney", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. Craven", "canonical_name": "Craven, J.", "given_names": "J.", "surname": "Craven", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "W. Addison", "canonical_name": "Addison, W.", "given_names": "W.", "surname": "Addison", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. S. Burra", "canonical_name": "Burra, J. S.", "given_names": "J. S.", "surname": "Burra", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "Major R. H. K. Willans", "canonical_name": "Willans, R. H. K.", "given_names": "R. H. K.", "surname": "Willans", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400, "military_rank": "Major"},
    {"name": "E. D. Vergette", "canonical_name": "Vergette, E. D.", "given_names": "E. D.", "surname": "Vergette", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. A. H. Tinling", "canonical_name": "Tinling, J. A. H.", "given_names": "J. A. H.", "surname": "Tinling", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "W. A. N. Davies", "canonical_name": "Davies, W. A. N.", "given_names": "W. A. N.", "surname": "Davies", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. A. S. Davies", "canonical_name": "Davies, J. A. S.", "given_names": "J. A. S.", "surname": "Davies", "position": "Native Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "A. E. Tuboku-Metzger", "canonical_name": "Tuboku-Metzger, A. E.", "given_names": "A. E.", "surname": "Tuboku-Metzger", "position": "Native Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 250, "salary_max": 350},
    {"name": "A. N. Morrison", "canonical_name": "Morrison, A. N.", "given_names": "A. N.", "surname": "Morrison", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "C. R. Morrison", "canonical_name": "Morrison, C. R.", "given_names": "C. R.", "surname": "Morrison", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "A. D. Ynasey", "canonical_name": "Ynasey, A. D.", "given_names": "A. D.", "surname": "Ynasey", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 90, "salary_max": 120},
    {"name": "J. B. Jarrett", "canonical_name": "Jarrett, J. B.", "given_names": "J. B.", "surname": "Jarrett", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "J. W. Carew", "canonical_name": "Carew, J. W.", "given_names": "J. W.", "surname": "Carew", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "T. R. Jones", "canonical_name": "Jones, T. R.", "given_names": "T. R.", "surname": "Jones", "position": "Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "J. W. Davies", "canonical_name": "Davies, J. W.", "given_names": "J. W.", "surname": "Davies", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "W. R. Macauley", "canonical_name": "Macauley, W. R.", "given_names": "W. R.", "surname": "Macauley", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. B. Campbell", "canonical_name": "Campbell, E. B.", "given_names": "E. B.", "surname": "Campbell", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "R. Vandermost", "canonical_name": "Vandermost, R.", "given_names": "R.", "surname": "Vandermost", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "W. A. John", "canonical_name": "John, W. A.", "given_names": "W. A.", "surname": "John", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "G. E. M. Hughes", "canonical_name": "Hughes, G. E. M.", "given_names": "G. E. M.", "surname": "Hughes", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "J. N. Johnson", "canonical_name": "Johnson, J. N.", "given_names": "J. N.", "surname": "Johnson", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "M. St. G. Auber", "canonical_name": "Auber, M. St. G.", "given_names": "M. St. G.", "surname": "Auber", "position": "Assistant Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "E. O. Johnson", "canonical_name": "Johnson, E. O.", "given_names": "E. O.", "surname": "Johnson", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 500, "salary_max": 700, "duty_allowance": 100},
    {"name": "S. Renshaw", "canonical_name": "Renshaw, S.", "given_names": "S.", "surname": "Renshaw", "position": "Senior Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "G. R. Moore", "canonical_name": "Moore, G. R.", "given_names": "G. R.", "surname": "Moore", "position": "Assistant Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. N. Edwin", "canonical_name": "Edwin, J. N.", "given_names": "J. N.", "surname": "Edwin", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 180, "salary_max": 220},
    {"name": "A. G. Johnson", "canonical_name": "Johnson, A. G.", "given_names": "A. G.", "surname": "Johnson", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 120, "salary_max": 150, "duty_allowance": 25},
    {"name": "W. B. Gilpin", "canonical_name": "Gilpin, W. B.", "given_names": "W. B.", "surname": "Gilpin", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "S. Benjamin", "canonical_name": "Benjamin, S.", "given_names": "S.", "surname": "Benjamin", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. H. Kelso", "canonical_name": "Kelso, J. H.", "given_names": "J. H.", "surname": "Kelso", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 65, "salary_max": 80},
    {"name": "J. F. Knox", "canonical_name": "Knox, J. F.", "given_names": "J. F.", "surname": "Knox", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. N. Taylor", "canonical_name": "Taylor, J. N.", "given_names": "J. N.", "surname": "Taylor", "position": "6th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 35, "salary_max": 45},
    {"name": "E. G. Taylor", "canonical_name": "Taylor, E. G.", "given_names": "E. G.", "surname": "Taylor", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "M. P. Cole", "canonical_name": "Cole, M. P.", "given_names": "M. P.", "surname": "Cole", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 70, "salary_max": 90},
    {"name": "C. J. Ella", "canonical_name": "Ella, C. J.", "given_names": "C. J.", "surname": "Ella", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "A. F. Dove", "canonical_name": "Dove, A. F.", "given_names": "A. F.", "surname": "Dove", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 35, "salary_max": 45},
    {"name": "J. O. Nicolls", "canonical_name": "Nicolls, J. O.", "given_names": "J. O.", "surname": "Nicolls", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "T. N. Spencer", "canonical_name": "Spencer, T. N.", "given_names": "T. N.", "surname": "Spencer", "position": "Treasury Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 50, "salary_max": 60, "location": "Bonthic"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()