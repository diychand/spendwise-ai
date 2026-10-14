# -*- coding: utf-8 -*-
"""
Chapter 4 Module for PG Project Report - SpendWise AI
Sections:
Chapter 4 System Analysis
4.1 Requirement Specification (Table 4.1, Table 4.2)
4.2 Characteristics of Existing System
4.3 Proposed System / Proposed Approach
4.4 Feasibility Study (Technical, Economic, Operational, Schedule)
4.5 Software Requirement Specification (SRS)
"""

def get_chapter4_pages():
    pages = []

    # -------------------------------------------------------------
    # PAGE 15 (Report Page 15): Chapter 4 Title & 4.1 Requirement Specification
    # -------------------------------------------------------------
    page1 = """
    <div class="page page-arabic" data-page="15">
        <div class="page-content">
            <h1 class="chapter-title">CHAPTER 4<br>SYSTEM ANALYSIS</h1>
            
            <h2 class="section-heading">4.1 Requirement Specification</h2>
            <p>
                System analysis constitutes the systematic investigation of computational needs, operational boundaries, and functional dependencies governing SpendWise AI. The objective is to translate user requirements, algorithmic models, and domain constraints into explicit functional and non-functional specifications.
            </p>
            <p>
                <strong>Functional Requirements (FR):</strong> Functional requirements define the core operational behaviors, transactional endpoints, and algorithmic transformations that the software must execute. Table 4.1 outlines the functional requirements matrix along with operational priority.
            </p>

            <p class="table-caption">Table 4.1 Functional Requirements Matrix and Operational Priority</p>
            <table class="academic-table">
                <thead>
                    <tr>
                        <th style="width: 15%;">Req. ID</th>
                        <th style="width: 30%;">Functional Requirement</th>
                        <th style="width: 40%;">Description & Operational Behavior</th>
                        <th style="width: 15%;">Priority</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>FR-01</strong></td>
                        <td>Transaction Ingestion & Parsing</td>
                        <td>Accept CSV ledger files via multipart upload; automatically detect delimiters, validate mandatory columns (date, description, amount, type), and parse rows into typed records.</td>
                        <td>Mandatory</td>
                    </tr>
                    <tr>
                        <td><strong>FR-02</strong></td>
                        <td>Multi-Tier Categorization</td>
                        <td>Execute a three-tier classification hierarchy (Regex &rarr; SGDClassifier TF-IDF &rarr; Gemini LLM) to assign one of 14 standardized expense categories to each transaction.</td>
                        <td>Mandatory</td>
                    </tr>
                    <tr>
                        <td><strong>FR-03</strong></td>
                        <td>Anomaly Detection & Scoring</td>
                        <td>Evaluate each transaction through an Isolation Forest ensemble and rolling category Z-scores; flag statistical outliers with confidence scores and anomaly flags.</td>
                        <td>High</td>
                    </tr>
                    <tr>
                        <td><strong>FR-04</strong></td>
                        <td>Financial Analytics & Breakdown</td>
                        <td>Aggregate transactions by category, calculate net discretionary cash flow, identify recurring subscriptions, and generate monthly spending velocity summaries.</td>
                        <td>High</td>
                    </tr>
                    <tr>
                        <td><strong>FR-05</strong></td>
                        <td>Contextual RAG Indexing</td>
                        <td>Generate dual-space document indexes: sparse lexical BM25 index and dense semantic vector embeddings via Gemini Text-Embedding-004; cache vectors in SQLite.</td>
                        <td>Mandatory</td>
                    </tr>
                    <tr>
                        <td><strong>FR-06</strong></td>
                        <td>Hybrid Query Retrieval</td>
                        <td>Expand user queries via HyDE; perform parallel sparse and dense retrieval; fuse candidate rankings using Reciprocal Rank Fusion (RRF); filter via CRAG heuristics.</td>
                        <td>Mandatory</td>
                    </tr>
                    <tr>
                        <td><strong>FR-07</strong></td>
                        <td>Conversational Advisory Agent</td>
                        <td>Synthesize natural language financial guidance grounded strictly in retrieved transaction context; prevent arithmetic and factual hallucinations.</td>
                        <td>High</td>
                    </tr>
                    <tr>
                        <td><strong>FR-08</strong></td>
                        <td>Claude-Style User Interface</td>
                        <td>Render upward-stacking chat messages above a permanently anchored bottom input bar with automated scroll anchoring, metric KPI cards, and charts.</td>
                        <td>High</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="page-footer">15</div>
    </div>
    """
    pages.append(page1)

    # -------------------------------------------------------------
    # PAGE 16 (Report Page 16): Non-Functional Requirements & Table 4.2
    # -------------------------------------------------------------
    page2 = """
    <div class="page page-arabic" data-page="16">
        <div class="page-content">
            <p>
                <strong>Non-Functional Requirements (NFR):</strong> Non-functional requirements establish the quality attributes, performance envelopes, security protocols, and operational constraints under which the platform operates. Table 4.2 details these engineering constraints.
            </p>

            <p class="table-caption">Table 4.2 Non-Functional Engineering Requirements</p>
            <table class="academic-table">
                <thead>
                    <tr>
                        <th style="width: 20%;">Category</th>
                        <th style="width: 25%;">Requirement Target</th>
                        <th style="width: 55%;">Technical Specification & Verification Method</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Performance & Latency</strong></td>
                        <td>Sub-second Transaction Processing</td>
                        <td>Tier 1 rules execute in &lt; 0.2 ms; Tier 2 ML executes in &lt; 1.5 ms; total ingestion of 500 transactions completes in &lt; 3.0 seconds under normal CPU load.</td>
                    </tr>
                    <tr>
                        <td><strong>Conversational Latency</strong></td>
                        <td>Interactive Query Response</td>
                        <td>Hybrid retrieval (HyDE + BM25 + Vector Search + RRF) completes in &lt; 800 ms; LLM advisory synthesis completes in &lt; 2.5 seconds total end-to-end.</td>
                    </tr>
                    <tr>
                        <td><strong>Scalability</strong></td>
                        <td>Ledger Capacity</td>
                        <td>System supports databases of up to 100,000 transaction records without degrading query retrieval or tabular dashboard aggregation performance.</td>
                    </tr>
                    <tr>
                        <td><strong>Data Privacy & Security</strong></td>
                        <td>Local Data Sovereignty</td>
                        <td>All raw transaction ledgers reside locally in an encrypted or access-controlled SQLite database. No raw personally identifiable information is sent to third parties.</td>
                    </tr>
                    <tr>
                        <td><strong>Reliability & Fault Tolerance</strong></td>
                        <td>Graceful Degradation</td>
                        <td>If external Gemini API endpoints encounter rate limits or network dropouts, the system gracefully falls back to local Tier 2 ML predictions without crashing.</td>
                    </tr>
                    <tr>
                        <td><strong>Maintainability & Modularity</strong></td>
                        <td>Decoupled Architecture</td>
                        <td>FastAPI REST backend and Streamlit frontend operate as independent processes communicating over standard HTTP/JSON contracts.</td>
                    </tr>
                </tbody>
            </table>

            <h2 class="section-heading">4.2 Characteristics of Existing System</h2>
            <p>
                An exhaustive examination of existing personal financial management tools reveals multiple systemic deficiencies:
            </p>
            <p>
                1. <em>Monolithic and Static Categorization Rules:</em> Most commercial systems rely on static merchant lookup tables. When a vendor updates its payment terminal string or a user shops at an unindexed merchant, transactions default to "Miscellaneous", requiring tedious manual reclassification.
            </p>
            <p>
                2. <em>High Latency and Prohibitive Cost of Pure LLM Approaches:</em> Emerging AI prototypes attempt to pass every raw transaction line directly into cloud-hosted LLM prompts. For an active user generating 200 monthly transactions, direct LLM parsing consumes thousands of tokens and takes over 30 seconds, generating high recurring API subscription costs.
            </p>
        </div>
        <div class="page-footer">16</div>
    </div>
    """
    pages.append(page2)

    # -------------------------------------------------------------
    # PAGE 17 (Report Page 17): 4.2 Characteristics (cont.) & 4.3 Proposed System
    # -------------------------------------------------------------
    page3 = """
    <div class="page page-arabic" data-page="17">
        <div class="page-content">
            <p>
                3. <em>Absence of Multi-Dimensional Anomaly Detection:</em> Existing systems either lack anomaly detection entirely or implement crude static thresholds (e.g., flagging any charge over $500). They cannot differentiate between an anticipated, routine rent payment and a sudden 300% spike in discretionary dining out.
            </p>
            <p>
                4. <em>Arithmetic Hallucination in Generic Financial Chatbots:</em> When users query general-purpose AI models about their financial records, the models frequently hallucinate totals, miscalculate savings rates, and fail to track recurring subscriptions accurately due to the absence of factual ledger grounding.
            </p>

            <h2 class="section-heading">4.3 Proposed System / Proposed Approach</h2>
            <p>
                SpendWise AI eliminates the aforementioned deficiencies by introducing a unified, modular financial intelligence platform engineered around the following core innovations:
            </p>
            <p>
                <strong>1. Three-Tier Categorization Cascade:</strong> By sequencing deterministic regex rules (Tier 1), regularized SGDClassifier statistical machine learning (Tier 2), and Google Gemini few-shot LLM reasoning (Tier 3), SpendWise AI captures over 90% of transactions at zero API cost in sub-millisecond timeframes, reserving foundation models strictly for complex semantic edge cases.
            </p>
            <p>
                <strong>2. Dual-Engine Statistical & Unsupervised Anomaly Detection:</strong> The platform combines Isolation Forest tree ensembles—which isolate spatial outliers across multi-dimensional transaction vectors—with category-specific rolling Z-scores. This enables the system to flag genuine anomalies, duplicate charges, and runaway subscription price hikes without requiring labeled fraud training data.
            </p>
            <p>
                <strong>3. 2026 Hybrid Contextual RAG Advisory Framework:</strong> SpendWise AI integrates Hypothetical Document Embeddings (HyDE) to bridge query syntax with ledger representations, dual BM25 lexical and Gemini dense vector retrieval to capture both exact numbers and semantic concepts, Reciprocal Rank Fusion (RRF) for optimal rank aggregation, and Corrective RAG (CRAG) heuristics to ensure conversational financial advice is 100% grounded in verified ledger facts.
            </p>
            <p>
                <strong>4. Claude-Style Conversational Interface:</strong> The user interface is engineered in Streamlit with custom CSS to provide an ergonomic chat experience where messages stack upward above a fixed bottom input bar, maintaining visibility of the latest responses without requiring manual scrolling.
            </p>
        </div>
        <div class="page-footer">17</div>
    </div>
    """
    pages.append(page3)

    # -------------------------------------------------------------
    # PAGE 18 (Report Page 18): 4.4 Feasibility Study
    # -------------------------------------------------------------
    page4 = """
    <div class="page page-arabic" data-page="18">
        <div class="page-content">
            <h2 class="section-heading">4.4 Feasibility Study</h2>
            <p>
                Prior to system implementation, an in-depth feasibility study was conducted across four primary dimensions to ensure the project's viability, economic sustainability, and operational efficacy:
            </p>
            <p>
                <strong>1. Technical Feasibility:</strong> The technical feasibility of SpendWise AI was established by verifying the availability, maturity, and compatibility of the chosen technology stack. The backend is built in Python 3.14 utilizing FastAPI, a production-grade framework with asynchronous I/O capabilities. Scikit-learn provides mature, CPU-optimized implementations of TF-IDF, SGDClassifier, and Isolation Forests, allowing high-throughput machine learning inference on standard consumer hardware. The Google GenAI SDK provides reliable, low-latency access to Gemini 2.5 Flash and Text-Embedding-004 models. SQLite provides an embedded, zero-configuration database that easily handles hundreds of thousands of records. All required libraries are open-source and actively maintained.
            </p>
            <p>
                <strong>2. Economic Feasibility:</strong> A primary design goal of SpendWise AI was minimizing operational expenditure. Commercial personal finance platforms often impose monthly subscription fees ($10–$25/month). Emerging AI financial tools incur heavy LLM token costs by processing all data through proprietary models. In contrast, SpendWise AI's three-tier cascading architecture resolves ~72% of transactions via Tier 1 regex rules and ~18% via Tier 2 local ML models, routing only ~10% to the Gemini API. This reduces cloud API token consumption by over 84%, resulting in negligible marginal operating costs (fractions of a cent per upload). Furthermore, all underlying software frameworks are open-source, eliminating licensing fees.
            </p>
            <p>
                <strong>3. Operational Feasibility:</strong> Operational feasibility assesses how readily end-users can operate the system in real-world scenarios. SpendWise AI features an intuitive web interface built in Streamlit. Users need only drag and drop their bank-exported CSV ledger files; the system automatically detects column variations and normalizes headers without requiring technical manual mapping. The conversational interface operates identically to popular AI chat assistants (Claude/ChatGPT), allowing users to ask natural questions (e.g., "Where did I spend the most this month?") without learning structured query syntax.
            </p>
            <p>
                <strong>4. Schedule and Behavioral Feasibility:</strong> The project schedule was partitioned into structured developmental milestones: backend architecture, ML pipeline engineering, RAG retrieval design, frontend implementation, and rigorous test case validation. The project was completed comfortably within the allotted academic timeline.
            </p>
        </div>
        <div class="page-footer">18</div>
    </div>
    """
    pages.append(page4)

    # -------------------------------------------------------------
    # PAGE 19 (Report Page 19): 4.5 Software Requirement Specification
    # -------------------------------------------------------------
    page5 = """
    <div class="page page-arabic" data-page="19">
        <div class="page-content">
            <h2 class="section-heading">4.5 Software Requirement Specification</h2>
            <p>
                The Software Requirement Specification (SRS) for SpendWise AI adheres to IEEE 830 standards for software engineering requirements documentation:
            </p>
            <p>
                <strong>1. User Classes and Characteristics:</strong>
            </p>
            <ul>
                <li><em>Individual Consumers:</em> Everyday users seeking automated expense categorization, visual spending breakdowns, and conversational budgeting advice without technical overhead.</li>
                <li><em>Financial Analysts & Power Users:</em> Users requiring granular category audits, anomaly detection inspection, CSV data exports, and multi-turn financial scenario modeling.</li>
                <li><em>System Administrators:</em> Technical users responsible for managing local SQLite database backups, configuring API keys, and monitoring backend microservice logs.</li>
            </ul>
            <p>
                <strong>2. External Interface Requirements:</strong>
            </p>
            <ul>
                <li><em>User Interface (UI):</em> Responsive web application with sidebar navigation, metric cards, interactive charts, and a Claude-style pinned conversational chat interface.</li>
                <li><em>Software Interfaces (API):</em> RESTful HTTP/JSON endpoints exposed by FastAPI on port 8000, adhering to OpenAPI 3.0 standards.</li>
                <li><em>Communications Interface:</em> Asynchronous HTTPS client connections to Google Gemini API servers utilizing TLS 1.3 encryption.</li>
            </ul>
            <p>
                <strong>3. Operating Environment:</strong> Cross-platform support across Microsoft Windows 10/11, macOS Sonoma/Sequoia, and Linux distributions (Ubuntu 22.04 LTS). Standard web browser compatibility with Google Chrome (v110+), Mozilla Firefox (v115+), and Apple Safari (v16+).
            </p>
            <p>
                <strong>4. System Constraints and Dependencies:</strong> The platform depends on a valid Google Gemini API key configured in a local <code>.env</code> file. Database storage is managed via SQLite with automatic local file locking and write-ahead logging (WAL) for concurrency protection.
            </p>
        </div>
        <div class="page-footer">19</div>
    </div>
    """
    pages.append(page5)

    return pages
