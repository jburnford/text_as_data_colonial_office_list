"""
Gambia Colonial Office List 1867 - Extracted Data (Merged from 2 sections)
"""
COLONY = "Gambia"
YEAR = 1867

OFFICIALS = [{'name': 'Admiral Patey', 'canonical_name': 'Patey, Admiral', 'surname': 'Patey', 'position': 'Administrator', 'department': 'Civil Establishment - Gambia', 'salary_min': 1300, 'salary_max': 1300, 'allowances': '200l. table money'}, {'name': 'H. G. M. Robertson', 'canonical_name': 'Robertson, H. G. M.', 'given_names': 'H. G. M.', 'surname': 'Robertson', 'position': '1st Writer', 'department': 'Civil Establishment - Gambia', 'salary_min': 300, 'salary_max': 300}, {'name': 'Thos. Johnson', 'canonical_name': 'Johnson, Thomas', 'given_names': 'Thomas', 'surname': 'Johnson', 'position': '2nd Writer', 'department': 'Civil Establishment - Gambia', 'salary_min': 104, 'salary_max': 104}, {'name': 'G. H. Kneller', 'canonical_name': 'Kneller, G. H.', 'given_names': 'G. H.', 'surname': 'Kneller', 'position': 'Collector of Customs', 'department': 'Civil Establishment - Gambia', 'salary_min': 475, 'salary_max': 475}, {'name': 'C. F. Stubbs', 'canonical_name': 'Stubbs, C. F.', 'given_names': 'C. F.', 'surname': 'Stubbs', 'position': 'Clerk', 'department': 'Civil Establishment - Gambia', 'salary_min': 200, 'salary_max': 200}, {'name': 'P. L. Hughes', 'canonical_name': 'Hughes, P. L.', 'given_names': 'P. L.', 'surname': 'Hughes', 'position': 'Tide-Surveyor and Superintendent of Quarantine', 'department': 'Civil Establishment - Gambia', 'salary_min': 190, 'salary_max': 190}, {'name': 'C. B. Primet', 'canonical_name': 'Primet, C. B.', 'given_names': 'C. B.', 'surname': 'Primet', 'position': 'Auditor', 'department': 'Civil Establishment - Gambia', 'salary_min': 200, 'salary_max': 200}, {'name': 'Rev. James Robbin', 'canonical_name': 'Robbin, James', 'given_names': 'James', 'surname': 'Robbin', 'position': 'Acting Colonial and Garrison Chaplain', 'department': 'Civil Establishment - Gambia', 'salary_min': 250, 'salary_max': 250, 'acting_status': 'Acting'}, {'name': 'J. Melton', 'canonical_name': 'Melton, J.', 'given_names': 'J.', 'surname': 'Melton', 'position': 'Postmaster', 'department': 'Civil Establishment - Gambia', 'salary_min': 80, 'salary_max': 80}, {'name': 'W. H. Sherwood', 'canonical_name': 'Sherwood, W. H.', 'given_names': 'W. H.', 'surname': 'Sherwood', 'position': 'High Sheriff', 'department': 'Judicial Establishment - Gambia'}, {'name': 'Seymour Gay', 'canonical_name': 'Gay, Seymour', 'given_names': 'Seymour', 'surname': 'Gay', 'position': 'Superintendent of Police', 'department': 'Judicial Establishment - Gambia', 'salary_min': 50, 'salary_max': 50}, {'name': 'J. Smith', 'canonical_name': 'Smith, J.', 'given_names': 'J.', 'surname': 'Smith', 'position': 'Resident Manager of Combo', 'department': 'Judicial Establishment - Gambia', 'salary_min': 80, 'salary_max': 80, 'qualifications': ['J.P.']}, {'name': 'Dr. Sherwood', 'canonical_name': 'Sherwood, Dr.', 'given_names': 'Dr.', 'surname': 'Sherwood', 'position': 'Police Magistrate', 'department': 'Judicial Establishment - Gambia', 'acting_status': 'Acting'}]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()
