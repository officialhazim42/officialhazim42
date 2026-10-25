import os

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('scratch/rendered_section_04.md', 'r', encoding='utf-8') as f:
    cards_section = f.read()

# Replace badge
old_badge = 'https://img.shields.io/badge/VERIFIED_PROJECTS-10_Active-0284C7?style=for-the-badge" alt="10 Verified Projects"'
new_badge = 'https://img.shields.io/badge/VERIFIED_PROJECTS-11_Active-0284C7?style=for-the-badge" alt="11 Verified Projects"'

assert old_badge in readme, "old_badge not found in README.md"
readme = readme.replace(old_badge, new_badge)

start_marker = '<!-- ================================================================= -->\n<!-- PROJECT 01 — COMPLETE CARD: PDFHub'
end_marker = '<!-- PROJECT 10 — COMPLETE CARD: Deployment Dashboard'

p01_pos = readme.find(start_marker)
p10_pos = readme.find(end_marker)
table_end = readme.find('</table>', p10_pos) + len('</table>')

assert p01_pos != -1, "start_marker not found"
assert p10_pos != -1, "end_marker not found"

new_readme = readme[:p01_pos] + cards_section + readme[table_end:]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme)

print('README.md updated successfully!')
