"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "F. MacLagan", "canonical_name": "MacLagan, F.", "given_names": "F.", "surname": "MacLagan", "position": "Director of Medical Services", "department": "Medical - Sierra Leone", "salary_min": 1500, "salary_max": 1500},
    {"name": "E. A. Renner", "canonical_name": "Renner, E. A.", "given_names": "E. A.", "surname": "Renner", "position": "Assistant Director of Medical Services", "department": "Medical - Sierra Leone", "salary_min": 1350, "salary_max": 1350, "honors": ["O.B.E."]},
    {"name": "W. M. Quin", "canonical_name": "Quin, W. M.", "given_names": "W. M.", "surname": "Quin", "position": "Specialists", "department": "Medical - Sierra Leone", "salary_min": 1300, "salary_max": 1300},
    {"name": "P. C. Cosgrove", "canonical_name": "Cosgrove, P. C.", "given_names": "P. C.", "surname": "Cosgrove", "position": "Specialists", "department": "Medical - Sierra Leone", "salary_min": 1300, "salary_max": 1300},
    {"name": "H. Peaston", "canonical_name": "Peaston, H.", "given_names": "H.", "surname": "Peaston", "position": "Senior Medical Officer", "department": "Medical - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "M. A. S. Margai", "canonical_name": "Margai, M. A. S.", "given_names": "M. A. S.", "surname": "Margai", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A", "honors": ["M.B.E."]},
    {"name": "A. J. Johnson", "canonical_name": "Johnson, A. J.", "given_names": "A. J.", "surname": "Johnson", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "M2"},
    {"name": "Miss S. M. Young", "canonical_name": "Young, S. M.", "given_names": "S. M.", "surname": "Young", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "C. A. McComiskey", "canonical_name": "McComiskey, C. A.", "given_names": "C. A.", "surname": "McComiskey", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "A. B. Abayomi-Cole", "canonical_name": "Abayomi-Cole, A. B.", "given_names": "A. B.", "surname": "Abayomi-Cole", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "A. S. Boyle-Hebron", "canonical_name": "Boyle-Hebron, A. S.", "given_names": "A. S.", "surname": "Boyle-Hebron", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "A. F. Tuboku-Metzger", "canonical_name": "Tuboku-Metzger, A. F.", "given_names": "A. F.", "surname": "Tuboku-Metzger", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "C. H. J. Baker", "canonical_name": "Baker, C. H. J.", "given_names": "C. H. J.", "surname": "Baker", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "D. E. Boye-Johnson", "canonical_name": "Boye-Johnson, D. E.", "given_names": "D. E.", "surname": "Boye-Johnson", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "W. R. Rochester", "canonical_name": "Rochester, W. R.", "given_names": "W. R.", "surname": "Rochester", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "F. I. C. Apted", "canonical_name": "Apted, F. I. C.", "given_names": "F. I. C.", "surname": "Apted", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "S. Caruana", "canonical_name": "Caruana, S.", "given_names": "S.", "surname": "Caruana", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "N. G. D. Campbell", "canonical_name": "Campbell, N. G. D.", "given_names": "N. G. D.", "surname": "Campbell", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "Miss S. E. J. Wright", "canonical_name": "Wright, S. E. J.", "given_names": "S. E. J.", "surname": "Wright", "position": "Medical Officers", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "D. Gollan", "canonical_name": "Gollan, D.", "given_names": "D.", "surname": "Gollan", "position": "Government Dentists", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "C. E. F. Wright", "canonical_name": "Wright, C. E. F.", "given_names": "C. E. F.", "surname": "Wright", "position": "Government Dentists", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "Miss M. Gosden", "canonical_name": "Gosden, M.", "given_names": "M.", "surname": "Gosden", "position": "Senior Pathologist", "department": "Medical - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "J. D. Reid", "canonical_name": "Reid, J. D.", "given_names": "J. D.", "surname": "Reid", "position": "Pathologist", "department": "Medical - Sierra Leone", "salary_scale": "A"},
    {"name": "Miss F. M. Harmer", "canonical_name": "Harmer, F. M.", "given_names": "F. M.", "surname": "Harmer", "position": "Senior Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N2"},
    {"name": "Miss A. Stewart", "canonical_name": "Stewart, A.", "given_names": "A.", "surname": "Stewart", "position": "Senior Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N2", "honors": ["M.B.E."]},
    {"name": "Misses S. M. Gimson", "canonical_name": "Gimson, S. M.", "given_names": "S. M.", "surname": "Gimson", "position": "Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N1"},
    {"name": "O. V. K. Johnson", "canonical_name": "Johnson, O. V. K.", "given_names": "O. V. K.", "surname": "Johnson", "position": "Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N1"},
    {"name": "F. N. Beer", "canonical_name": "Beer, F. N.", "given_names": "F. N.", "surname": "Beer", "position": "Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N1"},
    {"name": "C. R. Duguid", "canonical_name": "Duguid, C. R.", "given_names": "C. R.", "surname": "Duguid", "position": "Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N1"},
    {"name": "M. C. Thompson", "canonical_name": "Thompson, M. C.", "given_names": "M. C.", "surname": "Thompson", "position": "Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N1"},
    {"name": "Mrs. C. Lightfoot-Boston", "canonical_name": "Lightfoot-Boston, C.", "given_names": "C.", "surname": "Lightfoot-Boston", "position": "Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N1"},
    {"name": "Misses C. V. Price", "canonical_name": "Price, C. V.", "given_names": "C. V.", "surname": "Price", "position": "Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N1"},
    {"name": "A. Pratt", "canonical_name": "Pratt, A.", "given_names": "A.", "surname": "Pratt", "position": "Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N1"},
    {"name": "D. M. Hills", "canonical_name": "Hills, D. M.", "given_names": "D. M.", "surname": "Hills", "position": "Nursing Sisters", "department": "Medical - Sierra Leone", "salary_scale": "N1"},
    {"name": "R. Elliott", "canonical_name": "Elliott, R.", "given_names": "R.", "surname": "Elliott", "position": "Malaria Entomologist", "department": "Medical - Sierra Leone", "salary_scale": "A"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()