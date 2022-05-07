import json

filename = 'favnum.json'
num = input("What is your favourite number?")
with open(filename, 'w') as f:
	json.dump(num, f)

