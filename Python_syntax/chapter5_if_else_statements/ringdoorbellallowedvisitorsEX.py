allowed_visitors = ["luke", "clare", "snickers"]
visitors_today = []
visitor = "simon" #this is the name a visitor has enter
if visitor.lower() in allowed_visitors: #check if the visitors name change to lowercase is in allowed visitors
	print(f"Hi {visitor} you are welcome in!") 
else:
	print(f"Sorry {visitor}, you aren't allowed here.") #simon isnt on the list so this is printed out
	print(f"Please leave.\n")
	visitors_today.append(visitor) #this saves the entered name a list of "visitors today" so it can be checked later


print(f"These people visited today: {visitors_today}") #this shows who has visited and wasnt allowed in




