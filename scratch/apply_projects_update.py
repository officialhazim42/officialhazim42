with open('PROJECTS.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update table
old_table_row_02 = '| **[ImageHub](#02-imagehub)** | `02` | In-Browser Graphics Engine | `LIVE` | Pure JavaScript, HTML5 Canvas | [Launch Demo](https://imagehub.netlify.app/) | [Source Code](https://github.com/officialhazim42/imagehub) |'
new_table_row_02 = '| **[ImageHub](#02-imagehub)** | `02` | In-Browser Graphics Engine | `LIVE` | Pure JavaScript, HTML5 Canvas | [Launch Demo](https://images-hub.netlify.app/pages/index.html) | [Source Code](https://github.com/officialhazim42/imagehub) |'

old_table_row_04 = '| **[HabitsGrow (HabitFlow)](#04-habitsgrow)** | `04` | Productivity & Personal Growth PWA | `LIVE` | JavaScript (ES6+), PWA | [Launch Demo](https://habit-flow-ten-eta.vercel.app) | Private |'
new_table_row_04 = '| **[HabitsGrow](#04-habitsgrow)** | `04` | Productivity & Personal Growth PWA | `LIVE` | JavaScript (ES6+), PWA | [Launch Demo](https://habitsgrow.netlify.app/) | Private |'

old_table_row_10 = '| **[Deployment Dashboard](#10-deployment-dashboard)** | `10` | DevOps & Monitoring Prototype | `REPOSITORY ONLY` | HTML5, CSS3 | — | [Source Code](https://github.com/officialhazim42/week-5-deployment-production) |'
new_table_rows_10_11 = """| **[Deployment Dashboard](#10-deployment-dashboard)** | `10` | DevOps & Monitoring Prototype | `REPOSITORY ONLY` | HTML5, CSS3 | — | [Source Code](https://github.com/officialhazim42/week-5-deployment-production) |
| **[Shop (Net Gallery Hb)](#11-shop)** | `11` | Digital & Printing Services Platform | `LIVE` | HTML5, CSS3, JavaScript | [Launch Demo](https://net-gallery-hb.netlify.app/) | Private |"""

assert old_table_row_02 in content, "old_table_row_02 not found"
assert old_table_row_04 in content, "old_table_row_04 not found"
assert old_table_row_10 in content, "old_table_row_10 not found"

content = content.replace(old_table_row_02, new_table_row_02)
content = content.replace(old_table_row_04, new_table_row_04)
content = content.replace(old_table_row_10, new_table_rows_10_11)

# 2. Update ImageHub section link
old_p02_action = '[🌐 Launch Live Deployment](https://imagehub.netlify.app/)'
new_p02_action = '[🌐 Launch Live Deployment](https://images-hub.netlify.app/pages/index.html)'
assert old_p02_action in content, "old_p02_action not found"
content = content.replace(old_p02_action, new_p02_action)

# 3. Update HabitsGrow section
old_p04_header = '## <a id="04-habitsgrow"></a>04 / HabitsGrow (HabitFlow) — Modern Routine Building & Consistency Tracking PWA'
new_p04_header = '## <a id="04-habitsgrow"></a>04 / HabitsGrow — Grow Better Every Day'
assert old_p04_header in content, "old_p04_header not found"
content = content.replace(old_p04_header, new_p04_header)

old_p04_img = '<img src="assets/habitsgrow-preview.png" alt="HabitsGrow (HabitFlow) Preview"'
new_p04_img = '<img src="assets/habitsgrow-preview.png" alt="HabitsGrow Preview"'
assert old_p04_img in content, "old_p04_img not found"
content = content.replace(old_p04_img, new_p04_img)

old_p04_link = '[🌐 Launch Live Deployment](https://habit-flow-ten-eta.vercel.app)'
new_p04_link = '[🌐 Launch Live Deployment](https://habitsgrow.netlify.app/)'
assert old_p04_link in content, "old_p04_link not found"
content = content.replace(old_p04_link, new_p04_link)

# 4. Add Section 11 for Shop at the end
section_11 = """---

## <a id="11-shop"></a>11 / Shop (Net Gallery Hb) — Professional Digital & Local Printing Services Hub
**Category:** Digital & Printing Services Platform &nbsp;|&nbsp; **Status:** `LIVE`

<img src="assets/shop-preview.svg" alt="Net Gallery Hb Preview" width="100%" style="max-width: 700px; border-radius: 8px; border: 1px solid #1e3a5f;" />

### 📌 About the Project
A dedicated commercial service portal for Net Gallery Hb providing local citizens and students with official digital document processing, CSC governance services, custom photo merchandise, and on-demand professional printing.

### ⚡ Key Capabilities & Verified Features
- **Government & Citizen Services assistance:** CSC governance schemes, Ayushman Golden Card, PAN applications, Voter ID services & Driving Licence support
- **Custom merchandise & framing:** Professional digital photo printing, personalized mobile back covers, photo framing & instant passport photos
- **Seamless client engagement:** Responsive booking request forms, live dynamic pricing matrix, instant WhatsApp integration & UPI digital payment workflow
- **High-availability deployment:** Ultra-fast static delivery hosted on Netlify Edge

### 🛠️ Verified Technology Stack
`HTML5` `CSS3` `JavaScript` `Responsive DOM` `Netlify Edge`

### 🔗 Project Actions & Destinations
[🌐 Launch Live Deployment](https://net-gallery-hb.netlify.app/) &nbsp;•&nbsp; [← Back to Table of Contents](#-featured-projects-dossier--hazim-bashir-faqeer)
"""

if not content.endswith('\n'):
    content += '\n'
content += section_11

with open('PROJECTS.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('PROJECTS.md updated successfully!')
