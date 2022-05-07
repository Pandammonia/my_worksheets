import json

def getstoredusername():
	"""Get stored name if available"""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def getnewusername():
	"""Prompt for new username"""
	username = input("What is your username?")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greetuser():
	"""Greet user by name"""
	username = getstoredusername()
	if username:
		check = input(f"Is {username} your username? Please enter 'y' or 'n'")
		if check == 'y':
			print(f"Welcome back {username}")
		else:
			username = getnewusername()
			print(f"We'll remember it from now on {username}")


greetuser()