import requests
# Make API call and store response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
headers["Accept-Encoding"] = "gzip"
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Store API response in a variable
response_dict = r.json()
#Process results
print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")
#Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
#Examine repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
	print(key)
#In depth information of first respository
print("Selected information on first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Descriptioh: {repo_dict['description']}")
#Information on all returned depsitory
for repo_dict in repo_dicts:
	print(f"\nName: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	print(f"Descript {repo_dict['description']}")