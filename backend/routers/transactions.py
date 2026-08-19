import csv
import io
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Transaction
from routers.categorization import retrain_ml_model

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("/upload")
async def upload_transactions(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    decoded = contents.decode("utf-8")
    reader = csv.DictReader(io.StringIO(decoded))
    count = 0
    for row in reader:
        transaction = Transaction(
            date=row["date"],
            description=row["description"],
            amount=float(row["amount"]),
            type=row["type"],
        )
        db.add(transaction)
        count += 1
    db.commit()
    return {"message": f"Uploaded {count} transactions successfully"}


@router.get("/")
def list_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions


class CorrectionRequest(BaseModel):
    category: str


@router.patch("/{transaction_id}/correct")
def correct_transaction(transaction_id: int, request: CorrectionRequest, db: Session = Depends(get_db)):
    txn = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not txn:
        return {"error": f"Transaction {transaction_id} not found"}

    txn.category = request.category
    txn.category_source = "human"
    db.commit()

    # Immediately retrain the ML model so this correction takes effect right away
    retrain_result = retrain_ml_model(db)

    return {
        "message": f"Transaction {transaction_id} updated",
        "id": txn.id,
        "new_category": txn.category,
        "retrain_result": retrain_result,
    }