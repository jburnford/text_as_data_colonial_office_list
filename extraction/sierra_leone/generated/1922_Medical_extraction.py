"""
Sierra Leone Colonial Office List 1922 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1922

OFFICIALS = [
    {"name": "W. I. Taylor", "canonical_name": "Taylor, W. I.", "given_names": "W. I.", "surname": "Taylor", "position": "Principal Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 1350, "salary_max": 1350, "duty_allowance": 270},
    {"name": "J. B. Blate", "canonical_name": "Blate, J. B.", "given_names": "J. B.", "surname": "Blate", "position": "Provincial Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "C. H. Allan", "canonical_name": "Allan, C. H.", "given_names": "C. H.", "surname": "Allan", "position": "Senior Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 1000, "salary_max": 1150, "allowances": "100l. seniority allowance"},
    {"name": "E. W. Wood-Mason", "canonical_name": "Wood-Mason, E. W.", "given_names": "E. W.", "surname": "Wood-Mason", "position": "Senior Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 1000, "salary_max": 1150, "allowances": "100l. seniority allowance"},
    {"name": "J. C. Murphy", "canonical_name": "Murphy, J. C.", "given_names": "J. C.", "surname": "Murphy", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "J. S. Pearson", "canonical_name": "Pearson, J. S.", "given_names": "J. S.", "surname": "Pearson", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "J. M'Conaghy", "canonical_name": "M'Conaghy, J.", "given_names": "J.", "surname": "M'Conaghy", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "J. Y. Wood", "canonical_name": "Wood, J. Y.", "given_names": "J. Y.", "surname": "Wood", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "R. Semple", "canonical_name": "Semple, R.", "given_names": "R.", "surname": "Semple", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "M. Jackson", "canonical_name": "Jackson, M.", "given_names": "M.", "surname": "Jackson", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "J. M. Mackay", "canonical_name": "Mackay, J. M.", "given_names": "J. M.", "surname": "Mackay", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "W. F. Campbell", "canonical_name": "Campbell, W. F.", "given_names": "W. F.", "surname": "Campbell", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 600, "salary_max": 700},
    {"name": "W. O. Taylor", "canonical_name": "Taylor, W. O.", "given_names": "W. O.", "surname": "Taylor", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 800},
    {"name": "M. C. F. Easmon", "canonical_name": "Easmon, M. C. F.", "given_names": "M. C. F.", "surname": "Easmon", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 800},
    {"name": "E. J. Wright", "canonical_name": "Wright, E. J.", "given_names": "E. J.", "surname": "Wright", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 800},
    {"name": "E. H. Taylor Cummings", "canonical_name": "Taylor Cummings, E. H.", "given_names": "E. H.", "surname": "Taylor Cummings", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 800},
    {"name": "G. N. Metzger", "canonical_name": "Metzger, G. N.", "given_names": "G. N.", "surname": "Metzger", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 800},
    {"name": "E. A. Renner", "canonical_name": "Renner, E. A.", "given_names": "E. A.", "surname": "Renner", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 800},
    {"name": "L. R. Stevens", "canonical_name": "Stevens, L. R.", "given_names": "L. R.", "surname": "Stevens", "position": "Matron", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "K.G. Appleton", "canonical_name": "Appleton, K.G.", "given_names": "K.G.", "surname": "Appleton", "position": "Senior Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 350, "salary_max": 400},
    {"name": "I. Stevens", "canonical_name": "Stevens, I.", "given_names": "I.", "surname": "Stevens", "position": "Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "C. Littlewood", "canonical_name": "Littlewood, C.", "given_names": "C.", "surname": "Littlewood", "position": "Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "L. Blaber", "canonical_name": "Blaber, L.", "given_names": "L.", "surname": "Blaber", "position": "Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "V. Bell", "canonical_name": "Bell, V.", "given_names": "V.", "surname": "Bell", "position": "Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "J. C. Carr", "canonical_name": "Carr, J. C.", "given_names": "J. C.", "surname": "Carr", "position": "Dental Surgeon", "department": "Medical - Sierra Leone", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()