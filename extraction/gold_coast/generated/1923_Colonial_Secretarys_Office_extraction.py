"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Dr. J. C. Maxwell", "canonical_name": "Maxwell, J. C.", "given_names": "J. C.", "surname": "Maxwell",
     "position": "Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 1800, "duty_allowance": 360, "honors": ["C.M.G."]},
    {"name": "A. A. C. Finlay", "canonical_name": "Finlay, A. A. C.", "given_names": "A. A. C.", "surname": "Finlay",
     "position": "Chief Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 1200, "duty_allowance": 240, "honors": ["I.S.O."]},
    {"name": "D. B. Strathairn", "canonical_name": "Strathairn, D. B.", "given_names": "D. B.", "surname": "Strathairn",
     "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 1050, "duty_allowance": 210},
    {"name": "E. A. T. Taylor", "canonical_name": "Taylor, E. A. T.", "given_names": "E. A. T.", "surname": "Taylor",
     "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 1050, "duty_allowance": 210},
    {"name": "J. P. Ross", "canonical_name": "Ross, J. P.", "given_names": "J. P.", "surname": "Ross",
     "position": "Senior Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 1050, "duty_allowance": 210},
    {"name": "J. L. Trafford", "canonical_name": "Trafford, J. L.", "given_names": "J. L.", "surname": "Trafford",
     "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 500, "salary_max": 960, "allowances": "seniority allowance, 72l. from 720l., and Secretariat allowance, 120l."},
    {"name": "L. W. Wood", "canonical_name": "Wood, L. W.", "given_names": "L. W.", "surname": "Wood",
     "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 500, "salary_max": 960, "allowances": "seniority allowance, 72l. from 720l., and Secretariat allowance, 120l."},
    {"name": "Capt. W. H. Gilliland", "canonical_name": "Gilliland, W. H.", "given_names": "W. H.", "surname": "Gilliland",
     "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 500, "salary_max": 960, "allowances": "seniority allowance, 72l. from 720l., and Secretariat allowance, 120l.", "military_rank": "Captain"},
    {"name": "R. B. Crabbe", "canonical_name": "Crabbe, R. B.", "given_names": "R. B.", "surname": "Crabbe",
     "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 500, "salary_max": 960, "allowances": "seniority allowance, 72l. from 720l., and Secretariat allowance, 120l."},
    {"name": "W. T. Harragin", "canonical_name": "Harragin, W. T.", "given_names": "W. T.", "surname": "Harragin",
     "position": "Assistant Colonial Secretary", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 500, "salary_max": 960, "allowances": "seniority allowance, 72l. from 720l., and Secretariat allowance, 120l."},
    {"name": "W. Miller", "canonical_name": "Miller, W.", "given_names": "W.", "surname": "Miller",
     "position": "Assistant Colonial Secretary for Harbours and Railways", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 960, "duty_allowance": 96},
    {"name": "Miss E. J. James", "canonical_name": "James, E. J.", "given_names": "E. J.", "surname": "James",
     "position": "Secretariat Assistant", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 450, "salary_max": 600, "qualifications": ["B.A."]},
    {"name": "F. J. Ribeiro", "canonical_name": "Ribeiro, F. J.", "given_names": "F. J.", "surname": "Ribeiro",
     "position": "Chief Clerk", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 300, "salary_max": 396, "allowances": "personal allowance, 120l."},
    {"name": "A. W. Clerk", "canonical_name": "Clerk, A. W.", "given_names": "A. W.", "surname": "Clerk",
     "position": "Superintendent, Despatch Branch", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "P. Amu", "canonical_name": "Amu, P.", "given_names": "P.", "surname": "Amu",
     "position": "Superintendent, Miscellaneous Branch", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 330, "salary_max": 396},
    {"name": "L. R. J. Ruttmern", "canonical_name": "Ruttmern, L. R. J.", "given_names": "L. R. J.", "surname": "Ruttmern",
     "position": "Superintendent, Registration Branch", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "C. M. Holm", "canonical_name": "Holm, C. M.", "given_names": "C. M.", "surname": "Holm",
     "position": "Superintendent, Correspondence Branch", "department": "Colonial Secretary's Office - Gold Coast", "salary_min": 300, "salary_max": 396},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()