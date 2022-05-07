import json


def greetuser():
	"""Greet user by name"""
	filename = '\\username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		username = input("What is your username?")
		with open(filename, 'w') as f:
			jason.dump(username, f)
			print(f"Well remember you from now on {username}")
	else:
		print(f"Welcome back {username}")


greetuser()