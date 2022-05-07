ans_yes = ["Yes", "y"]
ans_no = ['No','n']

def check(word):
	ans_yes = ["Yes", "y"]
	if word in ans_yes:
		return True
	else:
		return False


print("Welcome to a super simple choose your own adventure game.....\n")
print("The sound of a cockeril stirs you from your slumber, its starting to get light outside")
inp = input("You hear a banging at the door, would you like to answer it?")
if check(inp):
	print("You walk to the door")
else:
	print("You ignore the door")
