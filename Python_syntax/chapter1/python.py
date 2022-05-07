firstname = "luke"
secondname = "peacock"
fullname = f"{firstname} {secondname}" # f inserts a variables value into the string by formatting it
print(fullname) # so this becomes Luke Peacock
print(f"Hello, {fullname.title()}")
# this can be simplified by assigning the final message to a variable however

message = f"Hello {fullname.title()}"
print (message)

# text can be formatted using \n for a new line or \t for a tab space

print("\tHello")
print("Hello\nHiya\nHola")

#\n\t can be used together
print("\tHello\n\tLuke\n\tPeacock\n\tHow are you?")

python = "extra white space "
print(python) 
print(python.rstrip()) 
print(python)
python = python.rstrip() #to actually strip whitespace for good execute the command on the variable
print(python)
python = " extra left wspace"
python = python.lstrip()
python = " extra both side "
python = python.strip() # removes all