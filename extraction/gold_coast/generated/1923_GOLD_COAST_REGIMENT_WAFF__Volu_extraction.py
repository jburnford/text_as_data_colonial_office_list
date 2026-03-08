"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "Lieut.-Colonel J. R. Meiklejohn", "canonical_name": "Meiklejohn, J. R.", "given_names": "J. R.", "surname": "Meiklejohn", "position": "Commanding Officer", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut.-Colonel", "honors": ["D.S.O."]},
    {"name": "Capt. I. H. Maconell", "canonical_name": "Maconell, I. H.", "given_names": "I. H.", "surname": "Maconell", "position": "Second in Command, acting", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Capt.", "honors": ["D.S.O."]},
    {"name": "Lieut. W. M. Harrington", "canonical_name": "Harrington, W. M.", "given_names": "W. M.", "surname": "Harrington", "position": "Adjutant", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut.", "honors": ["M.C.", "M.M."]},
    {"name": "Lieut. A. W. Valentine", "canonical_name": "Valentine, A. W.", "given_names": "A. W.", "surname": "Valentine", "position": "Assistant Adjutant", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut.", "honors": ["M.B.E."]},
    {"name": "Capt. H. E. Allen", "canonical_name": "Allen, H. E.", "given_names": "H. E.", "surname": "Allen", "position": "Captains of Infantry", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Capt."},
    {"name": "Capt. R. M. Lees", "canonical_name": "Lees, R. M.", "given_names": "R. M.", "surname": "Lees", "position": "Captains of Infantry", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Capt."},
    {"name": "Capt. R. C. Wynter", "canonical_name": "Wynter, R. C.", "given_names": "R. C.", "surname": "Wynter", "position": "Captains of Infantry", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Capt.", "honors": ["M.C."]},
    {"name": "Capt. W. L. R. Dryland", "canonical_name": "Dryland, W. L. R.", "given_names": "W. L. R.", "surname": "Dryland", "position": "Captains of Infantry", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Capt."},
    {"name": "Capt. J. E. Law", "canonical_name": "Law, J. E.", "given_names": "J. E.", "surname": "Law", "position": "Captains of Infantry", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Capt."},
    {"name": "Capt. E. C. Downes", "canonical_name": "Downes, E. C.", "given_names": "E. C.", "surname": "Downes", "position": "Captains of Infantry", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Capt."},
    {"name": "Capt. E. G. Jonas", "canonical_name": "Jonas, E. G.", "given_names": "E. G.", "surname": "Jonas", "position": "Captains of Infantry", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Capt."},
    {"name": "Capt. C. R. Smith", "canonical_name": "Smith, C. R.", "given_names": "C. R.", "surname": "Smith", "position": "Quartermaster", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Capt."},
    {"name": "Lieut. G. E. Edwards", "canonical_name": "Edwards, G. E.", "given_names": "G. E.", "surname": "Edwards", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut.", "honors": ["M.C."]},
    {"name": "Lieut. W. R. Fuller", "canonical_name": "Fuller, W. R.", "given_names": "W. R.", "surname": "Fuller", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut."},
    {"name": "Lieut. C. H. Horsley", "canonical_name": "Horsley, C. H.", "given_names": "C. H.", "surname": "Horsley", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut.", "honors": ["M.C."]},
    {"name": "Lieut. G. O. H. Sergeant", "canonical_name": "Sergeant, G. O. H.", "given_names": "G. O. H.", "surname": "Sergeant", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut.", "honors": ["M.C."]},
    {"name": "Lieut. N. M. Gordon", "canonical_name": "Gordon, N. M.", "given_names": "N. M.", "surname": "Gordon", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut.", "honors": ["M.C."]},
    {"name": "Lieut. F. C. Prickett", "canonical_name": "Prickett, F. C.", "given_names": "F. C.", "surname": "Prickett", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut.", "honors": ["O.B.E.", "M.C."]},
    {"name": "Lieut. S. T. C. Wright", "canonical_name": "Wright, S. T. C.", "given_names": "S. T. C.", "surname": "Wright", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut."},
    {"name": "Lieut. E. I. Gore-Hickman", "canonical_name": "Gore-Hickman, E. I.", "given_names": "E. I.", "surname": "Gore-Hickman", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut."},
    {"name": "Lieut. J. St. J. Balguy", "canonical_name": "Balguy, J. St. J.", "given_names": "J. St. J.", "surname": "Balguy", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut."},
    {"name": "Lieut. J. H. Adams", "canonical_name": "Adams, J. H.", "given_names": "J. H.", "surname": "Adams", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut."},
    {"name": "Lieut. J. G. MacKellar", "canonical_name": "MacKellar, J. G.", "given_names": "J. G.", "surname": "MacKellar", "position": "Sappers (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut."},
    {"name": "Lieut. G. E. Prismall", "canonical_name": "Prismall, G. E.", "given_names": "G. E.", "surname": "Prismall", "position": "Battery Subalterns", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut."},
    {"name": "Lieut. O. G. Freeman", "canonical_name": "Freeman, O. G.", "given_names": "O. G.", "surname": "Freeman", "position": "Battery Subalterns", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut."},
    {"name": "Lieut. C. E. Wingrove", "canonical_name": "Wingrove, C. E.", "given_names": "C. E.", "surname": "Wingrove", "position": "Intelligence Officer", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut."},
    {"name": "Lieut. G. Murray", "canonical_name": "Murray, G.", "given_names": "G.", "surname": "Murray", "position": "O.C. Signal School", "department": "GOLD COAST REGIMENT, W.A.F.F.", "military_rank": "Lieut."},
    {"name": "T. A. Medhurst", "canonical_name": "Medhurst, T. A.", "given_names": "T. A.", "surname": "Medhurst", "position": "Bandmaster", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "W. J. Goodwright", "canonical_name": "Goodwright, W. J.", "given_names": "W. J.", "surname": "Goodwright", "position": "Battery Sergeant-Major", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "R. Moon", "canonical_name": "Moon, R.", "given_names": "R.", "surname": "Moon", "position": "Company Sergeant-Majors", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "J. O'Shea", "canonical_name": "O'Shea, J.", "given_names": "J.", "surname": "O'Shea", "position": "Company Sergeant-Majors", "department": "GOLD COAST REGIMENT, W.A.F.F.", "honors": ["D.C.M."]},
    {"name": "F. Soper", "canonical_name": "Soper, F.", "given_names": "F.", "surname": "Soper", "position": "Company Sergeant-Majors", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "T. Wray", "canonical_name": "Wray, T.", "given_names": "T.", "surname": "Wray", "position": "Company Sergeant-Majors", "department": "GOLD COAST REGIMENT, W.A.F.F.", "honors": ["D.C.M."]},
    {"name": "A. J. Avenell", "canonical_name": "Avenell, A. J.", "given_names": "A. J.", "surname": "Avenell", "position": "Armourer Staff-Sergeants", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "G. A. White", "canonical_name": "White, G. A.", "given_names": "G. A.", "surname": "White", "position": "Armourer Staff-Sergeants", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "L. E. Iggleton", "canonical_name": "Iggleton, L. E.", "given_names": "L. E.", "surname": "Iggleton", "position": "Battery Section Sergeant", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "A. Morgan", "canonical_name": "Morgan, A.", "given_names": "A.", "surname": "Morgan", "position": "Platoon Sergeants (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "W. J. Congdon", "canonical_name": "Congdon, W. J.", "given_names": "W. J.", "surname": "Congdon", "position": "Platoon Sergeants (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "J. V. McArdle", "canonical_name": "McArdle, J. V.", "given_names": "J. V.", "surname": "McArdle", "position": "Platoon Sergeants (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "L. Curtis", "canonical_name": "Curtis, L.", "given_names": "L.", "surname": "Curtis", "position": "Platoon Sergeants (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "R. E. Hunt", "canonical_name": "Hunt, R. E.", "given_names": "R. E.", "surname": "Hunt", "position": "Platoon Sergeants (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "G. Brown", "canonical_name": "Brown, G.", "given_names": "G.", "surname": "Brown", "position": "Platoon Sergeants (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "R. S. Gargraves", "canonical_name": "Gargraves, R. S.", "given_names": "R. S.", "surname": "Gargraves", "position": "Platoon Sergeants (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "J. P. Daly", "canonical_name": "Daly, J. P.", "given_names": "J. P.", "surname": "Daly", "position": "Platoon Sergeants (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "T. H. Collins", "canonical_name": "Collins, T. H.", "given_names": "T. H.", "surname": "Collins", "position": "Platoon Sergeants (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F."},
    {"name": "R. McDermott", "canonical_name": "McDermott, R.", "given_names": "R.", "surname": "McDermott", "position": "Platoon Sergeants (Infantry)", "department": "GOLD COAST REGIMENT, W.A.F.F."}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()