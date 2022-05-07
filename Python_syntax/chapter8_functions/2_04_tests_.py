def sandwich(*filling):
	for fill in filling:
		print(f"Adding {fill}")
	print(f"Your sandwich contains:")
	print(f"-{filling}\n")

sandwich('ham', 'lettuce', 'cheese', 'tomato')
sandwich('ham')
sandwich('cheese', 'tomato')

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info


user_profile = build_profile('luke', 'peacock', location = 'hartlepool', age = '32')
print(user_profile)

def car_maker(manufacturer, model_name, **car_info):
	car_info['manufacturer'] = manufacturer
	car_info['model name'] = model_name
	return car_info

car = car_maker('audi', 'a4', made_in = '1998', made_at = 'berlin')
print(car)