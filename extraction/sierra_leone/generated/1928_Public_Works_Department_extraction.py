"""
Sierra Leone Colonial Office List 1928 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1928

OFFICIALS = [
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.Inst.C.E."], "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "A. S. Bradshaw", "canonical_name": "Bradshaw, A. S.", "given_names": "A. S.", "surname": "Bradshaw", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "allowances": "personal allowance 100l."},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Public Health Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E.", "F.S.I."], "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "B. W. Fitch-Jones", "canonical_name": "Fitch-Jones, B. W.", "given_names": "B. W.", "surname": "Fitch-Jones", "position": "Executive Engineer, Grade I", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.S.A."], "salary_min": 720, "salary_max": 920, "allowances": "allowance 72l."},
    {"name": "J. R. Gwyther", "canonical_name": "Gwyther, J. R.", "given_names": "J. R.", "surname": "Gwyther", "position": "Executive Engineer, Grade I", "department": "Public Works Department - Sierra Leone", "honors": ["M.C."], "qualifications": ["A.M.S.E."], "salary_min": 720, "salary_max": 920, "allowances": "allowance 72l."},
    {"name": "J. R. C. Tyler", "canonical_name": "Tyler, J. R. C.", "given_names": "J. R. C.", "surname": "Tyler", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "W. G. Tomlinson", "canonical_name": "Tomlinson, W. G.", "given_names": "W. G.", "surname": "Tomlinson", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["B.Eng."], "salary_min": 600, "salary_max": 920},
    {"name": "D. J. Brown", "canonical_name": "Brown, D. J.", "given_names": "D. J.", "surname": "Brown", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.I.M.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "C. J. Kemp Small", "canonical_name": "Small, C. J. Kemp", "given_names": "C. J. Kemp", "surname": "Small", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "J. H. C. Shakespear", "canonical_name": "Shakespear, J. H. C.", "given_names": "J. H. C.", "surname": "Shakespear", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "A. A. Clements", "canonical_name": "Clements, A. A.", "given_names": "A. A.", "surname": "Clements", "position": "Executive Engineer, Grade 3", "department": "Public Works Department - Sierra Leone", "qualifications": ["B.Sc.", "A.M.I.C.E."], "salary_scale": "C"},
    {"name": "A. W. Lindsey", "canonical_name": "Lindsey, A. W.", "given_names": "A. W.", "surname": "Lindsey", "position": "Executive Engineer, Grade 3", "department": "Public Works Department - Sierra Leone", "qualifications": ["B.A.", "B.A.I."], "salary_scale": "C"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Executive Engineer, Grade 3", "department": "Public Works Department - Sierra Leone", "salary_scale": "C"},
    {"name": "A. Archer-Betham", "canonical_name": "Archer-Betham, A.", "given_names": "A.", "surname": "Archer-Betham", "position": "Architect", "department": "Public Works Department - Sierra Leone", "qualifications": ["F.R.I.B.A."], "salary_min": 600, "salary_max": 600},
    {"name": "W. C. T. Rolls", "canonical_name": "Rolls, W. C. T.", "given_names": "W. C. T.", "surname": "Rolls", "position": "Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "allowances": "seniority allowance 72l. from 720l."},
    {"name": "B. L. Philips", "canonical_name": "Philips, B. L.", "given_names": "B. L.", "surname": "Philips", "position": "Deputy Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "T. V. Badger", "canonical_name": "Badger, T. V.", "given_names": "T. V.", "surname": "Badger", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Lawson", "canonical_name": "Lawson, J.", "given_names": "J.", "surname": "Lawson", "position": "Stock Verifier", "department": "Public Works Department - Sierra Leone", "salary_min": 400, "salary_max": 630},
    {"name": "E. G. Russell", "canonical_name": "Russell, E. G.", "given_names": "E. G.", "surname": "Russell", "position": "Building Inspector", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "F. H. Judd", "canonical_name": "Judd, F. H.", "given_names": "F. H.", "surname": "Judd", "position": "Electrical Engineer", "department": "Public Works Department - Sierra Leone", "salary_scale": "C"},
    {"name": "S. Shenton", "canonical_name": "Shenton, S.", "given_names": "S.", "surname": "Shenton", "position": "Assistant Electrical Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 720},
    {"name": "S. C. Benjamin", "canonical_name": "Benjamin, S. C.", "given_names": "S. C.", "surname": "Benjamin", "position": "African Assistant Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "M. B. Reader", "canonical_name": "Reader, M. B.", "given_names": "M. B.", "surname": "Reader", "position": "African Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "A. W. Spencer", "canonical_name": "Spencer, A. W.", "given_names": "A. W.", "surname": "Spencer", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 560, "salary_max": 600},
    {"name": "W. H. Brown", "canonical_name": "Brown, W. H.", "given_names": "W. H.", "surname": "Brown", "position": "Clerk of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 460, "salary_max": 560},
    {"name": "H. Flint", "canonical_name": "Flint, H.", "given_names": "H.", "surname": "Flint", "position": "Senior Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "S. Bennett", "canonical_name": "Bennett, S.", "given_names": "S.", "surname": "Bennett", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "G. A. Rimmer", "canonical_name": "Rimmer, G. A.", "given_names": "G. A.", "surname": "Rimmer", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. R. Bull", "canonical_name": "Bull, A. R.", "given_names": "A. R.", "surname": "Bull", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "J. F. Gigg", "canonical_name": "Gigg, J. F.", "given_names": "J. F.", "surname": "Gigg", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "R. C. Quin", "canonical_name": "Quin, R. C.", "given_names": "R. C.", "surname": "Quin", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "F. G. B. Mortimer", "canonical_name": "Mortimer, F. G. B.", "given_names": "F. G. B.", "surname": "Mortimer", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "C. J. R. Elms", "canonical_name": "Elms, C. J. R.", "given_names": "C. J. R.", "surname": "Elms", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "C. Carter", "canonical_name": "Carter, C.", "given_names": "C.", "surname": "Carter", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "P. M. Haste", "canonical_name": "Haste, P. M.", "given_names": "P. M.", "surname": "Haste", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "T. Walsh", "canonical_name": "Walsh, T.", "given_names": "T.", "surname": "Walsh", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "W. W. Wallace", "canonical_name": "Wallace, W. W.", "given_names": "W. W.", "surname": "Wallace", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. Moore", "canonical_name": "Moore, A.", "given_names": "A.", "surname": "Moore", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "J. Edminson", "canonical_name": "Edminson, J.", "given_names": "J.", "surname": "Edminson", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "E. F. Rhodes", "canonical_name": "Rhodes, E. F.", "given_names": "E. F.", "surname": "Rhodes", "position": "Mechanical Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "F. H. Bowden", "canonical_name": "Bowden, F. H.", "given_names": "F. H.", "surname": "Bowden", "position": "Roads Foreman", "department": "Public Works Department - Sierra Leone", "honors": ["O.B.E."], "salary_scale": "F"},
    {"name": "S. G. Farley", "canonical_name": "Farley, S. G.", "given_names": "S. G.", "surname": "Farley", "position": "Roads Foreman", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "W. G. Morgan", "canonical_name": "Morgan, W. G.", "given_names": "W. G.", "surname": "Morgan", "position": "Roads Foreman", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "T. Maloney", "canonical_name": "Maloney, T.", "given_names": "T.", "surname": "Maloney", "position": "Electrical Fitter", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "E. T. Macfoye", "canonical_name": "Macfoye, E. T.", "given_names": "E. T.", "surname": "Macfoye", "position": "Chief African Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. C. Jones", "canonical_name": "Jones, A. C.", "given_names": "A. C.", "surname": "Jones", "position": "Chief African Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "G. H. Porter", "canonical_name": "Porter, G. H.", "given_names": "G. H.", "surname": "Porter", "position": "Office Assistant", "department": "Public Works Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "J. T. D. Smith", "canonical_name": "Smith, J. T. D.", "given_names": "J. T. D.", "surname": "Smith", "position": "African Clerk, Grade 1", "department": "Public Works Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. A. Thompson", "canonical_name": "Thompson, A. A.", "given_names": "A. A.", "surname": "Thompson", "position": "African Clerk, Grade 1", "department": "Public Works Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()