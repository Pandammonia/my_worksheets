filename = 'C:/Users/lukep/Desktop/PY/Python crash course/chapter10/pi_million_digits.txt'
with open(filename) as openedfile:
	lines = openedfile.readlines()

pi_string = ""
for line in lines:
	pi_string += line.strip()
print(f"{pi_string[:52]} is pi to 50 digits.")	
print(len(pi_string))

birthday = input("What is your birthday in the format: ddmmyy; ")
if birthday in pi_string:
	print(f"Your birthday is in pi!")

else:
	print("Sorry your birthday isn't in pi")
