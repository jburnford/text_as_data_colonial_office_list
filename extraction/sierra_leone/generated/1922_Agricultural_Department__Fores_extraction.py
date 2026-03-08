"""
Sierra Leone Colonial Office List 1922 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1922

OFFICIALS = [
    {"name": "D. W. Scottland", "canonical_name": "Scottland, D. W.", "given_names": "D. W.", "surname": "Scottland", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200},
    {"name": "H. Waterland", "canonical_name": "Waterland, H.", "given_names": "H.", "surname": "Waterland", "position": "Assistants in Agricultural Department", "department": "Agricultural Department - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "J. A. Guvezian", "canonical_name": "Guvezian, J. A.", "given_names": "J. A.", "surname": "Guvezian", "position": "Assistants in Agricultural Department", "department": "Agricultural Department - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "S. L. Moseley", "canonical_name": "Moseley, S. L.", "given_names": "S. L.", "surname": "Moseley", "position": "Superintendent, Experimental Farm", "department": "Agricultural Department - Sierra Leone", "salary_min": 184, "salary_max": 204},
    {"name": "L. A. King-Church", "canonical_name": "King-Church, L. A.", "given_names": "L. A.", "surname": "King-Church", "position": "Conservator of Forests", "department": "Forest Department - Sierra Leone"},
    {"name": "K. G. Burbridge", "canonical_name": "Burbridge, K. G.", "given_names": "K. G.", "surname": "Burbridge", "position": "Assistant Conservators of Forests", "department": "Forest Department - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "E. Macdonald", "canonical_name": "Macdonald, E.", "given_names": "E.", "surname": "Macdonald", "position": "Assistant Conservators of Forests", "department": "Forest Department - Sierra Leone", "salary_min": 480, "salary_max": 920},
    {"name": "D. G. Thomas", "canonical_name": "Thomas, D. G.", "given_names": "D. G.", "surname": "Thomas", "position": "Assistant Conservators of Forests", "department": "Forest Department - Sierra Leone", "salary_min": 480, "salary_max": 920}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()