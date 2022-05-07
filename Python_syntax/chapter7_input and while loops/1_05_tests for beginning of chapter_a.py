#movie tickets age 3 < free, 3 - 12 £10, over 12 - £15

prompt = "Ticket prices vary depending on age, enter your age and ill give you the price"

age = input(prompt)
age = int(age)

if age <= 3:
	print("Your ticket is free!")
elif age > 3 and age < 12:
	print("Your ticket is £10!")
else:
	print("Your ticket is £15!")
