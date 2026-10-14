# -*- coding: utf-8 -*-
"""
CSS Styles for PG Project Report - SpendWise AI
Adheres strictly to the guidelines:
- Times New Roman font throughout
- Normal text: 12pt, 1.5 line spacing, 5-space paragraph indent
- Headings: 14pt (bold, no underlines, no colons)
- Subheadings: 13pt (bold, no underlines, no colons)
- Margins: Left 4 cm, Top 3 cm, Bottom 3 cm, Right 2 cm
- Page numbering at bottom-middle of each page
"""

REPORT_CSS = """
@page {
    size: A4 portrait;
    margin-left: 4cm;
    margin-top: 3cm;
    margin-bottom: 3cm;
    margin-right: 2cm;
    @bottom-center {
        content: counter(page);
        font-family: 'Times New Roman', Times, serif;
        font-size: 11pt;
    }
}

*, *::before, *::after {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    background-color: #f1f5f9;
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #111827;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

/* Screen Page Container Simulation */
.report-container {
    width: 100%;
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px 0;
}

.page {
    background: #ffffff;
    width: 210mm;
    min-height: 297mm;
    margin: 25px auto;
    padding-left: 40mm;   /* 4 cm Left margin */
    padding-right: 20mm;  /* 2 cm Right margin */
    padding-top: 30mm;    /* 3 cm Top margin */
    padding-bottom: 30mm; /* 3 cm Bottom margin */
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    position: relative;
    page-break-after: always;
    break-after: page;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.page-content {
    flex: 1 0 auto;
}

.page-footer {
    text-align: center;
    font-family: 'Times New Roman', Times, serif;
    font-size: 11pt;
    color: #374151;
    padding-top: 15px;
    margin-top: auto;
}

/* Headings: Strictly NO Underline, NO Colons */
h1.chapter-title {
    font-family: 'Times New Roman', Times, serif;
    font-size: 14pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin-top: 0;
    margin-bottom: 24px;
    line-height: 1.4;
    text-decoration: none !important;
}

h2.section-heading {
    font-family: 'Times New Roman', Times, serif;
    font-size: 14pt;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 12px;
    text-align: left;
    text-decoration: none !important;
}

h3.subsection-heading {
    font-family: 'Times New Roman', Times, serif;
    font-size: 13pt;
    font-weight: bold;
    margin-top: 16px;
    margin-bottom: 8px;
    text-align: left;
    text-decoration: none !important;
}

h4.subsubsection-heading {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    font-weight: bold;
    margin-top: 12px;
    margin-bottom: 6px;
    text-align: left;
    text-decoration: none !important;
}

p {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    text-align: justify;
    text-justify: inter-word;
    margin-top: 0;
    margin-bottom: 12px;
    text-indent: 5ch; /* Fresh paragraph commences after five spaces */
}

p.no-indent {
    text-indent: 0;
}

/* Tables */
table.academic-table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-family: 'Times New Roman', Times, serif;
    font-size: 11pt;
    line-height: 1.35;
}

table.academic-table th, table.academic-table td {
    border: 1px solid #1f2937;
    padding: 7px 10px;
    vertical-align: top;
}

table.academic-table th {
    background-color: #f3f4f6;
    font-weight: bold;
    text-align: center;
}

.table-caption {
    font-weight: bold;
    font-size: 11pt;
    margin-bottom: 6px;
    text-align: center;
}

/* Figures & HTML5 SVG Diagrams */
.figure-container {
    width: 100%;
    margin: 18px 0;
    text-align: center;
    page-break-inside: avoid;
}

.figure-container svg {
    max-width: 100%;
    height: auto;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    background-color: #ffffff;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.figure-caption {
    font-weight: bold;
    font-size: 11pt;
    margin-top: 8px;
    text-align: center;
}

/* Code Snippets */
pre.code-block {
    background-color: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #1e3a8a;
    padding: 12px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 9.5pt;
    line-height: 1.4;
    overflow-x: auto;
    white-space: pre-wrap;
    margin: 14px 0;
}

/* Lists */
ol, ul {
    margin-top: 6px;
    margin-bottom: 14px;
    padding-left: 28px;
}

li {
    font-size: 12pt;
    line-height: 1.5;
    margin-bottom: 6px;
    text-align: justify;
}

/* Preliminary Specific Styling */
.title-page-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
    text-align: center;
}

.certificate-box {
    margin-top: 20px;
    line-height: 1.8;
}

.sig-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    margin-top: 60px;
}

.sig-box {
    text-align: center;
    line-height: 1.3;
}

/* Print Stylesheet Overrides */
@media print {
    body {
        background-color: #ffffff;
    }
    .report-container {
        max-width: 100%;
        margin: 0;
        padding: 0;
    }
    .page {
        margin: 0;
        box-shadow: none;
        width: 100%;
        min-height: 100%;
        padding-left: 40mm !important;
        padding-right: 20mm !important;
        padding-top: 30mm !important;
        padding-bottom: 30mm !important;
        page-break-after: always;
        break-after: page;
    }
}
"""
