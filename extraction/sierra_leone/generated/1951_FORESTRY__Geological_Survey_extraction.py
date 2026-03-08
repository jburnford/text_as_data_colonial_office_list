"""
Sierra Leone Colonial Office List 1951 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1951

OFFICIALS = [
    {"name": "D. H. Hodgson", "canonical_name": "Hodgson, D. H.", "given_names": "D. H.", "surname": "Hodgson", "position": "Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "R. S. Pelly", "canonical_name": "Pelly, R. S.", "given_names": "R. S.", "surname": "Pelly", "position": "Senior Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "H. C. King", "canonical_name": "King, H. C.", "given_names": "H. C.", "surname": "King", "position": "Senior Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "G. E. Crichton", "canonical_name": "Crichton, G. E.", "given_names": "G. E.", "surname": "Crichton", "position": "Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "J. K. Ross", "canonical_name": "Ross, J. K.", "given_names": "J. K.", "surname": "Ross", "position": "Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "R. M. Palmer", "canonical_name": "Palmer, R. M.", "given_names": "R. M.", "surname": "Palmer", "position": "Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "A. J. Browning", "canonical_name": "Browning, A. J.", "given_names": "A. J.", "surname": "Browning", "position": "Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "A. C. Frith", "canonical_name": "Frith, A. C.", "given_names": "A. C.", "surname": "Frith", "position": "Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "I. G. Bulmer", "canonical_name": "Bulmer, I. G.", "given_names": "I. G.", "surname": "Bulmer", "position": "Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "I. Paul", "canonical_name": "Paul, I.", "given_names": "I.", "surname": "Paul", "position": "Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "G. Small", "canonical_name": "Small, G.", "given_names": "G.", "surname": "Small", "position": "Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "J. E. F. Douay", "canonical_name": "Douay, J. E. F.", "given_names": "J. E. F.", "surname": "Douay", "position": "Assistant Conservator of Forests", "department": "FORESTRY - Sierra Leone", "salary_scale": "A"},
    {"name": "R. A. Price", "canonical_name": "Price, R. A.", "given_names": "R. A.", "surname": "Price", "position": "Forest Engineer", "department": "FORESTRY - Sierra Leone", "salary_scale": "B"},
    {"name": "J. D. Pollett", "canonical_name": "Pollett, J. D.", "given_names": "J. D.", "surname": "Pollett", "position": "Director of Geological Survey", "department": "Geological Survey - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "C. O. Baker", "canonical_name": "Baker, C. O.", "given_names": "C. O.", "surname": "Baker", "position": "Geologist", "department": "Geological Survey - Sierra Leone", "salary_scale": "A"},
    {"name": "J. V. Buller", "canonical_name": "Buller, J. V.", "given_names": "J. V.", "surname": "Buller", "position": "Geologist", "department": "Geological Survey - Sierra Leone", "salary_scale": "A"},
    {"name": "P. A. Ashworth", "canonical_name": "Ashworth, P. A.", "given_names": "P. A.", "surname": "Ashworth", "position": "Geologist", "department": "Geological Survey - Sierra Leone", "salary_scale": "A"},
    {"name": "J. Middleton", "canonical_name": "Middleton, J.", "given_names": "J.", "surname": "Middleton", "position": "Geologist", "department": "Geological Survey - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()