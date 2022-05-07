import requests

#make an API call and store response.

url= 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#store API response in variable
response_dict = r.json()
#Process results.
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")

#open firt