class Restaurant:
	def __init__(self, name, foodtype):
		self.name = name
		self.foodtype = foodtype

	def describe_restaurant(self):
		print(f"The restaurant is called {self.name} and it serves {self.foodtype}.")

	def open_rest(self):
		print(f"The restaurant is now open!")

class Icecreamstand(Restaurant):
	def __init__(self, name, foodtype):
		super().__init__(name, foodtype)
		self.flavours = [] # this creates the list attribute and leaves it empty for now

	def addflavours(self, *icecreamflavour): #the asterisk allows it to be any amount of input
			self.flavours.append(icecreamflavour) #appends users input to my empty list 

	def showflavours(self):
		print(f"{self.flavours}")


icecreamstand1 = Icecreamstand('Lukes ices', 'Ice creams')
icecreamstand1.addflavours('Vanilla', 'Strawberry', 'Chocolate', 'mint')
icecreamstand1.showflavours()