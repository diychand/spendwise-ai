from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import pandas as pd

from database import get_db
from models import Transaction
from agent.query_agent import generate_pandas_code, explain_result
from agent.sandbox import run_sandboxed_query

router = APIRouter(prefix="/agent", tags=["agent"])


class QueryRequest(BaseModel):
    question: str


@router.post("/query")
def query_transactions(request: QueryRequest, db: Session = Depends(get_db)):
    # Step 1: Load all transactions into a DataFrame
    transactions = db.query(Transaction).all()

    if not transactions:
        return {"error": "No transaction data available"}

    data = [{
        "date": t.date,
        "description": t.description,
        "amount": t.amount,
        "type": t.type,
        "category": t.category,
        "is_anomaly": t.is_anomaly,
    } for t in transactions]

    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])

    # Step 2: Ask the LLM to generate pandas code for this question
    generated_code = generate_pandas_code(request.question)

    # Step 3 & 4: Validate and execute in the sandbox
    success, result = run_sandboxed_query(generated_code, df)

    if not success:
        return {
            "question": request.question,
            "generated_code": generated_code,
            "error": result,
        }

    # Step 5: Convert the result to a natural language answer
    # Convert pandas/numpy types to plain Python types first, so they're JSON-safe
    if hasattr(result, "item"):  # numpy scalar types have .item()
        result = result.item()
    elif isinstance(result, pd.Series):
        result = result.to_dict()
    elif isinstance(result, pd.DataFrame):
        result = result.to_dict(orient="records")

    answer = explain_result(request.question, result)

    return {
        "question": request.question,
        "generated_code": generated_code,
        "raw_result": result,
        "answer": answer,
    }