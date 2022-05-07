class Dog:
	"""a simple dog"""
	def __init__(self, name, age):
		"""initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""makes the doggo sit"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""makes the doggo roll over"""
		print(f"{self.name} rolled over!")

my_dog = Dog('Kaiser', 7)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name} he is {my_dog.age} years old!")
print(f"Your dog's name is {your_dog.name}. She is {your_dog.age} years old!")
my_dog.sit()
my_dog.roll_over()
your_dog.roll_over()