"""
Sierra Leone Colonial Office List 1911 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1911

OFFICIALS = [
    {"name": "R. White", "canonical_name": "White, R.", "given_names": "R.", "surname": "White", "position": "Acting Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 75, "salary_max": 75, "acting_status": "Acting"},
    {"name": "U. J. Lawrence", "canonical_name": "Lawrence, U. J.", "given_names": "U. J.", "surname": "Lawrence", "position": "Deputy Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "T. A. Moses", "canonical_name": "Moses, T. A.", "given_names": "T. A.", "surname": "Moses", "position": "Clerk", "department": "Port and Marine Department - Sierra Leone", "salary_min": 40, "salary_max": 60},
    {"name": "R. M. Forde", "canonical_name": "Forde, R. M.", "given_names": "R. M.", "surname": "Forde", "position": "Principal Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 800, "salary_max": 1000, "duty_allowance": 160},
    {"name": "R. H. Kennan", "canonical_name": "Kennan, R. H.", "given_names": "R. H.", "surname": "Kennan", "position": "Senior Sanitary Officer", "department": "Medical Department - Sierra Leone", "salary_min": 800, "salary_max": 900, "duty_allowance": 160},
    {"name": "D. Alexander", "canonical_name": "Alexander, D.", "given_names": "D.", "surname": "Alexander", "position": "Junior Sanitary Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 700},
    {"name": "J. B. H. Davson", "canonical_name": "Davson, J. B. H.", "given_names": "J. B. H.", "surname": "Davson", "position": "Senior Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 600, "salary_max": 700, "duty_allowance": 120},
    {"name": "J. F. Ward", "canonical_name": "Ward, J. F.", "given_names": "J. F.", "surname": "Ward", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "D. Burrows", "canonical_name": "Burrows, D.", "given_names": "D.", "surname": "Burrows", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "C. H. Allan", "canonical_name": "Allan, C. H.", "given_names": "C. H.", "surname": "Allan", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "E. W. Wood-Mason", "canonical_name": "Wood-Mason, E. W.", "given_names": "E. W.", "surname": "Wood-Mason", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "H. E. Arbuckle", "canonical_name": "Arbuckle, H. E.", "given_names": "H. E.", "surname": "Arbuckle", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "R. W. Orpen", "canonical_name": "Orpen, R. W.", "given_names": "R. W.", "surname": "Orpen", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "W. N. Alexander", "canonical_name": "Alexander, W. N.", "given_names": "W. N.", "surname": "Alexander", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. C. Murphy", "canonical_name": "Murphy, J. C.", "given_names": "J. C.", "surname": "Murphy", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. S. Pearson", "canonical_name": "Pearson, J. S.", "given_names": "J. S.", "surname": "Pearson", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. McConaghy", "canonical_name": "McConaghy, J.", "given_names": "J.", "surname": "McConaghy", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "W. A. Nicholson", "canonical_name": "Nicholson, W. A.", "given_names": "W. A.", "surname": "Nicholson", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "J. Y. Wood", "canonical_name": "Wood, J. Y.", "given_names": "J. Y.", "surname": "Wood", "position": "Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "W. Renner", "canonical_name": "Renner, W.", "given_names": "W.", "surname": "Renner", "position": "Local Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "allowances": "50l. personal"},
    {"name": "W. F. Campbell", "canonical_name": "Campbell, W. F.", "given_names": "W. F.", "surname": "Campbell", "position": "Local Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "W. A. O. Taylor", "canonical_name": "Taylor, W. A. O.", "given_names": "W. A. O.", "surname": "Taylor", "position": "Local Medical Officer", "department": "Medical Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "G. M. Spilsbury", "canonical_name": "Spilsbury, G. M.", "given_names": "G. M.", "surname": "Spilsbury", "position": "Medical Clerk", "department": "Medical Department - Sierra Leone", "salary_min": 130, "salary_max": 150},
    {"name": "M. W. Frazer", "canonical_name": "Frazer, M. W.", "given_names": "M. W.", "surname": "Frazer", "position": "1st Assistant Clerk", "department": "Medical Department - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "M. St. G. Auber", "canonical_name": "Auber, M. St. G.", "given_names": "M. St. G.", "surname": "Auber", "position": "2nd Assistant Clerk", "department": "Medical Department - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "C. A. Inniss", "canonical_name": "Inniss, C. A.", "given_names": "C. A.", "surname": "Inniss", "position": "Storekeeper", "department": "Medical Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "M. N. Lardner", "canonical_name": "Lardner, M. N.", "given_names": "M. N.", "surname": "Lardner", "position": "Resident Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "O. E. King", "canonical_name": "King, O. E.", "given_names": "O. E.", "surname": "King", "position": "Assistant Dispenser and Steward", "department": "Medical Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "E. G. Luke", "canonical_name": "Luke, E. G.", "given_names": "E. G.", "surname": "Luke", "position": "1st Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 80, "salary_max": 110},
    {"name": "J. P. Metzger", "canonical_name": "Metzger, J. P.", "given_names": "J. P.", "surname": "Metzger", "position": "1st Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 80, "salary_max": 110},
    {"name": "W. A. Macauley", "canonical_name": "Macauley, W. A.", "given_names": "W. A.", "surname": "Macauley", "position": "1st Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 80, "salary_max": 110},
    {"name": "Caleb H. Johnson", "canonical_name": "Johnson, Caleb H.", "given_names": "Caleb H.", "surname": "Johnson", "position": "1st Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 80, "salary_max": 110},
    {"name": "D. T. Betts", "canonical_name": "Betts, D. T.", "given_names": "D. T.", "surname": "Betts", "position": "1st Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 80, "salary_max": 110},
    {"name": "I. H. Wright", "canonical_name": "Wright, I. H.", "given_names": "I. H.", "surname": "Wright", "position": "1st Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 80, "salary_max": 110},
    {"name": "D. M. Thomas", "canonical_name": "Thomas, D. M.", "given_names": "D. M.", "surname": "Thomas", "position": "2nd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "O. E. Nylander", "canonical_name": "Nylander, O. E.", "given_names": "O. E.", "surname": "Nylander", "position": "2nd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "P. J. John", "canonical_name": "John, P. J.", "given_names": "P. J.", "surname": "John", "position": "2nd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "H. E. Frazer", "canonical_name": "Frazer, H. E.", "given_names": "H. E.", "surname": "Frazer", "position": "2nd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "T. L. Hooke", "canonical_name": "Hooke, T. L.", "given_names": "T. L.", "surname": "Hooke", "position": "2nd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "M. O. Frazer", "canonical_name": "Frazer, M. O.", "given_names": "M. O.", "surname": "Frazer", "position": "2nd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 60, "salary_max": 75},
    {"name": "M. P. Neville", "canonical_name": "Neville, M. P.", "given_names": "M. P.", "surname": "Neville", "position": "3rd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 45, "salary_max": 60},
    {"name": "E. H. Beccles", "canonical_name": "Beccles, E. H.", "given_names": "E. H.", "surname": "Beccles", "position": "3rd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 45, "salary_max": 60},
    {"name": "T. C. Williams", "canonical_name": "Williams, T. C.", "given_names": "T. C.", "surname": "Williams", "position": "3rd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 45, "salary_max": 60},
    {"name": "J. A. Anderson", "canonical_name": "Anderson, J. A.", "given_names": "J. A.", "surname": "Anderson", "position": "3rd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 45, "salary_max": 60},
    {"name": "E. F. Smith", "canonical_name": "Smith, E. F.", "given_names": "E. F.", "surname": "Smith", "position": "3rd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 45, "salary_max": 60},
    {"name": "J. J. Thomas", "canonical_name": "Thomas, J. J.", "given_names": "J. J.", "surname": "Thomas", "position": "3rd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 45, "salary_max": 60},
    {"name": "P. G. Buck", "canonical_name": "Buck, P. G.", "given_names": "P. G.", "surname": "Buck", "position": "3rd Class Dispensers", "department": "Medical Department - Sierra Leone", "salary_min": 45, "salary_max": 60}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()