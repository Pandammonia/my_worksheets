class Restaurant:
	def __init__(self, name, foodtype):
		self.name = name
		self.foodtype = foodtype

	def describe_restaurant(self):
		print(f"The restaurant is called {self.name} and it serves {self.foodtype}.")

	def open_rest(self):
		print(f"The restaurant is now open!")

rest = Restaurant('Golden Dragon', 'Chinese')
rest.describe_restaurant()
rest.open_rest()

rest1 = Restaurant('Pizza time', 'Pizzas')
rest2 = Restaurant("Toni's", 'Kebabs')

rest1.describe_restaurant()
rest2.describe_restaurant()
rest.describe_restaurant()