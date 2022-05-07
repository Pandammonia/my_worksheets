def get_formatted_name(first, last, middle = ''):
	"""Generate a formatted full name"""
	if middle:
		full = f"{first} {middle} {last}"
	else:
		full = f"{first} {last}"
	return full.title()

