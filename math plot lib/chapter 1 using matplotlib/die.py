from random import randint

class Die:
	"""Single die class"""
	def __init__(self, num_sides=6):
		"""Assumes die is 6 sided"""
		self.num_sides = num_sides

	def roll(self):
		"""Return a value between 1 and no of sides"""
		return randint(1, self.num_sides)

