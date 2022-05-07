def GetName():
	name = input("Please tell me your name >")
	return name

def print_msg(user_name):
	print(f"Hello {user_name}, nice to see you!")

def Main():
	user_name = GetName()
	print_msg(user_name)

def create_acc():
	user = input("Please enter a username")
	password = input("Please enter a password")
	filename = 'login.txt'
	with open(filename, 'a') as file:
		file.write(user)
		file.write(",")
		file.write(password)
		file.write("\n")

def login():
    usercheck = input("Please enter your username > ")
    password = input("Please enter your password > ")
    filename = 'login.txt'
    check = {}
    with open(filename, 'r') as file:
    	for line in file:
    		(userName, password) = line.split(',')
    		check[userName] = password
    		if usercheck in check:
    			if check[usercheck] == password:
    				print("Correct username and password!")
    			else:
    				print("Wrong password")


Main()
checkuser = input("Do you have a username?")
if checkuser.lower() == 'yes':
	login()
else:
	create_acc()
