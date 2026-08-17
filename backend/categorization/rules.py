# Keyword -> Category mapping.
# We check if any keyword appears in the transaction description (case-insensitive).
RULES = {
    "Food": ["SWIGGY", "ZOMATO", "DOMINOS", "MCDONALDS", "STARBUCKS"],
    "Travel": ["UBER", "OLA", "IRCTC", "INDIGO", "REDBUS"],
    "Shopping": ["AMAZON", "FLIPKART", "MYNTRA", "AJIO", "RELIANCE TRENDS"],
    "Bills": ["ELECTRICITY", "AIRTEL", "JIO FIBER", "WATER DEPT"],
    "Entertainment": ["NETFLIX", "SPOTIFY", "BOOKMYSHOW", "PVR"],
    "Groceries": ["BIGBASKET", "DMART", "BLINKIT", "ZEPTO"],
    "Salary": ["SALARY CREDIT"],
    "Rent": ["RENT PAYMENT"],
}

def categorize_by_rule(description: str):
    """
    Checks the transaction description against known keywords.
    Returns the category name if a match is found, otherwise None.
    """
    description_upper = description.upper()
    for category, keywords in RULES.items():
        for keyword in keywords:
            if keyword in description_upper:
                return category
    return None  # no rule matched