"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "W. T. Prout", "canonical_name": "Prout, W. T.", "given_names": "W. T.", "surname": "Prout", "position": "Colonial Surgeon", "department": "Medical - Sierra Leone", "qualifications": ["M.B."], "allowances": "50l., travelling allowance, 91l. 5s."},
    {"name": "Wm. Renner", "canonical_name": "Renner, William", "given_names": "Wm.", "surname": "Renner", "position": "Assistant Surgeon", "department": "Medical - Sierra Leone", "qualifications": ["M.R.C.S."], "salary_min": 300, "salary_max": 350, "allowances": "and allowance 45l. 12s. 6d."},
    {"name": "M. L. Jarrett", "canonical_name": "Jarrett, M. L.", "given_names": "M. L.", "surname": "Jarrett", "position": "Assistant Surgeon", "department": "Medical - Sierra Leone", "qualifications": ["M.R.C.S."], "salary_min": 250, "salary_max": 250},
    {"name": "I. N. Paris", "canonical_name": "Paris, I. N.", "given_names": "I. N.", "surname": "Paris", "position": "Assistant Surgeon", "department": "Medical - Sierra Leone", "qualifications": ["M.B."], "salary_min": 200, "salary_max": 200, "allowances": "and allowance 45l. 12s. 6d."},
    {"name": "T. Bishop", "canonical_name": "Bishop, T.", "given_names": "T.", "surname": "Bishop", "position": "Assistant Surgeon for Frontier Police", "department": "Medical - Sierra Leone", "qualifications": ["L.R.C.P."], "salary_min": 300, "salary_max": 350, "allowances": "and 91l. allowance"},
    {"name": "D. Thomas Cole", "canonical_name": "Cole, D. Thomas", "given_names": "D. Thomas", "surname": "Cole", "position": "Medical Clerk and Storekeeper", "department": "Medical - Sierra Leone", "salary_min": 135, "salary_max": 135, "allowances": "and quarters"},
    {"name": "G. L. Davies", "canonical_name": "Davies, G. L.", "given_names": "G. L.", "surname": "Davies", "position": "Compounder", "department": "Medical - Sierra Leone", "salary_min": 90, "salary_max": 90, "allowances": "and quarters"},
    {"name": "H. W. Lewis", "canonical_name": "Lewis, H. W.", "given_names": "H. W.", "surname": "Lewis", "position": "Keeper, Lunatic Asylum", "department": "Medical - Sierra Leone", "location": "Kissy", "salary_min": 60, "salary_max": 60},
    {"name": "W. Z. Young", "canonical_name": "Young, W. Z.", "given_names": "W. Z.", "surname": "Young", "position": "Dispenser", "department": "Medical - Sierra Leone", "location": "Waterloo", "salary_min": 50, "salary_max": 50, "allowances": "and quarters"},
    {"name": "M. Aubec", "canonical_name": "Aubec, M.", "given_names": "M.", "surname": "Aubec", "position": "Dispenser", "department": "Medical - Sierra Leone", "location": "Hastings", "salary_min": 36, "salary_max": 36, "allowances": "and quarters"},
    {"name": "C. A. Innis", "canonical_name": "Innis, C. A.", "given_names": "C. A.", "surname": "Innis", "position": "Dispenser", "department": "Medical - Sierra Leone", "location": "York", "salary_min": 40, "salary_max": 40, "allowances": "and quarters"},
    {"name": "A. W. Elliott", "canonical_name": "Elliott, A. W.", "given_names": "A. W.", "surname": "Elliott", "position": "Dispenser", "department": "Medical - Sierra Leone", "location": "Sherbro", "salary_min": 50, "salary_max": 50, "allowances": "and quarters"},
    {"name": "S. A. Bell", "canonical_name": "Bell, S. A.", "given_names": "S. A.", "surname": "Bell", "position": "Dispenser", "department": "Medical - Sierra Leone", "location": "Sulymah", "salary_min": 60, "salary_max": 60, "allowances": "and quarters"},
    {"name": "M. N. Lardner", "canonical_name": "Lardner, M. N.", "given_names": "M. N.", "surname": "Lardner", "position": "Dispenser", "department": "Medical - Sierra Leone", "location": "Regent", "salary_min": 36, "salary_max": 36, "allowances": "and quarters"},
    {"name": "J. G. Roberts", "canonical_name": "Roberts, J. G.", "given_names": "J. G.", "surname": "Roberts", "position": "Dispenser", "department": "Medical - Sierra Leone", "location": "Kissy", "salary_min": 36, "salary_max": 36, "allowances": "and quarters"},
    {"name": "E. G. Luke", "canonical_name": "Luke, E. G.", "given_names": "E. G.", "surname": "Luke", "position": "Dispenser", "department": "Medical - Sierra Leone", "location": "Goderich", "salary_min": 36, "salary_max": 36, "allowances": "and quarters"},
    {"name": "J. E. Baker", "canonical_name": "Baker, J. E.", "given_names": "J. E.", "surname": "Baker", "position": "Dispenser", "department": "Medical - Sierra Leone", "location": "Falaba", "salary_min": 63, "salary_max": 70, "allowances": "and quarters"},
    {"name": "E. O. King", "canonical_name": "King, E. O.", "given_names": "E. O.", "surname": "King", "position": "Dispenser", "department": "Medical - Sierra Leone", "location": "Mongheri", "salary_min": 63, "salary_max": 70, "allowances": "and qtrs."},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()