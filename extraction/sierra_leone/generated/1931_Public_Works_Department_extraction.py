"""
Sierra Leone Colonial Office List 1931 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1931

OFFICIALS = [
    {"name": "W. S. Lake", "canonical_name": "Lake, W. S.", "given_names": "W. S.", "surname": "Lake", "position": "Director of Public Works", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.Inst. C.E."], "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "C. Wilson Brown", "canonical_name": "Brown, C. Wilson", "given_names": "C. Wilson", "surname": "Brown", "position": "Deputy Director of Public Works", "department": "Public Works Department - Sierra Leone", "military_rank": "Capt.", "honors": ["M.C."], "qualifications": ["A.R.T.C.", "F.R.G.S.", "A.M.I.C.E."], "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "B. W. Fitch Jones", "canonical_name": "Jones, B. W. Fitch", "given_names": "B. W. Fitch", "surname": "Jones", "position": "Assistant Director of Public Works", "department": "Public Works Department - Sierra Leone", "qualifications": ["F.R.I.B.A."], "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "O. G. Price", "canonical_name": "Price, O. G.", "given_names": "O. G.", "surname": "Price", "position": "Public Health Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E.", "F.S.I."], "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "J. R. C. Tyler", "canonical_name": "Tyler, J. R. C.", "given_names": "J. R. C.", "surname": "Tyler", "position": "Provincial Engineer", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 720, "salary_max": 920, "allowances": "72L"},
    {"name": "W. G. Tomlinson", "canonical_name": "Tomlinson, W. G.", "given_names": "W. G.", "surname": "Tomlinson", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["B.Eng."], "salary_min": 600, "salary_max": 920},
    {"name": "D. J. Brown", "canonical_name": "Brown, D. J.", "given_names": "D. J.", "surname": "Brown", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["M.I.M.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "J. H. C. Shakespear", "canonical_name": "Shakespear, J. H. C.", "given_names": "J. H. C.", "surname": "Shakespear", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "H. C. King", "canonical_name": "King, H. C.", "given_names": "H. C.", "surname": "King", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["A.M.I.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "W. L. Thompson", "canonical_name": "Thompson, W. L.", "given_names": "W. L.", "surname": "Thompson", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "qualifications": ["C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "P. M. Cran", "canonical_name": "Cran, P. M.", "given_names": "P. M.", "surname": "Cran", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "honors": ["O.B.E."], "qualifications": ["B.Sc.", "A.M.I.C.E."], "salary_min": 600, "salary_max": 920},
    {"name": "T. W. McLeod", "canonical_name": "McLeod, T. W.", "given_names": "T. W.", "surname": "McLeod", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "A. R. Smee", "canonical_name": "Smee, A. R.", "given_names": "A. R.", "surname": "Smee", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "W. H. Jackson", "canonical_name": "Jackson, W. H.", "given_names": "W. H.", "surname": "Jackson", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "A. S. Elliott", "canonical_name": "Elliott, A. S.", "given_names": "A. S.", "surname": "Elliott", "position": "Executive Engineer, Grade 2", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 920},
    {"name": "J. Stevenson", "canonical_name": "Stevenson, J.", "given_names": "J.", "surname": "Stevenson", "position": "Quantity Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 510, "salary_max": 720},
    {"name": "W. C. T. Rolls", "canonical_name": "Rolls, W. C. T.", "given_names": "W. C. T.", "surname": "Rolls", "position": "Chief Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 800, "duty_allowance": 72},
    {"name": "B. L. Phillips", "canonical_name": "Phillips, B. L.", "given_names": "B. L.", "surname": "Phillips", "position": "Deputy Chief Accountant", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "T. V. Badger", "canonical_name": "Badger, T. V.", "given_names": "T. V.", "surname": "Badger", "position": "Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A", "duty_allowance": 50},
    {"name": "F. E. Wells", "canonical_name": "Wells, F. E.", "given_names": "F. E.", "surname": "Wells", "position": "Assistant Accountant and Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Lawson", "canonical_name": "Lawson, J.", "given_names": "J.", "surname": "Lawson", "position": "Stock Verifier", "department": "Public Works Department - Sierra Leone", "salary_scale": "A"},
    {"name": "W. E. Concom", "canonical_name": "Concom, W. E.", "given_names": "W. E.", "surname": "Concom", "position": "Building Inspector", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "G. N. Watts", "canonical_name": "Watts, G. N.", "given_names": "G. N.", "surname": "Watts", "position": "Assistant Electrical Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "H. Watkin", "canonical_name": "Watkin, H.", "given_names": "H.", "surname": "Watkin", "position": "Assistant Electrical Engineer", "department": "Public Works Department - Sierra Leone", "salary_min": 600, "salary_max": 720},
    {"name": "L. P. John", "canonical_name": "John, L. P.", "given_names": "L. P.", "surname": "John", "position": "Assistant Accountant, Electricity Sub-Department", "department": "Public Works Department - Sierra Leone", "salary_min": 450, "salary_max": 720},
    {"name": "S. C. Benjamin", "canonical_name": "Benjamin, S. C.", "given_names": "S. C.", "surname": "Benjamin", "position": "African Assistant Accountant", "department": "Public Works Department - Sierra Leone", "salary_min": 360, "salary_max": 450},
    {"name": "A. E. Laverse", "canonical_name": "Laverse, A. E.", "given_names": "A. E.", "surname": "Laverse", "position": "African Assistant Storekeeper", "department": "Public Works Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "A. W. Spencer", "canonical_name": "Spencer, A. W.", "given_names": "A. W.", "surname": "Spencer", "position": "Inspector of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 560, "salary_max": 600},
    {"name": "F. H. Bawden", "canonical_name": "Bawden, F. H.", "given_names": "F. H.", "surname": "Bawden", "position": "Senior Foreman of Works", "department": "Public Works Department - Sierra Leone", "honors": ["O.B.E."], "salary_min": 500, "salary_max": 560},
    {"name": "H. Flint", "canonical_name": "Flint, H.", "given_names": "H.", "surname": "Flint", "position": "Senior Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "W. H. Brown", "canonical_name": "Brown, W. H.", "given_names": "W. H.", "surname": "Brown", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "W. J. Morgan", "canonical_name": "Morgan, W. J.", "given_names": "W. J.", "surname": "Morgan", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "S. Bennett", "canonical_name": "Bennett, S.", "given_names": "S.", "surname": "Bennett", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "G. A. Rimmer", "canonical_name": "Rimmer, G. A.", "given_names": "G. A.", "surname": "Rimmer", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. R. Bull", "canonical_name": "Bull, A. R.", "given_names": "A. R.", "surname": "Bull", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "J. F. Gigg", "canonical_name": "Gigg, J. F.", "given_names": "J. F.", "surname": "Gigg", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "R. C. Quin", "canonical_name": "Quin, R. C.", "given_names": "R. C.", "surname": "Quin", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "C. Carter", "canonical_name": "Carter, C.", "given_names": "C.", "surname": "Carter", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "T. Walah", "canonical_name": "Walah, T.", "given_names": "T.", "surname": "Walah", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "W. W. Wallace", "canonical_name": "Wallace, W. W.", "given_names": "W. W.", "surname": "Wallace", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. Moore", "canonical_name": "Moore, A.", "given_names": "A.", "surname": "Moore", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "J. D. Galloway", "canonical_name": "Galloway, J. D.", "given_names": "J. D.", "surname": "Galloway", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. C. Woods", "canonical_name": "Woods, A. C.", "given_names": "A. C.", "surname": "Woods", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. O'Neill", "canonical_name": "O'Neill, A.", "given_names": "A.", "surname": "O'Neill", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "W. J. Tribbeck", "canonical_name": "Tribbeck, W. J.", "given_names": "W. J.", "surname": "Tribbeck", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. Urquhart", "canonical_name": "Urquhart, A.", "given_names": "A.", "surname": "Urquhart", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "F. B. House", "canonical_name": "House, F. B.", "given_names": "F. B.", "surname": "House", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "C. B. Collins", "canonical_name": "Collins, C. B.", "given_names": "C. B.", "surname": "Collins", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "W. J. MacRitchie", "canonical_name": "MacRitchie, W. J.", "given_names": "W. J.", "surname": "MacRitchie", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "O. L. A. Parkin", "canonical_name": "Parkin, O. L. A.", "given_names": "O. L. A.", "surname": "Parkin", "position": "Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "H. C. Ford", "canonical_name": "Ford, H. C.", "given_names": "H. C.", "surname": "Ford", "position": "Quarry Foreman", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "D. A. Ross", "canonical_name": "Ross, D. A.", "given_names": "D. A.", "surname": "Ross", "position": "Mechanical Foreman of Works", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "A. B. Smith", "canonical_name": "Smith, A. B.", "given_names": "A. B.", "surname": "Smith", "position": "Mains and Distribution Foreman", "department": "Public Works Department - Sierra Leone", "salary_min": 500, "salary_max": 560},
    {"name": "T. Maloney", "canonical_name": "Maloney, T.", "given_names": "T.", "surname": "Maloney", "position": "Electrical Foreman", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "L. T. Simpson", "canonical_name": "Simpson, L. T.", "given_names": "L. T.", "surname": "Simpson", "position": "Shift Foreman (Electricity Sub-Dept.)", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "V. M. Raine", "canonical_name": "Raine, V. M.", "given_names": "V. M.", "surname": "Raine", "position": "Shift Foreman (Electricity Sub-Dept.)", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "A. G. Black", "canonical_name": "Black, A. G.", "given_names": "A. G.", "surname": "Black", "position": "Shift Foreman (Electricity Sub-Dept.)", "department": "Public Works Department - Sierra Leone", "salary_scale": "F"},
    {"name": "E. T. Macfoye", "canonical_name": "Macfoye, E. T.", "given_names": "E. T.", "surname": "Macfoye", "position": "Chief African Surveyor", "department": "Public Works Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "A. C. Jones", "canonical_name": "Jones, A. C.", "given_names": "A. C.", "surname": "Jones", "position": "Chief African Draughtsman", "department": "Public Works Department - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. W. B. Wright", "canonical_name": "Wright, M. W. B.", "given_names": "M. W. B.", "surname": "Wright", "position": "Office Assistant", "department": "Public Works Department - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "A. A. Thompson", "canonical_name": "Thompson, A. A.", "given_names": "A. A.", "surname": "Thompson", "position": "African Clerk, Grade I", "department": "Public Works Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. P. Harleston", "canonical_name": "Harleston, A. P.", "given_names": "A. P.", "surname": "Harleston", "position": "African Clerk, Grade I", "department": "Public Works Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "F. N. Jones", "canonical_name": "Jones, F. N.", "given_names": "F. N.", "surname": "Jones", "position": "African Clerk, Grade I", "department": "Public Works Department - Sierra Leone", "salary_min": 210, "salary_max": 250},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()