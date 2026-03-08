"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone"},
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "travelling allowance 91l. 5s."},
    {"name": "W. T. Prout", "canonical_name": "Prout, W. T.", "given_names": "W. T.", "surname": "Prout", "position": "Colonial Surgeon", "department": "Medical Department - Sierra Leone", "qualifications": ["M.B."], "salary_min": 50, "salary_max": 50, "allowances": "travelling allowance, 91l. 5s."},
    {"name": "Wm. Renner", "canonical_name": "Renner, Wm.", "given_names": "Wm.", "surname": "Renner", "position": "Assistant ditto", "department": "Medical Department - Sierra Leone", "qualifications": ["M.R.C.S."], "salary_min": 300, "salary_max": 350, "allowances": "allowance 45l. 12s. 6d."},
    {"name": "M. L. Jarrett", "canonical_name": "Jarrett, M. L.", "given_names": "M. L.", "surname": "Jarrett", "position": "Assistant ditto", "department": "Medical Department - Sierra Leone", "qualifications": ["M.R.C.S."], "salary_min": 250, "salary_max": 250},
    {"name": "I. N. Paris", "canonical_name": "Paris, I. N.", "given_names": "I. N.", "surname": "Paris", "position": "Assistant ditto", "department": "Medical Department - Sierra Leone", "qualifications": ["M.B."], "salary_min": 200, "salary_max": 200, "allowances": "allowance 45l. 12s. 6d."},
    {"name": "T. Bishop", "canonical_name": "Bishop, T.", "given_names": "T.", "surname": "Bishop", "position": "Assistant ditto for Frontier Police", "department": "Medical Department - Sierra Leone", "qualifications": ["L.R.C.P."], "salary_min": 300, "salary_max": 350, "allowances": "91l. allowance"},
    {"name": "D. Thomas Cole", "canonical_name": "Cole, D. Thomas", "given_names": "D. Thomas", "surname": "Cole", "position": "Medical Clerk and Storekeeper", "department": "Medical Department - Sierra Leone", "salary_min": 135, "salary_max": 135},
    {"name": "G. L. Davies", "canonical_name": "Davies, G. L.", "given_names": "G. L.", "surname": "Davies", "position": "Compounder", "department": "Medical Department - Sierra Leone", "salary_min": 90, "salary_max": 90}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()