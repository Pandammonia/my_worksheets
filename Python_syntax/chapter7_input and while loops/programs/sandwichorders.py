sandwich_orders = ["pastrami", "pastrami", "pastrami", "blt", "tuna and ham", "tuna and ham", "sweetcorn", "ham and cheese"]
finished_orders = []

while sandwich_orders:
	for sandwich in sandwich_orders:
		if sandwich == 'pastrami':
			print(f"Sorry but we dont have any {sandwich}")
			sandwich_orders.remove('pastrami')
		sandwich = sandwich_orders.pop()
		print(f"Hey i made your {sandwich}") # remove this line for just a list at the end
		finished_orders.append(sandwich)

print(f"Here is the list of finished sandwiches: {finished_orders}") #remove this for a 1 by 1 printout of what was made



