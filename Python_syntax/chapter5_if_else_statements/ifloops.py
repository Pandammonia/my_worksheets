cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())

topping = "mushrooms"
if topping != "anchovies": # != is NOT equal to
	print("no anchovies!")

age_0 = 21
age_1 = 23
(age_0 >= 19) and (age_1 >=19) # true
age_0 = 7
age_1 = 21
if age_0 >= 18 or age_1 >=18:
	print("One of you is old enough!")

requested_pizza_toppings =["mushrooms", "ham", "pineapple", "pepperoni"]
"mushrooms" in requested_pizza_toppings #true
"cookie" in requested_pizza_toppings #false

banned_users = "dave", "james", "larry"
user = "luke"

if user not in banned_users:
	print(f"You can post {user}")
else:
	print(f"Sorry {user} you are banned still")

# Conditional Tests: Write a series of conditional tests. Print a statement 
#describing each test and your prediction for the results of each test. Your code 
#should look something like this

allowed_visitors = ["luke", "clare", "snickers"]
visitor = "jamie"

print("I dont think you're going to be allowed in {visitor}")
if visitor in allowed_visitors:
	print(f"You are allowed in {visitor}")
else:
	print(f"Sorry {visitor}, but you arent allowed here.")