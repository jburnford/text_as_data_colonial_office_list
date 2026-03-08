"""
Sierra Leone Colonial Office List 1894 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1894

OFFICIALS = [
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "travelling allowance 91l. 5s."},
    {"name": "F. J. Smart", "canonical_name": "Smart, F. J.", "given_names": "F. J.", "surname": "Smart", "position": "Schoolmaster", "department": "Educational Department - Sierra Leone", "location": "Isles de Los", "salary_min": 36, "salary_max": 36, "allowances": "rent, 7l. 4s."},
    {"name": "D. P. Ross", "canonical_name": "Ross, D. P.", "given_names": "D. P.", "surname": "Ross", "position": "Colonial Surgeon", "department": "Medical Department - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "travelling allowance, 91l. 5s.", "honors": ["C.M.G."], "qualifications": ["M.D.", "F.R.C.S."]},
    {"name": "Wm. Renner", "canonical_name": "Renner, Wm.", "given_names": "Wm.", "surname": "Renner", "position": "Assistant Surgeon", "department": "Medical Department - Sierra Leone", "salary_min": 800, "salary_max": 800, "allowances": "allowance 45l. 12s. 6d.", "qualifications": ["M.R.C.S."]},
    {"name": "M. L. Jarrett", "canonical_name": "Jarrett, M. L.", "given_names": "M. L.", "surname": "Jarrett", "position": "Assistant Surgeon", "department": "Medical Department - Sierra Leone", "salary_min": 250, "salary_max": 250, "qualifications": ["M.R.C.S."]},
    {"name": "I. N. Paris", "canonical_name": "Paris, I. N.", "given_names": "I. N.", "surname": "Paris", "position": "Assistant Surgeon", "department": "Medical Department - Sierra Leone", "salary_min": 200, "salary_max": 200, "allowances": "allowance 45l. 12s. 6d.", "qualifications": ["M.B."]},
    {"name": "D. Thomas Cole", "canonical_name": "Cole, D. Thomas", "given_names": "D. Thomas", "surname": "Cole", "position": "Medical Clerk and Storekeeper", "department": "Medical Department - Sierra Leone", "salary_min": 130, "salary_max": 130, "allowances": "quarters"},
    {"name": "G. L. Davies", "canonical_name": "Davies, G. L.", "given_names": "G. L.", "surname": "Davies", "position": "Compounder", "department": "Medical Department - Sierra Leone", "salary_min": 70, "salary_max": 70, "allowances": "quarters"},
    {"name": "W. Macauley", "canonical_name": "Macauley, W.", "given_names": "W.", "surname": "Macauley", "position": "Keeper, Lunatic Asylum", "department": "Medical Department - Sierra Leone", "location": "Kissy", "salary_min": 60, "salary_max": 60},
    {"name": "W. Z. Young", "canonical_name": "Young, W. Z.", "given_names": "W. Z.", "surname": "Young", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "location": "Waterloo", "salary_min": 50, "salary_max": 50, "allowances": "quarters"},
    {"name": "E. O. King", "canonical_name": "King, E. O.", "given_names": "E. O.", "surname": "King", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "location": "Hastings", "salary_min": 36, "salary_max": 36, "allowances": "quarters"},
    {"name": "C. A. Innis", "canonical_name": "Innis, C. A.", "given_names": "C. A.", "surname": "Innis", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "location": "York", "salary_min": 40, "salary_max": 40, "allowances": "quarters"},
    {"name": "E. J. During", "canonical_name": "During, E. J.", "given_names": "E. J.", "surname": "During", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "location": "Kent", "salary_min": 40, "salary_max": 40, "allowances": "quarters"},
    {"name": "A. W. Elliott", "canonical_name": "Elliott, A. W.", "given_names": "A. W.", "surname": "Elliott", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "location": "Sherbro", "salary_min": 50, "salary_max": 50, "allowances": "quarters"},
    {"name": "S. A. Bell", "canonical_name": "Bell, S. A.", "given_names": "S. A.", "surname": "Bell", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "location": "Sulymah", "salary_min": 60, "salary_max": 60, "allowances": "quarters"},
    {"name": "M. N. Lardner", "canonical_name": "Lardner, M. N.", "given_names": "M. N.", "surname": "Lardner", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "location": "Regent", "salary_min": 36, "salary_max": 36, "allowances": "quarters"},
    {"name": "J. G. Roberts", "canonical_name": "Roberts, J. G.", "given_names": "J. G.", "surname": "Roberts", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "location": "Kissy", "salary_min": 36, "salary_max": 36, "allowances": "quarters"},
    {"name": "E. G. Luke", "canonical_name": "Luke, E. G.", "given_names": "E. G.", "surname": "Luke", "position": "Dispenser", "department": "Medical Department - Sierra Leone", "location": "Goderich", "salary_min": 36, "salary_max": 36, "allowances": "quarters"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()