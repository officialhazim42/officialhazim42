import os
import html
import xml.etree.ElementTree as ET

os.makedirs("assets/cards", exist_ok=True)
os.makedirs("assets/tech", exist_ok=True)
os.makedirs("assets/buttons", exist_ok=True)

# ==============================================================================
# 1. STATUS BADGES
# ==============================================================================
badge_live_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="84" height="26" viewBox="0 0 84 26" fill="none">
  <defs>
    <linearGradient id="live-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#022c22" />
      <stop offset="100%" stop-color="#064e3b" />
    </linearGradient>
    <style>
      @keyframes pulseGlow {
        0%, 100% { r: 5px; opacity: 0.35; }
        50% { r: 8px; opacity: 0.85; }
      }
      @keyframes pulseCore {
        0%, 100% { opacity: 0.9; }
        50% { opacity: 1; }
      }
      .live-glow { animation: pulseGlow 2.2s ease-in-out infinite; }
      .live-core { animation: pulseCore 2.2s ease-in-out infinite; }
      @media (prefers-reduced-motion: reduce) {
        .live-glow, .live-core { animation: none; }
      }
    </style>
  </defs>
  <rect x="0.5" y="0.5" width="83" height="25" rx="5" fill="url(#live-bg)" stroke="#10b981" stroke-width="1.2" />
  <circle class="live-glow" cx="15" cy="13" r="5" fill="#34d399" />
  <circle class="live-core" cx="15" cy="13" r="3.2" fill="#10b981" />
  <circle cx="15" cy="13" r="1.5" fill="#ecfdf5" />
  <text x="27" y="17" fill="#34d399" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="800" letter-spacing="1px">LIVE</text>
</svg>"""

with open("assets/badge-live.svg", "w", encoding="utf-8") as f:
    f.write(badge_live_svg)

badge_repo_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="144" height="26" viewBox="0 0 144 26" fill="none">
  <defs>
    <linearGradient id="repo-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="143" height="25" rx="5" fill="url(#repo-bg)" stroke="#334155" stroke-width="1.2" />
  <g transform="translate(11, 7)">
    <path d="M4 2.5L1 6L4 9.5" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M8 2.5L11 6L8 9.5" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
  </g>
  <text x="30" y="17" fill="#94a3b8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="10.5" font-weight="700" letter-spacing="0.6px">REPOSITORY ONLY</text>
</svg>"""

with open("assets/badge-repo-only.svg", "w", encoding="utf-8") as f:
    f.write(badge_repo_svg)

# ==============================================================================
# 2. ACTION BUTTONS
# ==============================================================================
btn_live_demo = """<svg xmlns="http://www.w3.org/2000/svg" width="136" height="34" viewBox="0 0 136 34" fill="none">
  <defs>
    <linearGradient id="live-btn-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="60%" stop-color="#0369a1" />
      <stop offset="100%" stop-color="#0b1b3a" />
    </linearGradient>
    <linearGradient id="live-btn-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#60a5fa" />
      <stop offset="100%" stop-color="#38bdf8" />
    </linearGradient>
    <filter id="live-btn-glow" x="-15%" y="-30%" width="130%" height="160%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0284c7" flood-opacity="0.4" />
    </filter>
    <style>
      .btn-box { transition: all 0.25s ease; }
      .btn-box:hover { stroke: #67e8f9; filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.65)); }
      .arrow-anim { animation: arrowMove 2s ease-in-out infinite; }
      @keyframes arrowMove { 0%, 100% { transform: translateX(0); } 50% { transform: translateX(2.5px); } }
      @media (prefers-reduced-motion: reduce) { .arrow-anim { animation: none; } }
    </style>
  </defs>
  <rect class="btn-box" x="1" y="1" width="134" height="32" rx="6" fill="url(#live-btn-bg)" stroke="url(#live-btn-border)" stroke-width="1.2" filter="url(#live-btn-glow)" />
  <g transform="translate(11, 9)">
    <circle cx="8" cy="8" r="7" stroke="#38bdf8" stroke-width="1.2" fill="none"/>
    <ellipse cx="8" cy="8" rx="3.5" ry="7" stroke="#38bdf8" stroke-width="1.1" fill="none"/>
    <line x1="1" y1="8" x2="15" y2="8" stroke="#38bdf8" stroke-width="1.1"/>
  </g>
  <text x="33" y="21.5" fill="#ffffff" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="800" letter-spacing="1px">LIVE DEMO</text>
  <g class="arrow-anim" transform="translate(114, 21.5)">
    <text fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="900">↗</text>
  </g>
</svg>"""

with open("assets/buttons/btn-live-demo.svg", "w", encoding="utf-8") as f:
    f.write(btn_live_demo)

btn_view_repo = """<svg xmlns="http://www.w3.org/2000/svg" width="166" height="34" viewBox="0 0 166 34" fill="none">
  <defs>
    <linearGradient id="repo-btn-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f2244" />
      <stop offset="100%" stop-color="#081226" />
    </linearGradient>
    <filter id="repo-btn-glow" x="-15%" y="-30%" width="130%" height="160%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#1e3a5f" flood-opacity="0.3" />
    </filter>
    <style>
      .repo-box { transition: all 0.25s ease; }
      .repo-box:hover { stroke: #38bdf8; filter: drop-shadow(0 0 6px rgba(56, 189, 248, 0.4)); }
      .arrow-anim { animation: arrowMove 2s ease-in-out infinite; }
      @keyframes arrowMove { 0%, 100% { transform: translateX(0); } 50% { transform: translateX(2.5px); } }
      @media (prefers-reduced-motion: reduce) { .arrow-anim { animation: none; } }
    </style>
  </defs>
  <rect class="repo-box" x="1" y="1" width="164" height="32" rx="6" fill="url(#repo-btn-bg)" stroke="#1e3a5f" stroke-width="1.2" filter="url(#repo-btn-glow)" />
  <g transform="translate(10, 9)">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8C0 11.54 2.29 14.53 5.47 15.59C5.87 15.66 6.02 15.42 6.02 15.21C6.02 15.02 6.01 14.39 6.01 13.72C4 14.09 3.48 13.23 3.32 12.78C3.23 12.55 2.84 11.84 2.5 11.65C2.22 11.5 1.82 11.13 2.49 11.12C3.12 11.11 3.57 11.7 3.72 11.94C4.44 13.15 5.59 12.81 6.05 12.6C6.12 12.08 6.33 11.73 6.56 11.53C4.78 11.33 2.92 10.64 2.92 7.58C2.92 6.71 3.23 5.99 3.74 5.43C3.66 5.23 3.38 4.41 3.82 3.31C3.82 3.31 4.49 3.1 6.02 4.13C6.66 3.95 7.34 3.86 8.02 3.86C8.7 3.86 9.38 3.95 10.02 4.13C11.55 3.09 12.22 3.31 12.22 3.31C12.66 4.41 12.38 5.23 12.3 5.43C12.81 5.99 13.12 6.7 13.12 7.58C13.12 10.65 11.25 11.33 9.47 11.53C9.76 11.78 10.01 12.26 10.01 13.01C10.01 14.08 10 14.94 10 15.21C10 15.42 10.15 15.67 10.55 15.59C13.71 14.53 16 11.53 16 8C16 3.58 12.42 0 8 0Z" fill="#38bdf8"/>
  </g>
  <text x="32" y="21.5" fill="#f8fafc" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="700" letter-spacing="0.8px">VIEW REPOSITORY</text>
  <g class="arrow-anim" transform="translate(146, 21.5)">
    <text fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="900">↗</text>
  </g>
</svg>"""

with open("assets/buttons/btn-view-repo.svg", "w", encoding="utf-8") as f:
    f.write(btn_view_repo)

btn_project_specs = """<svg xmlns="http://www.w3.org/2000/svg" width="148" height="34" viewBox="0 0 148 34" fill="none">
  <defs>
    <linearGradient id="specs-btn-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a1329" />
      <stop offset="100%" stop-color="#050a16" />
    </linearGradient>
    <style>
      .specs-box { transition: all 0.25s ease; }
      .specs-box:hover { stroke: #06b6d4; filter: drop-shadow(0 0 6px rgba(6, 182, 212, 0.4)); }
      .arrow-anim { animation: arrowMove 2s ease-in-out infinite; }
      @keyframes arrowMove { 0%, 100% { transform: translateX(0); } 50% { transform: translateX(2.5px); } }
      @media (prefers-reduced-motion: reduce) { .arrow-anim { animation: none; } }
    </style>
  </defs>
  <rect class="specs-box" x="1" y="1" width="146" height="32" rx="6" fill="url(#specs-btn-bg)" stroke="#1e3a5f" stroke-width="1.2" />
  <g transform="translate(11, 10)">
    <path d="M1 2C1 1.45 1.45 1 2 1H5C6.1 1 7 1.9 7 3V12C7 11.2 6.2 10.5 5 10.5H2C1.45 10.5 1 10.95 1 11.5V2Z" stroke="#06b6d4" stroke-width="1.2" fill="none"/>
    <path d="M13 2C13 1.45 12.55 1 12 1H9C7.9 1 7 1.9 7 3V12C7 11.2 7.8 10.5 9 10.5H12C12.55 10.5 13 10.95 13 11.5V2Z" stroke="#06b6d4" stroke-width="1.2" fill="none"/>
  </g>
  <text x="31" y="21.5" fill="#cbd5e1" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="700" letter-spacing="0.8px">PROJECT SPECS</text>
  <g class="arrow-anim" transform="translate(131, 21.5)">
    <text fill="#06b6d4" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="900">→</text>
  </g>
</svg>"""

with open("assets/buttons/btn-project-specs.svg", "w", encoding="utf-8") as f:
    f.write(btn_project_specs)

btn_private = """<svg xmlns="http://www.w3.org/2000/svg" width="168" height="34" viewBox="0 0 168 34" fill="none">
  <rect x="0.5" y="0.5" width="167" height="33" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1" />
  <g transform="translate(12, 10)">
    <rect x="2.5" y="4.5" width="11" height="8" rx="1.5" stroke="#94a3b8" stroke-width="1.2" fill="#1e293b"/>
    <path d="M5 4.5V3C5 1.9 5.9 1 7 1H9C10.1 1 11 1.9 11 3V4.5" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round"/>
    <circle cx="8" cy="8.5" r="1" fill="#94a3b8"/>
  </g>
  <text x="34" y="21.5" fill="#94a3b8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="10.5" font-weight="700" letter-spacing="0.8px">PRIVATE CODEBASE</text>
</svg>"""

with open("assets/buttons/btn-private-codebase.svg", "w", encoding="utf-8") as f:
    f.write(btn_private)

# ==============================================================================
# 3. TECH BADGES
# ==============================================================================
def create_tech_badge(filename, label, icon_svg, width=None):
    if width is None:
        width = int(len(label) * 7.5 + 38)
        if width < 82:
            width = 82
            
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="24" viewBox="0 0 {width} 24" fill="none">
  <rect x="0.5" y="0.5" width="{width - 1}" height="23" rx="4" fill="#0b1730" stroke="#1e3a5f" stroke-width="1"/>
  <g transform="translate(8, 4)">
    {icon_svg}
  </g>
  <text x="28" y="16" fill="#e2e8f0" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="10.5" font-weight="700" letter-spacing="0.3px">{html.escape(label)}</text>
</svg>"""
    with open(f"assets/tech/{filename}", "w", encoding="utf-8") as f:
        f.write(svg)

icons = {
    "javascript": """<rect width="16" height="16" rx="2" fill="#F7DF1E"/>
<text x="2.5" y="12" fill="#000000" font-family="system-ui, sans-serif" font-size="9" font-weight="900">JS</text>""",

    "webassembly": """<circle cx="8" cy="8" r="7.5" fill="#654FF0"/>
<text x="3" y="11.5" fill="#ffffff" font-family="system-ui, sans-serif" font-size="8" font-weight="900">WA</text>""",

    "pdflib": """<rect width="16" height="16" rx="2" fill="#E11D48"/>
<text x="1.5" y="11.5" fill="#ffffff" font-family="system-ui, sans-serif" font-size="7" font-weight="900">PDF</text>""",

    "pdfjs": """<rect width="16" height="16" rx="2" fill="#DC2626"/>
<path d="M4 3H10L13 6V13H4V3Z" fill="#ffffff"/>
<text x="5" y="11" fill="#DC2626" font-family="system-ui, sans-serif" font-size="6" font-weight="900">JS</text>""",

    "html5": """<path d="M1.5 0.5L3 14L8 15.5L13 14L14.5 0.5H1.5Z" fill="#E34F26"/>
<path d="M8 2V14.2L11.8 13.1L13 2H8Z" fill="#EF652A"/>
<path d="M4.5 4.5H11.5L11.2 7H5.9L6.1 9.5H11L10.6 12L8 12.7L5.4 12L5.2 10.5H3.7L4.1 13.5L8 14.5L11.9 13.5L12.5 4.5H4.5Z" fill="#FFFFFF"/>""",

    "css3": """<path d="M1.5 0.5L3 14L8 15.5L13 14L14.5 0.5H1.5Z" fill="#1572B6"/>
<path d="M8 2V14.2L11.8 13.1L13 2H8Z" fill="#33A9DC"/>
<path d="M4.5 4.5H11.5L11.2 7H5.9L6.1 9.5H11L10.6 12L8 12.7L5.4 12L5.2 10.5H3.7L4.1 13.5L8 14.5L11.9 13.5L12.5 4.5H4.5Z" fill="#FFFFFF"/>""",

    "canvas": """<rect width="16" height="16" rx="3" fill="#0c2340" stroke="#E34F26" stroke-width="1"/>
<circle cx="5" cy="5" r="1.5" fill="#E34F26"/>
<circle cx="11" cy="5" r="1.5" fill="#38BDF8"/>
<circle cx="8" cy="11" r="1.5" fill="#3ECF8E"/>""",

    "webapis": """<circle cx="8" cy="8" r="7" stroke="#38BDF8" stroke-width="1.2" fill="none"/>
<circle cx="8" cy="8" r="3" fill="#38BDF8"/>""",

    "serviceworkers": """<rect width="16" height="16" rx="3" fill="#5A0FC8"/>
<path d="M4 8C4 5.79 5.79 4 8 4C10.21 4 12 5.79 12 8C12 10.21 10.21 12 8 12" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" fill="none"/>
<circle cx="8" cy="8" r="1.5" fill="#ffffff"/>""",

    "nextjs": """<circle cx="8" cy="8" r="7.5" fill="#000000" stroke="#38BDF8" stroke-width="1"/>
<path d="M5 11.5V4.5H6.5L11 11.5H9.5L6.5 6.8V11.5H5Z" fill="#ffffff"/>""",

    "react": """<ellipse cx="8" cy="8" rx="7" ry="2.8" stroke="#61DAFB" stroke-width="1.1" fill="none"/>
<ellipse cx="8" cy="8" rx="7" ry="2.8" stroke="#61DAFB" stroke-width="1.1" fill="none" transform="rotate(60 8 8)"/>
<ellipse cx="8" cy="8" rx="7" ry="2.8" stroke="#61DAFB" stroke-width="1.1" fill="none" transform="rotate(120 8 8)"/>
<circle cx="8" cy="8" r="1.5" fill="#61DAFB"/>""",

    "typescript": """<rect width="16" height="16" rx="2" fill="#3178C6"/>
<text x="2" y="12" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="900">TS</text>""",

    "tailwindcss": """<path d="M4 7C5 5 7 5 8 6C9 7 10 7.5 12 7.5C14 7.5 15.5 6 15.5 6C15.5 6 14.5 8 13.5 9C12.5 10 11.5 10 9.5 9.5C8 9 7 9.5 6 10.5C5 11.5 4 11.5 4 11.5L4 7Z" fill="#06B6D4"/>""",

    "pwa": """<rect width="16" height="16" rx="3" fill="#5A0FC8"/>
<text x="1.5" y="11.5" fill="#ffffff" font-family="system-ui, sans-serif" font-size="7" font-weight="900">PWA</text>""",

    "supabase": """<path d="M8.5 0.5L1.5 9.5H8L7.5 15.5L14.5 6.5H8L8.5 0.5Z" fill="#3ECF8E"/>""",

    "vercel": """<path d="M8 2L14.5 13H1.5L8 2Z" fill="#ffffff"/>""",

    "netlify": """<path d="M8 1L14.5 7.5L8 14L1.5 7.5L8 1Z" fill="#00C7B7"/>
<path d="M8 4L11.5 7.5L8 11L4.5 7.5L8 4Z" fill="#ffffff"/>""",

    "bash": """<rect width="16" height="16" rx="2" fill="#1e293b"/>
<path d="M3 5L6.5 8L3 11" stroke="#4EAA25" stroke-width="1.5" stroke-linecap="round"/>
<line x1="8" y1="11" x2="13" y2="11" stroke="#4EAA25" stroke-width="1.5"/>""",

    "linux": """<ellipse cx="8" cy="8.5" rx="5" ry="6.5" fill="#FCC624"/>
<ellipse cx="8" cy="9.5" rx="3.5" ry="4.5" fill="#ffffff"/>
<circle cx="6.5" cy="5.5" r="1" fill="#000000"/>
<circle cx="9.5" cy="5.5" r="1" fill="#000000"/>
<polygon points="7,7 9,7 8,8.5" fill="#E34F26"/>""",

    "termux": """<rect width="16" height="16" rx="2" fill="#000000" stroke="#3DDC84" stroke-width="1"/>
<path d="M3 5L6 8L3 11" stroke="#3DDC84" stroke-width="1.4" stroke-linecap="round"/>
<line x1="7.5" y1="11" x2="12" y2="11" stroke="#3DDC84" stroke-width="1.4"/>""",

    "markdown": """<rect width="16" height="16" rx="2" fill="#081226" stroke="#94A3B8" stroke-width="1"/>
<path d="M2.5 11V5H4.5L6.5 7.5L8.5 5H10.5V11H9V7.5L7.2 9.8H5.8L4 7.5V11H2.5Z" fill="#94A3B8"/>
<path d="M12.5 8.5L14 10.5L15.5 8.5H14.5V5H13.5V8.5H12.5Z" fill="#38BDF8"/>""",

    "webspeech": """<path d="M2 5.5H5L8.5 2.5V13.5L5 10.5H2V5.5Z" fill="#38BDF8"/>
<path d="M11 5C11.8 5.8 12.3 6.8 12.3 8C12.3 9.2 11.8 10.2 11 11" stroke="#38BDF8" stroke-width="1.3" stroke-linecap="round" fill="none"/>
<path d="M13 3C14.3 4.3 15 6.1 15 8C15 9.9 14.3 11.7 13 13" stroke="#38BDF8" stroke-width="1.3" stroke-linecap="round" fill="none"/>""",

    "localstorage": """<ellipse cx="8" cy="4" rx="6" ry="2" fill="#38BDF8"/>
<path d="M2 4V8C2 9.1 4.7 10 8 10C11.3 10 14 9.1 14 8V4" stroke="#38BDF8" stroke-width="1.2" fill="none"/>
<path d="M2 8V12C2 13.1 4.7 14 8 14C11.3 14 14 13.1 14 12V8" stroke="#38BDF8" stroke-width="1.2" fill="none"/>""",

    "dom": """<rect x="5.5" y="2" width="5" height="3" rx="1" fill="#38BDF8"/>
<line x1="8" y1="5" x2="8" y2="8" stroke="#38BDF8" stroke-width="1.2"/>
<line x1="3.5" y1="8" x2="12.5" y2="8" stroke="#38BDF8" stroke-width="1.2"/>
<line x1="3.5" y1="8" x2="3.5" y2="11" stroke="#38BDF8" stroke-width="1.2"/>
<line x1="12.5" y1="8" x2="12.5" y2="11" stroke="#38BDF8" stroke-width="1.2"/>
<rect x="1" y="11" width="5" height="3" rx="1" fill="#38BDF8"/>
<rect x="10" y="11" width="5" height="3" rx="1" fill="#38BDF8"/>"""
}

badges = [
    ("tech-javascript.svg", "JavaScript (ES6+)", icons["javascript"]),
    ("tech-webassembly.svg", "WebAssembly", icons["webassembly"]),
    ("tech-pdflib.svg", "pdf-lib", icons["pdflib"]),
    ("tech-pdfjs.svg", "pdf.js", icons["pdfjs"]),
    ("tech-html5.svg", "HTML5", icons["html5"]),
    ("tech-css3.svg", "CSS3", icons["css3"]),
    ("tech-canvas.svg", "HTML5 Canvas", icons["canvas"]),
    ("tech-webapis.svg", "Web APIs", icons["webapis"]),
    ("tech-serviceworkers.svg", "Service Workers", icons["serviceworkers"]),
    ("tech-nextjs.svg", "Next.js 15+", icons["nextjs"]),
    ("tech-react.svg", "React 19", icons["react"]),
    ("tech-typescript.svg", "TypeScript", icons["typescript"]),
    ("tech-tailwindcss.svg", "Tailwind CSS", icons["tailwindcss"]),
    ("tech-pwa.svg", "PWA", icons["pwa"]),
    ("tech-supabase.svg", "Supabase", icons["supabase"]),
    ("tech-vercel.svg", "Vercel Edge", icons["vercel"]),
    ("tech-netlify.svg", "Netlify Edge", icons["netlify"]),
    ("tech-bash.svg", "Shell / Bash", icons["bash"]),
    ("tech-linux.svg", "Linux CLI", icons["linux"]),
    ("tech-termux.svg", "Android Termux", icons["termux"]),
    ("tech-markdown.svg", "Markdown", icons["markdown"]),
    ("tech-webspeech.svg", "Web Speech API", icons["webspeech"]),
    ("tech-localstorage.svg", "LocalStorage API", icons["localstorage"]),
    ("tech-dom.svg", "DOM Architecture", icons["dom"])
]

for filename, label, icon in badges:
    create_tech_badge(filename, label, icon)

print(f"Generated {len(badges)} technology badges.")

# ==============================================================================
# 4. HEADER SVGS (01 to 10)
# ==============================================================================
# Vector icons for project headers (22x22)
header_icons = {
    "01": """<rect x="2" y="1" width="16" height="20" rx="2" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<line x1="6" y1="6" x2="14" y2="6" stroke="#38bdf8" stroke-width="1.3"/>
<line x1="6" y1="10" x2="14" y2="10" stroke="#38bdf8" stroke-width="1.3"/>
<line x1="6" y1="14" x2="11" y2="14" stroke="#38bdf8" stroke-width="1.3"/>""",

    "02": """<rect x="1" y="2" width="20" height="17" rx="3" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<circle cx="6.5" cy="7.5" r="2" fill="#38bdf8"/>
<path d="M3 16L9 10L13 14L16 11L19 15" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>""",

    "03": """<path d="M11 2L19 5.5V11C19 16 11 20 11 20C11 20 3 16 3 11V5.5L11 2Z" stroke="#38bdf8" stroke-width="1.5" fill="#081b38" stroke-linejoin="round"/>
<circle cx="11" cy="10" r="2.5" fill="#38bdf8"/>""",

    "04": """<path d="M4 18C4 18 5 11 11 11M11 11C11 11 11 5 18 4C18 4 18 11 11 11M11 11C11 11 11 18 4 18Z" stroke="#38bdf8" stroke-width="1.5" fill="#081b38" stroke-linejoin="round"/>
<path d="M11 11C11 16 7 19 4 19" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round"/>""",

    "05": """<polygon points="12,1 4,12 11,12 10,21 18,10 11,10" stroke="#38bdf8" stroke-width="1.4" fill="#081b38" stroke-linejoin="round"/>""",

    "06": """<rect x="1" y="2" width="20" height="17" rx="3" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<path d="M5 7L9 10.5L5 14" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round"/>
<line x1="11" y1="14" x2="16" y2="14" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round"/>""",

    "07": """<rect x="1" y="4" width="20" height="15" rx="3" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<path d="M7 4L8.5 1.5H13.5L15 4" stroke="#38bdf8" stroke-width="1.3" fill="#081b38"/>
<circle cx="11" cy="11.5" r="4" stroke="#38bdf8" stroke-width="1.4" fill="none"/>
<circle cx="11" cy="11.5" r="1.5" fill="#38bdf8"/>""",

    "08": """<path d="M3 7H7L12 3V19L7 15H3V7Z" stroke="#38bdf8" stroke-width="1.4" fill="#081b38" stroke-linejoin="round"/>
<path d="M15 7C16.5 8.2 17.5 10 17.5 11C17.5 12 16.5 13.8 15 15" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round" fill="none"/>
<path d="M17.5 4C20 6 21 8.5 21 11C21 13.5 20 16 17.5 18" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round" fill="none"/>""",

    "09": """<rect x="2" y="2" width="18" height="18" rx="3" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<path d="M6 7L8 9L12 5" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="13" y1="8" x2="16" y2="8" stroke="#38bdf8" stroke-width="1.3"/>
<line x1="6" y1="13" x2="16" y2="13" stroke="#38bdf8" stroke-width="1.3"/>
<line x1="6" y1="16" x2="13" y2="16" stroke="#38bdf8" stroke-width="1.3"/>""",

    "10": """<rect x="1" y="2" width="20" height="17" rx="3" stroke="#38bdf8" stroke-width="1.4" fill="#081b38"/>
<line x1="1" y1="7" x2="21" y2="7" stroke="#38bdf8" stroke-width="1.2"/>
<circle cx="4" cy="4.5" r="1" fill="#38bdf8"/>
<circle cx="7" cy="4.5" r="1" fill="#38bdf8"/>
<line x1="5" y1="15" x2="8" y2="11" stroke="#38bdf8" stroke-width="1.4"/>
<line x1="8" y1="11" x2="11" y2="13" stroke="#38bdf8" stroke-width="1.4"/>
<line x1="11" y1="13" x2="16" y2="9" stroke="#38bdf8" stroke-width="1.4"/>"""
}

project_headers = [
    ("header-01.svg", "01", "PDFHub", "CLIENT-SIDE WEBASSEMBLY SUITE", True),
    ("header-02.svg", "02", "ImageHub", "IN-BROWSER GRAPHICS ENGINE", True),
    ("header-03.svg", "03", "CyberGuard YUVA", "CYBER DEFENSE PORTAL & COMMUNITY", True),
    ("header-04.svg", "04", "HabitsGrow (HabitFlow)", "PRODUCTIVITY & PERSONAL GROWTH PWA", True),
    ("header-05.svg", "05", "Advanced Image Compressor", "CLIENT-SIDE MULTI-FORMAT COMPRESSION UTILITY", True),
    ("header-06.svg", "06", "Termux Command Guide", "TECHNICAL DOCUMENTATION HANDBOOK", False),
    ("header-07.svg", "07", "Passport Photo Maker", "CLIENT-SIDE MEDIA TOOL", False),
    ("header-08.svg", "08", "Text to Audio Converter", "SPEECH SYNTHESIS TOOL", False),
    ("header-09.svg", "09", "Student Task Manager", "ACADEMIC WORKFLOW WEB TOOL", False),
    ("header-10.svg", "10", "Deployment Dashboard", "DEVOPS & MONITORING PROTOTYPE", False)
]

for filename, num, name, tagline, is_live in project_headers:
    status_markup = ""
    if is_live:
        status_markup = """<g transform="translate(778, 20)">
    <rect width="84" height="28" rx="5" fill="#022c22" stroke="#10b981" stroke-width="1.2" />
    <circle class="live-glow" cx="16" cy="14" r="5" fill="#34d399" />
    <circle class="live-core" cx="16" cy="14" r="3.2" fill="#10b981" />
    <circle cx="16" cy="14" r="1.5" fill="#ecfdf5" />
    <text x="28" y="18.5" fill="#34d399" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="800" letter-spacing="1px">LIVE</text>
  </g>"""
    else:
        status_markup = """<g transform="translate(718, 20)">
    <rect width="144" height="28" rx="5" fill="#0f172a" stroke="#334155" stroke-width="1.2" />
    <g transform="translate(11, 7.5)">
      <path d="M4 2.5L1 6L4 9.5" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M8 2.5L11 6L8 9.5" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <text x="30" y="18.5" fill="#94a3b8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="10.5" font-weight="700" letter-spacing="0.6px">REPOSITORY ONLY</text>
  </g>"""

    icon_vector = header_icons.get(num, "")
    esc_name = html.escape(name)
    esc_tagline = html.escape(tagline)

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
        0%, 100% {{ r: 5px; opacity: 0.35; }}
        50% {{ r: 8px; opacity: 0.85; }}
      }}
      @keyframes pulseCore {{
        0%, 100% {{ opacity: 0.9; }}
        50% {{ opacity: 1; }}
      }}
      .live-glow {{ animation: pulseGlow 2.2s ease-in-out infinite; }}
      .live-core {{ animation: pulseCore 2.2s ease-in-out infinite; }}
      @media (prefers-reduced-motion: reduce) {{
        .live-glow, .live-core {{ animation: none; }}
      }}
    </style>
  </defs>

  <!-- Card Header Container -->
  <rect x="0.5" y="0.5" width="879" height="67" rx="8" fill="url(#hdr-bg-{num})" stroke="#1e3a5f" stroke-width="1.2" />

  <!-- Top Accent Cyan Filament Line -->
  <rect x="14" y="1" width="260" height="2" rx="1" fill="url(#filament-{num})" />

  <!-- Project Number Badge Pill -->
  <rect x="18" y="17" width="76" height="34" rx="6" fill="#081b38" stroke="#0284c7" stroke-width="1.3" />
  <text x="25" y="39" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="13" font-weight="800" letter-spacing="1px">{num} / 10</text>

  <!-- Project Vector Icon -->
  <g transform="translate(108, 17)">
    {icon_vector}
  </g>

  <!-- Project Title -->
  <text x="138" y="34" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="17" font-weight="800" letter-spacing="0.3px">{esc_name}</text>

  <!-- Project Tagline -->
  <text x="139" y="51" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="10.5" font-weight="700" letter-spacing="1.2px">{esc_tagline}</text>

  <!-- Status Indicator Badge -->
  {status_markup}
</svg>"""

    with open(f"assets/cards/{filename}", "w", encoding="utf-8") as f:
        f.write(svg)

print(f"Generated {len(project_headers)} header SVGs.")
