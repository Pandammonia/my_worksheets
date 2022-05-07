filename = 'guest.txt'
with open(filename, 'w') as file:
	guest = input("Please enter your name")
	file.write(guest)
	print(f"Welcome to the hotel, {guest}")