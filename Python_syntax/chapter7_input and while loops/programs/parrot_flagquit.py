prompt ="Tell me something and i will repeat it back to you:"
prompt += "\nEnter 'quit' to stop the program."

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)