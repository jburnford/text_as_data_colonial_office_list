"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.Inst. C.E."], "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Deputy Director of Public Works", "department": "Public Works Department - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "B. W. Fitton Jones", "canonical_name": "Jones, B. W. Fitton", "given_names": "B. W. Fitton", "surname": "Jones", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "qualifications": ["F.R.I.B.A."], "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Public Health Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E.", "F.S.I."], "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Provincial Engineer", "department": "Public Works Department - Sierra Leone", "honors": ["M.C."], "qualifications": ["M.Inst. Struct. E.", "A.M.S.E."], "salary_min": 720, "salary_max": 920, "allowances": "72l."},
    {"name": "J. R. C. Tyler", "canonical_name": "Tyler, J. R. C.", "given_names": "J. R. C.", "surname": "Tyler", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "W. G. Tomlinson", "canonical_name": "Tomlinson, W. G.", "given_names": "W. G.", "surname": "Tomlinson", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["B.Eng."], "salary_min": 600, "salary_max": 920},
    {"name": "D. J. Brown", "canonical_name": "Brown, D. J.", "given_names": "D. J.", "surname": "Brown", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.I.M.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "C. J. Kemp Small", "canonical_name": "Small, C. J. Kemp", "given_names": "C. J. Kemp", "surname": "Small", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "J. H. C. Shakespear", "canonical_name": "Shakespear, J. H. C.", "given_names": "J. H. C.", "surname": "Shakespear", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "H. C. King", "canonical_name": "King, H. C.", "given_names": "H. C.", "surname": "King", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "W. L. Thompson", "canonical_name": "Thompson, W. L.", "given_names": "W. L.", "surname": "Thompson", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "P. M. Cran", "canonical_name": "Cran, P. M.", "given_names": "P. M.", "surname": "Cran", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "honors": ["O.B.E."], "qualifications": ["B.Sc.", "A.M.I.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Executive Engineers, Grade 3", "department": "Public Works Department - Sierra Leone", "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Executive Engineers, Grade 3", "department": "Public Works Department - Sierra Leone", "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Executive Engineers, Grade 3", "department": "Public Works Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. Archer-Betham", "canonical_name": "Archer-Betham, A.", "given_names": "A.", "surname": "Archer-Betham", "position": "Architect", "department": "Public Works Department - Sierra Leone", "qualifications": ["F.R.I.B.A."], "salary_min": 600, "salary_max": 600},
    {"name": "J. Stevenson", "canonical_name": "Stevenson, J.", "given_names": "J.", "surname": "Stevenson", "position": "Quantity Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 540, "salary_max": 720},
    {"name": "W. C. T. Rolls", "canonical_name": "Rolls, W. C. T.", "given_names": "W. C. T.", "surname": "Rolls", "position": "Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "allowances": "seniority allowance 72l. from 720l."},
    {"name": "B. L. Philips", "canonical_name": "Philips, B. L.", "given_names": "B. L.", "surname": "Philips", "position": "Deputy Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "T. V. Badger", "canonical_name": "Badger, T. V.", "given_names": "T. V.", "surname": "Badger", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Lawson", "canonical_name": "Lawson, J.", "given_names": "J.", "surname": "Lawson", "position": "Stock Verifier", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 600},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Building Inspector", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "G. R. Bain", "canonical_name": "Bain, G. R.", "given_names": "G. R.", "surname": "Bain", "position": "Chief Electrical Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920, "allowances": "seniority allowance of 72l. from 720l."},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Electrical Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "A. B. Smith", "canonical_name": "Smith, A. B.", "given_names": "A. B.", "surname": "Smith", "position": "Cable Joiner", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 500},
    {"name": "S. C. Benjamin", "canonical_name": "Benjamin, S. C.", "given_names": "S. C.", "surname": "Benjamin", "position": "African Assistant Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "M. B. Reader", "canonical_name": "Reader, M. B.", "given_names": "M. B.", "surname": "Reader", "position": "African Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "A. W. Spencer", "canonical_name": "Spencer, A. W.", "given_names": "A. W.", "surname": "Spencer", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 560, "salary_max": 600},
    {"name": "W. H. Brown", "canonical_name": "Brown, W. H.", "given_names": "W. H.", "surname": "Brown", "position": "Clerk of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 460, "salary_max": 560},
    {"name": "H. Flint", "canonical_name": "Flint, H.", "given_names": "H.", "surname": "Flint", "position": "Senior Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "S. Bennett", "canonical_name": "Bennett, S.", "given_names": "S.", "surname": "Bennett", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "G. A. Rimmer", "canonical_name": "Rimmer, G. A.", "given_names": "G. A.", "surname": "Rimmer", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. R. Bull", "canonical_name": "Bull, A. R.", "given_names": "A. R.", "surname": "Bull", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "J. F. Gigg", "canonical_name": "Gigg, J. F.", "given_names": "J. F.", "surname": "Gigg", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "R. C. Quin", "canonical_name": "Quin, R. C.", "given_names": "R. C.", "surname": "Quin", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "C. J. R. Elms", "canonical_name": "Elms, C. J. R.", "given_names": "C. J. R.", "surname": "Elms", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "C. Carter", "canonical_name": "Carter, C.", "given_names": "C.", "surname": "Carter", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "T. Walsh", "canonical_name": "Walsh, T.", "given_names": "T.", "surname": "Walsh", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "W. W. Wallace", "canonical_name": "Wallace, W. W.", "given_names": "W. W.", "surname": "Wallace", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. Moore", "canonical_name": "Moore, A.", "given_names": "A.", "surname": "Moore", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "J. Edminson", "canonical_name": "Edminson, J.", "given_names": "J.", "surname": "Edminson", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "H. Matthews", "canonical_name": "Matthews, H.", "given_names": "H.", "surname": "Matthews", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "F. A. E. Beer", "canonical_name": "Beer, F. A. E.", "given_names": "F. A. E.", "surname": "Beer", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "J. D. Galloway", "canonical_name": "Galloway, J. D.", "given_names": "J. D.", "surname": "Galloway", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. C. Woods", "canonical_name": "Woods, A. C.", "given_names": "A. C.", "surname": "Woods", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. O'Neil", "canonical_name": "O'Neil, A.", "given_names": "A.", "surname": "O'Neil", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "W. G. Mortimore", "canonical_name": "Mortimore, W. G.", "given_names": "W. G.", "surname": "Mortimore", "position": "Foremen of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "E. F. Rhodes", "canonical_name": "Rhodes, E. F.", "given_names": "E. F.", "surname": "Rhodes", "position": "Mechanical Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 660},
    {"name": "F. H. Bawden", "canonical_name": "Bawden, F. H.", "given_names": "F. H.", "surname": "Bawden", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "honors": ["O.B.E."], "salary_scale": "F"},
    {"name": "S. G. Farley", "canonical_name": "Farley, S. G.", "given_names": "S. G.", "surname": "Farley", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "W. G. Morgan", "canonical_name": "Morgan, W. G.", "given_names": "W. G.", "surname": "Morgan", "position": "Roads Foremen", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "T. Maloney", "canonical_name": "Maloney, T.", "given_names": "T.", "surname": "Maloney", "position": "Electrical Fitters", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "F. H. Berry", "canonical_name": "Berry, F. H.", "given_names": "F. H.", "surname": "Berry", "position": "Electrical Fitters", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "G. M. D. H. Elliott", "canonical_name": "Elliott, G. M. D. H.", "given_names": "G. M. D. H.", "surname": "Elliott", "position": "Wireman", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "E. T. Macfoye", "canonical_name": "Macfoye, E. T.", "given_names": "E. T.", "surname": "Macfoye", "position": "Chief African Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. C. Jones", "canonical_name": "Jones, A. C.", "given_names": "A. C.", "surname": "Jones", "position": "Chief African Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "Office Assistant", "department": "Public Works Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "A. A. Thompson", "canonical_name": "Thompson, A. A.", "given_names": "A. A.", "surname": "Thompson", "position": "African Clerks, Grade 1", "department": "Public Works Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. P. Harleston", "canonical_name": "Harleston, A. P.", "given_names": "A. P.", "surname": "Harleston", "position": "African Clerks, Grade 1", "department": "Public Works Department - Sierra Leone", "salary_min": 210, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()