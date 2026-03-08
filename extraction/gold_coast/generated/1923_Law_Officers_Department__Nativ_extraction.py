"""
Gold Coast Colonial Office List 1923 - Extracted Data
"""
COLONY = "Gold Coast"
YEAR = 1923

OFFICIALS = [
    {"name": "R. W. H. Wilkinson", "canonical_name": "Wilkinson, R. W. H.", "given_names": "R. W. H.", "surname": "Wilkinson",
     "position": "Attorney-General", "department": "Law Officers' Department - Gold Coast", "salary_min": 1500, "salary_max": 1500, "duty_allowance": 300},
    {"name": "C. Carnegie Brown", "canonical_name": "Brown, C. Carnegie", "given_names": "C. Carnegie", "surname": "Brown",
     "position": "Solicitor-General", "department": "Law Officers' Department - Gold Coast", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "J. J. Treacy", "canonical_name": "Treacy, J. J.", "given_names": "J. J.", "surname": "Treacy",
     "position": "European Crown Counsel", "department": "Law Officers' Department - Gold Coast", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "J. Aitken", "canonical_name": "Aitken, J.", "given_names": "J.", "surname": "Aitken",
     "position": "European Crown Counsel", "department": "Law Officers' Department - Gold Coast", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "L. E. V. McCarthy", "canonical_name": "McCarthy, L. E. V.", "given_names": "L. E. V.", "surname": "McCarthy",
     "position": "African Crown Counsel", "department": "Law Officers' Department - Gold Coast", "salary_min": 720, "salary_max": 960, "allowances": "72l. seniority allowance"},
    {"name": "Odartey Golightly", "canonical_name": "Golightly, Odartey", "given_names": "Odartey", "surname": "Golightly",
     "position": "Chief Clerk", "department": "Law Officers' Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "J. Maxwell", "canonical_name": "Maxwell, J.", "given_names": "J.", "surname": "Maxwell",
     "position": "Secretary for Native Affairs", "department": "Native Affairs Department - Gold Coast", "salary_min": 1350, "salary_max": 1350, "duty_allowance": 270},
    {"name": "C. W. Welman", "canonical_name": "Welman, C. W.", "given_names": "C. W.", "surname": "Welman",
     "position": "Deputy Secretary for Native Affairs", "department": "Native Affairs Department - Gold Coast", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "J. C. de Graaff Johnson", "canonical_name": "Johnson, J. C. de Graaff", "given_names": "J. C. de Graaff", "surname": "Johnson",
     "position": "Assistant Secretary for Native Affairs", "department": "Native Affairs Department - Gold Coast", "salary_min": 375, "salary_max": 780},
    {"name": "Chas. Fairweather", "canonical_name": "Fairweather, Charles", "given_names": "Charles", "surname": "Fairweather",
     "position": "Government Printer", "department": "Printing Office - Gold Coast", "salary_min": 600, "salary_max": 800, "allowances": "72l. seniority allowance"},
    {"name": "C. E. Heath", "canonical_name": "Heath, C. E.", "given_names": "C. E.", "surname": "Heath",
     "position": "Assistant Government Printers", "department": "Printing Office - Gold Coast", "salary_min": 450, "salary_max": 600},
    {"name": "W. H. Crocker", "canonical_name": "Crocker, W. H.", "given_names": "W. H.", "surname": "Crocker",
     "position": "Assistant Government Printers", "department": "Printing Office - Gold Coast", "salary_min": 450, "salary_max": 600},
    {"name": "R. H. Payne", "canonical_name": "Payne, R. H.", "given_names": "R. H.", "surname": "Payne",
     "position": "Assistant Government Printers", "department": "Printing Office - Gold Coast", "salary_min": 450, "salary_max": 600},
    {"name": "M. G. Okai", "canonical_name": "Okai, M. G.", "given_names": "M. G.", "surname": "Okai",
     "position": "Superintendent, Composing Room", "department": "Printing Office - Gold Coast", "salary_min": 264, "salary_max": 360},
    {"name": "T. R. N. Asante", "canonical_name": "Asante, T. R. N.", "given_names": "T. R. N.", "surname": "Asante",
     "position": "Superintendent, Machine Room", "department": "Printing Office - Gold Coast", "salary_min": 264, "salary_max": 360},
    {"name": "H. M. Lewis", "canonical_name": "Lewis, H. M.", "given_names": "H. M.", "surname": "Lewis",
     "position": "Treasurer", "department": "Treasury Department - Gold Coast", "salary_min": 1350, "salary_max": 1350, "duty_allowance": 270},
    {"name": "R. E. Burns", "canonical_name": "Burns, R. E.", "given_names": "R. E.", "surname": "Burns",
     "position": "Deputy Treasurer", "department": "Treasury Department - Gold Coast", "salary_min": 1050, "salary_max": 1050, "duty_allowance": 210},
    {"name": "D. B. Hinson", "canonical_name": "Hinson, D. B.", "given_names": "D. B.", "surname": "Hinson",
     "position": "Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "H. Vane Percy", "canonical_name": "Percy, H. Vane", "given_names": "H. Vane", "surname": "Percy",
     "position": "Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "G. A. D. Davies", "canonical_name": "Davies, G. A. D.", "given_names": "G. A. D.", "surname": "Davies",
     "position": "Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "C. J. Hodgens", "canonical_name": "Hodgens, C. J.", "given_names": "C. J.", "surname": "Hodgens",
     "position": "Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "military_rank": "M.C.", "allowances": "72l. seniority allowance from 720l."},
    {"name": "Capt. J. H. Stephens", "canonical_name": "Stephens, J. H.", "given_names": "J. H.", "surname": "Stephens",
     "position": "Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "military_rank": "M.C.", "allowances": "72l. seniority allowance from 720l."},
    {"name": "F. A. C. Jones", "canonical_name": "Jones, F. A. C.", "given_names": "F. A. C.", "surname": "Jones",
     "position": "Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "Alex Konuah", "canonical_name": "Konuah, Alex", "given_names": "Alex", "surname": "Konuah",
     "position": "African Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 375, "salary_max": 780},
    {"name": "P. H. Schandorf", "canonical_name": "Schandorf, P. H.", "given_names": "P. H.", "surname": "Schandorf",
     "position": "African Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 375, "salary_max": 780},
    {"name": "J. F. Thompson", "canonical_name": "Thompson, J. F.", "given_names": "J. F.", "surname": "Thompson",
     "position": "Sub-Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "C. R. Hammond", "canonical_name": "Hammond, C. R.", "given_names": "C. R.", "surname": "Hammond",
     "position": "Sub-Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "Stephen Coleman", "canonical_name": "Coleman, Stephen", "given_names": "Stephen", "surname": "Coleman",
     "position": "Sub-Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "F. L. J. Cato", "canonical_name": "Cato, F. L. J.", "given_names": "F. L. J.", "surname": "Cato",
     "position": "Sub-Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "Sam Baidoo", "canonical_name": "Baidoo, Sam", "given_names": "Sam", "surname": "Baidoo",
     "position": "Sub-Assistants", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "A. I. Anteson", "canonical_name": "Anteson, A. I.", "given_names": "A. I.", "surname": "Anteson",
     "position": "Chief Clerk", "department": "Treasury Department - Gold Coast", "salary_min": 300, "salary_max": 396},
    {"name": "W. Bowerley", "canonical_name": "Bowerley, W.", "given_names": "W.", "surname": "Bowerley",
     "position": "Auditor", "department": "Audit Department - Gold Coast", "salary_min": 1100, "salary_max": 1100, "duty_allowance": 220},
    {"name": "L. G. Corney", "canonical_name": "Corney, L. G.", "given_names": "L. G.", "surname": "Corney",
     "position": "Deputy Auditor", "department": "Audit Department - Gold Coast", "salary_min": 960, "salary_max": 960, "duty_allowance": 96},
    {"name": "W. L. Mackinnon", "canonical_name": "Mackinnon, W. L.", "given_names": "W. L.", "surname": "Mackinnon",
     "position": "Assistant Auditors", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "Capt. C. Griffith", "canonical_name": "Griffith, C.", "given_names": "C.", "surname": "Griffith",
     "position": "Assistant Auditors", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "military_rank": "Captain", "allowances": "72l. seniority allowance from 720l."},
    {"name": "Capt. W. H. Lemriere", "canonical_name": "Lemriere, W. H.", "given_names": "W. H.", "surname": "Lemriere",
     "position": "Assistant Auditors", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "military_rank": "Captain", "allowances": "72l. seniority allowance from 720l."},
    {"name": "N. C. Fonnerau", "canonical_name": "Fonnerau, N. C.", "given_names": "N. C.", "surname": "Fonnerau",
     "position": "Assistant Auditors", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "A. C. Hands", "canonical_name": "Hands, A. C.", "given_names": "A. C.", "surname": "Hands",
     "position": "Assistant Auditors", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "E. H. C. Lillicrup", "canonical_name": "Lillicrup, E. H. C.", "given_names": "E. H. C.", "surname": "Lillicrup",
     "position": "Assistant Auditors", "department": "Audit Department - Gold Coast", "salary_min": 450, "salary_max": 920, "allowances": "72l. seniority allowance from 720l."},
    {"name": "V. C. Randolph", "canonical_name": "Randolph, V. C.", "given_names": "V. C.", "surname": "Randolph",
     "position": "Chief Audit Clerk", "department": "Audit Department - Gold Coast", "salary_min": 300, "salary_max": 396}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()