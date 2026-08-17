from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from collections import defaultdict

from database import get_db
from models import Transaction
from anomaly.detector import detect_anomalies_zscore, detect_anomalies_isolation_forest

router = APIRouter(prefix="/anomaly", tags=["anomaly"])


@router.post("/detect")
def run_anomaly_detection(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(Transaction.type == "DEBIT").all()

    # Group transactions by category, since "unusual" depends on category context
    by_category = defaultdict(list)
    for txn in transactions:
        by_category[txn.category].append(txn)

    total_flagged = 0

    for category, txns in by_category.items():
        amounts = [t.amount for t in txns]

        z_flags = detect_anomalies_zscore(amounts)
        iso_flags = detect_anomalies_isolation_forest(amounts)

        for i, txn in enumerate(txns):
            # Flag as anomaly if EITHER method agrees it's unusual
            is_anomaly = z_flags[i] or iso_flags[i]
            txn.is_anomaly = 1 if is_anomaly else 0
            if is_anomaly:
                total_flagged += 1

    db.commit()

    return {
        "total_transactions_checked": len(transactions),
        "total_flagged_as_anomaly": total_flagged,
    }


@router.get("/flagged")
def get_flagged_transactions(db: Session = Depends(get_db)):
    flagged = db.query(Transaction).filter(Transaction.is_anomaly == 1).all()
    return flagged