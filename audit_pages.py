import re

with open(r'c:\spendwise-ai\SPENDWISE_PG_PROJECT_REPORT.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's count how many times <div class="page " or <div class="page- occurs
matches = list(re.finditer(r'<div class="page\s+([^"]+)"(?:\s+data-page="([^"]+)")?>', text))
print(f"Total page matches: {len(matches)}")
for idx, m in enumerate(matches):
    print(f"Match {idx+1}: class='{m.group(1)}', data-page='{m.group(2)}'")
