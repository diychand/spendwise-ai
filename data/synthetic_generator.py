import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Categories and sample merchant-like descriptions for each
CATEGORY_MERCHANTS = {
    "Food": ["SWIGGY", "ZOMATO", "DOMINOS", "MCDONALDS", "STARBUCKS"],
    "Travel": ["UBER", "OLA", "IRCTC", "INDIGO AIRLINES", "REDBUS"],
    "Shopping": ["AMAZON", "FLIPKART", "MYNTRA", "AJIO", "RELIANCE TRENDS"],
    "Bills": ["ELECTRICITY BOARD", "AIRTEL POSTPAID", "JIO FIBER", "WATER DEPT"],
    "Entertainment": ["NETFLIX", "SPOTIFY", "BOOKMYSHOW", "PVR CINEMAS"],
    "Groceries": ["BIGBASKET", "DMART", "BLINKIT", "ZEPTO"],
    "Salary": ["SALARY CREDIT - COMPANY XYZ"],
    "Rent": ["RENT PAYMENT - LANDLORD"],
}
# These merchants are NOT in the rules dictionary on purpose -
# they force transactions to fall through to ML/LLM categorization
UNKNOWN_MERCHANTS = {
    "Food": ["FAASOS", "BEHROUZ BIRYANI", "THEOBROMA"],
    "Travel": ["RAPIDO", "METRO CARD RECHARGE"],
    "Shopping": ["NYKAA", "MEESHO", "TATA CLIQ"],
    "Groceries": ["NATURE'S BASKET", "SPENCER'S"],
    "Entertainment": ["SONY LIV", "HOTSTAR"],
}

def random_date(start_days_ago=180):
    days_ago = random.randint(0, start_days_ago)
    return (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")

def generate_transaction():
    category = random.choices(
        list(CATEGORY_MERCHANTS.keys()),
        weights=[15, 10, 12, 10, 8, 15, 3, 1],
        k=1
    )[0]

    # 25% chance of using an "unknown" merchant the rules won't catch
    if category in UNKNOWN_MERCHANTS and random.random() < 0.25:
        merchant = random.choice(UNKNOWN_MERCHANTS[category])
    else:
        merchant = random.choice(CATEGORY_MERCHANTS[category])

    if category == "Salary":
        amount = round(random.uniform(30000, 80000), 2)
        txn_type = "CREDIT"
    elif category == "Rent":
        amount = round(random.uniform(8000, 25000), 2)
        txn_type = "DEBIT"
    else:
        amount = round(random.uniform(100, 5000), 2)
        txn_type = "DEBIT"

    description = f"{merchant} REF{random.randint(100000,999999)}"

    return {
        "date": random_date(),
        "description": description,
        "amount": amount,
        "type": txn_type,
    }

def generate_dataset(num_transactions=500, output_file="synthetic_transactions.csv"):
    transactions = [generate_transaction() for _ in range(num_transactions)]
    transactions.sort(key=lambda x: x["date"])

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "description", "amount", "type"])
        writer.writeheader()
        writer.writerows(transactions)

    print(f"Generated {num_transactions} transactions -> {output_file}")

if __name__ == "__main__":
    generate_dataset()