import os
import re
import xml.etree.ElementTree as ET

SVG_FILES = [
    'assets/section-stats.svg',
    'assets/streak-metrics.svg',
    'assets/github-stats.svg',
    'assets/language-stats-card.svg',
    'assets/monthly-trend.svg',
    'assets/contribution-heatmap.svg'
]

def verify():
    all_ok = True
    print("=== VERIFYING SECTION 07 SVG ASSETS ===")
    for path in SVG_FILES:
        print(f"\nChecking: {path}")
        if not os.path.exists(path):
            print(f"  [FAIL] File does not exist: {path}")
            all_ok = False
            continue

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for encoding corruption
        for bad in ['â€“', 'â€¢', 'â˜…', 'â']:
            if bad in content:
                print(f"  [FAIL] Mojibake encoding defect found: '{bad}'")
                all_ok = False

        # Parse XML
        try:
            root = ET.fromstring(content)
            print(f"  [PASS] Well-formed XML")
        except ET.ParseError as e:
            print(f"  [FAIL] XML syntax error: {e}")
            all_ok = False
            continue

        # Check viewBox
        vb = root.get('viewBox')
        if not vb:
            print(f"  [FAIL] Missing viewBox")
            all_ok = False
        else:
            vb_parts = [float(x) for x in vb.split()]
            vw, vh = vb_parts[2], vb_parts[3]
            print(f"  [PASS] viewBox: {vb} (w={vw}, h={vh})")

        # Check negative text coordinates
        # Find all <text> elements
        neg_text = []
        for text_tag in root.iter('{http://www.w3.org/2000/svg}text'):
            y_val = text_tag.get('y')
            if y_val and float(y_val) < 0:
                neg_text.append((text_tag.text, y_val))
        
        if neg_text:
            print(f"  [WARN] Negative text coordinates found: {neg_text}")
        else:
            print(f"  [PASS] No negative text coordinates")

    print("\n" + ("="*40))
    if all_ok:
        print("ALL 6 SVG ASSETS ARE 100% VALID & VERIFIED!")
    else:
        print("FAILURES DETECTED IN ASSETS AUDIT")
    print("="*40)

if __name__ == '__main__':
    verify()

