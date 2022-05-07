import json

def getfavnum():
	"""Tries to retrieve favourite number from favnum.json, if file isnt found returns FALSE"""
	filename = 'favnum.json'
	try:
		with open(filename) as f:
			num = json.load(f)
	except FileNotFoundError:
		return None  
	else:
		return num


def askforfavnum():
	"""Asks user for favourite number then stores it"""
	filename = 'favnum.json'
	favnu = input("Please enter your favourite number")
	with open(filename, 'w') as f:
		json.dump(favnu, f)
		print("We've stored your favourite number!")


def showfavnum():
	favnum = getfavnum() # 1. this line asks the function getfavnum() for the favourite number
	if favnum: # If a number is returned then this is ran
		print(f"Your favourite number is: {favnum}")
		input("Please enter")
	else:
		askforfavnum() # If FALSE is returned, this function is ran

showfavnum()