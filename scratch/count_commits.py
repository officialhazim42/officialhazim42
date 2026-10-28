import subprocess, json

# 1. Total commits across repos
repos_cmd = subprocess.run(['gh', 'repo', 'list', 'officialhazim42', '--limit', '100', '--json', 'name,isPrivate'], capture_output=True, text=True)
repos = json.loads(repos_cmd.stdout)
public_repos = [r['name'] for r in repos if not r['isPrivate']]

commit_counts = {}
author_commits = {}

for r in public_repos:
    res = subprocess.run(['gh', 'api', f'repos/officialhazim42/{r}/commits?per_page=100'], capture_output=True, text=True)
    if res.returncode == 0:
        commits = json.loads(res.stdout)
        commit_counts[r] = len(commits)
        my_commits = 0
        for c in commits:
            author = c.get('author')
            if author and author.get('login') == 'officialhazim42':
                my_commits += 1
            elif not author:
                # check committer
                committer = c.get('commit', {}).get('author', {}).get('name')
                if 'hazim' in str(committer).lower():
                    my_commits += 1
        author_commits[r] = my_commits

total_repo_commits = sum(commit_counts.values())
total_author_commits = sum(author_commits.values())
print(f"Total commits across 13 public repos: {total_repo_commits}")
print(f"Total author commits across 13 public repos: {total_author_commits}")
for r in public_repos:
    print(f"  {r}: {author_commits[r]} author commits ({commit_counts[r]} total)")

# Also commit search query
search_res = subprocess.run(['gh', 'api', 'search/commits?q=author:officialhazim42'], capture_output=True, text=True)
search_data = json.loads(search_res.stdout)
print(f"\nGitHub Search API author:officialhazim42 total_count: {search_data.get('total_count')}")

