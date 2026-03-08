"""
Sierra Leone Colonial Office List 1927 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1927

OFFICIALS = [
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "qualifications": ["M. Inst. C.E."], "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "A. S. Bradshaw", "canonical_name": "Bradshaw, A. S.", "given_names": "A. S.", "surname": "Bradshaw", "position": "Assistant ditto", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "allowances": "personal allowance 100l."},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Public Health Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E.", "F.S.I."], "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "location": "Ireland"},
    {"name": "G. Stanley", "canonical_name": "Stanley, G.", "given_names": "G.", "surname": "Stanley", "position": "Executive Engineer, Grade I", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 720, "salary_max": 920, "allowances": "allowance 72l."},
    {"name": "B. W. Fitch-Jones", "canonical_name": "Fitch-Jones, B. W.", "given_names": "B. W.", "surname": "Fitch-Jones", "position": "Executive Engineer, Grade I", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.S.A."], "salary_min": 720, "salary_max": 920, "allowances": "allowance 72l."},
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Executive Engineer, Grade I", "department": "Public Works Department - Sierra Leone", "honors": ["M.C."], "qualifications": ["A.M.S.E."], "salary_min": 720, "salary_max": 920, "allowances": "allowance 72l."},
    {"name": "J. R. C. Tyler", "canonical_name": "Tyler, J. R. C.", "given_names": "J. R. C.", "surname": "Tyler", "position": "Executive Engineers, Grade 3", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.Inst.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "W. C. Tomlinson", "canonical_name": "Tomlinson, W. C.", "given_names": "W. C.", "surname": "Tomlinson", "position": "Executive Engineers, Grade 3", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "A. A. Clements", "canonical_name": "Clements, A. A.", "given_names": "A. A.", "surname": "Clements", "position": "Executive Engineers, Grade 3", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.R.S.I."], "salary_min": 480, "salary_max": 720, "salary_scale": "C"},
    {"name": "A. W. Lindsay", "canonical_name": "Lindsay, A. W.", "given_names": "A. W.", "surname": "Lindsay", "position": "Executive Engineers, Grade 3", "department": "Public Works Department - Sierra Leone", "qualifications": ["B.A.I."], "salary_min": 480, "salary_max": 720, "salary_scale": "C"},
    {"name": "D. J. Brown", "canonical_name": "Brown, D. J.", "given_names": "D. J.", "surname": "Brown", "position": "Executive Engineers, Grade 3", "department": "Public Works Department - Sierra Leone", "salary_min": 540, "salary_max": 920},
    {"name": "A. Archer-Betham", "canonical_name": "Archer-Betham, A.", "given_names": "A.", "surname": "Archer-Betham", "position": "Architect", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.", "F.R.I.B.A."], "salary_min": 600, "salary_max": 600},
    {"name": "W. C. T. Rolls", "canonical_name": "Rolls, W. C. T.", "given_names": "W. C. T.", "surname": "Rolls", "position": "Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "allowances": "seniority allowance 72l. after 720l."},
    {"name": "B. L. Philips", "canonical_name": "Philips, B. L.", "given_names": "B. L.", "surname": "Philips", "position": "Deputy Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A", "salary_max": 720},
    {"name": "T. V. Badger", "canonical_name": "Badger, T. V.", "given_names": "T. V.", "surname": "Badger", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A", "salary_max": 600},
    {"name": "F. H. Judd", "canonical_name": "Judd, F. H.", "given_names": "F. H.", "surname": "Judd", "position": "Electrical Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "S. C. Benjamin", "canonical_name": "Benjamin, S. C.", "given_names": "S. C.", "surname": "Benjamin", "position": "African Assistant Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "M. B. Reader", "canonical_name": "Reader, M. B.", "given_names": "M. B.", "surname": "Reader", "position": "African Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "A. W. Spencer", "canonical_name": "Spencer, A. W.", "given_names": "A. W.", "surname": "Spencer", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 560, "salary_max": 600},
    {"name": "W. H. Brown", "canonical_name": "Brown, W. H.", "given_names": "W. H.", "surname": "Brown", "position": "Clerk of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 460, "salary_max": 560},
    {"name": "F. O'Doherty", "canonical_name": "O'Doherty, F.", "given_names": "F.", "surname": "O'Doherty", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "salary_scale": "F"},
    {"name": "S. Bennett", "canonical_name": "Bennett, S.", "given_names": "S.", "surname": "Bennett", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "salary_scale": "F"},
    {"name": "G. A. Rimmer", "canonical_name": "Rimmer, G. A.", "given_names": "G. A.", "surname": "Rimmer", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "salary_scale": "F"},
    {"name": "A. R. Bull", "canonical_name": "Bull, A. R.", "given_names": "A. R.", "surname": "Bull", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "salary_scale": "F"},
    {"name": "J. Eliminson", "canonical_name": "Eliminson, J.", "given_names": "J.", "surname": "Eliminson", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "salary_scale": "F"},
    {"name": "E. F. Rhodes", "canonical_name": "Rhodes, E. F.", "given_names": "E. F.", "surname": "Rhodes", "position": "Mechanical Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560, "salary_scale": "F"},
    {"name": "F. H. Bawden", "canonical_name": "Bawden, F. H.", "given_names": "F. H.", "surname": "Bawden", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "honors": ["O.B.E."], "salary_min": 400, "salary_max": 500, "salary_scale": "F"},
    {"name": "S. G. Farley", "canonical_name": "Farley, S. G.", "given_names": "S. G.", "surname": "Farley", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "salary_scale": "F"},
    {"name": "W. J. Morgan", "canonical_name": "Morgan, W. J.", "given_names": "W. J.", "surname": "Morgan", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "salary_scale": "F"},
    {"name": "S. Shenton", "canonical_name": "Shenton, S.", "given_names": "S.", "surname": "Shenton", "position": "Cable Joiner", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "E. T. Macfoye", "canonical_name": "Macfoye, E. T.", "given_names": "E. T.", "surname": "Macfoye", "position": "Chief African Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. C. Jones", "canonical_name": "Jones, A. C.", "given_names": "A. C.", "surname": "Jones", "position": "Chief African Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "Office Assistant", "department": "Public Works Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "African Clerk, Grade I", "department": "Public Works Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. A. Thompson", "canonical_name": "Thompson, A. A.", "given_names": "A. A.", "surname": "Thompson", "position": "African Clerk, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 160, "salary_max": 200},
    {"name": "F. E. Garnon", "canonical_name": "Garnon, F. E.", "given_names": "F. E.", "surname": "Garnon", "position": "African Clerk, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 160, "salary_max": 200}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()