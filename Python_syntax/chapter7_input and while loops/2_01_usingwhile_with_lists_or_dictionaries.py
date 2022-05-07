unconfirmed_users = ['alice', 'brian', 'sarah']
confirmed_users =[]

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

print(f"The following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(f"{confirmed_user.title()}")

pets = ["dog", "cat", "dog", "rabbit", "fish", "dog"]
print(f"\n{pets}")
while 'dog' in pets: #if 'dog' is in pets then this is true
	pets.remove('dog') #it is true so python executes this and removes the string 'dog' and returns to the while beginning
print(pets)

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