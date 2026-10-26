import os
import html

os.makedirs("assets/cards", exist_ok=True)
os.makedirs("assets/buttons", exist_ok=True)

header_icons = {
    "shop": """<path d="M3 7L5 3H17L19 7" stroke="#38bdf8" stroke-width="1.4" stroke-linejoin="round" fill="#081b38"/>
<path d="M3 7H19V19C19 20.1 18.1 21 17 21H5C3.9 21 3 20.1 3 19V7Z" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<path d="M8 10V13C8 14.65 9.35 16 11 16C12.65 16 14 14.65 14 13V10" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round"/>""",

    "cyberguard": """<path d="M11 2L19 5.5V11C19 16 11 20 11 20C11 20 3 16 3 11V5.5L11 2Z" stroke="#38bdf8" stroke-width="1.5" fill="#081b38" stroke-linejoin="round"/>
<circle cx="11" cy="10" r="2.5" fill="#38bdf8"/>""",

    "pdfhub": """<rect x="2" y="1" width="16" height="20" rx="2" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<line x1="6" y1="6" x2="14" y2="6" stroke="#38bdf8" stroke-width="1.3"/>
<line x1="6" y1="10" x2="14" y2="10" stroke="#38bdf8" stroke-width="1.3"/>
<line x1="6" y1="14" x2="11" y2="14" stroke="#38bdf8" stroke-width="1.3"/>""",

    "imagehub": """<rect x="1" y="2" width="20" height="17" rx="3" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<circle cx="6.5" cy="7.5" r="2" fill="#38bdf8"/>
<path d="M3 16L9 10L13 14L16 11L19 15" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>""",

    "habitsgrow": """<path d="M4 18C4 18 5 11 11 11M11 11C11 11 11 5 18 4C18 4 18 11 11 11M11 11C11 11 11 18 4 18Z" stroke="#38bdf8" stroke-width="1.5" fill="#081b38" stroke-linejoin="round"/>
<path d="M11 11C11 16 7 19 4 19" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round"/>""",

    "compressor": """<polygon points="12,1 4,12 11,12 10,21 18,10 11,10" stroke="#38bdf8" stroke-width="1.4" fill="#081b38" stroke-linejoin="round"/>""",

    "termux": """<rect x="1" y="2" width="20" height="17" rx="3" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<path d="M5 7L9 10.5L5 14" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round"/>
<line x1="11" y1="14" x2="16" y2="14" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round"/>""",

    "passport": """<rect x="1" y="4" width="20" height="15" rx="3" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<path d="M7 4L8.5 1.5H13.5L15 4" stroke="#38bdf8" stroke-width="1.3" fill="#081b38"/>
<circle cx="11" cy="11.5" r="4" stroke="#38bdf8" stroke-width="1.4" fill="none"/>
<circle cx="11" cy="11.5" r="1.5" fill="#38bdf8"/>""",

    "audio": """<path d="M3 7H7L12 3V19L7 15H3V7Z" stroke="#38bdf8" stroke-width="1.4" fill="#081b38" stroke-linejoin="round"/>
<path d="M15 7C16.5 8.2 17.5 10 17.5 11C17.5 12 16.5 13.8 15 15" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round" fill="none"/>
<path d="M17.5 4C20 6 21 8.5 21 11C21 13.5 20 16 17.5 18" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round" fill="none"/>""",

    "taskmanager": """<rect x="2" y="2" width="18" height="18" rx="3" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<path d="M6 7L8 9L12 5" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="13" y1="8" x2="16" y2="8" stroke="#38bdf8" stroke-width="1.3"/>
<line x1="6" y1="13" x2="16" y2="13" stroke="#38bdf8" stroke-width="1.3"/>
<line x1="6" y1="16" x2="13" y2="16" stroke="#38bdf8" stroke-width="1.3"/>""",

    "deployment": """<rect x="1" y="2" width="20" height="17" rx="3" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<line x1="1" y1="7" x2="21" y2="7" stroke="#38bdf8" stroke-width="1.2"/>
<circle cx="4" cy="4.5" r="1" fill="#38bdf8"/>
<circle cx="7" cy="4.5" r="1" fill="#38bdf8"/>
<line x1="5" y1="15" x2="8" y2="11" stroke="#38bdf8" stroke-width="1.4"/>
<line x1="8" y1="11" x2="11" y2="13" stroke="#38bdf8" stroke-width="1.4"/>
<line x1="11" y1="13" x2="16" y2="9" stroke="#38bdf8" stroke-width="1.4"/>"""
}

# New project order:
# 01 - Shop
# 02 - CyberGuard YUVA
# 03 - PDFHub
# 04 - ImageHub
# 05 - HabitsGrow
# 06 - Advanced Image Compressor
# 07 - Termux Command Guide
# 08 - Passport Photo Maker
# 09 - Text to Audio Converter
# 10 - Student Task Manager
# 11 - Deployment Dashboard
project_headers = [
    ("header-01.svg", "01", "shop", "Shop (Net Gallery Hb)", "DIGITAL & PRINTING SERVICES PLATFORM", True),
    ("header-02.svg", "02", "cyberguard", "CyberGuard YUVA", "CYBER DEFENSE PORTAL & COMMUNITY", True),
    ("header-03.svg", "03", "pdfhub", "PDFHub", "CLIENT-SIDE WEBASSEMBLY SUITE", True),
    ("header-04.svg", "04", "imagehub", "ImageHub", "13 FREE IN-BROWSER IMAGE TOOLS ONLINE", True),
    ("header-05.svg", "05", "habitsgrow", "HabitsGrow", "GROW BETTER EVERY DAY", True),
    ("header-06.svg", "06", "compressor", "Advanced Image Compressor", "CLIENT-SIDE MULTI-FORMAT COMPRESSION UTILITY", True),
    ("header-07.svg", "07", "termux", "Termux Command Guide", "TECHNICAL DOCUMENTATION HANDBOOK", False),
    ("header-08.svg", "08", "passport", "Passport Photo Maker", "CLIENT-SIDE MEDIA TOOL", False),
    ("header-09.svg", "09", "audio", "Text to Audio Converter", "SPEECH SYNTHESIS TOOL", False),
    ("header-10.svg", "10", "taskmanager", "Student Task Manager", "ACADEMIC WORKFLOW WEB TOOL", False),
    ("header-11.svg", "11", "deployment", "Deployment Dashboard", "DEVOPS & MONITORING PROTOTYPE", False)
]

# Generate header SVGs
for filename, num, icon_key, name, tagline, is_live in project_headers:
    icon_vector = header_icons[icon_key]
    esc_name = html.escape(name)
    esc_tagline = html.escape(tagline)
    
    if is_live:
        status_markup = """  <g transform="translate(778, 20)">
    <rect width="84" height="28" rx="5" fill="#022c22" stroke="#10b981" stroke-width="1.2" />
    <circle class="live-glow" cx="16" cy="14" r="5" fill="#34d399" />
    <circle class="live-core" cx="16" cy="14" r="3.2" fill="#10b981" />
    <circle class="live-highlight" cx="16" cy="14" r="1.5" fill="#ffffff" />
    <text x="28" y="18.5" fill="#34d399" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="800" letter-spacing="1px">LIVE</text>
  </g>"""
    else:
        status_markup = """  <g transform="translate(718, 20)">
    <rect width="144" height="28" rx="5" fill="#0f172a" stroke="#334155" stroke-width="1.2" />
    <g transform="translate(11, 7.5)">
      <path d="M4 2.5L1 6L4 9.5" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M8 2.5L11 6L8 9.5" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <text x="30" y="18.5" fill="#94a3b8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="10.5" font-weight="700" letter-spacing="0.6px">REPOSITORY ONLY</text>
  </g>"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="68" viewBox="0 0 880 68" fill="none">
  <defs>
    <linearGradient id="hdr-bg-{num}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#071126" />
      <stop offset="50%" stop-color="#0a193b" />
      <stop offset="100%" stop-color="#060c1d" />
    </linearGradient>
    <linearGradient id="filament-{num}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#06b6d4" stop-opacity="1" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.1" />
    </linearGradient>
    <style>
      @keyframes pulseGlow {{
        0%, 15% {{ r: 4px; opacity: 0.15; fill: #059669; }}
        25% {{ r: 4.5px; opacity: 0.3; fill: #10b981; }}
        40% {{ r: 5px; opacity: 0.4; fill: #10b981; }}
        55%, 70% {{ r: 8px; opacity: 0.85; fill: #34d399; }}
        85% {{ r: 8.5px; opacity: 0.35; fill: #10b981; }}
        100% {{ r: 4px; opacity: 0.15; fill: #059669; }}
      }}
      @keyframes pulseCore {{
        0%, 15% {{ fill: #047857; opacity: 0.9; }}
        25% {{ fill: #065f46; opacity: 1; }}
        40%, 50% {{ fill: #047857; opacity: 1; }}
        60%, 75% {{ fill: #10b981; opacity: 1; }}
        90%, 100% {{ fill: #047857; opacity: 0.9; }}
      }}
      @keyframes pulseHighlight {{
        0%, 10% {{ opacity: 0; r: 1px; }}
        20%, 30% {{ opacity: 1; r: 1.8px; }}
        45% {{ opacity: 0.4; r: 1.4px; }}
        60%, 75% {{ opacity: 0.9; r: 1.6px; }}
        90%, 100% {{ opacity: 0.1; r: 1px; }}
      }}
      .live-glow {{ animation: pulseGlow 2.8s ease-in-out infinite; }}
      .live-core {{ animation: pulseCore 2.8s ease-in-out infinite; }}
      .live-highlight {{ animation: pulseHighlight 2.8s ease-in-out infinite; }}
      @media (prefers-reduced-motion: reduce) {{
        .live-glow, .live-core, .live-highlight {{ animation: none; }}
      }}
    </style>
  </defs>

  <!-- Card Header Container -->
  <rect x="0.5" y="0.5" width="879" height="67" rx="8" fill="url(#hdr-bg-{num})" stroke="#1e3a5f" stroke-width="1.2" />

  <!-- Top Accent Cyan Filament Line -->
  <rect x="14" y="1" width="260" height="2" rx="1" fill="url(#filament-{num})" />

  <!-- Project Number Badge Pill -->
  <rect x="18" y="17" width="76" height="34" rx="6" fill="#081b38" stroke="#0284c7" stroke-width="1.3" />
  <text x="25" y="39" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="13" font-weight="800" letter-spacing="1px">{num} / 11</text>

  <!-- Project Vector Icon -->
  <g transform="translate(108, 17)">
    {icon_vector}
  </g>

  <!-- Project Title -->
  <text x="138" y="34" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="17" font-weight="800" letter-spacing="0.3px">{esc_name}</text>

  <!-- Project Tagline -->
  <text x="139" y="51" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="10.5" font-weight="700" letter-spacing="1.2px">{esc_tagline}</text>

{status_markup}
</svg>"""

    with open(f"assets/cards/{filename}", "w", encoding="utf-8") as f:
        f.write(svg)

print("All 11 project headers generated successfully in assets/cards/.")

# Generate refined assets/badge-live.svg
badge_live_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="90" height="28" viewBox="0 0 90 28" fill="none">
  <defs>
    <linearGradient id="live-badge-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#022c22" />
      <stop offset="100%" stop-color="#064e3b" />
    </linearGradient>
    <style>
      @keyframes pulseGlow {
        0%, 15% { r: 4px; opacity: 0.15; fill: #059669; }
        25% { r: 4.5px; opacity: 0.3; fill: #10b981; }
        40% { r: 5px; opacity: 0.4; fill: #10b981; }
        55%, 70% { r: 8px; opacity: 0.85; fill: #34d399; }
        85% { r: 8.5px; opacity: 0.35; fill: #10b981; }
        100% { r: 4px; opacity: 0.15; fill: #059669; }
      }
      @keyframes pulseCore {
        0%, 15% { fill: #047857; opacity: 0.9; }
        25% { fill: #065f46; opacity: 1; }
        40%, 50% { fill: #047857; opacity: 1; }
        60%, 75% { fill: #10b981; opacity: 1; }
        90%, 100% { fill: #047857; opacity: 0.9; }
      }
      @keyframes pulseHighlight {
        0%, 10% { opacity: 0; r: 1px; }
        20%, 30% { opacity: 1; r: 1.8px; }
        45% { opacity: 0.4; r: 1.4px; }
        60%, 75% { opacity: 0.9; r: 1.6px; }
        90%, 100% { opacity: 0.1; r: 1px; }
      }
      .live-glow { animation: pulseGlow 2.8s ease-in-out infinite; }
      .live-core { animation: pulseCore 2.8s ease-in-out infinite; }
      .live-highlight { animation: pulseHighlight 2.8s ease-in-out infinite; }
      @media (prefers-reduced-motion: reduce) {
        .live-glow, .live-core, .live-highlight { animation: none; }
      }
    </style>
  </defs>
  <rect x="0.5" y="0.5" width="89" height="27" rx="6" fill="url(#live-badge-bg)" stroke="#10b981" stroke-width="1.2" />
  <circle class="live-glow" cx="16" cy="14" r="5" fill="#34d399" />
  <circle class="live-core" cx="16" cy="14" r="3.2" fill="#10b981" />
  <circle class="live-highlight" cx="16" cy="14" r="1.5" fill="#ffffff" />
  <text x="30" y="17.5" fill="#34d399" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="800" letter-spacing="1px">LIVE</text>
</svg>"""

with open("assets/badge-live.svg", "w", encoding="utf-8") as f:
    f.write(badge_live_svg)

print("assets/badge-live.svg updated successfully.")

# Generate refined assets/badge-repo-only.svg
badge_repo_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="144" height="28" viewBox="0 0 144 28" fill="none">
  <defs>
    <linearGradient id="repo-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="143" height="27" rx="6" fill="url(#repo-bg)" stroke="#334155" stroke-width="1.2" />
  <g transform="translate(11, 8)">
    <path d="M4 2.5L1 6L4 9.5" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M8 2.5L11 6L8 9.5" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
  </g>
  <text x="30" y="18" fill="#94a3b8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="10.5" font-weight="700" letter-spacing="0.6px">REPOSITORY ONLY</text>
</svg>"""

with open("assets/badge-repo-only.svg", "w", encoding="utf-8") as f:
    f.write(badge_repo_svg)

print("assets/badge-repo-only.svg updated successfully.")

# Update assets/btn-visit-cyberguard.svg with "VISIT CYBERGUARD YUVA"
btn_visit_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 42" width="250" height="42">
  <defs>
    <linearGradient id="btn-bg-cg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="50%" stop-color="#0369a1" />
      <stop offset="100%" stop-color="#0b1b3a" />
    </linearGradient>
    <linearGradient id="btn-border-cg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#60a5fa" />
      <stop offset="100%" stop-color="#38bdf8" />
    </linearGradient>
    <filter id="btn-glow-cg" x="-15%" y="-30%" width="130%" height="160%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0284c7" flood-opacity="0.45" />
    </filter>
    <style>
      .btn-rect { transition: all 0.25s ease; }
      .btn-rect:hover { stroke: #67e8f9; filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.65)); }
      .btn-text { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11px; font-weight: 800; fill: #ffffff; letter-spacing: 1.1px; }
      .arrow-symbol { font-family: system-ui, -apple-system, sans-serif; font-size: 14px; font-weight: 900; fill: #38bdf8; animation: arrowShift 2s ease-in-out infinite; }
      @keyframes arrowShift { 0%, 100% { transform: translateX(0); } 50% { transform: translateX(3px); } }
      @media (prefers-reduced-motion: reduce) { .arrow-symbol { animation: none; } }
    </style>
  </defs>
  <rect class="btn-rect" x="1.5" y="1.5" width="247" height="39" rx="8" fill="url(#btn-bg-cg)" stroke="url(#btn-border-cg)" stroke-width="1.5" filter="url(#btn-glow-cg)" />
  <g transform="translate(14, 12)">
    <path d="M 9 2 L 15 4.5 L 15 9 C 15 13 9 16 9 16 C 9 16 3 13 3 9 L 3 4.5 Z" stroke="#38bdf8" stroke-width="1.3" fill="#061226" stroke-linejoin="round" />
    <circle cx="9" cy="8.5" r="1.5" fill="#38bdf8" />
  </g>
  <text x="38" y="25" class="btn-text">VISIT CYBERGUARD YUVA</text>
  <g transform="translate(225, 25)">
    <text class="arrow-symbol">→</text>
  </g>
</svg>"""

with open("assets/btn-visit-cyberguard.svg", "w", encoding="utf-8") as f:
    f.write(btn_visit_svg)

print("assets/btn-visit-cyberguard.svg updated with VISIT CYBERGUARD YUVA.")
