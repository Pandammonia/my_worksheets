user_0 = {
	'username': 'Pandammonia',
	'first name':'luke',
	'second name':'peacock',
	}

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}\n")

favourite_languages = {
	'jen': 'python',
	'sarah':'C',
	'edward':'ruby',
	'phil':'python',
	}

friends = ['jen', 'phil']
for name in favourite_languages.keys():
	print(name.title())
	if name in friends:
		language = favourite_languages[name].title()
		print(f"Hey {name.title()}, i see you like {language}")

favourite_languages = {
	'jen': 'python',
	'sarah':'C',
	'edward':'ruby',
	'phil':'python',
	}

if 'erin' not in favourite_languages.keys():
	print(f"\nErin, please take our poll!\n")

favourite_languages = {
	'jen': 'python',
	'sarah':'C',
	'edward':'ruby',
	'phil':'python',
	}

for name in sorted(favourite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll!")

favourite_languages = {
	'jen': 'python',
	'sarah':'C',
	'edward':'ruby',
	'phil':'python',
	}

print(f"The following languages have been mentioned:")
for language in favourite_languages.values():
	print(language.title())

#to repeat the repetition

favourite_languages = {
	'jen': 'python',
	'sarah':'C',
	'edward':'ruby',
	'phil':'python',
	}

print(f"The following languages have been mentioned:")
for language in set(favourite_languages.values()): #set creates a unique list
	print(language.title())

rivers ={
	'rhine':'germany',
	'amazon':'peru',
	'volga':'russia',
}

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}")

rivers ={
	'rhine':'germany',
	'amazon':'peru',
	'volga':'russia',
}

for river in rivers.keys():
	print(f"{river}")

for country in rivers.values():
	print(f"{country.title()}")