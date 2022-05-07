#theme pard admission prices: under 4: $free, 18 or less: $25 under 65: $40 over 65: $20

age = 68

if age < 4: #if age is less than 4
	price = 0 #set price to 0
elif age < 18: #else if age is less than 18
	price = 25 # set price to 25
elif age < 65: #if age is UNDER 65 set price to FULL
	price = 40
else:
	price = 20 #only ages that make it here are over 65

print(f"Your price is ${price}")

#the above can be made a lot simpler by replace the last else statement with another elif

age = 68

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20

# if youre testing for specific final conditions and want to match a statement use elif statement instead of an else catchall