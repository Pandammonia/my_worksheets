class Restaurant:
	def __init__(self, name, foodtype):
		self.name = name
		self.foodtype = foodtype
		self.numberserved = 0

	def describe_restaurant(self):
		print(f"The restaurant is called {self.name} and it serves {self.foodtype}.")

	def open_rest(self):
		print(f"The restaurant is now open!")

	def show_served(self,):
		print(f"The restaurant has served: {self.numberserved} people.")

	def peopleserved(self, customers):
		self.numberserved = customers

	def incremementpeopleserved(self, more):
		self.numberserved += more


rest = Restaurant('Golden dragon', 'chinese')
rest.show_served()
rest.peopleserved(15)
rest.show_served()
rest.incremementpeopleserved(10)
rest.show_served()