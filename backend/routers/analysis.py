from typing import Optional, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models import Transaction
from analysis.trends import get_monthly_category_spending, get_month_over_month_change, get_affordability_analysis

router = APIRouter(prefix="/analysis", tags=["analysis"])


@router.get("/monthly-category")
def monthly_category_spending(db: Session = Depends(get_db)):
    return get_monthly_category_spending(db)


@router.get("/monthly-trend")
def monthly_trend(db: Session = Depends(get_db)):
    return get_month_over_month_change(db)


@router.get("/affordability")
def affordability(purchase_amount: float, db: Session = Depends(get_db)):
    return get_affordability_analysis(db, purchase_amount)


@router.get("/months")
def get_available_months(db: Session = Depends(get_db)):
    """
    Returns a sorted list of distinct months (YYYY-MM) present in transactions, newest first.
    """
    rows = (
        db.query(func.substr(Transaction.date, 1, 7))
        .filter(Transaction.date != None)
        .distinct()
        .order_by(func.substr(Transaction.date, 1, 7).desc())
        .all()
    )
    return [r[0] for r in rows if r[0]]


@router.get("/monthly-breakdown")
def monthly_breakdown(
    month: str,
    category: Optional[str] = None,
    type: Optional[str] = "DEBIT",
    db: Session = Depends(get_db)
):
    """
    Returns transactions for a given month (YYYY-MM), grouped by category.
    Each group contains:
      - category: str
      - subtotal: float
      - transaction_count: int
      - transactions: list of dicts with id, date, description, amount, category, category_source, type

    If category is provided, returns only the group for that category.
    If type is provided (defaults to 'DEBIT'), filters by transaction type ('DEBIT', 'CREDIT', or None/'ALL' for all).
    """
    query = db.query(Transaction).filter(func.substr(Transaction.date, 1, 7) == month)

    if type and type.upper() != "ALL":
        query = query.filter(Transaction.type == type.upper())

    if category:
        query = query.filter(Transaction.category == category)

    transactions = query.order_by(Transaction.date.desc(), Transaction.id.desc()).all()

    grouped = {}
    for txn in transactions:
        cat = txn.category or "Uncategorized"
        if cat not in grouped:
            grouped[cat] = {
                "category": cat,
                "subtotal": 0.0,
                "transaction_count": 0,
                "transactions": [],
            }
        grouped[cat]["transactions"].append({
            "id": txn.id,
            "date": txn.date,
            "description": txn.description,
            "amount": round(txn.amount, 2),
            "category": txn.category,
            "category_source": txn.category_source,
            "type": txn.type,
        })
        grouped[cat]["subtotal"] = round(grouped[cat]["subtotal"] + txn.amount, 2)
        grouped[cat]["transaction_count"] += 1

    # If a specific category was queried but now has no transactions (e.g. after moving the last one),
    # return an empty group structure so the caller knows it is now empty.
    if category and category not in grouped:
        return [{
            "category": category,
            "subtotal": 0.0,
            "transaction_count": 0,
            "transactions": [],
        }]

    # Sort categories by subtotal descending
    result = sorted(grouped.values(), key=lambda x: x["subtotal"], reverse=True)
    return result


@router.get("/category-summary")
def category_summary(month: str, db: Session = Depends(get_db)):
    """
    Total expense per category for a given month (format: YYYY-MM).
    """
    rows = (
        db.query(Transaction.category, func.sum(Transaction.amount).label("total"))
        .filter(Transaction.type == "DEBIT")
        .filter(func.substr(Transaction.date, 1, 7) == month)
        .group_by(Transaction.category)
        .order_by(func.sum(Transaction.amount).desc())
        .all()
    )

    categories = [{"category": r[0], "total": round(r[1], 2)} for r in rows]
    total_spent = round(sum(c["total"] for c in categories), 2)

    return {"month": month, "categories": categories, "total_spent": total_spent}