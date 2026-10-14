import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

CATEGORY_MERCHANTS = {
    "Food": ["SWIGGY", "ZOMATO", "DOMINOS", "MCDONALDS", "STARBUCKS"],
    "Travel": ["UBER", "OLA", "IRCTC", "INDIGO AIRLINES", "REDBUS"],
    "Shopping": ["AMAZON", "FLIPKART", "MYNTRA", "AJIO", "RELIANCE TRENDS"],
    "Bills": ["ELECTRICITY BOARD", "AIRTEL POSTPAID", "JIO FIBER", "WATER DEPT"],
    "Entertainment": ["NETFLIX", "SPOTIFY", "BOOKMYSHOW", "PVR CINEMAS"],
    "Groceries": ["BIGBASKET", "DMART", "BLINKIT", "ZEPTO"],
}

UNKNOWN_MERCHANTS = {
    "Food": ["FAASOS", "BEHROUZ BIRYANI", "THEOBROMA"],
    "Travel": ["RAPIDO", "METRO CARD RECHARGE"],
    "Shopping": ["NYKAA", "MEESHO", "TATA CLIQ"],
    "Groceries": ["NATURE'S BASKET", "SPENCER'S"],
    "Entertainment": ["SONY LIV", "HOTSTAR"],
}

# Realistic monthly budget as a PERCENTAGE of that month's income,
# for a low-to-middle-income Indian household.
# These percentages are randomized slightly per month for realism.
BUDGET_PERCENTAGES = {
    "Rent": (0.20, 0.25),
    "Groceries": (0.12, 0.15),
    "Food": (0.07, 0.10),
    "Bills": (0.08, 0.10),
    "Travel": (0.05, 0.07),
    "Shopping": (0.05, 0.08),
    "Entertainment": (0.02, 0.04),
}

NUM_MONTHS = 6
MONTHLY_INCOME_BASE = 28000  # base salary, varies slightly month to month


def get_month_start_dates(num_months):
    """Returns the 1st of each of the last `num_months` months, oldest first."""
    today = datetime.now()
    dates = []
    year, month = today.year, today.month
    for _ in range(num_months):
        dates.append(datetime(year, month, 1))
        month -= 1
        if month == 0:
            month = 12
            year -= 1
    return list(reversed(dates))


def random_date_in_month(month_start):
    """A random date within the given month."""
    if month_start.month == 12:
        next_month = datetime(month_start.year + 1, 1, 1)
    else:
        next_month = datetime(month_start.year, month_start.month + 1, 1)
    days_in_month = (next_month - month_start).days
    offset = random.randint(0, days_in_month - 1)
    return (month_start + timedelta(days=offset)).strftime("%Y-%m-%d")


def split_amount_into_transactions(total, min_txns=1, max_txns=4):
    """Splits a total budget amount into a few random-sized transactions."""
    num_txns = random.randint(min_txns, max_txns)
    if num_txns == 1:
        return [round(total, 2)]

    cuts = sorted(random.uniform(0.1, 0.9) for _ in range(num_txns - 1))
    proportions = [cuts[0]] + [cuts[i] - cuts[i - 1] for i in range(1, len(cuts))] + [1 - cuts[-1]]
    return [round(total * p, 2) for p in proportions]


def generate_dataset(output_file="synthetic_transactions.csv"):
    transactions = []
    month_starts = get_month_start_dates(NUM_MONTHS)

    for month_start in month_starts:
        # 1. Monthly salary - always exactly one per month, small variation
        income = round(MONTHLY_INCOME_BASE + random.uniform(-2000, 3000), 2)
        salary_date = month_start + timedelta(days=random.randint(0, 2))  # paid near start of month
        transactions.append({
            "date": salary_date.strftime("%Y-%m-%d"),
            "description": f"SALARY CREDIT - COMPANY XYZ REF{random.randint(100000,999999)}",
            "amount": income,
            "type": "CREDIT",
        })

        # 2. Rent - one transaction per month
        rent_pct = random.uniform(*BUDGET_PERCENTAGES["Rent"])
        rent_amount = round(income * rent_pct, 2)
        rent_date = month_start + timedelta(days=random.randint(0, 4))
        transactions.append({
            "date": rent_date.strftime("%Y-%m-%d"),
            "description": f"RENT PAYMENT - LANDLORD REF{random.randint(100000,999999)}",
            "amount": rent_amount,
            "type": "DEBIT",
        })

        # 3. Other categories - split into a few transactions each, spread through the month
        for category in ["Groceries", "Food", "Bills", "Travel", "Shopping", "Entertainment"]:
            pct_range = BUDGET_PERCENTAGES[category]
            category_budget = income * random.uniform(*pct_range)
            amounts = split_amount_into_transactions(category_budget)

            for amt in amounts:
                if amt <= 0:
                    continue
                # Occasionally use an "unknown" merchant to test ML/LLM fallback
                if category in UNKNOWN_MERCHANTS and random.random() < 0.2:
                    merchant = random.choice(UNKNOWN_MERCHANTS[category])
                else:
                    merchant = random.choice(CATEGORY_MERCHANTS[category])

                transactions.append({
                    "date": random_date_in_month(month_start),
                    "description": f"{merchant} REF{random.randint(100000,999999)}",
                    "amount": amt,
                    "type": "DEBIT",
                })

        # 4. Occasionally add one unusually large expense (a genuine anomaly) - not every month
        if random.random() < 0.3:
            spike_category = random.choice(["Shopping", "Food", "Entertainment"])
            spike_amount = round(income * random.uniform(0.15, 0.25), 2)  # a big one-off expense
            merchant = random.choice(CATEGORY_MERCHANTS[spike_category])
            transactions.append({
                "date": random_date_in_month(month_start),
                "description": f"{merchant} REF{random.randint(100000,999999)}",
                "amount": spike_amount,
                "type": "DEBIT",
            })

    transactions.sort(key=lambda x: x["date"])

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "description", "amount", "type"])
        writer.writeheader()
        writer.writerows(transactions)

    print(f"Generated {len(transactions)} transactions across {NUM_MONTHS} months -> {output_file}")


if __name__ == "__main__":
    generate_dataset()