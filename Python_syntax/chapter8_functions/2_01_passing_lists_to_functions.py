def greet_users(names):
	"""Print a simple greeting to a user"""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)

usernames = ['luke', 'snickers', 'clare']

greet_users(usernames)

def print_models(unprinted_designs, completed_models):
	"""
	simulate printing each design until none are left.
	moves each design to completed models after being 
	printed 
	"""

	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""show all printed models"""
	print(f"\nFollowing models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['dodecahedron', 'spaceX', 'rubicks cube', 'spitfire']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#to pass a COPY of a list and not the original list itself use a slice

print_models(unprinted_designs[:], completed_models)
