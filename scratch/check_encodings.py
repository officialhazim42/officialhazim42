import os

files = [
    'assets/section-stats.svg',
    'assets/streak-metrics.svg',
    'assets/github-stats.svg',
    'assets/language-stats-card.svg',
    'assets/contribution-heatmap.svg',
    'assets/monthly-trend.svg'
]

for file in files:
    with open(file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    issues = []
    if 'â€' in content or 'â˜' in content or 'â' in content:
        issues.append('Detected potential Windows-1252/UTF-8 mojibake')
    for char in ['–', '—', '•', '★']:
        if char in content:
            issues.append(f'Contains literal character {char} (candidate for XML entity)')
    print(f"{file}: {issues if issues else 'Clean'}")

