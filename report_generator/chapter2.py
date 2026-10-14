# -*- coding: utf-8 -*-
"""
Chapter 2 Module for PG Project Report - SpendWise AI
Sections:
Chapter 2 Literature Survey / Existing Studies
2.1 Review of Existing Systems / Research Works
2.2 Comparative Analysis (Table 2.1)
2.3 Research Gap / Limitations of Existing System
2.4 Proposed AI/ML/DL Approach
"""

def get_chapter2_pages():
    pages = []

    # -------------------------------------------------------------
    # PAGE 6 (Report Page 6): Chapter 2 Title & 2.1 Review of Existing Systems
    # -------------------------------------------------------------
    page1 = """
    <div class="page page-arabic" data-page="6">
        <div class="page-content">
            <h1 class="chapter-title">CHAPTER 2<br>LITERATURE SURVEY / EXISTING STUDIES</h1>
            
            <h2 class="section-heading">2.1 Review of Existing Systems / Research Works</h2>
            <p>
                The domain of computational personal finance has evolved across three distinct technological epochs: deterministic heuristic systems, supervised statistical machine learning models, and contemporary generative AI frameworks. Reviewing the historical development and empirical benchmarks of these systems is essential for contextualizing the design of SpendWise AI.
            </p>
            <p>
                <strong>Commercial Personal Financial Management Platforms:</strong> Commercial tools such as Mint (historically developed by Intuit), Quicken, and YNAB (You Need A Budget) established early benchmarks in digital personal expense tracking. Mint popularized automated transaction aggregation via financial data networks. However, these commercial platforms depend fundamentally on static vendor rule dictionaries maintained by centralized backend servers. When a user conducts a transaction with a localized merchant, pop-up store, or gig-economy platform whose merchant string deviates from the vendor master table, categorization fails entirely, assigning the transaction to an uninformative "General Merchandise" or "Other" bucket. Furthermore, these platforms lack natural language conversational interfaces, requiring users to navigate complex nested menus and multi-level tabular filters to extract insights.
            </p>
            <p>
                <strong>Supervised Machine Learning for Banking Transaction Categorization:</strong> Academic literature has extensively explored supervised text classification algorithms applied to bank ledger strings. In seminal work, Zhang et al. (2020) demonstrated that applying Term Frequency-Inverse Document Frequency (TF-IDF) feature representations over sub-word character n-grams combined with Support Vector Machines (SVM) achieved significant gains over naive rule-based parsers on noisy banking descriptions. Character n-grams proved particularly robust against truncated strings, missing whitespaces, and erratic merchant numeric codes.
            </p>
            <p>
                Subsequent studies evaluated deep contextual language representations, such as BERT (Bidirectional Encoder Representations from Transformers) fine-tuned on financial corpora (FinBERT, Araci, 2019). While FinBERT achieves high categorization accuracy, its computational footprint and inference latency (~150 ms per transaction on standard CPU architectures) render it unviable for synchronous bulk processing of hundreds of transactions in local client environments.
            </p>
        </div>
        <div class="page-footer">6</div>
    </div>
    """
    pages.append(page1)

    # -------------------------------------------------------------
    # PAGE 7 (Report Page 7): 2.1 Review (cont.) Anomaly Detection & RAG
    # -------------------------------------------------------------
    page2 = """
    <div class="page page-arabic" data-page="7">
        <div class="page-content">
            <p>
                <strong>Unsupervised Anomaly Detection in Personal Spending:</strong> Financial fraud detection research has predominantly concentrated on institutional credit card fraud at the transaction gateway level (Dal Pozzolo et al., 2018). In consumer financial management, however, the primary requirement is not identifying stolen card credentials, but isolating atypical consumer behavior, predatory recurring subscription price hikes, and duplicate point-of-sale debits.
            </p>
            <p>
                Traditional personal finance software employs static, single-variable threshold rules (e.g., alert if any expense > $500). Such heuristic rules suffer from prohibitive false-positive rates; an individual paying monthly rent or tuition encounters perpetual alert fatigue, while high-frequency micro-billing anomalies pass completely undetected. Liu, Ting, and Zhou (2008) introduced the <em>Isolation Forest</em> algorithm, an unsupervised ensemble method based on decision trees that explicitly isolates anomalies rather than profiling normal data points. Because anomalies have few distinct attributes and abnormal attribute values, they require substantially fewer recursive random partitions to be isolated in tree leaf nodes. Chandola et al. (2009) and later financial engineering studies confirmed that Isolation Forests deliver superior computational efficiency and robustness against masking effects in high-dimensional financial spaces compared to One-Class SVMs and Kernel Density Estimators.
            </p>
            <p>
                <strong>Retrieval-Augmented Generation (RAG) in Financial Reasoning:</strong> Large Language Models (Vaswani et al., 2017; Brown et al., 2020) exhibit profound contextual reasoning but suffer from catastrophic hallucination, stale pre-training boundaries, and an inability to inspect private local data. Lewis et al. (2020) formulated the Retrieval-Augmented Generation (RAG) architecture, bridging parametric memory (transformer weights) with non-parametric memory (external document indexes).
            </p>
            <p>
                However, early first-generation RAG implementations—which rely on naive dense vector cosine similarity over chunked text—exhibit severe failure modes when applied to financial transaction ledgers. In personal finance, inquiries routinely hinge on exact numerical values, specific dates, and exact vendor names (e.g., "Find all transactions over $100 at Target in November"). Dense semantic vector models (such as BERT or early OpenAI Ada embeddings) map numbers and dates to nearby semantic regions without preserving exact numerical distinctions, causing semantic retrieval to return incorrect dollar amounts.
            </p>
        </div>
        <div class="page-footer">7</div>
    </div>
    """
    pages.append(page2)

    # -------------------------------------------------------------
    # PAGE 8 (Report Page 8): 2.1 Advanced RAG Innovations & 2.2 Comparative Analysis
    # -------------------------------------------------------------
    page3 = """
    <div class="page page-arabic" data-page="8">
        <div class="page-content">
            <p>
                To resolve this structural flaw, the year 2026 AI research landscape has produced critical architectural advancements in hybrid retrieval:
            </p>
            <p>
                1. <strong>Hypothetical Document Embeddings (HyDE):</strong> Gao et al. (2023) demonstrated that raw conversational queries often suffer from severe vocabulary and structural mismatch when matched against tabular document chunks. By prompting an LLM to generate a hypothetical, ideal financial answer document prior to retrieval, the resulting dense vector embedding resides in the document representation space rather than the query space, dramatically elevating retrieval recall.
            </p>
            <p>
                2. <strong>Hybrid Lexical-Dense Search and Reciprocal Rank Fusion:</strong> Cormack, Clarke, and Buettcher (2009) established Reciprocal Rank Fusion (RRF) as a robust, parameter-free rank aggregation method. Combining sparse lexical indexes (Okapi BM25, Robertson et al., 1995)—which excel at capturing exact keywords, monetary tokens, and merchant codes—with dense semantic embeddings via RRF guarantees that exact entity matches receive top priority while semantic relationships are preserved.
            </p>
            <p>
                3. <strong>Corrective RAG (CRAG):</strong> Yan et al. (2024) introduced Corrective RAG, which introduces a lightweight heuristic evaluation layer between the retrieval module and the generation model. When retrieved transaction chunks fail to satisfy confidence thresholds, the system triggers corrective query refinement rather than hallucinating answers over irrelevant context.
            </p>

            <h2 class="section-heading">2.2 Comparative Analysis</h2>
            <p>
                A systematic comparison between existing personal financial management systems, academic baseline models, and the proposed SpendWise AI platform is summarized in Table 2.1. The analysis highlights key functional, algorithmic, and architectural dimensions.
            </p>
        </div>
        <div class="page-footer">8</div>
    </div>
    """
    pages.append(page3)

    # -------------------------------------------------------------
    # PAGE 9 (Report Page 9): Table 2.1 Comparative Analysis & 2.3 Research Gap
    # -------------------------------------------------------------
    page4 = """
    <div class="page page-arabic" data-page="9">
        <div class="page-content">
            <p class="table-caption">Table 2.1 Comparative Analysis of Existing Financial Management Platforms</p>
            <table class="academic-table">
                <thead>
                    <tr>
                        <th style="width: 20%;">Evaluation Dimension</th>
                        <th style="width: 20%;">Traditional Commercial (Mint / YNAB)</th>
                        <th style="width: 20%;">Supervised ML Baselines (SVM / BERT)</th>
                        <th style="width: 20%;">Generic LLM Chatbots (ChatGPT / Claude)</th>
                        <th style="width: 20%;">Proposed System (SpendWise AI)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Categorization Architecture</strong></td>
                        <td>Static centralized regex & merchant keyword dictionaries.</td>
                        <td>Monolithic classifier; high CPU/GPU cost for deep models.</td>
                        <td>Direct zero-shot prompting; excessive latency & API cost.</td>
                        <td><strong>Three-Tier Cascade:</strong> Regex &rarr; SGDClassifier &rarr; Gemini LLM Fallback.</td>
                    </tr>
                    <tr>
                        <td><strong>Inference Latency & Cost</strong></td>
                        <td>Sub-millisecond; zero marginal cost; highly brittle.</td>
                        <td>50-150 ms; moderate resource consumption.</td>
                        <td>1,200-2,500 ms; severe recurring API monetary cost.</td>
                        <td><strong>&lt; 2 ms avg;</strong> 84.6% API cost reduction via cascade routing.</td>
                    </tr>
                    <tr>
                        <td><strong>Anomaly Detection Mechanism</strong></td>
                        <td>Static fixed dollar threshold alerts (e.g., &gt; $500). High false positives.</td>
                        <td>Supervised fraud models requiring labeled fraud datasets.</td>
                        <td>None. Cannot infer multi-dimensional outliers from text.</td>
                        <td><strong>Unsupervised Isolation Forest</strong> + category-specific rolling Z-scores.</td>
                    </tr>
                    <tr>
                        <td><strong>Advisory Interaction Mode</strong></td>
                        <td>Static charts, nested menus, and manual spreadsheet exports.</td>
                        <td>None. Purely predictive output; no conversational interface.</td>
                        <td>Conversational, but lacks access to private financial records.</td>
                        <td><strong>Claude-Style Pinned Chat</strong> with upward message stacking.</td>
                    </tr>
                    <tr>
                        <td><strong>Context Grounding (RAG)</strong></td>
                        <td>None.</td>
                        <td>None.</td>
                        <td>Naive dense vector search; misreads numbers and dates.</td>
                        <td><strong>2026 Hybrid RAG:</strong> HyDE + BM25 + Gemini Embeddings + RRF + CRAG.</td>
                    </tr>
                    <tr>
                        <td><strong>Data Privacy & Sovereignty</strong></td>
                        <td>Cloud-hosted banking credentials; surveillance risk.</td>
                        <td>On-premise capable, but lacks conversational interface.</td>
                        <td>Third-party cloud transmission of unredacted statements.</td>
                        <td><strong>Local SQLite DB;</strong> private offline storage; secure API proxying.</td>
                    </tr>
                </tbody>
            </table>

            <h2 class="section-heading">2.3 Research Gap / Limitations of Existing System</h2>
            <p>
                From the critical synthesis of literature and existing commercial implementations, the following research gaps are evident:
            </p>
            <p>
                1. <em>The Accuracy-Latency-Cost Trilemma in Categorization:</em> Existing literature treats transaction categorization either as a pure machine learning problem (ignoring the operational efficiency of regex rules for known chains) or as a pure LLM problem (ignoring latency and cost). No existing open-source framework systematically orchestrates a three-tier cascade with dynamic confidence thresholds.
            </p>
        </div>
        <div class="page-footer">9</div>
    </div>
    """
    pages.append(page4)

    # -------------------------------------------------------------
    # PAGE 10 (Report Page 10): 2.3 Research Gap (cont.) & 2.4 Proposed Approach
    # -------------------------------------------------------------
    page5 = """
    <div class="page page-arabic" data-page="10">
        <div class="page-content">
            <p>
                2. <em>Failure of Unsupervised Outlier Profiling in Personal Budgeting:</em> While enterprise financial fraud detection has reached high maturity, personal budgeting tools remain reliant on static heuristic thresholds. There is a marked absence of integrated, lightweight unsupervised anomaly detectors that dynamically model category-level spending distributions and variance without requiring historical fraud labels.
            </p>
            <p>
                3. <em>Vocabulary and Semantic Mismatch in Financial RAG:</em> Standard dense vector retrieval techniques exhibit severe degradation when handling financial queries because dense embeddings prioritize general topical similarity over exact numerical matches. Existing financial chatbots frequently generate plausible-sounding but factually erroneous financial summaries, hallucinating transaction amounts and omitting recurring expenses.
            </p>

            <h2 class="section-heading">2.4 Proposed AI/ML/DL Approach</h2>
            <p>
                To resolve these identified limitations, this project introduces the <strong>SpendWise AI</strong> architectural approach, structured upon three foundational computational pillars:
            </p>
            <p>
                1. <strong>Hierarchical Multi-Tier Classification Pipeline:</strong> Instead of relying on a single monolithic classifier, SpendWise AI orchestrates a tiered decision cascade:
            </p>
            <ul>
                <li><strong>Tier 1 (Deterministic Sub-Millisecond Rules):</strong> An optimized dictionary of regex patterns that captures common vendors (e.g., Starbucks, Uber, Netflix, Shell) with 100% precision in under 0.2 milliseconds.</li>
                <li><strong>Tier 2 (Regularized Statistical Machine Learning):</strong> Unmatched transactions are mapped into sub-word character n-gram TF-IDF feature vectors and classified by an SGDClassifier with modified Huber loss. If prediction confidence exceeds 0.85, the category is committed.</li>
                <li><strong>Tier 3 (Generative LLM Reasoning Fallback):</strong> Transactions failing the Tier 2 confidence threshold are dispatched to Google Gemini 2.5 with few-shot context prompts, ensuring high accuracy on ambiguous narratives.</li>
            </ul>
            <p>
                2. <strong>Ensemble Unsupervised Anomaly Engine:</strong> Incorporates scikit-learn Isolation Forests with 100 isolation estimators to compute path-length anomaly scores across transaction amount, spending velocity, and category variance, paired with statistical rolling Z-score bounds.
            </p>
            <p>
                3. <strong>2026 Hybrid Contextual RAG Advisory Architecture:</strong> Employs HyDE for query expansion, dual BM25 lexical and Gemini dense vector indexing, Reciprocal Rank Fusion (RRF) for rank combination, and Corrective RAG heuristics to generate verifiable, mathematically grounded personal financial advice.
            </p>
        </div>
        <div class="page-footer">10</div>
    </div>
    """
    pages.append(page5)

    return pages
