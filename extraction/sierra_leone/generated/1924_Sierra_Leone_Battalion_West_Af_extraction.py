"""
Sierra Leone Colonial Office List 1924 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1924

OFFICIALS = [
    {"name": "G. E. R. de Miremont", "canonical_name": "de Miremont, G. E. R.", "given_names": "G. E. R.", "surname": "de Miremont", "position": "Major", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 900, "salary_max": 900, "duty_allowance": 182, "honors": ["D.S.O.", "M.C."], "military_rank": "Major"},
    {"name": "F. W. Doke", "canonical_name": "Doke, F. W.", "given_names": "F. W.", "surname": "Doke", "position": "Adjutant and Quartermaster, Adjutant Lieut.", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "duty_allowance": 91, "military_rank": "Lieut."},
    {"name": "E. W. T. Rowe", "canonical_name": "Rowe, E. W. T.", "given_names": "E. W. T.", "surname": "Rowe", "position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Captain"},
    {"name": "C. C. Fowkes", "canonical_name": "Fowkes, C. C.", "given_names": "C. C.", "surname": "Fowkes", "position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "honors": ["M.C."], "military_rank": "Captain"},
    {"name": "P. Perfect", "canonical_name": "Perfect, P.", "given_names": "P.", "surname": "Perfect", "position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Captain"},
    {"name": "E. L. G. Beville", "canonical_name": "Beville, E. L. G.", "given_names": "E. L. G.", "surname": "Beville", "position": "Captains", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 700, "salary_max": 700, "military_rank": "Captain"},
    {"name": "A. Robertson", "canonical_name": "Robertson, A.", "given_names": "A.", "surname": "Robertson", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "N. B. Bradling", "canonical_name": "Bradling, N. B.", "given_names": "N. B.", "surname": "Bradling", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "R. M. Hall", "canonical_name": "Hall, R. M.", "given_names": "R. M.", "surname": "Hall", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "honors": ["M.C."], "military_rank": "Lieutenant"},
    {"name": "A. E. Salter", "canonical_name": "Salter, A. E.", "given_names": "A. E.", "surname": "Salter", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "honors": ["M.C."], "military_rank": "Lieutenant"},
    {"name": "V. J. Bradley", "canonical_name": "Bradley, V. J.", "given_names": "V. J.", "surname": "Bradley", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"},
    {"name": "S. H. Cave", "canonical_name": "Cave, S. H.", "given_names": "S. H.", "surname": "Cave", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "allowances": "46l. signalling allowance", "military_rank": "Lieutenant"},
    {"name": "S. H. Houle", "canonical_name": "Houle, S. H.", "given_names": "S. H.", "surname": "Houle", "position": "Lieutenants", "department": "Sierra Leone Battalion, WAFF - Sierra Leone", "salary_min": 510, "salary_max": 600, "military_rank": "Lieutenant"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()