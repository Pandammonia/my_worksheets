def greet_user(): #defines a function and tells python what kind of information it needs,
	"""Display a simple greeting"""
	print("Hello!")
greet_user()

def greet_user(username): #tells the function what to expect to process or what it needs (username)
	"""Display a simple greeting"""
	print(f"Hello!, {username.title()}") #tells the function what to do with the username (title it)

greet_user('jesse') 

# vWrite a function called display_message() that prints one sentence telling everyone what 
# you are learning about in this chapter. C

def display_message():
	"""tells useres whats being learned about"""
	print("I am learning about functions and calling functions")

display_message()

def favourite_book(title):
	print(f"i love the book {title.title()}")

favourite_book('catch 22')
