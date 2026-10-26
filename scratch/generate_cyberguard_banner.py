import re

# Read the base64 logo from assets/cyberguard-emblem.svg
with open("assets/cyberguard-emblem.svg", "r", encoding="utf-8") as f:
    emblem_svg = f.read()

m = re.search(r'data:image/png;base64,([A-Za-z0-9+/=]+)', emblem_svg)
assert m, "Could not find base64 data in assets/cyberguard-emblem.svg"
base64_data = m.group(0)

banner_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="260" viewBox="0 0 880 260" fill="none">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="cgb-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#071126" />
      <stop offset="50%" stop-color="#0a193b" />
      <stop offset="100%" stop-color="#060c1d" />
    </linearGradient>

    <!-- Top Accent Filament Gradient -->
    <linearGradient id="cgb-filament" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#06b6d4" stop-opacity="1" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.1" />
    </linearGradient>

    <!-- Ambient Cyan Radial Glow Behind Logo -->
    <radialGradient id="cgb-logo-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.32" />
      <stop offset="60%" stop-color="#0284c7" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#0a193b" stop-opacity="0" />
    </radialGradient>

    <!-- Status Indicator Background -->
    <linearGradient id="cgb-status-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#022c22" />
      <stop offset="100%" stop-color="#064e3b" />
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

  <!-- Main Card Body Container -->
  <rect x="0.5" y="0.5" width="879" height="259" rx="12" fill="url(#cgb-bg)" stroke="#1e3a5f" stroke-width="1.5" />

  <!-- Top Cyan Filament Accent Line -->
  <rect x="20" y="2" width="340" height="2.5" rx="1" fill="url(#cgb-filament)" />

  <!-- Corner Brackets (Cyber Defense Motif) -->
  <path d="M 12 24 V 12 H 24" stroke="#38bdf8" stroke-width="1.6" fill="none" />
  <path d="M 856 12 H 868 V 24" stroke="#38bdf8" stroke-width="1.6" fill="none" />
  <path d="M 12 236 V 248 H 24" stroke="#38bdf8" stroke-width="1.6" fill="none" />
  <path d="M 856 248 H 868 V 236" stroke="#38bdf8" stroke-width="1.6" fill="none" />

  <!-- LEFT HERO SECTION: Logo Frame & Ambient Halo -->
  <g transform="translate(32, 28)">
    <!-- Radial Ambient Lighting -->
    <circle cx="102" cy="102" r="98" fill="url(#cgb-logo-glow)" />

    <!-- Sleek Outer Cybernetic Ring -->
    <circle cx="102" cy="102" r="95" stroke="#1e3a5f" stroke-width="1.4" fill="none" />
    <circle cx="102" cy="102" r="88" stroke="#0284c7" stroke-width="1" stroke-dasharray="10 8" fill="none" />

    <!-- Center Base Background for Logo -->
    <circle cx="102" cy="102" r="80" fill="#08142c" stroke="#1e3a5f" stroke-width="1" />

    <!-- Official CyberGuard YUVA Logo (100% Unaltered 1:1 Aspect Ratio) -->
    <image href="{base64_data}" x="22" y="22" width="160" height="160" preserveAspectRatio="xMidYMid meet" />
  </g>

  <!-- RIGHT HERO SECTION: Typography & Information Architecture -->
  <g transform="translate(262, 0)">
    <!-- Category Pill Badge -->
    <rect x="0" y="28" width="242" height="26" rx="5" fill="#081b38" stroke="#0284c7" stroke-width="1.2" />
    <circle cx="14" cy="41" r="3.5" fill="#38bdf8" />
    <text x="25" y="45" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="10.5" font-weight="800" letter-spacing="1.2px">DEFENSIVE CYBER INITIATIVE</text>

    <!-- Verified Live Status Badge (Top Right) -->
    <g transform="translate(516, 28)">
      <rect width="84" height="26" rx="5" fill="url(#cgb-status-bg)" stroke="#10b981" stroke-width="1.2" />
      <circle class="live-glow" cx="15" cy="13" r="5" fill="#34d399" />
      <circle class="live-core" cx="15" cy="13" r="3.2" fill="#10b981" />
      <circle class="live-highlight" cx="15" cy="13" r="1.5" fill="#ffffff" />
      <text x="27" y="17" fill="#34d399" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="800" letter-spacing="1px">LIVE</text>
    </g>

    <!-- Project Title -->
    <text x="0" y="93" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="28" font-weight="900" letter-spacing="0.3px">CyberGuard YUVA</text>

    <!-- Subtitle / Club Role -->
    <text x="1" y="119" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="14.5" font-weight="700" letter-spacing="0.8px">Youth Cyber Defense Club &amp; Community</text>

    <!-- Slogan Pill Banner -->
    <rect x="0" y="137" width="375" height="28" rx="6" fill="#0c1d3f" stroke="#1e3a5f" stroke-width="1" />
    <text x="16" y="155.5" fill="#93c5fd" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="12" font-weight="800" letter-spacing="2px">SECURE &#160;•&#160; EDUCATE &#160;•&#160; EMPOWER</text>

    <!-- Supporting Mission Line -->
    <text x="1" y="191" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="12.5" font-weight="500">Cultivating Defensive Literacy, Privacy Hygiene &amp; Threat Resistance</text>

    <!-- Tech Stack Pill Row -->
    <g transform="translate(1, 209)">
      <rect x="0" y="0" width="68" height="20" rx="4" fill="#081b38" stroke="#1e3a5f" stroke-width="0.9" />
      <text x="8" y="13.5" fill="#94a3b8" font-family="ui-monospace, monospace" font-size="9.5" font-weight="700">Next.js 15+</text>

      <rect x="74" y="0" width="62" height="20" rx="4" fill="#081b38" stroke="#1e3a5f" stroke-width="0.9" />
      <text x="82" y="13.5" fill="#94a3b8" font-family="ui-monospace, monospace" font-size="9.5" font-weight="700">React 19</text>

      <rect x="142" y="0" width="76" height="20" rx="4" fill="#081b38" stroke="#1e3a5f" stroke-width="0.9" />
      <text x="150" y="13.5" fill="#94a3b8" font-family="ui-monospace, monospace" font-size="9.5" font-weight="700">TypeScript</text>

      <rect x="224" y="0" width="84" height="20" rx="4" fill="#081b38" stroke="#1e3a5f" stroke-width="0.9" />
      <text x="232" y="13.5" fill="#94a3b8" font-family="ui-monospace, monospace" font-size="9.5" font-weight="700">Tailwind CSS</text>

      <rect x="314" y="0" width="76" height="20" rx="4" fill="#081b38" stroke="#1e3a5f" stroke-width="0.9" />
      <text x="322" y="13.5" fill="#94a3b8" font-family="ui-monospace, monospace" font-size="9.5" font-weight="700">Vercel Edge</text>
    </g>

    <!-- Verified Domain Callout -->
    <text x="600" y="224" text-anchor="end" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="700">cyberguard-yuva.vercel.app ↗</text>
  </g>
</svg>"""

with open("assets/cyberguard-banner.svg", "w", encoding="utf-8") as f:
    f.write(banner_svg)

print("assets/cyberguard-banner.svg created successfully.")
