"""
Sierra Leone Colonial Office List 1913 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1913

OFFICIALS = [
    {"name": "R. F. Hunter", "canonical_name": "Hunter, R. F.", "given_names": "R. F.", "surname": "Hunter", "position": "Director of Education", "department": "Educational Department - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "R. Lean", "canonical_name": "Lean, R.", "given_names": "R.", "surname": "Lean", "position": "Principal, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 450, "salary_max": 500},
    {"name": "W. J. Holloway", "canonical_name": "Holloway, W. J.", "given_names": "W. J.", "surname": "Holloway", "position": "Vice-Principal, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 400, "salary_max": 450},
    {"name": "Miss M. M. McAllister", "canonical_name": "McAllister, M. M.", "given_names": "M. M.", "surname": "McAllister", "position": "Instructress, Model School", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300},
    {"name": "M. J. Marke", "canonical_name": "Marke, M. J.", "given_names": "M. J.", "surname": "Marke", "position": "Chief Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "50l. personal"},
    {"name": "S. J. Taylor", "canonical_name": "Taylor, S. J.", "given_names": "S. J.", "surname": "Taylor", "position": "Chief Inspector of Schools", "department": "Educational Department - Sierra Leone", "salary_min": 150, "salary_max": 200},
    {"name": "H. Deen", "canonical_name": "Deen, H.", "given_names": "H.", "surname": "Deen", "position": "Second Grade Clerk", "department": "Educational Department - Sierra Leone", "salary_min": 130, "salary_max": 160},
    {"name": "F. J. Hollist", "canonical_name": "Hollist, F. J.", "given_names": "F. J.", "surname": "Hollist", "position": "Fifth Clerk", "department": "Educational Department - Sierra Leone", "salary_min": 50, "salary_max": 70},
    {"name": "W. Hopkins", "canonical_name": "Hopkins, W.", "given_names": "W.", "surname": "Hopkins", "position": "Director of Agriculture", "department": "Agricultural Department - Sierra Leone", "salary_min": 600, "salary_max": 600, "duty_allowance": 120},
    {"name": "D. W. Scotland", "canonical_name": "Scotland, D. W.", "given_names": "D. W.", "surname": "Scotland", "position": "Assistant in Agricultural Department", "department": "Agricultural Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "A. N. Forster", "canonical_name": "Forster, A. N.", "given_names": "A. N.", "surname": "Forster", "position": "Veterinary Officer", "department": "Agricultural Department - Sierra Leone", "salary_min": 450, "salary_max": 500},
    {"name": "C. E. Lane-Poole", "canonical_name": "Lane-Poole, C. E.", "given_names": "C. E.", "surname": "Lane-Poole", "position": "Conservator of Forests", "department": "Forestry Department - Sierra Leone", "salary_min": 600, "salary_max": 600, "duty_allowance": 100},
    {"name": "G. Aylmer", "canonical_name": "Aylmer, G.", "given_names": "G.", "surname": "Aylmer", "position": "Assistant Conservator", "department": "Forestry Department - Sierra Leone", "salary_min": 300, "salary_max": 400},
    {"name": "J. Hartley", "canonical_name": "Hartley, J.", "given_names": "J.", "surname": "Hartley", "position": "Overseer", "department": "Forestry Department - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "12l. personal"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()