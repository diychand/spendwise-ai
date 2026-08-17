import pandas as pd
from sqlalchemy.orm import Session
from models import Transaction


def get_monthly_category_spending(db: Session):
    """
    Returns spending grouped by month and category, for DEBIT transactions only.
    """
    transactions = db.query(Transaction).filter(Transaction.type == "DEBIT").all()

    if not transactions:
        return []

    # Convert to a pandas DataFrame - much easier to group/aggregate than raw loops
    data = [{
        "date": t.date,
        "category": t.category,
        "amount": t.amount
    } for t in transactions]

    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)  # e.g. "2026-02"

    grouped = df.groupby(["month", "category"])["amount"].sum().reset_index()

    return grouped.to_dict(orient="records")


def get_month_over_month_change(db: Session):
    """
    Returns total spending per month, plus the percentage change from the previous month.
    """
    transactions = db.query(Transaction).filter(Transaction.type == "DEBIT").all()

    if not transactions:
        return []

    data = [{"date": t.date, "amount": t.amount} for t in transactions]
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)

    monthly_totals = df.groupby("month")["amount"].sum().reset_index()
    monthly_totals = monthly_totals.sort_values("month")

    monthly_totals["pct_change"] = monthly_totals["amount"].pct_change() * 100
    monthly_totals["pct_change"] = monthly_totals["pct_change"].round(2)

    result = monthly_totals.to_dict(orient="records")

    # Manually replace any NaN in pct_change with None (valid JSON null)
    for row in result:
        if pd.isna(row["pct_change"]):
            row["pct_change"] = None

    return result

def get_affordability_analysis(db: Session, purchase_amount: float):
    """
    Estimates whether a purchase is affordable based on average monthly surplus.
    """
    from models import Transaction

    transactions = db.query(Transaction).all()

    if not transactions:
        return {"error": "No transaction data available"}

    data = [{
        "date": t.date,
        "amount": t.amount,
        "type": t.type
    } for t in transactions]

    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)

    # Income = CREDIT transactions, Expenses = DEBIT transactions, grouped by month
    monthly_income = df[df["type"] == "CREDIT"].groupby("month")["amount"].sum()
    monthly_expenses = df[df["type"] == "DEBIT"].groupby("month")["amount"].sum()

    # Align months that appear in both (some months might only have one or the other)
    all_months = sorted(set(monthly_income.index) | set(monthly_expenses.index))
    monthly_income = monthly_income.reindex(all_months, fill_value=0)
    monthly_expenses = monthly_expenses.reindex(all_months, fill_value=0)

    monthly_surplus = monthly_income - monthly_expenses
    avg_monthly_surplus = monthly_surplus.mean()

    if avg_monthly_surplus <= 0:
        return {
            "purchase_amount": purchase_amount,
            "avg_monthly_surplus": round(avg_monthly_surplus, 2),
            "verdict": "Not recommended",
            "explanation": "Your average monthly spending exceeds your income, so this purchase would strain your finances further."
        }

    months_needed = purchase_amount / avg_monthly_surplus

    if months_needed <= 1:
        verdict = "Easily affordable"
        explanation = "You could cover this purchase within your current month's surplus."
    elif months_needed <= 3:
        verdict = "Affordable with planning"
        explanation = f"Saving your average monthly surplus, you could afford this in about {months_needed:.1f} months."
    else:
        verdict = "Consider waiting"
        explanation = f"At your current savings rate, this would take about {months_needed:.1f} months to afford comfortably."

    return {
        "purchase_amount": purchase_amount,
        "avg_monthly_surplus": round(avg_monthly_surplus, 2),
        "months_needed": round(months_needed, 1),
        "verdict": verdict,
        "explanation": explanation,
    }