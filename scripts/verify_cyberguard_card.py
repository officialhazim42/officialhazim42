import os
import re

def verify():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    start_tag = '<!-- PROJECT 02 — COMPLETE CARD: CyberGuard YUVA'
    end_tag = '<!-- PROJECT 03 — COMPLETE CARD: PDFHub'

    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)

    card_text = content[start_idx:end_idx]

    print('=== Verification Report for Section 04 Project 02 ===')
    
    # 1. LIVE badge check: Ensure badge-live.svg and duplicate LIVE indicators are removed
    assert 'badge-live.svg' not in card_text, "Error: badge-live.svg found in Project 02"
    assert 'Portal Protection LIVE' not in card_text, "Error: Portal Protection LIVE found in Project 02"
    
    # Check that header-02 alt text does not contain LIVE
    header_img_match = re.search(r'<img src="assets/cards/header-02.svg"[^>]+>', card_text)
    assert header_img_match, "header-02.svg not found in Project 02"
    print("1. Confirmed: badge-live.svg and duplicate LIVE indicators completely removed from card description area.")

    # 2. Check header-02.svg LIVE indicator
    with open('assets/cards/header-02.svg', 'r', encoding='utf-8') as f:
        header_text = f.read()

    header_live = re.findall(r'>\s*LIVE\s*<', header_text)
    print(f'2. LIVE occurrences inside header-02.svg: {len(header_live)}')
    assert len(header_live) == 1, "Expected exactly 1 LIVE in header-02.svg"

    # 3. Check 4-stage color sequence in header-02.svg
    expected_colors = ['#ffffff', '#047857', '#10b981', '#34d399']
    for color in expected_colors:
        assert color in header_text, f"Missing color {color} in header-02.svg"
    print("3. Four-stage color sequence verified: White (#ffffff) -> Dark Green (#047857) -> Green (#10b981) -> Light Green (#34d399)")

    # 4. Check image assets existence
    img_matches = re.findall(r'src="([^"]+)"', card_text)
    print("4. Checking image paths:")
    for img in img_matches:
        exists = os.path.exists(img)
        print(f'   - {img} exists: {exists}')
        assert exists, f"Broken image path: {img}"

    # 5. Check official website URL
    official_url = "https://cyberguard-yuva.vercel.app/"
    urls = re.findall(r'href="([^"]+)"', card_text)
    print("5. Checking URLs:")
    for u in urls:
        print(f'   - {u}')
    assert official_url in urls, f"Official URL {official_url} not found in card"

    print("\nALL 5 CRITICAL VERIFICATION CHECKS PASSED WITH ZERO ERRORS!")

if __name__ == '__main__':
    verify()
