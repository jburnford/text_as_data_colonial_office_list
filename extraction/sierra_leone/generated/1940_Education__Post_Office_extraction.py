"""
Sierra Leone Colonial Office List 1940 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1940

OFFICIALS = [
    {"name": "W. E. Nicholson", "canonical_name": "Nicholson, W. E.", "given_names": "W. E.", "surname": "Nicholson", "position": "Director of Education", "department": "Education - Sierra Leone", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "H. E. T. Hodgson", "canonical_name": "Hodgson, H. E. T.", "given_names": "H. E. T.", "surname": "Hodgson", "position": "Senior Education Officer", "department": "Education - Sierra Leone", "salary_min": 840, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "S. Milburn", "canonical_name": "Milburn, S.", "given_names": "S.", "surname": "Milburn", "position": "Senior Education Officer", "department": "Education - Sierra Leone", "salary_min": 840, "salary_max": 920, "allowances": "72l. seniority allowance"},
    {"name": "W. J. Davies", "canonical_name": "Davies, W. J.", "given_names": "W. J.", "surname": "Davies", "position": "Principal, Prince of Wales School", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "C. P. Ellis", "canonical_name": "Ellis, C. P.", "given_names": "C. P.", "surname": "Ellis", "position": "Education Officer", "department": "Education - Sierra Leone", "salary_scale": "A"},
    {"name": "H. Earnshaw", "canonical_name": "Earnshaw, H.", "given_names": "H.", "surname": "Earnshaw", "position": "Education Officer", "department": "Education - Sierra Leone", "salary_min": 400, "salary_max": 840},
    {"name": "D. R. Buxton", "canonical_name": "Buxton, D. R.", "given_names": "D. R.", "surname": "Buxton", "position": "Education Officer", "department": "Education - Sierra Leone", "salary_min": 400, "salary_max": 840},
    {"name": "Miss A. M. McMath", "canonical_name": "McMath, A. M.", "given_names": "A. M.", "surname": "McMath", "position": "Lady Education Officer", "department": "Education - Sierra Leone", "salary_min": 500, "salary_max": 720},
    {"name": "S. M. Broderick", "canonical_name": "Broderick, S. M.", "given_names": "S. M.", "surname": "Broderick", "position": "Assistant Director of Education (Sierra Leone)", "department": "Education - Sierra Leone", "salary_min": 360, "salary_max": 500},
    {"name": "C. R. Rowlands", "canonical_name": "Rowlands, C. R.", "given_names": "C. R.", "surname": "Rowlands", "position": "Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "C. J. Tilt", "canonical_name": "Tilt, C. J.", "given_names": "C. J.", "surname": "Tilt", "position": "Assistant Postmaster General", "department": "Post Office - Sierra Leone", "salary_min": 660, "salary_max": 810},
    {"name": "E. S. B. Francis", "canonical_name": "Francis, E. S. B.", "given_names": "E. S. B.", "surname": "Francis", "position": "Staff Superintendent", "department": "Post Office - Sierra Leone", "salary_min": 310, "salary_max": 450}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()