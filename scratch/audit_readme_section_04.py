import os
import re

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

with open("PROJECTS.md", "r", encoding="utf-8") as f:
    projects_md = f.read()

with open("portfolio/index.html", "r", encoding="utf-8") as f:
    portfolio = f.read()

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

# 2. Check all 11 projects in README.md
for i in range(1, 12):
    num_str = f"{i:02d}"
    assert f"<!-- PROJECT {num_str} — COMPLETE CARD:" in readme, f"Missing card comment for project {num_str}"
    assert f'assets/cards/header-{num_str}.svg' in readme, f"Missing header-{num_str}.svg in README.md"
    assert os.path.exists(f'assets/cards/header-{num_str}.svg'), f"Header file missing on disk: assets/cards/header-{num_str}.svg"
print("All 11 project cards and headers verified in README.md.")

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

# Projects 06 to 10 must have REPOSITORY ONLY
for i in range(6, 11):
    num_str = f"{i:02d}"
    hdr_file = f"assets/cards/header-{num_str}.svg"
    with open(hdr_file, "r", encoding="utf-8") as f_hdr:
        hdr_txt = f_hdr.read()
        assert "REPOSITORY ONLY" in hdr_txt
        assert "LIVE" not in hdr_txt

# Projects 01, 02, 03, 04, 05, 11 must have LIVE
for i in [1, 2, 3, 4, 5, 11]:
    num_str = f"{i:02d}"
    hdr_file = f"assets/cards/header-{num_str}.svg"
    with open(hdr_file, "r", encoding="utf-8") as f_hdr:
        hdr_txt = f_hdr.read()
        assert "LIVE" in hdr_txt
        assert "REPOSITORY ONLY" not in hdr_txt

print("Status accuracy confirmed for all 11 projects.")

# 5. Check target URLs and ensure old ones are removed
assert "https://images-hub.netlify.app/pages/index.html" in readme
assert "https://imagehub.netlify.app/" not in readme
print("ImageHub: verified new URL https://images-hub.netlify.app/pages/index.html, old URL removed.")

assert "https://habitsgrow.netlify.app/" in readme
assert "https://habit-flow-ten-eta.vercel.app" not in readme
assert "HabitFlow" not in readme
print("HabitsGrow: verified new URL https://habitsgrow.netlify.app/, old URL and HabitFlow removed.")

assert "https://net-gallery-hb.netlify.app/" in readme
print("Shop (Net Gallery Hb): verified URL https://net-gallery-hb.netlify.app/.")

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

# 7. Check technical dossier links for all 11 in README.md
for i in range(1, 12):
    assert f"PROJECTS.md#{i:02d}-" in readme
print("All 11 technical dossier links are present and verified in README.md.")

# 8. Check PROJECTS.md
assert "https://images-hub.netlify.app/pages/index.html" in projects_md
assert "https://habitsgrow.netlify.app/" in projects_md
assert "https://net-gallery-hb.netlify.app/" in projects_md
assert "11-shop" in projects_md
print("PROJECTS.md verified with all updated URLs and Section 11.")

# 9. Check portfolio/index.html
assert "https://images-hub.netlify.app/pages/index.html" in portfolio
assert "https://habitsgrow.netlify.app/" in portfolio
assert "https://net-gallery-hb.netlify.app/" in portfolio
assert "11-shop" in portfolio
print("portfolio/index.html verified with all updated URLs and Project 11.")

print("\n=======================================================")
print("ALL VERIFICATION AUDITS PASSED COMPLETELY AND FLAWLESSLY!")
print("=======================================================")
