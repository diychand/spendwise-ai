# -*- coding: utf-8 -*-
"""
Standalone Diagram Generator for SpendWise AI Project Report.
Generates:
5.1 System Architecture (5.1_system_architecture.svg)
5.2 Context Diagram (5.2_context_diagram.svg)
5.3 Use Case Diagram (5.3_use_case_diagram.svg)
5.4 Activity Diagram (5.4_activity_diagram.svg)
5.5 ER Diagram (5.5_er_diagram.svg)
5.6 Database Design (5.6_database_design.svg)
5.7 User Interface Design (5.7_user_interface_design.svg)
Also creates an interactive HTML preview gallery (view_diagrams.html).
"""

from pathlib import Path

DIAGRAMS_DIR = Path(r"c:\spendwise-ai\diagrams")

def get_system_architecture_svg():
    return '''<svg viewBox="0 0 920 980" width="100%" height="980" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <marker id="arch-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 9 5 L 0 9 z" fill="#1e3a8a"/>
        </marker>
        <marker id="gemini-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 9 5 L 0 9 z" fill="#7c3aed"/>
        </marker>
        <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#1e3a8a"/>
            <stop offset="100%" stop-color="#2563eb"/>
        </linearGradient>
        <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#ffffff"/>
            <stop offset="100%" stop-color="#f8fafc"/>
        </linearGradient>
        <filter id="boxShadow" x="-2%" y="-2%" width="104%" height="106%">
            <feDropShadow dx="1" dy="2" stdDeviation="2.5" flood-opacity="0.12"/>
        </filter>
    </defs>

    <!-- Background Canvas -->
    <rect width="920" height="980" fill="#f8fafc" rx="8"/>

    <!-- Title Header -->
    <rect x="25" y="20" width="870" height="50" rx="8" fill="url(#headerGrad)"/>
    <text x="460" y="52" fill="#ffffff" font-family="Times New Roman, serif" font-size="16" font-weight="bold" text-anchor="middle" letter-spacing="0.5">
        SPENDWISE AI: MULTI-TIER SYSTEM ARCHITECTURE &amp; WORKFLOW
    </text>

    <!-- TIER 1: PRESENTATION LAYER -->
    <rect x="25" y="85" width="870" height="115" rx="8" fill="url(#cardGrad)" stroke="#3b82f6" stroke-width="1.8" filter="url(#boxShadow)"/>
    <rect x="25" y="85" width="870" height="28" rx="8" fill="#eff6ff"/>
    <text x="45" y="104" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="12.5" font-weight="bold">
        TIER 1: PRESENTATION LAYER (STREAMLIT WEB CLIENT - PORT 8501)
    </text>

    <!-- Components in Presentation Tier -->
    <rect x="45" y="125" width="190" height="60" rx="6" fill="#ffffff" stroke="#93c5fd" stroke-width="1.2"/>
    <text x="140" y="147" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">Claude-Style Chat UI</text>
    <text x="140" y="164" fill="#475569" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">Upward Stacking Messages</text>
    <text x="140" y="177" fill="#047857" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Fixed Bottom Input Bar</text>

    <rect x="255" y="125" width="190" height="60" rx="6" fill="#ffffff" stroke="#93c5fd" stroke-width="1.2"/>
    <text x="350" y="147" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">Financial KPI Dashboard</text>
    <text x="350" y="164" fill="#475569" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">Inflow, Outflow, Savings</text>
    <text x="350" y="177" fill="#475569" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">Real-time Anomaly Badges</text>

    <rect x="465" y="125" width="190" height="60" rx="6" fill="#ffffff" stroke="#93c5fd" stroke-width="1.2"/>
    <text x="560" y="147" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">Interactive Analytics</text>
    <text x="560" y="164" fill="#475569" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">Category Donut Charts</text>
    <text x="560" y="177" fill="#475569" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">Monthly Spending Curves</text>

    <rect x="675" y="125" width="200" height="60" rx="6" fill="#ffffff" stroke="#93c5fd" stroke-width="1.2"/>
    <text x="775" y="147" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">CSV Statement Ingest</text>
    <text x="775" y="164" fill="#475569" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">Drag &amp; Drop Ledger File</text>
    <text x="775" y="177" fill="#0369a1" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Auto-Sniffer Feedback</text>

    <!-- Connector Tier 1 -> Tier 2 -->
    <line x1="460" y1="200" x2="460" y2="230" stroke="#1e3a8a" stroke-width="2.2" marker-end="url(#arch-arrow)"/>
    <text x="468" y="218" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">REST / HTTP JSON Payloads</text>

    <!-- TIER 2: API GATEWAY & CONTROLLER LAYER -->
    <rect x="25" y="230" width="870" height="100" rx="8" fill="url(#cardGrad)" stroke="#0284c7" stroke-width="1.8" filter="url(#boxShadow)"/>
    <rect x="25" y="230" width="870" height="26" rx="8" fill="#f0f9ff"/>
    <text x="45" y="248" fill="#0369a1" font-family="Times New Roman, serif" font-size="12.5" font-weight="bold">
        TIER 2: API GATEWAY &amp; CONTROLLER LAYER (FASTAPI / UVICORN - PORT 8000)
    </text>

    <!-- Controller Endpoints -->
    <rect x="45" y="268" width="150" height="50" rx="5" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.2"/>
    <text x="120" y="287" fill="#0369a1" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">/transactions</text>
    <text x="120" y="303" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Dialect Sniff &amp; Validation</text>

    <rect x="215" y="268" width="150" height="50" rx="5" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.2"/>
    <text x="290" y="287" fill="#0369a1" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">/categorization</text>
    <text x="290" y="303" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Cascade Dispatcher</text>

    <rect x="385" y="268" width="150" height="50" rx="5" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.2"/>
    <text x="460" y="287" fill="#0369a1" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">/anomaly</text>
    <text x="460" y="303" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Isolation Forest &amp; Z-Score</text>

    <rect x="555" y="268" width="150" height="50" rx="5" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.2"/>
    <text x="630" y="287" fill="#0369a1" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">/analysis</text>
    <text x="630" y="303" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Recurring Subscriptions</text>

    <rect x="725" y="268" width="150" height="50" rx="5" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.2"/>
    <text x="800" y="287" fill="#0369a1" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">/agent/chat</text>
    <text x="800" y="303" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Hybrid RAG Copilot</text>

    <!-- Connectors to Processing Subsystems -->
    <line x1="290" y1="330" x2="160" y2="365" stroke="#1e3a8a" stroke-width="1.8" marker-end="url(#arch-arrow)"/>
    <line x1="460" y1="330" x2="460" y2="365" stroke="#1e3a8a" stroke-width="1.8" marker-end="url(#arch-arrow)"/>
    <line x1="800" y1="330" x2="740" y2="365" stroke="#1e3a8a" stroke-width="1.8" marker-end="url(#arch-arrow)"/>

    <!-- TIER 3: COMPUTATIONAL & MACHINE LEARNING ENGINES -->
    <!-- Column 1: Categorization Cascade -->
    <rect x="25" y="365" width="270" height="340" rx="8" fill="url(#cardGrad)" stroke="#059669" stroke-width="1.8" filter="url(#boxShadow)"/>
    <rect x="25" y="365" width="270" height="26" rx="8" fill="#ecfdf5"/>
    <text x="160" y="383" fill="#065f46" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">
        3-TIER CATEGORIZATION CASCADE
    </text>

    <!-- Tier 1 Box -->
    <rect x="40" y="405" width="240" height="70" rx="5" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
    <text x="160" y="425" fill="#166534" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">Tier 1: Deterministic Regex</text>
    <text x="160" y="442" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Curated 200+ Merchant Patterns</text>
    <text x="160" y="456" fill="#047857" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Latency &lt; 0.2 ms | 100% Conf (72% traffic)</text>

    <line x1="160" y1="475" x2="160" y2="495" stroke="#059669" stroke-width="1.5" marker-end="url(#arch-arrow)"/>
    <text x="175" y="488" fill="#059669" font-family="Times New Roman, serif" font-size="8">Unmatched</text>

    <!-- Tier 2 Box -->
    <rect x="40" y="495" width="240" height="85" rx="5" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
    <text x="160" y="515" fill="#166534" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">Tier 2: TF-IDF + SGDClassifier</text>
    <text x="160" y="532" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Sub-word Char N-grams (2-5)</text>
    <text x="160" y="546" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Modified Huber Loss Probability</text>
    <text x="160" y="562" fill="#047857" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Commit if Conf &ge; 0.85 (18% traffic)</text>

    <line x1="160" y1="580" x2="160" y2="605" stroke="#059669" stroke-width="1.5" marker-end="url(#arch-arrow)"/>
    <text x="175" y="595" fill="#7c3aed" font-family="Times New Roman, serif" font-size="8">Conf &lt; 0.85</text>

    <!-- Tier 3 Box -->
    <rect x="40" y="605" width="240" height="85" rx="5" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.2"/>
    <text x="160" y="625" fill="#6b21a8" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">Tier 3: Gemini 2.5 Flash LLM</text>
    <text x="160" y="642" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Few-Shot Structured JSON Prompt</text>
    <text x="160" y="656" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Semantic Edge Case Disambiguation</text>
    <text x="160" y="672" fill="#7c3aed" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Near-Human Accuracy (10% traffic)</text>

    <!-- Column 2: Anomaly Detection Engine -->
    <rect x="325" y="365" width="270" height="340" rx="8" fill="url(#cardGrad)" stroke="#d97706" stroke-width="1.8" filter="url(#boxShadow)"/>
    <rect x="325" y="365" width="270" height="26" rx="8" fill="#fffbeb"/>
    <text x="460" y="383" fill="#92400e" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">
        ANOMALY DETECTION ENGINE
    </text>

    <!-- Isolation Forest -->
    <rect x="340" y="415" width="240" height="95" rx="5" fill="#fffbeb" stroke="#fde68a" stroke-width="1.2"/>
    <text x="460" y="437" fill="#92400e" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">Isolation Forest Ensemble</text>
    <text x="460" y="456" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">100 Randomized iTrees</text>
    <text x="460" y="471" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Contamination = 0.03 | max_samples=256</text>
    <text x="460" y="486" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Path-Length Anomaly Scoring s(x, n)</text>
    <text x="460" y="501" fill="#b45309" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Multi-feature Spatial Outlier Isolation</text>

    <line x1="460" y1="510" x2="460" y2="540" stroke="#d97706" stroke-width="1.5" marker-end="url(#arch-arrow)"/>

    <!-- Rolling Z-Score -->
    <rect x="340" y="540" width="240" height="90" rx="5" fill="#fffbeb" stroke="#fde68a" stroke-width="1.2"/>
    <text x="460" y="562" fill="#92400e" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">Category Rolling Z-Scores</text>
    <text x="460" y="581" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Dynamic Baseline Mean &amp; Variance</text>
    <text x="460" y="596" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Threshold: Z = (x - &mu;) / &sigma; &gt; 2.5</text>
    <text x="460" y="613" fill="#b45309" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Duplicate Charge &amp; Price Hike Filter</text>

    <!-- Column 3: 2026 Hybrid RAG -->
    <rect x="625" y="365" width="270" height="340" rx="8" fill="url(#cardGrad)" stroke="#7c3aed" stroke-width="1.8" filter="url(#boxShadow)"/>
    <rect x="625" y="365" width="270" height="26" rx="8" fill="#f5f3ff"/>
    <text x="760" y="383" fill="#5b21b6" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">
        2026 HYBRID CONTEXTUAL RAG
    </text>

    <!-- HyDE -->
    <rect x="640" y="405" width="240" height="50" rx="5" fill="#faf5ff" stroke="#ddd6fe" stroke-width="1.2"/>
    <text x="760" y="425" fill="#6b21a8" font-family="Times New Roman, serif" font-size="10" font-weight="bold" text-anchor="middle">1. HyDE Query Expansion</text>
    <text x="760" y="442" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Synthesizes Hypothetical Finance Doc</text>

    <!-- Dual Retrieval Grid -->
    <rect x="640" y="465" width="115" height="65" rx="5" fill="#faf5ff" stroke="#ddd6fe" stroke-width="1.2"/>
    <text x="697" y="485" fill="#6b21a8" font-family="Times New Roman, serif" font-size="9" font-weight="bold" text-anchor="middle">Sparse BM25</text>
    <text x="697" y="501" fill="#475569" font-family="Times New Roman, serif" font-size="7.5" text-anchor="middle">Inverted Lexical Index</text>
    <text x="697" y="513" fill="#475569" font-family="Times New Roman, serif" font-size="7.5" text-anchor="middle">Exact Numbers &amp; Codes</text>

    <rect x="765" y="465" width="115" height="65" rx="5" fill="#faf5ff" stroke="#ddd6fe" stroke-width="1.2"/>
    <text x="822" y="485" fill="#6b21a8" font-family="Times New Roman, serif" font-size="9" font-weight="bold" text-anchor="middle">Dense Vector</text>
    <text x="822" y="501" fill="#475569" font-family="Times New Roman, serif" font-size="7.5" text-anchor="middle">Text-Embedding-004</text>
    <text x="822" y="513" fill="#475569" font-family="Times New Roman, serif" font-size="7.5" text-anchor="middle">Semantic Conceptual</text>

    <!-- RRF -->
    <rect x="640" y="540" width="240" height="55" rx="5" fill="#faf5ff" stroke="#ddd6fe" stroke-width="1.2"/>
    <text x="760" y="559" fill="#6b21a8" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold" text-anchor="middle">3. Reciprocal Rank Fusion (RRF)</text>
    <text x="760" y="575" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">RRF Score = &Sigma; 1 / (60 + Rank_i)</text>
    <text x="760" y="588" fill="#5b21b6" font-family="Times New Roman, serif" font-size="8" font-weight="bold" text-anchor="middle">Unified Top-K Document Ranking</text>

    <!-- CRAG -->
    <rect x="640" y="605" width="240" height="85" rx="5" fill="#faf5ff" stroke="#ddd6fe" stroke-width="1.2"/>
    <text x="760" y="625" fill="#6b21a8" font-family="Times New Roman, serif" font-size="10" font-weight="bold" text-anchor="middle">4. Corrective RAG (CRAG) &amp; LLM</text>
    <text x="760" y="642" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Confidence Gate Evaluator (&gamma; = 0.015)</text>
    <text x="760" y="656" fill="#334155" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Gemini 2.5 Flash Advisory Generator</text>
    <text x="760" y="672" fill="#7c3aed" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Zero Hallucination Guaranteed</text>

    <!-- Connectors down to Database Tier -->
    <line x1="160" y1="705" x2="160" y2="745" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="460" y1="705" x2="460" y2="745" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="760" y1="705" x2="760" y2="745" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="160" y1="745" x2="760" y2="745" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="460" y1="745" x2="460" y2="765" stroke="#1e3a8a" stroke-width="2.2" marker-end="url(#arch-arrow)"/>

    <!-- TIER 4: PERSISTENCE & STORAGE LAYER -->
    <rect x="25" y="765" width="870" height="110" rx="8" fill="url(#cardGrad)" stroke="#475569" stroke-width="1.8" filter="url(#boxShadow)"/>
    <rect x="25" y="765" width="870" height="26" rx="8" fill="#f1f5f9"/>
    <text x="45" y="783" fill="#1e293b" font-family="Times New Roman, serif" font-size="12.5" font-weight="bold">
        TIER 4: LOCAL PERSISTENCE &amp; STORAGE LAYER (SQLITE &amp; SQLALCHEMY ORM - SPENDWISE.DB)
    </text>

    <!-- Database Tables -->
    <rect x="45" y="803" width="260" height="60" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
    <text x="175" y="824" fill="#0f172a" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">Table: transactions</text>
    <text x="175" y="841" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">id (PK), date, description, amount, type,</text>
    <text x="175" y="854" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">category, is_anomaly, anomaly_score, user_id</text>

    <rect x="330" y="803" width="260" height="60" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
    <text x="460" y="824" fill="#0f172a" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">Table: rag_embeddings</text>
    <text x="460" y="841" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">id (PK), transaction_id (FK), chunk_text,</text>
    <text x="460" y="854" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">embedding_blob (768-dim float), updated_at</text>

    <rect x="615" y="803" width="260" height="60" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
    <text x="745" y="824" fill="#0f172a" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">Table: category_rules &amp; config</text>
    <text x="745" y="841" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">id (PK), pattern, category, priority,</text>
    <text x="745" y="854" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">match_type, is_active, user budget limits</text>

    <!-- EXTERNAL INTEGRATION BOX -->
    <rect x="25" y="895" width="870" height="65" rx="8" fill="#fdf4ff" stroke="#a855f7" stroke-width="1.8" stroke-dasharray="5 4"/>
    <text x="460" y="922" fill="#6b21a8" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">
        EXTERNAL CLOUD INTEGRATION: GOOGLE GEMINI 2.5 REST API (TLS 1.3 ENCRYPTION)
    </text>
    <text x="460" y="942" fill="#7e22ce" font-family="Times New Roman, serif" font-size="9.5" text-anchor="middle">
        Dispatches Tier-3 Few-Shot Categorization &bull; Generates Text-Embedding-004 Dense Vectors &bull; HyDE Expansion &bull; Advisory Synthesis
    </text>
</svg>'''

def get_context_diagram_svg():
    return '''<svg viewBox="0 0 880 540" width="100%" height="540" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <marker id="ctx-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 9 5 L 0 9 z" fill="#1e3a8a"/>
        </marker>
        <linearGradient id="bubbleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#eff6ff"/>
            <stop offset="100%" stop-color="#dbeafe"/>
        </linearGradient>
        <filter id="ctxShadow" x="-2%" y="-2%" width="104%" height="106%">
            <feDropShadow dx="1" dy="2" stdDeviation="3" flood-opacity="0.12"/>
        </filter>
    </defs>

    <rect width="880" height="540" fill="#f8fafc" rx="8"/>

    <!-- Central Process Bubble (Process 0.0) -->
    <circle cx="440" cy="270" r="130" fill="url(#bubbleGrad)" stroke="#1e3a8a" stroke-width="3" filter="url(#ctxShadow)"/>
    <text x="440" y="240" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="16" font-weight="bold" text-anchor="middle">0.0</text>
    <text x="440" y="262" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="14" font-weight="bold" text-anchor="middle">SPENDWISE AI</text>
    <text x="440" y="280" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">FINANCIAL ADVISORY</text>
    <text x="440" y="298" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">SYSTEM</text>
    <text x="440" y="318" fill="#475569" font-family="Times New Roman, serif" font-size="9.5" text-anchor="middle">(Core Processing Engine)</text>

    <!-- External Entity 1: End User / Consumer (Left) -->
    <rect x="30" y="195" width="180" height="150" rx="8" fill="#ffffff" stroke="#1e293b" stroke-width="2" filter="url(#ctxShadow)"/>
    <rect x="30" y="195" width="180" height="32" rx="8" fill="#0f172a"/>
    <text x="120" y="216" fill="#ffffff" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">END USER / CONSUMER</text>
    <text x="120" y="245" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Personal Account Holder</text>
    <text x="120" y="262" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Uploads CSV Statements</text>
    <text x="120" y="279" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Queries Advisory Agent</text>
    <text x="120" y="296" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Reviews Anomaly Alerts</text>
    <text x="120" y="313" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Inspects KPI Metrics</text>

    <!-- External Entity 2: Commercial Bank Export System (Top) -->
    <rect x="340" y="25" width="200" height="80" rx="8" fill="#ffffff" stroke="#1e293b" stroke-width="2" filter="url(#ctxShadow)"/>
    <rect x="340" y="25" width="200" height="28" rx="8" fill="#0f172a"/>
    <text x="440" y="44" fill="#ffffff" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">COMMERCIAL BANK / OFX</text>
    <text x="440" y="70" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Bank Export Gateway</text>
    <text x="440" y="88" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; CSV Statements / Ledgers</text>

    <!-- External Entity 3: Google Gemini Cloud AI (Right) -->
    <rect x="670" y="195" width="180" height="150" rx="8" fill="#ffffff" stroke="#6b21a8" stroke-width="2" filter="url(#ctxShadow)"/>
    <rect x="670" y="195" width="180" height="32" rx="8" fill="#6b21a8"/>
    <text x="760" y="216" fill="#ffffff" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">GOOGLE GEMINI AI</text>
    <text x="760" y="245" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Gemini 2.5 Flash LLM</text>
    <text x="760" y="262" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Text-Embedding-004</text>
    <text x="760" y="279" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Few-Shot Inference</text>
    <text x="760" y="296" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; HyDE Query Synthesis</text>
    <text x="760" y="313" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Grounded Advisory Agent</text>

    <!-- External Entity 4: Local Storage (Bottom) -->
    <rect x="340" y="435" width="200" height="80" rx="8" fill="#ffffff" stroke="#1e293b" stroke-width="2" filter="url(#ctxShadow)"/>
    <rect x="340" y="435" width="200" height="28" rx="8" fill="#0f172a"/>
    <text x="440" y="454" fill="#ffffff" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">LOCAL FILE SYSTEM</text>
    <text x="440" y="480" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; SQLite Database (spendwise.db)</text>
    <text x="440" y="498" fill="#334155" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">&bull; Vector Blob Cache &amp; Logs</text>

    <!-- DATA FLOWS -->
    <!-- User -> System (Top arrow) -->
    <path d="M 210 235 L 315 235" fill="none" stroke="#1e3a8a" stroke-width="1.8" marker-end="url(#ctx-arrow)"/>
    <text x="260" y="226" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Bank CSV Statement</text>
    <text x="260" y="246" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">Natural Language Queries</text>

    <!-- System -> User (Bottom arrow) -->
    <path d="M 315 305 L 210 305" fill="none" stroke="#047857" stroke-width="1.8" marker-end="url(#ctx-arrow)"/>
    <text x="260" y="297" fill="#047857" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Categorized Ledgers</text>
    <text x="260" y="322" fill="#047857" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">Anomaly Alerts &amp; Advice</text>

    <!-- Bank -> System -->
    <path d="M 440 105 L 440 140" fill="none" stroke="#1e3a8a" stroke-width="1.8" marker-end="url(#ctx-arrow)"/>
    <text x="448" y="126" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">Raw Statement Export</text>

    <!-- System -> Gemini -->
    <path d="M 565 235 L 670 235" fill="none" stroke="#7c3aed" stroke-width="1.8" marker-end="url(#ctx-arrow)"/>
    <text x="618" y="222" fill="#7c3aed" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Few-Shot Prompts</text>
    <text x="618" y="246" fill="#7c3aed" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">Chunks &amp; HyDE Prompts</text>

    <!-- Gemini -> System -->
    <path d="M 670 305 L 565 305" fill="none" stroke="#7c3aed" stroke-width="1.8" marker-end="url(#ctx-arrow)"/>
    <text x="618" y="297" fill="#7c3aed" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Category JSON Labels</text>
    <text x="618" y="322" fill="#7c3aed" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">768-d Vector Embeddings</text>

    <!-- System <-> Local Storage -->
    <path d="M 425 400 L 425 435" fill="none" stroke="#334155" stroke-width="1.8" marker-end="url(#ctx-arrow)"/>
    <text x="415" y="420" fill="#334155" font-family="Times New Roman, serif" font-size="8" text-anchor="end">Write Rows &amp; Blobs</text>

    <path d="M 455 435 L 455 400" fill="none" stroke="#334155" stroke-width="1.8" marker-end="url(#ctx-arrow)"/>
    <text x="465" y="420" fill="#334155" font-family="Times New Roman, serif" font-size="8" text-anchor="start">Read Ledger Records</text>
</svg>'''

def get_use_case_diagram_svg():
    return '''<svg viewBox="0 0 900 820" width="100%" height="820" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <marker id="uc-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 9 5 L 0 9 z" fill="#475569"/>
        </marker>
        <filter id="ucShadow" x="-2%" y="-2%" width="104%" height="106%">
            <feDropShadow dx="1" dy="2" stdDeviation="2.5" flood-opacity="0.1"/>
        </filter>
    </defs>

    <rect width="900" height="820" fill="#f8fafc" rx="8"/>

    <!-- System Boundary -->
    <rect x="230" y="35" width="440" height="750" rx="10" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.5" filter="url(#ucShadow)"/>
    <rect x="230" y="35" width="440" height="35" rx="10" fill="#eff6ff"/>
    <text x="450" y="58" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="13" font-weight="bold" text-anchor="middle" letter-spacing="0.5">
        SPENDWISE AI SYSTEM BOUNDARY
    </text>

    <!-- ACTOR 1: END USER (Left Top) -->
    <g transform="translate(60, 210)">
        <circle cx="50" cy="20" r="18" fill="#e0f2fe" stroke="#0f172a" stroke-width="2"/>
        <line x1="50" y1="38" x2="50" y2="85" stroke="#0f172a" stroke-width="2.5"/>
        <line x1="20" y1="52" x2="80" y2="52" stroke="#0f172a" stroke-width="2.5"/>
        <line x1="50" y1="85" x2="25" y2="135" stroke="#0f172a" stroke-width="2.5"/>
        <line x1="50" y1="85" x2="75" y2="135" stroke="#0f172a" stroke-width="2.5"/>
        <text x="50" y="160" fill="#0f172a" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">End User /</text>
        <text x="50" y="176" fill="#0f172a" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">Consumer</text>
    </g>

    <!-- ACTOR 2: AUDITOR / ADMIN (Left Bottom) -->
    <g transform="translate(60, 560)">
        <circle cx="50" cy="20" r="18" fill="#f1f5f9" stroke="#0f172a" stroke-width="2"/>
        <line x1="50" y1="38" x2="50" y2="85" stroke="#0f172a" stroke-width="2.5"/>
        <line x1="20" y1="52" x2="80" y2="52" stroke="#0f172a" stroke-width="2.5"/>
        <line x1="50" y1="85" x2="25" y2="135" stroke="#0f172a" stroke-width="2.5"/>
        <line x1="50" y1="85" x2="75" y2="135" stroke="#0f172a" stroke-width="2.5"/>
        <text x="50" y="160" fill="#0f172a" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">Financial Auditor /</text>
        <text x="50" y="176" fill="#0f172a" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">System Admin</text>
    </g>

    <!-- ACTOR 3: GOOGLE GEMINI SERVICE (Right) -->
    <rect x="710" y="340" width="160" height="100" rx="8" fill="#fdf4ff" stroke="#9333ea" stroke-width="2" filter="url(#ucShadow)"/>
    <text x="790" y="375" fill="#6b21a8" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">&lt;&lt;Service Actor&gt;&gt;</text>
    <text x="790" y="395" fill="#6b21a8" font-family="Times New Roman, serif" font-size="13" font-weight="bold" text-anchor="middle">Google Gemini</text>
    <text x="790" y="415" fill="#475569" font-family="Times New Roman, serif" font-size="10" text-anchor="middle">Cloud AI API</text>

    <!-- USE CASES (Ovals) -->
    <!-- UC 1: Upload CSV -->
    <ellipse cx="450" cy="110" rx="160" ry="26" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="450" y="115" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">
        UC-01: Ingest &amp; Validate Bank CSV Statement
    </text>

    <!-- UC 2: Cascading Categorization -->
    <ellipse cx="450" cy="190" rx="160" ry="30" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="450" y="188" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">
        UC-02: Auto-Categorize Transactions
    </text>
    <text x="450" y="204" fill="#047857" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">
        (Tier 1: Regex &bull; Tier 2: SGD ML &bull; Tier 3: Gemini)
    </text>

    <!-- UC 3: Outlier & Anomaly Detection -->
    <ellipse cx="450" cy="280" rx="160" ry="28" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="450" y="278" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">
        UC-03: Audit Anomalies &amp; Outliers
    </text>
    <text x="450" y="294" fill="#b45309" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">
        (Isolation Forest Ensemble + Rolling Z-Score)
    </text>

    <!-- UC 4: Financial Health Dashboard -->
    <ellipse cx="450" cy="370" rx="160" ry="28" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="450" y="368" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">
        UC-04: View KPI Metrics &amp; Spend Visuals
    </text>
    <text x="450" y="384" fill="#475569" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">
        (Inflow/Outflow Cards, Donut Charts, Net Savings)
    </text>

    <!-- UC 5: Recurring Subscriptions -->
    <ellipse cx="450" cy="460" rx="160" ry="26" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="450" y="465" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">
        UC-05: Detect Recurring Subscriptions
    </text>

    <!-- UC 6: Query Conversational Advisor -->
    <ellipse cx="450" cy="550" rx="160" ry="32" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="450" y="546" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">
        UC-06: Query Conversational Advisor
    </text>
    <text x="450" y="562" fill="#7c3aed" font-family="Times New Roman, serif" font-size="9" text-anchor="middle">
        (2026 Hybrid RAG: HyDE + BM25 + Vector + RRF + CRAG)
    </text>

    <!-- UC 7: Rule Overrides -->
    <ellipse cx="450" cy="640" rx="160" ry="26" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="450" y="645" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">
        UC-07: Configure Categorization Rules &amp; Overrides
    </text>

    <!-- UC 8: Export Audit Summary -->
    <ellipse cx="450" cy="725" rx="160" ry="26" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="450" y="730" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">
        UC-08: Export Verified Financial Audit Ledger
    </text>

    <!-- USER ASSOCIATION LINES -->
    <line x1="160" y1="260" x2="295" y2="120" stroke="#334155" stroke-width="1.5"/>
    <line x1="160" y1="265" x2="290" y2="190" stroke="#334155" stroke-width="1.5"/>
    <line x1="160" y1="270" x2="292" y2="280" stroke="#334155" stroke-width="1.5"/>
    <line x1="160" y1="275" x2="290" y2="370" stroke="#334155" stroke-width="1.5"/>
    <line x1="160" y1="280" x2="295" y2="460" stroke="#334155" stroke-width="1.5"/>
    <line x1="160" y1="285" x2="295" y2="540" stroke="#334155" stroke-width="1.5"/>

    <!-- ADMIN ASSOCIATION LINES -->
    <line x1="160" y1="620" x2="295" y2="640" stroke="#334155" stroke-width="1.5"/>
    <line x1="160" y1="630" x2="295" y2="720" stroke="#334155" stroke-width="1.5"/>

    <!-- GEMINI SERVICE ASSOCIATION LINES -->
    <line x1="710" y1="365" x2="605" y2="205" stroke="#9333ea" stroke-width="1.5" stroke-dasharray="4 4"/>
    <text x="668" y="275" fill="#7e22ce" font-family="Times New Roman, serif" font-size="8.5">&lt;&lt;invokes Tier 3&gt;&gt;</text>
    <line x1="710" y1="415" x2="605" y2="540" stroke="#9333ea" stroke-width="1.5" stroke-dasharray="4 4"/>
    <text x="668" y="490" fill="#7e22ce" font-family="Times New Roman, serif" font-size="8.5">&lt;&lt;synthesizes RAG&gt;&gt;</text>
</svg>'''

def get_activity_diagram_svg():
    return '''<svg viewBox="0 0 920 900" width="100%" height="900" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <marker id="act-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 9 5 L 0 9 z" fill="#1e3a8a"/>
        </marker>
        <marker id="err-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 9 5 L 0 9 z" fill="#dc2626"/>
        </marker>
        <filter id="actShadow" x="-2%" y="-2%" width="104%" height="106%">
            <feDropShadow dx="1" dy="2" stdDeviation="2" flood-opacity="0.1"/>
        </filter>
    </defs>

    <rect width="920" height="900" fill="#f8fafc" rx="8"/>

    <!-- Swimlanes Background -->
    <rect x="20" y="20" width="880" height="860" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
    
    <!-- Swimlane Headers -->
    <rect x="20" y="20" width="220" height="35" rx="8" fill="#eff6ff"/>
    <text x="130" y="42" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">USER / STREAMLIT UI</text>

    <rect x="240" y="20" width="220" height="35" fill="#f0fdf4"/>
    <text x="350" y="42" fill="#166534" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">FASTAPI CONTROLLER</text>

    <rect x="460" y="20" width="230" height="35" fill="#fffbeb"/>
    <text x="575" y="42" fill="#92400e" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">ML &amp; ANOMALY ENGINE</text>

    <rect x="690" y="20" width="210" height="35" rx="8" fill="#faf5ff"/>
    <text x="795" y="42" fill="#6b21a8" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">RAG &amp; DATABASE</text>

    <!-- Swimlane Vertical Dividers -->
    <line x1="240" y1="20" x2="240" y2="880" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>
    <line x1="460" y1="20" x2="460" y2="880" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>
    <line x1="690" y1="20" x2="690" y2="880" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>

    <!-- Start Node -->
    <circle cx="130" cy="80" r="14" fill="#1e3a8a"/>
    <text x="130" y="110" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="10" font-weight="bold" text-anchor="middle">Start Session</text>
    <line x1="130" y1="94" x2="130" y2="130" stroke="#1e3a8a" stroke-width="2" marker-end="url(#act-arrow)"/>

    <!-- Action 1: Upload File -->
    <rect x="40" y="130" width="180" height="45" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2" filter="url(#actShadow)"/>
    <text x="130" y="150" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold" text-anchor="middle">Select &amp; Upload Bank CSV</text>
    <text x="130" y="164" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Multipart file transfer</text>

    <!-- Connector UI -> Controller -->
    <path d="M 220 152 L 350 152 L 350 195" fill="none" stroke="#1e3a8a" stroke-width="2" marker-end="url(#act-arrow)"/>

    <!-- Action 2: Dialect Sniff & Validate -->
    <rect x="260" y="195" width="180" height="50" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.2" filter="url(#actShadow)"/>
    <text x="350" y="215" fill="#166534" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold" text-anchor="middle">Sniff Dialect &amp; Delimiters</text>
    <text x="350" y="230" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Validate Schema Headers</text>

    <line x1="350" y1="245" x2="350" y2="275" stroke="#1e3a8a" stroke-width="2" marker-end="url(#act-arrow)"/>

    <!-- Decision 1: Headers Valid? -->
    <polygon points="350,275 400,305 350,335 300,305" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="350" y="309" fill="#92400e" font-family="Times New Roman, serif" font-size="9" font-weight="bold" text-anchor="middle">Headers OK?</text>

    <!-- Branch: Invalid -> HTTP 400 back to UI -->
    <path d="M 300 305 L 130 305 L 130 350" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#err-arrow)"/>
    <text x="210" y="297" fill="#dc2626" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">[No: Missing Cols]</text>
    <rect x="40" y="350" width="180" height="42" rx="6" fill="#fee2e2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="130" y="368" fill="#991b1b" font-family="Times New Roman, serif" font-size="9" font-weight="bold" text-anchor="middle">Display HTTP 400 Error</text>
    <text x="130" y="381" fill="#991b1b" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">Prompt user with schema fix</text>

    <!-- Branch: Valid -> Iterate Rows -->
    <path d="M 400 305 L 575 305 L 575 350" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#act-arrow)"/>
    <text x="475" y="297" fill="#059669" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">[Yes: Valid Rows]</text>

    <!-- Action 3: Tier 1 Regex -->
    <rect x="480" y="350" width="190" height="45" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.2" filter="url(#actShadow)"/>
    <text x="575" y="370" fill="#92400e" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold" text-anchor="middle">Tier 1: Check Regex Rules</text>
    <text x="575" y="384" fill="#475569" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Match merchant string patterns</text>

    <line x1="575" y1="395" x2="575" y2="420" stroke="#1e3a8a" stroke-width="2" marker-end="url(#act-arrow)"/>

    <!-- Decision 2: Regex Hit? -->
    <polygon points="575,420 620,445 575,470 530,445" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="575" y="449" fill="#92400e" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Regex Hit?</text>

    <!-- Unmatched -> Tier 2 ML -->
    <line x1="575" y1="470" x2="575" y2="500" stroke="#1e3a8a" stroke-width="2" marker-end="url(#act-arrow)"/>
    <text x="583" y="488" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="8">[No]</text>

    <rect x="480" y="500" width="190" height="50" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.2" filter="url(#actShadow)"/>
    <text x="575" y="520" fill="#92400e" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold" text-anchor="middle">Tier 2: TF-IDF + SGDClassifier</text>
    <text x="575" y="535" fill="#475569" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">Character n-grams &amp; Huber loss</text>

    <line x1="575" y1="550" x2="575" y2="575" stroke="#1e3a8a" stroke-width="2" marker-end="url(#act-arrow)"/>

    <!-- Decision 3: Conf >= 0.85? -->
    <polygon points="575,575 620,600 575,625 530,600" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="575" y="604" fill="#92400e" font-family="Times New Roman, serif" font-size="8" font-weight="bold" text-anchor="middle">Conf &ge; 0.85?</text>

    <!-- Fallback -> Tier 3 Gemini -->
    <path d="M 530 600 L 485 600 L 485 645" fill="none" stroke="#7c3aed" stroke-width="1.5" marker-end="url(#act-arrow)"/>
    <text x="495" y="593" fill="#7c3aed" font-family="Times New Roman, serif" font-size="8">[No]</text>
    <rect x="475" y="645" width="105" height="42" rx="5" fill="#faf5ff" stroke="#a855f7" stroke-width="1.2"/>
    <text x="527" y="663" fill="#6b21a8" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Tier 3: Gemini LLM</text>
    <text x="527" y="675" fill="#475569" font-family="Times New Roman, serif" font-size="7.5" text-anchor="middle">Few-shot JSON</text>

    <!-- All classification paths merge to Anomaly Engine -->
    <line x1="620" y1="445" x2="665" y2="445" stroke="#059669" stroke-width="1.5"/>
    <line x1="665" y1="445" x2="665" y2="705" stroke="#059669" stroke-width="1.5"/>

    <line x1="620" y1="600" x2="645" y2="600" stroke="#059669" stroke-width="1.5"/>
    <line x1="645" y1="600" x2="645" y2="705" stroke="#059669" stroke-width="1.5"/>

    <path d="M 527 687 L 527 705 L 665 705" fill="none" stroke="#7c3aed" stroke-width="1.5"/>

    <path d="M 645 705 L 575 705 L 575 725" fill="none" stroke="#1e3a8a" stroke-width="2" marker-end="url(#act-arrow)"/>

    <!-- Action 4: Anomaly Detection -->
    <rect x="480" y="725" width="190" height="50" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.2" filter="url(#actShadow)"/>
    <text x="575" y="745" fill="#92400e" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold" text-anchor="middle">Run Isolation Forest &amp; Z-Score</text>
    <text x="575" y="760" fill="#475569" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">Calculate anomaly_score &amp; flag</text>

    <!-- Connector to Database & RAG -->
    <path d="M 670 750 L 795 750 L 795 780" fill="none" stroke="#1e3a8a" stroke-width="2" marker-end="url(#act-arrow)"/>

    <!-- Action 5: Save DB & Cache Vectors -->
    <rect x="710" y="780" width="170" height="55" rx="6" fill="#faf5ff" stroke="#a855f7" stroke-width="1.2" filter="url(#actShadow)"/>
    <text x="795" y="802" fill="#6b21a8" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold" text-anchor="middle">Commit to SQLite &amp; RAG</text>
    <text x="795" y="818" fill="#475569" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">Store rows &amp; 768-d vectors</text>

    <!-- Final Output to Dashboard -->
    <path d="M 795 835 L 795 855 L 130 855 L 130 805" fill="none" stroke="#1e3a8a" stroke-width="2" marker-end="url(#act-arrow)"/>

    <!-- Action 6: Render Dashboard -->
    <rect x="40" y="755" width="180" height="50" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2" filter="url(#actShadow)"/>
    <text x="130" y="776" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold" text-anchor="middle">Render Claude Chat &amp; KPIs</text>
    <text x="130" y="792" fill="#475569" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">Ready for conversational queries</text>

    <!-- Stop Node -->
    <circle cx="130" cy="730" r="13" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.5"/>
    <circle cx="130" cy="730" r="8" fill="#1e3a8a"/>
</svg>'''

def get_er_diagram_svg():
    return '''<svg viewBox="0 0 920 620" width="100%" height="620" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <filter id="erShadow" x="-2%" y="-2%" width="104%" height="106%">
            <feDropShadow dx="1" dy="2" stdDeviation="2.5" flood-opacity="0.12"/>
        </filter>
        <marker id="crow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">
            <path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#1e3a8a" stroke-width="1.5"/>
        </marker>
    </defs>

    <rect width="920" height="620" fill="#f8fafc" rx="8"/>

    <!-- TITLE -->
    <text x="460" y="32" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="15" font-weight="bold" text-anchor="middle">
        ENTITY-RELATIONSHIP (ER) DIAGRAM - SPENDWISE AI
    </text>

    <!-- ENTITY 1: USER / ACCOUNT -->
    <rect x="40" y="70" width="220" height="175" rx="6" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8" filter="url(#erShadow)"/>
    <rect x="40" y="70" width="220" height="30" rx="6" fill="#1e3a8a"/>
    <text x="150" y="90" fill="#ffffff" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">USER / ACCOUNT</text>
    <text x="52" y="122" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">PK  user_id: INTEGER</text>
    <text x="52" y="142" fill="#334155" font-family="Times New Roman, serif" font-size="9">    username: VARCHAR(50)</text>
    <text x="52" y="162" fill="#334155" font-family="Times New Roman, serif" font-size="9">    email: VARCHAR(100)</text>
    <text x="52" y="182" fill="#334155" font-family="Times New Roman, serif" font-size="9">    currency_code: VARCHAR(10)</text>
    <text x="52" y="202" fill="#334155" font-family="Times New Roman, serif" font-size="9">    monthly_income: FLOAT</text>
    <text x="52" y="222" fill="#334155" font-family="Times New Roman, serif" font-size="9">    created_at: TIMESTAMP</text>

    <!-- RELATIONSHIP 1: USER OWNS TRANSACTIONS (Diamond) -->
    <polygon points="360,157 410,132 460,157 410,182" fill="#f0fdf4" stroke="#059669" stroke-width="1.5"/>
    <text x="410" y="161" fill="#065f46" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold" text-anchor="middle">Owns</text>

    <line x1="260" y1="157" x2="360" y2="157" stroke="#1e3a8a" stroke-width="1.8"/>
    <text x="275" y="150" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold">1</text>

    <line x1="460" y1="157" x2="560" y2="157" stroke="#1e3a8a" stroke-width="1.8"/>
    <text x="540" y="150" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold">N</text>

    <!-- ENTITY 2: TRANSACTION -->
    <rect x="560" y="70" width="240" height="235" rx="6" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8" filter="url(#erShadow)"/>
    <rect x="560" y="70" width="240" height="30" rx="6" fill="#1e3a8a"/>
    <text x="680" y="90" fill="#ffffff" font-family="Times New Roman, serif" font-size="11.5" font-weight="bold" text-anchor="middle">TRANSACTION</text>
    <text x="572" y="120" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">PK  transaction_id: INTEGER</text>
    <text x="572" y="139" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">FK  user_id: INTEGER</text>
    <text x="572" y="158" fill="#334155" font-family="Times New Roman, serif" font-size="9">    date: VARCHAR(50)</text>
    <text x="572" y="177" fill="#334155" font-family="Times New Roman, serif" font-size="9">    description: TEXT</text>
    <text x="572" y="196" fill="#334155" font-family="Times New Roman, serif" font-size="9">    amount: FLOAT</text>
    <text x="572" y="215" fill="#334155" font-family="Times New Roman, serif" font-size="9">    type: VARCHAR(20) [DEBIT/CREDIT]</text>
    <text x="572" y="234" fill="#334155" font-family="Times New Roman, serif" font-size="9">    category: VARCHAR(50)</text>
    <text x="572" y="253" fill="#334155" font-family="Times New Roman, serif" font-size="9">    is_anomaly: BOOLEAN</text>
    <text x="572" y="272" fill="#334155" font-family="Times New Roman, serif" font-size="9">    anomaly_score: FLOAT</text>
    <text x="572" y="291" fill="#334155" font-family="Times New Roman, serif" font-size="9">    created_at: TIMESTAMP</text>

    <!-- RELATIONSHIP 2: TRANSACTION HAS EMBEDDING -->
    <polygon points="680,355 725,330 770,355 725,380" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5"/>
    <text x="725" y="359" fill="#5b21b6" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Embeds</text>

    <line x1="680" y1="305" x2="680" y2="355" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="680" y1="355" x2="680" y2="355" stroke="#1e3a8a" stroke-width="1.8"/>
    <text x="690" y="325" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold">1</text>

    <line x1="725" y1="380" x2="725" y2="430" stroke="#1e3a8a" stroke-width="1.8"/>
    <text x="735" y="410" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold">1</text>

    <!-- ENTITY 3: RAG_EMBEDDING -->
    <rect x="610" y="430" width="230" height="140" rx="6" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8" filter="url(#erShadow)"/>
    <rect x="610" y="430" width="230" height="28" rx="6" fill="#7c3aed"/>
    <text x="725" y="449" fill="#ffffff" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">RAG_EMBEDDING</text>
    <text x="622" y="478" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">PK  embedding_id: INTEGER</text>
    <text x="622" y="497" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">FK  transaction_id: INTEGER</text>
    <text x="622" y="516" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">    chunk_text: TEXT</text>
    <text x="622" y="535" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">    embedding_blob: BLOB (768-d)</text>
    <text x="622" y="554" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">    updated_at: TIMESTAMP</text>

    <!-- RELATIONSHIP 3: USER SETS BUDGET_GOAL -->
    <polygon points="150,305 195,280 240,305 195,330" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
    <text x="195" y="309" fill="#92400e" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold" text-anchor="middle">Sets</text>

    <line x1="150" y1="245" x2="150" y2="305" stroke="#1e3a8a" stroke-width="1.8"/>
    <text x="135" y="275" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold">1</text>

    <line x1="195" y1="330" x2="195" y2="430" stroke="#1e3a8a" stroke-width="1.8"/>
    <text x="205" y="400" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold">N</text>

    <!-- ENTITY 4: BUDGET_GOAL -->
    <rect x="80" y="430" width="220" height="140" rx="6" fill="#ffffff" stroke="#d97706" stroke-width="1.8" filter="url(#erShadow)"/>
    <rect x="80" y="430" width="220" height="28" rx="6" fill="#d97706"/>
    <text x="190" y="449" fill="#ffffff" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">BUDGET_GOAL</text>
    <text x="92" y="478" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">PK  goal_id: INTEGER</text>
    <text x="92" y="497" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">FK  user_id: INTEGER</text>
    <text x="92" y="516" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">    category: VARCHAR(50)</text>
    <text x="92" y="535" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">    monthly_limit: FLOAT</text>
    <text x="92" y="554" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">    alert_threshold: FLOAT</text>

    <!-- ENTITY 5: CATEGORY_RULE -->
    <rect x="345" y="430" width="220" height="140" rx="6" fill="#ffffff" stroke="#059669" stroke-width="1.8" filter="url(#erShadow)"/>
    <rect x="345" y="430" width="220" height="28" rx="6" fill="#059669"/>
    <text x="455" y="449" fill="#ffffff" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">CATEGORY_RULE</text>
    <text x="357" y="478" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">PK  rule_id: INTEGER</text>
    <text x="357" y="497" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">    pattern: VARCHAR(150)</text>
    <text x="357" y="516" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">    category: VARCHAR(50)</text>
    <text x="357" y="535" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">    priority: INTEGER</text>
    <text x="357" y="554" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">    is_active: BOOLEAN</text>

    <!-- Connector: Category Rule Classifies Transaction -->
    <path d="M 455 430 L 455 305 L 560 305" fill="none" stroke="#059669" stroke-width="1.5" stroke-dasharray="4 4"/>
    <text x="480" y="320" fill="#059669" font-family="Times New Roman, serif" font-size="8.5">Classifies (1:N)</text>
</svg>'''

def get_database_design_svg():
    return '''<svg viewBox="0 0 920 680" width="100%" height="680" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <marker id="db-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 9 5 L 0 9 z" fill="#1e3a8a"/>
        </marker>
        <filter id="dbShadow" x="-2%" y="-2%" width="104%" height="106%">
            <feDropShadow dx="1" dy="2" stdDeviation="2.5" flood-opacity="0.12"/>
        </filter>
    </defs>

    <rect width="920" height="680" fill="#f8fafc" rx="8"/>

    <text x="460" y="35" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="15" font-weight="bold" text-anchor="middle">
        RELATIONAL DATABASE DESIGN &amp; SCHEMA SPECIFICATION (SQLITE / SQLALCHEMY)
    </text>

    <!-- TABLE 1: transactions (Center Left) -->
    <g transform="translate(40, 60)" filter="url(#dbShadow)">
        <rect width="380" height="340" rx="6" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8"/>
        <rect width="380" height="32" rx="6" fill="#1e3a8a"/>
        <text x="190" y="21" fill="#ffffff" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">
            TABLE: transactions (Core Ledger Entity)
        </text>

        <!-- Column headers -->
        <rect y="32" width="380" height="24" fill="#f1f5f9"/>
        <text x="12" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Column Name</text>
        <text x="135" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Data Type</text>
        <text x="235" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Constraints &amp; Defaults</text>

        <!-- Rows -->
        <line x1="0" y1="56" x2="380" y2="56" stroke="#cbd5e1"/>
        <text x="12" y="75" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">id</text>
        <text x="135" y="75" fill="#334155" font-family="Times New Roman, serif" font-size="9">INTEGER</text>
        <text x="235" y="75" fill="#15803d" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">PK, AUTOINCREMENT</text>

        <line x1="0" y1="87" x2="380" y2="87" stroke="#e2e8f0"/>
        <text x="12" y="106" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">date</text>
        <text x="135" y="106" fill="#334155" font-family="Times New Roman, serif" font-size="9">VARCHAR(50)</text>
        <text x="235" y="106" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8.5">NOT NULL, ISO YYYY-MM-DD</text>

        <line x1="0" y1="118" x2="380" y2="118" stroke="#e2e8f0"/>
        <text x="12" y="137" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">description</text>
        <text x="135" y="137" fill="#334155" font-family="Times New Roman, serif" font-size="9">TEXT</text>
        <text x="235" y="137" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8.5">NOT NULL, Raw Statement</text>

        <line x1="0" y1="149" x2="380" y2="149" stroke="#e2e8f0"/>
        <text x="12" y="168" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">amount</text>
        <text x="135" y="168" fill="#334155" font-family="Times New Roman, serif" font-size="9">FLOAT</text>
        <text x="235" y="168" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8.5">NOT NULL, CHECK (amount &gt; 0)</text>

        <line x1="0" y1="180" x2="380" y2="180" stroke="#e2e8f0"/>
        <text x="12" y="199" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">type</text>
        <text x="135" y="199" fill="#334155" font-family="Times New Roman, serif" font-size="9">VARCHAR(20)</text>
        <text x="235" y="199" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8.5">CHECK ('DEBIT', 'CREDIT')</text>

        <line x1="0" y1="211" x2="380" y2="211" stroke="#e2e8f0"/>
        <text x="12" y="230" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">category</text>
        <text x="135" y="230" fill="#334155" font-family="Times New Roman, serif" font-size="9">VARCHAR(50)</text>
        <text x="235" y="230" fill="#475569" font-family="Times New Roman, serif" font-size="8.5">DEFAULT 'Uncategorized'</text>

        <line x1="0" y1="242" x2="380" y2="242" stroke="#e2e8f0"/>
        <text x="12" y="261" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">is_anomaly</text>
        <text x="135" y="261" fill="#334155" font-family="Times New Roman, serif" font-size="9">BOOLEAN</text>
        <text x="235" y="261" fill="#475569" font-family="Times New Roman, serif" font-size="8.5">DEFAULT 0 (False)</text>

        <line x1="0" y1="273" x2="380" y2="273" stroke="#e2e8f0"/>
        <text x="12" y="292" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">anomaly_score</text>
        <text x="135" y="292" fill="#334155" font-family="Times New Roman, serif" font-size="9">FLOAT</text>
        <text x="235" y="292" fill="#475569" font-family="Times New Roman, serif" font-size="8.5">DEFAULT 0.0 (Path score)</text>

        <line x1="0" y1="304" x2="380" y2="304" stroke="#e2e8f0"/>
        <text x="12" y="323" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">user_id</text>
        <text x="135" y="323" fill="#334155" font-family="Times New Roman, serif" font-size="9">INTEGER</text>
        <text x="235" y="323" fill="#1d4ed8" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">FK -&gt; users.id, DEFAULT 1</text>
    </g>

    <!-- TABLE 2: rag_embeddings (Top Right) -->
    <g transform="translate(500, 60)" filter="url(#dbShadow)">
        <rect width="380" height="215" rx="6" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8"/>
        <rect width="380" height="32" rx="6" fill="#7c3aed"/>
        <text x="190" y="21" fill="#ffffff" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">
            TABLE: rag_embeddings (Vector Cache)
        </text>

        <!-- Column headers -->
        <rect y="32" width="380" height="24" fill="#f5f3ff"/>
        <text x="12" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Column Name</text>
        <text x="135" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Data Type</text>
        <text x="235" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Constraints &amp; Semantics</text>

        <!-- Rows -->
        <line x1="0" y1="56" x2="380" y2="56" stroke="#ddd6fe"/>
        <text x="12" y="75" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">id</text>
        <text x="135" y="75" fill="#334155" font-family="Times New Roman, serif" font-size="9">INTEGER</text>
        <text x="235" y="75" fill="#15803d" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">PK, AUTOINCREMENT</text>

        <line x1="0" y1="87" x2="380" y2="87" stroke="#ede9fe"/>
        <text x="12" y="106" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">transaction_id</text>
        <text x="135" y="106" fill="#334155" font-family="Times New Roman, serif" font-size="9">INTEGER</text>
        <text x="235" y="106" fill="#1d4ed8" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">FK -&gt; transactions.id, UNIQUE</text>

        <line x1="0" y1="118" x2="380" y2="118" stroke="#ede9fe"/>
        <text x="12" y="137" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">chunk_text</text>
        <text x="135" y="137" fill="#334155" font-family="Times New Roman, serif" font-size="9">TEXT</text>
        <text x="235" y="137" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8.5">NOT NULL, Synthesized context</text>

        <line x1="0" y1="149" x2="380" y2="149" stroke="#ede9fe"/>
        <text x="12" y="168" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">embedding_blob</text>
        <text x="135" y="168" fill="#334155" font-family="Times New Roman, serif" font-size="9">BLOB</text>
        <text x="235" y="168" fill="#6b21a8" font-family="Times New Roman, serif" font-size="8.5">768-dim float32 array</text>

        <line x1="0" y1="180" x2="380" y2="180" stroke="#ede9fe"/>
        <text x="12" y="199" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">updated_at</text>
        <text x="135" y="199" fill="#334155" font-family="Times New Roman, serif" font-size="9">TIMESTAMP</text>
        <text x="235" y="199" fill="#475569" font-family="Times New Roman, serif" font-size="8.5">DEFAULT CURRENT_TIMESTAMP</text>
    </g>

    <!-- FOREIGN KEY CONNECTOR: transactions.id -> rag_embeddings.transaction_id -->
    <path d="M 420 135 L 460 135 L 460 165 L 500 165" fill="none" stroke="#1d4ed8" stroke-width="2" marker-end="url(#db-arrow)"/>
    <text x="465" y="152" fill="#1d4ed8" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">1:1 FK</text>

    <!-- TABLE 3: category_rules (Bottom Left) -->
    <g transform="translate(40, 440)" filter="url(#dbShadow)">
        <rect width="380" height="210" rx="6" fill="#ffffff" stroke="#059669" stroke-width="1.8"/>
        <rect width="380" height="32" rx="6" fill="#059669"/>
        <text x="190" y="21" fill="#ffffff" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">
            TABLE: category_rules (Tier-1 Regex Store)
        </text>

        <rect y="32" width="380" height="24" fill="#ecfdf5"/>
        <text x="12" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Column Name</text>
        <text x="135" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Data Type</text>
        <text x="235" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Constraints &amp; Notes</text>

        <line x1="0" y1="56" x2="380" y2="56" stroke="#a7f3d0"/>
        <text x="12" y="75" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">id</text>
        <text x="135" y="75" fill="#334155" font-family="Times New Roman, serif" font-size="9">INTEGER</text>
        <text x="235" y="75" fill="#15803d" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">PK, AUTOINCREMENT</text>

        <line x1="0" y1="87" x2="380" y2="87" stroke="#d1fae5"/>
        <text x="12" y="106" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">pattern</text>
        <text x="135" y="106" fill="#334155" font-family="Times New Roman, serif" font-size="9">VARCHAR(150)</text>
        <text x="235" y="106" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8.5">NOT NULL, Regex string</text>

        <line x1="0" y1="118" x2="380" y2="118" stroke="#d1fae5"/>
        <text x="12" y="137" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">category</text>
        <text x="135" y="137" fill="#334155" font-family="Times New Roman, serif" font-size="9">VARCHAR(50)</text>
        <text x="235" y="137" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8.5">NOT NULL, Target category</text>

        <line x1="0" y1="149" x2="380" y2="149" stroke="#d1fae5"/>
        <text x="12" y="168" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">priority</text>
        <text x="135" y="168" fill="#334155" font-family="Times New Roman, serif" font-size="9">INTEGER</text>
        <text x="235" y="168" fill="#475569" font-family="Times New Roman, serif" font-size="8.5">DEFAULT 1 (Evaluation order)</text>

        <line x1="0" y1="180" x2="380" y2="180" stroke="#d1fae5"/>
        <text x="12" y="199" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">is_active</text>
        <text x="135" y="199" fill="#334155" font-family="Times New Roman, serif" font-size="9">BOOLEAN</text>
        <text x="235" y="199" fill="#475569" font-family="Times New Roman, serif" font-size="8.5">DEFAULT 1 (Active toggle)</text>
    </g>

    <!-- TABLE 4: users & budget_goals (Bottom Right) -->
    <g transform="translate(500, 320)" filter="url(#dbShadow)">
        <rect width="380" height="330" rx="6" fill="#ffffff" stroke="#d97706" stroke-width="1.8"/>
        <rect width="380" height="32" rx="6" fill="#d97706"/>
        <text x="190" y="21" fill="#ffffff" font-family="Times New Roman, serif" font-size="12" font-weight="bold" text-anchor="middle">
            TABLE: users &amp; budget_goals (Settings Store)
        </text>

        <rect y="32" width="380" height="24" fill="#fffbeb"/>
        <text x="12" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Column Name</text>
        <text x="135" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Data Type</text>
        <text x="235" y="48" fill="#0f172a" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">Constraints &amp; Notes</text>

        <line x1="0" y1="56" x2="380" y2="56" stroke="#fde68a"/>
        <text x="12" y="75" fill="#0f172a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">id</text>
        <text x="135" y="75" fill="#334155" font-family="Times New Roman, serif" font-size="9">INTEGER</text>
        <text x="235" y="75" fill="#15803d" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">PK, AUTOINCREMENT</text>

        <line x1="0" y1="87" x2="380" y2="87" stroke="#fef3c7"/>
        <text x="12" y="106" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">username</text>
        <text x="135" y="106" fill="#334155" font-family="Times New Roman, serif" font-size="9">VARCHAR(50)</text>
        <text x="235" y="106" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8.5">NOT NULL, UNIQUE</text>

        <line x1="0" y1="118" x2="380" y2="118" stroke="#fef3c7"/>
        <text x="12" y="137" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">monthly_budget</text>
        <text x="135" y="137" fill="#334155" font-family="Times New Roman, serif" font-size="9">FLOAT</text>
        <text x="235" y="137" fill="#475569" font-family="Times New Roman, serif" font-size="8.5">Default spending cap</text>

        <line x1="0" y1="149" x2="380" y2="149" stroke="#fef3c7"/>
        <text x="12" y="168" fill="#0f172a" font-family="Times New Roman, serif" font-size="9">savings_target</text>
        <text x="135" y="168" fill="#334155" font-family="Times New Roman, serif" font-size="9">FLOAT</text>
        <text x="235" y="168" fill="#475569" font-family="Times New Roman, serif" font-size="8.5">Target % savings rate</text>

        <!-- Subtable divider -->
        <rect y="180" width="380" height="24" fill="#fef3c7"/>
        <text x="190" y="196" fill="#92400e" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold" text-anchor="middle">
            INDEXES &amp; PERFORMANCE OPTIMIZATIONS
        </text>

        <line x1="0" y1="204" x2="380" y2="204" stroke="#fde68a"/>
        <text x="12" y="223" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">idx_tx_date</text>
        <text x="135" y="223" fill="#475569" font-family="Times New Roman, serif" font-size="8">B-Tree on date</text>
        <text x="235" y="223" fill="#059669" font-family="Times New Roman, serif" font-size="8">Sub-millisecond timeseries queries</text>

        <line x1="0" y1="235" x2="380" y2="235" stroke="#fef3c7"/>
        <text x="12" y="254" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">idx_tx_category</text>
        <text x="135" y="254" fill="#475569" font-family="Times New Roman, serif" font-size="8">B-Tree on category</text>
        <text x="235" y="254" fill="#059669" font-family="Times New Roman, serif" font-size="8">Instant group-by aggregations</text>

        <line x1="0" y1="266" x2="380" y2="266" stroke="#fef3c7"/>
        <text x="12" y="285" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">idx_rag_tx</text>
        <text x="135" y="285" fill="#475569" font-family="Times New Roman, serif" font-size="8">Hash on transaction_id</text>
        <text x="235" y="285" fill="#059669" font-family="Times New Roman, serif" font-size="8">Instant RAG vector retrieval</text>

        <line x1="0" y1="297" x2="380" y2="297" stroke="#fef3c7"/>
        <text x="12" y="316" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">Journal Mode</text>
        <text x="135" y="316" fill="#475569" font-family="Times New Roman, serif" font-size="8">WAL (Write-Ahead Log)</text>
        <text x="235" y="316" fill="#059669" font-family="Times New Roman, serif" font-size="8">High-concurrency read/write</text>
    </g>
</svg>'''

def get_user_interface_design_svg():
    return '''<svg viewBox="0 0 960 920" width="100%" height="920" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <filter id="uiShadow" x="-2%" y="-2%" width="104%" height="106%">
            <feDropShadow dx="1" dy="3" stdDeviation="3" flood-opacity="0.15"/>
        </filter>
    </defs>

    <rect width="960" height="920" fill="#f1f5f9" rx="10"/>

    <!-- Browser Window Container -->
    <rect x="25" y="20" width="910" height="880" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="2" filter="url(#uiShadow)"/>

    <!-- Browser Top Bar -->
    <rect x="25" y="20" width="910" height="42" rx="8" fill="#f8fafc"/>
    <circle cx="50" cy="41" r="6" fill="#ef4444"/>
    <circle cx="70" cy="41" r="6" fill="#f59e0b"/>
    <circle cx="90" cy="41" r="6" fill="#10b981"/>

    <!-- URL Bar -->
    <rect x="130" y="28" width="600" height="26" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
    <text x="145" y="45" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold">&bull; https://</text>
    <text x="195" y="45" fill="#334155" font-family="-apple-system, sans-serif" font-size="10.5">localhost:8501 - SpendWise AI: Autonomous Financial Copilot</text>

    <!-- SIDEBAR (LEFT) -->
    <rect x="25" y="62" width="220" height="838" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
    
    <!-- Sidebar Branding -->
    <rect x="40" y="80" width="190" height="45" rx="6" fill="#1e3a8a"/>
    <text x="135" y="102" fill="#ffffff" font-family="Times New Roman, serif" font-size="13" font-weight="bold" text-anchor="middle">SPENDWISE AI</text>
    <text x="135" y="117" fill="#bfdbfe" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Financial Intelligence Copilot</text>

    <!-- Upload Statement Box -->
    <rect x="40" y="145" width="190" height="110" rx="6" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="4 4"/>
    <text x="135" y="175" fill="#2563eb" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">+ UPLOAD CSV</text>
    <text x="135" y="195" fill="#64748b" font-family="Times New Roman, serif" font-size="8.5" text-anchor="middle">Drag &amp; drop bank statement</text>
    <text x="135" y="210" fill="#64748b" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">Auto-detects delimiters &amp; format</text>
    <rect x="65" y="222" width="140" height="22" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
    <text x="135" y="237" fill="#1d4ed8" font-family="Times New Roman, serif" font-size="8" font-weight="bold" text-anchor="middle">bank_statement_nov.csv &check;</text>

    <!-- Run Audit Button -->
    <rect x="40" y="270" width="190" height="38" rx="6" fill="#2563eb"/>
    <text x="135" y="294" fill="#ffffff" font-family="Times New Roman, serif" font-size="11" font-weight="bold" text-anchor="middle">&blacktriangleright; RUN FULL AUDIT</text>

    <!-- Filters & Settings -->
    <text x="45" y="335" fill="#0f172a" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold">AUDIT CONTROLS:</text>
    <rect x="40" y="348" width="190" height="26" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="50" y="365" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">Date: Nov 01, 2026 - Nov 30, 2026</text>

    <rect x="40" y="382" width="190" height="26" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="50" y="399" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">Categories: All 14 Selected</text>

    <!-- System Status Badges in Sidebar -->
    <text x="45" y="445" fill="#0f172a" font-family="Times New Roman, serif" font-size="10" font-weight="bold">MICROSERVICE HEALTH:</text>
    <circle cx="52" cy="465" r="4" fill="#10b981"/>
    <text x="65" y="468" fill="#166534" font-family="Times New Roman, serif" font-size="8.5">FastAPI Backend: Online (:8000)</text>

    <circle cx="52" cy="485" r="4" fill="#10b981"/>
    <text x="65" y="488" fill="#166534" font-family="Times New Roman, serif" font-size="8.5">SQLite DB: Connected (ACID)</text>

    <circle cx="52" cy="505" r="4" fill="#10b981"/>
    <text x="65" y="508" fill="#166534" font-family="Times New Roman, serif" font-size="8.5">Gemini 2.5 Flash: Ready</text>

    <circle cx="52" cy="525" r="4" fill="#10b981"/>
    <text x="65" y="528" fill="#166534" font-family="Times New Roman, serif" font-size="8.5">RAG Vector Cache: 1,000 Embeds</text>

    <!-- MAIN DASHBOARD CONTENT AREA -->
    <!-- KPI CARDS ROW -->
    <rect x="260" y="75" width="150" height="65" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
    <text x="335" y="95" fill="#166534" font-family="Times New Roman, serif" font-size="9" font-weight="bold" text-anchor="middle">TOTAL CASH INFLOW</text>
    <text x="335" y="120" fill="#15803d" font-family="Times New Roman, serif" font-size="15" font-weight="bold" text-anchor="middle">$12,450.00</text>
    <text x="335" y="133" fill="#166534" font-family="Times New Roman, serif" font-size="7.5" text-anchor="middle">+8.2% vs last month</text>

    <rect x="425" y="75" width="150" height="65" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
    <text x="500" y="95" fill="#991b1b" font-family="Times New Roman, serif" font-size="9" font-weight="bold" text-anchor="middle">TOTAL CASH OUTFLOW</text>
    <text x="500" y="120" fill="#b91c1c" font-family="Times New Roman, serif" font-size="15" font-weight="bold" text-anchor="middle">$4,820.50</text>
    <text x="500" y="133" fill="#991b1b" font-family="Times New Roman, serif" font-size="7.5" text-anchor="middle">-4.1% vs last month</text>

    <rect x="590" y="75" width="150" height="65" rx="6" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.2"/>
    <text x="665" y="95" fill="#1e40af" font-family="Times New Roman, serif" font-size="9" font-weight="bold" text-anchor="middle">NET SAVINGS</text>
    <text x="665" y="120" fill="#1d4ed8" font-family="Times New Roman, serif" font-size="15" font-weight="bold" text-anchor="middle">+$7,629.50</text>
    <text x="665" y="133" fill="#1e40af" font-family="Times New Roman, serif" font-size="7.5" text-anchor="middle">Savings Rate: 61.3%</text>

    <rect x="755" y="75" width="165" height="65" rx="6" fill="#fffbeb" stroke="#fde68a" stroke-width="1.2"/>
    <text x="837" y="95" fill="#92400e" font-family="Times New Roman, serif" font-size="9" font-weight="bold" text-anchor="middle">ANOMALIES FLAGGED</text>
    <text x="837" y="120" fill="#b45309" font-family="Times New Roman, serif" font-size="15" font-weight="bold" text-anchor="middle">3 Outliers</text>
    <text x="837" y="133" fill="#92400e" font-family="Times New Roman, serif" font-size="7.5" text-anchor="middle">Action Required</text>

    <!-- MIDDLE ROW: TWO ANALYTICAL PANELS -->
    <!-- Donut Chart Box (Left) -->
    <rect x="260" y="152" width="315" height="175" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
    <text x="417" y="172" fill="#0f172a" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">
        EXPENSE CATEGORY BREAKDOWN
    </text>
    <!-- Donut SVG Mockup -->
    <circle cx="340" cy="245" r="48" fill="none" stroke="#2563eb" stroke-width="18" stroke-dasharray="140 160"/>
    <circle cx="340" cy="245" r="48" fill="none" stroke="#10b981" stroke-width="18" stroke-dasharray="60 240" stroke-dashoffset="-140"/>
    <circle cx="340" cy="245" r="48" fill="none" stroke="#f59e0b" stroke-width="18" stroke-dasharray="50 250" stroke-dashoffset="-200"/>
    <circle cx="340" cy="245" r="48" fill="none" stroke="#a855f7" stroke-width="18" stroke-dasharray="40 260" stroke-dashoffset="-250"/>
    <text x="340" y="249" fill="#0f172a" font-family="Times New Roman, serif" font-size="10" font-weight="bold" text-anchor="middle">Food 34%</text>

    <text x="425" y="215" fill="#2563eb" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">&bull; Food &amp; Dining: $1,642</text>
    <text x="425" y="235" fill="#10b981" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">&bull; Housing &amp; Rent: $1,200</text>
    <text x="425" y="255" fill="#f59e0b" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">&bull; Utilities &amp; Phone: $865</text>
    <text x="425" y="275" fill="#a855f7" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">&bull; Shopping: $720</text>
    <text x="425" y="295" fill="#64748b" font-family="Times New Roman, serif" font-size="8.5">&bull; Other: $393.50</text>

    <!-- Anomaly Table Box (Right) -->
    <rect x="590" y="152" width="330" height="175" rx="6" fill="#ffffff" stroke="#fca5a5" stroke-width="1.2"/>
    <rect x="590" y="152" width="330" height="26" rx="6" fill="#fef2f2"/>
    <text x="755" y="169" fill="#991b1b" font-family="Times New Roman, serif" font-size="10.5" font-weight="bold" text-anchor="middle">
        &bull; ANOMALY ALERTS (ISOLATION FOREST + Z-SCORE)
    </text>

    <text x="605" y="195" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">1. 2026-11-14: LUXURY CARTIER JEWELRY</text>
    <text x="620" y="209" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8">Amount: $1,450.00 | Category: Shopping | Z-Score: 4.2 (High Spike)</text>

    <text x="605" y="235" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">2. 2026-11-18: ADOBE CREATIVE CLOUD</text>
    <text x="620" y="249" fill="#b45309" font-family="Times New Roman, serif" font-size="8">Amount: $89.99 | Warning: Duplicate debit on same posting date!</text>

    <text x="605" y="275" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">3. 2026-11-22: ELECTRONICS WAREHOUSE</text>
    <text x="620" y="289" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8">Amount: $840.00 | Path Score: 0.74 (Unusual merchant node)</text>

    <!-- BOTTOM SECTION: CLAUDE-STYLE PINNED CHAT INTERFACE -->
    <rect x="260" y="340" width="660" height="540" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    
    <!-- Chat Header -->
    <rect x="260" y="340" width="660" height="32" rx="8" fill="#eff6ff"/>
    <text x="275" y="361" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="11" font-weight="bold">
        FINANCIAL ADVISORY AGENT (CLAUDE-STYLE PINNED CONVERSATION)
    </text>

    <!-- Upward Stacking Chat History Area -->
    <!-- Message 1: User -->
    <rect x="420" y="385" width="485" height="42" rx="10" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.2"/>
    <text x="435" y="403" fill="#1e3a8a" font-family="Times New Roman, serif" font-size="9" font-weight="bold">User:</text>
    <text x="435" y="417" fill="#1e293b" font-family="Times New Roman, serif" font-size="8.5">
        What subscriptions am I paying for this month, and how can I save $100?
    </text>

    <!-- Message 2: Assistant (SpendWise AI Grounded) -->
    <rect x="275" y="438" width="630" height="230" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#uiShadow)"/>
    <rect x="275" y="438" width="630" height="24" rx="10" fill="#f0fdf4"/>
    <text x="290" y="454" fill="#047857" font-family="Times New Roman, serif" font-size="9.5" font-weight="bold">
        SpendWise AI &bull; Hybrid Contextual RAG Verified
    </text>
    <text x="290" y="478" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5">
        Based on your verified ledger from November 2026, you have <strong>4 active recurring subscriptions</strong> totaling <strong>$349.97</strong>:
    </text>

    <!-- Table of Subscriptions -->
    <rect x="290" y="490" width="600" height="85" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
    <text x="305" y="508" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">&bull; Netflix 4K Premium:</text>
    <text x="500" y="508" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">$22.99 / mo (Billed on 4th)</text>
    <text x="700" y="508" fill="#059669" font-family="Times New Roman, serif" font-size="8">Status: Normal</text>

    <text x="305" y="528" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">&bull; Adobe Creative Cloud:</text>
    <text x="500" y="528" fill="#b91c1c" font-family="Times New Roman, serif" font-size="8.5">$89.99 / mo (&times;2 charges flagged!)</text>
    <text x="700" y="528" fill="#dc2626" font-family="Times New Roman, serif" font-size="8" font-weight="bold">DUPLICATE ALERT</text>

    <text x="305" y="548" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">&bull; Equinox Fitness Club:</text>
    <text x="500" y="548" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">$220.00 / mo (Billed on 1st)</text>
    <text x="700" y="548" fill="#059669" font-family="Times New Roman, serif" font-size="8">Status: Normal</text>

    <text x="305" y="568" fill="#0f172a" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">&bull; Spotify Family Plan:</text>
    <text x="500" y="568" fill="#334155" font-family="Times New Roman, serif" font-size="8.5">$16.99 / mo (Billed on 22nd)</text>
    <text x="700" y="568" fill="#059669" font-family="Times New Roman, serif" font-size="8">Status: Normal</text>

    <text x="290" y="595" fill="#15803d" font-family="Times New Roman, serif" font-size="8.5" font-weight="bold">
        Recommended Saving Actions (Net Savings: +$102.99 / month):
    </text>
    <text x="290" y="612" fill="#0f172a" font-family="Times New Roman, serif" font-size="8">
        1. <strong>Dispute Duplicate Debit:</strong> Request a refund of the $89.99 second Adobe debit posted on Nov 18.
    </text>
    <text x="290" y="628" fill="#0f172a" font-family="Times New Roman, serif" font-size="8">
        2. <strong>Downgrade Plan:</strong> Switching Netflix from 4K Premium ($22.99) to Standard ($15.49) saves an extra $7.50/mo.
    </text>
    <text x="290" y="650" fill="#64748b" font-family="Times New Roman, serif" font-size="7.5" font-style="italic">
        [Factual Grounding: 4 ledger items retrieved via BM25 + Gemini Dense Vectors, RRF score 0.0321, CRAG: Verified High Confidence]
    </text>

    <!-- Auto-scroll indicator -->
    <text x="590" y="730" fill="#94a3b8" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">
        [Conversation stacks upward automatically &bull; View remains anchored to latest message]
    </text>

    <!-- FIXED PINNED BOTTOM INPUT BAR (CLAUDE PATTERN) -->
    <rect x="280" y="805" width="620" height="52" rx="26" fill="#ffffff" stroke="#2563eb" stroke-width="2" filter="url(#uiShadow)"/>
    <text x="315" y="836" fill="#94a3b8" font-family="Times New Roman, serif" font-size="9.5">
        Ask a financial question about your ledger (e.g., Can I afford a $600 flight?)...
    </text>
    <!-- Send Button (Circle) -->
    <circle cx="875" cy="831" r="18" fill="#2563eb"/>
    <path d="M 868 831 L 880 824 L 880 838 z" fill="#ffffff"/>
    <text x="590" y="872" fill="#64748b" font-family="Times New Roman, serif" font-size="8" text-anchor="middle">
        Pinned Bottom Bar (st.chat_input) &bull; Remains stationary during chat history expansion
    </text>
</svg>'''

def main():
    DIAGRAMS_DIR.mkdir(parents=True, exist_ok=True)
    
    diagrams = [
        ("5.1_system_architecture.svg", get_system_architecture_svg(), "5.1 System Architecture"),
        ("5.2_context_diagram.svg", get_context_diagram_svg(), "5.2 Context Diagram"),
        ("5.3_use_case_diagram.svg", get_use_case_diagram_svg(), "5.3 Use Case Diagram"),
        ("5.4_activity_diagram.svg", get_activity_diagram_svg(), "5.4 Activity Diagram"),
        ("5.5_er_diagram.svg", get_er_diagram_svg(), "5.5 ER Diagram"),
        ("5.6_database_design.svg", get_database_design_svg(), "5.6 Database Design"),
        ("5.7_user_interface_design.svg", get_user_interface_design_svg(), "5.7 User Interface Design"),
    ]

    print("=" * 60)
    print("Generating Standalone High-Resolution SVGs...")
    print("=" * 60)

    for filename, svg_content, title in diagrams:
        filepath = DIAGRAMS_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"[+] Saved: {filename} ({title})")

    # Generate interactive HTML Gallery viewer
    viewer_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SpendWise AI - Chapter 5 Architecture &amp; System Diagrams</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Times New Roman', Times, serif;
            background: #f1f5f9;
            color: #0f172a;
            padding: 30px 20px;
        }
        .header {
            max-width: 1100px;
            margin: 0 auto 30px auto;
            text-align: center;
            background: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            border-left: 6px solid #1e3a8a;
        }
        .header h1 {
            font-size: 24pt;
            color: #1e3a8a;
            margin-bottom: 8px;
        }
        .header p {
            font-size: 13pt;
            color: #475569;
        }
        .nav-bar {
            max-width: 1100px;
            margin: 0 auto 30px auto;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }
        .nav-btn {
            background: #ffffff;
            color: #1e3a8a;
            border: 1px solid #cbd5e1;
            padding: 8px 16px;
            border-radius: 6px;
            font-family: inherit;
            font-size: 11pt;
            font-weight: bold;
            text-decoration: none;
            transition: all 0.2s;
        }
        .nav-btn:hover {
            background: #1e3a8a;
            color: #ffffff;
            border-color: #1e3a8a;
        }
        .diagram-card {
            max-width: 1100px;
            margin: 0 auto 40px auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }
        .diagram-title {
            font-size: 16pt;
            font-weight: bold;
            color: #1e3a8a;
            margin-bottom: 6px;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 8px;
        }
        .diagram-desc {
            font-size: 12pt;
            color: #475569;
            line-height: 1.6;
            margin-bottom: 20px;
            text-align: justify;
        }
        .svg-wrapper {
            width: 100%;
            overflow-x: auto;
            text-align: center;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 10px;
            background: #f8fafc;
        }
        .svg-wrapper svg {
            max-width: 100%;
            height: auto;
        }
        .actions-bar {
            margin-top: 15px;
            display: flex;
            justify-content: flex-end;
            gap: 15px;
        }
        .action-link {
            font-size: 11pt;
            color: #2563eb;
            text-decoration: none;
            font-weight: bold;
        }
        .action-link:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="header">
        <h1>SPENDWISE AI: CHAPTER 5 SYSTEM DESIGN DIAGRAMS</h1>
        <p>Complete High-Resolution HTML5 Vector Diagram Suite for PG Project Report (2026-2027)</p>
    </div>

    <div class="nav-bar">
        <a href="#d51" class="nav-btn">5.1 System Architecture</a>
        <a href="#d52" class="nav-btn">5.2 Context Diagram</a>
        <a href="#d53" class="nav-btn">5.3 Use Case Diagram</a>
        <a href="#d54" class="nav-btn">5.4 Activity Diagram</a>
        <a href="#d55" class="nav-btn">5.5 ER Diagram</a>
        <a href="#d56" class="nav-btn">5.6 Database Design</a>
        <a href="#d57" class="nav-btn">5.7 User Interface Design</a>
    </div>

    <!-- 5.1 System Architecture -->
    <div class="diagram-card" id="d51">
        <div class="diagram-title">Fig. 5.1 System Architecture &amp; Overall Workflow</div>
        <p class="diagram-desc">
            Illustrates the four-tier decoupled microservice architecture: Streamlit Presentation Tier (Claude-style chat UI &amp; KPI dashboard), FastAPI ASGI Gateway, Core Computational Engines (3-Tier Categorization Cascade, Isolation Forest Anomaly Engine, and 2026 Hybrid Contextual RAG), and SQLite Persistence with vector cache.
        </p>
        <div class="svg-wrapper">
            """ + get_system_architecture_svg() + """
        </div>
        <div class="actions-bar">
            <a href="5.1_system_architecture.svg" target="_blank" class="action-link">Open Standalone SVG &nearr;</a>
        </div>
    </div>

    <!-- 5.2 Context Diagram -->
    <div class="diagram-card" id="d52">
        <div class="diagram-title">Fig. 5.2 Level-0 Context Diagram</div>
        <p class="diagram-desc">
            Defines the high-level boundary of the SpendWise AI platform (Process 0.0) and all major data flows interacting with external entities: the End User, the Commercial Banking Export Gateway, the Google Gemini Cloud AI API, and the Local File Storage.
        </p>
        <div class="svg-wrapper">
            """ + get_context_diagram_svg() + """
        </div>
        <div class="actions-bar">
            <a href="5.2_context_diagram.svg" target="_blank" class="action-link">Open Standalone SVG &nearr;</a>
        </div>
    </div>

    <!-- 5.3 Use Case Diagram -->
    <div class="diagram-card" id="d53">
        <div class="diagram-title">Fig. 5.3 UML Use Case Diagram</div>
        <p class="diagram-desc">
            Models user and administrative interactions across the primary operational use cases of the SpendWise AI platform, illustrating relationships between End Users, System Auditors, and the Google Gemini AI service actor.
        </p>
        <div class="svg-wrapper">
            """ + get_use_case_diagram_svg() + """
        </div>
        <div class="actions-bar">
            <a href="5.3_use_case_diagram.svg" target="_blank" class="action-link">Open Standalone SVG &nearr;</a>
        </div>
    </div>

    <!-- 5.4 Activity Diagram -->
    <div class="diagram-card" id="d54">
        <div class="diagram-title">Fig. 5.4 UML Activity / State Machine Diagram</div>
        <p class="diagram-desc">
            Traces the operational workflow of transaction ingestion across swimlanes: Streamlit UI, FastAPI Controller, ML &amp; Anomaly Engine, and Database/RAG Layer. Covers delimiter sniffing, schema validation, Tier 1 regex matching, Tier 2 SGDClassifier, Tier 3 Gemini fallback, and Isolation Forest outlier scoring.
        </p>
        <div class="svg-wrapper">
            """ + get_activity_diagram_svg() + """
        </div>
        <div class="actions-bar">
            <a href="5.4_activity_diagram.svg" target="_blank" class="action-link">Open Standalone SVG &nearr;</a>
        </div>
    </div>

    <!-- 5.5 ER Diagram -->
    <div class="diagram-card" id="d55">
        <div class="diagram-title">Fig. 5.5 Entity-Relationship (ER) Diagram</div>
        <p class="diagram-desc">
            Details the conceptual data model of SpendWise AI, highlighting entities (USER, TRANSACTION, RAG_EMBEDDING, CATEGORY_RULE, BUDGET_GOAL), primary and foreign keys, and cardinalities (1:N and 1:1 relationships).
        </p>
        <div class="svg-wrapper">
            """ + get_er_diagram_svg() + """
        </div>
        <div class="actions-bar">
            <a href="5.5_er_diagram.svg" target="_blank" class="action-link">Open Standalone SVG &nearr;</a>
        </div>
    </div>

    <!-- 5.6 Database Design -->
    <div class="diagram-card" id="d56">
        <div class="diagram-title">Fig. 5.6 Relational Database Design &amp; Schema Specification</div>
        <p class="diagram-desc">
            Presents the physical table schemas for SQLite / SQLAlchemy ORM: the core transactions table, the rag_embeddings vector cache table (768-dim float blobs), category_rules table, and B-Tree indexing strategies for high-throughput queries.
        </p>
        <div class="svg-wrapper">
            """ + get_database_design_svg() + """
        </div>
        <div class="actions-bar">
            <a href="5.6_database_design.svg" target="_blank" class="action-link">Open Standalone SVG &nearr;</a>
        </div>
    </div>

    <!-- 5.7 User Interface Design -->
    <div class="diagram-card" id="d57">
        <div class="diagram-title">Fig. 5.7 User Interface Wireframe &amp; Layout Specification</div>
        <p class="diagram-desc">
            Comprehensive architectural wireframe of the Streamlit application (http://localhost:8501) featuring KPI metric cards, interactive category donut chart, outlier alert notifications, and the Claude-style pinned chat interface with auto-scrolling message stack and fixed bottom input bar.
        </p>
        <div class="svg-wrapper">
            """ + get_user_interface_design_svg() + """
        </div>
        <div class="actions-bar">
            <a href="5.7_user_interface_design.svg" target="_blank" class="action-link">Open Standalone SVG &nearr;</a>
        </div>
    </div>
</body>
</html>
"""

    viewer_file = DIAGRAMS_DIR / "view_diagrams.html"
    with open(viewer_file, "w", encoding="utf-8") as f:
        f.write(viewer_html)
    print(f"[+] Saved interactive gallery viewer: {viewer_file}")
    print("=" * 60)
    print("All 7 Diagrams Successfully Generated!")
    print("=" * 60)

if __name__ == "__main__":
    main()
