class Cat:
	def __init__ (self, age, breed):
		self.name = "cat"
		self.age = age
		self.breed = breed

	def cat_desc(self):
		print(f"{self.name} is {self.age} years old and a {self.breed}")
		return 

ages = ["2", "1", "5", "3", "4"]
breed = ["moggy", "alley cat", "siasmese", "scruffy cat", "cheshire cat"]

cats = []

for a, b in zip(ages, breed):
	catto = Cat(a,b)
	cats.append(catto)

for x in cats:
	x.cat_desc()
	
print(len(cats))

position = ["1", "2", "3"]
runners = ["snickers", "luke", "slowpoke"]
medals = ["gold", "silver", "bronze"]
result = zip(position, runners, medals)

print(set(result))