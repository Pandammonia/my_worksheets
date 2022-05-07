current_number = 0
while current_number <10: #number is 0 so while loop runs
	current_number += 1 #adds 1 to 0
	if current_number % 2 == 0: #is 1 divisible by 2? if TRUE then continue tells python to ignore the rest of the loop
		continue
	print(current_number) # otherwise the number is printed

