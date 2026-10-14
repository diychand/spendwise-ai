import os
import sys
import certifi
from pathlib import Path

# Setup SSL & paths
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
sys.path.append(str(Path(__file__).resolve().parent.parent))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from database import SessionLocal
from models import Transaction
from agent.rag_service import FinancialRAGService

def main():
    print("=== Testing SpendWise AI 2026 RAG Engine ===")
    db = SessionLocal()
    txs = db.query(Transaction).all()
    print(f"Loaded {len(txs)} transactions from database.")

    rag = FinancialRAGService.get_instance()
    print(f"Knowledge Base indexed: {len(rag.kb_documents)} guidelines.")

    test_queries = [
        "How much did I spend on Swiggy and dining out?",
        "Can I buy a car worth ₹6,00,000?",
        "What is the 50/30/20 rule and how does my budget compare?",
        "How can I cut expenses to save ₹10,000?"
    ]

    for q in test_queries:
        print("\n" + "="*70)
        print(f"QUERY: '{q}'")
        res = rag.retrieve(query=q, transactions=txs, top_k_tx=3, top_k_kb=2)
        print(f"Route: {res['route']} (HyDE used: {res['hyde_used']})")
        print(f"Latency: {res['latency_ms']} ms")
        print(f"CRAG Confidence: {res['crag']['confidence']}")

        print("\nTop Retrieved Transactions (RRF):")
        for i, t in enumerate(res["retrieved_transactions"][:3], 1):
            print(f"  {i}. [{t['date']}] ₹{t['amount']} ({t['category']}) - {t['description']} (RRF: {t['rrf_score']:.4f}, Dense: {t['dense_score']:.3f}, BM25: {t['bm25_score']:.2f})")

        print("\nTop Retrieved Knowledge Guidelines:")
        for i, k in enumerate(res["retrieved_knowledge"][:2], 1):
            print(f"  {i}. {k['title']} (RRF: {k['rrf_score']:.4f}, Dense: {k['dense_score']:.3f})")

        formatted = rag.format_evidence_for_prompt(res)
        print("\nSample Formatted Prompt Evidence (first 250 chars):")
        print(formatted[:250] + "...")

    db.close()
    print("\n=== All RAG tests completed successfully! ===")

if __name__ == "__main__":
    main()
