"""
Sierra Leone Colonial Office List 1925 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1925

OFFICIALS = [
    {"name": "C. H. King", "canonical_name": "King, C. H.", "given_names": "C. H.", "surname": "King", "position": "Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "military_rank": "Major"},
    {"name": "P. T. Brodie", "canonical_name": "Brodie, P. T.", "given_names": "P. T.", "surname": "Brodie", "position": "Assistant Commissioner of Police", "department": "Civil Police - Sierra Leone", "salary_scale": "A", "honors": ["D.S.O.", "M.C."], "military_rank": "Capt."},
    {"name": "J. Rabbitt", "canonical_name": "Rabbitt, J.", "given_names": "J.", "surname": "Rabbitt", "position": "Chief Inspector", "department": "Civil Police - Sierra Leone", "salary_min": 450, "salary_max": 510},
    {"name": "G. E. Biddle", "canonical_name": "Biddle, G. E.", "given_names": "G. E.", "surname": "Biddle", "position": "Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_scale": "A"},
    {"name": "A. P. Simmonds", "canonical_name": "Simmonds, A. P.", "given_names": "A. P.", "surname": "Simmonds", "position": "Assistant Superintendent of Prisons", "department": "Prisons - Sierra Leone", "salary_scale": "F"},
    {"name": "D. A. Williams", "canonical_name": "Williams, D. A.", "given_names": "D. A.", "surname": "Williams", "position": "Storekeeper", "department": "Prisons - Sierra Leone", "salary_min": 264, "salary_max": 372}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()