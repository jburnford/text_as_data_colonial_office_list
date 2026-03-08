"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Captain C. E. Cookson", "canonical_name": "Cookson, C. E.", "given_names": "C. E.", "surname": "Cookson",
     "position": "Inspector General of Prisons", "department": "Prisons Department - Gold Coast", "salary_min": 960, "salary_max": 960,
     "duty_allowance": 96, "military_rank": "Captain"},
    {"name": "Capt. H. R. Bilcliffe", "canonical_name": "Bilcliffe, H. R.", "given_names": "H. R.", "surname": "Bilcliffe",
     "position": "Deputy Inspector General of Prisons", "department": "Prisons Department - Gold Coast", "salary_min": 600, "salary_max": 800,
     "duty_allowance": 72, "military_rank": "Captain"},
    {"name": "J. Concannon", "canonical_name": "Concannon, J.", "given_names": "J.", "surname": "Concannon",
     "position": "Prison Superintendent", "department": "Prisons Department - Gold Coast", "salary_min": 440, "salary_max": 500,
     "allowances": "60l. allowance as Storekeeper when in Accra or Secondee"},
    {"name": "B. A. Francis", "canonical_name": "Francis, B. A.", "given_names": "B. A.", "surname": "Francis",
     "position": "Prison Superintendent", "department": "Prisons Department - Gold Coast", "salary_min": 440, "salary_max": 500,
     "allowances": "60l. allowance as Storekeeper when in Accra or Secondee"},
    {"name": "T. Ryan", "canonical_name": "Ryan, T.", "given_names": "T.", "surname": "Ryan",
     "position": "Prison Superintendent", "department": "Prisons Department - Gold Coast", "salary_min": 440, "salary_max": 500,
     "allowances": "60l. allowance as Storekeeper when in Accra or Secondee"},
    {"name": "C. Conn", "canonical_name": "Conn, C.", "given_names": "C.", "surname": "Conn",
     "position": "Prison Superintendent", "department": "Prisons Department - Gold Coast", "salary_min": 440, "salary_max": 500,
     "allowances": "60l. allowance as Storekeeper when in Accra or Secondee"},
    {"name": "W. R. Roberts", "canonical_name": "Roberts, W. R.", "given_names": "W. R.", "surname": "Roberts",
     "position": "Technical Instructor", "department": "Prisons Department - Gold Coast", "salary_min": 500, "salary_max": 560},
    {"name": "A. A. Wood", "canonical_name": "Wood, A. A.", "given_names": "A. A.", "surname": "Wood",
     "position": "Technical Instructor", "department": "Prisons Department - Gold Coast", "salary_min": 500, "salary_max": 560},
    {"name": "P. H. Roberts", "canonical_name": "Roberts, P. H.", "given_names": "P. H.", "surname": "Roberts",
     "position": "Assistant Prison Superintendent", "department": "Prisons Department - Gold Coast", "salary_min": 234, "salary_max": 340},
    {"name": "K. Kameron Sackey", "canonical_name": "Sackey, K. Kameron", "given_names": "K. Kameron", "surname": "Sackey",
     "position": "Chief Clerk", "department": "Prisons Department - Gold Coast", "salary_min": 300, "salary_max": 396},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()