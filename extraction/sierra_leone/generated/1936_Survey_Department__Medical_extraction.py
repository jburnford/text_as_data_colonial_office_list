"""
Sierra Leone Colonial Office List 1936 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1936

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Director of Surveys", "department": "Survey Department - Sierra Leone", "salary_min": 1060, "salary_max": 1060},
    {"name": "P. A. Goodwin", "canonical_name": "Goodwin, P. A.", "given_names": "P. A.", "surname": "Goodwin", "position": "Officer i/c. Cadastral Branch", "department": "Survey Department - Sierra Leone", "salary_scale": "C", "qualifications": ["M.S.M."]},
    {"name": "R. Temple", "canonical_name": "Temple, R.", "given_names": "R.", "surname": "Temple", "position": "Survey and Lands Officer", "department": "Survey Department - Sierra Leone", "salary_scale": "C"},
    {"name": "P. D. Oakley", "canonical_name": "Oakley, P. D.", "given_names": "P. D.", "surname": "Oakley", "position": "Director of Medical Services", "department": "Medical - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280},
    {"name": "Q. Stewart", "canonical_name": "Stewart, Q.", "given_names": "Q.", "surname": "Stewart", "position": "Surgical Specialist", "department": "Medical - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280},
    {"name": "E. S. Walls", "canonical_name": "Walls, E. S.", "given_names": "E. S.", "surname": "Walls", "position": "Senior Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 1000, "salary_max": 1150, "allowances": "100l. seniority allowance"},
    {"name": "C. B. Jennings", "canonical_name": "Jennings, C. B.", "given_names": "C. B.", "surname": "Jennings", "position": "Senior Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 1000, "salary_max": 1150, "allowances": "100l. seniority allowance"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Pathologist", "department": "Medical - Sierra Leone"},
    {"name": "A. W. Lewis", "canonical_name": "Lewis, A. W.", "given_names": "A. W.", "surname": "Lewis", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "W. Allan", "canonical_name": "Allan, W.", "given_names": "W.", "surname": "Allan", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "H. R. F. Tweedy", "canonical_name": "Tweedy, H. R. F.", "given_names": "H. R. F.", "surname": "Tweedy", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "H. Peaston", "canonical_name": "Peaston, H.", "given_names": "H.", "surname": "Peaston", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "A. Cathcart", "canonical_name": "Cathcart, A.", "given_names": "A.", "surname": "Cathcart", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "A. Johnson", "canonical_name": "Johnson, A.", "given_names": "A.", "surname": "Johnson", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "W. J. Laird", "canonical_name": "Laird, W. J.", "given_names": "W. J.", "surname": "Laird", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "W. M. Quin", "canonical_name": "Quin, W. M.", "given_names": "W. M.", "surname": "Quin", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "W. R. Williams", "canonical_name": "Williams, W. R.", "given_names": "W. R.", "surname": "Williams", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "E. J. Wright", "canonical_name": "Wright, E. J.", "given_names": "E. J.", "surname": "Wright", "position": "Senior African Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 740, "salary_max": 820},
    {"name": "E. A. Renner", "canonical_name": "Renner, E. A.", "given_names": "E. A.", "surname": "Renner", "position": "African Pathologist", "department": "Medical - Sierra Leone", "salary_min": 740, "salary_max": 820},
    {"name": "M. C. F. Easmon", "canonical_name": "Easmon, M. C. F.", "given_names": "M. C. F.", "surname": "Easmon", "position": "African Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 720},
    {"name": "E. H. Taylor-Cummins", "canonical_name": "Taylor-Cummins, E. H.", "given_names": "E. H.", "surname": "Taylor-Cummins", "position": "African Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 720},
    {"name": "W. B. Hughes", "canonical_name": "Hughes, W. B.", "given_names": "W. B.", "surname": "Hughes", "position": "African Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 720},
    {"name": "W. F. O. Taylor", "canonical_name": "Taylor, W. F. O.", "given_names": "W. F. O.", "surname": "Taylor", "position": "African Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 720},
    {"name": "M. A. S. Margai", "canonical_name": "Margai, M. A. S.", "given_names": "M. A. S.", "surname": "Margai", "position": "African Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 720},
    {"name": "A. E. MacMaster", "canonical_name": "MacMaster, A. E.", "given_names": "A. E.", "surname": "MacMaster", "position": "Senior Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "G. M. Spencer", "canonical_name": "Spencer, G. M.", "given_names": "G. M.", "surname": "Spencer", "position": "Senior Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "L. D. S. McPetrie", "canonical_name": "McPetrie, L. D. S.", "given_names": "L. D. S.", "surname": "McPetrie", "position": "Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 480},
    {"name": "N. M. Brown", "canonical_name": "Brown, N. M.", "given_names": "N. M.", "surname": "Brown", "position": "Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 480},
    {"name": "H. F. W. Young", "canonical_name": "Young, H. F. W.", "given_names": "H. F. W.", "surname": "Young", "position": "Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 480},
    {"name": "M. C. Jennings", "canonical_name": "Jennings, M. C.", "given_names": "M. C.", "surname": "Jennings", "position": "Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 480}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()