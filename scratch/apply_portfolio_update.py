with open('portfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Filter buttons
old_filter = """        <button class="filter-btn active" onclick="filterProjects('all')">All Projects (10)</button>
        <button class="filter-btn" onclick="filterProjects('live')">⚡ Live Deployments (5)</button>
        <button class="filter-btn" onclick="filterProjects('repo')">💻 Open Source Repositories (10)</button>"""

new_filter = """        <button class="filter-btn active" onclick="filterProjects('all')">All Projects (11)</button>
        <button class="filter-btn" onclick="filterProjects('live')">⚡ Live Deployments (6)</button>
        <button class="filter-btn" onclick="filterProjects('repo')">💻 Open Source Repositories (11)</button>"""

assert old_filter in content, "old_filter not found in portfolio/index.html"
content = content.replace(old_filter, new_filter)

# ImageHub URL & tagline
old_p02 = """"id": "02-imagehub",
    "num": "02",
    "name": "ImageHub",
    "tagline": "Professional In-Browser Image Manipulation Platform",
    "status": "LIVE",
    "statusType": "live",
    "category": "In-Browser Graphics Engine",
    "desc": "A production-grade, client-side digital image manipulation platform running locally in the web browser. Empowers users to compress, upscale, isolate subjects, crop, resize, and convert graphics without transmitting a single byte over the network.",
    "features": [
      "Client-side image processing: Compress, crop, resize, upscale, and isolate photo subjects locally",
      "Broad format support: Converts between JPG, PNG, WebP, and modern AVIF formats in-browser",
      "Offline-first PWA: Complete Service Worker caching for seamless offline editing workflows",
      "Zero backend dependencies: High-performance HTML5 Canvas rendering engine"
    ],
    "stack": [
      "Pure JavaScript",
      "HTML5 Canvas",
      "Web APIs",
      "CSS3",
      "Service Workers",
      "Netlify Edge"
    ],
    "repo": "https://github.com/officialhazim42/imagehub",
    "live": "https://imagehub.netlify.app/","""

new_p02 = """"id": "02-imagehub",
    "num": "02",
    "name": "ImageHub",
    "tagline": "13 Free In-Browser Image Tools Online",
    "status": "LIVE",
    "statusType": "live",
    "category": "In-Browser Graphics Engine",
    "desc": "A production-grade, client-side digital image manipulation platform running locally in the web browser. Empowers users to compress, upscale, isolate subjects, crop, resize, and convert graphics without transmitting a single byte over the network.",
    "features": [
      "Client-side image processing: Compress, crop, resize, upscale, and isolate photo subjects locally",
      "Broad format support: Converts between JPG, PNG, WebP, and modern AVIF formats in-browser",
      "Offline-first PWA: Complete Service Worker caching for seamless offline editing workflows",
      "Zero backend dependencies: High-performance HTML5 Canvas rendering engine"
    ],
    "stack": [
      "Pure JavaScript",
      "HTML5 Canvas",
      "Web APIs",
      "CSS3",
      "Service Workers",
      "Netlify Edge"
    ],
    "repo": "https://github.com/officialhazim42/imagehub",
    "live": "https://images-hub.netlify.app/pages/index.html","""

assert old_p02 in content, "old_p02 not found in portfolio/index.html"
content = content.replace(old_p02, new_p02)

# HabitsGrow
old_p04 = """"id": "04-habitsgrow",
    "num": "04",
    "name": "HabitsGrow (HabitFlow)",
    "tagline": "Modern Routine Building & Consistency Tracking PWA",
    "status": "LIVE",
    "statusType": "live",
    "category": "Productivity & Personal Growth PWA",
    "desc": "A responsive, privacy-centric Progressive Web App designed to help individuals build positive routines, maintain completion consistency streaks, visualize progress analytics, and document mindfulness reflections.",
    "features": [
      "Daily habit tracking: Intuitive streak counters, category grouping, and routine checklists",
      "Analytics dashboard: Interactive completion visualizer, calendar history, and streak trends",
      "Offline-first PWA: Full offline capabilities with Web App Manifest and Service Worker sync",
      "Secure state persistence: Cloud state synchronization backed by Supabase with Row Level Security"
    ],
    "stack": [
      "JavaScript (ES6+)",
      "PWA",
      "Service Workers",
      "HTML5/CSS3",
      "Supabase",
      "Vercel"
    ],
    "repo": "",
    "live": "https://habit-flow-ten-eta.vercel.app","""

new_p04 = """"id": "04-habitsgrow",
    "num": "04",
    "name": "HabitsGrow",
    "tagline": "Grow Better Every Day",
    "status": "LIVE",
    "statusType": "live",
    "category": "Productivity & Personal Growth PWA",
    "desc": "A responsive, privacy-centric Progressive Web App designed to help individuals build positive routines, maintain completion consistency streaks, visualize progress analytics, and document mindfulness reflections.",
    "features": [
      "Daily habit tracking: Intuitive streak counters, category grouping, and routine checklists",
      "Analytics dashboard: Interactive completion visualizer, calendar history, and streak trends",
      "Offline-first PWA: Full offline capabilities with Web App Manifest and Service Worker sync",
      "Secure state persistence: Cloud state synchronization backed by Supabase with Row Level Security"
    ],
    "stack": [
      "JavaScript (ES6+)",
      "PWA",
      "Service Workers",
      "HTML5/CSS3",
      "Supabase",
      "Netlify"
    ],
    "repo": "",
    "live": "https://habitsgrow.netlify.app/","""

assert old_p04 in content, "old_p04 not found in portfolio/index.html"
content = content.replace(old_p04, new_p04)

# Add Card 11 (Shop)
old_p10_end = """"readmeThumb": "assets/deployment-preview.svg",
    "icon": "\\ud83d\\udcca"
  }
];"""

new_p10_and_p11 = """"readmeThumb": "assets/deployment-preview.svg",
    "icon": "\\ud83d\\udcca"
  },
  {
    "id": "11-shop",
    "num": "11",
    "name": "Shop (Net Gallery Hb)",
    "tagline": "Professional Digital & Local Printing Services Hub",
    "status": "LIVE",
    "statusType": "live",
    "category": "Digital & Printing Services Platform",
    "desc": "A dedicated commercial service portal for Net Gallery Hb providing local citizens and students with official digital document processing, CSC governance services, custom photo merchandise, and on-demand professional printing.",
    "features": [
      "Government & Citizen Services assistance: CSC governance schemes, Ayushman Golden Card, PAN applications, Voter ID services & Driving Licence support",
      "Custom merchandise & framing: Professional digital photo printing, personalized mobile back covers, photo framing & instant passport photos",
      "Seamless client engagement: Responsive booking request forms, live dynamic pricing matrix, instant WhatsApp integration & UPI digital payment workflow",
      "High-availability deployment: Ultra-fast static delivery hosted on Netlify Edge"
    ],
    "stack": [
      "HTML5",
      "CSS3",
      "JavaScript",
      "Responsive DOM",
      "Netlify Edge"
    ],
    "repo": "",
    "live": "https://net-gallery-hb.netlify.app/",
    "thumbnail": "../assets/shop-preview.svg",
    "readmeThumb": "assets/shop-preview.svg",
    "icon": "\\ud83d\\udecd\\ufe0f"
  }
];"""

assert old_p10_end in content, "old_p10_end not found in portfolio/index.html"
content = content.replace(old_p10_end, new_p10_and_p11)

with open('portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('portfolio/index.html updated successfully!')
