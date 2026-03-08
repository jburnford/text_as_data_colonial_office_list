"""
Gold Coast Colonial Office List 1896 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1896

OFFICIALS = [
    {"name": "J. P. Smartt", "position": "Superintendent of Roads", "department": "Roads Department - Gold Coast", "salary_min": 400, "salary_max": 500},
    {"name": "G. E. Ferguson", "position": "Surveyor of Roads", "department": "Roads Department - Gold Coast", "salary_min": 300, "salary_max": 360},
    {"name": "James Harding", "position": "Road Constructor", "department": "Roads Department - Gold Coast", "salary_min": 150, "salary_max": 150},
    {"name": "P. J. Daly", "position": "Road Constructor", "department": "Roads Department - Gold Coast", "salary_min": 150, "salary_max": 150},
    {"name": "F. Bartels", "position": "Road Constructor", "department": "Roads Department - Gold Coast", "salary_min": 125, "salary_max": 125, "acting_status": "acting"},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()