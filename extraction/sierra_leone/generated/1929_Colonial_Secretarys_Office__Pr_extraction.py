"""
Sierra Leone Colonial Office List 1929 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1929

OFFICIALS = [
    {"name": "M. A. Young", "canonical_name": "Young, M. A.", "given_names": "M. A.", "surname": "Young", "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280},
    {"name": "Capt. C. E. Cookson", "canonical_name": "Cookson, C. E.", "given_names": "C. E.", "surname": "Cookson", "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210, "military_rank": "Captain"},
    {"name": "Capt. J. E. Benham", "canonical_name": "Benham, J. E.", "given_names": "J. E.", "surname": "Benham", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B", "military_rank": "Captain"},
    {"name": "T. N. Goddard", "canonical_name": "Goddard, T. N.", "given_names": "T. N.", "surname": "Goddard", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B", "honors": ["M.B.E."]},
    {"name": "D. C. Thompson", "canonical_name": "Thompson, D. C.", "given_names": "D. C.", "surname": "Thompson", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "D. B. Drummond", "canonical_name": "Drummond, D. B.", "given_names": "D. B.", "surname": "Drummond", "position": "Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_scale": "B"},
    {"name": "J. H. Cheetham Smart", "canonical_name": "Smart, J. H. Cheetham", "given_names": "J. H. Cheetham", "surname": "Smart", "position": "African Assistant Secretary", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "T. A. Thompson", "canonical_name": "Thompson, T. A.", "given_names": "T. A.", "surname": "Thompson", "position": "Staff Superintendent", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "S. T. Johnson", "canonical_name": "Johnson, S. T.", "given_names": "S. T.", "surname": "Johnson", "position": "Chief Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 264, "salary_max": 372},
    {"name": "M. S. Macauley", "canonical_name": "Macauley, M. S.", "given_names": "M. S.", "surname": "Macauley", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "A. E. Scott", "canonical_name": "Scott, A. E.", "given_names": "A. E.", "surname": "Scott", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "H. B. Marke", "canonical_name": "Marke, H. B.", "given_names": "H. B.", "surname": "Marke", "position": "First Grade Clerk", "department": "Colonial Secretary's Office - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "J. McCulloch", "canonical_name": "McCulloch, J.", "given_names": "J.", "surname": "McCulloch", "position": "Government Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 600, "salary_max": 720, "duty_allowance": 72},
    {"name": "G. Worthington", "canonical_name": "Worthington, G.", "given_names": "G.", "surname": "Worthington", "position": "Assistant Government Printer", "department": "Printing Branch - Sierra Leone", "salary_scale": "F"},
    {"name": "G. B. Cassell", "canonical_name": "Cassell, G. B.", "given_names": "G. B.", "surname": "Cassell", "position": "African Assistant Government Printer", "department": "Printing Branch - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "African Assistant Government Printers", "department": "Printing Branch - Sierra Leone", "salary_min": 190, "salary_max": 240},
    {"name": "W. D. Bowden", "canonical_name": "Bowden, W. D.", "given_names": "W. D.", "surname": "Bowden", "position": "Provincial Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "honors": ["C.B.E."]},
    {"name": "A. H. Ross", "canonical_name": "Ross, A. H.", "given_names": "A. H.", "surname": "Ross", "position": "Provincial Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220, "honors": ["C.B.E."]},
    {"name": "R. S. Hooker", "canonical_name": "Hooker, R. S.", "given_names": "R. S.", "surname": "Hooker", "position": "Provincial Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "N. G. Frere", "canonical_name": "Frere, N. G.", "given_names": "N. G.", "surname": "Frere", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "N. C. Hollins", "canonical_name": "Hollins, N. C.", "given_names": "N. C.", "surname": "Hollins", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "W. R. Lyon", "canonical_name": "Lyon, W. R.", "given_names": "W. R.", "surname": "Lyon", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B", "military_rank": "Major"},
    {"name": "E. R. Langley", "canonical_name": "Langley, E. R.", "given_names": "E. R.", "surname": "Langley", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "A. H. Stocks", "canonical_name": "Stocks, A. H.", "given_names": "A. H.", "surname": "Stocks", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "E. F. Sayers", "canonical_name": "Sayers, E. F.", "given_names": "E. F.", "surname": "Sayers", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "S. M. Despicht", "canonical_name": "Despicht, S. M.", "given_names": "S. M.", "surname": "Despicht", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "J. T. Kemp", "canonical_name": "Kemp, J. T.", "given_names": "J. T.", "surname": "Kemp", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "J. S. Fenton", "canonical_name": "Fenton, J. S.", "given_names": "J. S.", "surname": "Fenton", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "A. V. E. Pearse", "canonical_name": "Pearse, A. V. E.", "given_names": "A. V. E.", "surname": "Pearse", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "L. W. Wilson", "canonical_name": "Wilson, L. W.", "given_names": "L. W.", "surname": "Wilson", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "J. de B. Shaw", "canonical_name": "Shaw, J. de B.", "given_names": "J. de B.", "surname": "Shaw", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "E. Harnetty", "canonical_name": "Harnetty, E.", "given_names": "E.", "surname": "Harnetty", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "Capt. J. C. Page", "canonical_name": "Page, J. C.", "given_names": "J. C.", "surname": "Page", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B", "military_rank": "Captain"},
    {"name": "Capt. F. R. Ellis", "canonical_name": "Ellis, F. R.", "given_names": "F. R.", "surname": "Ellis", "position": "District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B", "military_rank": "Captain"},
    {"name": "P. H. Smith", "canonical_name": "Smith, P. H.", "given_names": "P. H.", "surname": "Smith", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "E. J. Tyndall", "canonical_name": "Tyndall, E. J.", "given_names": "E. J.", "surname": "Tyndall", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "C. G. Hancock", "canonical_name": "Hancock, C. G.", "given_names": "C. G.", "surname": "Hancock", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "G. Jackson", "canonical_name": "Jackson, G.", "given_names": "G.", "surname": "Jackson", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "L. H. Humpherson", "canonical_name": "Humpherson, L. H.", "given_names": "L. H.", "surname": "Humpherson", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "G. P. Taylor", "canonical_name": "Taylor, G. P.", "given_names": "G. P.", "surname": "Taylor", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "W. W. Barnhill", "canonical_name": "Barnhill, W. W.", "given_names": "W. W.", "surname": "Barnhill", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "A. M. Sim", "canonical_name": "Sim, A. M.", "given_names": "A. M.", "surname": "Sim", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "N. M. McRobert", "canonical_name": "McRobert, N. M.", "given_names": "N. M.", "surname": "McRobert", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "F. H. McCleary", "canonical_name": "McCleary, F. H.", "given_names": "F. H.", "surname": "McCleary", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "E. A. C. Talbot", "canonical_name": "Talbot, E. A. C.", "given_names": "E. A. C.", "surname": "Talbot", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "D. Cox", "canonical_name": "Cox, D.", "given_names": "D.", "surname": "Cox", "position": "Assistant District Commissioner", "department": "Provincial Administration - Sierra Leone", "salary_scale": "B"},
    {"name": "C. R. Morrison", "canonical_name": "Morrison, C. R.", "given_names": "C. R.", "surname": "Morrison", "position": "Office Assistant", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "A. T. A. Beekley", "canonical_name": "Beekley, A. T. A.", "given_names": "A. T. A.", "surname": "Beekley", "position": "Office Assistant", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "F. A. Devenaux", "canonical_name": "Devenaux, F. A.", "given_names": "F. A.", "surname": "Devenaux", "position": "Office Assistant", "department": "Provincial Administration - Sierra Leone", "salary_min": 350, "salary_max": 450},
    {"name": "E. S. George", "canonical_name": "George, E. S.", "given_names": "E. S.", "surname": "George", "position": "First Grade Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "S. A. Johnson", "canonical_name": "Johnson, S. A.", "given_names": "S. A.", "surname": "Johnson", "position": "First Grade Clerk", "department": "Provincial Administration - Sierra Leone", "salary_min": 210, "salary_max": 250}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()