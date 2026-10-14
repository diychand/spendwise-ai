from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import pandas as pd

from database import get_db
from models import Transaction
from agent.query_agent import generate_pandas_code, explain_result
from agent.sandbox import run_sandboxed_query
from agent.advice_agent import (
    compute_financial_profile,
    extract_purchase_details,
    calculate_goal_affordability,
    generate_advisor_response,
    generate_fallback_advice,
)
from agent.rag_service import FinancialRAGService
from logging_config import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/agent", tags=["agent"])


class QueryRequest(BaseModel):
    question: str


class AdviceRequest(BaseModel):
    question: str
    purchase_amount: Optional[float] = None
    timeframe_months: Optional[int] = None
    chat_history: Optional[List[Dict[str, Any]]] = None


class RAGRetrieveRequest(BaseModel):
    query: str
    top_k_tx: Optional[int] = 5
    top_k_kb: Optional[int] = 3


@router.post("/advice")
def get_financial_advice(request: AdviceRequest, db: Session = Depends(get_db)):
    try:
        transactions = db.query(Transaction).all()
        if not transactions:
            logger.warning("Advisor advice rejected: no transaction data")
            return {"error": "No transaction data available"}

        logger.info("Advisor query received: %r (transactions=%d)", request.question, len(transactions))

        # Step 1: Compute user's real financial profile
        profile = compute_financial_profile(transactions)

        # Step 2: Extract purchase details if specified or mentioned in text
        amount = request.purchase_amount
        timeframe = request.timeframe_months

        if amount is None:
            extracted = extract_purchase_details(request.question)
            amount = extracted.get("amount")
            if timeframe is None:
                timeframe = extracted.get("timeframe_months")

        # Step 3: Run affordability and accelerated cuts calculation if goal is present
        affordability = None
        if amount is not None and amount > 0:
            affordability = calculate_goal_affordability(amount, timeframe, profile)

        # Step 4: 2026 Hybrid RAG Retrieval (Adaptive Routing + BM25 + Gemini Dense + RRF + CRAG)
        rag_evidence = None
        try:
            rag_service = FinancialRAGService.get_instance()
            rag_evidence = rag_service.retrieve(
                query=request.question,
                transactions=transactions,
                top_k_tx=5,
                top_k_kb=3
            )
            logger.info("RAG retrieval completed (route=%s, latency=%.1fms, confidence=%s)",
                        rag_evidence.get("route"), rag_evidence.get("latency_ms", 0),
                        rag_evidence.get("crag", {}).get("confidence"))
        except Exception as rag_err:
            logger.warning("RAG retrieval failed (%s), proceeding with baseline financial profile", rag_err)

        # Step 5: Generate rich personalized advice with Gemini LLM grounded in RAG evidence
        advice_text = generate_advisor_response(
            question=request.question,
            profile=profile,
            affordability=affordability,
            chat_history=request.chat_history,
            rag_evidence=rag_evidence
        )

        evidence_summary = None
        if rag_evidence:
            evidence_summary = {
                "route": rag_evidence.get("route"),
                "confidence": rag_evidence.get("crag", {}).get("confidence", "MEDIUM"),
                "latency_ms": rag_evidence.get("latency_ms"),
                "hyde_used": rag_evidence.get("hyde_used", False),
                "transactions": [
                    {
                        "date": t.get("date"),
                        "amount": t.get("amount"),
                        "category": t.get("category"),
                        "description": t.get("description"),
                        "rrf_score": round(t.get("rrf_score", 0.0), 4),
                        "nature": t.get("nature")
                    }
                    for t in rag_evidence.get("retrieved_transactions", [])
                ],
                "guidelines": [
                    {
                        "title": k.get("title"),
                        "summary": k.get("summary"),
                        "category": k.get("category"),
                        "rrf_score": round(k.get("rrf_score", 0.0), 4)
                    }
                    for k in rag_evidence.get("retrieved_knowledge", [])
                ]
            }

        return {
            "question": request.question,
            "advice": advice_text,
            "profile_summary": {
                "avg_monthly_income": profile.get("avg_monthly_income"),
                "avg_monthly_expense": profile.get("avg_monthly_expense"),
                "avg_monthly_surplus": profile.get("avg_monthly_surplus"),
                "savings_rate_pct": profile.get("savings_rate_pct"),
                "num_months": profile.get("num_months"),
            },
            "affordability": affordability,
            "retrieved_evidence": evidence_summary,
        }
    except Exception as e:
        logger.exception("Error generating financial advice: %s", e)
        # Fallback to deterministic advice if an unexpected error occurs
        try:
            profile = compute_financial_profile(transactions) if 'transactions' in locals() else {}
            current_affordability = affordability if 'affordability' in locals() else None
            fallback_text = generate_fallback_advice(request.question, profile, current_affordability)
            return {
                "question": request.question,
                "advice": fallback_text,
                "profile_summary": {
                    "avg_monthly_income": profile.get("avg_monthly_income"),
                    "avg_monthly_expense": profile.get("avg_monthly_expense"),
                    "avg_monthly_surplus": profile.get("avg_monthly_surplus"),
                    "savings_rate_pct": profile.get("savings_rate_pct"),
                },
                "affordability": current_affordability,
            }
        except Exception:
            return {"error": f"Failed to generate advice: {str(e)}"}


@router.post("/query")
def query_transactions(request: QueryRequest, db: Session = Depends(get_db)):
    # Step 1: Load all transactions into a DataFrame
    transactions = db.query(Transaction).all()

    if not transactions:
        logger.warning("Agent query rejected: no transaction data")
        return {"error": "No transaction data available"}

    logger.info("Agent query received: %r (transactions=%d)", request.question, len(transactions))
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
    logger.info("Agent generated code for %r: %s", request.question, generated_code)

    # Step 3 & 4: Validate and execute in the sandbox
    success, result = run_sandboxed_query(generated_code, df)
    logger.info("Sandbox execution success=%s", success)

    if not success:
        logger.warning("Agent sandbox execution failed: %s", result)
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


@router.post("/rag/retrieve")
def retrieve_rag_context(request: RAGRetrieveRequest, db: Session = Depends(get_db)):
    """
    Direct endpoint to inspect 2026 Hybrid Contextual RAG retrieval results.
    Returns adaptive routing, HyDE output, BM25 + Dense scores, RRF fused rankings,
    and CRAG confidence assessment.
    """
    transactions = db.query(Transaction).all()
    rag_service = FinancialRAGService.get_instance()
    evidence = rag_service.retrieve(
        query=request.query,
        transactions=transactions,
        top_k_tx=request.top_k_tx or 5,
        top_k_kb=request.top_k_kb or 3
    )
    return evidence