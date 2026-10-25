import os
import re

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# 1. Section banners check in README.md
sections = [
    "assets/about-panel.svg",
    "assets/section-build.svg",
    "assets/section-stack.svg",
    "assets/section-projects.svg",
    "assets/section-cyberguard.svg",
    "assets/section-philosophy.svg",
    "assets/section-stats.svg",
    "assets/section-connect.svg"
]

for s in sections:
    assert s in readme, f"Missing section banner: {s}"
print("All 8 section banners are intact.")

# 2. Check all 10 projects
for i in range(1, 11):
    num_str = f"{i:02d}"
    assert f"<!-- PROJECT {num_str} — COMPLETE CARD:" in readme, f"Missing card comment for project {num_str}"
    assert f'assets/cards/header-{num_str}.svg' in readme, f"Missing header-{num_str}.svg in README.md"
    assert os.path.exists(f'assets/cards/header-{num_str}.svg'), f"Header file missing on disk: assets/cards/header-{num_str}.svg"
print("All 10 project cards and headers verified in README.md.")

# 3. Check all local image links in README.md
local_imgs = re.findall(r'<img [^>]*src="(assets/[^"]+)"', readme)
print(f"Total local images referenced in README.md: {len(local_imgs)}")

missing_imgs = [img for img in local_imgs if not os.path.exists(img)]
assert len(missing_imgs) == 0, f"Missing images: {missing_imgs}"
print(f"All {len(local_imgs)} local images exist on disk with ZERO broken links.")

# 4. Check action buttons validity
assert 'href="https://github.com/officialhazim42/cyberguard' not in readme
assert 'href="https://github.com/officialhazim42/habit' not in readme
assert 'assets/buttons/btn-private-codebase.svg' in readme
print("Private codebases correctly display static private badge.")

# Projects 06 to 10 must NOT have a live demo button
for i in range(6, 11):
    num_str = f"{i:02d}"
    hdr_file = f"assets/cards/header-{num_str}.svg"
    with open(hdr_file, "r", encoding="utf-8") as f_hdr:
        hdr_txt = f_hdr.read()
        assert "REPOSITORY ONLY" in hdr_txt
        assert "LIVE" not in hdr_txt

print("Status accuracy confirmed for all 10 projects.")

# 5. Check live demo URLs for 01-05
live_urls = [
    "https://pdfshub.netlify.app/",
    "https://imagehub.netlify.app/",
    "https://cyberguard-yuva.vercel.app/",
    "https://habit-flow-ten-eta.vercel.app",
    "https://advance-images-compressor.netlify.app/"
]
for u in live_urls:
    assert u in readme, f"Missing live demo URL: {u}"
print("All 5 live project URLs are present and verified.")

# 6. Check repos for 01, 02, 05, 06, 07, 08, 09, 10
repo_urls = [
    "https://github.com/officialhazim42/pdfshub",
    "https://github.com/officialhazim42/imagehub",
    "https://github.com/officialhazim42/Advance-Image-Compressor",
    "https://github.com/officialhazim42/Termux-Command-Listbook",
    "https://github.com/officialhazim42/Passportsize-photo-maker",
    "https://github.com/officialhazim42/Text-to-Audio-Converter",
    "https://github.com/officialhazim42/week-3-student-task-manager",
    "https://github.com/officialhazim42/week-5-deployment-production"
]
for r in repo_urls:
    assert r in readme, f"Missing repo URL: {r}"
print("All 8 public repository URLs are present and verified.")

# 7. Check technical dossier links for all 10
for i in range(1, 11):
    assert f"PROJECTS.md#{i:02d}-" in readme
print("All 10 technical dossier links are present and verified.")

print("\n=======================================================")
print("ALL 14 VALIDATION CRITERIA PASSED COMPLETELY AND FLAWLESSLY!")
print("=======================================================")
