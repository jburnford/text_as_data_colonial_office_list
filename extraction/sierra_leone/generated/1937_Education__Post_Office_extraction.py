"""
Sierra Leone Colonial Office List 1937 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1937

OFFICIALS = [
    {"name": "W. E. Nicholson", "canonical_name": "Nicholson, W. E.", "given_names": "W. E.", "surname": "Nicholson", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "S. Millburn", "canonical_name": "Millburn, S.", "given_names": "S.", "surname": "Millburn", "position": "Senior Superintendent of Education", "department": "Education - Sierra Leone", "salary_min": 840, "salary_max": 920},
    {"name": "W. J. Davies", "canonical_name": "Davies, W. J.", "given_names": "W. J.", "surname": "Davies", "position": "Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_min": 540, "salary_max": 920},
    {"name": "H. E. T. Hodgson", "canonical_name": "Hodgson, H. E. T.", "given_names": "H. E. T.", "surname": "Hodgson", "position": "Principal, Bo School", "department": "Education - Sierra Leone", "salary_min": 720, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "C. P. Ellis", "canonical_name": "Ellis, C. P.", "given_names": "C. P.", "surname": "Ellis", "position": "Vice-Principal, Prince of Wales' School", "department": "Education - Sierra Leone", "salary_scale": "C", "salary_min": 480, "salary_max": 920},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Master, Bo School", "department": "Education - Sierra Leone"},
    {"name": "A. Wurie", "canonical_name": "Wurie, A.", "given_names": "A.", "surname": "Wurie", "position": "Headmaster, Koyeima", "department": "Education - Sierra Leone", "salary_min": 210, "salary_max": 250},
    {"name": "Miss K. B. Coopoe", "canonical_name": "Coopoe, K. B.", "given_names": "K. B.", "surname": "Coopoe", "position": "Supervisor of Infant and Female Education", "department": "Education - Sierra Leone", "salary_min": 480, "salary_max": 720},
    {"name": "S. M. Broderick", "canonical_name": "Broderick, S. M.", "given_names": "S. M.", "surname": "Broderick", "position": "African Assistant Director of Education", "department": "Education - Sierra Leone", "salary_min": 310, "salary_max": 450},
    {"name": "C. B. Plenderleith", "canonical_name": "Plenderleith, C. B.", "given_names": "C. B.", "surname": "Plenderleith", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "honors": ["D.C.M."], "salary_min": 920, "salary_max": 920, "duty_allowance": 92},
    {"name": "V. K. Edwin", "canonical_name": "Edwin, V. K.", "given_names": "V. K.", "surname": "Edwin", "position": "Assistant Postmaster General and Accountant", "department": "Post Office - Sierra Leone", "salary_min": 360, "salary_max": 600},
    {"name": "E. S. B. Francis", "canonical_name": "Francis, E. S. B.", "given_names": "E. S. B.", "surname": "Francis", "position": "Staff Superintendent", "department": "Post Office - Sierra Leone", "salary_min": 310, "salary_max": 450}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()