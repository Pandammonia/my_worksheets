message = input("Tell me something, and ill repeat it") #assigns the input to message
print(message) #prints it

name = input("Please enter your name")
print(f"Hey {name}!") #uses f string to display name

prompt = "If you tell me who you are we can personalize messages for you."
prompt += "\n What is your name? " # this will now be displayed over two lines and results in a cleaner print

name = input(prompt)
print(f"Hey {name}")

age = input("What is your age?") # asks users age
age = int(age) #changes the inputted STR into an INT so we can now do INT operations on it
age >= 18 # are you 18 or older?

