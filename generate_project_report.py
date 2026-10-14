# -*- coding: utf-8 -*-
"""
Master Generator Script for SpendWise AI PG Project Report.
Adheres strictly to:
'DEPARTMENT OF COMPUTER APPLICATIONS - HANDOUT FOR PG PROJECT REPORT-2026-2027'

Rules enforced:
1. Paper & Margins: Left 4 cm, Top 3 cm, Bottom 3 cm, Right 2 cm.
2. Font: Times New Roman, 12pt body, 1.5 line spacing, 5-space paragraph indent.
3. Headings: 14pt bold, Subheadings 13pt bold.
4. STRICT: No underlines and No colons (:) in any headings or subheadings.
5. Minimum number of pages: 60 pages.
6. Numbering:
   - Preliminary certificate pages (Title, Bonafide, Ack 1, Ack 2, Completion, Plagiarism): NO page numbers.
   - Preliminary front matter (TOC, Abstract, List of Tables, List of Figures): lower-case Roman numerals (vii, viii, ix, x...).
   - Chapter pages: Arabic numerals (1, 2, 3...).
7. Figures and Tables serially numbered (Fig. 1.1, Fig. 5.1... Table 1.1, Table 2.1...).
8. All images/diagrams generated in HTML5 (inline SVG vector graphics).
9. Bibliography strictly in alphabetical order of author surnames.
"""

import os
import re
import sys
from pathlib import Path

# Add project root to sys.path so modules import cleanly
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from report_generator.styles import REPORT_CSS
from report_generator.preliminary import get_preliminary_pages
from report_generator.chapter1 import get_chapter1_pages
from report_generator.chapter2 import get_chapter2_pages
from report_generator.chapter3 import get_chapter3_pages
from report_generator.chapter4 import get_chapter4_pages
from report_generator.chapter5 import get_chapter5_pages
from report_generator.chapter6 import get_chapter6_pages
from report_generator.chapter7 import get_chapter7_pages
from report_generator.chapter8 import get_chapter8_pages
from report_generator.chapter9 import get_chapter9_pages
from report_generator.chapter10 import get_chapter10_pages

OUTPUT_FILE = ROOT_DIR / "SPENDWISE_PG_PROJECT_REPORT.html"

def audit_headings(html_content: str):
    """
    Validates that no heading (h1, h2, h3, h4) contains colons (:) or underlines.
    """
    heading_pattern = re.compile(r'<(h[1-4])[^>]*>(.*?)</\1>', re.IGNORECASE | re.DOTALL)
    violations = []
    
    for match in heading_pattern.finditer(html_content):
        tag, text = match.group(1), match.group(2)
        # Strip internal tags like <br>
        clean_text = re.sub(r'<[^>]+>', ' ', text).strip()
        if ':' in clean_text:
            violations.append(f"Colon found in <{tag}>: '{clean_text}'")
        if '<u>' in text.lower() or 'text-decoration: underline' in text.lower():
            violations.append(f"Underline found in <{tag}>: '{clean_text}'")
            
    return violations

def build_full_report():
    print("=" * 70)
    print("SPENDWISE AI: PG PROJECT REPORT MASTER BUILDER (2026-2027)")
    print("=" * 70)

    # Gather Preliminary Pages
    prelim_pages = get_preliminary_pages()
    print(f"[+] Loaded {len(prelim_pages)} preliminary pages.")

    # Gather Chapter Pages
    chapter_groups = [
        ("Chapter 1: Introduction", get_chapter1_pages()),
        ("Chapter 2: Literature Survey", get_chapter2_pages()),
        ("Chapter 3: Software Requirement Analysis", get_chapter3_pages()),
        ("Chapter 4: System Analysis", get_chapter4_pages()),
        ("Chapter 5: System Design", get_chapter5_pages()),
        ("Chapter 6: System Implementation", get_chapter6_pages()),
        ("Chapter 7: Testing and Evaluation", get_chapter7_pages()),
        ("Chapter 8: Results and Conclusion", get_chapter8_pages()),
        ("Chapter 9: Appendices", get_chapter9_pages()),
        ("Chapter 10: Bibliography / References", get_chapter10_pages())
    ]

    all_chapter_pages = []
    for title, pages in chapter_groups:
        print(f"    - {title}: {len(pages)} pages")
        all_chapter_pages.extend(pages)

    total_prelim = len(prelim_pages)
    total_chapters = len(all_chapter_pages)
    grand_total_pages = total_prelim + total_chapters

    print(f"[+] Total Chapter Pages: {total_chapters}")
    print(f"[+] Grand Total Document Pages: {grand_total_pages}")

    # Enforce minimum page count requirement (>= 60 pages)
    if grand_total_pages < 60:
        raise ValueError(f"Requirement violation: Report has {grand_total_pages} pages, but minimum required is 60 pages!")

    # Stamp page numbers strictly into Arabic pages
    stamped_chapter_pages = []
    for idx, page_html in enumerate(all_chapter_pages):
        page_num = idx + 1
        # Replace page-footer content with exact page_num
        stamped_html = re.sub(
            r'<div class="page-footer">.*?</div>',
            f'<div class="page-footer">{page_num}</div>',
            page_html,
            flags=re.DOTALL
        )
        # Update data-page attribute
        stamped_html = re.sub(r'data-page=".*?"', f'data-page="{page_num}"', stamped_html)
        stamped_chapter_pages.append(stamped_html)

    # Combine all pages
    all_pages_html = "\n".join(prelim_pages) + "\n" + "\n".join(stamped_chapter_pages)

    # Audit for Heading Rules (strictly NO colons, NO underlines)
    violations = audit_headings(all_pages_html)
    if violations:
        print("[!] Warning: Heading guideline violations detected:")
        for v in violations:
            print(f"    * {v}")
        print("[*] Automatically cleansing heading violations...")
        # Auto-clean colons in headings
        def clean_heading(match):
            tag, inner = match.group(1), match.group(2)
            cleaned_inner = inner.replace(":", " -")
            cleaned_inner = re.sub(r'</?u>', '', cleaned_inner, flags=re.IGNORECASE)
            return f"<{tag}>{cleaned_inner}</{tag}>"

        all_pages_html = re.sub(r'<(h[1-4])[^>]*>(.*?)</\1>', clean_heading, all_pages_html, flags=re.IGNORECASE | re.DOTALL)
        # Re-check
        remaining = audit_headings(all_pages_html)
        if not remaining:
            print("[+] All headings verified: 100% free of colons and underlines.")
    else:
        print("[+] Heading check passed: No colons or underlines in any heading.")

    # Assemble Master HTML Document
    master_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SpendWise AI - PG Project Report (2026-2027)</title>
    <!-- MathJax for KaTeX/LaTeX Mathematical Rendering -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
{REPORT_CSS}
    </style>
</head>
<body>
    <div class="report-container">
{all_pages_html}
    </div>
</body>
</html>
"""

    # Write out master report file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(master_html)

    file_size_kb = os.path.getsize(OUTPUT_FILE) / 1024
    word_count = len(re.findall(r'\b\w+\b', master_html))

    print("=" * 70)
    print(f"[SUCCESS] Report successfully generated at:")
    print(f"          {OUTPUT_FILE}")
    print(f"[METRICS] Total Pages: {grand_total_pages} (Requirement: &ge; 60 pages &check;)")
    print(f"          Total Words: ~{word_count:,} words")
    print(f"          File Size:   {file_size_kb:.1f} KB")
    print("=" * 70)

if __name__ == "__main__":
    build_full_report()
