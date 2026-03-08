"""
Sierra Leone Colonial Office List 1898 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1898

OFFICIALS = [
    {"name": "W. T. Prout", "canonical_name": "Prout, W. T.", "given_names": "W. T.", "surname": "Prout", "position": "Colonial Surgeon", "department": "Medical Department - Sierra Leone", "salary_min": 500, "salary_max": 500, "qualifications": ["M.B."], "allowances": "travelling allowance, 91l. 5s."},
    {"name": "Wm. Renner", "canonical_name": "Renner, Wm.", "given_names": "Wm.", "surname": "Renner", "position": "Assistant Surgeon", "department": "Medical Department - Sierra Leone", "salary_min": 300, "salary_max": 350, "qualifications": ["M.R.C.S."], "allowances": "and allowance 45l. 12s. 6d."},
    {"name": "M. L. Jarrett", "canonical_name": "Jarrett, M. L.", "given_names": "M. L.", "surname": "Jarrett", "position": "Assistant Surgeon", "department": "Medical Department - Sierra Leone", "salary_min": 250, "salary_max": 250, "qualifications": ["M.R.C.S."]},
    {"name": "T. Bishop", "canonical_name": "Bishop, T.", "given_names": "T.", "surname": "Bishop", "position": "Assistant Surgeon", "department": "Medical Department - Sierra Leone", "salary_min": 200, "salary_max": 200, "qualifications": ["L.R.C.P."], "allowances": "and allowance 45l. 12s. 6d."},
    {"name": "D. Thomas Cole", "canonical_name": "Cole, D. Thomas", "given_names": "D. Thomas", "surname": "Cole", "position": "Medical Clerk", "department": "Medical Department - Sierra Leone", "salary_min": 100, "salary_max": 100, "allowances": "and quarters"},
    {"name": "E. J. During", "canonical_name": "During, E. J.", "given_names": "E. J.", "surname": "During", "position": "Assistant Clerk and Storekeeper", "department": "Medical Department - Sierra Leone", "salary_min": 60, "salary_max": 70},
    {"name": "G. L. Davies", "canonical_name": "Davies, G. L.", "given_names": "G. L.", "surname": "Davies", "position": "Compounder", "department": "Medical Department - Sierra Leone", "salary_min": 90, "salary_max": 90, "allowances": "and quarters"},
    {"name": "H. W. Lewis", "canonical_name": "Lewis, H. W.", "given_names": "H. W.", "surname": "Lewis", "position": "Keeper, Lunatic Asylum, Kissy", "department": "Medical Department - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "W. Z. Young", "canonical_name": "Young, W. Z.", "given_names": "W. Z.", "surname": "Young", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 50, "salary_max": 50, "location": "Waterloo", "allowances": "and quarters"},
    {"name": "M. Aubec", "canonical_name": "Aubec, M.", "given_names": "M.", "surname": "Aubec", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 36, "salary_max": 36, "location": "Hastings", "allowances": "and quarters"},
    {"name": "C. A. Innis", "canonical_name": "Innis, C. A.", "given_names": "C. A.", "surname": "Innis", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 40, "salary_max": 40, "location": "York", "allowances": "and quarters"},
    {"name": "E. G. Luke", "canonical_name": "Luke, E. G.", "given_names": "E. G.", "surname": "Luke", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 40, "salary_max": 40, "location": "Kent", "allowances": "and quarters"},
    {"name": "A. W. Elliott", "canonical_name": "Elliott, A. W.", "given_names": "A. W.", "surname": "Elliott", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 50, "salary_max": 50, "location": "Sherbro", "allowances": "and quarters"},
    {"name": "S. A. Bell", "canonical_name": "Bell, S. A.", "given_names": "S. A.", "surname": "Bell", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 60, "salary_max": 60, "location": "Sulymah", "allowances": "and quarters"},
    {"name": "J. G. Roberts", "canonical_name": "Roberts, J. G.", "given_names": "J. G.", "surname": "Roberts", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 36, "salary_max": 36, "location": "Regent", "allowances": "and quarters"},
    {"name": "—Leigh", "canonical_name": "Leigh, —", "given_names": "—", "surname": "Leigh", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 36, "salary_max": 36, "location": "Kissy", "allowances": "and quarters"},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 36, "salary_max": 36, "location": "Godervich", "allowances": "and quarters"},
    {"name": "Paul Nicol", "canonical_name": "Nicol, Paul", "given_names": "Paul", "surname": "Nicol", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 63, "salary_max": 70, "location": "Fatuba", "allowances": "and quarters"},
    {"name": "E. O. King", "canonical_name": "King, E. O.", "given_names": "E. O.", "surname": "King", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "salary_min": 63, "salary_max": 70, "location": "Mongheri", "allowances": "and qtrs."},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()