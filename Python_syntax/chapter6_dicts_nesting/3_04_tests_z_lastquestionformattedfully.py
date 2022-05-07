cities = {
	'monaco':{
	'country':'france', 'population':'150,000','fact':'full of richos'},
	'hartlepool':{
	'country':'uk', 'population':'5 million','fact':'full of not richos'},
	'pripyat':{
	'country':'ukraine', 'population':'in trouble', 'fact':'soon to be speaking ruski'}
}

print(cities)

for city, info in cities.items():
	print(f"{city.title()} is located in:")
	a = info['country']
	b = info['fact']
	print(f"{a.title()}, its population is {info['population']} and is {b.title()}")
