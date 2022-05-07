def format_name1(first_name, last_name, middle_name = ''): #middle name is optional here
	"""returns a full formatted name"""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = format_name1('jimi', 'hendrix')
musician1 = format_name1('jon', 'jovi', 'bon') # this is how a full name needs to be passed though to be formatted correctly
print(musician, musician1)

