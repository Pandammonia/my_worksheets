prompt = "Please give me some pizza toppings and ill add them"
prompt += "\n(Enter 'done' when you're finished)"

topping = "" # sets topping to empty string so python can checl
while topping != 'done': #string isnt done so this is ran
	topping = input(prompt) #asks for input
	if topping == 'done': #checks if inout is "done"
		break #if it is "done" python exits the while loop here
	print(f"Adding {topping}") #if it isnt done, python adds the topping and retarts the loop

print("Your pizza is finished") #prints as last message