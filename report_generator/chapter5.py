# -*- coding: utf-8 -*-
"""
Chapter 5 Module for PG Project Report - SpendWise AI
Sections:
Chapter 5 System Design
5.1 System Architecture (Fig. 5.1 SVG)
5.2 Context Diagram (Fig. 5.2 SVG)
5.3 Use Case Diagram (Fig. 5.3 SVG)
5.4 Activity Diagram (Fig. 5.4 SVG)
5.5 ER Diagram (Fig. 5.5 SVG)
5.6 Database Design (Fig. 5.6 SVG & Tables 5.1, 5.2)
5.7 User Interface Design (Fig. 5.7 SVG UI Wireframe)
"""

from diagrams.generate_diagrams import (
    get_system_architecture_svg,
    get_context_diagram_svg,
    get_use_case_diagram_svg,
    get_activity_diagram_svg,
    get_er_diagram_svg,
    get_database_design_svg,
    get_user_interface_design_svg
)

def get_chapter5_pages():
    pages = []

    # -------------------------------------------------------------
    # PAGE 20 (Report Page 20): Chapter 5 Title & 5.1 System Architecture (Text)
    # -------------------------------------------------------------
    page1 = """
    <div class="page page-arabic" data-page="20">
        <div class="page-content">
            <h1 class="chapter-title">CHAPTER 5<br>SYSTEM DESIGN</h1>
            
            <h2 class="section-heading">5.1 System Architecture</h2>
            <p>
                The architectural design of SpendWise AI is structured as a decoupled, multi-tiered microservices ecosystem engineered to achieve high computational throughput, low inference latency, and robust semantic reasoning. The system reconciles the competing demands of local privacy, real-time response times, and sophisticated generative intelligence by partitioning workloads across specialized processing subsystems.
            </p>
            <p>
                The overall workflow consists of five interconnected subsystems:
            </p>
            <p>
                <strong>1. Presentation Tier (Streamlit Interface):</strong> Implemented as a responsive web dashboard incorporating a custom CSS-engineered Claude-style conversational interaction paradigm. The interface provides real-time transaction ingestion feedback, interactive spending visualizers, metric KPI cards, and an upward-stacking conversational chat history anchored above a fixed input container.
            </p>
            <p>
                <strong>2. API Gateway &amp; Controller Tier (FastAPI Backend):</strong> An asynchronous ASGI REST service executing on Uvicorn that orchestrates HTTP routing, multipart file streaming, schema validation via Pydantic models, and cross-origin resource negotiation.
            </p>
            <p>
                <strong>3. Multi-Tier Categorization Cascade:</strong> A hierarchical decision pipeline that cascades from deterministic regular expression dictionaries (Tier 1) to sub-word character n-gram TF-IDF regularized SGD classifiers (Tier 2), and finally to Google Gemini 2.5 Flash few-shot generative reasoning (Tier 3).
            </p>
            <p>
                <strong>4. Unsupervised Anomaly Engine:</strong> A dual-mode detector uniting scikit-learn Isolation Forests with rolling category Z-score boundaries to identify expenditure spikes and duplicate charges without labeled fraud training sets.
            </p>
            <p>
                <strong>5. 2026 Hybrid Contextual RAG Advisory Engine:</strong> An advanced retrieval framework utilizing Hypothetical Document Embeddings (HyDE), parallel dual-space retrieval (BM25 sparse search and Gemini dense embeddings), Reciprocal Rank Fusion (RRF), and Corrective RAG (CRAG) factual verification.
            </p>
            <p>
                <strong>6. Persistence &amp; Cache Layer (SQLite &amp; SQLAlchemy):</strong> An ACID-compliant embedded database managing relational ledger records, user metadata, and a precomputed vector embedding cache table (<code>rag_embeddings</code>).
            </p>
            <p>
                Fig. 5.1 illustrates the comprehensive system architecture and end-to-end data pipeline of SpendWise AI.
            </p>
        </div>
        <div class="page-footer">20</div>
    </div>
    """
    pages.append(page1)

    # -------------------------------------------------------------
    # PAGE 21 (Report Page 21): Fig. 5.1 System Architecture SVG Diagram
    # -------------------------------------------------------------
    page2 = f"""
    <div class="page page-arabic" data-page="21">
        <div class="page-content">
            <div class="figure-container">
                {get_system_architecture_svg()}
                <p class="figure-caption">Fig. 5.1 System Architecture and Overall Workflow of SpendWise AI</p>
            </div>
        </div>
        <div class="page-footer">21</div>
    </div>
    """
    pages.append(page2)

    # -------------------------------------------------------------
    # PAGE 22 (Report Page 22): 5.2 Context Diagram (Text & Fig. 5.2 SVG)
    # -------------------------------------------------------------
    page3 = f"""
    <div class="page page-arabic" data-page="22">
        <div class="page-content">
            <h2 class="section-heading">5.2 Context Diagram</h2>
            <p>
                The Level-0 Context Diagram defines the fundamental boundary of the SpendWise AI platform, encapsulating the entire computational engine within a single conceptual process (Process 0.0) and delineating its data flows with external entities. As shown in Fig. 5.2, the system interfaces with four primary external entities: the End User (who provides transaction CSVs and advisory prompts and receives interactive visual dashboards and advice), the Commercial Banking Export Gateway (the source of truth for financial ledgers), the Google Gemini Cloud AI Service (which provides high-order semantic reasoning and dense vector embeddings), and the Local Operating System File Storage (which ensures persistent local storage).
            </p>
            <div class="figure-container">
                {get_context_diagram_svg()}
                <p class="figure-caption">Fig. 5.2 Level-0 Context Diagram of the Financial Advisory Ecosystem</p>
            </div>
        </div>
        <div class="page-footer">22</div>
    </div>
    """
    pages.append(page3)

    # -------------------------------------------------------------
    # PAGE 23 (Report Page 23): 5.3 Use Case Diagram (Text & Fig. 5.3 SVG)
    # -------------------------------------------------------------
    page4 = f"""
    <div class="page page-arabic" data-page="23">
        <div class="page-content">
            <h2 class="section-heading">5.3 Use Case Diagram</h2>
            <p>
                The Use Case Diagram in Fig. 5.3 models the interactions between system actors and the core functional capabilities of SpendWise AI. Three distinct actors engage with the platform: the primary End User (who initiates ledger uploads, analyzes financial health KPIs, and engages in conversational advisory dialogues), the System Administrator / Auditor (who configures classification rules and inspects database caches), and the Google Gemini AI Cloud Service (which acts as an external system actor invoked during few-shot categorization and hybrid contextual RAG generation).
            </p>
            <div class="figure-container">
                {get_use_case_diagram_svg()}
                <p class="figure-caption">Fig. 5.3 Use Case Diagram Depicting User and AI System Interactions</p>
            </div>
        </div>
        <div class="page-footer">23</div>
    </div>
    """
    pages.append(page4)

    # -------------------------------------------------------------
    # PAGE 24 (Report Page 24): 5.4 Activity Diagram (Text & Fig. 5.4 SVG)
    # -------------------------------------------------------------
    page5 = f"""
    <div class="page page-arabic" data-page="24">
        <div class="page-content">
            <h2 class="section-heading">5.4 Activity Diagram</h2>
            <p>
                The Activity Diagram in Fig. 5.4 visualizes the operational lifecycle and state machine of transaction ingestion across swimlanes. As CSV records are parsed, the system validates schema formatting and routes records through the cascading decision tree. Deterministic regex rules evaluate first; upon failure, the statistical ML classifier evaluates character n-grams. When ML confidence drops below 0.85, the transaction seamlessly escalates to Google Gemini 2.5 Flash. Once categorized, transactions pass through the Isolation Forest and Z-score models before ACID commitment to SQLite.
            </p>
            <div class="figure-container">
                {get_activity_diagram_svg()}
                <p class="figure-caption">Fig. 5.4 Activity Diagram of Transaction Ingestion and Processing</p>
            </div>
        </div>
        <div class="page-footer">24</div>
    </div>
    """
    pages.append(page5)

    # -------------------------------------------------------------
    # PAGE 25 (Report Page 25): 5.5 ER Diagram (Text & Fig. 5.5 SVG)
    # -------------------------------------------------------------
    page6 = f"""
    <div class="page page-arabic" data-page="25">
        <div class="page-content">
            <h2 class="section-heading">5.5 ER Diagram</h2>
            <p>
                The Entity-Relationship (ER) Diagram in Fig. 5.5 models the conceptual domain schema of SpendWise AI. The data model comprises six interconnected entity sets: USER/ACCOUNT (capturing profile and income baselines), TRANSACTION (capturing individual financial debits/credits with categorical and anomaly attributes), RAG_EMBEDDING (maintaining 768-dimensional dense vector embeddings generated via Gemini Text-Embedding-004), CATEGORY_RULE (maintaining regex heuristics for Tier-1 evaluation), ANOMALY_RECORD (logging detected statistical deviations), and BUDGET_GOAL (tracking category spending limits).
            </p>
            <div class="figure-container">
                {get_er_diagram_svg()}
                <p class="figure-caption">Fig. 5.5 Entity-Relationship (ER) Diagram of SpendWise AI Database</p>
            </div>
        </div>
        <div class="page-footer">25</div>
    </div>
    """
    pages.append(page6)

    # -------------------------------------------------------------
    # PAGE 26 (Report Page 26): 5.6 Database Design (Text, Fig. 5.6 SVG & Tables)
    # -------------------------------------------------------------
    page7 = f"""
    <div class="page page-arabic" data-page="26">
        <div class="page-content">
            <h2 class="section-heading">5.6 Database Design</h2>
            <p>
                The physical database layer of SpendWise AI is engineered using SQLite and SQLAlchemy ORM, configured with write-ahead logging (WAL) for high concurrency. Fig. 5.6 details the relational database schema, highlighting column specifications, data types, primary and foreign key constraints, default values, and B-Tree indexes that enable sub-millisecond retrieval across multi-thousand transaction tables.
            </p>
            <div class="figure-container">
                {get_database_design_svg()}
                <p class="figure-caption">Fig. 5.6 Relational Database Design and Schema Specification</p>
            </div>
            <p>
                Table 5.1 defines the relational attributes and integrity constraints for the core <code>transactions</code> entity.
            </p>
            <p class="table-caption">Table 5.1 Transactions Relational Entity Schema Definition</p>
            <table class="academic-table">
                <thead>
                    <tr>
                        <th style="width: 20%;">Column Name</th>
                        <th style="width: 20%;">Data Type</th>
                        <th style="width: 20%;">Constraints</th>
                        <th style="width: 40%;">Description &amp; Functional Semantics</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><code>id</code></td>
                        <td>INTEGER</td>
                        <td>PRIMARY KEY, AUTOINCREMENT</td>
                        <td>Unique synthetic identifier for transactional records.</td>
                    </tr>
                    <tr>
                        <td><code>date</code></td>
                        <td>VARCHAR(50)</td>
                        <td>NOT NULL</td>
                        <td>Standardized transaction date in ISO YYYY-MM-DD format.</td>
                    </tr>
                    <tr>
                        <td><code>description</code></td>
                        <td>TEXT</td>
                        <td>NOT NULL</td>
                        <td>Raw merchant narrative string extracted from bank statement.</td>
                    </tr>
                    <tr>
                        <td><code>amount</code></td>
                        <td>FLOAT</td>
                        <td>NOT NULL, CHECK (amount &gt; 0)</td>
                        <td>Absolute monetary value of the debit or credit transaction.</td>
                    </tr>
                    <tr>
                        <td><code>type</code></td>
                        <td>VARCHAR(20)</td>
                        <td>NOT NULL, CHECK (type IN ('DEBIT', 'CREDIT'))</td>
                        <td>Cash-flow directionality indicator (DEBIT outflow or CREDIT inflow).</td>
                    </tr>
                    <tr>
                        <td><code>category</code></td>
                        <td>VARCHAR(50)</td>
                        <td>DEFAULT 'Uncategorized'</td>
                        <td>Assigned category allocated via multi-tier classification.</td>
                    </tr>
                    <tr>
                        <td><code>is_anomaly</code></td>
                        <td>BOOLEAN</td>
                        <td>DEFAULT 0</td>
                        <td>Binary outlier flag allocated via Isolation Forest and Z-score.</td>
                    </tr>
                    <tr>
                        <td><code>anomaly_score</code></td>
                        <td>FLOAT</td>
                        <td>DEFAULT 0.0</td>
                        <td>Continuous path-length anomaly score from Isolation Forest.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="page-footer">26</div>
    </div>
    """
    pages.append(page7)

    # -------------------------------------------------------------
    # PAGE 27 (Report Page 27): Table 5.2 & 5.7 User Interface Design (Text & Fig. 5.7 Wireframe)
    # -------------------------------------------------------------
    page8 = f"""
    <div class="page page-arabic" data-page="27">
        <div class="page-content">
            <p class="table-caption">Table 5.2 RAG Embeddings Vector Cache Schema Definition</p>
            <table class="academic-table" style="margin-bottom: 20px;">
                <thead>
                    <tr>
                        <th style="width: 20%;">Column Name</th>
                        <th style="width: 20%;">Data Type</th>
                        <th style="width: 20%;">Constraints</th>
                        <th style="width: 40%;">Description &amp; Functional Semantics</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><code>id</code></td>
                        <td>INTEGER</td>
                        <td>PRIMARY KEY, AUTOINCREMENT</td>
                        <td>Unique identifier for dense vector cache rows.</td>
                    </tr>
                    <tr>
                        <td><code>transaction_id</code></td>
                        <td>INTEGER</td>
                        <td>FOREIGN KEY (transactions.id)</td>
                        <td>References the parent transaction record.</td>
                    </tr>
                    <tr>
                        <td><code>chunk_text</code></td>
                        <td>TEXT</td>
                        <td>NOT NULL</td>
                        <td>Synthesized natural language document representation of transaction.</td>
                    </tr>
                    <tr>
                        <td><code>embedding_blob</code></td>
                        <td>BLOB</td>
                        <td>NOT NULL</td>
                        <td>Serialized 768-dimensional Float32 vector from Gemini Text-Embedding-004.</td>
                    </tr>
                    <tr>
                        <td><code>updated_at</code></td>
                        <td>TIMESTAMP</td>
                        <td>DEFAULT CURRENT_TIMESTAMP</td>
                        <td>Timestamp when embedding vector was computed.</td>
                    </tr>
                </tbody>
            </table>

            <h2 class="section-heading">5.7 User Interface Design</h2>
            <p>
                Fig. 5.7 depicts the UI wireframe of SpendWise AI. The layout features an ergonomic Claude-style chat paradigm where messages stack upward above a fixed bottom input bar. Real-time KPI metric cards, donut spending breakdown charts, and outlier alert cards reside above the conversational container, maintaining complete visibility.
            </p>
            <div class="figure-container">
                {get_user_interface_design_svg()}
                <p class="figure-caption">Fig. 5.7 User Interface Wireframe and Pinned Chat Component Layout</p>
            </div>
        </div>
        <div class="page-footer">27</div>
    </div>
    """
    pages.append(page8)

    return pages
