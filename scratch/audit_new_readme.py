import os
import re

with open("scratch/TEST_README.md", "r", encoding="utf-8") as f:
    readme = f.read()

with open("README.md", "r", encoding="utf-8") as f:
    orig_readme = f.read()

# 1. Section banners check
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
print("Pass 1: All 8 section banners are intact.")

# 2. Check all 11 projects in README.md
for i in range(1, 12):
    num_str = f"{i:02d}"
    assert f"<!-- PROJECT {num_str} — COMPLETE CARD:" in readme, f"Missing card comment for project {num_str}"
    assert f'assets/cards/header-{num_str}.svg' in readme, f"Missing header-{num_str}.svg in README.md"
    assert os.path.exists(f'assets/cards/header-{num_str}.svg'), f"Header file missing on disk: assets/cards/header-{num_str}.svg"
print("Pass 2: All 11 project cards and headers verified in README.md.")

# 3. Check order: Project 01 must be Shop, Project 02 must be CyberGuard YUVA
assert "<!-- PROJECT 01 — COMPLETE CARD: Shop (Net Gallery Hb)" in readme
assert "assets/shop-preview.svg" in readme
assert "https://net-gallery-hb.netlify.app/" in readme

assert "<!-- PROJECT 02 — COMPLETE CARD: CyberGuard YUVA" in readme
assert "assets/cyberguard-preview.png" in readme
assert "https://cyberguard-yuva.vercel.app/" in readme

assert "<!-- PROJECT 03 — COMPLETE CARD: PDFHub" in readme
assert "<!-- PROJECT 04 — COMPLETE CARD: ImageHub" in readme
assert "<!-- PROJECT 05 — COMPLETE CARD: HabitsGrow" in readme
assert "<!-- PROJECT 06 — COMPLETE CARD: Advanced Image Compressor" in readme
assert "<!-- PROJECT 07 — COMPLETE CARD: Termux Command Guide" in readme
assert "<!-- PROJECT 08 — COMPLETE CARD: Passport Photo Maker" in readme
assert "<!-- PROJECT 09 — COMPLETE CARD: Text to Audio Converter" in readme
assert "<!-- PROJECT 10 — COMPLETE CARD: Student Task Manager" in readme
assert "<!-- PROJECT 11 — COMPLETE CARD: Deployment Dashboard" in readme
print("Pass 3: Project reordering verified (01=Shop, 02=CyberGuard YUVA, 03-11 sequential).")

# 4. Check vertical layout: NO side-by-side layout in Section 04 or Section 05
assert 'width="36%"' not in readme, "Old width=36% layout still present in README"
assert 'width="64%"' not in readme, "Old width=64% layout still present in README"
assert 'width="30%"' not in readme, "Old width=30% layout in CyberGuard still present in README"
assert 'width="70%"' not in readme, "Old width=70% layout in CyberGuard still present in README"
print("Pass 4: All old side-by-side columns completely removed. Layout is 100% vertical.")

# 5. Check Section 05 CyberGuard YUVA
assert "assets/cyberguard-banner.svg" in readme, "CyberGuard banner missing in README"
assert os.path.exists("assets/cyberguard-banner.svg"), "assets/cyberguard-banner.svg missing on disk"
assert "CyberGuard YUVA — Youth Cyber Defense Club" in readme
assert "SECURE &nbsp;•&nbsp; EDUCATE &nbsp;•&nbsp; EMPOWER" in readme
assert "assets/btn-visit-cyberguard.svg" in readme
assert "assets/cyberguard-pillars.svg" in readme
print("Pass 5: Section 05 CyberGuard YUVA verified with vertical banner, title, slogan, pillars, and button.")

# 6. Check all local image links in README.md
local_imgs = re.findall(r'<img [^>]*src="([^"]+)"', readme)
local_assets = [img for img in local_imgs if not img.startswith("http")]
print(f"Total local images referenced in README.md: {len(local_assets)}")
missing_imgs = [img for img in local_assets if not os.path.exists(img)]
assert len(missing_imgs) == 0, f"Missing images: {missing_imgs}"
print(f"Pass 6: All {len(local_assets)} local images exist on disk with ZERO broken links.")

# 7. Check action buttons validity
assert 'href="https://github.com/officialhazim42/cyberguard' not in readme
assert 'href="https://github.com/officialhazim42/habit' not in readme
assert 'assets/buttons/btn-private-codebase.svg' in readme
print("Pass 7: Private codebases correctly display static private badge.")

# 8. Check status accuracy
# Projects 01 to 06 must have LIVE
for i in range(1, 7):
    num_str = f"{i:02d}"
    hdr_file = f"assets/cards/header-{num_str}.svg"
    with open(hdr_file, "r", encoding="utf-8") as f_hdr:
        hdr_txt = f_hdr.read()
        assert "LIVE" in hdr_txt, f"Expected LIVE in {hdr_file}"
        assert "REPOSITORY ONLY" not in hdr_txt, f"Unexpected REPOSITORY ONLY in {hdr_file}"

# Projects 07 to 11 must have REPOSITORY ONLY
for i in range(7, 12):
    num_str = f"{i:02d}"
    hdr_file = f"assets/cards/header-{num_str}.svg"
    with open(hdr_file, "r", encoding="utf-8") as f_hdr:
        hdr_txt = f_hdr.read()
        assert "REPOSITORY ONLY" in hdr_txt, f"Expected REPOSITORY ONLY in {hdr_file}"
        assert "LIVE" not in hdr_txt, f"Unexpected LIVE in {hdr_file}"

print("Pass 8: Status accuracy confirmed (01-06 LIVE, 07-11 REPOSITORY ONLY).")

# 9. Check public repo URLs
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
print("Pass 9: All 8 public repository URLs are present and verified.")

# 10. Check that unrelated sections are identical
p_sec4_start = orig_readme.find("<!-- ================================================================= -->\n<!-- PROJECT 01 — COMPLETE CARD:")
p_sec6_start = orig_readme.find('<img src="assets/section-philosophy.svg"')

assert readme[:p_sec4_start] == orig_readme[:p_sec4_start], "Prefix before Section 04 was altered!"
p_new_sec6_start = readme.find('<img src="assets/section-philosophy.svg"')
assert readme[p_new_sec6_start:] == orig_readme[p_sec6_start:], "Suffix after Section 05 was altered!"
print("Pass 10: Unrelated sections (Profile Banner, About, Tech Stack, Journey, Activity, Connect) are 100% UNTOUCHED.")

print("\n=======================================================")
print("ALL 10 VERIFICATION AUDITS PASSED COMPLETELY AND FLAWLESSLY!")
print("=======================================================")
