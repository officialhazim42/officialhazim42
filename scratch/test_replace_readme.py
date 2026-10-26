import os
import re

with open("README.md", "r", encoding="utf-8") as f:
    orig_readme = f.read()

# Verify section markers
assert "assets/section-projects.svg" in orig_readme
assert "assets/section-cyberguard.svg" in orig_readme
assert "assets/section-philosophy.svg" in orig_readme

# Find boundaries
p_sec4_start = orig_readme.find("<!-- ================================================================= -->\n<!-- PROJECT 01 — COMPLETE CARD:")
assert p_sec4_start != -1

p_sec5_start = orig_readme.find('<img src="assets/section-cyberguard.svg"')
assert p_sec5_start != -1

p_sec6_start = orig_readme.find('<img src="assets/section-philosophy.svg"')
assert p_sec6_start != -1

prefix = orig_readme[:p_sec4_start]
suffix = orig_readme[p_sec6_start:]

with open("scratch/preview_sec_04.md", "r", encoding="utf-8") as f:
    new_sec_04 = f.read()

with open("scratch/preview_sec_05.md", "r", encoding="utf-8") as f:
    new_sec_05 = f.read()

new_readme = prefix + new_sec_04 + "\n\n<br />\n\n" + new_sec_05 + "\n\n<br />\n\n" + suffix

with open("scratch/TEST_README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

print("scratch/TEST_README.md generated. Length:", len(new_readme))
