import json

#if username is stored load in, otherwise prompt for a username and store it

filename = 'username.json'
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What is your username?")
	with open(filename) as f:
		json.dump(username, f)
		print(f"We'll remember it for next time {username}!")
else:
	print(f"Welcome back {username}!")