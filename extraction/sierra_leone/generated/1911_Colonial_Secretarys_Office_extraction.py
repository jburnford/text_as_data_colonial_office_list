"""
Sierra Leone Colonial Office List 1911 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1911

OFFICIALS = [
    {"name": "G. B. Haddon Smith", "canonical_name": "Smith, G. B. Haddon", "given_names": "G. B.", "surname": "Smith", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 800, "salary_max": 1000, "honors": ["C.M.G."], "duty_allowance": 160},
    {"name": "E. E. Evelyn", "canonical_name": "Evelyn, E. E.", "given_names": "E. E.", "surname": "Evelyn", "position": "Senior Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "A. Farrar", "canonical_name": "Farrar, A.", "given_names": "A.", "surname": "Farrar", "position": "Ass't Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "N. C. Hollins", "canonical_name": "Hollins, N. C.", "given_names": "N. C.", "surname": "Hollins", "position": "Ass't Secretaries", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "A. W. M. Nylander", "canonical_name": "Nylander, A. W. M.", "given_names": "A. W. M.", "surname": "Nylander", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 200, "salary_max": 250, "allowances": "20l. personal"},
    {"name": "D. W. Carrol", "canonical_name": "Carrol, D. W.", "given_names": "D. W.", "surname": "Carrol", "position": "1st Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 140, "salary_max": 160},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "2nd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 120, "salary_max": 140},
    {"name": "J. H. C. Smart", "canonical_name": "Smart, J. H. C.", "given_names": "J. H. C.", "surname": "Smart", "position": "3rd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 120, "salary_max": 140},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "4th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "I. F. T. George", "canonical_name": "George, I. F. T.", "given_names": "I. F. T.", "surname": "George", "position": "5th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. L. John", "canonical_name": "John, J. L.", "given_names": "J. L.", "surname": "John", "position": "6th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Printer", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "C. J. Gilpin", "canonical_name": "Gilpin, C. J.", "given_names": "C. J.", "surname": "Gilpin", "position": "Assistant Printer", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 150, "allowances": "25l. personal"},
    {"name": "J. Macfoy", "canonical_name": "Macfoy, J.", "given_names": "J.", "surname": "Macfoy", "position": "1st Class Compositors", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "C. E. Turner", "canonical_name": "Turner, C. E.", "given_names": "C. E.", "surname": "Turner", "position": "1st Class Compositors", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "N. S. Thomas", "canonical_name": "Thomas, N. S.", "given_names": "N. S.", "surname": "Thomas", "position": "1st Class Compositors", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 60, "salary_max": 80},
    {"name": "A. T. George", "canonical_name": "George, A. T.", "given_names": "A. T.", "surname": "George", "position": "2nd Class Compositors", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "J. H. Danner", "canonical_name": "Danner, J. H.", "given_names": "J. H.", "surname": "Danner", "position": "2nd Class Compositors", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 50, "salary_max": 60}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()