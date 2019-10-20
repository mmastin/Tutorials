import requests

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'status code: {r.status_code}')

# store API response in a variable
response_dict = r.json()
print(f"total repos: {response_dict['total_count']}")

# explore info about the repos
repo_dicts = response_dict['items']
print(f'repos returned: {len(repo_dicts)}')

# examine the first repo
repo_dict = repo_dicts[0]
print(f'\nKeys: {len(repo_dict)}')
# for key in sorted(repo_dict.keys()):
#     print(key)

print('\nSelected info about the first repo:')
print(f"name: {repo_dict['name']}")
print(f"owner: {repo_dict['owner']['login']}")
print(f"stars: {repo_dict['stargazers_count']}")
print(f"repo: {repo_dict['html_url']}")
print(f"created: {repo_dict['created_at']}")
print(f"updated: {repo_dict['updated_at']}")
print(f"description: {repo_dict['description']}")