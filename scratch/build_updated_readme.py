import os
import re

# The 11 projects data in the requested new order:
# 01 - Shop (Net Gallery Hb)
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

projects = [
    {
        "num": "01",
        "id": "01-shop",
        "old_id": "11-shop",
        "name": "Shop (Net Gallery Hb)",
        "tagline": "DIGITAL & PRINTING SERVICES PLATFORM",
        "status": "LIVE",
        "preview": "assets/shop-preview.svg",
        "preview_alt": "01 / 11 — Shop (Net Gallery Hb) Preview Banner",
        "link_preview": "https://net-gallery-hb.netlify.app/",
        "desc_heading": "Professional Digital & Local Printing Services Hub",
        "desc_body": "A dedicated commercial service portal for Net Gallery Hb providing local citizens and students with official digital document processing, CSC governance services, custom photo merchandise, and on-demand professional printing.",
        "highlights": [
            "Government & Citizen Services assistance (CSC, Golden Card, PAN, Voter ID, Driving Licence)",
            "Professional digital photo printing, custom phone covers, photo framing & passport photos",
            "Responsive booking requests, live pricing matrix, instant WhatsApp integration & UPI payments"
        ],
        "tech_badges": [
            ("tech-html5.svg", "HTML5"),
            ("tech-css3.svg", "CSS3"),
            ("tech-javascript.svg", "JavaScript"),
            ("tech-dom.svg", "Responsive DOM"),
            ("tech-netlify.svg", "Netlify Edge")
        ],
        "status_badge": "assets/badge-live.svg",
        "actions": [
            ("btn-live-demo.svg", "https://net-gallery-hb.netlify.app/", "Launch Live Demo"),
            ("btn-private-codebase.svg", None, "Private Codebase"),
            ("btn-project-specs.svg", "PROJECTS.md#11-shop", "Read Technical Dossier")
        ]
    },
    {
        "num": "02",
        "id": "02-cyberguard-yuva",
        "old_id": "03-cyberguard-yuva",
        "name": "CyberGuard YUVA",
        "tagline": "CYBER DEFENSE PORTAL & COMMUNITY",
        "status": "LIVE",
        "preview": "assets/cyberguard-preview.png",
        "preview_alt": "02 / 11 — CyberGuard YUVA Youth Cyber Defense Portal Preview",
        "link_preview": "https://cyberguard-yuva.vercel.app/",
        "desc_heading": "Defensive Cyber Literacy & Student Safety Initiative",
        "desc_body": "Official web portal and digital learning hub for CyberGuard YUVA, a youth-led cyber defense initiative dedicated to cultivating defensive technical literacy, student privacy hygiene, and safe digital practices across schools and universities.",
        "highlights": [
            "Interactive student manuals, phishing resistance playbooks & threat hygiene matrices",
            "Modern SSR & Edge computing architecture engineered with Next.js 15+ and React 19",
            "Campus awareness programs, CTF preparation sessions & student cyber literacy"
        ],
        "tech_badges": [
            ("tech-nextjs.svg", "Next.js 15+"),
            ("tech-react.svg", "React 19"),
            ("tech-typescript.svg", "TypeScript"),
            ("tech-tailwindcss.svg", "Tailwind CSS"),
            ("tech-vercel.svg", "Vercel Edge")
        ],
        "status_badge": "assets/badge-live.svg",
        "actions": [
            ("btn-live-demo.svg", "https://cyberguard-yuva.vercel.app/", "Launch Live Demo"),
            ("btn-private-codebase.svg", None, "Private Codebase"),
            ("btn-project-specs.svg", "PROJECTS.md#03-cyberguard-yuva", "Read Technical Dossier")
        ]
    },
    {
        "num": "03",
        "id": "03-pdfhub",
        "old_id": "01-pdfhub",
        "name": "PDFHub",
        "tagline": "CLIENT-SIDE WEBASSEMBLY SUITE",
        "status": "LIVE",
        "preview": "assets/pdfhub-preview.png",
        "preview_alt": "03 / 11 — PDFHub Application Interface Preview",
        "link_preview": "https://pdfshub.netlify.app/",
        "desc_heading": "Privacy-First WebAssembly Architecture",
        "desc_body": "A comprehensive, privacy-first PDF utility suite engineered to execute 100% within the browser. Files are processed locally on the client device using WebAssembly and client-side JavaScript engines, guaranteeing that sensitive documents never touch external servers.",
        "highlights": [
            "33 specialized tools (merge, split, organize, compress, client-side OCR, repair, conversion)",
            "100% in-browser processing via WebAssembly and Web Workers — zero server uploads",
            "Offline PWA capability with persistent client state"
        ],
        "tech_badges": [
            ("tech-javascript.svg", "JavaScript (ES6+)"),
            ("tech-webassembly.svg", "WebAssembly"),
            ("tech-pdflib.svg", "pdf-lib"),
            ("tech-pdfjs.svg", "pdf.js"),
            ("tech-canvas.svg", "HTML5 Canvas"),
            ("tech-netlify.svg", "Netlify Edge")
        ],
        "status_badge": "assets/badge-live.svg",
        "actions": [
            ("btn-live-demo.svg", "https://pdfshub.netlify.app/", "Launch Live Demo"),
            ("btn-view-repo.svg", "https://github.com/officialhazim42/pdfshub", "View GitHub Repository"),
            ("btn-project-specs.svg", "PROJECTS.md#01-pdfhub", "Read Technical Dossier")
        ]
    },
    {
        "num": "04",
        "id": "04-imagehub",
        "old_id": "02-imagehub",
        "name": "ImageHub",
        "tagline": "13 FREE IN-BROWSER IMAGE TOOLS ONLINE",
        "status": "LIVE",
        "preview": "assets/imagehub-preview.svg",
        "preview_alt": "04 / 11 — ImageHub Graphics Engine Interface Preview",
        "link_preview": "https://images-hub.netlify.app/pages/index.html",
        "desc_heading": "Production-Grade Client-Side Image Manipulation",
        "desc_body": "A production-grade, client-side digital image manipulation platform running locally in the web browser. Empowers users to compress, upscale, isolate subjects, crop, resize, and convert graphics without transmitting a single byte over the network.",
        "highlights": [
            "Zero server dependencies with high-throughput HTML5 Canvas rendering",
            "Multi-format conversion (JPG, PNG, WebP, AVIF) with instant client-side processing",
            "Offline-first PWA with Service Worker caching and zero telemetry tracking"
        ],
        "tech_badges": [
            ("tech-javascript.svg", "Pure JavaScript"),
            ("tech-canvas.svg", "HTML5 Canvas"),
            ("tech-css3.svg", "CSS3"),
            ("tech-webapis.svg", "Web APIs"),
            ("tech-serviceworkers.svg", "Service Workers"),
            ("tech-netlify.svg", "Netlify Edge")
        ],
        "status_badge": "assets/badge-live.svg",
        "actions": [
            ("btn-live-demo.svg", "https://images-hub.netlify.app/pages/index.html", "Launch Live Demo"),
            ("btn-view-repo.svg", "https://github.com/officialhazim42/imagehub", "View GitHub Repository"),
            ("btn-project-specs.svg", "PROJECTS.md#02-imagehub", "Read Technical Dossier")
        ]
    },
    {
        "num": "05",
        "id": "05-habitsgrow",
        "old_id": "04-habitsgrow",
        "name": "HabitsGrow",
        "tagline": "GROW BETTER EVERY DAY",
        "status": "LIVE",
        "preview": "assets/habitsgrow-preview.png",
        "preview_alt": "05 / 11 — HabitsGrow Routine Tracker Interface Preview",
        "link_preview": "https://habitsgrow.netlify.app/",
        "desc_heading": "Privacy-Centric Routine & Streak Analytics",
        "desc_body": "A responsive, privacy-centric Progressive Web App designed to help individuals build positive routines, maintain completion consistency streaks, visualize progress analytics, and document mindfulness reflections.",
        "highlights": [
            "Daily habit tracking with category grouping, routine checklists & streak trends",
            "Offline-first PWA with Service Worker synchronization & Web App Manifest",
            "Cloud state persistence backed by Supabase with Row Level Security (RLS)"
        ],
        "tech_badges": [
            ("tech-javascript.svg", "JavaScript (ES6+)"),
            ("tech-pwa.svg", "PWA"),
            ("tech-serviceworkers.svg", "Service Workers"),
            ("tech-supabase.svg", "Supabase"),
            ("tech-html5.svg", "HTML5"),
            ("tech-css3.svg", "CSS3")
        ],
        "status_badge": "assets/badge-live.svg",
        "actions": [
            ("btn-live-demo.svg", "https://habitsgrow.netlify.app/", "Launch Live Demo"),
            ("btn-private-codebase.svg", None, "Private Codebase"),
            ("btn-project-specs.svg", "PROJECTS.md#04-habitsgrow", "Read Technical Dossier")
        ]
    },
    {
        "num": "06",
        "id": "06-advance-image-compressor",
        "old_id": "05-advance-image-compressor",
        "name": "Advanced Image Compressor",
        "tagline": "CLIENT-SIDE MULTI-FORMAT COMPRESSION UTILITY",
        "status": "LIVE",
        "preview": "assets/compressor-preview.svg",
        "preview_alt": "06 / 11 — Advanced Image Compressor Interface Preview",
        "link_preview": "https://advance-images-compressor.netlify.app/",
        "desc_heading": "High-Efficiency In-Browser Multi-Format Compression",
        "desc_body": "A focused, responsive web tool engineered for ultra-fast image compression with real-time compression ratios and format detection, packaged in a sleek dark glassmorphic UI.",
        "highlights": [
            "Modern AVIF compression engine supporting JPG, PNG, WebP & next-gen AVIF",
            "Real-time compression metrics, dynamic before/after previews & file size ratios",
            "Automated batch sequential renaming & organized archive exports"
        ],
        "tech_badges": [
            ("tech-html5.svg", "HTML5"),
            ("tech-css3.svg", "CSS3"),
            ("tech-javascript.svg", "Vanilla JavaScript"),
            ("tech-canvas.svg", "HTML5 Canvas"),
            ("tech-webapis.svg", "Web APIs"),
            ("tech-netlify.svg", "Netlify Edge")
        ],
        "status_badge": "assets/badge-live.svg",
        "actions": [
            ("btn-live-demo.svg", "https://advance-images-compressor.netlify.app/", "Launch Live Demo"),
            ("btn-view-repo.svg", "https://github.com/officialhazim42/Advance-Image-Compressor", "View GitHub Repository"),
            ("btn-project-specs.svg", "PROJECTS.md#05-advance-image-compressor", "Read Technical Dossier")
        ]
    },
    {
        "num": "07",
        "id": "07-termux-command-guide",
        "old_id": "06-termux-command-guide",
        "name": "Termux Command Guide",
        "tagline": "TECHNICAL DOCUMENTATION HANDBOOK",
        "status": "REPOSITORY ONLY",
        "preview": "assets/termux-preview.svg",
        "preview_alt": "07 / 11 — Termux Command Guide Terminal Handbook Preview",
        "link_preview": "https://github.com/officialhazim42/Termux-Command-Listbook",
        "desc_heading": "Native Android Terminal Operations & Hardware APIs",
        "desc_body": "A structured, practical reference handbook and command guide for mastering native Linux command-line operations and device integration APIs within the Termux Android terminal environment.",
        "highlights": [
            "Categorized Linux command index, package configurations & dev setups",
            "Practical recipes for interfacing with Android hardware sensors, storage & device APIs",
            "On-device development environment setup guides (Git, Node.js, Python)"
        ],
        "tech_badges": [
            ("tech-bash.svg", "Shell / Bash"),
            ("tech-linux.svg", "Linux CLI"),
            ("tech-termux.svg", "Android Termux"),
            ("tech-markdown.svg", "Markdown")
        ],
        "status_badge": "assets/badge-repo-only.svg",
        "actions": [
            ("btn-view-repo.svg", "https://github.com/officialhazim42/Termux-Command-Listbook", "View GitHub Repository"),
            ("btn-project-specs.svg", "PROJECTS.md#06-termux-command-guide", "Read Technical Dossier")
        ]
    },
    {
        "num": "08",
        "id": "08-passport-photo-maker",
        "old_id": "07-passport-photo-maker",
        "name": "Passport Photo Maker",
        "tagline": "CLIENT-SIDE MEDIA TOOL",
        "status": "REPOSITORY ONLY",
        "preview": "assets/passport-preview.svg",
        "preview_alt": "08 / 11 — Passport Photo Maker Grid Tool Preview",
        "link_preview": "https://github.com/officialhazim42/Passportsize-photo-maker",
        "desc_heading": "Standard Dimensions & Multi-Photo Print Generator",
        "desc_body": "A client-side utility built with HTML5 Canvas that enables users to crop, scale, and format photographs to international passport standards and generate multi-photo sheets ready for printing.",
        "highlights": [
            "Standard dimension presets supporting international passport standards (2x2 inch, 35x45mm)",
            "Automatic multi-photo tiling onto printable standard sheets",
            "100% in-browser HTML5 Canvas processing with instant high-resolution PNG export"
        ],
        "tech_badges": [
            ("tech-html5.svg", "HTML5"),
            ("tech-css3.svg", "CSS3"),
            ("tech-javascript.svg", "Vanilla JavaScript"),
            ("tech-canvas.svg", "Canvas API")
        ],
        "status_badge": "assets/badge-repo-only.svg",
        "actions": [
            ("btn-view-repo.svg", "https://github.com/officialhazim42/Passportsize-photo-maker", "View GitHub Repository"),
            ("btn-project-specs.svg", "PROJECTS.md#07-passport-photo-maker", "Read Technical Dossier")
        ]
    },
    {
        "num": "09",
        "id": "09-text-to-audio",
        "old_id": "08-text-to-audio",
        "name": "Text to Audio Converter",
        "tagline": "SPEECH SYNTHESIS TOOL",
        "status": "REPOSITORY ONLY",
        "preview": "assets/audio-preview.svg",
        "preview_alt": "09 / 11 — Text to Audio Converter Speech Engine Preview",
        "link_preview": "https://github.com/officialhazim42/Text-to-Audio-Converter",
        "desc_heading": "Native Browser Speech Synthesis & Audio Controls",
        "desc_body": "A lightweight web tool leveraging the browser-native Web Speech Synthesis API to convert written text into spoken audio with real-time controls for pitch, speech rate, and voice accents.",
        "highlights": [
            "Hardware-accelerated speech synthesis using native browser speech engines with zero external APIs",
            "Real-time audio adjustment sliders for speech rate, pitch tuning & voice accents",
            "Zero dependencies with 100% vanilla client execution and accessible UI"
        ],
        "tech_badges": [
            ("tech-html5.svg", "HTML5"),
            ("tech-css3.svg", "CSS3"),
            ("tech-javascript.svg", "JavaScript"),
            ("tech-webspeech.svg", "Web Speech API")
        ],
        "status_badge": "assets/badge-repo-only.svg",
        "actions": [
            ("btn-view-repo.svg", "https://github.com/officialhazim42/Text-to-Audio-Converter", "View GitHub Repository"),
            ("btn-project-specs.svg", "PROJECTS.md#08-text-to-audio", "Read Technical Dossier")
        ]
    },
    {
        "num": "10",
        "id": "10-student-task-manager",
        "old_id": "09-student-task-manager",
        "name": "Student Task Manager",
        "tagline": "ACADEMIC WORKFLOW WEB TOOL",
        "status": "REPOSITORY ONLY",
        "preview": "assets/task-manager-preview.svg",
        "preview_alt": "10 / 11 — Student Task Manager Workflow Interface Preview",
        "link_preview": "https://github.com/officialhazim42/week-3-student-task-manager",
        "desc_heading": "Responsive Task Organization & Persistent Local Storage",
        "desc_body": "An interactive task organization web application engineered with HTML, CSS, and JavaScript, featuring task creation, completion tracking, filtering, deletion, and local storage state persistence.",
        "highlights": [
            "Coursework assignment management with quick-switch filters (All, Active, Completed)",
            "LocalStorage state caching ensuring zero progress loss across browser sessions",
            "Clean responsive DOM architecture optimized for desktop and mobile devices"
        ],
        "tech_badges": [
            ("tech-html5.svg", "HTML5"),
            ("tech-css3.svg", "CSS3"),
            ("tech-javascript.svg", "JavaScript"),
            ("tech-localstorage.svg", "LocalStorage API")
        ],
        "status_badge": "assets/badge-repo-only.svg",
        "actions": [
            ("btn-view-repo.svg", "https://github.com/officialhazim42/week-3-student-task-manager", "View GitHub Repository"),
            ("btn-project-specs.svg", "PROJECTS.md#09-student-task-manager", "Read Technical Dossier")
        ]
    },
    {
        "num": "11",
        "id": "11-deployment-dashboard",
        "old_id": "10-deployment-dashboard",
        "name": "Deployment Dashboard",
        "tagline": "DEVOPS & MONITORING PROTOTYPE",
        "status": "REPOSITORY ONLY",
        "preview": "assets/deployment-preview.svg",
        "preview_alt": "11 / 11 — Deployment Dashboard Telemetry Interface Preview",
        "link_preview": "https://github.com/officialhazim42/week-5-deployment-production",
        "desc_heading": "Production Operations & Telemetry Monitoring Simulation",
        "desc_body": "A production deployment dashboard prototype demonstrating environment status, application telemetry, performance metrics, simulated server logs, health checks, and production release concepts.",
        "highlights": [
            "Simulated environment telemetry for production, staging, and development server states",
            "Real-time performance visualizers for CPU utilization, memory allocation & network latency",
            "Dynamic console log streaming with an automated pre-flight release readiness checklist"
        ],
        "tech_badges": [
            ("tech-html5.svg", "HTML5"),
            ("tech-css3.svg", "CSS3"),
            ("tech-javascript.svg", "JavaScript"),
            ("tech-dom.svg", "DOM Architecture")
        ],
        "status_badge": "assets/badge-repo-only.svg",
        "actions": [
            ("btn-view-repo.svg", "https://github.com/officialhazim42/week-5-deployment-production", "View GitHub Repository"),
            ("btn-project-specs.svg", "PROJECTS.md#10-deployment-dashboard", "Read Technical Dossier")
        ]
    }
]

def render_section_04():
    chunks = []
    for c in projects:
        # Header banner image
        header_img = f'<img src="assets/cards/header-{c["num"]}.svg" alt="{c["num"]} / 11 — {c["name"]} | {c["tagline"]} ({c["status"]})" width="100%" />'
        
        # Preview banner spanning full card width
        preview_markup = f'<a href="{c["link_preview"]}"><img src="{c["preview"]}" alt="{c["preview_alt"]}" width="100%" style="border-radius: 8px 8px 0 0; border: 1px solid #1e3a5f;" /></a>'
        
        # Description box
        highlights_md = "\n".join([f"> • {h}" for h in c["highlights"]])
        desc_box = f'> **{c["desc_heading"]}:** {c["desc_body"]}\n>\n> 🔹 **Verified Capabilities:**\n{highlights_md}'
        
        # Tech badges
        tech_imgs = " ".join([f'<img src="assets/tech/{b[0]}" height="24" alt="{b[1]}" />' for b in c["tech_badges"]])
        
        # Status indicator badge
        status_img = f'<img src="{c["status_badge"]}" height="26" alt="Status: {c["status"]}" />'
        
        # Actions
        action_parts = []
        for btn_file, url, alt in c["actions"]:
            if url:
                action_parts.append(f'<a href="{url}"><img src="assets/buttons/{btn_file}" height="34" alt="{alt}" /></a>')
            else:
                action_parts.append(f'<img src="assets/buttons/{btn_file}" height="34" alt="{alt}" />')
        actions_markup = " &nbsp;&nbsp; ".join(action_parts)
        
        card_html = f"""<!-- ================================================================= -->
<!-- PROJECT {c["num"]} — COMPLETE CARD: {c["name"]} {' ' * max(0, 45 - len(c["num"]) - len(c["name"]))} -->
<!-- ================================================================= -->

<a id="{c["id"]}"></a>
<a id="{c["old_id"]}"></a>
<table width="100%">
<tr>
<td align="center">

{preview_markup}

</td>
</tr>
<tr>
<td align="left">

{header_img}

<br /><br />

{desc_box}

<br />

{tech_imgs}

<br /><br />

{status_img}

<br /><br />

{actions_markup}

</td>
</tr>
</table>"""
        chunks.append(card_html)
    
    return "\n\n<br />\n\n".join(chunks)

def render_section_05():
    section_05_md = """<img src="assets/section-cyberguard.svg" alt="05 / CYBERGUARD YUVA" width="100%" />

<br />

<table width="100%">
<tr>
<td align="center">

  <a href="https://cyberguard-yuva.vercel.app/">
    <img src="assets/cyberguard-banner.svg" alt="CyberGuard YUVA — Youth Cyber Defense Club Official Banner" width="100%" style="border-radius: 8px 8px 0 0; border: 1px solid #1e3a5f;" />
  </a>

</td>
</tr>
<tr>
<td align="left">

### 🛡️ CyberGuard YUVA — Youth Cyber Defense Club
`DEFENSIVE CYBERSECURITY &amp; YOUTH DIGITAL SAFETY` &nbsp; <img src="assets/badge-live.svg" height="26" alt="Status: LIVE" /> &nbsp; <img src="https://img.shields.io/badge/PORTAL-PRODUCTION_LIVE-0284C7?style=flat-square&logo=vercel&logoColor=white" alt="Live on Vercel" />

<br /><br />

> **SECURE &nbsp;•&nbsp; EDUCATE &nbsp;•&nbsp; EMPOWER &nbsp;—&nbsp; Youth for a Safer Digital India**

Co-founded **CyberGuard YUVA**, a youth-led cyber defense initiative and community organization dedicated to cultivating defensive technical literacy, student privacy hygiene, threat resistance, and responsible online practices across schools and universities.

* **Flagship Platform:** Engineered an interactive, responsive Progressive Web App delivering structured cyber defense guides, threat advisory matrices, and student playbooks.
* **Community Leadership:** Leading student awareness programs, CTF preparation sessions, and collaborative digital safety campaigns.
* **Technology Stack:** Engineered with `Next.js 15+`, `React 19`, `TypeScript`, `Tailwind CSS`, `Lucide Icons`, and deployed on `Vercel Edge`.

<br />

<img src="assets/cyberguard-pillars.svg" alt="CyberGuard YUVA Mission Pillars: Defensive Education, Technical Literacy, Empower Youth" width="100%" />

<br /><br />

<a href="https://cyberguard-yuva.vercel.app/">
  <img src="assets/btn-visit-cyberguard.svg" alt="VISIT CYBERGUARD YUVA →" height="42" />
</a>
&nbsp;&nbsp;
<a href="PROJECTS.md#03-cyberguard-yuva">
  <img src="https://img.shields.io/badge/📖_PROJECT_SPECS-0F2244?style=for-the-badge&logo=gitbook&logoColor=38BDF8" alt="Read Technical Dossier" />
</a>
&nbsp;&nbsp;
<img src="https://img.shields.io/badge/CODEBASE-PRIVATE-1E293B?style=for-the-badge&logo=github&logoColor=94A3B8" alt="Private Repository" />

</td>
</tr>
</table>

<br />

<details>
<summary><b>🖥️ View CyberGuard YUVA Desktop Interface &amp; Live Platform Preview</b></summary>
<br />
<a href="https://cyberguard-yuva.vercel.app/">
  <img src="assets/cyberguard-preview.png" alt="CyberGuard YUVA Desktop Interface Preview" width="100%" style="border-radius: 8px; border: 1px solid #1e3a5f;" />
</a>
<p align="center"><sub>Official CyberGuard YUVA interactive web portal running in production at <a href="https://cyberguard-yuva.vercel.app/">cyberguard-yuva.vercel.app</a></sub></p>
</details>"""
    return section_05_md

sec_04 = render_section_04()
sec_05 = render_section_05()

with open("scratch/preview_sec_04.md", "w", encoding="utf-8") as f:
    f.write(sec_04)

with open("scratch/preview_sec_05.md", "w", encoding="utf-8") as f:
    f.write(sec_05)

print("Generated scratch/preview_sec_04.md and scratch/preview_sec_05.md.")
