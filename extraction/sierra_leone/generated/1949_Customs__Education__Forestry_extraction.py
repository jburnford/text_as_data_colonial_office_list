"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "H. M. Lucie-Smith", "canonical_name": "Lucie-Smith, H. M.", "given_names": "H. M.", "surname": "Lucie-Smith", "position": "Comptroller of Customs", "department": "Customs - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "C. E. Leembruggen", "canonical_name": "Leembruggen, C. E.", "given_names": "C. E.", "surname": "Leembruggen", "position": "Assistant Comptroller of Customs", "department": "Customs - Sierra Leone", "salary_scale": "B"},
    {"name": "A. A. Short", "canonical_name": "Short, A. A.", "given_names": "A. A.", "surname": "Short", "position": "Collector of Customs", "department": "Customs - Sierra Leone", "honors": ["M.B.E."], "salary_scale": "B"},
    {"name": "C. E. Donovan", "canonical_name": "Donovan, C. E.", "given_names": "C. E.", "surname": "Donovan", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "allowances": "£150 non-pensionable allowance as Education Adviser to the Government of the Gambia"},
    {"name": "R. C. Allen", "canonical_name": "Allen, R. C.", "given_names": "R. C.", "surname": "Allen", "position": "Principal Education Officer", "department": "Education - Sierra Leone", "salary_min": 1100, "salary_max": 1100},
    {"name": "C. L. Rice", "canonical_name": "Rice, C. L.", "given_names": "C. L.", "surname": "Rice", "position": "Education Officer", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "T. D. Evans", "canonical_name": "Evans, T. D.", "given_names": "T. D.", "surname": "Evans", "position": "Education Officer", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "A. D. J. Scott", "canonical_name": "Scott, A. D. J.", "given_names": "A. D. J.", "surname": "Scott", "position": "Education Officer", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "A. L. Gibbs", "canonical_name": "Gibbs, A. L.", "given_names": "A. L.", "surname": "Gibbs", "position": "Education Officer", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "C. E. Tuboku-Metzger", "canonical_name": "Tuboku-Metzger, C. E.", "given_names": "C. E.", "surname": "Tuboku-Metzger", "position": "Education Officer", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "E. J. B. Williams", "canonical_name": "Williams, E. J. B.", "given_names": "E. J. B.", "surname": "Williams", "position": "Education Officer", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "S. M. Broderick", "canonical_name": "Broderick, S. M.", "given_names": "S. M.", "surname": "Broderick", "position": "Assistant Director of Education (Sierra Leone)", "department": "Education - Sierra Leone", "honors": ["M.B.E."], "salary_scale": "A"},
    {"name": "Miss M. R. Grigor", "canonical_name": "Grigor, M. R.", "given_names": "M. R.", "surname": "Grigor", "position": "Senior Lady Education Officer", "department": "Education - Sierra Leone", "salary_scale": "C3"},
    {"name": "J. V. Taylor", "canonical_name": "Taylor, J. V.", "given_names": "J. V.", "surname": "Taylor", "position": "Principal, Prince of Wales School", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "D. H. Hodgson", "canonical_name": "Hodgson, D. H.", "given_names": "D. H.", "surname": "Hodgson", "position": "Conservator of Forests", "department": "Forestry - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "R. S. Pelly", "canonical_name": "Pelly, R. S.", "given_names": "R. S.", "surname": "Pelly", "position": "Senior Assistant Conservators of Forests", "department": "Forestry - Sierra Leone", "salary_scale": "A"},
    {"name": "H. C. King", "canonical_name": "King, H. C.", "given_names": "H. C.", "surname": "King", "position": "Senior Assistant Conservators of Forests", "department": "Forestry - Sierra Leone", "salary_scale": "A"},
    {"name": "G. E. Crichton", "canonical_name": "Crichton, G. E.", "given_names": "G. E.", "surname": "Crichton", "position": "Assistant Conservators of Forests", "department": "Forestry - Sierra Leone", "salary_scale": "A"},
    {"name": "J. K. Ross", "canonical_name": "Ross, J. K.", "given_names": "J. K.", "surname": "Ross", "position": "Assistant Conservators of Forests", "department": "Forestry - Sierra Leone", "salary_scale": "A"},
    {"name": "R. M. Palmer", "canonical_name": "Palmer, R. M.", "given_names": "R. M.", "surname": "Palmer", "position": "Assistant Conservators of Forests", "department": "Forestry - Sierra Leone", "salary_scale": "A"},
    {"name": "A. J. Browning", "canonical_name": "Browning, A. J.", "given_names": "A. J.", "surname": "Browning", "position": "Assistant Conservators of Forests", "department": "Forestry - Sierra Leone", "salary_scale": "A"},
    {"name": "A. C. Frith", "canonical_name": "Frith, A. C.", "given_names": "A. C.", "surname": "Frith", "position": "Assistant Conservators of Forests", "department": "Forestry - Sierra Leone", "salary_scale": "A"},
    {"name": "I. G. Bulmer", "canonical_name": "Bulmer, I. G.", "given_names": "I. G.", "surname": "Bulmer", "position": "Assistant Conservators of Forests", "department": "Forestry - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()