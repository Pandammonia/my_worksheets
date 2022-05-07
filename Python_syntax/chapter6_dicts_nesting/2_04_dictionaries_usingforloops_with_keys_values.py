

favourite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

polled = ["jen", "sarah", "jeniffer", "lewis",]

for name in polled:
	if name in favourite_languages.keys():
		print(f"Hey {name}, thanks for taking part")
	else:
		print(f"Hey {name}, would you like to take our survey?")