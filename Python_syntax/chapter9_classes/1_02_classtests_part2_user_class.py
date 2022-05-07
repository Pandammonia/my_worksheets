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

	def increment_login_attempts(self,):
		self.loginattempts += 1

	def showloginattempts(self):
		print(f"Current login attempts: {self.loginattempts}")

	def resetloginattempts(self):
		if self.loginattempts >=1:
			self.loginattempts = 0
		else:
			print(f"You haven't tried to login yet.")

user1 = User('Luke', 'Peacock', 'Hartlepool', '32')

user1.describe_user()
user1.increment_login_attempts()
user1.showloginattempts()
user1.resetloginattempts()
user1.showloginattempts()
user1.resetloginattempts()
user1.resetloginattempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.showloginattempts()