filename = 'programming.txt'

with open(filename, 'w') as file: #  w here means write and opens the file in write mode, (r) = read, (a) = append or (r+) read AND write
	file.write("I love programming,") #this will open or create this file and write the string to it
	file.write("Python is a language.") #this will be squished together with the line above it so use newline if writing \n