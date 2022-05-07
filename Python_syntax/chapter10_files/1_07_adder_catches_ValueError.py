print("Give me two numbers and ill add them")
print("Enter 'q' to quit")

while True:
	a = input("Please enter your first number ")
	if a == 'q':
		break
	b = input("Please enter your second number ")
	if b == 'q':
		break
	try:
		ans = int(a) + int(b)
	except ValueError:
		print("Please enter two numbers ")
	else:
		print(f"{a} plus {b} is {ans}")
