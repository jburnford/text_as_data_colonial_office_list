"""
Sierra Leone Colonial Office List 1896 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1896

OFFICIALS = [
    {"name": "The Colonial Surgeon", "canonical_name": "Colonial Surgeon, The", "surname": "Colonial Surgeon", "position": "Inspector of Health", "department": "Sanitary Department - Sierra Leone"},
    {"name": "T. M. Cole", "canonical_name": "Cole, T. M.", "given_names": "T. M.", "surname": "Cole", "position": "Clerk", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "A. F. Tarbet", "canonical_name": "Tarbet, A. F.", "given_names": "A. F.", "surname": "Tarbet", "position": "Inspector-General of Frontier Police", "department": "Police Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "allowances": "91l. 5s.", "military_rank": "Capt."},
    {"name": "W. S. Sharpe", "canonical_name": "Sharpe, W. S.", "given_names": "W. S.", "surname": "Sharpe", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l. allowance"},
    {"name": "E. D. Fairtlough", "canonical_name": "Fairtlough, E. D.", "given_names": "E. D.", "surname": "Fairtlough", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l. allowance"},
    {"name": "S. Moore", "canonical_name": "Moore, S.", "given_names": "S.", "surname": "Moore", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l. allowance"},
    {"name": "C. C. Trougton", "canonical_name": "Trougton, C. C.", "given_names": "C. C.", "surname": "Trougton", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l. allowance"},
    {"name": "C. H. Boileau", "canonical_name": "Boileau, C. H.", "given_names": "C. H.", "surname": "Boileau", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l. allowance"},
    {"name": "B. Cave-Brown-Cave", "canonical_name": "Cave-Brown-Cave, B.", "given_names": "B.", "surname": "Cave-Brown-Cave", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l. allowance"},
    {"name": "J. E. C. Blakeney", "canonical_name": "Blakeney, J. E. C.", "given_names": "J. E. C.", "surname": "Blakeney", "position": "Assistant Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "91l. allowance", "qualifications": ["C.E."]},
    {"name": "J. B. Pratt", "canonical_name": "Pratt, J. B.", "given_names": "J. B.", "surname": "Pratt", "position": "Assistant Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "91l. allowance"},
    {"name": "C. N. Taylor", "canonical_name": "Taylor, C. N.", "given_names": "C. N.", "surname": "Taylor", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "J. B. Johnson", "canonical_name": "Johnson, J. B.", "given_names": "J. B.", "surname": "Johnson", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "J. H. Jones", "canonical_name": "Jones, J. H.", "given_names": "J. H.", "surname": "Jones", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "D. P. H. Crowther", "canonical_name": "Crowther, D. P. H.", "given_names": "D. P. H.", "surname": "Crowther", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "A. B. Davies", "canonical_name": "Davies, A. B.", "given_names": "A. B.", "surname": "Davies", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Paymaster, Frontier Police", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "U. F. Lapham", "canonical_name": "Lapham, U. F.", "given_names": "U. F.", "surname": "Lapham", "position": "Superintendent, Civil Police", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l. allowance", "military_rank": "Capt."},
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Inspector", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 250, "allowances": "91l. allowance", "location": "rent", "per_diem": "40l."},
    {"name": "N. H. Sawyer", "canonical_name": "Sawyer, N. H.", "given_names": "N. H.", "surname": "Sawyer", "position": "Sub-Inspector", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()