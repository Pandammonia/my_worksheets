def make_pizza(*toppings): #an asterisk makes this function accept any number of arguments its passed
	"""print a list of pizza toppings"""
	print(f"Making a pizza with the following toppings:")
	for topping in toppings:
		print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('cheese', 'ham', 'pepper')

# place your "however many" arguments last

def make_pizza(size, *toppings):
	print(f"Making a {size} pizza with the following toppings:")
	for topping in toppings:
		print(f"-{topping}")

make_pizza('12', 'ham','cheese', 'pepperoni')

### ARBITRARY

def build_profile(first, last, **user_info): #** tells the function to create a dictionary and put in the user provided info
	"""build a dictionary with everything a user provides"""
	user_info['first_name'] = first 
	user_info['last_name'] = last #dictionary is callded user_info, keys are first_name / last_name / user provided below
	return user_info

user_profile = build_profile('luke', 'peacock', location = 'hartlepool', age = '32', field = 'python')
print(user_profile)

## this dictionary contains the key/value types in the function and the users own keys/value, eg - ['age'] : 32
