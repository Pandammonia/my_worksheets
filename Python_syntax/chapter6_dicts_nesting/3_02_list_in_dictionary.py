#store informtion sbout a pizza being ordered

pizza = {
	'crust':'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']} crust pizza"
" with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)

favourite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
	print(f"\n{name.title()}'s favourite languages are:") #this line prints names favourite languages are:
	for language in languages:
		print(f"\t{language.title()}") # followed immediately by: favourite languages

#written together the print codes would print out 16 lines in bad fomat