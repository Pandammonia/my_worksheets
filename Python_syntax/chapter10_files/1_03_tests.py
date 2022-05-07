file = 'test.txt'
with open(file) as file:
	line = file.readlines()

print(line)
for linenew in line:
	linenew.replace('python', 'cat')
	print(linenew.replace('python', 'cat'))