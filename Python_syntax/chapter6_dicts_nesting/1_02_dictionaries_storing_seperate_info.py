favourite_languages = {
	'jen': 'python',
	'sarah':'C',
	'edward':'ruby',
	'phil':'python',
	}
print(favourite_languages)

language = favourite_languages['sarah'].title()
print(f"Sarahs favourite language is: {language}")
favourite_languageget = favourite_languages.get('john', 'no language assigned.')
print(favourite_languageget)