import os
import re
import json
import time
import hashlib
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

import numpy as np
from rank_bm25 import BM25Okapi
from google import genai
from google.genai import types
from dotenv import load_dotenv

from logging_config import get_logger
from database import DB_PATH
from models import Transaction

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent.parent / ".env")
logger = get_logger(__name__)

# Core Model Configuration
EMBEDDING_MODEL = "models/gemini-embedding-2"
GENERATION_MODEL = "gemini-3.5-flash-lite"
KB_PATH = Path(__file__).resolve().parent.parent / "data" / "knowledge_base.json"


def get_genai_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    return genai.Client(api_key=api_key)


# ==============================================================================
# 1. EMBEDDING CACHE SYSTEM (SQLite-backed persistent vector store)
# ==============================================================================
class EmbeddingCache:
    """
    Persistent SQLite embedding cache to avoid redundant API calls and enable
    sub-10ms similarity searches on previously seen transactions and knowledge docs.
    """
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = str(db_path)
        self._init_table()
        self._memory_cache: Dict[str, np.ndarray] = {}

    def _init_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS rag_embeddings (
                    text_hash TEXT PRIMARY KEY,
                    text_content TEXT,
                    embedding_json TEXT
                )
            """)
            conn.commit()

    @staticmethod
    def hash_text(text: str) -> str:
        return hashlib.sha256(text.strip().encode("utf-8")).hexdigest()

    def get_many(self, hashes: List[str]) -> Dict[str, np.ndarray]:
        found = {}
        missing = []
        for h in hashes:
            if h in self._memory_cache:
                found[h] = self._memory_cache[h]
            else:
                missing.append(h)

        if missing:
            with sqlite3.connect(self.db_path) as conn:
                cur = conn.cursor()
                placeholders = ",".join("?" for _ in missing)
                cur.execute(
                    f"SELECT text_hash, embedding_json FROM rag_embeddings WHERE text_hash IN ({placeholders})",
                    missing
                )
                for thash, emb_json in cur.fetchall():
                    vec = np.array(json.loads(emb_json), dtype=np.float32)
                    self._memory_cache[thash] = vec
                    found[thash] = vec

        return found

    def put_many(self, entries: List[Tuple[str, str, np.ndarray]]):
        if not entries:
            return
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            records = [
                (thash, text, json.dumps(vec.tolist()))
                for thash, text, vec in entries
            ]
            cur.executemany(
                "INSERT OR REPLACE INTO rag_embeddings (text_hash, text_content, embedding_json) VALUES (?, ?, ?)",
                records
            )
            conn.commit()

        for thash, _, vec in entries:
            self._memory_cache[thash] = vec


# ==============================================================================
# 2. CONTEXTUAL CHUNK ENRICHER (from Nir Diamant's contextual_chunk_headers)
# ==============================================================================
class TransactionContextEnricher:
    """
    Enriches raw transaction rows with contextual metadata headers before indexing.
    Short merchant names ('Swiggy', 'Uber', 'Electricity') are enriched with:
    - Month and day of the week
    - Essential (Needs) vs Discretionary (Wants) budget tagging
    - Month total category spend context
    """
    DISCRETIONARY_CATEGORIES = {"Food", "Shopping", "Entertainment", "Travel"}
    ESSENTIAL_CATEGORIES = {"Rent", "Bills", "Groceries"}

    @classmethod
    def enrich(cls, transactions: List[Transaction]) -> List[Dict[str, Any]]:
        if not transactions:
            return []

        # First pass: compute monthly totals per category
        month_cat_totals: Dict[Tuple[str, str], float] = {}
        for t in transactions:
            m = t.date[:7] if t.date and len(t.date) >= 7 else "Unknown"
            cat = t.category or "Other"
            key = (m, cat)
            month_cat_totals[key] = month_cat_totals.get(key, 0.0) + (t.amount or 0.0)

        enriched_records = []
        for t in transactions:
            date_str = t.date or "2026-01-01"
            m = date_str[:7]
            cat = t.category or "Other"
            amt = float(t.amount or 0.0)
            ttype = (t.type or "DEBIT").upper()

            # Determine discretionary status
            if ttype == "CREDIT":
                nature = "Income / Credit Inflow"
            elif cat in cls.DISCRETIONARY_CATEGORIES:
                nature = "Discretionary (Want / Flexible Spending)"
            elif cat in cls.ESSENTIAL_CATEGORIES:
                nature = "Essential (Need / Fixed Commitment)"
            else:
                nature = "General Expense"

            month_cat_spend = month_cat_totals.get((m, cat), amt)

            # Build Nir Diamant style contextual header
            header = f"[Context: Month {m} | Type: {ttype} | Category: {cat} ({nature}) | Monthly Category Total: ₹{month_cat_spend:,.2f}]"
            content = f"Transaction: {t.description} | Amount: ₹{amt:,.2f} | Date: {date_str}"
            full_enriched_text = f"{header}\n{content}"

            enriched_records.append({
                "id": t.id,
                "date": date_str,
                "description": t.description,
                "amount": amt,
                "type": ttype,
                "category": cat,
                "nature": nature,
                "is_anomaly": bool(t.is_anomaly),
                "enriched_text": full_enriched_text,
                "header": header,
                "content": content
            })

        return enriched_records


# ==============================================================================
# 3. HYPOTHETICAL DOCUMENT EMBEDDING (HyDE) GENERATOR
# ==============================================================================
class HyDEGenerator:
    """
    Implements HyDE from Nir Diamant's RAG Techniques.
    For abstract, goal-oriented, or audit questions, generates a hypothetical
    financial statement excerpt or planning scenario to bridge semantic distance.
    """
    def __init__(self, client: genai.Client):
        self.client = client

    def generate_hypothetical_context(self, query: str) -> Optional[str]:
        prompt = f"""You are a financial retrieval assistant.
Given the user's financial question, generate a brief (2-3 sentence) hypothetical financial statement excerpt or scenario that directly answers or relates to this query.
Do not answer the user directly. Write the kind of transaction log summary or financial planning rule text that would be the perfect match in a database.

Query: "{query}"

Hypothetical excerpt:"""
        try:
            res = self.client.models.generate_content(
                model=GENERATION_MODEL,
                contents=prompt
            )
            return res.text.strip()
        except Exception as e:
            logger.warning("HyDE generation failed (%s), falling back to raw query", e)
            return None


# ==============================================================================
# 4. ADAPTIVE RETRIEVAL ROUTER (from Nir Diamant's adaptive_retrieval)
# ==============================================================================
class AdaptiveRouter:
    """
    Classifies user financial intent to optimize retrieval weights and scope:
    - TRANSACTION_LOOKUP: Exact merchant, date, or amount lookup (High BM25 weight)
    - GOAL_PLANNING: Asset purchases, car/bike plans, savings timelines (Knowledge + Transactions)
    - BUDGET_AUDIT: Expense reduction, overspending analysis, discretionary audits (HyDE + Balanced)
    - FINANCIAL_CONCEPT: General financial rules, tax laws, investment concepts (Knowledge Base)
    """
    @staticmethod
    def route_query(query: str) -> Dict[str, Any]:
        q = query.lower()

        # Check for specific merchants or transaction lookup patterns
        merchants = ["swiggy", "zomato", "uber", "ola", "amazon", "flipkart", "netflix", "landlord", "rent", "recharge", "groceries", "salary"]
        has_merchant = any(m in q for m in merchants)
        is_lookup = any(p in q for p in ["how much did i spend on", "find transaction", "show transactions", "what did i buy", "spent on", "last transaction", "highest expense", "my debit"])

        # Check for goal planning
        is_goal = any(p in q for p in ["buy a car", "buy car", "buy a bike", "buy bike", "can i afford", "purchase", "save for", "down payment", "emi for", "goal"])

        # Check for financial concept
        is_concept = any(p in q for p in ["what is", "explain", "50/30/20", "avalanche", "snowball", "rule for", "emergency fund definition", "80c", "nps", "tax regime"])

        # Check for budget audit
        is_audit = any(p in q for p in ["cut expense", "cut spending", "save more", "overspending", "bleeding money", "where am i spending", "budget audit", "reduce cost"])

        if is_lookup or has_merchant:
            return {
                "route": "TRANSACTION_LOOKUP",
                "bm25_weight": 0.65,
                "dense_weight": 0.35,
                "use_hyde": False,
                "search_transactions": True,
                "search_kb": False,
                "top_k_tx": 6,
                "top_k_kb": 1
            }
        elif is_goal:
            return {
                "route": "GOAL_PLANNING",
                "bm25_weight": 0.35,
                "dense_weight": 0.65,
                "use_hyde": True,
                "search_transactions": True,
                "search_kb": True,
                "top_k_tx": 5,
                "top_k_kb": 2
            }
        elif is_concept and not is_audit:
            return {
                "route": "FINANCIAL_CONCEPT",
                "bm25_weight": 0.30,
                "dense_weight": 0.70,
                "use_hyde": False,
                "search_transactions": False,
                "search_kb": True,
                "top_k_tx": 1,
                "top_k_kb": 3
            }
        else: # BUDGET_AUDIT or general query
            return {
                "route": "BUDGET_AUDIT",
                "bm25_weight": 0.45,
                "dense_weight": 0.55,
                "use_hyde": True,
                "search_transactions": True,
                "search_kb": True,
                "top_k_tx": 5,
                "top_k_kb": 2
            }


# ==============================================================================
# 5. HYBRID FUSION RETRIEVER (BM25 + Dense Gemini-Embedding-2 + RRF)
# ==============================================================================
class HybridRetriever:
    """
    Executes hybrid retrieval combining sparse BM25 and dense semantic search
    using Reciprocal Rank Fusion (RRF) as demonstrated in Nir Diamant's fusion_retrieval.py.
    """
    def __init__(self, client: genai.Client, cache: EmbeddingCache):
        self.client = client
        self.cache = cache

    @staticmethod
    def tokenize(text: str) -> List[str]:
        return re.findall(r"\b\w+\b", text.lower())

    def get_dense_embeddings(self, texts: List[str]) -> np.ndarray:
        """
        Embeds texts with batching and SQLite caching.
        """
        if not texts:
            return np.empty((0, 3072), dtype=np.float32)

        hashes = [self.cache.hash_text(t) for t in texts]
        cached = self.cache.get_many(hashes)

        missing_indices = [i for i, h in enumerate(hashes) if h not in cached]
        if missing_indices:
            missing_texts = [texts[i] for i in missing_indices]
            logger.info("Computing dense embeddings for %d uncached texts", len(missing_texts))

            # Batch in chunks of 25 to respect API payload limits
            BATCH_SIZE = 25
            to_save = []
            for start_idx in range(0, len(missing_texts), BATCH_SIZE):
                chunk = missing_texts[start_idx:start_idx + BATCH_SIZE]
                content_objects = [
                    types.Content(parts=[types.Part.from_text(text=t)])
                    for t in chunk
                ]
                try:
                    res = self.client.models.embed_content(
                        model=EMBEDDING_MODEL,
                        contents=content_objects
                    )
                    for j, emb in enumerate(res.embeddings):
                        vec = np.array(emb.values, dtype=np.float32)
                        # Normalize vector for cosine similarity
                        norm = np.linalg.norm(vec)
                        if norm > 0:
                            vec = vec / norm
                        orig_text = chunk[j]
                        thash = self.cache.hash_text(orig_text)
                        cached[thash] = vec
                        to_save.append((thash, orig_text, vec))
                except Exception as e:
                    logger.error("Error in dense embedding batch: %s", e)
                    # Fallback for failed items: zero vector
                    for orig_text in chunk:
                        thash = self.cache.hash_text(orig_text)
                        cached[thash] = np.zeros(3072, dtype=np.float32)

            if to_save:
                self.cache.put_many(to_save)

        # Assemble array in original order
        matrix = np.array([cached[h] for h in hashes], dtype=np.float32)
        return matrix

    def embed_single_query(self, query: str) -> np.ndarray:
        clean_q = query.strip().lower()
        q_hash = self.cache.hash_text(clean_q)
        cached = self.cache.get_many([q_hash])
        if q_hash in cached:
            return cached[q_hash]

        for attempt in range(2):
            try:
                res = self.client.models.embed_content(
                    model=EMBEDDING_MODEL,
                    contents=clean_q
                )
                vec = np.array(res.embeddings[0].values, dtype=np.float32)
                norm = np.linalg.norm(vec)
                if norm > 0:
                    vec = vec / norm
                self.cache.put_many([(q_hash, clean_q, vec)])
                return vec
            except Exception as e:
                if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
                    if attempt == 0:
                        logger.warning("Embedding rate limit encountered, waiting 2s before retry...")
                        time.sleep(2)
                        continue
                logger.warning("Embedding query failed (%s), falling back to sparse BM25", e)
                break

        return np.zeros(3072, dtype=np.float32)

    def retrieve_hybrid(
        self,
        query: str,
        documents: List[Dict[str, Any]],
        doc_embeddings: np.ndarray,
        bm25: Optional[BM25Okapi],
        top_k: int = 5,
        bm25_weight: float = 0.5,
        dense_weight: float = 0.5,
        rrf_k: int = 60
    ) -> List[Dict[str, Any]]:
        """
        Reciprocal Rank Fusion (RRF) between BM25 and Dense Cosine Similarity.
        Score = bm25_weight / (rrf_k + rank_bm25) + dense_weight / (rrf_k + rank_dense)
        """
        n_docs = len(documents)
        if n_docs == 0:
            return []

        # 1. Sparse BM25 scoring & ranking
        query_tokens = self.tokenize(query)
        if bm25 and query_tokens:
            bm25_scores = bm25.get_scores(query_tokens)
        else:
            bm25_scores = np.zeros(n_docs)

        bm25_rankings = np.argsort(-bm25_scores)  # descending order
        rank_bm25_map = {doc_idx: rank + 1 for rank, doc_idx in enumerate(bm25_rankings)}

        # 2. Dense Semantic scoring & ranking
        q_vec = self.embed_single_query(query)
        if doc_embeddings.shape[0] == n_docs and np.linalg.norm(q_vec) > 0:
            # Cosine similarity (vectors are already L2 normalized)
            dense_scores = np.dot(doc_embeddings, q_vec)
        else:
            dense_scores = np.zeros(n_docs)

        dense_rankings = np.argsort(-dense_scores)
        rank_dense_map = {doc_idx: rank + 1 for rank, doc_idx in enumerate(dense_rankings)}

        # 3. Reciprocal Rank Fusion
        fused_results = []
        for i in range(n_docs):
            r_bm25 = rank_bm25_map[i]
            r_dense = rank_dense_map[i]

            # RRF formula
            rrf_score = (bm25_weight / (rrf_k + r_bm25)) + (dense_weight / (rrf_k + r_dense))

            # Store rich candidate entry
            item = dict(documents[i])
            item["rrf_score"] = float(rrf_score)
            item["bm25_score"] = float(bm25_scores[i])
            item["dense_score"] = float(dense_scores[i])
            item["bm25_rank"] = r_bm25
            item["dense_rank"] = r_dense
            fused_results.append(item)

        # Sort descending by RRF score
        fused_results.sort(key=lambda x: x["rrf_score"], reverse=True)
        return fused_results[:top_k]


# ==============================================================================
# 6. CORRECTIVE RAG (CRAG) & RE-RANKING EVALUATOR
# ==============================================================================
class CRAGValidator:
    """
    Implements Corrective RAG (CRAG) from Nir Diamant's crag.py.
    Assesses confidence of retrieved candidates.
    If retrieval confidence is weak, triggers query adjustment or signals
    to LLM generator not to hallucinate unverified transactions.
    """
    @staticmethod
    def evaluate_retrieval(
        query: str,
        retrieved_txns: List[Dict[str, Any]],
        retrieved_kb: List[Dict[str, Any]],
        route: str
    ) -> Dict[str, Any]:
        confidence = "HIGH"
        notes = []

        if route == "TRANSACTION_LOOKUP":
            if not retrieved_txns:
                confidence = "LOW"
                notes.append("No transactions found matching query.")
            else:
                top_dense = retrieved_txns[0].get("dense_score", 0.0)
                top_bm25 = retrieved_txns[0].get("bm25_score", 0.0)
                if top_bm25 == 0 and top_dense < 0.30:
                    confidence = "LOW"
                    notes.append("Weak match with transactions; verify if merchant exists.")
                elif top_bm25 > 0 or top_dense >= 0.50:
                    confidence = "HIGH"
                else:
                    confidence = "MEDIUM"

        elif route == "GOAL_PLANNING":
            if not retrieved_kb:
                confidence = "MEDIUM"
                notes.append("No specific planning guidelines matched, defaulting to 50/30/20.")
            else:
                confidence = "HIGH"

        else: # BUDGET_AUDIT or FINANCIAL_CONCEPT
            if retrieved_kb or retrieved_txns:
                confidence = "HIGH"
            else:
                confidence = "MEDIUM"

        return {
            "confidence": confidence,
            "notes": notes,
            "top_tx_dense": retrieved_txns[0].get("dense_score", 0.0) if retrieved_txns else 0.0,
            "top_tx_bm25": retrieved_txns[0].get("bm25_score", 0.0) if retrieved_txns else 0.0,
        }


# ==============================================================================
# 7. FINANCIAL RAG SERVICE ORCHESTRATOR
# ==============================================================================
class FinancialRAGService:
    """
    Master service coordinating:
    1. Transaction context enrichment & indexing
    2. Curated knowledge base indexing
    3. Adaptive query routing
    4. Optional HyDE hypothetical document generation
    5. Hybrid BM25 + Dense vector retrieval with RRF fusion
    6. CRAG evaluation and prompt grounding formatting
    """
    _instance = None

    def __init__(self):
        self.client = get_genai_client()
        self.cache = EmbeddingCache()
        self.retriever = HybridRetriever(self.client, self.cache)
        self.hyde = HyDEGenerator(self.client)
        self.enricher = TransactionContextEnricher()

        # Knowledge Base State
        self.kb_documents: List[Dict[str, Any]] = []
        self.kb_embeddings: np.ndarray = np.empty((0, 3072), dtype=np.float32)
        self.kb_bm25: Optional[BM25Okapi] = None
        self._load_and_index_knowledge_base()

        # Transaction State
        self.tx_documents: List[Dict[str, Any]] = []
        self.tx_embeddings: np.ndarray = np.empty((0, 3072), dtype=np.float32)
        self.tx_bm25: Optional[BM25Okapi] = None
        self._last_tx_count: int = 0

    @classmethod
    def get_instance(cls) -> "FinancialRAGService":
        if cls._instance is None:
            cls._instance = FinancialRAGService()
        return cls._instance

    def _load_and_index_knowledge_base(self):
        if not KB_PATH.exists():
            logger.warning("Knowledge base file not found at %s", KB_PATH)
            return

        try:
            with open(KB_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.kb_documents = []
            kb_texts = []
            for doc in data:
                rules_str = "\n".join(f"- {r}" for r in doc.get("key_rules", []))
                keywords_str = ", ".join(doc.get("search_keywords", []))
                full_text = f"Title: {doc['title']}\nCategory: {doc.get('category','')}\nSummary: {doc.get('summary','')}\nKey Rules:\n{rules_str}\nDetailed Guidance: {doc.get('detailed_guidance','')}\nKeywords: {keywords_str}"

                doc_entry = dict(doc)
                doc_entry["enriched_text"] = full_text
                self.kb_documents.append(doc_entry)
                kb_texts.append(full_text)

            # Build BM25 index
            tokenized_kb = [self.retriever.tokenize(t) for t in kb_texts]
            self.kb_bm25 = BM25Okapi(tokenized_kb)

            # Pre-compute or load dense embeddings
            self.kb_embeddings = self.retriever.get_dense_embeddings(kb_texts)
            logger.info("Indexed %d knowledge base financial guidelines", len(self.kb_documents))
        except Exception as e:
            logger.exception("Failed to index knowledge base: %s", e)

    def sync_transactions(self, transactions: List[Transaction]):
        """
        Enriches and indexes transactions if transaction count has changed.
        """
        if len(transactions) == self._last_tx_count and self.tx_bm25 is not None:
            return

        logger.info("Synchronizing and enriching %d transactions for RAG", len(transactions))
        start = time.perf_counter()

        self.tx_documents = self.enricher.enrich(transactions)
        tx_texts = [t["enriched_text"] for t in self.tx_documents]

        # Build BM25 index
        tokenized_tx = [self.retriever.tokenize(t) for t in tx_texts]
        self.tx_bm25 = BM25Okapi(tokenized_tx)

        # Get dense embeddings (uses SQLite cache for existing ones)
        self.tx_embeddings = self.retriever.get_dense_embeddings(tx_texts)
        self._last_tx_count = len(transactions)

        logger.info("RAG transaction index complete in %.2fs (Indexed=%d)", time.perf_counter() - start, len(self.tx_documents))

    def retrieve(
        self,
        query: str,
        transactions: Optional[List[Transaction]] = None,
        top_k_tx: int = 5,
        top_k_kb: int = 3
    ) -> Dict[str, Any]:
        """
        Full 2026 RAG Retrieval Pipeline:
        1. Sync transactions if provided
        2. Route query (Adaptive Retrieval)
        3. HyDE query generation if applicable
        4. Hybrid retrieval over transactions (BM25 + Dense + RRF)
        5. Hybrid retrieval over knowledge base (BM25 + Dense + RRF)
        6. CRAG evaluation
        """
        start_time = time.perf_counter()

        if transactions:
            self.sync_transactions(transactions)

        # 1. Adaptive Query Routing
        route_info = AdaptiveRouter.route_query(query)
        route = route_info["route"]
        bm25_w = route_info["bm25_weight"]
        dense_w = route_info["dense_weight"]

        # 2. HyDE Generation
        search_query = query
        hyde_context = None
        if route_info["use_hyde"]:
            hyde_context = self.hyde.generate_hypothetical_context(query)
            if hyde_context:
                search_query = f"{query}\nContext: {hyde_context}"

        # 3. Retrieve Transactions
        retrieved_txns = []
        if route_info["search_transactions"] and self.tx_documents:
            k_tx = max(top_k_tx, route_info.get("top_k_tx", 5))
            retrieved_txns = self.retriever.retrieve_hybrid(
                query=search_query,
                documents=self.tx_documents,
                doc_embeddings=self.tx_embeddings,
                bm25=self.tx_bm25,
                top_k=k_tx,
                bm25_weight=bm25_w,
                dense_weight=dense_w
            )

        # 4. Retrieve Knowledge Base Rules
        retrieved_kb = []
        if route_info["search_kb"] and self.kb_documents:
            k_kb = max(top_k_kb, route_info.get("top_k_kb", 2))
            retrieved_kb = self.retriever.retrieve_hybrid(
                query=query, # Direct query usually best for KB concepts
                documents=self.kb_documents,
                doc_embeddings=self.kb_embeddings,
                bm25=self.kb_bm25,
                top_k=k_kb,
                bm25_weight=0.4,
                dense_weight=0.6
            )

        # 5. CRAG Validation
        crag_result = CRAGValidator.evaluate_retrieval(query, retrieved_txns, retrieved_kb, route)

        latency_ms = round((time.perf_counter() - start_time) * 1000, 1)

        return {
            "query": query,
            "route": route,
            "route_details": route_info,
            "hyde_used": hyde_context is not None,
            "hyde_passage": hyde_context,
            "retrieved_transactions": retrieved_txns,
            "retrieved_knowledge": retrieved_kb,
            "crag": crag_result,
            "latency_ms": latency_ms
        }

    @staticmethod
    def format_evidence_for_prompt(evidence: Dict[str, Any]) -> str:
        """
        Formats retrieved transaction evidence and verified knowledge base rules
        into high-signal prompt sections for the LLM generator.
        """
        txns = evidence.get("retrieved_transactions", [])
        kb_items = evidence.get("retrieved_knowledge", [])
        route = evidence.get("route", "GENERAL")
        crag = evidence.get("crag", {})

        parts = []

        if txns:
            tx_lines = ["RETRIEVED TRANSACTION EVIDENCE (Ground truth records from user database):"]
            for i, t in enumerate(txns, 1):
                date = t.get("date", "")
                desc = t.get("description", "")
                amt = t.get("amount", 0.0)
                cat = t.get("category", "")
                ttype = t.get("type", "DEBIT")
                nature = t.get("nature", "")
                tx_lines.append(f"[{i}] {date} | ₹{amt:,.2f} ({ttype}) | {cat} ({nature}) | {desc}")
            parts.append("\n".join(tx_lines))

        if kb_items:
            kb_lines = ["VERIFIED FINANCIAL BENCHMARKS & PLANNING RULES:"]
            for k in kb_items:
                title = k.get("title", "")
                summary = k.get("summary", "")
                rules = k.get("key_rules", [])
                guidance = k.get("detailed_guidance", "")
                rules_txt = " ".join(f"• {r}" for r in rules[:3])
                kb_lines.append(f"■ {title}: {summary}\n  Rules: {rules_txt}\n  Guidance: {guidance}")
            parts.append("\n".join(kb_lines))

        if crag.get("confidence") == "LOW":
            parts.append("CRAG DIRECTIVE: Retrieval confidence on specific merchant transactions is low. Ground your analysis strictly in the user's computed monthly surplus and category averages; do not invent unverified transactions.")

        return "\n\n".join(parts)
