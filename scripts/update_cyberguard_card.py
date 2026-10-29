import xml.etree.ElementTree as ET
import os

def create_header_02():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="68" viewBox="0 0 880 68" fill="none">
  <defs>
    <linearGradient id="hdr-bg-02" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#071126" />
      <stop offset="50%" stop-color="#0a193b" />
      <stop offset="100%" stop-color="#060c1d" />
    </linearGradient>
    <linearGradient id="filament-02" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#06b6d4" stop-opacity="1" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.1" />
    </linearGradient>
    <style>
      @keyframes pulseGlow {
        0%, 20% { r: 6px; opacity: 0.70; fill: #ffffff; filter: drop-shadow(0 0 4px rgba(255, 255, 255, 0.85)); }
        25%, 45% { r: 4.8px; opacity: 0.40; fill: #059669; filter: drop-shadow(0 0 3px rgba(5, 150, 105, 0.55)); }
        50%, 70% { r: 6.2px; opacity: 0.75; fill: #10b981; filter: drop-shadow(0 0 5px rgba(16, 185, 129, 0.80)); }
        75%, 95% { r: 7.2px; opacity: 0.90; fill: #6ee7b7; filter: drop-shadow(0 0 6px rgba(110, 231, 183, 0.90)); }
        100% { r: 6px; opacity: 0.70; fill: #ffffff; filter: drop-shadow(0 0 4px rgba(255, 255, 255, 0.85)); }
      }
      @keyframes pulseCore {
        0%, 20% { fill: #ffffff; }
        25%, 45% { fill: #047857; }
        50%, 70% { fill: #10b981; }
        75%, 95% { fill: #34d399; }
        100% { fill: #ffffff; }
      }
      @keyframes pulseHighlight {
        0%, 20% { opacity: 1; fill: #ffffff; r: 1.6px; }
        25%, 45% { opacity: 0.45; fill: #6ee7b7; r: 1.2px; }
        50%, 70% { opacity: 0.85; fill: #ffffff; r: 1.4px; }
        75%, 95% { opacity: 1; fill: #ffffff; r: 1.6px; }
        100% { opacity: 1; fill: #ffffff; r: 1.6px; }
      }
      @keyframes pulseText {
        0%, 20% { fill: #f8fafc; filter: drop-shadow(0 0 1.5px rgba(255, 255, 255, 0.5)); }
        25%, 45% { fill: #34d399; filter: none; }
        50%, 70% { fill: #34d399; filter: drop-shadow(0 0 2px rgba(16, 185, 129, 0.5)); }
        75%, 95% { fill: #6ee7b7; filter: drop-shadow(0 0 3px rgba(110, 231, 183, 0.6)); }
        100% { fill: #f8fafc; filter: drop-shadow(0 0 1.5px rgba(255, 255, 255, 0.5)); }
      }
      .live-glow { animation: pulseGlow 2.8s ease-in-out infinite; }
      .live-core { animation: pulseCore 2.8s ease-in-out infinite; }
      .live-highlight { animation: pulseHighlight 2.8s ease-in-out infinite; }
      .live-text { animation: pulseText 2.8s ease-in-out infinite; }
      @media (prefers-reduced-motion: reduce) {
        .live-glow, .live-core, .live-highlight, .live-text { animation: none; }
      }
    </style>
  </defs>

  <!-- Card Header Container -->
  <rect x="0.5" y="0.5" width="879" height="67" rx="8" fill="url(#hdr-bg-02)" stroke="#1e3a5f" stroke-width="1.2" />

  <!-- Top Accent Cyan Filament Line -->
  <rect x="14" y="1" width="260" height="2" rx="1" fill="url(#filament-02)" />

  <!-- Project Number Badge Pill -->
  <rect x="18" y="17" width="76" height="34" rx="6" fill="#081b38" stroke="#0284c7" stroke-width="1.3" />
  <text x="25" y="39" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="13" font-weight="800" letter-spacing="1px">02 / 11</text>

  <!-- Project Vector Icon -->
  <g transform="translate(108, 17)">
    <path d="M11 2L19 5.5V11C19 16 11 20 11 20C11 20 3 16 3 11V5.5L11 2Z" stroke="#38bdf8" stroke-width="1.5" fill="#081b38" stroke-linejoin="round"/>
    <circle cx="11" cy="10" r="2.5" fill="#38bdf8"/>
  </g>

  <!-- Project Title -->
  <text x="138" y="34" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="17" font-weight="800" letter-spacing="0.3px">CyberGuard YUVA</text>

  <!-- Project Tagline -->
  <text x="139" y="51" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="10" font-weight="700" letter-spacing="1.2px">YOUTH CYBER DEFENSE &amp; AWARENESS PLATFORM</text>

  <!-- Top Banner LIVE Status Pill -->
  <g transform="translate(778, 20)">
    <rect width="84" height="28" rx="5" fill="#022c22" stroke="#10b981" stroke-width="1.2" />
    <circle class="live-glow" cx="16" cy="14" r="6" fill="#ffffff" opacity="0.70">
      <animate attributeName="fill" values="#ffffff;#ffffff;#059669;#059669;#10b981;#10b981;#6ee7b7;#6ee7b7;#ffffff" keyTimes="0;0.20;0.25;0.45;0.50;0.70;0.75;0.95;1" dur="2.8s" repeatCount="indefinite" />
      <animate attributeName="r" values="6;6;4.8;4.8;6.2;6.2;7.2;7.2;6" keyTimes="0;0.20;0.25;0.45;0.50;0.70;0.75;0.95;1" dur="2.8s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.70;0.70;0.40;0.40;0.75;0.75;0.90;0.90;0.70" keyTimes="0;0.20;0.25;0.45;0.50;0.70;0.75;0.95;1" dur="2.8s" repeatCount="indefinite" />
    </circle>
    <circle class="live-core" cx="16" cy="14" r="3.2" fill="#ffffff">
      <animate attributeName="fill" values="#ffffff;#ffffff;#047857;#047857;#10b981;#10b981;#34d399;#34d399;#ffffff" keyTimes="0;0.20;0.25;0.45;0.50;0.70;0.75;0.95;1" dur="2.8s" repeatCount="indefinite" />
    </circle>
    <circle class="live-highlight" cx="16" cy="14" r="1.5" fill="#ffffff">
      <animate attributeName="fill" values="#ffffff;#ffffff;#6ee7b7;#6ee7b7;#ffffff;#ffffff;#ffffff;#ffffff;#ffffff" keyTimes="0;0.20;0.25;0.45;0.50;0.70;0.75;0.95;1" dur="2.8s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="1;1;0.45;0.45;0.85;0.85;1;1;1" keyTimes="0;0.20;0.25;0.45;0.50;0.70;0.75;0.95;1" dur="2.8s" repeatCount="indefinite" />
    </circle>
    <text class="live-text" x="28" y="18.5" fill="#34d399" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="800" letter-spacing="1px">
      LIVE
      <animate attributeName="fill" values="#f8fafc;#f8fafc;#34d399;#34d399;#34d399;#34d399;#6ee7b7;#6ee7b7;#f8fafc" keyTimes="0;0.20;0.25;0.45;0.50;0.70;0.75;0.95;1" dur="2.8s" repeatCount="indefinite" />
    </text>
  </g>
</svg>'''
    ET.fromstring(svg) # validate XML
    return svg

def create_cyberguard_panel():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="210" viewBox="0 0 880 210" fill="none">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="panel-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#071126" />
      <stop offset="50%" stop-color="#0a193b" />
      <stop offset="100%" stop-color="#060c1d" />
    </linearGradient>

    <!-- Top Accent Cyan Filament Line -->
    <linearGradient id="panel-filament" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#06b6d4" stop-opacity="1" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.1" />
    </linearGradient>

    <!-- Focus Card Gradient -->
    <linearGradient id="focus-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#091838" />
      <stop offset="100%" stop-color="#061026" />
    </linearGradient>
  </defs>

  <!-- Container Box -->
  <rect x="0.5" y="0.5" width="879" height="209" rx="8" fill="url(#panel-bg)" stroke="#1e3a5f" stroke-width="1.2" />

  <!-- Top Filament Line -->
  <rect x="14" y="1" width="220" height="2" rx="1" fill="url(#panel-filament)" />

  <!-- Top Bar: Organization Identity & Mission Motto -->
  <g transform="translate(24, 14)">
    <!-- Shield Emblem Icon -->
    <path d="M7 1L13 3.8V8C13 12 7 15 7 15C7 15 1 12 1 8V3.8L7 1Z" stroke="#38bdf8" stroke-width="1.4" fill="#081b38" stroke-linejoin="round"/>
    <circle cx="7" cy="7.5" r="1.8" fill="#38bdf8"/>
    <text x="22" y="12" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="11" font-weight="800" letter-spacing="1.2px">YOUTH CYBER DEFENSE CLUB</text>
  </g>

  <!-- Organization Motto Pill (Right Aligned) -->
  <g transform="translate(614, 13)">
    <rect width="242" height="22" rx="4" fill="#081b38" stroke="#0284c7" stroke-width="1" />
    <text x="14" y="15" fill="#38bdf8" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="9" font-weight="800" letter-spacing="1.2px">SECURE • EDUCATE • EMPOWER</text>
  </g>

  <!-- Subtitle & Mission Statement -->
  <g transform="translate(24, 44)">
    <line x1="0" y1="0" x2="832" y2="0" stroke="#1e3a5f" stroke-width="0.8" stroke-dasharray="4 4" />
    <text x="0" y="17" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="700" letter-spacing="0.2px">Defensive Cyber Literacy &amp; Student Safety Initiative</text>
    <text x="0" y="34" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="11" font-weight="450" letter-spacing="0.1px">Official web portal and digital learning hub dedicated to cultivating defensive technical literacy, student privacy hygiene, and safe digital practices across schools and universities.</text>
  </g>

  <!-- Key Focus Areas Grid (4 Columns) -->
  <!-- Focus Area 01: Cyber Awareness -->
  <g transform="translate(24, 94)">
    <rect width="193" height="98" rx="6" fill="url(#focus-card-bg)" stroke="#1e3a5f" stroke-width="1.1" />
    <rect x="6" y="0" width="36" height="2" rx="1" fill="#38bdf8" />
    <text x="12" y="20" fill="#0284c7" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="9.5" font-weight="800">01</text>
    <text x="32" y="20" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="700">Cyber Awareness</text>
    <circle cx="16" cy="42" r="2" fill="#38bdf8" />
    <text x="24" y="45" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Defensive literacy</text>
    <circle cx="16" cy="60" r="2" fill="#38bdf8" />
    <text x="24" y="63" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Threat hygiene matrices</text>
    <circle cx="16" cy="78" r="2" fill="#38bdf8" />
    <text x="24" y="81" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Campus initiatives</text>
  </g>

  <!-- Focus Area 02: Digital Safety -->
  <g transform="translate(237, 94)">
    <rect width="193" height="98" rx="6" fill="url(#focus-card-bg)" stroke="#1e3a5f" stroke-width="1.1" />
    <rect x="6" y="0" width="36" height="2" rx="1" fill="#38bdf8" />
    <text x="12" y="20" fill="#0284c7" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="9.5" font-weight="800">02</text>
    <text x="32" y="20" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="700">Digital Safety</text>
    <circle cx="16" cy="42" r="2" fill="#38bdf8" />
    <text x="24" y="45" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Student privacy hygiene</text>
    <circle cx="16" cy="60" r="2" fill="#38bdf8" />
    <text x="24" y="63" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Phishing resistance</text>
    <circle cx="16" cy="78" r="2" fill="#38bdf8" />
    <text x="24" y="81" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Safe device habits</text>
  </g>

  <!-- Focus Area 03: Youth Education -->
  <g transform="translate(450, 94)">
    <rect width="193" height="98" rx="6" fill="url(#focus-card-bg)" stroke="#1e3a5f" stroke-width="1.1" />
    <rect x="6" y="0" width="36" height="2" rx="1" fill="#38bdf8" />
    <text x="12" y="20" fill="#0284c7" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="9.5" font-weight="800">03</text>
    <text x="32" y="20" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="700">Youth Education</text>
    <circle cx="16" cy="42" r="2" fill="#38bdf8" />
    <text x="24" y="45" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Interactive playbooks</text>
    <circle cx="16" cy="60" r="2" fill="#38bdf8" />
    <text x="24" y="63" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">CTF prep sessions</text>
    <circle cx="16" cy="78" r="2" fill="#38bdf8" />
    <text x="24" y="81" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Curated study tracks</text>
  </g>

  <!-- Focus Area 04: Responsible Use -->
  <g transform="translate(663, 94)">
    <rect width="193" height="98" rx="6" fill="url(#focus-card-bg)" stroke="#1e3a5f" stroke-width="1.1" />
    <rect x="6" y="0" width="36" height="2" rx="1" fill="#38bdf8" />
    <text x="12" y="20" fill="#0284c7" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="9.5" font-weight="800">04</text>
    <text x="32" y="20" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="700">Responsible Use</text>
    <circle cx="16" cy="42" r="2" fill="#38bdf8" />
    <text x="24" y="45" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Ethical navigation</text>
    <circle cx="16" cy="60" r="2" fill="#38bdf8" />
    <text x="24" y="63" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Digital citizenship</text>
    <circle cx="16" cy="78" r="2" fill="#38bdf8" />
    <text x="24" y="81" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="450">Student peer safety</text>
  </g>
</svg>'''
    ET.fromstring(svg) # validate XML
    return svg

def update_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    start_tag = '<!-- PROJECT 02 — COMPLETE CARD: CyberGuard YUVA'
    end_tag = '<!-- PROJECT 03 — COMPLETE CARD: PDFHub'

    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)

    if start_idx == -1 or end_idx == -1:
        raise ValueError(f"Could not locate Project 02 boundaries (start: {start_idx}, end: {end_idx})")

    new_project_02 = '''<!-- PROJECT 02 — COMPLETE CARD: CyberGuard YUVA                              -->
<!-- ================================================================= -->

<a id="02-cyberguard-yuva"></a>
<a id="03-cyberguard-yuva"></a>
<table width="100%">
<tr>
<td align="center">

<a href="https://cyberguard-yuva.vercel.app/"><img src="assets/cyberguard-preview.png" alt="02 / 11 — CyberGuard YUVA Youth Cyber Defense Portal Preview" width="100%" style="border-radius: 8px 8px 0 0; border: 1px solid #1e3a5f;" /></a>

</td>
</tr>
<tr>
<td align="left">

<img src="assets/cards/header-02.svg" alt="02 / 11 — CyberGuard YUVA | Youth Cyber Defense &amp; Awareness Platform" width="100%" />

<br /><br />

<img src="assets/cards/cyberguard-panel.svg" alt="CyberGuard YUVA — Youth Cyber Defense &amp; Awareness Platform | Mission &amp; Focus Areas: Cyber Awareness, Digital Safety, Youth Education, Responsible Internet Use" width="100%" />

<br /><br />

<img src="assets/tech/tech-nextjs.svg" height="24" alt="Next.js 15+" /> <img src="assets/tech/tech-react.svg" height="24" alt="React 19" /> <img src="assets/tech/tech-typescript.svg" height="24" alt="TypeScript" /> <img src="assets/tech/tech-tailwindcss.svg" height="24" alt="Tailwind CSS" /> <img src="assets/tech/tech-vercel.svg" height="24" alt="Vercel Edge" />

<br /><br />

<a href="https://cyberguard-yuva.vercel.app/"><img src="assets/buttons/btn-live-demo.svg" height="34" alt="Launch Live Demo" /></a> &nbsp;&nbsp; <img src="assets/buttons/btn-private-codebase.svg" height="34" alt="Private Codebase" /> &nbsp;&nbsp; <a href="PROJECTS.md#03-cyberguard-yuva"><img src="assets/buttons/btn-project-specs.svg" height="34" alt="Read Technical Dossier" /></a>

</td>
</tr>
</table>

<br />

<!-- ================================================================= -->
'''

    # Ensure consistent CRLF line endings matching original README
    if '\r\n' in content:
        new_project_02 = new_project_02.replace('\r\n', '\n').replace('\n', '\r\n')

    updated_content = content[:start_idx] + new_project_02 + content[end_idx:]

    with open('README.md', 'w', encoding='utf-8', newline='') as f:
        f.write(updated_content)

    print("README.md Section 04 Project 02 updated successfully.")

def main():
    header_svg = create_header_02()
    panel_svg = create_cyberguard_panel()

    with open('assets/cards/header-02.svg', 'w', encoding='utf-8') as f:
        f.write(header_svg)
    print("Updated assets/cards/header-02.svg successfully.")

    with open('assets/cards/cyberguard-panel.svg', 'w', encoding='utf-8') as f:
        f.write(panel_svg)
    print("Created assets/cards/cyberguard-panel.svg successfully.")

    update_readme()

if __name__ == '__main__':
    main()
