print("Give me 2 numbers and ill divide them")
print("Enter q at any time to quit")
while True:
	no1 = input("First number?")
	if no1 == 'q':
		break
	no2 = input("Second number?")
	if no2 == 'q':
		break
	try:
		ans = int(no1) / int(no2)
	except ZeroDivisionError:
		print("You cant divide by zero!")
	else:
		print(ans)