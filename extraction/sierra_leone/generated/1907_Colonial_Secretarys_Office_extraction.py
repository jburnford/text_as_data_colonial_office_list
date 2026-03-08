"""
Sierra Leone Colonial Office List 1907 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1907

OFFICIALS = [
    {"name": "G. B. Haddon Smith", "canonical_name": "Smith, G. B. Haddon", "given_names": "G. B.", "surname": "Smith", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 800, "salary_max": 800, "duty_allowance": 160, "honors": ["C.M.G."]},
    {"name": "E. E. Evelyn", "canonical_name": "Evelyn, E. E.", "given_names": "E. E.", "surname": "Evelyn", "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "A. Farrar", "canonical_name": "Farrar, A.", "given_names": "A.", "surname": "Farrar", "position": "2nd Asst. Col. Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "A. W. M. Nylander", "canonical_name": "Nylander, A. W. M.", "given_names": "A. W. M.", "surname": "Nylander", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "D. W. Carroll", "canonical_name": "Carroll, D. W.", "given_names": "D. W.", "surname": "Carroll", "position": "1st Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "2nd Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 115, "salary_max": 140},
    {"name": "Hadir-u-deen", "canonical_name": "Hadir-u-deen", "surname": "Hadir-u-deen", "position": "4th Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "C. Gilpin", "canonical_name": "Gilpin, C.", "given_names": "C.", "surname": "Gilpin", "position": "2nd Printer and Bookbinder", "department": "Printing Branch - Sierra Leone", "salary_min": 60, "salary_max": 85},
    {"name": "J. Mafoey", "canonical_name": "Mafoey, J.", "given_names": "J.", "surname": "Mafoey", "position": "1st Class Compositors", "department": "Printing Branch - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "C. E. Turner", "canonical_name": "Turner, C. E.", "given_names": "C. E.", "surname": "Turner", "position": "1st Class Compositors", "department": "Printing Branch - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "N. S. Thomas", "canonical_name": "Thomas, N. S.", "given_names": "N. S.", "surname": "Thomas", "position": "1st Class Compositors", "department": "Printing Branch - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "A. T. George", "canonical_name": "George, A. T.", "given_names": "A. T.", "surname": "George", "position": "2nd Class Compositors", "department": "Printing Branch - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "J. H. Danner", "canonical_name": "Danner, J. H.", "given_names": "J. H.", "surname": "Danner", "position": "2nd Class Compositors", "department": "Printing Branch - Sierra Leone", "salary_min": 30, "salary_max": 40}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()