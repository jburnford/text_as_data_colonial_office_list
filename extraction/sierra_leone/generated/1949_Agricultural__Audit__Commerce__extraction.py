"""
Sierra Leone Colonial Office List 1949 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1949

OFFICIALS = [
    {"name": "R. R. Glanville", "canonical_name": "Glanville, R. R.", "given_names": "R. R.", "surname": "Glanville", "position": "Director of Agriculture", "department": "Agricultural - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "honors": ["C.B.E."]},
    {"name": "G. W. Lines", "canonical_name": "Lines, G. W.", "given_names": "G. W.", "surname": "Lines", "position": "Principal Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "honors": ["M.B.E."]},
    {"name": "F. C. Deighton", "canonical_name": "Deighton, F. C.", "given_names": "F. C.", "surname": "Deighton", "position": "Plant Pathologist", "department": "Agricultural - Sierra Leone", "salary_scale": "A", "honors": ["O.B.E."]},
    {"name": "F. A. Squire", "canonical_name": "Squire, F. A.", "given_names": "F. A.", "surname": "Squire", "position": "Entomologist", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "H. Macluskie", "canonical_name": "Macluskie, H.", "given_names": "H.", "surname": "Macluskie", "position": "Senior Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "A. F. Mackenzie", "canonical_name": "Mackenzie, A. F.", "given_names": "A. F.", "surname": "Mackenzie", "position": "Senior Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "E. I. Nisbett", "canonical_name": "Nisbett, E. I.", "given_names": "E. I.", "surname": "Nisbett", "position": "Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "R. M. Steven", "canonical_name": "Steven, R. M.", "given_names": "R. M.", "surname": "Steven", "position": "Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "P. Adames", "canonical_name": "Adames, P.", "given_names": "P.", "surname": "Adames", "position": "Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "E. S. Capstick", "canonical_name": "Capstick, E. S.", "given_names": "E. S.", "surname": "Capstick", "position": "Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "H. D. Jordan", "canonical_name": "Jordan, H. D.", "given_names": "H. D.", "surname": "Jordan", "position": "Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "T. P. Wheldon", "canonical_name": "Wheldon, T. P.", "given_names": "T. P.", "surname": "Wheldon", "position": "Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "J. M. Dent", "canonical_name": "Dent, J. M.", "given_names": "J. M.", "surname": "Dent", "position": "Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "T. S. Jones", "canonical_name": "Jones, T. S.", "given_names": "T. S.", "surname": "Jones", "position": "Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "J. A. Austin", "canonical_name": "Austin, J. A.", "given_names": "J. A.", "surname": "Austin", "position": "Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "E. H. Nichols", "canonical_name": "Nichols, E. H.", "given_names": "E. H.", "surname": "Nichols", "position": "Agricultural Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "H. W. Dougall", "canonical_name": "Dougall, H. W.", "given_names": "H. W.", "surname": "Dougall", "position": "Agricultural Chemist", "department": "Agricultural - Sierra Leone", "salary_scale": "A"},
    {"name": "S. M. Taylor", "canonical_name": "Taylor, S. M.", "given_names": "S. M.", "surname": "Taylor", "position": "Marketing Officer", "department": "Agricultural - Sierra Leone", "salary_scale": "A", "military_rank": "Major"},
    {"name": "F. P. L. Derriman", "canonical_name": "Derriman, F. P. L.", "given_names": "F. P. L.", "surname": "Derriman", "position": "Director of Audit", "department": "Audit - Sierra Leone", "salary_min": 1150, "salary_max": 1150},
    {"name": "D. P. Uttey", "canonical_name": "Uttey, D. P.", "given_names": "D. P.", "surname": "Uttey", "position": "Senior Auditor", "department": "Audit - Sierra Leone", "salary_scale": "B"},
    {"name": "G. T. C. Morris", "canonical_name": "Morris, G. T. C.", "given_names": "G. T. C.", "surname": "Morris", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_scale": "B"},
    {"name": "A. C. Wilson", "canonical_name": "Wilson, A. C.", "given_names": "A. C.", "surname": "Wilson", "position": "Assistant Auditor", "department": "Audit - Sierra Leone", "salary_scale": "B"},
    {"name": "F. G. Winward", "canonical_name": "Winward, F. G.", "given_names": "F. G.", "surname": "Winward", "position": "Director", "department": "Commerce and Industry - Sierra Leone", "salary_min": 1350, "salary_max": 1350, "honors": ["C.B.E."]}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()