"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "Right Rev. E. G. Ingham", "canonical_name": "Ingham, E. G.", "given_names": "E. G.", "surname": "Ingham", "position": "Bishop of Sierra Leone", "department": "Ecclesiastical Department - Sierra Leone", "qualifications": ["D.D."]},
    {"name": "Rev. S. Spain", "canonical_name": "Spain, S.", "given_names": "S.", "surname": "Spain", "position": "Colonial Chaplain", "department": "Ecclesiastical Department - Sierra Leone", "qualifications": ["B.A."], "salary_min": 204},
    {"name": "J. Midley", "canonical_name": "Midley, J.", "given_names": "J.", "surname": "Midley", "position": "Organist", "department": "Ecclesiastical Department - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "Clerk", "department": "Ecclesiastical Department - Sierra Leone", "salary_min": 25, "salary_max": 25},
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Board of Education - Sierra Leone"},
    {"name": "Hon. Sir Samuel Lewis", "canonical_name": "Lewis, Samuel", "given_names": "Samuel", "surname": "Lewis", "position": "Member", "department": "Board of Education - Sierra Leone", "honors": ["C.M.G."], "qualifications": ["B.L."]},
    {"name": "Rev. J. Claudius May", "canonical_name": "May, J. Claudius", "given_names": "J. Claudius", "surname": "May", "position": "Member", "department": "Board of Education - Sierra Leone", "qualifications": ["F.R.G.S."]},
    {"name": "Rev. O. Moore", "canonical_name": "Moore, O.", "given_names": "O.", "surname": "Moore", "position": "Member", "department": "Board of Education - Sierra Leone"},
    {"name": "Rev. W. Vivian", "canonical_name": "Vivian, W.", "given_names": "W.", "surname": "Vivian", "position": "Member", "department": "Board of Education - Sierra Leone"},
    {"name": "Jacob W. Lewis", "canonical_name": "Lewis, Jacob W.", "given_names": "Jacob W.", "surname": "Lewis", "position": "Clerk to Board", "department": "Board of Education - Sierra Leone", "salary_min": 20, "salary_max": 20},
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "travelling allowance 91l. 5s."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()