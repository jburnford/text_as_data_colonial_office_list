"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "H. M. Lewis", "canonical_name": "Lewis, H. M.", "given_names": "H. M.", "surname": "Lewis",
     "position": "Treasurer", "department": "Treasury Department - Gold Coast", "salary_min": 1350, "salary_max": 1350, "duty_allowance": 270},
    {"name": "R. E. Burns", "canonical_name": "Burns, R. E.", "given_names": "R. E.", "surname": "Burns",
     "position": "Deputy Treasurer", "department": "Treasury Department - Gold Coast", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "D. B. Hinson", "canonical_name": "Hinson, D. B.", "given_names": "D. B.", "surname": "Hinson",
     "position": "Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "H. Vane Percy", "canonical_name": "Percy, H. Vane", "given_names": "H. Vane", "surname": "Percy",
     "position": "Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "G. A. D. Davies", "canonical_name": "Davies, G. A. D.", "given_names": "G. A. D.", "surname": "Davies",
     "position": "Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "C. J. Hodgens", "canonical_name": "Hodgens, C. J.", "given_names": "C. J.", "surname": "Hodgens",
     "position": "Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "honors": ["M.C."], "allowances": "72l. seniority allowance from 720l."},
    {"name": "Capt. J. H. Stephens", "canonical_name": "Stephens, J. H.", "given_names": "J. H.", "surname": "Stephens",
     "position": "Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "honors": ["M.C."], "military_rank": "Captain", "allowances": "72l. seniority allowance from 720l."},
    {"name": "F. A. C. Jones", "canonical_name": "Jones, F. A. C.", "given_names": "F. A. C.", "surname": "Jones",
     "position": "Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "Alex Konuah", "canonical_name": "Konuah, Alex", "given_names": "Alex", "surname": "Konuah",
     "position": "African Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 375, "salary_max": 780},
    {"name": "P. H. Schandorf", "canonical_name": "Schandorf, P. H.", "given_names": "P. H.", "surname": "Schandorf",
     "position": "African Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 375, "salary_max": 780},
    {"name": "J. F. Thompson", "canonical_name": "Thompson, J. F.", "given_names": "J. F.", "surname": "Thompson",
     "position": "Sub-Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "C. R. Hammond", "canonical_name": "Hammond, C. R.", "given_names": "C. R.", "surname": "Hammond",
     "position": "Sub-Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "Stephen Coleman", "canonical_name": "Coleman, Stephen", "given_names": "Stephen", "surname": "Coleman",
     "position": "Sub-Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "F. L. J. Cato", "canonical_name": "Cato, F. L. J.", "given_names": "F. L. J.", "surname": "Cato",
     "position": "Sub-Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "Sam Baidoo", "canonical_name": "Baidoo, Sam", "given_names": "Sam", "surname": "Baidoo",
     "position": "Sub-Assistant", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "A. I. Anteson", "canonical_name": "Anteson, A. I.", "given_names": "A. I.", "surname": "Anteson",
     "position": "Chief Clerk", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()