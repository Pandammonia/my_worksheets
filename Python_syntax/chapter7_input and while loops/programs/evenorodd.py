number = input("Tell me a number and ill tell you if its even or odd")
number = int(number)
if number % 2 == 0:
	print(f"{number} is even!")
else:
	print(f"{number} is odd!")