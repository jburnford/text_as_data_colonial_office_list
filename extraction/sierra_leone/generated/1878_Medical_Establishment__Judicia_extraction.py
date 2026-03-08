"""
Sierra Leone Colonial Office List 1878 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1878

OFFICIALS = [
    {"name": "F. H. Lovell", "canonical_name": "Lovell, F. H.", "given_names": "F. H.", "surname": "Lovell", "position": "Colonial Surgeon", "department": "Medical - Sierra Leone", "salary_min": 500, "salary_max": 500, "allowances": "horse allowance, 91l. 5s."},
    {"name": "Robt. Smith", "canonical_name": "Smith, Robt.", "given_names": "Robt.", "surname": "Smith", "position": "Assistant Colonial Surgeon", "department": "Medical - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "horse allowance, 91l. 5s."},
    {"name": "D. Johnson", "canonical_name": "Johnson, D.", "given_names": "D.", "surname": "Johnson", "position": "Compounder and Storekeeper", "department": "Medical - Sierra Leone", "salary_min": 150, "salary_max": 150, "allowances": "quarters"},
    {"name": "D. Cole", "canonical_name": "Cole, D.", "given_names": "D.", "surname": "Cole", "position": "Medical Clerk", "department": "Medical - Sierra Leone", "salary_min": 75, "salary_max": 75, "allowances": "quarters"},
    {"name": "J. H. F. Roberts", "canonical_name": "Roberts, J. H. F.", "given_names": "J. H. F.", "surname": "Roberts", "position": "Inspector of Health", "department": "Sanitary - Sierra Leone", "salary_min": 350, "salary_max": 350},
    {"name": "W. C. During", "canonical_name": "During, W. C.", "given_names": "W. C.", "surname": "During", "position": "Clerk to Inspector of Health", "department": "Sanitary - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "H. J. Huggins", "canonical_name": "Huggins, H. J.", "given_names": "H. J.", "surname": "Huggins", "position": "Chief Justice and Judge of the Vice-Admiralty Court", "department": "Judicial - Sierra Leone", "salary_min": 1500, "salary_max": 1500},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk to Chief Justice", "department": "Judicial - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "W. W. Streeten", "canonical_name": "Streeten, W. W.", "given_names": "W. W.", "surname": "Streeten", "position": "Queen's Advocate", "department": "Judicial - Sierra Leone", "salary_min": 1000, "salary_max": 1000},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Clerk to Queen's Advocate", "department": "Judicial - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Assistant Clerk to Queen's Advocate", "department": "Judicial - Sierra Leone", "salary_min": 30, "salary_max": 30},
    {"name": "T. Marston", "canonical_name": "Marston, T.", "given_names": "T.", "surname": "Marston", "position": "Master and Registrar of the Supreme Court", "department": "Judicial - Sierra Leone", "salary_min": 500, "salary_max": 500},
    {"name": "A. B. Martyn", "canonical_name": "Martyn, A. B.", "given_names": "A. B.", "surname": "Martyn", "position": "Clerk to Master and Registrar", "department": "Judicial - Sierra Leone", "salary_min": 160, "salary_max": 160},
    {"name": "John Meheux", "canonical_name": "Meheux, John", "given_names": "John", "surname": "Meheux", "position": "Sheriff and Provost-Marshal", "department": "Judicial - Sierra Leone", "salary_min": 400, "salary_max": 400},
    {"name": "A. Montagu", "canonical_name": "Montagu, A.", "given_names": "A.", "surname": "Montagu", "position": "Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 300, "salary_max": 300},
    {"name": "J. M. Thomas", "canonical_name": "Thomas, J. M.", "given_names": "J. M.", "surname": "Thomas", "position": "Clerk to Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "J. H. Lacton", "canonical_name": "Lacton, J. H.", "given_names": "J. H.", "surname": "Lacton", "position": "Clerk to Registrar-General", "department": "Judicial - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "D. Carroll", "canonical_name": "Carroll, D.", "given_names": "D.", "surname": "Carroll", "position": "Registrar of Court of Summary Jurisdiction", "department": "Judicial - Sierra Leone", "salary_min": 150, "salary_max": 150},
    {"name": "J. Cole", "canonical_name": "Cole, J.", "given_names": "J.", "surname": "Cole", "position": "Clerk to Registrar", "department": "Judicial - Sierra Leone", "salary_min": 60, "salary_max": 60},
    {"name": "J. Ashwood", "canonical_name": "Ashwood, J.", "given_names": "J.", "surname": "Ashwood", "position": "Coroner for Freetown", "department": "Judicial - Sierra Leone", "salary_min": 100, "salary_max": 100},
    {"name": "T. Marston", "canonical_name": "Marston, T.", "given_names": "T.", "surname": "Marston", "position": "Registrar of Vice-Admiralty Court", "department": "Judicial - Sierra Leone"},
    {"name": "John Meheux", "canonical_name": "Meheux, John", "given_names": "John", "surname": "Meheux", "position": "Marshal of Vice-Admiralty Court", "department": "Judicial - Sierra Leone"},
    {"name": "Major M. Doorly", "canonical_name": "Doorly, M.", "given_names": "M.", "surname": "Doorly", "position": "Police Magistrate", "department": "Police and Gaols - Sierra Leone", "salary_min": 500, "salary_max": 500, "military_rank": "Major"},
    {"name": "J. M. Davis", "canonical_name": "Davis, J. M.", "given_names": "J. M.", "surname": "Davis", "position": "Clerk of Police", "department": "Police and Gaols - Sierra Leone", "acting_status": "acting", "salary_min": 200, "salary_max": 200},
    {"name": "J. C. Loggie", "canonical_name": "Loggie, J. C.", "given_names": "J. C.", "surname": "Loggie", "position": "Inspector-General of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 400, "salary_max": 400, "allowances": "travelling allowance, 91l. 5s.", "honors": ["C.M.G."]},
    {"name": "Geo. Neville", "canonical_name": "Neville, Geo.", "given_names": "Geo.", "surname": "Neville", "position": "Inspector of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 80, "salary_max": 80},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sub-Inspector of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "VACANT", "canonical_name": "VACANT", "surname": "VACANT", "position": "Sub-Inspector of Police", "department": "Police and Gaols - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "W. E. Inniss", "canonical_name": "Inniss, W. E.", "given_names": "W. E.", "surname": "Inniss", "position": "Keeper of Freetown Gaol", "department": "Police and Gaols - Sierra Leone", "salary_min": 200, "salary_max": 250, "allowances": "quarters"},
    {"name": "John Thompson", "canonical_name": "Thompson, John", "given_names": "John", "surname": "Thompson", "position": "Assistant Keeper of Freetown Gaol", "department": "Police and Gaols - Sierra Leone", "salary_min": 100, "salary_max": 100, "allowances": "quarters"},
    {"name": "The Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Manager, 1st Eastern District", "department": "Manager of Districts - Sierra Leone", "salary_min": 45, "salary_max": 45, "allowances": "12s. 6d., travelling allowance"},
    {"name": "The Police Magistrate", "canonical_name": "Police Magistrate, The", "surname": "Police Magistrate", "position": "Manager, Mountain District", "department": "Manager of Districts - Sierra Leone"},
    {"name": "Wm. Budge", "canonical_name": "Budge, Wm.", "given_names": "Wm.", "surname": "Budge", "position": "Manager and Coroner, 2nd Eastern District", "department": "Manager of Districts - Sierra Leone", "salary_min": 320, "salary_max": 320, "allowances": "travelling allowance, 91l. 5s. 0d., and a house"},
    {"name": "J. B. Elliott", "canonical_name": "Elliott, J. B.", "given_names": "J. B.", "surname": "Elliott", "position": "Manager and Coroner, Western District", "department": "Manager of Districts - Sierra Leone", "salary_min": 270, "salary_max": 270, "allowances": "40l. rent"}
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()