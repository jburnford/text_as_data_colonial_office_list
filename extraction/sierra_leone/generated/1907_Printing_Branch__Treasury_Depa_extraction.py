"""
Sierra Leone Colonial Office List 1907 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1907

OFFICIALS = [
    {"name": "G. T. Parker", "canonical_name": "Parker, G. T.", "given_names": "G. T.", "surname": "Parker", "position": "Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "C. Gilpin", "canonical_name": "Gilpin, C.", "given_names": "C.", "surname": "Gilpin", "position": "2nd Printer and Bookbinder", "department": "Printing Branch - Sierra Leone", "salary_min": 60, "salary_max": 85},
    {"name": "J. Mafoey", "canonical_name": "Mafoey, J.", "given_names": "J.", "surname": "Mafoey", "position": "1st Class Compositors", "department": "Printing Branch - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "C. E. Turner", "canonical_name": "Turner, C. E.", "given_names": "C. E.", "surname": "Turner", "position": "1st Class Compositors", "department": "Printing Branch - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "N. S. Thomas", "canonical_name": "Thomas, N. S.", "given_names": "N. S.", "surname": "Thomas", "position": "1st Class Compositors", "department": "Printing Branch - Sierra Leone", "salary_min": 40, "salary_max": 50},
    {"name": "A. T. George", "canonical_name": "George, A. T.", "given_names": "A. T.", "surname": "George", "position": "2nd Class Compositors", "department": "Printing Branch - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "J. H. Danner", "canonical_name": "Danner, J. H.", "given_names": "J. H.", "surname": "Danner", "position": "2nd Class Compositors", "department": "Printing Branch - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "E. O. Johnson", "canonical_name": "Johnson, E. O.", "given_names": "E. O.", "surname": "Johnson", "position": "Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 500, "salary_max": 700},
    {"name": "S. Renshaw", "canonical_name": "Renshaw, S.", "given_names": "S.", "surname": "Renshaw", "position": "Assistant Colonial Treasurer", "department": "Treasury Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "J. N. Edwin", "canonical_name": "Edwin, J. N.", "given_names": "J. N.", "surname": "Edwin", "position": "Chief Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 180, "salary_max": 220},
    {"name": "A. G. Johnson", "canonical_name": "Johnson, A. G.", "given_names": "A. G.", "surname": "Johnson", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "W. B. Gilpin", "canonical_name": "Gilpin, W. B.", "given_names": "W. B.", "surname": "Gilpin", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "J. H. Kelson", "canonical_name": "Kelson, J. H.", "given_names": "J. H.", "surname": "Kelson", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 65, "salary_max": 80},
    {"name": "J. F. Knox", "canonical_name": "Knox, J. F.", "given_names": "J. F.", "surname": "Knox", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 45, "salary_max": 55},
    {"name": "G. P. Bull", "canonical_name": "Bull, G. P.", "given_names": "G. P.", "surname": "Bull", "position": "5th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 35, "salary_max": 45},
    {"name": "E. G. Taylor", "canonical_name": "Taylor, E. G.", "given_names": "E. G.", "surname": "Taylor", "position": "1st Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 100, "salary_max": 120},
    {"name": "S. Benjamin", "canonical_name": "Benjamin, S.", "given_names": "S.", "surname": "Benjamin", "position": "2nd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 70, "salary_max": 90},
    {"name": "C. J. Elba", "canonical_name": "Elba, C. J.", "given_names": "C. J.", "surname": "Elba", "position": "3rd Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 50, "salary_max": 60},
    {"name": "W. S. Zizer", "canonical_name": "Zizer, W. S.", "given_names": "W. S.", "surname": "Zizer", "position": "4th Clerk", "department": "Treasury Department - Sierra Leone", "salary_min": 30, "salary_max": 40},
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "Harbour Master", "department": "Port and Marine Department - Sierra Leone", "salary_min": 200, "salary_max": 250},
    {"name": "R. Moses", "canonical_name": "Moses, R.", "given_names": "R.", "surname": "Moses", "position": "Clerk", "department": "Port and Marine Department - Sierra Leone", "salary_min": 40, "salary_max": 60}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()