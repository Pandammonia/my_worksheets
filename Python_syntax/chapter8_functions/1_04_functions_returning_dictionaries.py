def build_person(first_name, last_name):
	"""return a dictionary about a person"""
	person = {'first': first_name, 'last': last_name} #declare dictionary with the keys first and last
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age = None): #none is a placeholder when a variable is declared without a value none=false
	"""dictionary with optional age"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person 

musician = build_person('jimi', 'hendrix', age = 42)
print(musician)