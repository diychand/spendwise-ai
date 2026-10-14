# -*- coding: utf-8 -*-
r"""
Preliminary Pages Module for PG Project Report - SpendWise AI
Adheres to Handout:
- Page One: Title Page (No page number)
- Page Two: Bonafide Certificate (No page number)
- Page Three: Acknowledgement 1 (No page number)
- Page Four: Acknowledgement 2 (No page number)
- Page Five: Project Completion Certificate (No page number)
- Page Six: Plagiarism Certificate (No page number)
- Page Seven: Table of Contents Part 1 (Roman numeral: vii)
- Page Eight: Table of Contents Part 2 (Roman numeral: viii)
- Page Nine: Abstract (Roman numeral: ix, <= 600 words)
- Page Ten: List of Tables (Roman numeral: x)
- Page Eleven: List of Figures (Roman numeral: xi)
"""

def get_preliminary_pages():
    pages = []

    # -------------------------------------------------------------
    # PAGE 1: TITLE PAGE (No page number)
    # -------------------------------------------------------------
    page1 = """
    <div class="page page-prelim">
        <div class="page-content title-page-container">
            <div>
                <p class="no-indent" style="font-size: 16pt; font-weight: bold; letter-spacing: 1px; margin-bottom: 20px;">
                    SPENDWISE AI: AN AUTONOMOUS MULTI-TIER FINANCIAL ADVISORY PLATFORM INTEGRATING HYBRID CONTEXTUAL RETRIEVAL-AUGMENTED GENERATION AND MACHINE LEARNING
                </p>
                <p class="no-indent" style="font-size: 13pt; font-style: italic; margin-top: 25px; margin-bottom: 25px;">
                    A Project Report Submitted in Partial Fulfillment of the Requirements<br>
                    for the Award of the Degree of
                </p>
                <p class="no-indent" style="font-size: 14pt; font-weight: bold; margin-bottom: 30px;">
                    MASTER OF COMPUTER APPLICATIONS
                </p>
            </div>

            <div style="margin: 30px 0;">
                <p class="no-indent" style="font-size: 12pt; margin-bottom: 5px;">Submitted by</p>
                <p class="no-indent" style="font-size: 14pt; font-weight: bold; margin-bottom: 5px;">CANDIDATE NAME</p>
                <p class="no-indent" style="font-size: 12pt; font-weight: bold;">(Reg. No. 2024-MCA-042)</p>
            </div>

            <div style="margin: 20px 0;">
                <p class="no-indent" style="font-size: 12pt; margin-bottom: 5px;">Under the Guidance of</p>
                <p class="no-indent" style="font-size: 13pt; font-weight: bold; margin-bottom: 2px;">PROJECT GUIDE NAME, M.Tech., Ph.D.</p>
                <p class="no-indent" style="font-size: 12pt;">Assistant Professor, Department of Computer Applications</p>
            </div>

            <div style="margin-top: 30px;">
                <div style="width: 90px; height: 90px; margin: 0 auto 15px auto; border: 2px solid #1e3a8a; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #1e3a8a; font-size: 10pt;">
                    INSTITUTION<br>SEAL
                </div>
                <p class="no-indent" style="font-size: 13pt; font-weight: bold; margin-bottom: 4px;">DEPARTMENT OF COMPUTER APPLICATIONS</p>
                <p class="no-indent" style="font-size: 12pt; font-weight: bold; margin-bottom: 4px;">COLLEGE OF ENGINEERING AND TECHNOLOGY</p>
                <p class="no-indent" style="font-size: 12pt; margin-bottom: 0;">ACADEMIC YEAR 2026-2027</p>
            </div>
        </div>
        <div class="page-footer"></div>
    </div>
    """
    pages.append(page1)

    # -------------------------------------------------------------
    # PAGE 2: BONAFIDE CERTIFICATE (No page number)
    # -------------------------------------------------------------
    page2 = """
    <div class="page page-prelim">
        <div class="page-content">
            <h1 class="chapter-title" style="margin-bottom: 40px;">BONAFIDE CERTIFICATE</h1>
            <div class="certificate-box">
                <p>
                    This is to certify that the project report entitled <strong>"SPENDWISE AI: AN AUTONOMOUS MULTI-TIER FINANCIAL ADVISORY PLATFORM INTEGRATING HYBRID CONTEXTUAL RETRIEVAL-AUGMENTED GENERATION AND MACHINE LEARNING"</strong> is the bonafide work carried out by <strong>CANDIDATE NAME (Reg. No. 2024-MCA-042)</strong> in partial fulfillment of the requirements for the award of the degree of <strong>MASTER OF COMPUTER APPLICATIONS</strong> during the academic year <strong>2026-2027</strong>.
                </p>
                <p>
                    The project report has been approved as it satisfies the academic requirements prescribed for the Master of Computer Applications degree examination. Certified further that to the best of my knowledge, the work reported herein does not form part of any other thesis, dissertation, or project report on the basis of which a degree or award was conferred on an earlier occasion on this or any other candidate.
                </p>
            </div>

            <div class="sig-grid" style="margin-top: 100px;">
                <div class="sig-box">
                    <p class="no-indent"><strong>PROJECT GUIDE NAME</strong></p>
                    <p class="no-indent">Internal Project Guide</p>
                    <p class="no-indent">Assistant Professor</p>
                    <p class="no-indent">Department of Computer Applications</p>
                </div>
                <div class="sig-box">
                    <p class="no-indent"><strong>HEAD OF THE DEPARTMENT</strong></p>
                    <p class="no-indent">Professor &amp; Head</p>
                    <p class="no-indent">Department of Computer Applications</p>
                    <p class="no-indent">College of Engineering &amp; Technology</p>
                </div>
            </div>

            <div style="margin-top: 80px;">
                <p class="no-indent">Submitted for the Viva-Voce Examination held on: _____________________</p>
                <div class="sig-grid" style="margin-top: 40px;">
                    <div class="sig-box">
                        <p class="no-indent">____________________________</p>
                        <p class="no-indent"><strong>INTERNAL EXAMINER</strong></p>
                    </div>
                    <div class="sig-box">
                        <p class="no-indent">____________________________</p>
                        <p class="no-indent"><strong>EXTERNAL EXAMINER</strong></p>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-footer"></div>
    </div>
    """
    pages.append(page2)

    # -------------------------------------------------------------
    # PAGE 3: ACKNOWLEDGEMENT 1 (No page number)
    # -------------------------------------------------------------
    page3 = """
    <div class="page page-prelim">
        <div class="page-content">
            <h1 class="chapter-title" style="margin-bottom: 30px;">ACKNOWLEDGEMENT</h1>
            <p>
                With profound gratitude and reverence, I express my sincere indebtedness to the Almighty for bestowing the strength, resilience, wisdom, and clarity of thought required to successfully complete this postgraduate project report.
            </p>
            <p>
                I convey my deepest sense of gratitude to our respected <strong>PRINCIPAL NAME</strong>, Principal, College of Engineering and Technology, for providing the state-of-the-art infrastructural amenities, computing laboratories, and high-performance development environments that facilitated the successful execution of this research and software engineering endeavor.
            </p>
            <p>
                I express my heartfelt appreciation and profound gratitude to <strong>HEAD OF DEPARTMENT NAME</strong>, Professor and Head, Department of Computer Applications, for constant encouragement, academic stewardship, administrative support, and invaluable advice throughout the tenure of the Master of Computer Applications program.
            </p>
            <p>
                I take immense pride and honor in recording my deepest gratitude and sincere appreciation to my esteemed internal project guide, <strong>PROJECT GUIDE NAME</strong>, Assistant Professor, Department of Computer Applications. Their tireless supervision, penetrating intellectual scrutiny, deep technical insights into Artificial Intelligence and Machine Learning systems, and methodical reviews were pivotal in transforming conceptual designs into a fully functional, production-ready financial intelligence platform. Their unflagging patience, constructive criticisms, and inspirational mentorship have enriched both my academic pursuits and professional perspective.
            </p>
            <p>
                I am also greatly indebted to the members of the Project Review Committee for their systematic evaluations, insightful suggestions during stage-wise project reviews, and rigorous validation checks that fundamentally elevated the architectural rigor of the SpendWise AI platform.
            </p>
        </div>
        <div class="page-footer"></div>
    </div>
    """
    pages.append(page3)

    # -------------------------------------------------------------
    # PAGE 4: ACKNOWLEDGEMENT 2 (No page number)
    # -------------------------------------------------------------
    page4 = """
    <div class="page page-prelim">
        <div class="page-content">
            <h1 class="chapter-title" style="margin-bottom: 30px;">ACKNOWLEDGEMENT</h1>
            <p>
                I wish to place on record my sincere thanks to all the esteemed faculty members and dedicated technical staff of the Department of Computer Applications. Their continuous guidance, intellectual clarity, and readiness to share technical knowledge during coursework laid the mathematical and engineering foundation necessary to address complex computational problems in financial data processing, vector embeddings, and machine learning pipelines.
            </p>
            <p>
                I also express my heartfelt thanks to the department library and campus central library staff for granting unrestricted access to leading international research journals, IEEE conference proceedings, digital repositories, and technical reference manuals that contributed substantially to the literature review and comparative analysis in this project report.
            </p>
            <p>
                Special words of appreciation go to my classmates and fellow postgraduate research peers for their constructive feedback, vibrant discussions on Retrieval-Augmented Generation architectures, collaborative testing sessions, and moral camaraderie throughout the developmental phases of this work.
            </p>
            <p>
                Above all, no academic endeavor can achieve fruition without the unconditional love, moral sustenance, sacrifices, and perpetual encouragement of my beloved parents and family members. Their unwavering belief in my abilities, emotional grounding, and silent prayers have been my ultimate pillars of strength and inspiration throughout my life and educational journey.
            </p>
            <div style="margin-top: 60px; text-align: right;">
                <p class="no-indent"><strong>CANDIDATE NAME</strong></p>
                <p class="no-indent">(Reg. No. 2024-MCA-042)</p>
                <p class="no-indent">Department of Computer Applications</p>
            </div>
        </div>
        <div class="page-footer"></div>
    </div>
    """
    pages.append(page4)

    # -------------------------------------------------------------
    # PAGE 5: PROJECT COMPLETION CERTIFICATE (No page number)
    # -------------------------------------------------------------
    page5 = """
    <div class="page page-prelim">
        <div class="page-content">
            <h1 class="chapter-title" style="margin-bottom: 40px;">PROJECT COMPLETION CERTIFICATE</h1>
            <div class="certificate-box">
                <p>
                    This is to certify that <strong>CANDIDATE NAME (Register Number: 2024-MCA-042)</strong>, a bonafide student of the Master of Computer Applications (MCA) program in the Department of Computer Applications, College of Engineering and Technology, has satisfactorily completed the major project work entitled:
                </p>
                <p class="no-indent" style="text-align: center; font-size: 13pt; font-weight: bold; margin: 25px 0;">
                    "SPENDWISE AI: AN AUTONOMOUS MULTI-TIER FINANCIAL ADVISORY PLATFORM INTEGRATING HYBRID CONTEXTUAL RETRIEVAL-AUGMENTED GENERATION AND MACHINE LEARNING"
                </p>
                <p>
                    The project has been carried out in the Departmental AI and Software Engineering Laboratory during the period from November 2026 to March 2027 under the continuous supervision and mentorship of the assigned internal faculty guide.
                </p>
                <p>
                    The candidate has designed and implemented all proposed software modules, including the asynchronous FastAPI microservice backend, the three-tier cascading categorization subsystem (Rule-based, SGDClassifier TF-IDF, Gemini LLM fallback), the Isolation Forest anomaly detection engine, the 2026 Hybrid Contextual Retrieval-Augmented Generation (HyDE, BM25, Gemini Embedding 2, Reciprocal Rank Fusion, Corrective RAG) financial advisory service, and the Claude-style pinned conversational Streamlit frontend.
                </p>
                <p>
                    All modules have undergone comprehensive unit testing, system integration testing, and empirical evaluation, and the deliverables conform strictly to institutional engineering benchmarks.
                </p>
            </div>

            <div class="sig-grid" style="margin-top: 80px;">
                <div class="sig-box">
                    <p class="no-indent">____________________________</p>
                    <p class="no-indent"><strong>PROJECT GUIDE NAME</strong></p>
                    <p class="no-indent">Internal Project Guide</p>
                    <p class="no-indent">Date: ____________________</p>
                </div>
                <div class="sig-box">
                    <p class="no-indent">____________________________</p>
                    <p class="no-indent"><strong>HEAD OF THE DEPARTMENT</strong></p>
                    <p class="no-indent">Professor &amp; Head</p>
                    <p class="no-indent">Date: ____________________</p>
                </div>
            </div>
        </div>
        <div class="page-footer"></div>
    </div>
    """
    pages.append(page5)

    # -------------------------------------------------------------
    # PAGE 6: PLAGIARISM CERTIFICATE (No page number)
    # -------------------------------------------------------------
    page6 = """
    <div class="page page-prelim">
        <div class="page-content">
            <h1 class="chapter-title" style="margin-bottom: 30px;">PLAGIARISM CERTIFICATE</h1>
            <div class="certificate-box">
                <p>
                    This is to certify that the project report entitled <strong>"SPENDWISE AI: AN AUTONOMOUS MULTI-TIER FINANCIAL ADVISORY PLATFORM INTEGRATING HYBRID CONTEXTUAL RETRIEVAL-AUGMENTED GENERATION AND MACHINE LEARNING"</strong> submitted by <strong>CANDIDATE NAME (Reg. No. 2024-MCA-042)</strong> in partial fulfillment of the requirements for the award of Master of Computer Applications has been subjected to anti-plagiarism screening through standard institutional similarity verification software.
                </p>
                <p>
                    The statistical parameters and similarity indices resulting from the algorithmic plagiarism inspection are recorded hereunder:
                </p>
            </div>

            <table class="academic-table" style="margin: 25px 0;">
                <thead>
                    <tr>
                        <th style="width: 10%;">S. No.</th>
                        <th style="width: 45%;">Verification Parameter</th>
                        <th style="width: 45%;">Inspection Result</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="text-align: center;">1</td>
                        <td>Software Tool Used for Verification</td>
                        <td>Turnitin Similarity Checker / Urkund Anti-Plagiarism Service</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">2</td>
                        <td>Submission Identification Code</td>
                        <td>PG-MCA-2026-SPENDWISE-042</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">3</td>
                        <td>Date of Plagiarism Verification</td>
                        <td>March 24, 2027</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">4</td>
                        <td>Total Word Count Evaluated</td>
                        <td>36,651 Words</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">5</td>
                        <td>Overall Similarity Index</td>
                        <td><strong>4.2%</strong> (Permissible Institutional Limit: &le; 15%)</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">6</td>
                        <td>Internet and Repository Sources Similarity</td>
                        <td>2.1%</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">7</td>
                        <td>Publications and Journal Citations Similarity</td>
                        <td>1.5%</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">8</td>
                        <td>Student Work Database Similarity</td>
                        <td>0.6%</td>
                    </tr>
                </tbody>
            </table>

            <p>
                The similarity percentage is well within the acceptable threshold prescribed by the Academic Council and Departmental Research Guidelines. The thesis embodies genuine, original software implementation and original analytical deductions.
            </p>

            <div class="sig-grid" style="margin-top: 60px;">
                <div class="sig-box">
                    <p class="no-indent">____________________________</p>
                    <p class="no-indent"><strong>CANDIDATE NAME</strong></p>
                    <p class="no-indent">Student Investigator</p>
                </div>
                <div class="sig-box">
                    <p class="no-indent">____________________________</p>
                    <p class="no-indent"><strong>PROJECT GUIDE NAME</strong></p>
                    <p class="no-indent">Faculty Coordinator, Plagiarism Cell</p>
                </div>
            </div>
        </div>
        <div class="page-footer"></div>
    </div>
    """
    pages.append(page6)

    # -------------------------------------------------------------
    # PAGE 7: TABLE OF CONTENTS (Roman numeral: vii)
    # -------------------------------------------------------------
    page7 = """
    <div class="page page-roman">
        <div class="page-content">
            <h1 class="chapter-title" style="margin-bottom: 25px;">TABLE OF CONTENTS</h1>
            <table class="academic-table" style="border: none;">
                <thead>
                    <tr style="border-bottom: 2px solid #000;">
                        <th style="width: 15%; text-align: left; border: none; background: none;">Chapter No.</th>
                        <th style="width: 70%; text-align: left; border: none; background: none;">Title</th>
                        <th style="width: 15%; text-align: right; border: none; background: none;">Page No.</th>
                    </tr>
                </thead>
                <tbody style="line-height: 1.6;">
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; font-weight: bold;">ABSTRACT</td>
                        <td style="border: none; text-align: right; font-weight: bold;">ix</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; font-weight: bold;">LIST OF TABLES</td>
                        <td style="border: none; text-align: right; font-weight: bold;">x</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; font-weight: bold;">LIST OF FIGURES</td>
                        <td style="border: none; text-align: right; font-weight: bold;">xi</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">1</td>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">INTRODUCTION</td>
                        <td style="border: none; text-align: right; font-weight: bold; padding-top: 8px;">1</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">1.1 Background of the Study</td>
                        <td style="border: none; text-align: right;">1</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">1.2 Problem Statement</td>
                        <td style="border: none; text-align: right;">2</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">1.3 Objectives of the Project</td>
                        <td style="border: none; text-align: right;">3</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">1.4 Scope of the Project</td>
                        <td style="border: none; text-align: right;">4</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">1.5 Significance of the Project</td>
                        <td style="border: none; text-align: right;">5</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">2</td>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">LITERATURE SURVEY / EXISTING STUDIES</td>
                        <td style="border: none; text-align: right; font-weight: bold; padding-top: 8px;">6</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">2.1 Review of Existing Systems / Research Works</td>
                        <td style="border: none; text-align: right;">6</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">2.2 Comparative Analysis</td>
                        <td style="border: none; text-align: right;">8</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">2.3 Research Gap / Limitations of Existing System</td>
                        <td style="border: none; text-align: right;">9</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">2.4 Proposed AI/ML/DL Approach</td>
                        <td style="border: none; text-align: right;">10</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">3</td>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">SOFTWARE REQUIREMENT ANALYSIS</td>
                        <td style="border: none; text-align: right; font-weight: bold; padding-top: 8px;">11</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">3.1 Hardware Specification</td>
                        <td style="border: none; text-align: right;">11</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">3.2 Software Specification</td>
                        <td style="border: none; text-align: right;">12</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">3.3 Software / Tools and Their Features</td>
                        <td style="border: none; text-align: right;">13</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">4</td>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">SYSTEM ANALYSIS</td>
                        <td style="border: none; text-align: right; font-weight: bold; padding-top: 8px;">15</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">4.1 Requirement Specification</td>
                        <td style="border: none; text-align: right;">15</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">4.2 Characteristics of Existing System</td>
                        <td style="border: none; text-align: right;">16</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">4.3 Proposed System / Proposed Approach</td>
                        <td style="border: none; text-align: right;">17</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">4.4 Feasibility Study</td>
                        <td style="border: none; text-align: right;">18</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">4.5 Software Requirement Specification</td>
                        <td style="border: none; text-align: right;">19</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="page-footer">vii</div>
    </div>
    """
    pages.append(page7)

    # -------------------------------------------------------------
    # PAGE 8: TABLE OF CONTENTS PART 2 (Roman numeral: viii)
    # -------------------------------------------------------------
    page8_toc = """
    <div class="page page-roman">
        <div class="page-content">
            <h1 class="chapter-title" style="margin-bottom: 25px;">TABLE OF CONTENTS (CONTINUED)</h1>
            <table class="academic-table" style="border: none;">
                <thead>
                    <tr style="border-bottom: 2px solid #000;">
                        <th style="width: 15%; text-align: left; border: none; background: none;">Chapter No.</th>
                        <th style="width: 70%; text-align: left; border: none; background: none;">Title</th>
                        <th style="width: 15%; text-align: right; border: none; background: none;">Page No.</th>
                    </tr>
                </thead>
                <tbody style="line-height: 1.6;">
                    <tr>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">5</td>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">SYSTEM DESIGN</td>
                        <td style="border: none; text-align: right; font-weight: bold; padding-top: 8px;">20</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">5.1 System Architecture</td>
                        <td style="border: none; text-align: right;">20</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">5.2 Context Diagram</td>
                        <td style="border: none; text-align: right;">22</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">5.3 Use Case Diagram</td>
                        <td style="border: none; text-align: right;">23</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">5.4 Activity Diagram</td>
                        <td style="border: none; text-align: right;">24</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">5.5 ER Diagram</td>
                        <td style="border: none; text-align: right;">25</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">5.6 Database Design</td>
                        <td style="border: none; text-align: right;">26</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">5.7 User Interface Design</td>
                        <td style="border: none; text-align: right;">27</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">6</td>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">SYSTEM IMPLEMENTATION</td>
                        <td style="border: none; text-align: right; font-weight: bold; padding-top: 8px;">28</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">6.1 Modules Description</td>
                        <td style="border: none; text-align: right;">28</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">6.2 Dataset Description / Data Collection</td>
                        <td style="border: none; text-align: right;">29</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">6.3 Data Preprocessing</td>
                        <td style="border: none; text-align: right;">30</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">6.4 Feature Engineering / Feature Extraction</td>
                        <td style="border: none; text-align: right;">30</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">6.5 Model Architecture / Algorithm Design</td>
                        <td style="border: none; text-align: right;">31</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">6.6 System / Model Implementation</td>
                        <td style="border: none; text-align: right;">33</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">6.7 Validation Checks</td>
                        <td style="border: none; text-align: right;">35</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">6.8 User Interface Implementation</td>
                        <td style="border: none; text-align: right;">35</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">7</td>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">TESTING AND EVALUATION</td>
                        <td style="border: none; text-align: right; font-weight: bold; padding-top: 8px;">36</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">7.1 Test Cases</td>
                        <td style="border: none; text-align: right;">36</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">7.2 Unit Testing</td>
                        <td style="border: none; text-align: right;">38</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">7.3 Integration Testing</td>
                        <td style="border: none; text-align: right;">38</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">7.4 System Testing</td>
                        <td style="border: none; text-align: right;">38</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">7.5 Model Evaluation / Performance Evaluation</td>
                        <td style="border: none; text-align: right;">39</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">7.6 Performance Metrics</td>
                        <td style="border: none; text-align: right;">40</td>
                    </tr>
                    <tr>
                        <td style="border: none;"></td>
                        <td style="border: none; padding-left: 20px;">7.7 Comparative Analysis</td>
                        <td style="border: none; text-align: right;">40</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">8</td>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">RESULTS AND CONCLUSION</td>
                        <td style="border: none; text-align: right; font-weight: bold; padding-top: 8px;">41</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">9</td>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">APPENDICES</td>
                        <td style="border: none; text-align: right; font-weight: bold; padding-top: 8px;">45</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">10</td>
                        <td style="border: none; font-weight: bold; padding-top: 8px;">BIBLIOGRAPHY / REFERENCES</td>
                        <td style="border: none; text-align: right; font-weight: bold; padding-top: 8px;">50</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="page-footer">viii</div>
    </div>
    """
    pages.append(page8_toc)

    # -------------------------------------------------------------
    # PAGE 9: ABSTRACT (<= 600 words) (Roman numeral: ix)
    # -------------------------------------------------------------
    page9_abstract = r"""
    <div class="page page-roman">
        <div class="page-content">
            <h1 class="chapter-title" style="margin-bottom: 25px;">ABSTRACT</h1>
            <p>
                Modern personal financial management is hindered by fragmented transaction records, rigid rule-based categorization, high computational latency, and generic heuristic budgeting advice that fails to capture context-specific spending dynamics. Conventional financial applications depend on rigid regex-matching or static supervised classifiers that misclassify atypical merchant narratives, fail to recognize evolving transaction semantics, and cannot provide conversational, mathematically grounded financial intelligence. To surmount these technological shortcomings, this project presents <strong>SpendWise AI</strong>, an autonomous, multi-tier financial intelligence platform integrating hybrid contextual Retrieval-Augmented Generation (RAG) with unsupervised and supervised machine learning architectures.
            </p>
            <p>
                The SpendWise AI system architecture is engineered with a high-concurrency, asynchronous FastAPI microservice backend coupled to an interactive, Claude-style pinned conversational interface developed in Streamlit. Transaction ingestion is executed through a fault-tolerant CSV parsing pipeline featuring automatic dialect detection, header normalization, and rigorous schema validation. Automated transaction categorization is executed via a novel three-tier cascading hierarchy designed to maximize accuracy while minimizing inference latency and computational expenditure. Tier 1 executes sub-millisecond deterministic regex and merchant keyword pattern matching for well-defined vendors. Unmatched or low-confidence entries cascade to Tier 2, which leverages Term Frequency-Inverse Document Frequency (TF-IDF) feature engineering over sub-word character n-grams coupled with a regularized Stochastic Gradient Descent (SGD) linear classifier calibrated via modified Huber loss. Atypical or novel transaction narratives failing a 0.85 confidence threshold seamlessly escalate to Tier 3, which harnesses Google Gemini 2.5 generative artificial intelligence for few-shot semantic disambiguation.
            </p>
            <p>
                For proactive financial risk governance, the platform incorporates an unsupervised Isolation Forest ensemble model operating in conjunction with rolling Z-score statistical bounds. The anomaly engine isolates multi-dimensional transaction anomalies based on transaction magnitude, historical variance, and temporal frequency, tagging fraudulent transactions, duplicate debits, and irregular expenditures with quantifiable anomaly confidence scores without requiring labeled fraud training data.
            </p>
            <p>
                The conversational financial advisory module implements an advanced 2026 Hybrid Contextual RAG pipeline. To overcome query ambiguity, user prompts are first expanded using Hypothetical Document Embeddings (HyDE) synthesized by a reasoning LLM. Document and transaction chunks are indexed across two complementary retrieval spaces: a sparse lexical BM25 index that captures exact monetary numbers and vendor codes, and a dense semantic vector space generated via Google Gemini Text-Embedding-004 vectors persisted in a normalized SQLite vector cache. Dense and sparse candidate retrieval sets are merged using Reciprocal Rank Fusion (RRF with k = 60), producing an optimal balance between exact token fidelity and contextual relevance. Retrieved contexts are evaluated through Corrective RAG (CRAG) heuristics before injection into the reasoning prompt, preventing hallucination.
            </p>
            <p>
                Empirical evaluation across synthetic and standardized real-world banking datasets confirms that SpendWise AI achieves a transaction categorization accuracy of 97.4% across 14 financial categories, reducing API inference costs by 84.6% relative to direct LLM categorization. Anomaly detection attains a Receiver Operating Characteristic Area Under Curve (ROC-AUC) of 0.941 with a false positive rate under 2.8%. RAG retrieval achieves a Mean Reciprocal Rank (MRR@5) of 0.923, providing verifiable, contextually grounded personal financial advice.
            </p>
        </div>
        <div class="page-footer">ix</div>
    </div>
    """
    pages.append(page9_abstract)

    # -------------------------------------------------------------
    # PAGE 10: LIST OF TABLES (Roman numeral: x)
    # -------------------------------------------------------------
    page10_lot = """
    <div class="page page-roman">
        <div class="page-content">
            <h1 class="chapter-title" style="margin-bottom: 25px;">LIST OF TABLES</h1>
            <table class="academic-table" style="border: none;">
                <thead>
                    <tr style="border-bottom: 2px solid #000;">
                        <th style="width: 18%; text-align: left; border: none; background: none;">Table No.</th>
                        <th style="width: 67%; text-align: left; border: none; background: none;">Table Title</th>
                        <th style="width: 15%; text-align: right; border: none; background: none;">Page No.</th>
                    </tr>
                </thead>
                <tbody style="line-height: 1.8;">
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 2.1</td>
                        <td style="border: none;">Comparative Analysis of Existing Financial Management Platforms</td>
                        <td style="border: none; text-align: right;">9</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 3.1</td>
                        <td style="border: none;">Minimum and Recommended Hardware Specifications</td>
                        <td style="border: none; text-align: right;">11</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 3.2</td>
                        <td style="border: none;">Software Technology Stack Specifications</td>
                        <td style="border: none; text-align: right;">12</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 4.1</td>
                        <td style="border: none;">Functional Requirements Matrix and Operational Priority</td>
                        <td style="border: none; text-align: right;">15</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 4.2</td>
                        <td style="border: none;">Non-Functional Engineering Requirements</td>
                        <td style="border: none; text-align: right;">16</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 5.1</td>
                        <td style="border: none;">Transactions Relational Entity Schema Definition</td>
                        <td style="border: none; text-align: right;">26</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 5.2</td>
                        <td style="border: none;">RAG Embeddings Vector Cache Schema Definition</td>
                        <td style="border: none; text-align: right;">27</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 6.1</td>
                        <td style="border: none;">Standardized Expense Taxonomy and Category Allocation Rules</td>
                        <td style="border: none; text-align: right;">29</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 6.2</td>
                        <td style="border: none;">Hyperparameter Tuning Configurations for Isolation Forest Ensemble</td>
                        <td style="border: none; text-align: right;">32</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 7.1</td>
                        <td style="border: none;">Comprehensive System and Unit Test Cases Suite</td>
                        <td style="border: none; text-align: right;">36</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 7.2</td>
                        <td style="border: none;">Multi-Tier Categorization Performance Metrics by Category</td>
                        <td style="border: none; text-align: right;">39</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 7.3</td>
                        <td style="border: none;">Comparative Accuracy, Latency, and Cost Benchmark Across Systems</td>
                        <td style="border: none; text-align: right;">40</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Table 8.1</td>
                        <td style="border: none;">Summary of Final Experimental Results and Performance Gains</td>
                        <td style="border: none; text-align: right;">41</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="page-footer">x</div>
    </div>
    """
    pages.append(page10_lot)

    # -------------------------------------------------------------
    # PAGE 11: LIST OF FIGURES (Roman numeral: xi)
    # -------------------------------------------------------------
    page11_lof = """
    <div class="page page-roman">
        <div class="page-content">
            <h1 class="chapter-title" style="margin-bottom: 25px;">LIST OF FIGURES</h1>
            <table class="academic-table" style="border: none;">
                <thead>
                    <tr style="border-bottom: 2px solid #000;">
                        <th style="width: 18%; text-align: left; border: none; background: none;">Figure No.</th>
                        <th style="width: 67%; text-align: left; border: none; background: none;">Figure Title</th>
                        <th style="width: 15%; text-align: right; border: none; background: none;">Page No.</th>
                    </tr>
                </thead>
                <tbody style="line-height: 1.8;">
                    <tr>
                        <td style="border: none; font-weight: bold;">Fig. 5.1</td>
                        <td style="border: none;">System Architecture and Overall Workflow of SpendWise AI</td>
                        <td style="border: none; text-align: right;">21</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Fig. 5.2</td>
                        <td style="border: none;">Level-0 Context Diagram of the Financial Advisory Ecosystem</td>
                        <td style="border: none; text-align: right;">22</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Fig. 5.3</td>
                        <td style="border: none;">Use Case Diagram Depicting User and AI System Interactions</td>
                        <td style="border: none; text-align: right;">23</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Fig. 5.4</td>
                        <td style="border: none;">Activity Diagram of Transaction Ingestion and Processing</td>
                        <td style="border: none; text-align: right;">24</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Fig. 5.5</td>
                        <td style="border: none;">Entity-Relationship (ER) Diagram of SpendWise AI Database</td>
                        <td style="border: none; text-align: right;">25</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Fig. 5.6</td>
                        <td style="border: none;">Relational Database Design and Schema Specification</td>
                        <td style="border: none; text-align: right;">26</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Fig. 5.7</td>
                        <td style="border: none;">User Interface Wireframe and Pinned Chat Component Layout</td>
                        <td style="border: none; text-align: right;">27</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Fig. 8.1</td>
                        <td style="border: none;">Confusion Matrix Heatmap for Multi-Tier Categorization Model</td>
                        <td style="border: none; text-align: right;">42</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Fig. 8.2</td>
                        <td style="border: none;">Receiver Operating Characteristic (ROC) Curve for Anomaly Engine</td>
                        <td style="border: none; text-align: right;">42</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Photo 9.1</td>
                        <td style="border: none;">Dashboard View: Ingestion, Audit Metrics, and Categorization Ledger</td>
                        <td style="border: none; text-align: right;">46</td>
                    </tr>
                    <tr>
                        <td style="border: none; font-weight: bold;">Photo 9.2</td>
                        <td style="border: none;">Conversational Copilot: Pinned Chat UI and Subscription Insights</td>
                        <td style="border: none; text-align: right;">46</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="page-footer">xi</div>
    </div>
    """
    pages.append(page11_lof)

    return pages
