"""
Sierra Leone Colonial Office List 1939 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1939

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Assistant Postmaster General and Accountant", "department": "Post Office - Sierra Leone", "salary_min": 360, "salary_max": 600},
    {"name": "E. S. B. Francis", "canonical_name": "Francis, E. S. B.", "given_names": "E. S. B.", "surname": "Francis", "position": "Staff Superintendent", "department": "Post Office - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "F. J. Martin", "canonical_name": "Martin, F. J.", "given_names": "F. J.", "surname": "Martin", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "qualifications": ["M.A.", "Ph.D.", "F.I.C."], "duty_allowance": 210},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Entomologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 450, "salary_max": 840},
    {"name": "F. C. Deighton", "canonical_name": "Deighton, F. C.", "given_names": "F. C.", "surname": "Deighton", "position": "Plant Pathologist", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "J. W. D. Fisher", "canonical_name": "Fisher, J. W. D.", "given_names": "J. W. D.", "surname": "Fisher", "position": "Senior Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "R. R. Glanville", "canonical_name": "Glanville, R. R.", "given_names": "R. R.", "surname": "Glanville", "position": "Senior Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "honors": ["M.B.E."], "salary_scale": "C"},
    {"name": "E. I. Nisbet", "canonical_name": "Nisbet, E. I.", "given_names": "E. I.", "surname": "Nisbet", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "G. M. Roddan", "canonical_name": "Roddan, G. M.", "given_names": "G. M.", "surname": "Roddan", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "E. S. Garner", "canonical_name": "Garner, E. S.", "given_names": "E. S.", "surname": "Garner", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. F. MacKenzie", "canonical_name": "MacKenzie, A. F.", "given_names": "A. F.", "surname": "MacKenzie", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_scale": "C"},
    {"name": "H. Machuskie", "canonical_name": "Machuskie, H.", "given_names": "H.", "surname": "Machuskie", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_min": 450, "salary_max": 840},
    {"name": "J. D. Gillespie", "canonical_name": "Gillespie, J. D.", "given_names": "J. D.", "surname": "Gillespie", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_min": 450, "salary_max": 840},
    {"name": "M. J. Douglas", "canonical_name": "Douglas, M. J.", "given_names": "M. J.", "surname": "Douglas", "position": "Agricultural Officer", "department": "Agricultural Department - Sierra Leone", "salary_min": 450, "salary_max": 840},
    {"name": "S. A. Roach", "canonical_name": "Roach, S. A.", "given_names": "S. A.", "surname": "Roach", "position": "Live Stock Officer", "department": "Agricultural Department - Sierra Leone", "salary_min": 450, "salary_max": 690},
    {"name": "F. W. B. Allinson", "canonical_name": "Allinson, F. W. B.", "given_names": "F. W. B.", "surname": "Allinson", "position": "Inspector of Plants and Produce", "department": "Agricultural Department - Sierra Leone", "salary_min": 400, "salary_max": 690}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()