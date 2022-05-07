requested_toppings = ["mushrooms", "green peppers", "extra cheese",]
for reqtop in requested_toppings:
	if reqtop == "green peppers":
		print("Sorry, we're out of green pepper.")
	else:
		print(f"Adding {reqtop}")
print("All done\n")



req_toppings =[]
if req_toppings:
	for req_tops2 in req_toppings:
		print(f"Adding {req_tops2}")
	print("\n Okay all done!")
else:
	print("You really want a plain pizza?\n")



available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese",]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}")
	else:
		print(f"Sorry we dont put {requested_topping} on pizza.")

print("Okay you're all done\n")


#make an admin login list with guests and a different greeting for each one

pc_users = ["admin", "luke", "snickers"]
login_attempt = "luke"
if pc_users:  #this chcecks if the lits is true(holds something) or is false(empty) this block runs on true
	if login_attempt == "admin":
		print(f"Hey admin, nice to see you")
	elif login_attempt == "snickers":
		print("Hmm, i dont think you should be using this snickers.")
	else:
		print("Hey user, how are you today?")

else:
	print("We need some users!")
current_users = ["Luke", "snickers", "clare", "ryan"]
new_users = ["gail", "danny", "john", "lewis", "luke"]
current_lower = []
for i in current_users:
	current_lower.append(i.lower())
print(f"{current_lower}\n")


for new_user in new_users:
	if new_user in current_users:
		print(f"Sorry, but {new_user} is taken already.")
	else:
		print("Okay, that username is fine.")
current_users = ["Luke", "snickers", "clare", "ryan"]
new_users = ["gail", "danny", "john", "lewis", "luke"]
current_lower = []
for i in current_users:
	current_lower.append(i.lower())
print(f"{current_lower}\n")


for new_user in new_users:
	if new_user in current_users:
		print(f"Sorry, but {new_user} is taken already.")
	else:
		print("Okay, that username is fine.")