luke = {'first name' : 'luke', 'second name' : 'peacock', 'age': 32, 'city': 'hartlepool'}
snickers = {'first name' : 'snic', 'second name' : 'kers', 'age': 3, 'city': 'hartlepool'}
clare = {'first name' : 'clare', 'second name' : 'cahill', 'age': 60, 'city': 'saltburn'}

people = [luke, snickers, clare]

for person in people:
	print(person)

snickers = {'animal kind': 'cat', 'owner':'luke',}
kaiser = {'animal kind': 'dog', 'owner':'luke',}

pets = [snickers, kaiser]

for pet in pets:
	print(pet)

fav_places = {
	'luke': ['pripyat', 'ukraine', 'chernobyl'],
	'snickers': ['home', 'bed', 'anywhere on luke']
}

for name, places in fav_places.items():
	print(f"Hey {name.title()}, your favourite places are:")
	for place in places:
		print(place.title())


fav_numbers = {
	'luke': ['12', '13', '14'],
	'snickers': ['1', '2', '3',]
}

for name, num in fav_numbers.items():
	print(f"Hey {name.title()}, your favourite numbers are:")
	for nums in num:
		print(nums.title())

	cities = {
		'monaco':{
		'country':'france', 'population':'150,000','fact':'full of richos'},
		'hartlepool':{
		'country':'uk', 'population':'5million','fact':'full of not richos'},
		'pripyat':{
		'country':'ukraine', 'population':'in trouble', 'fact':'soon to be speaking ruski'}
	}

	print(cities)

	for city, info in cities.items():
		print(f"{city.title()} is located in {info['country']}, it has a population of {info['population']}, and is: {info['fact']}.")




