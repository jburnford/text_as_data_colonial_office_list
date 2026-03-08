"""
Gambia Colonial Office List 1921 - Extracted Data
"""
COLONY = "Gambia"
YEAR = 1921

OFFICIALS = [
    {"name": "T. F. G. Mayer", "canonical_name": "Mayer, T. F. G.", "given_names": "T. F. G.", "surname": "Mayer", "position": "Senior Medical Officer", "department": "Medical - Gambia", "salary_min": 1000, "salary_max": 1500, "allowances": "250l. staff and seniority allowances"},
    {"name": "F. C. V. Thompson", "canonical_name": "Thompson, F. C. V.", "given_names": "F. C. V.", "surname": "Thompson", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "R. H. Miller", "canonical_name": "Miller, R. H.", "given_names": "R. H.", "surname": "Miller", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance", "military_rank": "Captain"},
    {"name": "J. C. Watt", "canonical_name": "Watt, J. C.", "given_names": "J. C.", "surname": "Watt", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance", "military_rank": "Captain", "honors": ["M.C."]},
    {"name": "E. B. Bate", "canonical_name": "Bate, E. B.", "given_names": "E. B.", "surname": "Bate", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "G. E. Craig", "canonical_name": "Craig, G. E.", "given_names": "G. E.", "surname": "Craig", "position": "Medical Officer", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "J. Cair", "canonical_name": "Cair, J.", "given_names": "J.", "surname": "Cair", "position": "Dental Surgeon", "department": "Medical - Gambia", "salary_min": 660, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "M. Thompson", "canonical_name": "Thompson, M.", "given_names": "M.", "surname": "Thompson", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "P. Stagg", "canonical_name": "Stagg, P.", "given_names": "P.", "surname": "Stagg", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "C. G. Leggat", "canonical_name": "Leggat, C. G.", "given_names": "C. G.", "surname": "Leggat", "position": "Nursing Sister", "department": "Medical - Gambia", "salary_min": 250, "salary_max": 300},
    {"name": "J. F. Johnson", "canonical_name": "Johnson, J. F.", "given_names": "J. F.", "surname": "Johnson", "position": "Chief Dispenser and Storekeeper", "department": "Medical - Gambia", "salary_min": 150, "salary_max": 210},
    {"name": "E. W. Johns", "canonical_name": "Johns, E. W.", "given_names": "E. W.", "surname": "Johns", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 110, "salary_max": 142},
    {"name": "W. M. Rollings", "canonical_name": "Rollings, W. M.", "given_names": "W. M.", "surname": "Rollings", "position": "Dispenser", "department": "Medical - Gambia", "salary_min": 110, "salary_max": 142},
    {"name": "J. T. Williams", "canonical_name": "Williams, J. T.", "given_names": "J. T.", "surname": "Williams", "position": "Assistant Dispenser", "department": "Medical - Gambia", "salary_min": 60, "salary_max": 84},
    {"name": "W. E. Baxter", "canonical_name": "Baxter, W. E.", "given_names": "W. E.", "surname": "Baxter", "position": "Assistant Dispenser", "department": "Medical - Gambia", "salary_min": 60, "salary_max": 84},
    {"name": "C. Shaw", "canonical_name": "Shaw, C.", "given_names": "C.", "surname": "Shaw", "position": "2nd Grade Clerk", "department": "Medical - Gambia", "salary_min": 90, "salary_max": 170},
    {"name": "E. B. Williams", "canonical_name": "Williams, E. B.", "given_names": "E. B.", "surname": "Williams", "position": "3rd Grade Clerk", "department": "Medical - Gambia", "salary_min": 50, "salary_max": 80},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Medical Officer of Health", "department": "Board of Health - Gambia", "salary_min": 800, "salary_max": 962, "allowances": "staff and seniority allowances, 222l."},
    {"name": "C. Wolfendale", "canonical_name": "Wolfendale, C.", "given_names": "C.", "surname": "Wolfendale", "position": "Sanitary Inspector", "department": "Board of Health - Gambia", "salary_min": 440, "salary_max": 500},
    {"name": "A. E. V. Vaughan", "canonical_name": "Vaughan, A. E. V.", "given_names": "A. E. V.", "surname": "Vaughan", "position": "Assistant Sanitary Inspector", "department": "Board of Health - Gambia", "salary_min": 400, "salary_max": 460},
    {"name": "J. A. Yorke", "canonical_name": "Yorke, J. A.", "given_names": "J. A.", "surname": "Yorke", "position": "Clerk of the Market", "department": "Board of Health - Gambia", "salary_min": 84, "salary_max": 108},
    {"name": "J. A. Johnson", "canonical_name": "Johnson, J. A.", "given_names": "J. A.", "surname": "Johnson", "position": "Inspector of Nuisances", "department": "Board of Health - Gambia", "salary_min": 84, "salary_max": 108},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()