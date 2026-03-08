"""
Sierra Leone Colonial Office List 1907 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1907

OFFICIALS = [
    {"name": "A. H. Hanley", "canonical_name": "Hanley, A. H.", "given_names": "A. H.", "surname": "Hanley", "position": "Principal Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 800, "salary_max": 1000, "honors": ["C.M.G."]},
    {"name": "T. Hood", "canonical_name": "Hood, T.", "given_names": "T.", "surname": "Hood", "position": "Senior Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 600, "salary_max": 700},
    {"name": "J. F. W. Ward", "canonical_name": "Ward, J. F. W.", "given_names": "J. F. W.", "surname": "Ward", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. B. Davson", "canonical_name": "Davson, J. B.", "given_names": "J. B.", "surname": "Davson", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "C. B. Hunter", "canonical_name": "Hunter, C. B.", "given_names": "C. B.", "surname": "Hunter", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "D. Burrows", "canonical_name": "Burrows, D.", "given_names": "D.", "surname": "Burrows", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "St. G. Gray", "canonical_name": "Gray, St. G.", "given_names": "St. G.", "surname": "Gray", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "A. T. Latchmore", "canonical_name": "Latchmore, A. T.", "given_names": "A. T.", "surname": "Latchmore", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "C. H. Allan", "canonical_name": "Allan, C. H.", "given_names": "C. H.", "surname": "Allan", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "O. J. F. C. Greenidge", "canonical_name": "Greenidge, O. J. F. C.", "given_names": "O. J. F. C.", "surname": "Greenidge", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "E. W. Wood-Mason", "canonical_name": "Wood-Mason, E. W.", "given_names": "E. W.", "surname": "Wood-Mason", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. Moore", "canonical_name": "Moore, J.", "given_names": "J.", "surname": "Moore", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "H. E. Arbuckle", "canonical_name": "Arbuckle, H. E.", "given_names": "H. E.", "surname": "Arbuckle", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "W. Renner", "canonical_name": "Renner, W.", "given_names": "W.", "surname": "Renner", "position": "Local Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. Scotland", "canonical_name": "Scotland, J.", "given_names": "J.", "surname": "Scotland", "position": "Local Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "W. F. Campbell", "canonical_name": "Campbell, W. F.", "given_names": "W. F.", "surname": "Campbell", "position": "Local Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "G. M. Spilsbury", "canonical_name": "Spilsbury, G. M.", "given_names": "G. M.", "surname": "Spilsbury", "position": "Medical Clerk", "department": "Medical - Sierra Leone", "salary_min": 130, "salary_max": 150},
    {"name": "D. T. Betts", "canonical_name": "Betts, D. T.", "given_names": "D. T.", "surname": "Betts", "position": "1st Assistant", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "M. W. Frazer", "canonical_name": "Frazer, M. W.", "given_names": "M. W.", "surname": "Frazer", "position": "2nd Assistant", "department": "Medical - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "C. A. Innis", "canonical_name": "Innis, C. A.", "given_names": "C. A.", "surname": "Innis", "position": "Storekeeper", "department": "Medical - Sierra Leone"},
    {"name": "W. Z. Young", "canonical_name": "Young, W. Z.", "given_names": "W. Z.", "surname": "Young", "position": "Compounder", "department": "Medical - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "M. N. Lardner", "canonical_name": "Lardner, M. N.", "given_names": "M. N.", "surname": "Lardner", "position": "Assistant Dispenser and Steward", "department": "Medical - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "E. G. Luke", "canonical_name": "Luke, E. G.", "given_names": "E. G.", "surname": "Luke", "position": "1st Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 75, "salary_max": 110},
    {"name": "J. Metzger", "canonical_name": "Metzger, J.", "given_names": "J.", "surname": "Metzger", "position": "1st Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 75, "salary_max": 110},
    {"name": "A. W. Macauley", "canonical_name": "Macauley, A. W.", "given_names": "A. W.", "surname": "Macauley", "position": "2nd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "J. H. Wright", "canonical_name": "Wright, J. H.", "given_names": "J. H.", "surname": "Wright", "position": "2nd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "C. H. Johnson", "canonical_name": "Johnson, C. H.", "given_names": "C. H.", "surname": "Johnson", "position": "2nd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "H. E. Frazer", "canonical_name": "Frazer, H. E.", "given_names": "H. E.", "surname": "Frazer", "position": "2nd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "O. Nylander", "canonical_name": "Nylander, O.", "given_names": "O.", "surname": "Nylander", "position": "2nd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "D. M. Thomas", "canonical_name": "Thomas, D. M.", "given_names": "D. M.", "surname": "Thomas", "position": "2nd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "P. J. John", "canonical_name": "John, P. J.", "given_names": "P. J.", "surname": "John", "position": "3rd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 45, "salary_max": 60},
    {"name": "M. O. Frazer", "canonical_name": "Frazer, M. O.", "given_names": "M. O.", "surname": "Frazer", "position": "3rd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 45, "salary_max": 60},
    {"name": "T. M. Hooke", "canonical_name": "Hooke, T. M.", "given_names": "T. M.", "surname": "Hooke", "position": "3rd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 45, "salary_max": 60},
    {"name": "J. A. Short", "canonical_name": "Short, J. A.", "given_names": "J. A.", "surname": "Short", "position": "3rd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 45, "salary_max": 60},
    {"name": "J. F. Johnson", "canonical_name": "Johnson, J. F.", "given_names": "J. F.", "surname": "Johnson", "position": "3rd Class Dispenser", "department": "Medical - Sierra Leone", "salary_min": 45, "salary_max": 60}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()