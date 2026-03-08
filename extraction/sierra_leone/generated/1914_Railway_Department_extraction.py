"""
Sierra Leone Colonial Office List 1914 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1914

OFFICIALS = [
    {"name": "H. C. Morcom", "canonical_name": "Morcom, H. C.", "given_names": "H. C.", "surname": "Morcom", "position": "General Manager", "department": "Railway Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "R. W. Espeut", "canonical_name": "Espeut, R. W.", "given_names": "R. W.", "surname": "Espeut", "position": "Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 450, "salary_max": 500, "duty_allowance": 100},
    {"name": "E. D. Willoughby", "canonical_name": "Willoughby, E. D.", "given_names": "E. D.", "surname": "Willoughby", "position": "Senior Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "A. H. Salt", "canonical_name": "Salt, A. H.", "given_names": "A. H.", "surname": "Salt", "position": "Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "R. M. Johnston", "canonical_name": "Johnston, R. M.", "given_names": "R. M.", "surname": "Johnston", "position": "Junior Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "H. D. Schneider", "canonical_name": "Schneider, H. D.", "given_names": "H. D.", "surname": "Schneider", "position": "Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "L. C. E. Hammett", "canonical_name": "Hammett, L. C. E.", "given_names": "L. C. E.", "surname": "Hammett", "position": "Assistant Maintenance Engineer", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "S. Renshaw", "canonical_name": "Renshaw, S.", "given_names": "S.", "surname": "Renshaw", "position": "Chief Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "E. G. Barker", "canonical_name": "Barker, E. G.", "given_names": "E. G.", "surname": "Barker", "position": "Locomotive Superintendent", "department": "Railway Department - Sierra Leone", "salary_min": 550, "salary_max": 550, "duty_allowance": 110},
    {"name": "R. L. Hunt", "canonical_name": "Hunt, R. L.", "given_names": "R. L.", "surname": "Hunt", "position": "Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "A. E. Munn", "canonical_name": "Munn, A. E.", "given_names": "A. E.", "surname": "Munn", "position": "Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "A. J. E. Deacon", "canonical_name": "Deacon, A. J. E.", "given_names": "A. J. E.", "surname": "Deacon", "position": "Assistant Accountant", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 350},
    {"name": "J. D. Martin", "canonical_name": "Martin, J. D.", "given_names": "J. D.", "surname": "Martin", "position": "Traffic Manager", "department": "Railway Department - Sierra Leone", "salary_min": 500, "salary_max": 600, "duty_allowance": 100},
    {"name": "A. J. Cullen", "canonical_name": "Cullen, A. J.", "given_names": "A. J.", "surname": "Cullen", "position": "Traffic Officer, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. T. Tillotson", "canonical_name": "Tillotson, J. T.", "given_names": "J. T.", "surname": "Tillotson", "position": "Traffic Officer, 1st Grade", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "W. Pearson", "canonical_name": "Pearson, W.", "given_names": "W.", "surname": "Pearson", "position": "Traffic Officer, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_min": 225, "salary_max": 245},
    {"name": "H. C. F. Fisher", "canonical_name": "Fisher, H. C. F.", "given_names": "H. C. F.", "surname": "Fisher", "position": "Traffic Officer, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_min": 225, "salary_max": 245},
    {"name": "H. McPhee", "canonical_name": "McPhee, H.", "given_names": "H.", "surname": "McPhee", "position": "Traffic Officer, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_min": 225, "salary_max": 245},
    {"name": "J. P. Ison", "canonical_name": "Ison, J. P.", "given_names": "J. P.", "surname": "Ison", "position": "Traffic Officer, 2nd Grade", "department": "Railway Department - Sierra Leone", "salary_min": 225, "salary_max": 245},
    {"name": "J. B. Sidney", "canonical_name": "Sidney, J. B.", "given_names": "J. B.", "surname": "Sidney", "position": "Clerical Assistant", "department": "Railway Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "S. A. Macauley", "canonical_name": "Macauley, S. A.", "given_names": "S. A.", "surname": "Macauley", "position": "Chief Clerk", "department": "Railway Department - Sierra Leone", "salary_min": 120, "salary_max": 150},
    {"name": "P. Nicolls", "canonical_name": "Nicolls, P.", "given_names": "P.", "surname": "Nicolls", "position": "Traffic Supervisor and Travelling Inspector of Accounts", "department": "Railway Department - Sierra Leone", "salary_min": 300, "salary_max": 300},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()