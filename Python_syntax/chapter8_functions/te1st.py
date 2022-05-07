class Restaurant:
	def __init__(self, name, foodtype):
		self.name = name
		self.foodtype = foodtype

	def describe_restaurant(self):
		print(f"The restaurant is called {self.name} and it serves {self.foodtype}.")

	def open_rest(self):
		print(f"The restaurant is now open!")

class Icecreamstand(Restaurant):
	def __init__(self, name, foodtype, *flavours):
		super().__init__(name, foodtype)
		self.flavours = [] # this creates a list that can be defined by user

	def showflavours(self): #the asterisk allows it to be any amount of input
			print(f"{self.flavours}")


icecreamstand1 = Icecreamstand('Lukes ices', 'Ice creams', 'vanilla', 'strawberry', 'chocolate', 'mint')
icecreamstand1.showflavours()

