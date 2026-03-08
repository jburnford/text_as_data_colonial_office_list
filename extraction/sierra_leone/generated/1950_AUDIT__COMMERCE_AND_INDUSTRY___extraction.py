"""
Sierra Leone Colonial Office List 1950 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1950

OFFICIALS = [
    {"name": "F. P. L. Derriman", "canonical_name": "Derriman, F. P. L.", "given_names": "F. P. L.", "surname": "Derriman", "position": "Director of Audit", "department": "AUDIT - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Senior Auditor", "department": "AUDIT - Sierra Leone", "salary_scale": "B"},
    {"name": "G. T. C. Morris", "canonical_name": "Morris, G. T. C.", "given_names": "G. T. C.", "surname": "Morris", "position": "Assistant Auditor", "department": "AUDIT - Sierra Leone", "salary_scale": "B"},
    {"name": "A. C. Wilson", "canonical_name": "Wilson, A. C.", "given_names": "A. C.", "surname": "Wilson", "position": "Assistant Auditor", "department": "AUDIT - Sierra Leone", "salary_scale": "B"},
    {"name": "F. G. Winward", "canonical_name": "Winward, F. G.", "given_names": "F. G.", "surname": "Winward", "position": "Director", "department": "COMMERCE AND INDUSTRY - Sierra Leone", "salary_min": 1200, "salary_max": 1200, "honors": ["C.B.E."]},
    {"name": "E. J. D. Cross", "canonical_name": "Cross, E. J. D.", "given_names": "E. J. D.", "surname": "Cross", "position": "Commercial Assistant", "department": "COMMERCE AND INDUSTRY - Sierra Leone", "salary_scale": "B"},
    {"name": "J. Thorpe", "canonical_name": "Thorpe, J.", "given_names": "J.", "surname": "Thorpe", "position": "Commercial Assistant", "department": "COMMERCE AND INDUSTRY - Sierra Leone", "salary_scale": "B"},
    {"name": "S. B. Nicol-Cole", "canonical_name": "Nicol-Cole, S. B.", "given_names": "S. B.", "surname": "Nicol-Cole", "position": "Commercial Assistant", "department": "COMMERCE AND INDUSTRY - Sierra Leone", "salary_scale": "B"},
    {"name": "H. M. Lucie-Smith", "canonical_name": "Lucie-Smith, H. M.", "given_names": "H. M.", "surname": "Lucie-Smith", "position": "Comptroller of Customs", "department": "CUSTOMS - Sierra Leone", "salary_min": 1200, "salary_max": 1200},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Comptroller of Customs", "department": "CUSTOMS - Sierra Leone", "salary_min": 660, "salary_max": 900},
    {"name": "C. A. Asgill", "canonical_name": "Asgill, C. A.", "given_names": "C. A.", "surname": "Asgill", "position": "Collector of Customs", "department": "CUSTOMS - Sierra Leone", "salary_scale": "B"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()