luke = {'first name' : 'luke', 'second name' : 'peacock', 'age': 32, 'city': 'hartlepool'}
print(f"Your first name is: {luke['first name']}")
print(f"Your second name is {luke['second name']}")
print(f"Your age is {luke['age']}")
print(f"You live in {luke['city']}\n")

colours = {'Luke':'blue', 'snickers':'red', 'Clare':'green',}#
print(f"Clares favourite colour is: {colours['Clare']}")
print(f"Lukes favourite colour is: {colours['Luke']}\n")

python = {
	'print':'display text',
	'elif':'else if so and so is equal to',
	'for loop':'run through a for loop doing something',
}

for function, use in python.items():
	print(f"{function} is used to {use}")


