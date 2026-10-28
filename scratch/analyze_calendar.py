import subprocess, json
from collections import defaultdict

query = """
query($login: String!) {
  user(login: $login) {
    createdAt
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

res = subprocess.run(['gh', 'api', 'graphql', '-F', 'login=officialhazim42', '-f', f'query={query}'], capture_output=True, text=True)
data = json.loads(res.stdout)
cal = data['data']['user']['contributionsCollection']['contributionCalendar']
print('Total contributions (past 365 days):', cal['totalContributions'])

all_days = []
monthly = defaultdict(int)
for week in cal['weeks']:
    for d in week['contributionDays']:
        all_days.append((d['date'], d['contributionCount']))
        ym = d['date'][:7]
        monthly[ym] += d['contributionCount']

print('\nMonthly breakdown (past 13 months):')
for ym in sorted(monthly.keys()):
    print(f'  {ym}: {monthly[ym]}')

longest_streak = 0
streak_count = 0
longest_start = None
longest_end = None
cur_start = None

for i, (dt, count) in enumerate(all_days):
    if count > 0:
        if streak_count == 0:
            cur_start = dt
        streak_count += 1
        if streak_count > longest_streak:
            longest_streak = streak_count
            longest_start = cur_start
            longest_end = dt
    else:
        streak_count = 0

last_active_idx = None
for i in range(len(all_days)-1, -1, -1):
    if all_days[i][1] > 0:
        last_active_idx = i
        break

if last_active_idx is not None:
    cur_streak_days = []
    for i in range(last_active_idx, -1, -1):
        if all_days[i][1] > 0:
            cur_streak_days.append(all_days[i][0])
        else:
            break
    print(f'\nCurrent streak: {len(cur_streak_days)} days (from {cur_streak_days[-1]} to {cur_streak_days[0]})')

print(f'Longest streak: {longest_streak} days (from {longest_start} to {longest_end})')

