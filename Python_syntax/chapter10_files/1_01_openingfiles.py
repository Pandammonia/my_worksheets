with open('pi.txt') as file_object: #opens the text file as file object
	for line in file_object: #for loop to work through each line
		print(line.rstrip()) #rstrip removes any whitespace

filename = 'pi.txt' #changes the files location to "filename" var so it can be switched easily
with open(filename) as file_object:
	lines = file_object.readlines() #this lets you take the files contents outside the WITH block by asasigning it to a variable

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))