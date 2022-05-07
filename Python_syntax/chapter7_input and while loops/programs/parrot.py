prompt ="Tell me something and i will repeat it back to you:"
prompt += "\nEnter 'quit' to stop the program."

message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(f"{message}")