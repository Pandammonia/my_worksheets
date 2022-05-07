import json

username = input("What is your chosen username?") # asssign input to variable

filename = 'username.json' #name file
with open (filename, 'w') as f: #with the file in write mode as F
	json.dump(username, f) # dump this info to file
	print(f"We'll remember your username for when you return {username}!")