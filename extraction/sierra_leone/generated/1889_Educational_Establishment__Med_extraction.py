"""
Sierra Leone Colonial Office List 1889 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1889

OFFICIALS = [
    {"name": "T. S. Wilson", "canonical_name": "Wilson, T. S.", "given_names": "T. S.", "surname": "Wilson", "position": "Head Master, Government Practising School", "department": "Educational Establishment - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "Mary A. Macauley", "canonical_name": "Macauley, Mary A.", "given_names": "Mary A.", "surname": "Macauley", "position": "Schoolmistress", "department": "Educational Establishment - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "I. Steinwehr", "canonical_name": "Steinwehr, I.", "given_names": "I.", "surname": "Steinwehr", "position": "Ditto", "department": "Educational Establishment - Sierra Leone", "salary_min": 24, "salary_max": 24},
    {"name": "D. P. Ross", "canonical_name": "Ross, D. P.", "given_names": "D. P.", "surname": "Ross", "position": "Colonial Surgeon", "department": "Medical Establishment - Sierra Leone", "salary_min": 500, "salary_max": 500, "qualifications": ["M.D.", "F.R.C.S."], "allowances": "travelling allowance, 91l. 1s."},
    {"name": "Wm. Renner", "canonical_name": "Renner, Wm.", "given_names": "Wm.", "surname": "Renner", "position": "Assistant ditto", "department": "Medical Establishment - Sierra Leone", "salary_min": 300, "salary_max": 300, "qualifications": ["M.R.C.S."], "allowances": "and allowance 45l. 12s. 6d."},
    {"name": "M. L. Jarrett", "canonical_name": "Jarrett, M. L.", "given_names": "M. L.", "surname": "Jarrett", "position": "Assistant ditto", "department": "Medical Establishment - Sierra Leone", "salary_min": 250, "salary_max": 250, "qualifications": ["M.R.C.S."]},
    {"name": "D. Thomas Cole", "canonical_name": "Cole, D. Thomas", "given_names": "D. Thomas", "surname": "Cole", "position": "Medical Clerk and Storekeeper", "department": "Medical Establishment - Sierra Leone", "salary_min": 120, "salary_max": 120},
    {"name": "G. L. Davies", "canonical_name": "Davies, G. L.", "given_names": "G. L.", "surname": "Davies", "position": "Compounder", "department": "Medical Establishment - Sierra Leone", "salary_min": 70, "salary_max": 70},
    {"name": "W. Macauley", "canonical_name": "Macauley, W.", "given_names": "W.", "surname": "Macauley", "position": "Keeper, Lunatic Asylum", "department": "Medical Establishment - Sierra Leone", "salary_min": 60, "salary_max": 60, "location": "Kissy"},
    {"name": "T. M. Cole", "canonical_name": "Cole, T. M.", "given_names": "T. M.", "surname": "Cole", "position": "Clerk", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 50}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()