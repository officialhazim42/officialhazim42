import os

def update():
    readme_path = "README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = '<img src="assets/section-stats.svg"'
    end_marker = '<img src="assets/section-connect.svg"'

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print(f"Error: Markers not found. start={start_idx}, end={end_idx}")
        return False

    new_section_07 = """<img src="assets/section-stats.svg" alt="07 / GITHUB ACTIVITY AND METRICS" width="100%" />

<br />

<!-- ================================================================= -->
<!-- ROW 1: TELEMETRY METRIC CARDS (TOTAL CONTRIBUTIONS, STREAKS)      -->
<!-- ================================================================= -->

<img src="assets/streak-metrics.svg" alt="GitHub Contribution Velocity &amp; Streak Analytics: 245 Total Contributions, 12-Day Current Streak, 12-Day Longest Streak" width="100%" />

<br />

<!-- ================================================================= -->
<!-- ROW 2: SIDE-BY-SIDE ANALYTICS (GITHUB STATS & LANGUAGE AUDIT)     -->
<!-- ================================================================= -->

<table width="100%">
<tr>
<td width="50%" valign="top">
  <img src="assets/github-stats.svg" alt="HAZIM BASHIR FAQEER &#8212; Verified GitHub Profile Telemetry &amp; Developer Metrics" width="100%" />
</td>
<td width="50%" valign="top">
  <img src="assets/language-stats-card.svg" alt="Verified Public Codebase Language Distribution &#8212; 3.81 MB Analyzed Across 13 Repositories" width="100%" />
</td>
</tr>
</table>

<br />

<!-- ================================================================= -->
<!-- ROW 3: ANNUAL CONTRIBUTION ACTIVITY HEATMAP (368 DAYS)           -->
<!-- ================================================================= -->

<img src="assets/contribution-heatmap.svg" alt="Annual GitHub Contribution Activity Heatmap: 245 contributions across 368 days (Oct 26, 2025 &#8211; Oct 28, 2026)" width="100%" />

<br />

<!-- ================================================================= -->
<!-- ROW 4: MONTHLY CONTRIBUTION VELOCITY & TREND TRAJECTORY          -->
<!-- ================================================================= -->

<img src="assets/monthly-trend.svg" alt="Monthly Contribution Velocity &amp; Activity Trajectory: 13-month progression showing peak 126 contributions in October 2026" width="100%" />

<br />

<!-- ================================================================= -->
<!-- VERIFIED TELEMETRY AUDIT MATRIX                                  -->
<!-- ================================================================= -->

| Telemetry Dimension | Verified Metric | Audit Scope &amp; Source Verification |
| :--- | :--- | :--- |
| **Total Contributions**<br /><sub>ANNUAL VELOCITY</sub> | <code><b>245</b> Activity Units</code><br /><sub>Verified 365-Day Sum</sub> | Verified across 368 calendar days (Oct 26, 2025 &#8211; Oct 28, 2026)<br /><sub>Direct GitHub contribution calendar audit &#8226; +126 in Oct 2026</sub> |
| **Current &amp; Longest Streak**<br /><sub>ACTIVE CONSISTENCY</sub> | <code><b>12</b> Consecutive Days</code><br /><sub>Oct 17 &#8211; Oct 28, 2026</sub> | Active run: Oct 17 &#8211; Oct 28, 2026 (Verified streak record)<br /><sub>Continuous daily contribution sequence with zero missed intervals</sub> |
| **Total Author Commits**<br /><sub>SOURCE CODE EDITS</sub> | <code><b>116</b> Commits</code><br /><sub>Direct Repository Pushes</sub> | Direct author commits across 13 public repository trees (232 commit search matches)<br /><sub>Audited via GitHub Search API author query across public repositories</sub> |
| **Public Codebase Volume**<br /><sub>BYTE DISTRIBUTION</sub> | <code><b>3,806,304</b> Bytes</code> <b>(3.81 MB)</b><br /><sub>HTML 61.2% &#8226; JS 31.4% &#8226; CSS 4.1% &#8226; Python 3.3%</sub> | HTML (61.19%), JavaScript ES6+ (31.36%), CSS3 (4.11%), Python (3.34%)<br /><sub>Comprehensive repository byte breakdown across all 13 public repositories</sub> |
| **Repository Footprint**<br /><sub>PROJECT ECOSYSTEM</sub> | <code><b>13</b> Public Repositories</code><br /><sub>Standalone Suites</sub> | Pure client-side engines, in-browser utilities &amp; PWA apps<br /><sub>Zero server-upload client computing utilities &amp; cybersecurity learning platforms</sub> |

<br />

"""

    updated_content = content[:start_idx] + new_section_07 + content[end_idx:]
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Successfully updated Section 07 in README.md!")
    return True

if __name__ == "__main__":
    update()

