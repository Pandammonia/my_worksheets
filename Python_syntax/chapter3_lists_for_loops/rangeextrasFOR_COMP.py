for value in range(0,5):
	print(value)

numbers = list(range(6))
print(numbers)

squares = []
for value in range (1,11):
	squares.append(value**2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))
print(max(digits))
print(sum(digits))

#use a for loop to print 1 through 20

twenty = []
for value in range(1,21):
	twenty.append(value)

print(twenty)

#1 - 100,000 then print each

_100k = []
for value in range(100):
	_100k.append(value)
print(sum(_100k))

just100 = []
for value in range(1,101):
	just100.append(value)

print(just100)
print(min(just100))
print(max(just100))
print(len(just100))

#4-6. Odd Numbers: Use the third argument of the range() function to make a 
#list of the odd numbers from 1 to 20. Use a for loop to print each number

oddnumbers = []
for value in range(1,103,2):
	oddnumbers.append(value)

print(oddnumbers)

threetothirty = []
for value in range(3,33,3):
	threetothirty.append(value)

print(threetothirty)

#List the first 10 cubes

cubes =[]
for value in range (1,11):
	cubes.append(value ** 3)

print(cubes)

cubes = [value ** 3 for value in range(1,11)] #list comprehension
print(cubes)