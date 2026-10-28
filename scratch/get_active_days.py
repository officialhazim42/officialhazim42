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

all_days = []
active_days = 0
for week in cal['weeks']:
    for d in week['contributionDays']:
        all_days.append(d)
        if d['contributionCount'] > 0:
            active_days += 1

print(f"Total days: {len(all_days)}")
print(f"Active days: {active_days}")
print(f"First day: {all_days[0]['date']}, Last day: {all_days[-1]['date']}")

