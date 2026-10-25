import os
import re

with open("scratch/rendered_section_04.md", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Check all 10 project cards
for i in range(1, 11):
    num_str = f"{i:02d}"
    assert f"<!-- PROJECT {num_str} — COMPLETE CARD:" in content, f"Missing card comment for {num_str}"
    assert f'<a id="' in content, f"Missing anchor for {num_str}"
    assert f'assets/cards/header-{num_str}.svg' in content, f"Missing header-{num_str}.svg"
    assert os.path.exists(f'assets/cards/header-{num_str}.svg'), f"File assets/cards/header-{num_str}.svg missing!"

# 2. Check all referenced images
imgs = re.findall(r'<img [^>]*src="([^"]+)"', content)
print(f"Total img tags in rendered section: {len(imgs)}")

missing = 0
for src in imgs:
    if not os.path.exists(src):
        print(f"MISSING ASSET: {src}")
        missing += 1

assert missing == 0, f"{missing} assets missing!"
print("All referenced assets exist on disk!")

# 3. Check status
for i in range(1, 6):
    num_str = f"{i:02d}"
    with open(f"assets/cards/header-{num_str}.svg", "r", encoding="utf-8") as f_hdr:
        hdr_txt = f_hdr.read()
        assert "LIVE" in hdr_txt, f"Expected LIVE in header-{num_str}.svg"
        assert "#10b981" in hdr_txt, f"Expected green #10b981 in header-{num_str}.svg"
        assert "pulseGlow" in hdr_txt, f"Expected pulsing animation in header-{num_str}.svg"

for i in range(6, 11):
    num_str = f"{i:02d}"
    with open(f"assets/cards/header-{num_str}.svg", "r", encoding="utf-8") as f_hdr:
        hdr_txt = f_hdr.read()
        assert "REPOSITORY ONLY" in hdr_txt, f"Expected REPOSITORY ONLY in header-{num_str}.svg"
        assert "#334155" in hdr_txt, f"Expected dark slate in header-{num_str}.svg"

print("All status requirements verified (01-05 green pulsing LIVE, 06-10 REPOSITORY ONLY).")

# 4. Check for unsupported scripts
assert "<script" not in content.lower(), "Found <script> tag!"
assert "javascript:" not in content.lower(), "Found javascript: URI!"

print("Validation script completed successfully with ZERO errors.")
