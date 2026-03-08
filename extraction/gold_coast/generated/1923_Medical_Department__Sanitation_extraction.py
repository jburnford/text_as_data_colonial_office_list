"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "J. M. Dalziel", "position": "Deputy Director of Sanitary Services", "department": "Medical Department. / Sanitation Branch.", "salary_min": 1300, "duty_allowance": 260},
    {"name": "A. C. Lorena", "position": "Senior Sanitary Officers", "department": "Medical Department. / Sanitation Branch.", "salary_min": 1050, "salary_max": 1200, "duty_allowance": 210},
    {"name": "H. O'Hara May", "position": "Senior Sanitary Officers", "department": "Medical Department. / Sanitation Branch.", "salary_min": 1050, "salary_max": 1200, "duty_allowance": 210},
    {"name": "W. G. Watt", "position": "Medical Officers of Health", "department": "Medical Department. / Sanitation Branch.", "salary_min": 1000, "salary_max": 1150, "seniority_allowance": 100, "staff_pay": 150},
    {"name": "T. A. Downe", "position": "Medical Officers of Health", "department": "Medical Department. / Sanitation Branch.", "salary_min": 1000, "salary_max": 1150, "seniority_allowance": 100, "staff_pay": 150},
    {"name": "D. J. F. O'Donoghue", "position": "Medical Officers of Health", "department": "Medical Department. / Sanitation Branch.", "salary_min": 800, "salary_max": 960, "seniority_allowance": 72, "staff_pay": 150},
    {"name": "P. S. Selwyn-Clarke", "position": "Medical Officers of Health", "department": "Medical Department. / Sanitation Branch.", "salary_min": 800, "salary_max": 960, "seniority_allowance": 72, "staff_pay": 150},
    {"name": "G. C. M. Davies", "position": "Medical Officers of Health", "department": "Medical Department. / Sanitation Branch.", "salary_min": 800, "salary_max": 960, "seniority_allowance": 72, "staff_pay": 150},
    {"name": "J. A. A. Duncan", "position": "Medical Officers of Health", "department": "Medical Department. / Sanitation Branch.", "salary_min": 800, "salary_max": 960, "seniority_allowance": 72, "staff_pay": 150},
    {"name": "H. T. Lucas", "position": "Superintending Sanitary Inspector", "department": "Medical Department. / Sanitation Branch.", "salary_min": 440, "salary_max": 500},
    {"name": "E. G. Gray", "position": "Superintending Sanitary Inspector", "department": "Medical Department. / Sanitation Branch.", "salary_min": 440, "salary_max": 500},
    {"name": "P. P. Horn", "position": "Superintending Sanitary Inspector", "department": "Medical Department. / Sanitation Branch.", "salary_min": 440, "salary_max": 500},
    {"name": "V. R. Coe", "position": "Superintending Sanitary Inspector", "department": "Medical Department. / Sanitation Branch.", "salary_min": 440, "salary_max": 500},
    {"name": "J. C. Barnor", "position": "Chief Clerk", "department": "Medical Department. / Sanitation Branch.", "salary_min": 300, "salary_max": 396},
    {"name": "C. M. G. Hoyte", "position": "Sanitary Inspector and Training Officer", "department": "Medical Department. / Sanitation Branch.", "salary_min": 300, "salary_max": 396},
    {"name": "S. Parkinson Bruce", "position": "Vaccinator", "department": "Medical Department. / Sanitation Branch.", "salary_min": 300, "salary_max": 396},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()