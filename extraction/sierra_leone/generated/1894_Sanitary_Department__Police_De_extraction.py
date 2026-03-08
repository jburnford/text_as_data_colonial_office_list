"""
Sierra Leone Colonial Office List 1894 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1894

OFFICIALS = [
    {"name": "The Colonial Surgeon", "canonical_name": "Colonial Surgeon, The", "surname": "Colonial Surgeon", "position": "Inspector of Health", "department": "Sanitary Department - Sierra Leone"},
    {"name": "T. M. Cole", "canonical_name": "Cole, T. M.", "given_names": "T. M.", "surname": "Cole", "position": "Clerk", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "A. F. Tarbet", "canonical_name": "Tarbet, A. F.", "given_names": "A. F.", "surname": "Tarbet", "position": "Inspector-General of Police", "department": "Police Department - Sierra Leone", "salary_min": 400, "salary_max": 400, "allowances": "91l. 5s."},
    {"name": "A. D. Campbell", "canonical_name": "Campbell, A. D.", "given_names": "A. D.", "surname": "Campbell", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l. allowance", "military_rank": "Capt."},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l. allowance"},
    {"name": "N. H. Sawyer", "canonical_name": "Sawyer, N. H.", "given_names": "N. H.", "surname": "Sawyer", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "C. N. Taylor", "canonical_name": "Taylor, C. N.", "given_names": "C. N.", "surname": "Taylor", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "J. B. Johnson", "canonical_name": "Johnson, J. B.", "given_names": "J. B.", "surname": "Johnson", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "J. H. Jones", "canonical_name": "Jones, J. H.", "given_names": "J. H.", "surname": "Jones", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "D. P. H. Crowther", "canonical_name": "Crowther, D. P. H.", "given_names": "D. P. H.", "surname": "Crowther", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "J. O'Connor", "canonical_name": "O'Connor, J.", "given_names": "J.", "surname": "O'Connor", "position": "Keeper of Freetown Gaol", "department": "Gaol Department - Sierra Leone", "salary_min": 250, "salary_max": 250},
    {"name": "R. A. George", "canonical_name": "George, R. A.", "given_names": "R. A.", "surname": "George", "position": "Under Gaoler", "department": "Gaol Department - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "Mary E. Wilson", "canonical_name": "Wilson, Mary E.", "given_names": "Mary E.", "surname": "Wilson", "position": "Mulron", "department": "Gaol Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "Rachel Macauley", "canonical_name": "Macauley, Rachel", "given_names": "Rachel", "surname": "Macauley", "position": "Under ditto", "department": "Gaol Department - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "S. W. Adams", "canonical_name": "Adams, S. W.", "given_names": "S. W.", "surname": "Adams", "position": "Gaoler at Sherboro", "department": "Gaol Department - Sierra Leone", "salary_min": 73, "salary_max": 73},
    {"name": "W. M. Huggins", "canonical_name": "Huggins, W. M.", "given_names": "W. M.", "surname": "Huggins", "position": "D. Commissioner", "department": "Eastern District - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l. 5s."},
    {"name": "J. B. M'Cormack", "canonical_name": "M'Cormack, J. B.", "given_names": "J. B.", "surname": "M'Cormack", "position": "Clerk", "department": "Eastern District - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "the D. Commissioner", "canonical_name": "Commissioner, The D.", "given_names": "The D.", "surname": "Commissioner", "position": "Coroner", "department": "Eastern District - Sierra Leone", "salary_min": 20, "salary_max": 20}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()