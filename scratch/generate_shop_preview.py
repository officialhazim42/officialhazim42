preview_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 294" width="100%" height="100%">
  <defs>
    <linearGradient id="shop-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a1329" />
      <stop offset="50%" stop-color="#0c1833" />
      <stop offset="100%" stop-color="#060b18" />
    </linearGradient>
    <radialGradient id="shop-glow" cx="80%" cy="30%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.25" />
      <stop offset="100%" stop-color="#0a1329" stop-opacity="0" />
    </radialGradient>
  </defs>
  <rect width="100%" height="100%" rx="12" fill="url(#shop-bg)" stroke="#1e3a5f" stroke-width="1.5" />
  <rect width="100%" height="100%" rx="12" fill="url(#shop-glow)" />

  <rect x="36" y="22" width="168" height="22" rx="11" fill="#081226" stroke="#1e3a5f" stroke-width="1" />
  <circle cx="48" cy="33" r="3" fill="#10b981" />
  <text x="58" y="37" font-family="ui-monospace, monospace" font-size="10" font-weight="700" fill="#38bdf8">DIGITAL SERVICES PLATFORM</text>

  <text x="36" y="92" font-family="system-ui, sans-serif" font-size="28" font-weight="800" fill="#ffffff">Shop — Net Gallery Hb</text>
  <text x="36" y="118" font-family="ui-monospace, monospace" font-size="12" font-weight="600" fill="#93c5fd" letter-spacing="1.5px">PRINTING • CSC SERVICES • PHOTO GIFTS</text>

  <g transform="translate(36, 140)">
    <rect width="230" height="34" rx="6" fill="#081226" stroke="#1e3a5f" stroke-width="1" />
    <text x="14" y="22" font-family="system-ui, sans-serif" font-size="11" fill="#cbd5e1">⚡ CSC &amp; Citizen Portal Support</text>

    <rect x="245" width="230" height="34" rx="6" fill="#081226" stroke="#1e3a5f" stroke-width="1" />
    <text x="259" y="22" font-family="system-ui, sans-serif" font-size="11" fill="#cbd5e1">⚡ Custom Phone Covers &amp; Frames</text>

    <rect y="44" width="230" height="34" rx="6" fill="#081226" stroke="#1e3a5f" stroke-width="1" />
    <text x="14" y="66" font-family="system-ui, sans-serif" font-size="11" fill="#cbd5e1">⚡ High-Res Printing &amp; Passport Photos</text>

    <rect x="245" y="44" width="230" height="34" rx="6" fill="#081226" stroke="#1e3a5f" stroke-width="1" />
    <text x="259" y="66" font-family="system-ui, sans-serif" font-size="11" fill="#cbd5e1">⚡ Instant UPI Payments &amp; Booking</text>
  </g>

  <text x="36" y="265" font-family="ui-monospace, monospace" font-size="11" fill="#38bdf8">net-gallery-hb.netlify.app</text>
  <text x="524" y="265" text-anchor="end" font-family="ui-monospace, monospace" font-size="11" font-weight="700" fill="#10b981">● LIVE IN PRODUCTION</text>
</svg>
"""

with open("assets/shop-preview.svg", "w", encoding="utf-8") as f:
    f.write(preview_svg)

print("Generated assets/shop-preview.svg successfully.")
