class Icecreamstand():
	def __init__(self, name, foodtype):
		self.name = name
		self.type = foodtype
		self.flavours = []

	def showiceinfo(self):
		print(f"{self.name} is a {self.type}")

	def addflav(self, *flavours):
		self.flavours.append(flavours)

	def showflav(self):
		print(f"{self.flavours}")

ics1 = Icecreamstand('Lukes ices', 'Ice cream stand')
ics1.showiceinfo()
ics1.addflav('Vanilla', 'Chocolate', 'Strawberry', 'Mint')
ics1.showflav()