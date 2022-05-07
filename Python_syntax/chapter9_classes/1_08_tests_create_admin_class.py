class User():
		
	def __init__(self, first, last, city, age):
		self.first = first
		self.last = last
		self.city = city
		self.age = age
		self.loginattempts = 0

	def describe_user(self):
		print(f"{self.first} {self.last} is  {self.age} years old and from the city {self.city}")

	def greet_user(self):
		print(f"Hey {self.first}, how are you doing today!")

class Admin(User):
	def __init__(self, first, last, city, age):
		super().__init__(first, last, city, age)
		self.privilidges = ['can delete post', 'can edit post']

	def showpriv(self):
		print(f"{self.privilidges}")


luke = Admin('Luke', 'Peacock', 'Hartlepool', 32)
luke.showpriv()
