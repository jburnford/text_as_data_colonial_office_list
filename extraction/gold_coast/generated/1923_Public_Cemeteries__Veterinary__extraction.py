"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "J. M. Dalziel", "position": "Registrar of Births and Deaths", "department": "Public Cemeteries - Gold Coast"},
    {"name": "Captain W. P. B. Beal", "canonical_name": "Beal, Captain W. P. B.", "given_names": "W. P. B.", "surname": "Beal", "position": "Principal Veterinary Officer", "department": "Veterinary Department - Gold Coast", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "military_rank": "Captain", "qualifications": ["M.R.C.V.S."]},
    {"name": "Capt. S. R. Rippon", "canonical_name": "Rippon, Capt. S. R.", "given_names": "S. R.", "surname": "Rippon", "position": "Veterinary Officers", "department": "Veterinary Department - Gold Coast", "salary_min": 600, "salary_max": 920, "military_rank": "Captain", "qualifications": ["M.R.C.V.S."], "seniority_allowance": 72},
    {"name": "Capt. D. G. Grealy", "canonical_name": "Grealy, Capt. D. G.", "given_names": "D. G.", "surname": "Grealy", "position": "Veterinary Officers", "department": "Veterinary Department - Gold Coast", "salary_min": 600, "salary_max": 920, "military_rank": "Captain", "qualifications": ["M.R.C.V.S."], "seniority_allowance": 72},
    {"name": "Lieut. A. E. Miller", "canonical_name": "Miller, Lieut. A. E.", "given_names": "A. E.", "surname": "Miller", "position": "Inspectors of Livestock", "department": "Veterinary Department - Gold Coast", "salary_min": 480, "salary_max": 720, "military_rank": "Lieut.", "honors": ["M.C."]},
    {"name": "Gurbakhsh Singh", "position": "Veterinary Superintendent", "department": "Veterinary Department - Gold Coast", "salary_min": 300, "salary_max": 400},
    {"name": "D. J. Oman", "position": "Director of Education", "department": "Education Department - Gold Coast", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "R. F. Houter", "position": "Deputy Director of Education", "department": "Education Department - Gold Coast", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "R. P. W. Mayall", "position": "Senior Inspector of Schools", "department": "Education Department - Gold Coast", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "J. P. Robertson", "position": "Provincial Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72},
    {"name": "A. Gardner", "position": "Provincial Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72},
    {"name": "H. A. Wright", "position": "Provincial Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72},
    {"name": "H. Blackmore", "position": "Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72},
    {"name": "A. Aitken", "position": "Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72},
    {"name": "Capt. A. B. Douglas", "canonical_name": "Douglas, Capt. A. B.", "given_names": "A. B.", "surname": "Douglas", "position": "Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "military_rank": "Captain", "seniority_allowance": 72},
    {"name": "E. J. Enstics", "position": "Shorthand Instructor and Office Assistant", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "Major D. Hedog-Jones", "canonical_name": "Hedog-Jones, Major D.", "given_names": "D.", "surname": "Hedog-Jones", "position": "Organizer of Practical Education", "department": "Education Department - Gold Coast", "salary_min": 600, "salary_max": 920, "military_rank": "Major", "seniority_allowance": 72},
    {"name": "T. D. Cranston", "position": "Acting Principal", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72, "acting_allowance": 120},
    {"name": "J. Dewhurst", "position": "Assistant Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72},
    {"name": "Capt. H. D. Harrison", "canonical_name": "Harrison, Capt. H. D.", "given_names": "H. D.", "surname": "Harrison", "position": "Assistant Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "military_rank": "Captain", "seniority_allowance": 72},
    {"name": "Rev. A. H. Candler", "canonical_name": "Candler, Rev. A. H.", "given_names": "A. H.", "surname": "Candler", "position": "Assistant Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72},
    {"name": "Rev. R. Fisher", "canonical_name": "Fisher, Rev. R.", "given_names": "R.", "surname": "Fisher", "position": "House Master", "department": "Education Department - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72},
    {"name": "H. McLaren", "position": "Principal", "department": "Education Department - Gold Coast", "salary_min": 800, "salary_max": 920, "seniority_allowance": 72},
    {"name": "R. Horsley", "position": "Housemaster", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "T. A. Calvin", "position": "European Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "V. W. Wright", "position": "European Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "D. J. Owen", "position": "European Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "J. S. McDermid", "position": "Headmasters", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72},
    {"name": "Major E. St. J. Christophers", "canonical_name": "Christophers, Major E. St. J.", "given_names": "E. St. J.", "surname": "Christophers", "position": "Headmasters", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "military_rank": "Major", "seniority_allowance": 72},
    {"name": "Capt. H. G. Hendrie", "canonical_name": "Hendrie, Capt. H. G.", "given_names": "H. G.", "surname": "Hendrie", "position": "Headmasters", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "military_rank": "Captain", "seniority_allowance": 72},
    {"name": "H. G. Ardron", "position": "Headmasters", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72},
    {"name": "J. Spio-Garbrah", "position": "Head Masters", "department": "Education Department - Gold Coast", "salary_min": 400, "salary_max": 780},
    {"name": "Jon. Attram", "position": "Head Masters", "department": "Education Department - Gold Coast", "salary_min": 400, "salary_max": 780},
    {"name": "J. D. Cranston (Mrs.)", "canonical_name": "Cranston, J. D. (Mrs.)", "given_names": "J. D.", "surname": "Cranston", "position": "Head Mistresses", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "M. K. Quartery-Papafio", "canonical_name": "Quartery-Papafio, M. K.", "given_names": "M. K.", "surname": "Quartery-Papafio", "position": "Head Mistresses", "department": "Education Department - Gold Coast", "salary_min": 400, "salary_max": 780},
    {"name": "W. S. D. Tudhope", "position": "Director of Agriculture", "department": "Department of Agriculture - Gold Coast", "salary_min": 1200, "salary_max": 1200, "duty_allowance": 240},
    {"name": "Lieut.-Colonel A. Ogilvy", "canonical_name": "Ogilvy, Lieut.-Colonel A.", "given_names": "A.", "surname": "Ogilvy", "position": "Deputy Director of Agriculture", "department": "Department of Agriculture - Gold Coast", "salary_min": 1000, "salary_max": 1000, "duty_allowance": 200, "military_rank": "Lieut.-Colonel", "qualifications": ["N.D.D."]},
    {"name": "J. M. Dunbar", "position": "Secretary", "department": "Department of Agriculture - Gold Coast", "salary_min": 450, "salary_max": 720},
    {"name": "R. H. Bunting", "position": "Government Mycologist and Assistant Director of Agriculture (Scientific)", "department": "Research Branch - Gold Coast", "salary_min": 960, "salary_max": 960, "duty_allowance": 96, "qualifications": ["F.L.S."]},
    {"name": "W. H. Patterson", "position": "Government Entomologist", "department": "Research Branch - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72},
    {"name": "H. A. Dade", "position": "Assistant Mycologist", "department": "Research Branch - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72, "qualifications": ["A.R.C.S."]},
    {"name": "G. S. Cotterell", "position": "Assistant Entomologist", "department": "Research Branch - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72, "qualifications": ["A.R.C.S.", "F.E.S."]},
    {"name": "R. Coull", "position": "Agricultural Chemists", "department": "Research Branch - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72, "qualifications": ["B.Sc."]},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()