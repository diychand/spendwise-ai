# -*- coding: utf-8 -*-
"""
Chapter 1 Module for PG Project Report - SpendWise AI
Sections:
Chapter 1 Introduction
1.1 Background of the Study
1.2 Problem Statement
1.3 Objectives of the Project
1.4 Scope of the Project
1.5 Significance of the Project
"""

def get_chapter1_pages():
    pages = []

    # -------------------------------------------------------------
    # PAGE 1 (Report Page 1): Chapter 1 Title & 1.1 Background
    # -------------------------------------------------------------
    page1 = """
    <div class="page page-arabic" data-page="1">
        <div class="page-content">
            <h1 class="chapter-title">CHAPTER 1<br>INTRODUCTION</h1>
            
            <h2 class="section-heading">1.1 Background of the Study</h2>
            <p>
                In an increasingly digitized global economy, electronic financial transactions have superseded conventional paper currency across commercial, retail, and peer-to-peer domains. The ubiquity of debit cards, credit instruments, mobile point-of-sale systems, and unified payment interfaces has generated vast volumes of personal financial transactional records. Individual consumers routinely engage with dozens of disparate merchants each month, producing heterogeneous transactional ledger streams characterized by cryptic merchant codes, inconsistent memo syntax, and temporal fragmentation.
            </p>
            <p>
                Despite the widespread availability of digital banking applications, personal financial management remains a daunting cognitive challenge for the average individual. Most retail banking interfaces function merely as static digital ledgers; they display historical debit and credit entries chronologically without offering predictive foresight, intelligent categorization, or actionable budgetary guidance. Consequently, users struggle to maintain a clear mental model of their true discretionary cash flow, fail to detect creeping expenditure patterns across subscription services, and remain vulnerable to undetected financial anomalies and fraudulent recurring debits.
            </p>
            <p>
                Traditional personal financial management software applications have historically relied on rigid, rule-based heuristics and static regular expressions to parse transaction descriptions. While computationally inexpensive, deterministic keyword matching fails catastrophically when encountering obfuscated banking codes, regional vendor aliases, abbreviations, and non-standardized payment gateway descriptions. A merchant description such as "SQ *BLUE BOTTLE COFFEE SAN FRANCISCO" or "POS DEBIT - AMZN MKTPLACE PMTS 800-992-3845" is easily fragmented by brittle rule sets, leading to large volumes of misclassified or "Uncategorized" expenditures that erode user trust and undermine long-term financial planning.
            </p>
            <p>
                Simultaneously, the discipline of Artificial Intelligence has witnessed a paradigm shift through the emergence of Large Language Models (LLMs) and dense semantic vector representations. Modern transformer architectures demonstrate unprecedented capabilities in natural language understanding, semantic disambiguation, and multi-step reasoning. However, direct naive application of cloud-hosted generative LLMs to large-scale transaction categorization introduces prohibitive API monetary costs, unacceptably high round-trip latency, and critical privacy vulnerabilities associated with transmitting unredacted personal banking data over external networks.
            </p>
        </div>
        <div class="page-footer">1</div>
    </div>
    """
    pages.append(page1)

    # -------------------------------------------------------------
    # PAGE 2 (Report Page 2): 1.1 Background (cont.) & 1.2 Problem Statement
    # -------------------------------------------------------------
    page2 = """
    <div class="page page-arabic" data-page="2">
        <div class="page-content">
            <p>
                To resolve this tension between computational efficiency and semantic intelligence, modern AI systems design favors tiered, hybrid architectures. In such configurations, ultra-fast deterministic rules handle unambiguous merchant entities in sub-millisecond durations, lightweight machine learning classifiers manage the intermediate distribution of common spending patterns, and powerful generative foundation models are reserved exclusively as an intelligent escalation tier for highly ambiguous or novel edge cases.
            </p>
            <p>
                Furthermore, financial advice cannot be reliably delivered through static statistical summaries alone. Real-world financial decision-making is inherently conversational and contextual. When a consumer inquires, "Can I afford a $1,200 vacation next month without compromising my quarterly emergency reserve?", an intelligent system must synthesize historical cash inflow patterns, non-discretionary recurring liabilities, projected seasonal anomalies, and personalized savings goals. Generic LLM chatbots cannot perform this task accurately without ground-truth factual grounding, as they are prone to mathematical hallucination and lack visibility into the user's localized transaction database.
            </p>
            <p>
                Retrieval-Augmented Generation (RAG) has emerged as the premier architectural paradigm for grounding generative AI systems on domain-specific factual corpuses. However, standard naive RAG pipelines—which rely solely on dense cosine similarity over generic text chunks—exhibit severe degradation in personal financial contexts. Financial inquiries often involve precise monetary figures, dates, and vendor names where semantic similarity fails to differentiate between a "$150.00 utility bill" and a "$1,500.00 rent payment." Addressing this operational bottleneck requires advanced 2026 RAG innovations, notably Hypothetical Document Embeddings (HyDE), hybrid sparse-dense retrieval combining BM25 with dense vector embeddings, Reciprocal Rank Fusion (RRF), and Corrective RAG (CRAG) factual verification.
            </p>

            <h2 class="section-heading">1.2 Problem Statement</h2>
            <p>
                Contemporary personal finance systems suffer from three fundamental architectural and algorithmic deficiencies that impair their effectiveness as autonomous financial copilots:
            </p>
            <p>
                1. <strong>Brittleness and High Latency in Transaction Categorization:</strong> Existing solutions either utilize rigid rule tables that fail to generalize to novel merchants, or route all transactions through computationally expensive foundation models, resulting in unsustainable latency and financial cost. There exists an acute need for a multi-tiered cascading categorization framework that guarantees real-time throughput while achieving near-human semantic precision across arbitrary transaction ledgers.
            </p>
        </div>
        <div class="page-footer">2</div>
    </div>
    """
    pages.append(page2)

    # -------------------------------------------------------------
    # PAGE 3 (Report Page 3): 1.2 Problem Statement (cont.) & 1.3 Objectives
    # -------------------------------------------------------------
    page3 = """
    <div class="page page-arabic" data-page="3">
        <div class="page-content">
            <p>
                2. <strong>Absence of Unsupervised Multi-Dimensional Anomaly Detection:</strong> Most personal budgeting applications treat all transactions uniformly, failing to notify users of statistical spending spikes, duplicate card charges, or atypical vendor charges until monthly credit statements are reviewed. Traditional threshold-based alerts (e.g., flagging any transaction exceeding $500) produce overwhelming false positive rates because they ignore personal spending variance, category-specific baselines, and temporal seasonality. An effective financial system requires unsupervised machine learning capable of isolating multi-dimensional statistical outliers without requiring labeled historical fraud datasets.
            </p>
            <p>
                3. <strong>Hallucination and Contextual Disconnection in Conversational Financial Advisory:</strong> Existing generative AI assistants applied to financial domains hallucinate arithmetic calculations, formulate ungrounded recommendations, and fail to incorporate multi-month fiscal trends. Standard RAG architectures fail in financial analysis due to vocabulary mismatch between conversational queries and raw banking ledger descriptions. A rigorous, mathematically grounded hybrid retrieval architecture is needed to ground conversational advice in verifiable transactional evidence.
            </p>

            <h2 class="section-heading">1.3 Objectives of the Project</h2>
            <p>
                The primary objective of this project is to conceptualize, architect, implement, and validate <strong>SpendWise AI</strong>, an autonomous, multi-tier financial intelligence platform that unifies deterministic rules, machine learning classifiers, unsupervised anomaly detection, and state-of-the-art hybrid contextual RAG.
            </p>
            <p>
                The specific technical and research objectives of this investigation include:
            </p>
            <ol>
                <li>
                    <strong>Design and Engineering of an Asynchronous REST Microservice Backend:</strong> To develop a high-performance backend using FastAPI and SQLAlchemy ORM that orchestrates transaction ingestion, automated normalization, persistent SQLite storage, and analytical aggregation with sub-second response times.
                </li>
                <li>
                    <strong>Implementation of a Three-Tier Cascading Categorization Engine:</strong> To construct a hierarchical classification pipeline comprising Tier 1 regex/pattern dictionaries for sub-millisecond execution, Tier 2 TF-IDF n-gram vectorization with regularized Stochastic Gradient Descent (SGDClassifier) for high-speed statistical inference, and Tier 3 Google Gemini LLM few-shot reasoning for ambiguous edge cases.
                </li>
            </ol>
        </div>
        <div class="page-footer">3</div>
    </div>
    """
    pages.append(page3)

    # -------------------------------------------------------------
    # PAGE 4 (Report Page 4): 1.3 Objectives (cont.) & 1.4 Scope
    # -------------------------------------------------------------
    page4 = """
    <div class="page page-arabic" data-page="4">
        <div class="page-content">
            <ol start="3">
                <li>
                    <strong>Deployment of an Unsupervised Isolation Forest Anomaly Detection Engine:</strong> To formulate and evaluate an unsupervised ensemble anomaly detection model combining scikit-learn Isolation Forests with rolling category-specific Z-score statistical boundaries to detect expenditure outliers, duplicate charges, and irregular billing without labeled training data.
                </li>
                <li>
                    <strong>Formulation of a 2026 Hybrid Contextual RAG Financial Advisor:</strong> To build an advanced conversational reasoning agent integrating Hypothetical Document Embeddings (HyDE) for query expansion, dual-space sparse BM25 and dense Gemini Text-Embedding-004 indexing, Reciprocal Rank Fusion (RRF) rank aggregation, and Corrective RAG (CRAG) hallucination prevention heuristics.
                </li>
                <li>
                    <strong>Construction of a Modern, Claude-Style Conversational User Interface:</strong> To implement an ergonomic Streamlit frontend featuring an upward-stacking chat history, a permanently anchored bottom input bar, automated scroll anchoring, interactive financial metric cards, and responsive spending distribution visualizers.
                </li>
                <li>
                    <strong>Empirical Evaluation and Benchmarking:</strong> To rigorously evaluate system categorization accuracy, inference latency, anomaly detection ROC-AUC, RAG retrieval precision (MRR@5), and cost efficiency against baseline single-tier architectures.
                </li>
            </ol>

            <h2 class="section-heading">1.4 Scope of the Project</h2>
            <p>
                The scope of the SpendWise AI project encompasses the complete lifecycle of personal financial data ingestion, processing, modeling, analysis, and conversational interaction:
            </p>
            <p>
                The transactional ingestion subsystem supports arbitrary CSV ledger exports from major commercial banks. The system incorporates intelligent schema inference capable of auto-detecting and mapping non-standard column headers (e.g., "Trans Date", "Debit Amount", "Merchant Narrative") into a standardized internal representation.
            </p>
            <p>
                The categorization engine covers 14 standardized personal finance categories encompassing Food & Dining, Transportation, Utilities, Housing, Entertainment, Healthcare, Shopping, Personal Care, Education, Investments, Income, Transfers, Travel, and Miscellaneous Fees.
            </p>
        </div>
        <div class="page-footer">4</div>
    </div>
    """
    pages.append(page4)

    # -------------------------------------------------------------
    # PAGE 5 (Report Page 5): 1.4 Scope (cont.) & 1.5 Significance
    # -------------------------------------------------------------
    page5 = """
    <div class="page page-arabic" data-page="5">
        <div class="page-content">
            <p>
                The analytical scope includes temporal spending aggregations, recurring liability detection (e.g., identifying monthly SaaS subscriptions and utility bills), net cash flow velocity tracking, and discretionary savings ceiling computations.
            </p>
            <p>
                The conversational intelligence engine is designed to handle natural language financial inquiries, multi-turn budgeting negotiations, "what-if" scenario modeling, and structured debt reduction recommendations grounded directly in the user's uploaded ledger records.
            </p>
            <p>
                <em>System Boundaries:</em> The system operates as a private, single-user local deployment to maximize consumer data sovereignty and financial confidentiality. Direct integration with live banking Open-Banking APIs (e.g., Plaid, Yodlee) falls outside the immediate scope of this academic prototype due to institutional regulatory and licensing constraints; however, the data ingestion abstraction layer is architecturally decoupled to enable straightforward API adapter extensions in enterprise environments.
            </p>

            <h2 class="section-heading">1.5 Significance of the Project</h2>
            <p>
                SpendWise AI makes several significant contributions to applied computer science, machine learning systems engineering, and computational financial intelligence:
            </p>
            <p>
                <strong>Architectural Contribution:</strong> It demonstrates the practical viability of a multi-tier classification hierarchy that slashes generative AI inference costs by over 80% while retaining state-of-the-art semantic comprehension. This tiered approach establishes an engineering template for production AI systems where latency and operating costs are critical design constraints.
            </p>
            <p>
                <strong>Methodological Contribution:</strong> The research integrates cutting-edge 2026 RAG techniques—specifically HyDE query hallucination, sparse-dense Reciprocal Rank Fusion, and CRAG retrieval validation—into the financial domain, demonstrating how hybrid retrieval eliminates the classic vocabulary mismatch problem inherent in banking ledgers.
            </p>
            <p>
                <strong>Societal Impact:</strong> By democratizing institutional-grade financial intelligence through an accessible, private, conversational interface, SpendWise AI empowers everyday individuals to attain financial literacy, eliminate predatory subscription leaks, and achieve long-term wealth preservation.
            </p>
        </div>
        <div class="page-footer">5</div>
    </div>
    """
    pages.append(page5)

    return pages
