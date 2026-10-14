# -*- coding: utf-8 -*-
"""
Chapter 3 Module for PG Project Report - SpendWise AI
Sections:
Chapter 3 Software Requirement Analysis
3.1 Hardware Specification (Table 3.1)
3.2 Software Specification (Table 3.2)
3.3 Software / Tools and Their Features
"""

def get_chapter3_pages():
    pages = []

    # -------------------------------------------------------------
    # PAGE 11 (Report Page 11): Chapter 3 Title & 3.1 Hardware Specification
    # -------------------------------------------------------------
    page1 = """
    <div class="page page-arabic" data-page="11">
        <div class="page-content">
            <h1 class="chapter-title">CHAPTER 3<br>SOFTWARE REQUIREMENT ANALYSIS</h1>
            
            <h2 class="section-heading">3.1 Hardware Specification</h2>
            <p>
                The computational requirements for the development, training, and operational deployment of SpendWise AI were carefully analyzed to ensure high processing throughput, minimal inference latency, and cross-platform accessibility. Because SpendWise AI utilizes a tiered architecture—offloading dense semantic embeddings and few-shot reasoning to cloud-hosted APIs while executing deterministic rules, statistical machine learning models, and vector database operations locally—the local hardware footprint remains accessible on standard consumer workstations.
            </p>
            <p>
                Table 3.1 delineates both the minimum operational hardware requirements and the recommended engineering specifications utilized during platform development and stress testing.
            </p>

            <p class="table-caption">Table 3.1 Minimum and Recommended Hardware Specifications</p>
            <table class="academic-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Hardware Component</th>
                        <th style="width: 35%;">Minimum Specification</th>
                        <th style="width: 40%;">Recommended Development Specification</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Processor (CPU)</strong></td>
                        <td>Dual-Core 64-bit x86/ARM Processor @ 2.0 GHz</td>
                        <td>Intel Core i7-13700H / AMD Ryzen 7 7840HS (16 Cores, 24 Threads @ 3.8 GHz)</td>
                    </tr>
                    <tr>
                        <td><strong>Random Access Memory (RAM)</strong></td>
                        <td>8 GB DDR4 RAM @ 2400 MHz</td>
                        <td>16 GB / 32 GB DDR5 RAM @ 4800 MHz</td>
                    </tr>
                    <tr>
                        <td><strong>Mass Storage</strong></td>
                        <td>500 MB free storage for application files and SQLite DB</td>
                        <td>512 GB PCIe 4.0 NVMe Solid State Drive (Read: 5000 MB/s, Write: 4200 MB/s)</td>
                    </tr>
                    <tr>
                        <td><strong>Display Resolution</strong></td>
                        <td>1366 &times; 768 WXGA Standard Display</td>
                        <td>1920 &times; 1080 Full HD or Higher Display for Streamlit Dashboard</td>
                    </tr>
                    <tr>
                        <td><strong>Network Interface</strong></td>
                        <td>Standard Broadband Internet (1 Mbps) for API dispatch</td>
                        <td>High-Speed Dedicated Broadband (50 Mbps or higher, Low Latency &lt; 20 ms)</td>
                    </tr>
                    <tr>
                        <td><strong>Hardware Acceleration</strong></td>
                        <td>Not mandatory (CPU-based inference supported)</td>
                        <td>Dedicated GPU (NVIDIA RTX 4060) or NPU for batch vectorization (Optional)</td>
                    </tr>
                </tbody>
            </table>

            <p>
                The local CPU orchestrates asynchronous event loops, vectorized tabular computations via NumPy and Pandas, TF-IDF sparse matrix construction, and Isolation Forest tree evaluations. The memory footprint comfortably accommodates in-memory lexical BM25 indexes and cached vector arrays without swapping to disk.
            </p>
        </div>
        <div class="page-footer">11</div>
    </div>
    """
    pages.append(page1)

    # -------------------------------------------------------------
    # PAGE 12 (Report Page 12): 3.2 Software Specification & Table 3.2
    # -------------------------------------------------------------
    page2 = """
    <div class="page page-arabic" data-page="12">
        <div class="page-content">
            <h2 class="section-heading">3.2 Software Specification</h2>
            <p>
                The software environment was selected to maximize developer productivity, architectural modularity, runtime reliability, and asynchronous concurrency. The platform is implemented in Python, leveraging a microservices architecture that separates the REST API backend from the presentation interface.
            </p>
            <p>
                Table 3.2 outlines the software stack, programming languages, core libraries, and infrastructure environments employed in SpendWise AI.
            </p>

            <p class="table-caption">Table 3.2 Software Technology Stack Specifications</p>
            <table class="academic-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Layer / Component</th>
                        <th style="width: 40%;">Technology / Framework Selected</th>
                        <th style="width: 35%;">Version & Configuration</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Operating System</strong></td>
                        <td>Microsoft Windows 11 64-bit / Linux (Ubuntu 22.04 LTS)</td>
                        <td>x86_64 / ARM64 POSIX Compliant</td>
                    </tr>
                    <tr>
                        <td><strong>Core Language Runtime</strong></td>
                        <td>Python 3.14 Programming Language Runtime</td>
                        <td>Standard CPython 64-bit with Virtual Environment</td>
                    </tr>
                    <tr>
                        <td><strong>Backend Framework</strong></td>
                        <td>FastAPI High-Performance ASGI Web Framework</td>
                        <td>Version 0.141.1 with Uvicorn 0.52.3 ASGI Server</td>
                    </tr>
                    <tr>
                        <td><strong>Frontend Interface</strong></td>
                        <td>Streamlit Reactive Application Framework</td>
                        <td>Version 1.61.1 with Custom CSS Injection</td>
                    </tr>
                    <tr>
                        <td><strong>Relational Database & ORM</strong></td>
                        <td>SQLite Embedded Database Engine & SQLAlchemy</td>
                        <td>SQLAlchemy 2.0.52 ORM with Declarative Mapping</td>
                    </tr>
                    <tr>
                        <td><strong>Machine Learning & Statistics</strong></td>
                        <td>Scikit-learn, SciPy, and NumPy</td>
                        <td>Scikit-learn 1.9.0, SciPy 1.18.0, NumPy 2.5.2</td>
                    </tr>
                    <tr>
                        <td><strong>Generative AI & Embeddings</strong></td>
                        <td>Google GenAI SDK (Gemini 2.5 Flash, Text-Embedding-004)</td>
                        <td>google-genai Version 2.18.1 with HTTPX Transport</td>
                    </tr>
                    <tr>
                        <td><strong>Lexical Search & Retrieval</strong></td>
                        <td>Rank-BM25 (Okapi BM25 Implementation)</td>
                        <td>Version 0.2.2 with Token Normalization</td>
                    </tr>
                    <tr>
                        <td><strong>Tabular Data Processing</strong></td>
                        <td>Pandas High-Performance Data Analysis Toolkit</td>
                        <td>Version 3.0.5 with Fast Parquet/CSV Parsers</td>
                    </tr>
                    <tr>
                        <td><strong>Data Visualization</strong></td>
                        <td>Altair & Plotly Express Interactive Charting</td>
                        <td>Altair 6.2.2, Plotly 6.9.0</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="page-footer">12</div>
    </div>
    """
    pages.append(page2)

    # -------------------------------------------------------------
    # PAGE 13 (Report Page 13): 3.3 Software / Tools and Their Features
    # -------------------------------------------------------------
    page3 = """
    <div class="page page-arabic" data-page="13">
        <div class="page-content">
            <h2 class="section-heading">3.3 Software / Tools and Their Features</h2>
            <p>
                Each software tool and framework within the SpendWise AI technology stack was selected to satisfy specific architectural requirements:
            </p>
            <p>
                <strong>1. FastAPI and Uvicorn:</strong> FastAPI is a modern, asynchronous Web framework for building REST APIs with Python based on standard Python type hints. Built upon Starlette and Pydantic, FastAPI provides asynchronous request handling via standard <code>async / await</code> syntax, ensuring that non-blocking I/O operations (such as external Gemini API calls and database writes) execute concurrently without stalling worker threads. In SpendWise AI, FastAPI automatically generates interactive OpenAPI (Swagger) documentation, validates incoming JSON payloads, and handles file streaming for large CSV transaction uploads.
            </p>
            <p>
                <strong>2. Streamlit:</strong> Streamlit is an open-source Python framework designed for rapid development of data-centric web applications. In this project, Streamlit's reactive execution model is enhanced via custom CSS styling to realize a modern, Claude-style pinned conversational interface. Unlike traditional web applications requiring separate JavaScript frontends, Streamlit allows deep, direct integration with the local Python data pipeline while maintaining reactive session state across user interactions.
            </p>
            <p>
                <strong>3. SQLAlchemy ORM and SQLite:</strong> SQLite provides a self-contained, serverless, zero-configuration transactional SQL database engine. Coupled with SQLAlchemy 2.0's declarative Object Relational Mapping (ORM), the database abstraction layer provides ACID guarantees for financial ledger storage. It ensures atomicity during bulk transaction uploads, enforces schema constraints across financial entities, and maintains an optimized vector embedding cache table (<code>rag_embeddings</code>) for instant semantic vector retrieval.
            </p>
            <p>
                <strong>4. Scikit-learn Machine Learning Library:</strong> Scikit-learn provides robust, computationally efficient implementations of state-of-the-art machine learning algorithms. In SpendWise AI, scikit-learn fulfills two critical roles:
            </p>
            <ul>
                <li><em>TF-IDF Vectorization & SGDClassifier:</em> <code>TfidfVectorizer</code> extracts sub-word character n-grams (ranges 2-5) from merchant descriptions. <code>SGDClassifier</code> optimizes a linear classifier using modified Huber loss, outputting calibrated probability estimates.</li>
                <li><em>Isolation Forest Anomaly Detection:</em> <code>IsolationForest</code> builds an ensemble of isolation trees to identify multi-dimensional spending outliers without requiring labeled ground truth.</li>
            </ul>
        </div>
        <div class="page-footer">13</div>
    </div>
    """
    pages.append(page3)

    # -------------------------------------------------------------
    # PAGE 14 (Report Page 14): 3.3 Tools (cont.) Gemini & BM25
    # -------------------------------------------------------------
    page4 = """
    <div class="page page-arabic" data-page="14">
        <div class="page-content">
            <p>
                <strong>5. Google Gemini Generative AI Platform (google-genai SDK):</strong> Google's Gemini 2.5 Flash model and <code>text-embedding-004</code> represent cutting-edge foundation models optimized for low latency, long context windows, and complex reasoning. In SpendWise AI, the Gemini SDK is deployed in two specific modules:
            </p>
            <ul>
                <li><em>Tier 3 Categorization Fallback:</em> When a transaction description is ambiguous, a structured JSON prompt with few-shot examples guides Gemini 2.5 Flash to disambiguate the merchant category with near-perfect human accuracy.</li>
                <li><em>HyDE Expansion & Conversational Advisory:</em> Gemini generates hypothetical document contexts for financial queries and synthesizes final conversational advisory responses grounded in retrieved ledger records.</li>
            </ul>
            <p>
                <strong>6. Rank-BM25 Lexical Retrieval Engine:</strong> The <code>rank-bm25</code> library implements the Okapi BM25 probabilistic retrieval algorithm. In financial retrieval, dense semantic embeddings often fail on exact numeric amounts, specific account IDs, and truncated merchant acronyms. BM25 constructs an in-memory inverted index that computes term frequency and inverse document frequency, ensuring that exact token matches receive top priority during hybrid search.
            </p>
            <p>
                <strong>7. Pandas and NumPy Data Engineering:</strong> Pandas provides fast, flexible tabular data structures (DataFrames) optimized for financial timeseries manipulation. In SpendWise AI, Pandas handles CSV dialect detection, date normalization, chronological sorting, and group-by aggregations for category breakdowns and cash-flow trend visualizations. NumPy provides vectorized mathematical computations for Z-score normalization and Euclidean distance calculations.
            </p>
            <p>
                <strong>8. Plotly Express and Altair Visualizers:</strong> Interactive visualization libraries embedded directly into the Streamlit UI provide responsive donut charts, monthly spend velocity curves, and anomaly highlight scatter plots, transforming raw database records into clear visual financial insights.
            </p>
        </div>
        <div class="page-footer">14</div>
    </div>
    """
    pages.append(page4)

    return pages
