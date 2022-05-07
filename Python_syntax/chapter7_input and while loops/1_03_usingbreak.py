prompt ="Tell me a city that you have visited"
prompt += "\n(Enter 'quit' when you're done)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"Wow, i'd love to go to {city} myself!.")
