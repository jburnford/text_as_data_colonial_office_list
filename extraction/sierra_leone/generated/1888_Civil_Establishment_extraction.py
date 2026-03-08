"""
Sierra Leone Colonial Office List 1888 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1888

OFFICIALS = [
    {"name": "J. S. Hay", "canonical_name": "Hay, J. S.", "given_names": "J. S.", "surname": "Hay", "position": "Administrator", "department": "Civil Establishment - Sierra Leone", "salary_min": 1300, "salary_max": 1300, "honors": ["C.M.G."]},
    {"name": "W. Higginson", "canonical_name": "Higginson, W.", "given_names": "W.", "surname": "Higginson", "position": "Government Secretary and Superintendent of Police", "department": "Civil Establishment - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "Robt. H. Syrett", "canonical_name": "Syrett, Robt. H.", "given_names": "Robt. H.", "surname": "Syrett", "position": "Governor's Clerk", "department": "Civil Establishment - Sierra Leone", "salary_min": 160, "salary_max": 160},
    {"name": "M. A. Savage", "canonical_name": "Savage, M. A.", "given_names": "M. A.", "surname": "Savage", "position": "Arabic Writer and General Interpreter", "department": "Civil Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. T. Coker", "canonical_name": "Coker, J. T.", "given_names": "J. T.", "surname": "Coker", "position": "Government Printer", "department": "Government Printing Office - Sierra Leone", "salary_min": 75, "salary_max": 75},
    {"name": "C. W. Thomas", "canonical_name": "Thomas, C. W.", "given_names": "C. W.", "surname": "Thomas", "position": "Assistant Printer", "department": "Government Printing Office - Sierra Leone", "salary_min": 24, "salary_max": 24},
    {"name": "Gilbert T. Carter", "canonical_name": "Carter, Gilbert T.", "given_names": "Gilbert T.", "surname": "Carter", "position": "Treasurer, and Postmaster", "department": "Treasury and Post Office - Sierra Leone", "salary_min": 700, "salary_max": 700, "per_diem": "1s. per diem"},
    {"name": "S. D. A. Coker", "canonical_name": "Coker, S. D. A.", "given_names": "S. D. A.", "surname": "Coker", "position": "First Clerk", "department": "Treasury and Post Office - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "A. J. Nicol", "canonical_name": "Nicol, A. J.", "given_names": "A. J.", "surname": "Nicol", "position": "Assistant Clerk", "department": "Treasury and Post Office - Sierra Leone", "salary_min": 65, "salary_max": 65},
    {"name": "S. C. King", "canonical_name": "King, S. C.", "given_names": "S. C.", "surname": "King", "position": "Sorter and Copyist", "department": "Treasury and Post Office - Sierra Leone", "salary_min": 36, "salary_max": 36},
    {"name": "C. G. Blackburn", "canonical_name": "Blackburn, C. G.", "given_names": "C. G.", "surname": "Blackburn", "position": "Collector of Customs", "department": "Customs Department - Sierra Leone", "salary_min": 450, "salary_max": 450},
    {"name": "S. J. Aubert", "canonical_name": "Aubert, S. J.", "given_names": "S. J.", "surname": "Aubert", "position": "Clerk", "department": "Customs Department - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "J. Dougan", "canonical_name": "Dougan, J.", "given_names": "J.", "surname": "Dougan", "position": "Tide Surveyor and Quarantine Officer", "department": "Customs Department - Sierra Leone", "salary_min": 200, "salary_max": 200},
    {"name": "W. J. Davis", "canonical_name": "Davis, W. J.", "given_names": "W. J.", "surname": "Davis", "position": "Landing Waiter and Locker", "department": "Customs Department - Sierra Leone", "salary_min": 90, "salary_max": 90},
    {"name": "J. N. C. Wilhelm", "canonical_name": "Wilhelm, J. N. C.", "given_names": "J. N. C.", "surname": "Wilhelm", "position": "2nd Landing Waiter and Locker", "department": "Customs Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "J. H. Brady", "canonical_name": "Brady, J. H.", "given_names": "J. H.", "surname": "Brady", "position": "Colonial Engineer and Sanitary Inspector", "department": "Surveyor's Department - Sierra Leone", "salary_min": 500, "salary_max": 500, "per_diem": "2s. 3d. a day"},
    {"name": "G. J. Joiner", "canonical_name": "Joiner, G. J.", "given_names": "G. J.", "surname": "Joiner", "position": "Foreman of Works", "department": "Surveyor's Department - Sierra Leone", "salary_min": 72, "salary_max": 72},
    {"name": "T. J. Carew", "canonical_name": "Carew, T. J.", "given_names": "T. J.", "surname": "Carew", "position": "Storekeeper and Clerk", "department": "Surveyor's Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "M. Taylor", "canonical_name": "Taylor, M.", "given_names": "M.", "surname": "Taylor", "position": "Messenger and Copyist", "department": "Surveyor's Department - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "Thomas H. Spilsbury", "canonical_name": "Spilsbury, Thomas H.", "given_names": "Thomas H.", "surname": "Spilsbury", "position": "Colonial Surgeon", "department": "Medical Establishment - Sierra Leone", "salary_min": 400, "salary_max": 400, "per_diem": "2s. 3d. per day"},
    {"name": "George Spilsbury", "canonical_name": "Spilsbury, George", "given_names": "George", "surname": "Spilsbury", "position": "Dispenser", "department": "Medical Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "J. R. Maxwell", "canonical_name": "Maxwell, J. R.", "given_names": "J. R.", "surname": "Maxwell", "position": "Chief Magistrate", "department": "Judicial Establishment - Sierra Leone", "salary_min": 600, "salary_max": 600},
    {"name": "W. C. Cates", "canonical_name": "Cates, W. C.", "given_names": "W. C.", "surname": "Cates", "position": "Clerk of Courts", "department": "Judicial Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. A. Martin", "canonical_name": "Martin, J. A.", "given_names": "J. A.", "surname": "Martin", "position": "Assistant Clerk of Courts", "department": "Judicial Establishment - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Hon. James Topp", "canonical_name": "Topp, Hon. James", "given_names": "Hon. James", "surname": "Topp", "position": "Coroner", "department": "Judicial Establishment - Sierra Leone"},
    {"name": "R. H. Syrett", "canonical_name": "Syrett, R. H.", "given_names": "R. H.", "surname": "Syrett", "position": "Deputy Coroner", "department": "Judicial Establishment - Sierra Leone"},
    {"name": "Hon. James Topp", "canonical_name": "Topp, Hon. James", "given_names": "Hon. James", "surname": "Topp", "position": "Sheriff", "department": "Judicial Establishment - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "Sergeant Sherrington", "canonical_name": "Sherrington, Sergeant", "given_names": "Sergeant", "surname": "Sherrington", "position": "Gaoler", "department": "Judicial Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "E. A. M. Smith", "canonical_name": "Smith, E. A. M.", "given_names": "E. A. M.", "surname": "Smith", "position": "Manager of Districts", "department": "Managers of Districts - Sierra Leone", "location": "McCarthy's Island", "salary_min": 250, "salary_max": 250, "per_diem": "2s. 3d. per diem"},
    {"name": "J. H. Finden", "canonical_name": "Finden, J. H.", "given_names": "J. H.", "surname": "Finden", "position": "Manager of Districts", "department": "Managers of Districts - Sierra Leone", "location": "British Combo", "salary_min": 100, "salary_max": 100, "per_diem": "2s. 3d. per diem"},
    {"name": "C. B. D. Nicol", "canonical_name": "Nicol, C. B. D.", "given_names": "C. B. D.", "surname": "Nicol", "position": "Clerk and Organist", "department": "Ecclesiastical Establishment - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "M. B. Mason", "canonical_name": "Mason, M. B.", "given_names": "M. B.", "surname": "Mason", "position": "Keeper of Cemetery", "department": "Ecclesiastical Establishment - Sierra Leone", "salary_min": 25, "salary_max": 25},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()