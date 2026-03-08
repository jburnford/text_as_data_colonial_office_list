"""
Sierra Leone Colonial Office List 1923 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1923

OFFICIALS = [
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Director, Medical and Sanitary Services", "department": "Medical - Sierra Leone", "salary_min": 1400, "salary_max": 1400, "duty_allowance": 280},
    {"name": "J. B. Rate", "canonical_name": "Rate, J. B.", "given_names": "J. B.", "surname": "Rate", "position": "Deputy Director, Medical Services", "department": "Medical - Sierra Leone", "salary_min": 1300, "salary_max": 1300, "duty_allowance": 260},
    {"name": "C. H. Allan", "canonical_name": "Allan, C. H.", "given_names": "C. H.", "surname": "Allan", "position": "Senior Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 1000, "salary_max": 1150},
    {"name": "E. W. Wood-Mason", "canonical_name": "Wood-Mason, E. W.", "given_names": "E. W.", "surname": "Wood-Mason", "position": "Senior Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 1000, "salary_max": 1150},
    {"name": "J. C. Murphy", "canonical_name": "Murphy, J. C.", "given_names": "J. C.", "surname": "Murphy", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 1000, "salary_max": 1150},
    {"name": "J. M'Conaghy", "canonical_name": "M'Conaghy, J.", "given_names": "J.", "surname": "M'Conaghy", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "J. Y. Wood", "canonical_name": "Wood, J. Y.", "given_names": "J. Y.", "surname": "Wood", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "M. Jackson", "canonical_name": "Jackson, M.", "given_names": "M.", "surname": "Jackson", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "J. M. Mackay", "canonical_name": "Mackay, J. M.", "given_names": "J. M.", "surname": "Mackay", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "E. S. Walls", "canonical_name": "Walls, E. S.", "given_names": "E. S.", "surname": "Walls", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "J. W. Hartley", "canonical_name": "Hartley, J. W.", "given_names": "J. W.", "surname": "Hartley", "position": "Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 660, "salary_max": 960},
    {"name": "W. O. Taylor", "canonical_name": "Taylor, W. O.", "given_names": "W. O.", "surname": "Taylor", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "M. C. F. Kasmon", "canonical_name": "Kasmon, M. C. F.", "given_names": "M. C. F.", "surname": "Kasmon", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "E. J. Wright", "canonical_name": "Wright, E. J.", "given_names": "E. J.", "surname": "Wright", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "E. H. Taylor Cummings", "canonical_name": "Taylor Cummings, E. H.", "given_names": "E. H.", "surname": "Taylor Cummings", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "G. N. Metzger", "canonical_name": "Metzger, G. N.", "given_names": "G. N.", "surname": "Metzger", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "E. A. Renner", "canonical_name": "Renner, E. A.", "given_names": "E. A.", "surname": "Renner", "position": "African Medical Staff", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 600},
    {"name": "L. R. Stevens", "canonical_name": "Stevens, L. R.", "given_names": "L. R.", "surname": "Stevens", "position": "Matron", "department": "Medical - Sierra Leone", "salary_min": 380, "salary_max": 440},
    {"name": "K. G. Appleton", "canonical_name": "Appleton, K. G.", "given_names": "K. G.", "surname": "Appleton", "position": "Senior Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 380, "salary_max": 440},
    {"name": "C. Littlewood", "canonical_name": "Littlewood, C.", "given_names": "C.", "surname": "Littlewood", "position": "Senior Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 380, "salary_max": 440},
    {"name": "I. Stevens", "canonical_name": "Stevens, I.", "given_names": "I.", "surname": "Stevens", "position": "Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "V. Bell", "canonical_name": "Bell, V.", "given_names": "V.", "surname": "Bell", "position": "Nursing Sister", "department": "Medical - Sierra Leone", "salary_min": 250, "salary_max": 300},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()