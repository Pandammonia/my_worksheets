import json

numbers =['2', '3', '5', '7', '11', '13'] #creates a list of empty numbers
filename = 'numbers.json' #gives a file to store to 'numbers.json'
with open (filename, 'w') as f: #open file as filename in WRITE mode as variavble f
	json.dump(numbers, f) #dump numbers into F numbers.json



filename = 'numbers.json'
with open(filename) as f:
	numbers = json.load(f)

print(numbers)
