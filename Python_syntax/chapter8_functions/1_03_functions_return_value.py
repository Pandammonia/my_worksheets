def format_name(first_name, last_name):
	"""return a formatted name from a first and last name"""
	full_name = f"{first_name} {last_name}" # take the input and make a new variable; full name from it
	return full_name.title() # titles the result and returns it to the call

musician = format_name('jimi', 'hendrix') # you need to assign a variable for the return call to be assigned to
print(musician)

## optional values

def format_name(first_name, middle_name, last_name): #middle name is required here so it wont wont without one
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

def format_name1(first_name, last_name, middle_name = ''): #middle name is optional here
	"""returns a full formatted name"""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}" #if a middle name is present this is ran
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = format_name1('jimi', 'hendrix')
musician1 = format_name1('jon', 'jovi', 'bon') # this is how a full name needs to be passed though to be formatted correctly
print(musician, musician1)