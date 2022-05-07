responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb one day?")

	responses[name] = response #stores the response in the empty dictionary

	repeat = input("Would you like another person to respond? (Yes/no)")
	if repeat == 'no':
		polling_active = False

#outside the loop we can now print the results

print("\n--- Poll Results ---")
for name,response in responses.items():
	print(f"{name} would like to climb {response}.")