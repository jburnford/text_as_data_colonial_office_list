"""
Sierra Leone Colonial Office List 1898 - Extracted Data
"""
COLONY = "Sierra Leone"
YEAR = 1898

OFFICIALS = [
    {"name": "The Colonial Surgeon", "canonical_name": "Colonial Surgeon, The", "surname": "Colonial Surgeon", "position": "Inspector of Health", "department": "Sanitary Department - Sierra Leone"},
    {"name": "T. M. Cole", "canonical_name": "Cole, T. M.", "given_names": "T. M.", "surname": "Cole", "position": "Clerk", "department": "Sanitary Department - Sierra Leone", "salary_min": 50, "salary_max": 50},
    {"name": "A. F. Tarbet", "canonical_name": "Tarbet, A. F.", "given_names": "A. F.", "surname": "Tarbet", "position": "Inspector-General of Frontier Police", "department": "Police Department - Sierra Leone", "salary_min": 400, "salary_max": 500, "allowances": "91l. 5s.", "military_rank": "Major"},
    {"name": "S. Moore", "canonical_name": "Moore, S.", "given_names": "S.", "surname": "Moore", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 350, "allowances": "91l. allowance"},
    {"name": "C. C. Troughton", "canonical_name": "Troughton, C. C.", "given_names": "C. C.", "surname": "Troughton", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 350, "allowances": "91l. allowance"},
    {"name": "B. Cave-Brown-Cave", "canonical_name": "Cave-Brown-Cave, B.", "given_names": "B.", "surname": "Cave-Brown-Cave", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 350, "allowances": "91l. allowance"},
    {"name": "J. E. C. Blakeney", "canonical_name": "Blakeney, J. E. C.", "given_names": "J. E. C.", "surname": "Blakeney", "position": "Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 350, "allowances": "91l. allowance"},
    {"name": "E. C. Mayne", "canonical_name": "Mayne, E. C.", "given_names": "E. C.", "surname": "Mayne", "position": "Assistant Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "91l. allowance", "military_rank": "Captain"},
    {"name": "C. E. Birch", "canonical_name": "Birch, C. E.", "given_names": "C. E.", "surname": "Birch", "position": "Assistant Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "91l. allowance", "military_rank": "Lieut."},
    {"name": "G. A. Gildes", "canonical_name": "Gildes, G. A.", "given_names": "G. A.", "surname": "Gildes", "position": "Assistant Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "91l. allowance"},
    {"name": "H. G. Warren", "canonical_name": "Warren, H. G.", "given_names": "H. G.", "surname": "Warren", "position": "Assistant Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "91l. allowance", "military_rank": "Captain"},
    {"name": "C. N. Hastings", "canonical_name": "Hastings, C. N.", "given_names": "C. N.", "surname": "Hastings", "position": "Assistant Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "91l. allowance", "military_rank": "Captain"},
    {"name": "J. E. Harden", "canonical_name": "Harden, J. E.", "given_names": "J. E.", "surname": "Harden", "position": "Assistant Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "91l. allowance", "military_rank": "Captain"},
    {"name": "E. B. Wallis", "canonical_name": "Wallis, E. B.", "given_names": "E. B.", "surname": "Wallis", "position": "Assistant Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 300, "allowances": "91l. allowance", "military_rank": "Captain"},
    {"name": "C. N. Taylor", "canonical_name": "Taylor, C. N.", "given_names": "C. N.", "surname": "Taylor", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "J. B. Johnson", "canonical_name": "Johnson, J. B.", "given_names": "J. B.", "surname": "Johnson", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "J. H. Jones", "canonical_name": "Jones, J. H.", "given_names": "J. H.", "surname": "Jones", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "D. P. H. Crowther", "canonical_name": "Crowther, D. P. H.", "given_names": "D. P. H.", "surname": "Crowther", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "A. B. Davies", "canonical_name": "Davies, A. B.", "given_names": "A. B.", "surname": "Davies", "position": "Sub-Inspectors", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
    {"name": "Z. E. T. Williams", "canonical_name": "Williams, Z. E. T.", "given_names": "Z. E. T.", "surname": "Williams", "position": "Paymaster Clerk, Frontier Police", "department": "Police Department - Sierra Leone", "salary_min": 75, "salary_max": 100},
    {"name": "G. L. Brooks", "canonical_name": "Brooks, G. L.", "given_names": "G. L.", "surname": "Brooks", "position": "Superintendent, Civil Police", "department": "Police Department - Sierra Leone", "salary_min": 300, "salary_max": 300, "allowances": "91l.", "duty_allowance": 40},
    {"name": "J. M. Robin", "canonical_name": "Robin, J. M.", "given_names": "J. M.", "surname": "Robin", "position": "Inspector", "department": "Police Department - Sierra Leone", "salary_min": 250, "salary_max": 250, "allowances": "91l.", "duty_allowance": 40},
    {"name": "N. H. Sawyer", "canonical_name": "Sawyer, N. H.", "given_names": "N. H.", "surname": "Sawyer", "position": "Sub-Inspector", "department": "Police Department - Sierra Leone", "salary_min": 100, "salary_max": 150},
]

def get_extraction():
    return {"colony": COLONY, "year": YEAR, "total_officials": len(OFFICIALS), "officials": OFFICIALS}

def main():
    import json
    print(json.dumps(get_extraction(), indent=2))

if __name__ == "__main__":
    main()