current_users = ["Luke", "snickers", "clare", "ryan"]
new_users = ["gail", "danny", "john", "lewis", "luke", "CLARE"]
current_lower = []
for i in current_users:
	current_lower.append(i.lower()) #copies current users and lower cases all inside it
new_users_lower = []
for i in new_users:
	new_users_lower.append(i.lower()) # copies new users and lower cases everyone inside it

for new in new_users_lower:
	if new in current_lower:
		print(f"Sorry but {new} is taken!")
	else:
		print("That name is fine!")