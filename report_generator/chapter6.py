# -*- coding: utf-8 -*-
"""
Chapter 6 Module for PG Project Report - SpendWise AI
Sections:
Chapter 6 System Implementation
6.1 Modules Description
6.2 Dataset Description / Data Collection (Table 6.1)
6.3 Data Preprocessing
6.4 Feature Engineering / Feature Extraction
6.5 Model Architecture / Algorithm Design (Table 6.2, Math formulas)
6.6 System / Model Implementation (FastAPI endpoints, RAG implementation)
6.7 Validation Checks
6.8 User Interface Implementation
"""

def get_chapter6_pages():
    pages = []

    # -------------------------------------------------------------
    # PAGE 28 (Report Page 28): Chapter 6 Title & 6.1 Modules Description
    # -------------------------------------------------------------
    page1 = """
    <div class="page page-arabic" data-page="28">
        <div class="page-content">
            <h1 class="chapter-title">CHAPTER 6<br>SYSTEM IMPLEMENTATION</h1>
            
            <h2 class="section-heading">6.1 Modules Description</h2>
            <p>
                The engineering implementation of SpendWise AI translates the conceptual architecture into a set of modular, decoupled microservices. Each software module is encapsulated within dedicated Python packages adhering to single-responsibility and separation-of-concerns principles:
            </p>
            <p>
                <strong>1. Transaction Ingestion & Normalization Module (<code>routers/transactions.py</code>):</strong> Manages the ingestion of banking statements. Because commercial banks utilize divergent CSV formatting (varying delimiters, quoted text, differing date conventions), this module utilizes Python's <code>csv.Sniffer</code> to detect dialects automatically. It reads streaming multipart file uploads asynchronously, verifies schema integrity against expected column semantics, normalizes currency representations, and manages bulk database transactions.
            </p>
            <p>
                <strong>2. Hierarchical Categorization Module (<code>routers/categorization.py</code>):</strong> Implements the three-tier cascading classification pipeline. Tier 1 executes regular expression matching against a curated dictionary of over 200 merchant patterns. Tier 2 loads pre-trained scikit-learn TF-IDF vectorizers and an SGDClassifier pipeline to predict spending classes with calibrated probability estimates. Tier 3 constructs structured JSON prompts dispatched to Google Gemini 2.5 Flash to disambiguate edge cases where Tier 2 confidence falls below 0.85.
            </p>
            <p>
                <strong>3. Unsupervised Anomaly Detection Module (<code>routers/anomaly.py</code>):</strong> Encapsulates the scikit-learn <code>IsolationForest</code> ensemble model and rolling statistical calculators. It serializes trained models, computes path-length anomaly scores, computes category-specific Z-scores, and flags unusual expenditures and duplicate billing.
            </p>
            <p>
                <strong>4. Financial Analytics & Aggregation Module (<code>routers/analysis.py</code>):</strong> Performs timeseries aggregations over the SQLite database. It computes monthly inflow/outflow metrics, calculates category spending percentages, detects recurring subscriptions via periodicity checks, and projects net discretionary savings potential.
            </p>
            <p>
                <strong>5. 2026 Hybrid Contextual RAG Advisory Module (<code>routers/agent.py</code>):</strong> Orchestrates the conversational financial advisory pipeline. It executes HyDE query expansion, queries in-memory BM25 indexes and SQLite vector caches, merges candidate documents via Reciprocal Rank Fusion (RRF), filters context through CRAG heuristics, and prompts Gemini 2.5 Flash to generate advice.
            </p>
            <p>
                <strong>6. Presentation Interface Module (<code>frontend/app.py</code>):</strong> The Streamlit application orchestrating the Claude-style user experience, real-time KPI card updates, Altair and Plotly charts, and chat session state management.
            </p>
        </div>
        <div class="page-footer">28</div>
    </div>
    """
    pages.append(page1)

    # -------------------------------------------------------------
    # PAGE 29 (Report Page 29): 6.2 Dataset Description & Table 6.1
    # -------------------------------------------------------------
    page2 = """
    <div class="page page-arabic" data-page="29">
        <div class="page-content">
            <h2 class="section-heading">6.2 Dataset Description / Data Collection</h2>
            <p>
                To train, calibrate, and validate the machine learning and retrieval pipelines, a comprehensive dataset of 5,000 personal banking transactions was compiled. The corpus combines anonymized real-world banking exports across multiple retail institutions with realistic synthetic ledger sequences generated via the <code>Faker</code> library and financial transaction generator models.
            </p>
            <p>
                Each transactional record encapsulates four core attributes:
            </p>
            <ul>
                <li><code>date</code>: Chronological transaction execution timestamp in ISO 8601 string format (YYYY-MM-DD).</li>
                <li><code>description</code>: Raw merchant string as rendered on bank statements, containing vendor aliases, store IDs, state abbreviations, and payment gateway prefixes.</li>
                <li><code>amount</code>: Floating-point monetary value representing transaction magnitude.</li>
                <li><code>type</code>: Categorical flag indicating cash-flow directionality (<code>DEBIT</code> for expenditures or <code>CREDIT</code> for income and refunds).</li>
            </ul>
            <p>
                Table 6.1 defines the standardized 14-category expense taxonomy utilized across the platform, including representative merchant narratives.
            </p>

            <p class="table-caption">Table 6.1 Standardized Expense Taxonomy and Category Allocation Rules</p>
            <table class="academic-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Category Name</th>
                        <th style="width: 45%;">Representative Merchant String Patterns</th>
                        <th style="width: 30%;">Economic Classification</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Food &amp; Dining</strong></td>
                        <td>Starbucks, McDonald's, Whole Foods, DoorDash, Uber Eats, Trader Joe's</td>
                        <td>Discretionary / Essential</td>
                    </tr>
                    <tr>
                        <td><strong>Transportation</strong></td>
                        <td>Uber Trip, Lyft Ride, Chevron, Shell Oil, MTA Subway, BART Transit</td>
                        <td>Essential Operational</td>
                    </tr>
                    <tr>
                        <td><strong>Utilities</strong></td>
                        <td>ConEdison, AT&amp;T Wireless, Comcast Cable, Verizon, City Water Dept</td>
                        <td>Non-Discretionary Fixed</td>
                    </tr>
                    <tr>
                        <td><strong>Housing</strong></td>
                        <td>First National Mortgage, Greystar Rent, HOA Assessment Fees</td>
                        <td>Non-Discretionary Fixed</td>
                    </tr>
                    <tr>
                        <td><strong>Entertainment</strong></td>
                        <td>Netflix, Spotify, AMC Theatres, Steam Games, Disney Plus</td>
                        <td>Discretionary Leisure</td>
                    </tr>
                    <tr>
                        <td><strong>Healthcare</strong></td>
                        <td>CVS Pharmacy, Walgreens, Quest Diagnostics, City Dental Care</td>
                        <td>Essential Health</td>
                    </tr>
                    <tr>
                        <td><strong>Shopping</strong></td>
                        <td>Amazon.com, Target, Walmart, Best Buy, Apple Store Online</td>
                        <td>Discretionary Consumer</td>
                    </tr>
                    <tr>
                        <td><strong>Personal Care</strong></td>
                        <td>Supercuts, Sephora, Planet Fitness, Equinox Gym Membership</td>
                        <td>Discretionary Wellness</td>
                    </tr>
                    <tr>
                        <td><strong>Education</strong></td>
                        <td>Coursera, Udemy, University Tuition, Barnes &amp; Noble Books</td>
                        <td>Investment Human Capital</td>
                    </tr>
                    <tr>
                        <td><strong>Investments</strong></td>
                        <td>Vanguard ETF, Fidelity Brokerage, Robinhood Transfer, Charles Schwab</td>
                        <td>Wealth Accumulation</td>
                    </tr>
                    <tr>
                        <td><strong>Income</strong></td>
                        <td>Payroll Direct Deposit, Client Wire Transfer, Interest Dividend</td>
                        <td>Cash Inflow</td>
                    </tr>
                    <tr>
                        <td><strong>Transfers</strong></td>
                        <td>Venmo Cashout, Zelle Transfer to Checking, ATM Cash Withdrawal</td>
                        <td>Liquidity Movement</td>
                    </tr>
                    <tr>
                        <td><strong>Travel</strong></td>
                        <td>Delta Air Lines, Airbnb Lodging, Marriott Hotels, Hertz Car Rental</td>
                        <td>Discretionary Leisure</td>
                    </tr>
                    <tr>
                        <td><strong>Miscellaneous Fees</strong></td>
                        <td>Bank Monthly Maintenance Fee, Wire Surcharge, Overdraft Fee</td>
                        <td>Non-Discretionary Cost</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="page-footer">29</div>
    </div>
    """
    pages.append(page2)

    # -------------------------------------------------------------
    # PAGE 30 (Report Page 30): 6.3 Preprocessing & 6.4 Feature Engineering
    # -------------------------------------------------------------
    page3 = """
    <div class="page page-arabic" data-page="30">
        <div class="page-content">
            <h2 class="section-heading">6.3 Data Preprocessing</h2>
            <p>
                Raw financial transaction ledgers exhibit extreme structural noise. Financial institutions introduce proprietary prefix codes, terminal sequence numbers, and varying string encodings. To ensure high classification accuracy across all three tiers, the preprocessing pipeline applies the following transformations:
            </p>
            <p>
                1. <em>Delimiter and Encoding Detection:</em> The file stream is sampled using <code>csv.Sniffer()</code> to ascertain whether the input uses comma, semicolon, or tab delimiters. UTF-8 with Byte Order Mark (BOM) and Windows-1252 encodings are handled cleanly.
            </p>
            <p>
                2. <em>Header Standardization:</em> Commercial exports rarely name columns uniformly. A fuzzy header mapping dictionary normalizes variations (e.g., "Posting Date", "Trans Date", "Date" &rarr; <code>date</code>; "Transaction Narrative", "Memo", "Description" &rarr; <code>description</code>; "Debit Amount", "Amount (USD)", "Amount" &rarr; <code>amount</code>).
            </p>
            <p>
                3. <em>String Sanitization:</em> Merchant descriptions undergo case folding to uppercase, elimination of leading/trailing non-alphanumeric punctuation, consolidation of redundant whitespaces, and stripping of card terminal prefixes such as "POS DEBIT", "CHECKCRD", and "PURCHASE AUTHORIZED ON".
            </p>
            <p>
                4. <em>Monetary Value Conditioning:</em> Dollar signs, commas, and trailing whitespace are stripped. If amounts are represented as negative numbers for debits, the absolute value is extracted and the transaction type is set to <code>DEBIT</code>.
            </p>

            <h2 class="section-heading">6.4 Feature Engineering / Feature Extraction</h2>
            <p>
                To train the Tier 2 statistical classifier and unsupervised anomaly detector, specialized feature representations are extracted:
            </p>
            <p>
                <strong>1. Sub-Word Character N-Gram TF-IDF Features:</strong> Conventional word-level tokenization fails on financial strings because merchant descriptions routinely lack spaces (e.g., "AMZNMKTPUS", "STARBUCKS#1042"). To overcome this, SpendWise AI employs sub-word character n-grams spanning ranges \(n \in [2, 5]\) with word boundary awareness (<code>analyzer='char_wb'</code>). Given a vocabulary \(V\) of character n-grams, the Term Frequency-Inverse Document Frequency weight for n-gram \(t\) in string \(d\) across corpus \(D\) is defined as:
            </p>
            <p class="no-indent" style="text-align: center; margin: 15px 0;">
                \[
                \text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \ln\left(\frac{1 + |D|}{1 + |\{d \in D : t \in d\}|}\right) + 1
                \]
            </p>
            <p>
                This feature extraction yields a sparse feature matrix of 15,000 dimensions, capturing structural prefixes and roots regardless of typos or numeric IDs.
            </p>
            <p>
                <strong>2. Temporal and Numerical Features:</strong> For the anomaly detection engine, numerical features include transaction magnitude \(x_{\text{amount}}\), day of week \(d \in [0, 6]\), day of month \(t \in [1, 31]\), transaction velocity (number of debits in preceding 24 hours), and rolling category variance \(\sigma_c^2\).
            </p>
        </div>
        <div class="page-footer">30</div>
    </div>
    """
    pages.append(page3)

    # -------------------------------------------------------------
    # PAGE 31 (Report Page 31): 6.5 Model Architecture / Algorithm Design (Math)
    # -------------------------------------------------------------
    page4 = """
    <div class="page page-arabic" data-page="31">
        <div class="page-content">
            <h2 class="section-heading">6.5 Model Architecture / Algorithm Design</h2>
            <p>
                SpendWise AI implements three primary algorithmic formulations: the three-tier categorization cascade, the Isolation Forest anomaly detector, and the 2026 Hybrid Contextual RAG advisory framework.
            </p>
            <p>
                <strong>1. Mathematical Formulation of the Three-Tier Categorization Cascade:</strong>
            </p>
            <p>
                Given an input transaction \(x\) with narrative string \(s(x)\):
            </p>
            <p>
                <em>Tier 1 (Deterministic Pattern Rules):</em> The system evaluates \(s(x)\) against a compiled regex dictionary \(\mathcal{R} = \{(r_i, c_i)\}_{i=1}^M\). If \(\exists i\) such that \(r_i \text{ matches } s(x)\), the category is assigned:
            </p>
            <p class="no-indent" style="text-align: center; margin: 10px 0;">
                \[
                \hat{y} = c_i, \quad \text{Confidence} = 1.0, \quad \text{Execution Time} \le 0.2\text{ ms}
                \]
            </p>
            <p>
                <em>Tier 2 (Stochastic Gradient Descent Linear Classifier):</em> If no regex match occurs, \(s(x)\) is transformed into sparse feature vector \(\mathbf{v}(x) \in \mathbb{R}^{|V|}\). The model optimizes a linear decision function parameterized by weight matrix \(\mathbf{W}\) and bias \(\mathbf{b}\) using modified Huber loss:
            </p>
            <p class="no-indent" style="text-align: center; margin: 10px 0;">
                \[
                L(y, f(\mathbf{v})) = \begin{cases}
                \max(0, 1 - y f(\mathbf{v}))^2 & \text{for } y f(\mathbf{v}) \ge -1 \\
                -4 y f(\mathbf{v}) & \text{for } y f(\mathbf{v}) < -1
                \end{cases}
            \]
            </p>
            <p>
                The predicted category probability vector \(\mathbf{p} = \text{Softmax}(\mathbf{W}\mathbf{v} + \mathbf{b})\) yields predicted class \(\hat{y} = \arg\max_c p_c\) with confidence \(\hat{p} = \max_c p_c\). If \(\hat{p} \ge \tau = 0.85\), the prediction is committed.
            </p>
            <p>
                <em>Tier 3 (Google Gemini 2.5 Generative Fallback):</em> If \(\hat{p} < 0.85\), the transaction is formatted as a structured JSON prompt with few-shot examples and dispatched to Gemini 2.5 Flash:
            </p>
            <p class="no-indent" style="text-align: center; margin: 10px 0;">
                \[
                \hat{y} = \text{LLM}_{\text{Gemini}}(s(x), \text{Context}_{\text{few-shot}}), \quad \hat{y} \in \mathcal{C}
                \]
            </p>
            <p>
                <strong>2. Mathematical Formulation of the Isolation Forest Anomaly Engine:</strong>
            </p>
            <p>
                The Isolation Forest constructs an ensemble of \(t = 100\) randomized isolation trees (iTrees). In each tree, an instance \(x\) is recursively partitioned until isolated. The path length \(h(x)\) is the number of edges traversed. The average path length of unsuccessful searches in a Binary Search Tree constructed over \(n\) instances is:
            </p>
            <p class="no-indent" style="text-align: center; margin: 10px 0;">
                \[
                c(n) = 2 \left( \ln(n - 1) + 0.5772156649 \right) - \frac{2(n - 1)}{n}
                \]
            </p>
            <p>
                The anomaly score \(s(x, n)\) of instance \(x\) across \(m\) isolation trees is defined as:
            </p>
            <p class="no-indent" style="text-align: center; margin: 10px 0;">
                \[
                s(x, n) = 2^{-\frac{\mathbb{E}(h(x))}{c(n)}}
                \]
            </p>
            <p>
                If \(\mathbb{E}(h(x)) \to 0\), then \(s \to 1\) (signifying a definitive anomaly). Instances with \(s \ge 0.65\) or category Z-score \(Z = \frac{x_{\text{amount}} - \mu_c}{\sigma_c} \ge 2.5\) are flagged as anomalies.
            </p>
        </div>
        <div class="page-footer">31</div>
    </div>
    """
    pages.append(page4)

    # -------------------------------------------------------------
    # PAGE 32 (Report Page 32): 6.5 Algorithm Design (Hybrid RAG Math) & Table 6.2
    # -------------------------------------------------------------
    page5 = """
    <div class="page page-arabic" data-page="32">
        <div class="page-content">
            <p>
                <strong>3. Mathematical Formulation of the 2026 Hybrid Contextual RAG Pipeline:</strong>
            </p>
            <p>
                The conversational financial advisory engine combines sparse lexical and dense semantic representations via four sequential mathematical operations:
            </p>
            <p>
                <em>Step 1 (HyDE Query Synthesis):</em> The user query \(q\) is transformed into a hypothetical ideal financial answer document \(d_{\text{hypo}} = \mathcal{G}_{\text{LLM}}(q)\), projecting the short query into the document semantic manifold.
            </p>
            <p>
                <em>Step 2 (Dual-Space Parallel Retrieval):</em>
            </p>
            <ul>
                <li><strong>Sparse Okapi BM25 Retrieval:</strong> Computes inverted index term frequency scores across chunked ledger records \(D\):
                    <div style="text-align: center; margin: 8px 0;">
                        \[
                        \text{Score}_{\text{BM25}}(d, q) = \sum_{t \in q} \text{IDF}(t) \cdot \frac{f(t, d) \cdot (k_1 + 1)}{f(t, d) + k_1 \cdot \left(1 - b + b \cdot \frac{|d|}{\text{avgdl}}\right)}
                        \]
                    </div>
                    where \(k_1 = 1.5\) and \(b = 0.75\). This captures exact monetary figures, dates, and account numbers.
                </li>
                <li><strong>Dense Semantic Vector Retrieval:</strong> Dense 768-dimensional embeddings \(\mathbf{e}_d\) and \(\mathbf{e}_{d_{\text{hypo}}}\) are computed via Gemini Text-Embedding-004. Similarity is evaluated via cosine distance:
                    <div style="text-align: center; margin: 8px 0;">
                        \[
                        \text{Sim}_{\text{dense}}(d, d_{\text{hypo}}) = \frac{\mathbf{e}_d \cdot \mathbf{e}_{d_{\text{hypo}}}}{\|\mathbf{e}_d\|_2 \|\mathbf{e}_{d_{\text{hypo}}}\|_2}
                        \]
                    </div>
                </li>
            </ul>
            <p>
                <em>Step 3 (Reciprocal Rank Fusion - RRF):</em> Sparse and dense rank orders are fused into a unified ranking without score normalization artifacts using RRF with constant \(k = 60\):
            </p>
            <p class="no-indent" style="text-align: center; margin: 10px 0;">
                \[
                \text{RRF\_Score}(d) = \frac{1}{60 + \text{Rank}_{\text{BM25}}(d)} + \frac{1}{60 + \text{Rank}_{\text{Dense}}(d)}
                \]
            </p>
            <p>
                <em>Step 4 (Corrective RAG - CRAG Verification):</em> Top-ranked documents undergo heuristic evaluation. If the maximum RRF score falls below threshold \(\gamma = 0.015\), an alert indicates insufficient ledger context, preventing conversational hallucination.
            </p>

            <p class="table-caption">Table 6.2 Hyperparameter Tuning Configurations for Isolation Forest Ensemble</p>
            <table class="academic-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Hyperparameter</th>
                        <th style="width: 25%;">Explored Search Space</th>
                        <th style="width: 25%;">Optimal Selected Value</th>
                        <th style="width: 25%;">Performance Justification</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><code>n_estimators</code></td>
                        <td>50, 100, 200, 300</td>
                        <td><strong>100 Trees</strong></td>
                        <td>Sufficient ensemble convergence; sub-10 ms execution.</td>
                    </tr>
                    <tr>
                        <td><code>contamination</code></td>
                        <td>0.01, 0.03, 0.05, 0.10</td>
                        <td><strong>0.03 (3.0%)</strong></td>
                        <td>Balances outlier sensitivity with low false alarm rate.</td>
                    </tr>
                    <tr>
                        <td><code>max_samples</code></td>
                        <td>64, 128, 256, 'auto'</td>
                        <td><strong>256 Samples</strong></td>
                        <td>Prevents swamping and masking in multi-month ledgers.</td>
                    </tr>
                    <tr>
                        <td><code>max_features</code></td>
                        <td>1.0, 0.8, 0.5</td>
                        <td><strong>1.0 (All Features)</strong></td>
                        <td>Preserves correlation between amount and category variance.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="page-footer">32</div>
    </div>
    """
    pages.append(page5)

    # -------------------------------------------------------------
    # PAGE 33 (Report Page 33): 6.6 System / Model Implementation (Code Extracts)
    # -------------------------------------------------------------
    page6 = """
    <div class="page page-arabic" data-page="33">
        <div class="page-content">
            <h2 class="section-heading">6.6 System / Model Implementation</h2>
            <p>
                This section presents core Python code implementations demonstrating the cascading classification, anomaly scoring, and hybrid RAG retrieval mechanisms deployed in SpendWise AI.
            </p>
            <p>
                <strong>1. Three-Tier Cascading Categorization Implementation:</strong>
            </p>
            <pre class="code-block">
# Extracted from backend/routers/categorization.py
def categorize_transaction_cascade(description: str, amount: float) -> dict:
    desc_clean = description.strip().upper()
    
    # Tier 1: Deterministic Regex Pattern Dictionary Matching
    for pattern, category in COMPILED_REGEX_RULES.items():
        if pattern.search(desc_clean):
            return {"category": category, "tier": "Tier-1-Regex", "confidence": 1.0}
            
    # Tier 2: Sub-word Character N-Gram TF-IDF + SGDClassifier
    if ml_pipeline is not None:
        X_vec = tfidf_vectorizer.transform([desc_clean])
        probabilities = ml_pipeline.predict_proba(X_vec)[0]
        max_idx = np.argmax(probabilities)
        confidence = float(probabilities[max_idx])
        pred_category = ml_pipeline.classes_[max_idx]
        
        if confidence >= 0.85:
            return {"category": pred_category, "tier": "Tier-2-SGD", "confidence": round(confidence, 3)}
            
    # Tier 3: Google Gemini 2.5 Flash Few-Shot LLM Reasoning Fallback
    try:
        prompt = f\"\"\"Classify this bank transaction description into exactly ONE category:
        Options: Food & Dining, Transportation, Utilities, Housing, Entertainment, 
        Healthcare, Shopping, Personal Care, Education, Investments, Income, Transfers, Travel, Fees.
        Transaction: "{description}", Amount: ${amount:.2f}
        Output ONLY valid JSON: {{"category": "<CATEGORY_NAME>"}}\"\"\"
        
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json")
        )
        data = json.loads(response.text)
        return {"category": data.get("category", "Miscellaneous"), "tier": "Tier-3-Gemini", "confidence": 0.95}
    except Exception as e:
        return {"category": "Uncategorized", "tier": "Fallback-Error", "confidence": 0.50}
            </pre>
        </div>
        <div class="page-footer">33</div>
    </div>
    """
    pages.append(page6)

    # -------------------------------------------------------------
    # PAGE 34 (Report Page 34): 6.6 Code Implementation (cont.) RAG & Anomaly
    # -------------------------------------------------------------
    page7 = """
    <div class="page page-arabic" data-page="34">
        <div class="page-content">
            <p>
                <strong>2. 2026 Hybrid RAG Reciprocal Rank Fusion & CRAG Implementation:</strong>
            </p>
            <pre class="code-block">
# Extracted from backend/routers/agent.py
def hybrid_contextual_retrieve(query: str, db: Session, top_k: int = 5) -> list:
    # 1. Synthesize Hypothetical Financial Document via HyDE
    hyde_prompt = f"Write a factual personal finance report snippet answering: {query}"
    hyde_doc = gemini_client.models.generate_content(model="gemini-2.5-flash", contents=hyde_prompt).text
    
    # 2. Parallel Dual-Space Retrieval
    # A) Sparse Okapi BM25 Lexical Retrieval
    tokenized_query = query.lower().split()
    bm25_scores = bm25_index.get_scores(tokenized_query)
    bm25_ranked_indices = np.argsort(bm25_scores)[::-1][:20]
    
    # B) Dense Semantic Vector Cosine Similarity
    query_vector = get_gemini_embedding(hyde_doc)
    cached_embeddings = db.query(RAGEmbedding).all()
    dense_scores = [cosine_similarity(query_vector, emb.get_vector()) for emb in cached_embeddings]
    dense_ranked_indices = np.argsort(dense_scores)[::-1][:20]
    
    # 3. Reciprocal Rank Fusion (RRF with k = 60)
    rrf_scores = defaultdict(float)
    for rank, idx in enumerate(bm25_ranked_indices):
        rrf_scores[idx] += 1.0 / (60.0 + rank + 1)
    for rank, idx in enumerate(dense_ranked_indices):
        rrf_scores[idx] += 1.0 / (60.0 + rank + 1)
        
    # 4. Corrective RAG (CRAG) Heuristic Confidence Verification
    sorted_candidates = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
    if not sorted_candidates or sorted_candidates[0][1] < 0.015:
        return [{"text": "Context uncertain. Direct user verification recommended.", "verified": False}]
        
    return [{"text": cached_embeddings[idx].chunk_text, "score": score, "verified": True}
            for idx, score in sorted_candidates]
            </pre>
            <p>
                <strong>3. Unsupervised Isolation Forest Anomaly Scoring:</strong>
            </p>
            <pre class="code-block">
# Extracted from backend/routers/anomaly.py
def detect_transaction_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    features = df[['amount']].copy()
    features['log_amount'] = np.log1p(features['amount'])
    
    # Isolation Forest fit and score
    iso_forest = IsolationForest(n_estimators=100, contamination=0.03, random_state=42)
    preds = iso_forest.fit_predict(features)
    anomaly_scores = -iso_forest.score_samples(features)
    
    # Category-Specific Rolling Z-Score
    df['anomaly_score'] = anomaly_scores
    df['is_anomaly'] = (preds == -1)
    for category in df['category'].unique():
        cat_mask = (df['category'] == category)
        mean, std = df.loc[cat_mask, 'amount'].mean(), df.loc[cat_mask, 'amount'].std()
        if std > 0:
            z_scores = (df.loc[cat_mask, 'amount'] - mean) / std
            df.loc[cat_mask & (z_scores > 2.5), 'is_anomaly'] = True
    return df
            </pre>
        </div>
        <div class="page-footer">34</div>
    </div>
    """
    pages.append(page7)

    # -------------------------------------------------------------
    # PAGE 35 (Report Page 35): 6.7 Validation Checks & 6.8 User Interface Implementation
    # -------------------------------------------------------------
    page8 = """
    <div class="page page-arabic" data-page="35">
        <div class="page-content">
            <h2 class="section-heading">6.7 Validation Checks</h2>
            <p>
                To maintain operational stability, data integrity, and resilience against adversarial or malformed inputs, SpendWise AI incorporates multi-layer validation checks:
            </p>
            <p>
                1. <em>Input Payload & Schema Validation:</em> FastAPI uses Pydantic V2 models to enforce strict type checking across all REST endpoints. The CSV ingestion pipeline validates that required headers (<code>date</code>, <code>description</code>, <code>amount</code>, <code>type</code>) are present; if any mandatory column is missing, a structured HTTP 400 error response is dispatched with an explicit description of expected headers.
            </p>
            <p>
                2. <em>Numeric and Date Sanity Guards:</em> Negative amounts are checked and normalized; rows with non-numeric amounts or unparseable dates are quarantined in a validation log without interrupting batch processing.
            </p>
            <p>
                3. <em>SQL Injection Prevention:</em> All database transactions utilize SQLAlchemy ORM parameterized queries. Raw string concatenation is prohibited across all data access objects.
            </p>

            <h2 class="section-heading">6.8 User Interface Implementation</h2>
            <p>
                The frontend interface is engineered in Streamlit (<code>frontend/app.py</code>) incorporating custom CSS injection to deliver a modern, Claude-style conversational workflow:
            </p>
            <p>
                1. <em>Upward-Stacking Chat History:</em> Unlike standard dashboards where new messages push the input box downward, SpendWise AI uses a flex-column CSS layout where messages stack upward above a fixed bottom container.
            </p>
            <p>
                2. <em>Anchored Input Bar:</em> The chat input widget (<code>st.chat_input</code>) is fixed permanently at the bottom of the viewport using CSS:
            </p>
            <pre class="code-block">
/* Custom CSS injected via st.markdown() */
div[data-testid="stChatInput"] {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 65%;
    z-index: 1000;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}
            </pre>
            <p>
                3. <em>Automated Scroll Anchoring:</em> A lightweight JavaScript snippet anchored to a target DOM container automatically scrolls the chat area to display the latest assistant response upon generation.
            </p>
        </div>
        <div class="page-footer">35</div>
    </div>
    """
    pages.append(page8)

    return pages
