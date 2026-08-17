from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Transaction
from categorization.rules import categorize_by_rule
from categorization.ml_classifier import train_model, load_model, predict_category
from categorization.llm_fallback import categorize_with_llm
import time

router = APIRouter(prefix="/categorize", tags=["categorization"])


@router.post("/rules")
def run_rule_categorization(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(Transaction.category == None).all()

    categorized_count = 0
    for txn in transactions:
        category = categorize_by_rule(txn.description)
        if category:
            txn.category = category
            txn.category_source = "rule"
            categorized_count += 1

    db.commit()
    remaining = db.query(Transaction).filter(Transaction.category == None).count()

    return {
        "categorized_by_rules": categorized_count,
        "still_uncategorized": remaining,
    }


@router.post("/train-ml")
def train_ml_model(db: Session = Depends(get_db)):
    labeled = db.query(Transaction).filter(
        Transaction.category_source.in_(["rule", "human"])
    ).all()

    if len(labeled) < 10:
        return {"error": "Not enough labeled data to train yet"}

    descriptions = [t.description for t in labeled]
    categories = [t.category for t in labeled]

    train_model(descriptions, categories)

    return {"message": f"Model trained on {len(labeled)} transactions ({sum(1 for t in labeled if t.category_source == 'human')} from human corrections)"}


@router.post("/ml")
def run_ml_categorization(db: Session = Depends(get_db)):
    model, vectorizer = load_model()
    if model is None:
        return {"error": "No trained model found. Call /categorize/train-ml first."}

    transactions = db.query(Transaction).filter(Transaction.category == None).all()

    categorized_count = 0
    for txn in transactions:
        predicted = predict_category(txn.description, model, vectorizer)
        txn.category = predicted
        txn.category_source = "ml"
        categorized_count += 1

    db.commit()
    remaining = db.query(Transaction).filter(Transaction.category == None).count()

    return {
        "categorized_by_ml": categorized_count,
        "still_uncategorized": remaining,
    }


@router.post("/llm")
def run_llm_categorization(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(Transaction.category == None).all()

    categorized_count = 0
    for txn in transactions:
        category = categorize_with_llm(txn.description)
        txn.category = category
        txn.category_source = "llm"
        categorized_count += 1
        time.sleep(4.5)  # stay under Gemini's free-tier rate limit (15 requests/minute)

    db.commit()
    remaining = db.query(Transaction).filter(Transaction.category == None).count()

    return {
        "categorized_by_llm": categorized_count,
        "still_uncategorized": remaining,
    }