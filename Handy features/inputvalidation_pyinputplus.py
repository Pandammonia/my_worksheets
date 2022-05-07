while True:
	print("Enter your age:")
	age = input()
	try:
		age = int(age)
	except:
		print("Please use numeric digits.")
		continue
	if age <1:
		print("Please enter a positive number only")
		continue
	break

print(f"Your age is: {age}")
input()

------------------------------------------------------

import pyinputplus as pyip
while True:
	prompt = 'Want to know how to keep an idiot busy?\n'
	response = pyip.inputYesNo(prompt)
	if response == 'no':
		break
print("Okay, thanks!")

-------------------------------------------------------

import pyinputplus as pyip

def addsUpToTen(numbers):
	numbersList = list(numbers) #takes input and makes list from it
	for i, digit in enumerate(numbersList):
		numbersList[i] = int(digit)
	if sum(numbersList) !=10:
		raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
	return int(numbers) #return an int form of numbers

response = pyip.inputCustom(addsUpToTen)