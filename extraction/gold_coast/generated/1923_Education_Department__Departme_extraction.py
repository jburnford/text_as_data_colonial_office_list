"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "D. J. Oman", "canonical_name": "Oman, D. J.", "given_names": "D. J.", "surname": "Oman",
     "position": "Director of Education", "department": "Education Department - Gold Coast", "salary_min": 1200, "duty_allowance": 240},
    {"name": "R. F. Houter", "canonical_name": "Houter, R. F.", "given_names": "R. F.", "surname": "Houter",
     "position": "Deputy Director of Education", "department": "Education Department - Gold Coast", "salary_min": 1050, "duty_allowance": 210},
    {"name": "R. P. W. Mayall", "canonical_name": "Mayall, R. P. W.", "given_names": "R. P. W.", "surname": "Mayall",
     "position": "Senior Inspector of Schools", "department": "Education Department - Gold Coast", "salary_min": 1050, "duty_allowance": 210},
    {"name": "J. P. Robertson", "canonical_name": "Robertson, J. P.", "given_names": "J. P.", "surname": "Robertson",
     "position": "Provincial Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72},
    {"name": "A. Gardner", "canonical_name": "Gardner, A.", "given_names": "A.", "surname": "Gardner",
     "position": "Provincial Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72},
    {"name": "H. A. Wright", "canonical_name": "Wright, H. A.", "given_names": "H. A.", "surname": "Wright",
     "position": "Provincial Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72},
    {"name": "H. Blackmore", "canonical_name": "Blackmore, H.", "given_names": "H.", "surname": "Blackmore",
     "position": "Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72},
    {"name": "A. Aitken", "canonical_name": "Aitken, A.", "given_names": "A.", "surname": "Aitken",
     "position": "Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72},
    {"name": "Capt. A. B. Douglas", "canonical_name": "Douglas, Capt. A. B.", "given_names": "A. B.", "surname": "Douglas",
     "position": "Inspectors of Schools", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72, "military_rank": "Captain"},
    {"name": "E. J. Enstics", "canonical_name": "Enstics, E. J.", "given_names": "E. J.", "surname": "Enstics",
     "position": "Shorthand Instructor and Office Assistant", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "Major D. Hedog-Jones", "canonical_name": "Hedog-Jones, Major D.", "given_names": "D.", "surname": "Hedog-Jones",
     "position": "Organizer of Practical Education", "department": "Education Department - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72, "military_rank": "Major"},
    {"name": "T. D. Cranston", "canonical_name": "Cranston, T. D.", "given_names": "T. D.", "surname": "Cranston",
     "position": "Acting Principal", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72, "acting_status": "Acting"},
    {"name": "J. Dewhurst", "canonical_name": "Dewhurst, J.", "given_names": "J.", "surname": "Dewhurst",
     "position": "Assistant Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72},
    {"name": "Capt. H. D. Harrison", "canonical_name": "Harrison, Capt. H. D.", "given_names": "H. D.", "surname": "Harrison",
     "position": "Assistant Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72, "military_rank": "Captain"},
    {"name": "Rev. A. H. Candler", "canonical_name": "Candler, Rev. A. H.", "given_names": "A. H.", "surname": "Candler",
     "position": "Assistant Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 920, "seniority_allowance": 72},
    {"name": "Rev. R. Fisher", "canonical_name": "Fisher, Rev. R.", "given_names": "R.", "surname": "Fisher",
     "position": "House Master", "department": "Education Department - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72},
    {"name": "H. McLaren", "canonical_name": "McLaren, H.", "given_names": "H.", "surname": "McLaren",
     "position": "Principal", "department": "Education Department - Gold Coast", "salary_min": 800, "salary_max": 920, "seniority_allowance": 72},
    {"name": "R. Horsley", "canonical_name": "Horsley, R.", "given_names": "R.", "surname": "Horsley",
     "position": "Housemaster", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "T. A. Calvin", "canonical_name": "Calvin, T. A.", "given_names": "T. A.", "surname": "Calvin",
     "position": "European Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "V. W. Wright", "canonical_name": "Wright, V. W.", "given_names": "V. W.", "surname": "Wright",
     "position": "European Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "D. J. Owen", "canonical_name": "Owen, D. J.", "given_names": "D. J.", "surname": "Owen",
     "position": "European Masters", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "J. S. McDermid", "canonical_name": "McDermid, J. S.", "given_names": "J. S.", "surname": "McDermid",
     "position": "Headmasters", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72},
    {"name": "Major E. St. J. Christophers", "canonical_name": "Christophers, Major E. St. J.", "given_names": "E. St. J.", "surname": "Christophers",
     "position": "Headmasters", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72, "military_rank": "Major"},
    {"name": "Capt. H. G. Hendrie", "canonical_name": "Hendrie, Capt. H. G.", "given_names": "H. G.", "surname": "Hendrie",
     "position": "Headmasters", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72, "military_rank": "Captain"},
    {"name": "H. G. Ardron", "canonical_name": "Ardron, H. G.", "given_names": "H. G.", "surname": "Ardron",
     "position": "Headmasters", "department": "Education Department - Gold Coast", "salary_min": 490, "salary_max": 920, "seniority_allowance": 72},
    {"name": "J. Spio-Garbrah", "canonical_name": "Spio-Garbrah, J.", "given_names": "J.", "surname": "Spio-Garbrah",
     "position": "Head Masters", "department": "Education Department - Gold Coast", "salary_min": 400, "salary_max": 780},
    {"name": "Jon. Attram", "canonical_name": "Attram, Jon.", "given_names": "Jon.", "surname": "Attram",
     "position": "Head Masters", "department": "Education Department - Gold Coast", "salary_min": 400, "salary_max": 780},
    {"name": "J. D. Cranston (Mrs.)", "canonical_name": "Cranston, J. D. (Mrs.)", "given_names": "J. D.", "surname": "Cranston",
     "position": "Head Mistresses", "department": "Education Department - Gold Coast", "salary_min": 480, "salary_max": 720},
    {"name": "M. K. Quartery-Papafio", "canonical_name": "Quartey-Papafio, M. K.", "given_names": "M. K.", "surname": "Quartey-Papafio",
     "position": "Head Mistresses", "department": "Education Department - Gold Coast", "salary_min": 400, "salary_max": 780},
    {"name": "W. S. D. Tudhope", "canonical_name": "Tudhope, W. S. D.", "given_names": "W. S. D.", "surname": "Tudhope",
     "position": "Director of Agriculture", "department": "Department of Agriculture - Gold Coast", "salary_min": 1200, "duty_allowance": 240},
    {"name": "Lieut.-Colonel A. Ogilvy", "canonical_name": "Ogilvy, Lieut.-Colonel A.", "given_names": "A.", "surname": "Ogilvy",
     "position": "Deputy Director of Agriculture", "department": "Department of Agriculture - Gold Coast", "salary_min": 1000, "duty_allowance": 200, "military_rank": "Lieutenant-Colonel"},
    {"name": "J. M. Dunbar", "canonical_name": "Dunbar, J. M.", "given_names": "J. M.", "surname": "Dunbar",
     "position": "Secretary", "department": "Department of Agriculture - Gold Coast", "salary_min": 450, "salary_max": 720},
    {"name": "R. H. Bunting", "canonical_name": "Bunting, R. H.", "given_names": "R. H.", "surname": "Bunting",
     "position": "Government Mycologist and Assistant Director of Agriculture (Scientific)", "department": "Research Branch - Gold Coast", "salary_min": 960, "duty_allowance": 96},
    {"name": "W. H. Patterson", "canonical_name": "Patterson, W. H.", "given_names": "W. H.", "surname": "Patterson",
     "position": "Government Entomologist", "department": "Research Branch - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72},
    {"name": "H. A. Dade", "canonical_name": "Dade, H. A.", "given_names": "H. A.", "surname": "Dade",
     "position": "Assistant Mycologist", "department": "Research Branch - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72},
    {"name": "G. S. Cotterell", "canonical_name": "Cotterell, G. S.", "given_names": "G. S.", "surname": "Cotterell",
     "position": "Assistant Entomologist", "department": "Research Branch - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72},
    {"name": "R. Coull", "canonical_name": "Coull, R.", "given_names": "R.", "surname": "Coull",
     "position": "Agricultural Chemists", "department": "Research Branch - Gold Coast", "salary_min": 600, "salary_max": 920, "seniority_allowance": 72},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()