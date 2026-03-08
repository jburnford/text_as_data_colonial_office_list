"""
Gold Coast Colonial Office List 1880 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1880

OFFICIALS = [
    {"name": "J. A. T. Buckle", "canonical_name": "Buckle, J. A. T.", "given_names": "J. A. T.", "surname": "Buckle",
     "position": "Auditor", "department": "Audit Office - Gold Coast", "salary_min": 700, "allowances": "Free quarters."},
    {"name": "E. W. Bruce", "canonical_name": "Bruce, E. W.", "given_names": "E. W.", "surname": "Bruce",
     "position": "Second Clerk", "department": "Audit Office - Gold Coast", "salary_min": 60},
    {"name": "D. Ashong", "canonical_name": "Ashong, D.", "given_names": "D.", "surname": "Ashong",
     "position": "Messenger", "department": "Audit Office - Gold Coast", "salary_min": 12},
    {"name": "E. R. Cole", "canonical_name": "Cole, E. R.", "given_names": "E. R.", "surname": "Cole",
     "position": "Postmaster", "department": "Post Office - Gold Coast", "location": "Accra", "salary_min": 150},
    {"name": "R. H. Woolley", "canonical_name": "Woolley, R. H.", "given_names": "R. H.", "surname": "Woolley",
     "position": "Clerk and Sorter", "department": "Post Office - Gold Coast", "salary_min": 30},
    {"name": "Joseph Dawson", "canonical_name": "Dawson, Joseph", "given_names": "Joseph", "surname": "Dawson",
     "position": "Messenger", "department": "Post Office - Gold Coast", "salary_min": 12},
    {"name": "E. J. da Costa", "canonical_name": "da Costa, E. J.", "given_names": "E. J.", "surname": "da Costa",
     "position": "Postmaster", "department": "Post Office - Gold Coast", "location": "Cape Coast", "salary_min": 60},
    {"name": "Nathaniel Thompson", "canonical_name": "Thompson, Nathaniel", "given_names": "Nathaniel", "surname": "Thompson",
     "position": "Clerk and Sorter", "department": "Post Office - Gold Coast", "salary_min": 40},
    {"name": "R. H. Blankson", "canonical_name": "Blankson, R. H.", "given_names": "R. H.", "surname": "Blankson",
     "position": "Assistant Clerk", "department": "Post Office - Gold Coast", "salary_min": 20},
    {"name": "Adolphus FitzJohn", "canonical_name": "FitzJohn, Adolphus", "given_names": "Adolphus", "surname": "FitzJohn",
     "position": "Postmaster", "department": "Post Office - Gold Coast", "location": "Quittah", "salary_min": 10},
    {"name": "S. S. Cole", "canonical_name": "Cole, S. S.", "given_names": "S. S.", "surname": "Cole",
     "position": "First Printer", "department": "Printing Office - Gold Coast", "salary_min": 150},
    {"name": "G. T. A. Thompson", "canonical_name": "Thompson, G. T. A.", "given_names": "G. T. A.", "surname": "Thompson",
     "position": "Second Printer", "department": "Printing Office - Gold Coast", "salary_min": 70},
    {"name": "J. B. Thomas", "canonical_name": "Thomas, J. B.", "given_names": "J. B.", "surname": "Thomas",
     "position": "Third Printer", "department": "Printing Office - Gold Coast", "salary_min": 45},
    {"name": "J. F. Smith", "canonical_name": "Smith, J. F.", "given_names": "J. F.", "surname": "Smith",
     "position": "Pressman", "department": "Printing Office - Gold Coast", "salary_min": 21},
    {"name": "J. T. Clegg", "canonical_name": "Clegg, J. T.", "given_names": "J. T.", "surname": "Clegg",
     "position": "Second Pressman", "department": "Printing Office - Gold Coast", "salary_min": 15},
    {"name": "G. A. Samuel", "canonical_name": "Samuel, G. A.", "given_names": "G. A.", "surname": "Samuel",
     "position": "Apprentice", "department": "Printing Office - Gold Coast", "salary_min": 12},
    {"name": "Charles Hill", "canonical_name": "Hill, Charles", "given_names": "Charles", "surname": "Hill",
     "position": "Second Apprentice", "department": "Printing Office - Gold Coast", "salary_min": 12},
    {"name": "Quamina Agill", "canonical_name": "Agill, Quamina", "given_names": "Quamina", "surname": "Agill",
     "position": "Bookbinder", "department": "Printing Office - Gold Coast", "salary_min": 26},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()