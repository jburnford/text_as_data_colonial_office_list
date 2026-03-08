"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "A. W. Nylander", "canonical_name": "Nylander, A. W.", "given_names": "A. W.", "surname": "Nylander", "position": "2nd Clerk", "department": "Medical Department. / Sanitary Department. - Sierra Leone", "salary_min": 48, "salary_max": 48},
    {"name": "W. S. Saunders", "canonical_name": "Saunders, W. S.", "given_names": "W. S.", "surname": "Saunders", "position": "Registrar of Births, Deaths, and Marriages", "department": "Medical Department. / Sanitary Department. - Sierra Leone"},
    {"name": "Rev. G. J. Macalay", "canonical_name": "Macalay, G. J.", "given_names": "G. J.", "surname": "Macalay", "position": "Registrar of Births, Deaths, and Marriages", "department": "Medical Department. / Sanitary Department. - Sierra Leone"},
    {"name": "Rev. N. J. Cole", "canonical_name": "Cole, N. J.", "given_names": "N. J.", "surname": "Cole", "position": "Registrar of Births, Deaths, and Marriages", "department": "Medical Department. / Sanitary Department. - Sierra Leone"},
    {"name": "L. Taylor", "canonical_name": "Taylor, L.", "given_names": "L.", "surname": "Taylor", "position": "Registrar of Births, Deaths, and Marriages", "department": "Medical Department. / Sanitary Department. - Sierra Leone"},
    {"name": "H. A. Williams", "canonical_name": "Williams, H. A.", "given_names": "H. A.", "surname": "Williams", "position": "Registrar of Births, Deaths, and Marriages", "department": "Medical Department. / Sanitary Department. - Sierra Leone"},
    {"name": "M. L. Jarrett", "canonical_name": "Jarrett, M. L.", "given_names": "M. L.", "surname": "Jarrett", "position": "Registrar of Births, Deaths, and Marriages", "department": "Medical Department. / Sanitary Department. - Sierra Leone"},
    {"name": "J. J. Warburton", "canonical_name": "Warburton, J. J.", "given_names": "J. J.", "surname": "Warburton", "position": "Registrar of Births, Deaths, and Marriages", "department": "Medical Department. / Sanitary Department. - Sierra Leone"},
    {"name": "Right Rev. E. G. Ingham", "canonical_name": "Ingham, E. G.", "given_names": "E. G.", "surname": "Ingham", "position": "Bishop of Sierra Leone", "department": "Medical Department. / Sanitary Department. - Sierra Leone", "qualifications": ["D.D."]},
    {"name": "Rev. S. Spain", "canonical_name": "Spain, S.", "given_names": "S.", "surname": "Spain", "position": "Colonial Chaplain", "department": "Medical Department. / Sanitary Department. - Sierra Leone", "salary_min": 204, "salary_max": 204, "qualifications": ["B.A."]},
    {"name": "J. Midley", "canonical_name": "Midley, J.", "given_names": "J.", "surname": "Midley", "position": "Organist", "department": "Medical Department. / Sanitary Department. - Sierra Leone", "salary_min": 40, "salary_max": 40},
    {"name": "E. W. Cole", "canonical_name": "Cole, E. W.", "given_names": "E. W.", "surname": "Cole", "position": "Clerk", "department": "Medical Department. / Sanitary Department. - Sierra Leone", "salary_min": 25, "salary_max": 25}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()