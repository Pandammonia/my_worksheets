def describe_pet(animal_type, pet_name):
	"""displays info about a pet"""
	print(f"\n I have a {animal_type}.")
	print(f"My {animal_type} is called {pet_name.title()} \n")

describe_pet('cat', 'snickers')
describe_pet('dog', 'kaisser')
describe_pet(animal_type = 'cat', pet_name = 'snickers')

def describe_dog(pet_name, animal_type = 'dog'): #this sets the default animal type to a dog meaning all thats needed is the name
	"""descibes a DOG"""
	print(f"My {pet_name} is a {animal_type}")

describe_dog('kaisser')
describe_dog(pet_name = 'snickers', animal_type = 'cat') #this overwrites the default values stored in the function (cat over dog)

# default values must be the last parameter in your function call (at the end of the brackets)

describe_dog('snickers', 'cat') #you can still overwrite by providing an argument as seen here

def make_shirt(shirt_size, shirt_writing):
	print(f"The shirt you have ordered is a size: {shirt_size}, written on the back is {shirt_writing.title()}")

make_shirt('small', 'middlesbrough FC')
make_shirt('medium', 'Hartlepool')
make_shirt('large', 'tranmere fc')

def make_shirt(shirt_size = 'large', shirt_writing = 'i love python'):
	print(f"Your shirt is a size: {shirt_size}, it has {shirt_writing} written on the back.")

make_shirt()
make_shirt('small')
make_shirt('large', 'i love something that isnt python')

def describe_city(city, country):
	print(f"{city.title()} is in {country}")

describe_city('rio', 'brazil')
describe_city('london', 'england')
describe_city('munich', 'germany')
describe_city('frankfurt', 'germany')