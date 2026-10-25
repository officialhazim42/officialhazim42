import urllib.request
import json

headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request('https://api.github.com/users/officialhazim42/repos?per_page=100', headers=headers)
with urllib.request.urlopen(req) as resp:
    repos = json.loads(resp.read().decode('utf-8'))

with open('scratch/all_repos_info.txt', 'w', encoding='utf-8') as f:
    for r in repos:
        f.write(f"{r['name']} --> desc: {r.get('description')} --> homepage: {r.get('homepage')}\n")

print("Saved repo details to scratch/all_repos_info.txt")
