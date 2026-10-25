import os

# Let's inspect the 10 projects data
projects = [
    {
        "num": "01",
        "total": "10",
        "name": "PDFHub",
        "icon": "📄",
        "tagline": "CLIENT-SIDE WEBASSEMBLY SUITE",
        "status": "LIVE",
        "category": "Client-Side WebAssembly Suite",
        "preview": "assets/pdfhub-preview.png",
        "preview_alt": "PDFHub Preview",
        "desc": "A comprehensive, privacy-first PDF utility suite engineered to execute 100% within the browser. Files are processed locally on the client device using WebAssembly and client-side JavaScript engines, guaranteeing that sensitive documents never touch external servers.",
        "features": [
            "33 specialized in-browser tools (merge, split, compress, OCR, convert)",
            "Zero server uploads with 100% client-side WebAssembly execution",
            "Offline PWA capability with persistent client storage"
        ],
        "tech": [
            {"name": "JavaScript (ES6+)", "logo": "javascript", "color": "F7DF1E"},
            {"name": "WebAssembly", "logo": "webassembly", "color": "654FF0"},
            {"name": "pdf-lib", "logo": "adobeacrobatreader", "color": "EC1C24"},
            {"name": "pdf.js", "logo": "mozilla", "color": "000000"},
            {"name": "HTML5 Canvas", "logo": "html5", "color": "E34F26"},
            {"name": "Netlify Edge", "logo": "netlify", "color": "00C7B7"}
        ],
        "actions": [
            {"label": "LIVE DEMO", "url": "https://pdfshub.netlify.app/", "primary": True, "icon": "🌐"},
            {"label": "VIEW REPOSITORY", "url": "https://github.com/officialhazim42/pdfshub", "primary": False, "icon": "💻"},
            {"label": "PROJECT SPECS", "url": "PROJECTS.md#01-pdfhub", "primary": False, "icon": "📖"}
        ]
    },
    {
        "num": "02",
        "total": "10",
        "name": "ImageHub",
        "icon": "🖼️",
        "tagline": "IN-BROWSER GRAPHICS ENGINE",
        "status": "LIVE",
        "category": "In-Browser Graphics Engine",
        "preview": "assets/imagehub-preview.svg",
        "preview_alt": "ImageHub Preview",
        "desc": "A production-grade, client-side digital image manipulation platform running locally in the web browser. Empowers users to compress, upscale, isolate subjects, crop, resize, and convert graphics without transmitting a single byte over the network.",
        "features": [
            "Zero server dependencies with high-throughput HTML5 Canvas rendering",
            "Broad format support (JPG, PNG, WebP, modern AVIF) with client-side conversion",
            "Service Worker caching for seamless offline editing workflows"
        ],
        "tech": [
            {"name": "JavaScript", "logo": "javascript", "color": "F7DF1E"},
            {"name": "HTML5 Canvas", "logo": "html5", "color": "E34F26"},
            {"name": "CSS3", "logo": "css3", "color": "1572B6"},
            {"name": "Web APIs", "logo": "googlechrome", "color": "4285F4"},
            {"name": "Service Workers", "logo": "pwa", "color": "5A0FC8"}
        ],
        "actions": [
            {"label": "LIVE DEMO", "url": "https://imagehub.netlify.app/", "primary": True, "icon": "🌐"},
            {"label": "VIEW REPOSITORY", "url": "https://github.com/officialhazim42/imagehub", "primary": False, "icon": "💻"},
            {"label": "PROJECT SPECS", "url": "PROJECTS.md#02-imagehub", "primary": False, "icon": "📖"}
        ]
    },
    {
        "num": "03",
        "total": "10",
        "name": "CyberGuard YUVA",
        "icon": "🛡️",
        "tagline": "CYBER DEFENSE PORTAL & COMMUNITY",
        "status": "LIVE",
        "category": "Cyber Defense Portal & Community",
        "preview": "assets/cyberguard-preview.png",
        "preview_alt": "CyberGuard YUVA Preview",
        "desc": "Official web portal and digital learning hub for CyberGuard YUVA, a youth-led cyber defense initiative dedicated to cultivating defensive technical literacy, student privacy hygiene, and safe digital practices across schools and universities.",
        "features": [
            "Interactive student manuals, phishing resistance playbooks & threat hygiene matrices",
            "Modern SSR & Edge computing architecture deployed on Vercel Edge",
            "Campus awareness programs, CTF preparation & collaborative digital safety"
        ],
        "tech": [
            {"name": "Next.js 15+", "logo": "nextdotjs", "color": "ffffff"},
            {"name": "React 19", "logo": "react", "color": "61DAFB"},
            {"name": "TypeScript", "logo": "typescript", "color": "3178C6"},
            {"name": "Tailwind CSS", "logo": "tailwindcss", "color": "06B6D4"},
            {"name": "Vercel Edge", "logo": "vercel", "color": "ffffff"}
        ],
        "actions": [
            {"label": "LIVE DEMO", "url": "https://cyberguard-yuva.vercel.app/", "primary": True, "icon": "🌐"},
            {"label": "PRIVATE CODEBASE", "url": None, "primary": False, "icon": "🔒"},
            {"label": "PROJECT SPECS", "url": "PROJECTS.md#03-cyberguard-yuva", "primary": False, "icon": "📖"}
        ]
    },
    {
        "num": "04",
        "total": "10",
        "name": "HabitsGrow (HabitFlow)",
        "icon": "🌱",
        "tagline": "PRODUCTIVITY & PERSONAL GROWTH PWA",
        "status": "LIVE",
        "category": "Productivity & Personal Growth PWA",
        "preview": "assets/habitsgrow-preview.png",
        "preview_alt": "HabitsGrow Preview",
        "desc": "A responsive, privacy-centric Progressive Web App designed to help individuals build positive routines, maintain completion consistency streaks, visualize progress analytics, and document mindfulness reflections.",
        "features": [
            "Daily habit tracking with streaks, routine categorization & analytics visualizer",
            "Offline-first PWA with Service Worker synchronization & Web App Manifest",
            "Cloud state persistence backed by Supabase with Row Level Security"
        ],
        "tech": [
            {"name": "JavaScript (ES6+)", "logo": "javascript", "color": "F7DF1E"},
            {"name": "PWA", "logo": "pwa", "color": "5A0FC8"},
            {"name": "Service Workers", "logo": "w3c", "color": "005A9C"},
            {"name": "Supabase", "logo": "supabase", "color": "3ECF8E"},
            {"name": "HTML5 / CSS3", "logo": "html5", "color": "E34F26"}
        ],
        "actions": [
            {"label": "LIVE DEMO", "url": "https://habit-flow-ten-eta.vercel.app", "primary": True, "icon": "🌐"},
            {"label": "PRIVATE CODEBASE", "url": None, "primary": False, "icon": "🔒"},
            {"label": "PROJECT SPECS", "url": "PROJECTS.md#04-habitsgrow", "primary": False, "icon": "📖"}
        ]
    },
    {
        "num": "05",
        "total": "10",
        "name": "Advanced Image Compressor",
        "icon": "⚡",
        "tagline": "CLIENT-SIDE MULTI-FORMAT COMPRESSION UTILITY",
        "status": "LIVE",
        "category": "Compression Utility",
        "preview": "assets/compressor-preview.svg",
        "preview_alt": "Advanced Image Compressor Preview",
        "desc": "A focused, responsive web tool engineered for ultra-fast image compression with real-time compression ratios and format detection, packaged in a sleek dark glassmorphic UI.",
        "features": [
            "Modern AVIF engine supporting JPG, PNG, WebP & AVIF format generation",
            "Dynamic before-and-after compression metrics with real-time file size previews",
            "Automated batch sequential renaming & organized archive exports"
        ],
        "tech": [
            {"name": "HTML5", "logo": "html5", "color": "E34F26"},
            {"name": "CSS3", "logo": "css3", "color": "1572B6"},
            {"name": "JavaScript", "logo": "javascript", "color": "F7DF1E"},
            {"name": "Canvas API", "logo": "html5", "color": "E34F26"},
            {"name": "Netlify", "logo": "netlify", "color": "00C7B7"}
        ],
        "actions": [
            {"label": "LIVE DEMO", "url": "https://advance-images-compressor.netlify.app/", "primary": True, "icon": "🌐"},
            {"label": "VIEW REPOSITORY", "url": "https://github.com/officialhazim42/Advance-Image-Compressor", "primary": False, "icon": "💻"},
            {"label": "PROJECT SPECS", "url": "PROJECTS.md#05-advance-image-compressor", "primary": False, "icon": "📖"}
        ]
    },
    {
        "num": "06",
        "total": "10",
        "name": "Termux Command Guide",
        "icon": "💻",
        "tagline": "TECHNICAL DOCUMENTATION HANDBOOK",
        "status": "REPOSITORY ONLY",
        "category": "Technical Documentation Handbook",
        "preview": "assets/termux-preview.svg",
        "preview_alt": "Termux Command Guide Preview",
        "desc": "A structured, practical reference handbook and command guide for mastering native Linux command-line operations and device integration APIs within the Termux Android terminal environment.",
        "features": [
            "Categorized Linux command index, package configurations & dev setups",
            "Termux hardware & sensor API integration recipes for Android",
            "On-device development environment setup guides (Git, Node.js, Python)"
        ],
        "tech": [
            {"name": "Shell / Bash", "logo": "gnubash", "color": "4EAA25"},
            {"name": "Linux CLI", "logo": "linux", "color": "FCC624"},
            {"name": "Android Termux", "logo": "android", "color": "3DDC84"},
            {"name": "Markdown", "logo": "markdown", "color": "ffffff"}
        ],
        "actions": [
            {"label": "VIEW REPOSITORY", "url": "https://github.com/officialhazim42/Termux-Command-Listbook", "primary": True, "icon": "💻"},
            {"label": "PROJECT SPECS", "url": "PROJECTS.md#06-termux-command-guide", "primary": False, "icon": "📖"}
        ]
    },
    {
        "num": "07",
        "total": "10",
        "name": "Passport Photo Maker",
        "icon": "📸",
        "tagline": "CLIENT-SIDE MEDIA TOOL",
        "status": "REPOSITORY ONLY",
        "category": "Client-Side Media Tool",
        "preview": "assets/passport-preview.svg",
        "preview_alt": "Passport Photo Maker Preview",
        "desc": "A client-side utility built with HTML5 Canvas that enables users to crop, scale, and format photographs to international passport standards and generate multi-photo sheets ready for printing.",
        "features": [
            "International standard dimension presets (2x2 inch, 35x45mm)",
            "Automatic multi-photo tiling onto printable standard sheets",
            "In-browser processing with HTML5 Canvas and zero server data transfer"
        ],
        "tech": [
            {"name": "HTML5", "logo": "html5", "color": "E34F26"},
            {"name": "CSS3", "logo": "css3", "color": "1572B6"},
            {"name": "JavaScript", "logo": "javascript", "color": "F7DF1E"},
            {"name": "Canvas API", "logo": "html5", "color": "E34F26"}
        ],
        "actions": [
            {"label": "VIEW REPOSITORY", "url": "https://github.com/officialhazim42/Passportsize-photo-maker", "primary": True, "icon": "💻"},
            {"label": "PROJECT SPECS", "url": "PROJECTS.md#07-passport-photo-maker", "primary": False, "icon": "📖"}
        ]
    },
    {
        "num": "08",
        "total": "10",
        "name": "Text to Audio Converter",
        "icon": "🔊",
        "tagline": "SPEECH SYNTHESIS TOOL",
        "status": "REPOSITORY ONLY",
        "category": "Speech Synthesis Tool",
        "preview": "assets/audio-preview.svg",
        "preview_alt": "Text to Audio Converter Preview",
        "desc": "A lightweight web tool leveraging the browser-native Web Speech Synthesis API to convert written text into spoken audio with real-time controls for pitch, speech rate, and voice accents.",
        "features": [
            "Hardware-accelerated native browser speech synthesis engine",
            "Dynamic sliders for real-time speech rate, pitch tuning & voice accents",
            "Zero cloud dependencies with 100% vanilla client execution"
        ],
        "tech": [
            {"name": "HTML5", "logo": "html5", "color": "E34F26"},
            {"name": "CSS3", "logo": "css3", "color": "1572B6"},
            {"name": "JavaScript", "logo": "javascript", "color": "F7DF1E"},
            {"name": "Web Speech API", "logo": "w3c", "color": "005A9C"}
        ],
        "actions": [
            {"label": "VIEW REPOSITORY", "url": "https://github.com/officialhazim42/Text-to-Audio-Converter", "primary": True, "icon": "💻"},
            {"label": "PROJECT SPECS", "url": "PROJECTS.md#08-text-to-audio", "primary": False, "icon": "📖"}
        ]
    },
    {
        "num": "09",
        "total": "10",
        "name": "Student Task Manager",
        "icon": "📝",
        "tagline": "ACADEMIC WORKFLOW WEB TOOL",
        "status": "REPOSITORY ONLY",
        "category": "Academic Workflow Web Tool",
        "preview": "assets/task-manager-preview.svg",
        "preview_alt": "Student Task Manager Preview",
        "desc": "An interactive task organization web application engineered with HTML, CSS, and JavaScript, featuring task creation, completion tracking, filtering, deletion, and local storage state persistence.",
        "features": [
            "Intuitive coursework task organization with active & completed filter views",
            "State persistence via LocalStorage ensuring zero data loss across sessions",
            "Responsive DOM architecture optimized for desktop and mobile devices"
        ],
        "tech": [
            {"name": "HTML5", "logo": "html5", "color": "E34F26"},
            {"name": "CSS3", "logo": "css3", "color": "1572B6"},
            {"name": "JavaScript", "logo": "javascript", "color": "F7DF1E"},
            {"name": "LocalStorage API", "logo": "googlechrome", "color": "4285F4"}
        ],
        "actions": [
            {"label": "VIEW REPOSITORY", "url": "https://github.com/officialhazim42/week-3-student-task-manager", "primary": True, "icon": "💻"},
            {"label": "PROJECT SPECS", "url": "PROJECTS.md#09-student-task-manager", "primary": False, "icon": "📖"}
        ]
    },
    {
        "num": "10",
        "total": "10",
        "name": "Deployment Dashboard",
        "icon": "📊",
        "tagline": "DEVOPS & MONITORING PROTOTYPE",
        "status": "REPOSITORY ONLY",
        "category": "DevOps & Monitoring Prototype",
        "preview": "assets/deployment-preview.svg",
        "preview_alt": "Deployment Dashboard Preview",
        "desc": "A production deployment dashboard prototype demonstrating environment status, application telemetry, performance metrics, simulated server logs, health checks, and production release concepts.",
        "features": [
            "Simulated environment telemetry for production, staging & dev environments",
            "Real-time visualizers for CPU allocation, memory usage & network latency",
            "Dynamic console log streaming and automated pre-flight release readiness checklist"
        ],
        "tech": [
            {"name": "HTML5", "logo": "html5", "color": "E34F26"},
            {"name": "CSS3", "logo": "css3", "color": "1572B6"},
            {"name": "JavaScript", "logo": "javascript", "color": "F7DF1E"},
            {"name": "DOM Architecture", "logo": "w3c", "color": "005A9C"}
        ],
        "actions": [
            {"label": "VIEW REPOSITORY", "url": "https://github.com/officialhazim42/week-5-deployment-production", "primary": True, "icon": "💻"},
            {"label": "PROJECT SPECS", "url": "PROJECTS.md#10-deployment-dashboard", "primary": False, "icon": "📖"}
        ]
    }
]

print(f"Loaded {len(projects)} projects.")
